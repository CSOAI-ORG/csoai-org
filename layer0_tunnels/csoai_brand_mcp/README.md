# CSOAI Brand MCP Server

An MCP (Model Context Protocol) server for brand authority, AEO/GEO/SEO optimization, social post generation, and conversion optimization within the CSOAI ecosystem.

## Tools

| Tool | Description |
|------|-------------|
| `generate_seo_content` | SEO-optimized content for a topic + region |
| `generate_social_post` | Social media post for a platform + tone |
| `optimize_conversion` | Conversion-optimized copy for a page type |
| `generate_ad_variations` | Multiple ad headline variations |
| `analyze_brand_sentiment` | Brand sentiment analysis by source |
| `generate_geo_content` | Local SEO content for location + service |
| `create_content_calendar` | Multi-month content calendar |

## Install

```bash
pip install -r requirements.txt
```

## Run

```bash
python server.py
```

## Connect (Claude Desktop)

Add to `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "csoai-brand": {
      "command": "python",
      "args": ["/Users/nicholas/clawd/csoai-org/layer0_tunnels/csoai_brand_mcp/server.py"]
    }
  }
}
```

## License

MIT — CSOAI LTD
