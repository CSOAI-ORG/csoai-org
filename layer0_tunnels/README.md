# CSOAI Layer 0 Trust Infrastructure (2026)

## The Sovereign Foundation for AI Agents

While others build Layer 1-4 protocols (MCP, A2A, x402, ACP), **CSOAI provides the missing Layer 0 foundation**: Identity, Compliance, and Cross-Regional Policy Enforcement. 

This repository contains the Enterprise-Ready Python SDK and API Server required to tunnel external protocols into the CSOAI Trust Infrastructure.

## Designed for Enterprise Adoption

This SDK is built specifically for seamless integration by top enterprise platforms (Google A2A, Microsoft AGT, Stripe ACP, Coinbase x402). 

It features:
- **Pydantic Validation**: Strict type-checking and schema validation.
- **FastAPI Server**: High-performance, async-native REST API.
- **Docker-Ready**: Instant deployment to Kubernetes, AWS ECS, or Google Cloud Run.
- **Protocol Tunnels**: Direct adapters for W3C DID, IETF AIP, SPIFFE/WIMSE.

---

## The Growth Engine: Brand Authority & Distribution MCP
Layer 0 is only valuable if it achieves mass adoption. Included in this repository is the **CSOAI Brand Authority & Distribution MCP Toolkit** (`csoai_brand_authority_mcp.py`).

This 53,000+ character MCP server completely automates:
1. **100% Brand Consistency** across all 13 domains.
2. **AEO/GEO/SEO** for 6 platforms (ChatGPT, Perplexity, Google, Gemini, Claude, Copilot).
3. **Conversion Optimization** across 7 funnel stages.
4. **Distribution Automation** via a 6-week launch timeline.

### How to use with Kimi (or Claude/Cursor):
You and your AI assistants (like Kimi) can run this MCP server to generate marketing assets on the fly.

```bash
# Install the MCP SDK
pip install mcp

# Run the FastMCP server
fastmcp run csoai_brand_authority_mcp.py
```
*Note: Kimi can connect to this server via SSE or stdio to instantly generate localized campaign strategies, A/B test variants, and UTM tags.*

---

## Quickstart

### 1. Run Everything Instantly (Docker Compose)
The easiest way to run the entire stack—bypassing any local Python version conflicts—is via `docker-compose`. This spins up the Enterprise API on port 8000 and the FastMCP Growth Engine on port 8001.

```bash
cd layer0_tunnels
docker-compose up --build -d
```
- API Docs: `http://localhost:8000/docs`
- MCP Server (SSE): `http://localhost:8001/sse`

### 2. Run with Docker (API Only)
```bash
docker build -t csoai-layer0 .
docker run -p 8000:8000 csoai-layer0
```
Visit `http://localhost:8000/docs` to view the interactive OpenAPI documentation.

### 2. Run Locally
```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

## Integration Points

### For Payment Providers (Stripe ACP, Coinbase x402)
Use the `/v1/payment/pre-check` endpoint to verify agent compliance *before* authorizing fund transfers.

### For Coordination Protocols (Google A2A, Slim.tools)
Use the `/v1/policy/evaluate` endpoint to ensure agent-to-agent delegations do not violate cross-regional boundaries (EU AI Act, GDPR, TC260).

### For Governance Frameworks (Microsoft AGT)
Our SDK maps internal PDCA policies directly to Microsoft AGT YAML configurations natively.

## Security
All endpoints (except health) require an authorization token (mapped to SPIFFE/WIMSE in production).
