# Agentic.Market Listing Configuration

This document describes how to list the CSOAI compliance MCPs on [Coinbase Agentic.Market](https://agentic.market) — the marketplace for agent-discoverable, monetized tools.

---

## Overview

Agentic.Market is Coinbase's directory of x402-enabled MCP servers. When your endpoint receives its first verified USDC payment, it becomes eligible for auto-listing. This turns your compliance tools into discoverable, revenue-generating infrastructure for AI agents.

---

## Required Metadata

Create `agentic-market.json` in your repo root:

```json
{
  "name": "CSOAI Compliance Gateway",
  "description": "Per-call compliance intelligence for EU AI Act, DORA, NIS2, and CRA. Pay-as-you-go USDC billing via x402.",
  "version": "1.0.0",
  "author": "CSOAI LTD",
  "license": "MIT",
  "category": "Compliance & Regulatory",
  "tags": ["compliance", "eu-ai-act", "dora", "nis2", "cra", "regulatory", "mcp", "x402"],
  "endpoint": {
    "url": "https://x402-gateway-csoai.org/mcp",
    "protocol": "mcp-streamable-http",
    "auth": "x402-usdc"
  },
  "pricing": {
    "model": "per-call",
    "currency": "USDC",
    "network": "Base",
    "tools": {
      "get_compliance_map": { "price": "0.10", "unit": "USD" },
      "get_crosswalk": { "price": "0.05", "unit": "USD" },
      "get_dome_status": { "price": "0.00", "unit": "USD", "note": "FREE — lead gen" },
      "get_council_votes": { "price": "0.05", "unit": "USD" },
      "verify_sigil_certificate": { "price": "0.02", "unit": "USD" },
      "get_framework_gaps": { "price": "0.15", "unit": "USD" },
      "get_regulatory_countdowns": { "price": "0.00", "unit": "USD", "note": "FREE" },
      "get_region_status": { "price": "0.05", "unit": "USD" },
      "get_agent_card": { "price": "0.00", "unit": "USD", "note": "FREE — discovery" }
    }
  },
  "agent_card": {
    "url": "https://csoai.org/.well-known/agent.json",
    "a2a_version": "0.1"
  },
  "support": {
    "email": "agents@csoai.org",
    "docs": "https://csoai.org/docs/mcp",
    "status": "https://csoai.org/api/dome/status.json"
  }
}
```

---

## Pricing Strategy

### Tiered Freemium

| Tier | Tools | Price | Purpose |
|------|-------|-------|---------|
| **Free** | `get_dome_status`, `get_regulatory_countdowns`, `get_agent_card` | $0.00 | Lead generation, discovery, agent onboarding |
| **Standard** | `get_crosswalk`, `get_council_votes`, `get_region_status` | $0.05 | Core compliance lookups |
| **Premium** | `get_compliance_map`, `verify_sigil_certificate` | $0.10 / $0.02 | High-value data & verification |
| **Enterprise** | `get_framework_gaps` | $0.15 | Deep analysis, gap identification |

### Rationale

- **Free tier** maximizes surface area — any agent can discover and test
- **$0.05 standard** is below the cognitive cost of manual lookup (agents pay willingly)
- **$0.15 enterprise** reflects the analytical value of gap reports (can save $100K+ in non-compliance fines)
- All prices are **per-call**, no subscriptions — aligns with agentic "pay for what you use" ethos

---

## Auto-Listing After First Payment

Agentic.Market auto-discovers x402 endpoints. To ensure listing:

1. **First payment must settle** on mainnet (`eip155:8453`)
2. **Endpoint must be public** (no auth beyond x402)
3. **Agent Card must be valid** at `/.well-known/agent.json`

### Verification Checklist

```bash
# 1. Test free tool (should work without payment)
curl -X POST https://your-gateway.run.app/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_dome_status","arguments":{}}}'

# 2. Test paid tool without payment (should return x402 challenge)
curl -X POST https://your-gateway.run.app/mcp \
  -H "Content-Type: application/json" \
  -d '{"jsonrpc":"2.0","id":1,"method":"tools/call","params":{"name":"get_compliance_map","arguments":{"region":"eu"}}}'

# 3. Verify Agent Card
curl https://csoai.org/.well-known/agent.json | jq .

# 4. Check x402 Bazaar indexing (after first mainnet payment)
curl https://x402.org/bazaar/endpoint?url=https://your-gateway.run.app/mcp
```

---

## Manual Listing (if auto-list fails)

Submit via Agentic.Market API:

```bash
curl -X POST https://agentic.market/api/v1/listings \
  -H "Authorization: Bearer $AGENTIC_MARKET_API_KEY" \
  -H "Content-Type: application/json" \
  -d @agentic-market.json
```

Or via the web UI:
1. Go to [https://agentic.market/submit](https://agentic.market/submit)
2. Paste your MCP endpoint URL
3. Upload `agentic-market.json`
4. Verify ownership (sign a message with your CDP wallet)

---

## Post-Listing: Revenue Optimization

### Dynamic Pricing

After 100+ paid calls, adjust prices based on demand:

```python
# Example: surge pricing for high-demand tools
if daily_calls > 1000:
    price_multiplier = 1.25  # 25% surge
```

### Bundle Discounts

Offer discounted bundles for high-volume agents:

```json
{
  "bundles": {
    "compliance-suite": {
      "tools": ["get_compliance_map", "get_crosswalk", "get_region_status"],
      "price": "0.15",
      "savings": "0.05"
    }
  }
}
```

### Analytics

Track revenue per tool:

```bash
# Cloud Run logs → BigQuery → Looker Studio
gcloud logging read "resource.type=cloud_run_revision AND jsonPayload.tool_name=*" \
  --format json | jq '.[] | {tool: .jsonPayload.tool_name, revenue: .jsonPayload.x402_amount}'
```

---

## Legal & Compliance

- **KYC**: Not required for pure software listings on Agentic.Market
- **Tax**: USDC revenue is taxable income — consult your accountant
- **Terms**: Ensure your terms of service cover automated agent usage
- **GDPR**: Compliance data itself is public; no PPAI (personal data) in MCP responses

---

**CSOAI LTD (UK CH 16939677) · MIT**
