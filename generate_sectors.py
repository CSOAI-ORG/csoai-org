#!/usr/bin/env python3
"""Generate 96 sector × regulation SEO pages for csoai.org."""

from pathlib import Path

SECTORS = [
    ("healthcare", "Healthcare", "Hospitals, clinics, medical devices, telemedicine, and pharma AI"),
    ("finance", "Finance & Banking", "Retail banking, investment, trading, and fintech AI"),
    ("insurance", "Insurance", "Underwriting, claims, risk assessment, and actuarial AI"),
    ("legal", "Legal & Law Firms", "Contract review, litigation support, and legal research AI"),
    ("education", "Education", "Universities, K-12, edtech, and personalised learning AI"),
    ("government", "Government & Public Sector", "Smart cities, public services, and defence AI"),
    ("manufacturing", "Manufacturing", "Industry 4.0, predictive maintenance, and robotics AI"),
    ("retail", "Retail & E-commerce", "Recommendation engines, inventory, and customer service AI"),
    ("energy", "Energy & Utilities", "Grid management, renewables, and oil & gas AI"),
    ("transportation", "Transportation & Logistics", "Autonomous vehicles, fleet, and supply chain AI"),
    ("media", "Media & Publishing", "Content generation, moderation, and distribution AI"),
    ("nonprofit", "Non-profit & NGO", "Humanitarian, advocacy, and social impact AI"),
]

REGULATIONS = [
    ("eu-ai-act", "EU AI Act", "The world's first comprehensive AI law. Risk-based classification with strict liability for high-risk systems.", ["Article 9 — Risk Management", "Article 10 — Data Governance", "Article 13 — Transparency", "Article 14 — Human Oversight", "Article 15 — Accuracy & Robustness"]),
    ("gdpr", "GDPR", "General Data Protection Regulation. Rights to access, rectification, erasure, and portability.", ["Article 15 — Right of Access", "Article 17 — Right to Erasure", "Article 20 — Data Portability", "Article 22 — Automated Decision-Making", "Article 35 — DPIA"]),
    ("dora", "DORA", "Digital Operational Resilience Act for financial sector. ICT risk management and incident reporting.", ["Article 6 — ICT Risk Management", "Article 19 — Incident Reporting", "Article 24 — Resilience Testing"]),
    ("nis2", "NIS2", "Network and Information Security Directive. Expands scope to important entities across all sectors.", ["Article 21 — Cybersecurity Risk Management", "Article 23 — Incident Reporting"]),
    ("cra", "CRA", "Cyber Resilience Act. Security requirements for products with digital elements.", ["Article 10 — Security Requirements", "Article 13 — Vulnerability Handling", "Article 14 — Security Updates"]),
    ("iso-42001", "ISO 42001", "AI Management Systems standard. Clause-based governance structure.", ["Clause 4 — Context", "Clause 5 — Leadership", "Clause 6 — Planning", "Clause 7 — Support", "Clause 8 — Operation", "Clause 9 — Performance Evaluation", "Clause 10 — Improvement"]),
    ("hipaa", "HIPAA", "US healthcare data protection. Privacy Rule, Security Rule, Breach Notification.", ["Privacy Rule — PHI Protection", "Security Rule — Safeguards", "Breach Notification Rule"]),
    ("uk-ai", "UK AI Regulation", "UK's pro-innovation approach to AI regulation. Sector-specific guidance.", ["Safety — Risk management", "Security — Cyber resilience", "Fairness — Non-discrimination", "Accountability — Governance", "Contestability — Redress"]),
]

