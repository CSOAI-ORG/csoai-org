"""
x402 Gateway Wrap — Payment middleware for the csoai-gateway-mcp.

Wraps every tool from csoai_gateway_mcp with per-call x402 USDC billing.
Free tools (lead gen) pass through transparently. Paid tools return an
x402 PaymentRequired challenge on first call; execute on verified payment.

Env:
    X402_ENABLED=1              # required to activate billing
    X402_PAY_TO=0x...           # Coinbase CDP receiving address (Base)
    X402_NETWORK=eip155:8453    # Base mainnet (default)
    X402_FACILITATOR_URL=...    # optional override
"""
from __future__ import annotations

import json
import logging
import os
import sys
from typing import Any

# Add parent gateway MCP to path so we can import its server module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "csoai_gateway_mcp"))

import requests
from mcp.server.fastmcp import FastMCP, Context
from mcp.server.fastmcp.exceptions import ToolError

# Re-use the x402 primitives from meok-compliance-gateway (same repo, copied inline
# so this wrap is self-contained and deployable without the full gateway tree).
# If meok_x402.py is available on PYTHONPATH, we prefer it; otherwise inline.
try:
    from meok_x402 import paywalled, build_challenge, PAYMENT_RESPONSE_META_KEY, PAYMENT_META_KEY
except ImportError:
    # Inline minimal x402 bridge (same logic, no external meok dependency)
    import contextvars
    import functools
    import math

    log = logging.getLogger("x402.gateway_wrap")
    _paid_call: contextvars.ContextVar[bool] = contextvars.ContextVar("x402_paid", default=False)
    PAYMENT_META_KEY = "x402/payment"
    PAYMENT_RESPONSE_META_KEY = "x402/payment-response"

    _USDC = {
        "eip155:8453": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
        "eip155:84532": "0x036CbD53842c5426634e7929541eC2318f3dCF7e",
    }
    _USDC_DECIMALS = 6

    def _enabled() -> bool:
        return os.environ.get("X402_ENABLED", "").strip().lower() in ("1", "true", "yes", "on")

    def _network() -> str:
        return os.environ.get("X402_NETWORK", "eip155:8453")

    def _asset(network: str) -> str:
        return os.environ.get("X402_ASSET") or _USDC.get(network, _USDC["eip155:8453"])

    def _price_to_atomic(price: str) -> str:
        dollars = float(str(price).strip().lstrip("$"))
        if not math.isfinite(dollars):
            raise ValueError(f"Invalid price: {price!r}")
        return str(int(round(dollars * (10 ** _USDC_DECIMALS))))

    def _accepts(price: str) -> list:
        from x402.schemas import PaymentRequirements
        network = _network()
        return [
            PaymentRequirements(
                scheme="exact",
                network=network,
                asset=_asset(network),
                amount=_price_to_atomic(price),
                pay_to=os.environ["X402_PAY_TO"],
                max_timeout_seconds=int(os.environ.get("X402_TIMEOUT", "300")),
            )
        ]

    def build_challenge(tool_name: str, price: str, error: str = "Payment required") -> dict:
        from x402 import ResourceInfo
        from x402.schemas import PaymentRequired
        challenge = PaymentRequired(
            x402_version=1,
            error=error,
            resource=ResourceInfo(url=f"mcp://tool/{tool_name}", service_name="csoai-gateway-mcp"),
            accepts=_accepts(price),
        )
        return challenge.model_dump(by_alias=True)

    _server = None

    def _resource_server():
        global _server
        if _server is None:
            from x402 import x402ResourceServerSync
            from x402.http import HTTPFacilitatorClientSync
            url = os.environ.get("X402_FACILITATOR_URL")
            facilitator = HTTPFacilitatorClientSync({"url": url}) if url else HTTPFacilitatorClientSync()
            _server = x402ResourceServerSync(facilitator)
        return _server

    def _extract_meta(ctx: Any) -> dict:
        for path in (
            lambda: ctx.request_context.request.params.meta,
            lambda: ctx.request_context.meta,
            lambda: ctx.request_context.request.params.model_extra.get("_meta"),
        ):
            try:
                meta = path()
                if meta:
                    return dict(meta)
            except Exception:
                continue
        return {}

    def _unpaid(tool_name: str, price: str, error: str = "Payment required"):
        envelope = {PAYMENT_RESPONSE_META_KEY: build_challenge(tool_name, price, error)}
        raise ToolError(json.dumps(envelope))

    def paywalled(price: str | None = None, *, tool_name: str | None = None):
        price = price or os.environ.get("X402_PRICE", "$0.10")

        def deco(fn):
            if not _enabled():
                return fn
            name = tool_name or fn.__name__

            @functools.wraps(fn)
            def wrapper(*args, **kwargs):
                ctx = kwargs.get("ctx")
                if ctx is None:
                    for v in list(kwargs.values()) + list(args):
                        if hasattr(v, "request_context"):
                            ctx = v
                            break
                payment = _extract_meta(ctx).get(PAYMENT_META_KEY) if ctx else None
                if not payment:
                    return _unpaid(name, price)
                try:
                    server = _resource_server()
                    reqs = server.find_matching_requirements(_accepts(price), payment)
                    verify = server.verify_payment(payment, reqs)
                    if not getattr(verify, "is_valid", False):
                        return _unpaid(name, price, getattr(verify, "invalid_reason", None) or "verification failed")
                    token = _paid_call.set(True)
                    try:
                        result = fn(*args, **kwargs)
                    finally:
                        _paid_call.reset(token)
                    try:
                        server.settle_payment(payment, reqs)
                    except Exception as exc:
                        log.warning("x402 settle failed for %s: %r", name, exc)
                    return result
                except Exception as exc:
                    if type(exc).__name__ == "ToolError":
                        raise
                    log.error("x402 path errored for %s, failing OPEN: %r", name, exc)
                    return fn(*args, **kwargs)

            return wrapper

        return deco


