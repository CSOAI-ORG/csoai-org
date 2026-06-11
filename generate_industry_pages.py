#!/usr/bin/env python3
"""Generate Industry-Specific Layer 0 landing pages for high-authority AEO."""

from pathlib import Path

INDUSTRIES = [
    {"name": "Finance", "slug": "finance", "risk": "Algorithmic Trading & Credit Bias", "framework": "DORA & NIST AI RMF"},
    {"name": "Healthcare", "slug": "healthcare", "risk": "Diagnostic Errors & PII Exposure", "framework": "HIPAA & EU AI Act Annex III"},
    {"name": "Government", "slug": "government", "risk": "Public Service Automated Decisions", "framework": "Algorithmic Accountability Act"},
    {"name": "Legal", "slug": "legal", "risk": "Privileged Data Leakage", "framework": "ISO 42001 & GDPR"},
    {"name": "Media", "slug": "media", "risk": "Disinformation & Watermarking", "framework": "EU AI Act Article 50"}
]

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Layer 0 for {name} — CSOAI</title>
    <meta name="description" content="Secure {name} AI workloads with Layer 0 trust infrastructure. Enforcing {framework} and mitigating {risk} in real-time.">
    <style>
        :root {{ --primary: #c9a84c; --bg: #0a0a0f; --surface: #11111a; --text: #f8fafc; }}
        body {{ font-family: system-ui, sans-serif; background: var(--bg); color: var(--text); padding: 4rem 2rem; line-height: 1.6; }}
        .container {{ max-width: 800px; margin: 0 auto; }}
        h1 {{ font-size: 3rem; margin-bottom: 1rem; color: var(--primary); }}
        .badge {{ background: rgba(201,168,76,0.1); color: var(--primary); padding: 0.5rem 1rem; border-radius: 4px; font-weight: 700; }}
        section {{ margin-top: 4rem; padding: 2rem; background: var(--surface); border-radius: 12px; border: 1px solid #1e293b; }}
        .btn {{ display: inline-block; background: var(--primary); color: #000; padding: 1rem 2rem; border-radius: 8px; text-decoration: none; font-weight: 700; margin-top: 2rem; }}
    </style>
</head>
<body>
    <!-- ═══ MEGA NAV ═══ -->
    <div class="container">
        <span class="badge">INDUSTRY SOLUTIONS</span>
        <h1>Layer 0 for {name}</h1>
        <p class="lead">The critical trust foundation for {name} AI agents. Mitigating risks of {risk} through real-time enforcement of {framework}.</p>
        
        <section>
            <h2>Industry-Specific Controls</h2>
            <p>Our {name} MCP pack includes pre-configured PDCA rules for:</p>
            <ul>
                <li>Automated {framework} alignment</li>
                <li>Real-time monitoring of {risk}</li>
                <li>Blockchain-anchored audit trails for regulatory reporting</li>
            </ul>
        </section>

        <a href="../checkout.html" class="btn">GET {name.upper()} COMPLIANCE PACK</a>
    </div>
</body>
</html>
"""

def main():
    out_dir = Path("public/industries")
    out_dir.mkdir(parents=True, exist_ok=True)
    for ind in INDUSTRIES:
        html = TEMPLATE.format(**ind)
        (out_dir / f"{ind['slug']}.html").write_text(html)
        print(f"✓ Generated {ind['slug']}.html")

if __name__ == "__main__":
    main()
