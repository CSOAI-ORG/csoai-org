# CSOAI Gateway MCP

A Python **FastMCP** meta-server that exposes all [csoai.org](https://csoai.org) public data as Model Context Protocol (MCP) tools.

## What It Does

This server proxies csoai.org's static JSON API endpoints and surfaces them as typed MCP tools, enabling any MCP-compatible client (Claude Desktop, Cursor, etc.) to query compliance maps, framework crosswalks, DOME status, council votes, and SIGIL verification data in real time.

## Tools Exposed

| Tool | Endpoint | Description |
|------|----------|-------------|
| `get_compliance_map` | `/api/map.json` | Global 6-region compliance map |
| `get_crosswalk` | `/api/crosswalk.json` | Framework crosswalk matrix |
| `get_dome_status` | `/api/dome/status.json` | DOME global status & stats |
| `get_council_votes` | `/api/council/votes.json` | BFT council voting state |
| `verify_sigil_certificate` | `/api/sigil/verify.json` | SIGIL certificate verification |
| `get_framework_gaps` | `/api/crosswalk.json` | Compliance gaps per framework |
| `get_regulatory_countdowns` | `/api/map.json` | Upcoming regulatory deadlines |
| `get_region_status` | `/api/map.json` | Single region details |
| `get_agent_card` | `/.well-known/agent.json` | A2A Agent Card |

## Quick Start

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the server

```bash
python server.py
```

The server will start on the default FastMCP transport (stdio for MCP clients, or SSE if configured).

### 3. Connect an MCP client

Add to your MCP client config (e.g. Claude Desktop `claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "csoai-gateway": {
      "command": "python",
      "args": ["/absolute/path/to/server.py"]
    }
  }
}
```

## Requirements

- Python 3.10+
- `mcp>=1.27.0`
- `requests>=2.31.0`

## Architecture

- **Base URL:** `https://csoai.org/api`
- **Well-Known:** `https://csoai.org/.well-known`
- All tools use `requests.get()` with a 15-second timeout.
- Filtering (`region`, `domain`, `framework`) is performed client-side after fetching the full dataset.

## License

MIT — CSOAI.org