# ── Price map: tool_name → USDC price (or None for FREE lead-gen tools) ───────────────
_TOOL_PRICES: dict[str, str | None] = {
    "get_compliance_map": "$0.10",
    "get_crosswalk": "$0.05",
    "get_dome_status": None,          # FREE — lead generation
    "get_council_votes": "$0.05",
    "verify_sigil_certificate": "$0.02",
    "get_framework_gaps": "$0.15",
    "get_regulatory_countdowns": None,  # FREE
    "get_region_status": "$0.05",
    "get_agent_card": None,           # FREE — discovery
}

BASE_URL = "https://csoai.org/api"
WELL_KNOWN_URL = "https://csoai.org/.well-known"

mcp = FastMCP("x402-gateway-wrap")


def _fetch(endpoint: str, params: dict | None = None) -> dict:
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.get(url, params=params or {}, timeout=15)
    resp.raise_for_status()
    return resp.json()


# ── Tool implementations (mirrored from csoai_gateway_mcp, with x402 wrappers) ──────

@mcp.tool()
@paywalled("$0.10")
def get_compliance_map(region: str = "all") -> dict:
    """Retrieve the global compliance map from csoai.org. [$0.10]"""
    data = _fetch("map.json")
    if region != "all":
        data["regions"] = [r for r in data.get("regions", []) if r.get("id") == region]
        data["total_regions"] = len(data["regions"])
    return data


@mcp.tool()
@paywalled("$0.05")
def get_crosswalk(domain: str = "all") -> dict:
    """Retrieve the framework crosswalk matrix from csoai.org. [$0.05]"""
    data = _fetch("crosswalk.json")
    if domain != "all":
        data["crosswalk"] = [c for c in data.get("crosswalk", []) if c.get("domain") == domain]
        data["total_domains"] = len(data["crosswalk"])
    return data


@mcp.tool()
def get_dome_status() -> dict:
    """Retrieve the current DOME global status from csoai.org. [FREE]"""
    return _fetch("dome/status.json")


@mcp.tool()
@paywalled("$0.05")
def get_council_votes() -> dict:
    """Retrieve the BFT council voting state from csoai.org. [$0.05]"""
    return _fetch("council/votes.json")


@mcp.tool()
@paywalled("$0.02")
def verify_sigil_certificate(cert_id: str) -> dict:
    """Verify a SIGIL certificate against the csoai.org verification spec. [$0.02]"""
    return _fetch("sigil/verify.json", params={"cert_id": cert_id})


@mcp.tool()
@paywalled("$0.15")
def get_framework_gaps(framework: str) -> dict:
    """Retrieve compliance gaps for a specific framework from csoai.org. [$0.15]"""
    data = _fetch("crosswalk.json")
    gaps = []
    for entry in data.get("crosswalk", []):
        coverage = entry.get(framework)
        if coverage in (None, "", "gap", "missing", "not_covered"):
            gaps.append({"domain": entry.get("domain"), "coverage": coverage, "risk": entry.get("risk")})
    return {
        "framework": framework,
        "total_gaps": len(gaps),
        "gaps": gaps,
        "generated_at": data.get("generated_at"),
        "version": data.get("version"),
    }


@mcp.tool()
def get_regulatory_countdowns() -> dict:
    """Retrieve upcoming regulatory deadlines from csoai.org. [FREE]"""
    data = _fetch("map.json")
    countdowns = []
    for region in data.get("regions", []):
        dtd = region.get("days_to_deadline")
        if dtd is not None:
            countdowns.append({
                "region_id": region.get("id"),
                "region_name": region.get("name"),
                "days_to_deadline": dtd,
                "deadline_date": region.get("deadline_date"),
                "status": region.get("status"),
                "status_label": region.get("status_label"),
                "color": region.get("color"),
            })
    countdowns.sort(key=lambda x: x["days_to_deadline"])
    return {"countdowns": countdowns, "generated_at": data.get("generated_at"), "version": data.get("version")}


@mcp.tool()
@paywalled("$0.05")
def get_region_status(region_id: str) -> dict:
    """Retrieve detailed status for a single region from csoai.org. [$0.05]"""
    data = _fetch("map.json")
    for region in data.get("regions", []):
        if region.get("id") == region_id:
            return {
                "region": region,
                "global_stats": data.get("global_stats"),
                "generated_at": data.get("generated_at"),
                "version": data.get("version"),
            }
    return {
        "error": f"Region '{region_id}' not found",
        "available_regions": [r.get("id") for r in data.get("regions", [])],
    }


@mcp.tool()
def get_agent_card() -> dict:
    """Retrieve the csoai.org A2A Agent Card from the well-known endpoint. [FREE]"""
    resp = requests.get(f"{WELL_KNOWN_URL}/agent.json", timeout=15)
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    mcp.run()