SECTOR_REG_CONTENT = {
    ("healthcare", "eu-ai-act"): "Medical AI is classified as high-risk under the EU AI Act. This includes diagnostic systems, surgical robots, and patient triage algorithms. CSOAI's three-layer safety model provides the risk management system, data governance, and human oversight required by Articles 9-14.",
    ("healthcare", "gdpr"): "Healthcare AI processes sensitive health data (special category under GDPR Article 9). CSOAI's Memory Sovereignty (Article 9) and Selective Forgetting (Article 11) ensure patient data is never used for training without explicit consent.",
    ("healthcare", "hipaa"): "HIPAA requires administrative, physical, and technical safeguards for Protected Health Information. CSOAI's Privacy by Design (Article 25) and Guardian Archetype provide automated HIPAA compliance monitoring.",
    ("finance", "eu-ai-act"): "Credit scoring, fraud detection, and algorithmic trading are high-risk under the EU AI Act. CSOAI's PBFT Council deliberates on every high-stakes financial decision, providing the human oversight and explainability required by Article 14.",
    ("finance", "dora"): "DORA requires financial institutions to manage ICT third-party risk. CSOAI's threat detection NN and adversarial testing satisfy Article 6's risk management requirements.",
    ("finance", "gdpr"): "Financial AI processes vast quantities of personal data. CSOAI's audit trail and signed attestations provide the accountability and transparency required for GDPR compliance in automated lending and insurance.",
    ("insurance", "eu-ai-act"): "Insurance pricing and claims processing are high-risk AI applications. CSOAI's care_pattern_analyzer NN monitors for unfair discrimination in automated underwriting, ensuring compliance with Article 10's data governance requirements.",
    ("insurance", "gdpr"): "Insurance AI must balance automated decision-making with data subject rights. CSOAI's Partnership Charter gives policyholders audit rights over automated claims decisions.",
    ("legal", "eu-ai-act"): "Legal AI for judicial decision support is high-risk. CSOAI's Ethics Advisor and Constitutional Scholar specialists ensure every legal recommendation is checked against the 52-article charter.",
    ("legal", "gdpr"): "Legal AI processes client confidential information. CSOAI's Memory Sovereignty ensures client data is never shared with third parties or used for model training.",
    ("education", "eu-ai-act"): "AI for student assessment and admission is high-risk. CSOAI's partnership_detection_ml monitors for bias in automated grading, while the council provides human oversight for contested decisions.",
    ("education", "gdpr"): "Student data is highly sensitive. CSOAI's selective forgetting allows students to request deletion of their learning data, while memory portability enables transfer between institutions.",
    ("government", "eu-ai-act"): "Government AI for biometric identification and critical infrastructure is prohibited or high-risk. CSOAI's threat_detection_nn provides real-time safety monitoring for citizen-facing AI systems.",
    ("government", "uk-ai"): "The UK's sector-based approach requires adaptable compliance. CSOAI's framework crosswalks map UK guidance to the EU AI Act, NIST, and ISO 42001 simultaneously.",
    ("manufacturing", "eu-ai-act"): "AI for industrial safety systems is high-risk. CSOAI's Systems Architect specialist models failure modes, while the clone sandbox tests adversarial scenarios before deployment.",
    ("manufacturing", "iso-42001"): "Manufacturing AI requires management system certification. CSOAI's ISO 42001 crosswalk maps all 7 clauses to specific charter articles and MCP tools.",
    ("retail", "eu-ai-act"): "Biometric identification and emotion recognition in retail are high-risk. CSOAI's Privacy Guardian enforces data minimisation, while the Compliance Oracle interprets regulatory boundaries.",
    ("retail", "gdpr"): "Retail recommendation engines process behavioural data at scale. CSOAI's audit trail tracks every automated decision, enabling GDPR Article 22 contestation.",
    ("energy", "eu-ai-act"): "AI for critical infrastructure (power grids, pipelines) is high-risk. CSOAI's BFT council provides resilience against both cyber attacks and model failures.",
    ("energy", "nis2"): "Energy operators are designated as essential entities under NIS2. CSOAI's adversarial testing and incident reporting satisfy Articles 21 and 23.",
    ("transportation", "eu-ai-act"): "Autonomous vehicles and traffic management are high-risk. CSOAI's relationship_evolution_nn models system degradation over time, predicting failures before they occur.",
    ("transportation", "cra"): "Connected vehicles are products with digital elements under CRA. CSOAI's vulnerability tracking and signed security updates satisfy Articles 10, 13, and 14.",
    ("media", "eu-ai-act"): "Generative AI for media content requires transparency (Article 52). CSOAI's creativity_assessment_nn evaluates output for harm, while signed attestations prove compliance.",
    ("media", "gdpr"): "Media AI processes personal data for content personalisation. CSOAI's cultural awareness (47 traditions) ensures content respects diverse user backgrounds.",
    ("nonprofit", "eu-ai-act"): "Non-profits using AI for social services must comply with high-risk requirements. CSOAI's free tier ensures compliance is accessible regardless of budget.",
    ("nonprofit", "gdpr"): "Non-profits often handle vulnerable populations' data. CSOAI's Maternal Covenant Bond (Article 6) ensures care-based, non-extractive AI governance.",
}

# Default content for combinations not explicitly mapped
def default_content(sector, reg, sector_desc, reg_desc, reg_articles):
    return f"{sector} organisations using AI must comply with {reg}. {sector_desc}. {reg_desc}. CSOAI maps {reg} requirements to the 52-Article Partnership Charter, providing runtime enforcement, signed attestations, and public verify URLs."

