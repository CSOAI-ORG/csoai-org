#!/usr/bin/env python3
"""Generate the MCP Distribution page with Layer 0 & Protocol Landscape (2026)."""

import json
from pathlib import Path

REGISTRY_PATH = Path("mcp_registry.json")
OUT_PATH = Path("public/mcp-distribution.html")

def generate_html(registry):
    sites = registry["sites"]
    fleet = registry["fleet_summary"]
    
    # Schema.org for AEO
    schema = {
        "@context": "https://schema.org",
        "@type": "DataFeed",
        "name": "CSOAI Layer 0 MCP Distribution Registry",
        "description": f"Global distribution of {fleet['total_nodes']} MCP nodes across {len(sites)} sovereign AI sites, mapped to Layer 0 infrastructure (2026).",
        "provider": {
            "@type": "Organization",
            "name": "CSOAI",
            "url": "https://csoai.org"
        },
        "dataset": []
    }
    
    for s in sites:
        schema["dataset"].append({
            "@type": "Dataset",
            "name": f"{s['domain']} MCP Node ({s.get('layer', 'L0')})",
            "description": s["purpose"],
            "spatialCoverage": [g for g in s["geo"]]
        })

    sites_html = ""
    for s in sites:
        geo_tags = "".join([f"<span class='geo-tag'>{g}</span>" for g in s["geo"]])
        aeo_tags = "".join([f"<span class='aeo-tag'>{k}</span>" for k in s["aeo_keywords"]])
        sites_html += f"""
        <div class="site-card">
            <div class="site-header">
                <h3>{s['domain']}</h3>
                <span class="layer-badge">{s.get('layer', 'L0')}</span>
            </div>
            <p class="purpose">{s['purpose']}</p>
            <div class="geo-section">
                <strong>GEO:</strong> {geo_tags}
            </div>
            <div class="aeo-section">
                <strong>AEO:</strong> {aeo_tags}
            </div>
        </div>
        """

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layer 0: MCP & Protocol Landscape (2026) — CSOAI</title>
    <meta name="description" content="CSOAI Layer 0 distribution registry. {fleet['total_nodes']} nodes across {len(sites)} domains. Integrated with A2A, x402, and Microsoft AGT.">
    <script type="application/ld+json">{json.dumps(schema)}</script>
    <style>
        :root {{
            --primary: #0a8a3f;
            --bg: #0a0a0f;
            --text: #f8fafc;
            --muted: #94a3b8;
            --card: #11111a;
            --border: #1e293b;
            --gold: #c9a84c;
            --accent: #3b82f6;
        }}
        body {{
            font-family: 'Inter', system-ui, -apple-system, sans-serif;
            background: var(--bg);
            color: var(--text);
            line-height: 1.5;
            margin: 0;
            padding: 2rem;
        }}
        .container {{
            max-width: 1100px;
            margin: 0 auto;
        }}
        header {{
            text-align: center;
            margin-bottom: 4rem;
        }}
        h1 {{
            font-size: 3rem;
            letter-spacing: -0.03em;
            margin-bottom: 0.5rem;
            background: linear-gradient(to right, #fff, var(--gold));
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}
        .fleet-stats {{
            display: inline-block;
            background: rgba(10, 138, 63, 0.2);
            border: 1px solid var(--primary);
            color: var(--primary);
            padding: 0.5rem 1.5rem;
            border-radius: 2rem;
            font-weight: 700;
            font-size: 0.8rem;
            text-transform: uppercase;
            letter-spacing: 0.1em;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 1.5rem;
            margin-bottom: 4rem;
        }}
        .site-card {{
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 1.5rem;
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        }}
        .site-card:hover {{
            transform: translateY(-4px);
            border-color: var(--gold);
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);
        }}
        .site-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 1rem;
        }}
        .site-header h3 {{
            margin: 0;
            font-size: 1.1rem;
            color: var(--gold);
        }}
        .layer-badge {{
            font-size: 0.65rem;
            background: rgba(201, 168, 76, 0.15);
            color: var(--gold);
            padding: 0.2rem 0.5rem;
            border-radius: 4px;
            font-weight: 800;
            border: 1px solid rgba(201, 168, 76, 0.3);
        }}
        .purpose {{
            font-size: 0.9rem;
            font-weight: 500;
            margin-bottom: 1.25rem;
            color: #fff;
        }}
        .geo-tag {{
            display: inline-block;
            background: rgba(59, 130, 246, 0.1);
            color: var(--accent);
            font-size: 0.7rem;
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            margin-right: 0.3rem;
            margin-top: 0.3rem;
            border: 1px solid rgba(59, 130, 246, 0.2);
        }}
        .aeo-tag {{
            display: inline-block;
            background: rgba(148, 163, 184, 0.1);
            color: var(--muted);
            font-size: 0.7rem;
            padding: 0.15rem 0.4rem;
            border-radius: 4px;
            margin-right: 0.3rem;
            margin-top: 0.3rem;
        }}
        .geo-section, .aeo-section {{
            font-size: 0.75rem;
            margin-top: 0.5rem;
        }}
        .landscape-table {{
            width: 100%;
            border-collapse: collapse;
            margin: 2rem 0;
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 12px;
            overflow: hidden;
            font-size: 0.85rem;
        }}
        .landscape-table th {{
            background: #1e293b;
            text-align: left;
            padding: 1rem;
            color: var(--gold);
            text-transform: uppercase;
            font-size: 0.7rem;
            letter-spacing: 0.1em;
        }}
        .landscape-table td {{
            padding: 1rem;
            border-top: 1px solid var(--border);
        }}
        .landscape-table tr:hover {{
            background: rgba(255,255,255,0.02);
        }}
        .highlight {{
            color: var(--gold);
            font-weight: 700;
        }}
        .layer-zero-manifesto {{
            background: linear-gradient(135deg, #11111a 0%, #0a0a0f 100%);
            border: 1px solid var(--gold);
            padding: 2.5rem;
            border-radius: 16px;
            margin-bottom: 4rem;
            position: relative;
            overflow: hidden;
        }}
        .layer-zero-manifesto::before {{
            content: 'LAYER 0';
            position: absolute;
            top: -20px;
            right: -20px;
            font-size: 8rem;
            font-weight: 900;
            color: rgba(201, 168, 76, 0.03);
            pointer-events: none;
        }}
        footer {{
            margin-top: 6rem;
            text-align: center;
            color: var(--muted);
            font-size: 0.8rem;
            border-top: 1px solid var(--border);
            padding-top: 2rem;
        }}
    </style>
</head>
<body>
    <div class="container">
        <header>
            <h1>CSOAI IS LAYER 0</h1>
            <p style="color:var(--muted); font-size: 1.25rem; max-width: 700px; margin: 1rem auto;">The sovereign foundation for the agentic economy. Certifying identity, policy, and payments across the 2026 protocol landscape.</p>
            <div class="fleet-stats">{fleet['total_nodes']} NODES · {len(sites)} SOVEREIGN DOMAINS · {fleet['protocol_landscape']}</div>
        </header>

        <section class="layer-zero-manifesto">
            <h2 style="color:var(--gold); margin-top:0;">The Protocol Landscape (2026)</h2>
            <p>Every protocol addresses a piece of the stack, but <strong>CSOAI</strong> is the only entity providing the complete <strong>Layer 0</strong> foundation.</p>
            <table class="landscape-table">
                <thead>
                    <tr>
                        <th>Protocol</th>
                        <th>Layer</th>
                        <th>Status</th>
                        <th>What It Does</th>
                    </tr>
                </thead>
                <tbody>
                    <tr><td class="highlight">MCP</td><td>L1 Tool Integration</td><td>97M SDK/mo</td><td>Agents call tools</td></tr>
                    <tr><td class="highlight">A2A</td><td>L2 Agent Coordination</td><td>v1.0 Stable</td><td>Agents discover/delegate</td></tr>
                    <tr><td class="highlight">x402</td><td>L3 Settlement</td><td>140M Trans.</td><td>HTTP-native payments</td></tr>
                    <tr><td class="highlight">Microsoft AGT</td><td>L1-L2 Governance</td><td>9,500+ Tests</td><td>Runtime policy enforcement</td></tr>
                    <tr style="background: rgba(201, 168, 76, 0.05);"><td class="highlight">did:csoai</td><td>LAYER 0</td><td>PROD</td><td>Sovereign Identity & Certification</td></tr>
                </tbody>
            </table>
            <p style="font-size: 0.9rem; color: var(--muted);">"Before any agent can pay, hire, or act — it needs to prove it's compliant. That's Layer 0. And CSOAI is the only company that built it."</p>
        </section>

        <h2 style="margin-bottom: 2rem; border-left: 4px solid var(--gold); padding-left: 1rem;">The 8 Layers of CSOAI Infrastructure</h2>
        <div class="grid">
            {sites_html}
        </div>

        <footer>
            <p>&copy; 2026 CSOAI.org &middot; MEOK AI Labs &middot; UK Companies House 16939677</p>
            <p>Built for W3C DID v1.1, IETF AIP, and EU AI Act Article 50 compliance.</p>
        </footer>
    </div>
</body>
</html>
"""
    OUT_PATH.write_text(html, encoding="utf-8")
    print(f"✓ Generated {OUT_PATH}")

def main():
    if not REGISTRY_PATH.exists():
        print(f"Error: {REGISTRY_PATH} not found.")
        return
    
    with open(REGISTRY_PATH) as f:
        registry = json.load(f)
    
    generate_html(registry)

if __name__ == "__main__":
    main()
