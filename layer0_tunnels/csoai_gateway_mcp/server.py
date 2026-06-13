"""
CSOAI Gateway MCP — Meta-server exposing csoai.org data as MCP tools.

A FastMCP server that proxies csoai.org's static JSON API endpoints,
providing AI agents with structured access to compliance maps, framework
crosswalks, DOME status, council votes, and SIGIL verification data.
"""

import requests
from mcp.server.fastmcp import FastMCP

BASE_URL = "https://csoai.org/api"
WELL_KNOWN_URL = "https://csoai.org/.well-known"

mcp = FastMCP("csoai-gateway-mcp")


def _fetch(endpoint: str, params: dict | None = None) -> dict:
    """Helper to GET a csoai.org JSON endpoint and return parsed JSON."""
    url = f"{BASE_URL}/{endpoint}"
    resp = requests.get(url, params=params or {}, timeout=15)
    resp.raise_for_status()
    return resp.json()


@mcp.tool()
def get_compliance_map(region: str = "all") -> dict:
    """
    Retrieve the global compliance map from csoai.org.

    Args:
        region: Region ID to filter by, or "all" for every region.

    Returns:
        Compliance map data including regions, frameworks, and global stats.
    """
    data = _fetch("map.json")
    if region != "all":
        data["regions"] = [
            r for r in data.get("regions", []) if r.get("id") == region
        ]
        data["total_regions"] = len(data["regions"])
    return data


@mcp.tool()
def get_crosswalk(domain: str = "all") -> dict:
    """
    Retrieve the framework crosswalk matrix from csoai.org.

    Args:
        domain: Domain slug to filter by, or "all" for every domain.

    Returns:
        Crosswalk matrix mapping domains to framework coverage.
    """
    data = _fetch("crosswalk.json")
    if domain != "all":
        data["crosswalk"] = [
            c for c in data.get("crosswalk", []) if c.get("domain") == domain
        ]
        data["total_domains"] = len(data["crosswalk"])
    return data


@mcp.tool()
def get_dome_status() -> dict:
    """
    Retrieve the current DOME global status from csoai.org.

    Returns:
        DOME status including layer, stats, region heat map,
        regulatory clocks, recent activity, and blockchain anchor state.
    """
    return _fetch("dome/status.json")


@mcp.tool()
def get_council_votes() -> dict:
    """
    Retrieve the BFT council voting state from csoai.org.

    Returns:
        Council composition, node status, recent votes, vote counts,
        and current PBFT consensus state.
    """
    return _fetch("council/votes.json")


@mcp.tool()
def verify_sigil_certificate(cert_id: str) -> dict:
    """
    Verify a SIGIL certificate against the csoai.org verification spec.

    Args:
        cert_id: The SIGIL certificate identifier to verify.

    Returns:
        Verification result for the given certificate ID.
    """
    return _fetch("sigil/verify.json", params={"cert_id": cert_id})


@mcp.tool()
def get_framework_gaps(framework: str) -> dict:
    """
    Retrieve compliance gaps for a specific framework from csoai.org.

    Args:
        framework: Framework ID (e.g. "eu_ai_act", "nist_ai_rmf", "iso_42001", "tc260").

    Returns:
        Domains where the specified framework has gaps or missing coverage.
    """
    data = _fetch("crosswalk.json")
    gaps = []
    for entry in data.get("crosswalk", []):
        coverage = entry.get(framework)
        if coverage in (None, "", "gap", "missing", "not_covered"):
            gaps.append({
                "domain": entry.get("domain"),
                "coverage": coverage,
                "risk": entry.get("risk"),
            })
    return {
        "framework": framework,
        "total_gaps": len(gaps),
        "gaps": gaps,
        "generated_at": data.get("generated_at"),
        "version": data.get("version"),
    }


@mcp.tool()
def get_regulatory_countdowns() -> dict:
    """
    Retrieve upcoming regulatory deadlines from csoai.org.

    Returns:
        Sorted list of regions with their days-to-deadline and deadline dates.
    """
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
    return {
        "countdowns": countdowns,
        "generated_at": data.get("generated_at"),
        "version": data.get("version"),
    }


@mcp.tool()
def get_region_status(region_id: str) -> dict:
    """
    Retrieve detailed status for a single region from csoai.org.

    Args:
        region_id: The region identifier (e.g. "eu", "us", "cn", "sg", "uk", "au").

    Returns:
        Single region details including frameworks, agents, compliance score,
        violations, and deadline information.
    """
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
    """
    Retrieve the csoai.org A2A Agent Card from the well-known endpoint.

    Returns:
        Agent Card JSON describing the csoai.org agent's capabilities,
        endpoints, and metadata.
    """
    resp = requests.get(
        f"{WELL_KNOWN_URL}/agent.json", timeout=15
    )
    resp.raise_for_status()
    return resp.json()


if __name__ == "__main__":
    mcp.run()