TEMPLATE = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{sector} AI Compliance — {reg} | CSOAI</title>
<meta name="robots" content="index,follow">
<meta name="description" content="{meta_desc}">
<link rel="canonical" href="https://csoai.org/sectors/{slug}">
<style>
:root{{--ink:#0f172a;--muted:#5a5e66;--gold:#c9a84c;--card:#f7f8fa;--border:#e6e8ec;--brand:#0a8a3f}}
body{{font-family:system-ui,-apple-system,sans-serif;max-width:880px;margin:2.5rem auto;padding:0 1.5rem;color:var(--ink);line-height:1.65}}
h1{{margin:0 0 .5rem;font-size:2.3rem;letter-spacing:-.02em}}
h2{{margin-top:2.5rem;margin-bottom:.5rem;border-bottom:1px solid var(--border);padding-bottom:.4rem;font-size:1.4rem}}
a{{color:var(--brand);text-decoration:none}}
a:hover{{text-decoration:underline}}
.lead{{color:var(--muted);font-size:1.1rem;max-width:720px;margin-top:.75rem}}
.req-box{{background:var(--card);border:1px solid var(--border);border-radius:.55rem;padding:1.1rem 1.25rem;margin:1rem 0}}
.req-box h4{{margin:0 0 .5rem;font-size:1rem}}
.req-box p{{margin:0;font-size:.9rem;color:var(--muted)}}
.cta{{display:inline-block;background:var(--brand);color:white;padding:.85rem 1.5rem;border-radius:.5rem;font-weight:600;text-decoration:none;margin-top:.5rem}}
.foot{{margin-top:3rem;color:#888;font-size:.85rem;border-top:1px solid var(--border);padding-top:1.5rem}}
.breadcrumb{{font-size:.8rem;color:var(--muted);margin-bottom:1rem}}
.breadcrumb a{{color:var(--muted)}}
</style>
</head><body>

<p class="breadcrumb"><a href="/">CSOAI</a> · <a href="/frameworks">Frameworks</a> · <a href="/frameworks/{reg_slug}">{reg}</a> · {sector}</p>

<p style="text-transform:uppercase;letter-spacing:.12em;font-size:.78rem;color:var(--gold);margin-bottom:.5rem;font-weight:600">Sector Compliance</p>
<h1>{sector} AI Compliance: {reg}</h1>
<p class="lead">{lead}</p>

<h2>Key {reg} Requirements for {sector}</h2>
{requirements}

<h2>CSOAI Compliance Coverage</h2>
<div class="req-box">
<h4>52-Article Charter Mapping</h4>
<p>CSOAI's Partnership Charter maps {reg} requirements to enforceable articles. Every decision is checked against the charter by the PBFT council.</p>
</div>
<div class="req-box">
<h4>Signed Attestations</h4>
<p>Every compliance decision is cryptographically signed with the AI's internal state. Public verify URL at proofof.ai.</p>
</div>
<div class="req-box">
<h4>Neural Net Monitoring</h4>
<p>6 trained NNs continuously monitor: care validation, threat detection, partnership health, relationship evolution, care patterns, and creative output quality.</p>
</div>

<h2>Get Certified</h2>
<p>Run a CSOAI compliance audit for {sector} against {reg}. Free until 2 December 2027.</p>
<a href="/certify" class="cta">Start Free Certification →</a>

<p class="foot">© 2026 CSOAI LTD (UK 16939677) · <a href="/methodology">Methodology</a> · <a href="/asti">ASSTI Benchmark</a> · <a href="https://meok.ai">MEOK AI Labs</a></p>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{sector} AI Compliance: {reg}",
  "datePublished": "2026-05-28",
  "author": {{"@type": "Person", "name": "Nicholas Templeman"}},
  "publisher": {{"@type": "Organization", "name": "CSOAI LTD", "url": "https://csoai.org"}},
  "about": {{"@type": "Thing", "name": "{reg}"}},
  "mainEntityOfPage": "https://csoai.org/sectors/{slug}"
}}
</script>

</body></html>
'''

def generate():
    out = Path(__file__).parent / "sectors"
    out.mkdir(exist_ok=True)
    count = 0

    for sec_slug, sector, sec_desc in SECTORS:
        for reg_slug, reg, reg_desc, reg_articles in REGULATIONS:
            slug = f"{sec_slug}-{reg_slug}"
            content = SECTOR_REG_CONTENT.get((sec_slug, reg_slug), default_content(sector, reg, sec_desc, reg_desc, reg_articles))
            meta_desc = f"{sector} AI compliance with {reg}. {content[:120]}..."

            reqs_html = "\n".join(
                f'<div class="req-box"><h4>{art}</h4><p>CSOAI maps this to enforceable charter articles with runtime verification.</p></div>'
                for art in reg_articles[:5]
            )

            html = TEMPLATE.format(
                slug=slug,
                sector=sector,
                reg=reg,
                reg_slug=reg_slug,
                lead=content,
                meta_desc=meta_desc,
                requirements=reqs_html,
            )

            (out / f"{slug}.html").write_text(html, encoding="utf-8")
            count += 1

    print(f"Generated {count} sector pages in {out}")

if __name__ == "__main__":
    generate()
