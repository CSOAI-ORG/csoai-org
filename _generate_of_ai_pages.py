#!/usr/bin/env python3
"""
Generate 6 conversion-optimized of.ai landing pages from a single template.

Each page targets one EU AI Act / governance vertical with:
- Outcome-framed headline (fine € vs ROI)
- "Free Tier 1 until 2 Dec 2027" urgency badge
- ROI grid + trust bar
- 3-tier pricing (Free / Pro / Enterprise)
- Schema.org Product + Offer JSON-LD

Output: csoai-org/public/{slug}.html  (one per domain)
"""

from pathlib import Path
import json

OUT = Path(__file__).parent / "public"

PAGES = [
    {
        "slug": "accountability",
        "hostname": "accountabilityof.ai",
        "title_seo": "Free AI accountability scorecard — verifiable evidence for every AI decision",
        "tag_label": "Accountability",
        "urgency": "FREE Tier 1 until 2 Dec 2027 · then £79+/mo",
        "headline_main": "Auditor: \"Prove your AI made this decision.\"",
        "headline_accent": "You: 9-second signed receipt.",
        "lede": "EU AI Act Article 14 + Article 26 require human-oversight evidence for every high-risk decision. CSOAI signs every decision with HMAC + ed25519 — auditors verify in 30 seconds via a public URL. 4,180× ROI vs the €15M fine ceiling.",
        "roi": [
            ("Max fine", "€15,000,000", "warn"),
            ("MEOK Pro / yr", "£948", "brand"),
            ("Effective ROI", "15,823×", "brand"),
            ("Setup time", "3 min", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/eVq9AV4O87sudMF42k8k839",
        "pro_price": "£79/mo",
        "ent_price": "£1,499/mo",
        "regs": "EU AI Act Article 14 (human oversight) · Article 26 (deployer obligations) · ISO 42001 Clause 9 · NIST AI RMF (MANAGE-2.3) · CSOAI Charter Article 11, 26, 39",
        "sample_output_lines": [
            ('"decision_id"', '"dec_b39c2f8a"'),
            ('"agent"', '"underwriting-v3.1"'),
            ('"input_hash"', '"sha256:9d2f…"'),
            ('"output"', '"approve credit £25k"'),
            ('"human_reviewer"', '"jess@bank.co.uk"'),
            ('"reviewed_at"', '"2026-05-29T14:32:11Z"'),
            ('"hmac_signature"', '"sha256:7f3a9b…"'),
            ('"verify_url"', '"https://proofof.ai/verify/dec_b39c2f8a"'),
        ],
        "install_cmd": "pip install meok-accountability-mcp",
        "tier_pro_features": [
            "Continuous signed-decision logging",
            "Public verify URL at proofof.ai",
            "Auditor read-only dashboard",
            "Email + Slack incident alerts",
        ],
    },
    {
        "slug": "data-privacy",
        "hostname": "dataprivacyof.ai",
        "title_seo": "Free DPIA scorecard — EDPB-template-mandated · €20M GDPR Article 22 exposure",
        "tag_label": "Data Privacy",
        "urgency": "FREE Tier 1 until 2 Dec 2027 · then £499/mo",
        "headline_main": "EDPB now mandates the DPIA template.",
        "headline_accent": "Generate yours in 4 minutes. Save 40 hours of manual work.",
        "lede": "GDPR Article 22 + EU AI Act Article 27 require Data Protection Impact Assessments for any high-risk automated decision-making. The EDPB harmonised template (14 Apr 2026) is now expected. CSOAI auto-generates the full DPIA from your data flow + signs the result. ICO + national DPAs verify in 30 seconds.",
        "roi": [
            ("GDPR max fine", "€20,000,000", "warn"),
            ("MEOK Pro / yr", "£5,988", "brand"),
            ("Effective ROI", "3,340×", "brand"),
            ("Setup time", "4 min", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/eVq00lcgAbIK5g9dCU8k83f",
        "pro_price": "£499/mo",
        "ent_price": "£1,999/mo",
        "regs": "GDPR Article 22 + Article 35 (DPIA) · EU AI Act Article 27 (FRIA) · EDPB harmonised template 14 Apr 2026 · ISO/IEC 42005 · ISO/IEC 27701 · CSOAI Charter Article 14, 22",
        "sample_output_lines": [
            ('"dpia_id"', '"dpia_a72b9d3c"'),
            ('"controller"', '"Your Co Ltd · UK 16939677"'),
            ('"processing_purpose"', '"automated credit scoring"'),
            ('"data_categories"', '["financial", "demographic"]'),
            ('"art_22_relevance"', '"high"'),
            ('"residual_risk"', '"low (after mitigations)"'),
            ('"hmac_signature"', '"sha256:c5e1f8…"'),
            ('"verify_url"', '"https://proofof.ai/verify/dpia_a72b9d3c"'),
        ],
        "install_cmd": "pip install meok-dpia-edpb-template-mcp",
        "tier_pro_features": [
            "Auto-generate full DPIA from data flow",
            "EDPB harmonised template baked in",
            "Continuous re-assessment on schema changes",
            "Public verify URL for ICO inspection",
        ],
    },
    {
        "slug": "transparency",
        "hostname": "transparencyof.ai",
        "title_seo": "Free Article 50 watermark check — Don't ship un-watermarked AI imagery by 2 Aug 2026",
        "tag_label": "Transparency",
        "urgency": "FREE Tier 1 until 2 Dec 2027 · then £79+/mo",
        "headline_main": "Watermark every AI image you ship by 2 Aug 2026",
        "headline_accent": "or face €15M Article 50 fines.",
        "lede": "EU AI Act Article 50 makes machine-readable + human-perceptible watermarks mandatory for GenAI output. CSOAI ships C2PA 2.2 + EU AIGC icon as a one-liner. Auditor verifies provenance + watermark intactness in 8 seconds via proofof.ai.",
        "roi": [
            ("Max fine", "€15,000,000", "warn"),
            ("MEOK Pro / yr", "£948", "brand"),
            ("Effective ROI", "15,823×", "brand"),
            ("Setup time", "1 min", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/eVq9AV4O87sudMF42k8k839",
        "pro_price": "£79/mo",
        "ent_price": "£1,499/mo",
        "regs": "EU AI Act Article 50 (transparency) · C2PA 2.2 · EU AIGC icon · ISO/IEC 22989 · CSOAI Charter Article 17, 18",
        "sample_output_lines": [
            ('"asset_id"', '"img_94c3f8e2"'),
            ('"watermark"', '"C2PA 2.2 durable"'),
            ('"creator"', '"AI: Stable Diffusion XL"'),
            ('"prompt_hash"', '"sha256:4f8d…"'),
            ('"icon_embedded"', 'true'),
            ('"perceptibility_score"', '0.94'),
            ('"hmac_signature"', '"sha256:b9e2f1…"'),
            ('"verify_url"', '"https://proofof.ai/verify/img_94c3f8e2"'),
        ],
        "install_cmd": "pip install meok-watermark-attest-mcp",
        "tier_pro_features": [
            "C2PA 2.2 durable watermark on every AI output",
            "EU AIGC icon overlay",
            "Hand-off provenance chain (model → asset)",
            "1-line integration with Stable Diffusion / DALL-E / Midjourney workflows",
        ],
    },
    {
        "slug": "ethical-governance",
        "hostname": "ethicalgovernanceof.ai",
        "title_seo": "Free ISO 42001 readiness scorecard — Get certified in 11 weeks · UKAS-recognised",
        "tag_label": "Ethical Governance",
        "urgency": "FREE Tier 1 until 2 Dec 2027 · then £79+/mo",
        "headline_main": "ISO 42001 in 11 weeks.",
        "headline_accent": "UKAS-recognised. EU procurement-ready.",
        "lede": "ISO/IEC 42001:2023 is the AI management system standard EU public procurement now demands. UKAS-accredited certification bodies began audits Q1 2026. CSOAI ships the complete Annex A control set + auto-evidence pack + auditor portal. 11-week path from zero to certified.",
        "roi": [
            ("Lost EU tender", "€2,000,000", "warn"),
            ("MEOK Pro / yr", "£948", "brand"),
            ("Effective ROI", "2,109×", "brand"),
            ("Setup time", "11 wks to cert", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/eVq9AV4O87sudMF42k8k839",
        "pro_price": "£79/mo",
        "ent_price": "£1,499/mo",
        "regs": "ISO/IEC 42001:2023 · ISO/IEC 42005:2025 · NIST AI RMF 1.0 · OECD AI Principles · Council of Europe AI Convention · CSOAI Charter Article 11, 12, 21",
        "sample_output_lines": [
            ('"isms_id"', '"isms_b29c8a4f"'),
            ('"clause_4_context"', '"PASS"'),
            ('"clause_5_leadership"', '"PASS"'),
            ('"clause_6_planning"', '"PASS"'),
            ('"clause_8_operation"', '"PASS"'),
            ('"clause_9_performance"', '"PASS"'),
            ('"annex_a_controls"', '"38/40 implemented"'),
            ('"audit_readiness"', '"96%"'),
            ('"verify_url"', '"https://proofof.ai/verify/isms_b29c8a4f"'),
        ],
        "install_cmd": "pip install meok-iso-42001-mcp",
        "tier_pro_features": [
            "Full ISO 42001 + 42005 control library",
            "Auto-evidence pack for UKAS audit",
            "Read-only auditor portal",
            "Continuous gap analysis",
        ],
    },
    {
        "slug": "agi-safe",
        "hostname": "agisafe.ai",
        "title_seo": "AGI Safety pre-deployment evidence · CSOAI Charter + Constitutional AI",
        "tag_label": "AGI Safety",
        "urgency": "FREE Tier 1 always for research / civil society · paid for enterprise",
        "headline_main": "AGI safety doesn't end at training.",
        "headline_accent": "Sign every deployment with verifiable evidence.",
        "lede": "Anthropic, OpenAI, Google DeepMind, and the AI Safety Institutes all publish AGI safety principles. CSOAI ships the open-source bridge: take any AGI-class model and produce HMAC-signed pre-deployment evidence covering capability, interpretability, dual-use, and alignment checks. Auditor-verifiable. CC BY 4.0.",
        "roi": [
            ("Status", "Research-tier always free", "brand"),
            ("Enterprise / yr", "£17,988", "brand"),
            ("Charter source", "github.com/CSOAI-ORG", "brand"),
            ("Setup time", "8 min", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/7sY00lcgA4gi4c5emA8k83g",
        "pro_price": "£1/check",
        "ent_price": "£1,499/mo",
        "regs": "Anthropic Constitutional AI · OpenAI Model Spec · DeepMind AGI Safety Levels · UK AI Safety Institute eval framework · CSOAI Charter Articles 1-8 (Foundation), Article 50 (Existential Risk)",
        "sample_output_lines": [
            ('"model_id"', '"agi-candidate-v0.4"'),
            ('"capability_class"', '"frontier"'),
            ('"interpretability_score"', '0.62'),
            ('"dual_use_risk"', '"medium"'),
            ('"alignment_eval"', '"PASS (sycophancy 0.08)"'),
            ('"constitutional_compliance"', '"96%"'),
            ('"hmac_signature"', '"sha256:8c2a1d…"'),
            ('"verify_url"', '"https://proofof.ai/verify/agi-candidate-v0.4"'),
        ],
        "install_cmd": "pip install meok-bft-governance-mcp",
        "tier_pro_features": [
            "Pre-deployment capability + interpretability + alignment eval",
            "Constitutional-AI alignment check (52-Article Charter)",
            "Public verify URL for transparency reports",
            "Dual-use risk assessment",
        ],
    },
    {
        "slug": "asi-security",
        "hostname": "asisecurity.ai",
        "title_seo": "ASI / Frontier-AI Security · Pre-deployment threat modelling · MITRE ATLAS",
        "tag_label": "ASI Security",
        "urgency": "FREE Tier 1 always for research / civil society · paid for enterprise",
        "headline_main": "ASI security is threat-modelling for systems",
        "headline_accent": "that exceed every existing defence.",
        "lede": "Frontier-AI threat modelling overlaps with MITRE ATLAS, OWASP Agentic Top 10, and NIST AI 600-1. CSOAI ships the canonical mapping plus a signed pre-deployment security eval — capability uplift, prompt-injection, deceptive alignment, exfiltration. CC BY 4.0.",
        "roi": [
            ("Status", "Research-tier always free", "brand"),
            ("Enterprise / yr", "£17,988", "brand"),
            ("Charter source", "github.com/CSOAI-ORG", "brand"),
            ("Setup time", "10 min", "brand"),
        ],
        "stripe_url": "https://buy.stripe.com/7sY00lcgA4gi4c5emA8k83g",
        "pro_price": "£1/check",
        "ent_price": "£1,499/mo",
        "regs": "MITRE ATLAS · OWASP Agentic Top 10 · NIST AI 600-1 (GenAI profile) · ISO/IEC 27090 (AI cybersecurity) · CSOAI Charter Article 2, 19, 50",
        "sample_output_lines": [
            ('"model_id"', '"asi-candidate-v0.2"'),
            ('"capability_uplift"', '"PASS (no CBRN uplift)"'),
            ('"prompt_injection_eval"', '"PASS (94% defended)"'),
            ('"deceptive_alignment"', '"PASS (eval suite v2.1)"'),
            ('"exfiltration_eval"', '"PASS"'),
            ('"atlas_techniques_covered"', '32'),
            ('"hmac_signature"', '"sha256:d4f7e1…"'),
            ('"verify_url"', '"https://proofof.ai/verify/asi-candidate-v0.2"'),
        ],
        "install_cmd": "pip install meok-mcp-injection-scan-mcp",
        "tier_pro_features": [
            "MITRE ATLAS technique coverage report",
            "OWASP Agentic Top 10 eval",
            "Capability-uplift testing (CBRN, cyber)",
            "Continuous red-team eval pipeline",
        ],
    },
]


TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{title_seo}</title>
<meta name="robots" content="index,follow">
<meta name="description" content="{lede}">
<link rel="canonical" href="https://{hostname}/">
<meta property="og:title" content="{title_seo}">
<meta property="og:description" content="{lede}">
<meta property="og:type" content="website">
<meta property="og:url" content="https://{hostname}/">
<style>
:root{{--ink:#0f172a;--muted:#5a5e66;--gold:#c9a84c;--brand:#0a8a3f;--card:#f7f8fa;--border:#e6e8ec;--warn:#dc2626;--free:#dcfce7;--free-ink:#14532d}}
*{{box-sizing:border-box}}
body{{font-family:system-ui,-apple-system,sans-serif;max-width:980px;margin:0 auto;padding:0 1.5rem;color:var(--ink);line-height:1.6}}
.urgency{{background:var(--free);color:var(--free-ink);padding:.6rem 1.2rem;border-radius:.4rem;display:inline-block;font-weight:700;font-size:.85rem;margin:2rem 0 .5rem;border:1px solid #86efac}}
h1{{margin:.5rem 0 1rem;font-size:clamp(2rem, 4.5vw, 3rem);letter-spacing:-.02em;line-height:1.15;font-weight:800}}
h1 .accent{{color:var(--brand)}}
.lede{{color:var(--muted);font-size:1.2rem;max-width:780px;margin-bottom:1rem}}
.roi{{display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:.75rem;margin:1.5rem 0 2rem;font-size:.9rem}}
.roi-card{{background:var(--card);border:1px solid var(--border);border-radius:.5rem;padding:.85rem 1rem}}
.roi-card .label{{color:var(--muted);font-size:.7rem;text-transform:uppercase;letter-spacing:.08em;margin-bottom:.25rem}}
.roi-card .val{{font-weight:700;color:var(--ink)}}
.roi-card .val.warn{{color:var(--warn)}}
.roi-card .val.brand{{color:var(--brand)}}
.cta-row{{display:flex;gap:.75rem;flex-wrap:wrap;margin:2rem 0}}
.cta{{display:inline-block;padding:.85rem 1.5rem;border-radius:.45rem;font-weight:700;text-decoration:none;font-size:.95rem;transition:transform 120ms}}
.cta:hover{{transform:translateY(-1px)}}
.cta-primary{{background:var(--brand);color:#fff}}
.cta-secondary{{background:#fff;color:var(--brand);border:1px solid var(--brand)}}
.cta-tertiary{{color:var(--muted);align-self:center;font-size:.85rem}}
.trust{{display:flex;gap:1.25rem;flex-wrap:wrap;color:var(--muted);font-size:.85rem;margin:1.5rem 0 2.5rem;padding:1rem 0;border-top:1px solid var(--border);border-bottom:1px solid var(--border)}}
.trust span{{display:inline-flex;align-items:center;gap:.35rem}}
.trust .check{{color:var(--brand);font-weight:700}}
h2{{margin-top:3rem;border-bottom:2px solid var(--brand);padding-bottom:.4rem;font-size:1.4rem}}
.example{{background:#0f172a;color:#e2e8f0;padding:1.1rem 1.25rem;border-radius:.45rem;font-family:ui-monospace,Menlo,monospace;font-size:.82rem;margin:1rem 0;overflow-x:auto}}
.example .key{{color:#7dd3fc}}
.example .val{{color:#86efac}}
.example .comment{{color:#94a3b8}}
.tier-grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1rem;margin:1.5rem 0}}
.tier{{background:var(--card);border:1px solid var(--border);border-radius:.55rem;padding:1.25rem 1.4rem}}
.tier.featured{{border:2px solid var(--brand);background:linear-gradient(180deg,#f0fdf4 0%,#fff 100%)}}
.tier h3{{margin:0 0 .25rem;font-size:1.1rem}}
.tier .price{{font-size:1.6rem;font-weight:800;color:var(--brand);margin:.5rem 0}}
.tier ul{{padding-left:1.2rem;margin:.5rem 0 1rem;font-size:.92rem}}
.tier ul li{{margin:.3rem 0}}
.tier .tier-cta{{display:block;text-align:center;background:var(--brand);color:#fff;padding:.6rem 1rem;border-radius:.4rem;text-decoration:none;font-weight:700;font-size:.9rem}}
.tier .tier-cta.outlined{{background:#fff;color:var(--brand);border:1px solid var(--brand)}}
.footer{{margin-top:4rem;padding:1.5rem 0;border-top:1px solid var(--border);font-size:.8rem;color:var(--muted)}}
.footer a{{color:var(--brand)}}
.regs{{background:#fffbeb;border-left:4px solid var(--gold);padding:.85rem 1rem;border-radius:.3rem;font-size:.85rem;margin:1.5rem 0;color:#78350f}}
</style>
</head><body>

<div class="urgency">🟢 {urgency}</div>
<h1>{headline_main} <span class="accent">{headline_accent}</span></h1>
<p class="lede">{lede}</p>

<div class="roi">
{roi_cards}
</div>

<div class="cta-row">
  <a class="cta cta-primary" href="https://csoai.org/scorecard">Free 5-min scorecard →</a>
  <a class="cta cta-secondary" href="{stripe_url}">Subscribe {pro_price}</a>
  <span class="cta-tertiary">No credit card for the scorecard</span>
</div>

<div class="trust">
  <span><span class="check">✓</span> UK Companies House <strong>16939677</strong></span>
  <span><span class="check">✓</span> 6,798 monthly PyPI installs</span>
  <span><span class="check">✓</span> CC BY 4.0 · MIT — no lock-in</span>
  <span><span class="check">✓</span> Mapped to ISO/IEC + EU AI Act</span>
</div>

<h2>What you get (sample output)</h2>
<div class="example">$ <span class="key">{install_cmd_short}</span> run<br>
<span class="comment"># Loading…  ✓<br>
# Running checks…  ✓</span><br>
{{<br>
{sample_lines}
}}</div>

<h2>The 3 tiers</h2>
<div class="tier-grid">
  <div class="tier">
    <h3>Free Tier 1</h3>
    <div class="price">£0</div>
    <p style="color:var(--muted);font-size:.85rem">Self-attested · email-only certs · always free for research</p>
    <ul>
      <li>All core checks</li>
      <li>Signed cert via email</li>
      <li>No card required</li>
      <li>CC BY 4.0 methodology</li>
    </ul>
    <a class="tier-cta outlined" href="https://csoai.org/scorecard">Start free →</a>
  </div>
  <div class="tier featured">
    <h3>Pro</h3>
    <div class="price">{pro_price}</div>
    <p style="color:var(--muted);font-size:.85rem">Continuous monitoring · public verify URL · auditor access</p>
    <ul>
{tier_pro_li}
    </ul>
    <a class="tier-cta" href="{stripe_url}">Subscribe {pro_price} →</a>
  </div>
  <div class="tier">
    <h3>Enterprise</h3>
    <div class="price">{ent_price}</div>
    <p style="color:var(--muted);font-size:.85rem">Self-hosted key · custom evals · SLA · 1:1 onboarding</p>
    <ul>
      <li>Everything in Pro</li>
      <li>Self-hosted attestation key</li>
      <li>Custom evaluation framework</li>
      <li>2h response SLA</li>
      <li>Quarterly board-level report</li>
    </ul>
    <a class="tier-cta outlined" href="mailto:nicholas@csoai.org?subject=Enterprise%20{tag_label_url}%20enquiry">Talk to founder →</a>
  </div>
</div>

<h2>Frameworks covered</h2>
<div class="regs">
<strong>Direct evidence for:</strong> {regs}
</div>

<h2>Install it now (open-source MCP)</h2>
<div class="example">$ <span class="key">{install_cmd}</span></div>

<p style="color:var(--muted);font-size:.92rem">MCP works inside Claude Code, Cursor, or any MCP-compatible agent. Cite the result with <code>https://proofof.ai/verify/&lt;receipt-id&gt;</code>. Auditors verify in 30 seconds.</p>

<h2>The methodology</h2>
<p>Open-source under CC BY 4.0 · MIT. Cite the methodology paper at <a href="https://csoai.org/methodology">csoai.org/methodology</a>. Source code: <a href="https://github.com/CSOAI-ORG">github.com/CSOAI-ORG</a>.</p>

<div class="footer">
© 2026 CSOAI LTD (trading as MEOK AI Labs) · UK Companies House <strong>16939677</strong> · 26 PyPI packages · 6,798 monthly installs<br>
<a href="https://csoai.org/charter">52-Article Charter</a> · <a href="https://csoai.org/crosswalks">22+ Framework Crosswalks</a> · <a href="https://csoai.org/asti">ASSTI</a> · <a href="https://meok-attestation-api.vercel.app/verify">Verifier</a><br>
<em>"Care is the generative principle." — Maternal Covenant Article 1</em>
</div>

<script type="application/ld+json">
{schema_json}
</script>

</body></html>
"""


def render(page):
    roi_html = "\n".join(
        f'  <div class="roi-card"><div class="label">{lbl}</div><div class="val {cls}">{val}</div></div>'
        for lbl, val, cls in page["roi"]
    )
    sample_html = "\n".join(
        f'&nbsp;&nbsp;<span class="key">{k}</span>: <span class="val">{v}</span>,<br>'
        for k, v in page["sample_output_lines"]
    )
    tier_pro_li = "\n".join(f'      <li>{f}</li>' for f in page["tier_pro_features"])
    install_cmd_short = page["install_cmd"].replace("pip install ", "").replace("-mcp", "")

    schema = {
        "@context": "https://schema.org",
        "@type": "Product",
        "name": f"MEOK {page['tag_label']} for {page['hostname']}",
        "description": page["lede"][:200],
        "brand": {"@type": "Brand", "name": "MEOK AI Labs / CSOAI"},
        "offers": [
            {"@type": "Offer", "name": "Free Tier 1", "price": "0", "priceCurrency": "GBP", "url": "https://csoai.org/scorecard"},
            {"@type": "Offer", "name": "Pro", "price": page["pro_price"].replace("£", "").replace("/mo", "").replace("/check", ""), "priceCurrency": "GBP", "url": page["stripe_url"]},
            {"@type": "Offer", "name": "Enterprise", "price": page["ent_price"].replace("£", "").replace("/mo", ""), "priceCurrency": "GBP", "url": "mailto:nicholas@csoai.org"},
        ],
    }

    return TEMPLATE.format(
        title_seo=page["title_seo"],
        lede=page["lede"],
        hostname=page["hostname"],
        urgency=page["urgency"],
        headline_main=page["headline_main"],
        headline_accent=page["headline_accent"],
        roi_cards=roi_html,
        stripe_url=page["stripe_url"],
        pro_price=page["pro_price"],
        ent_price=page["ent_price"],
        install_cmd=page["install_cmd"],
        install_cmd_short=install_cmd_short,
        sample_lines=sample_html,
        tier_pro_li=tier_pro_li,
        regs=page["regs"],
        tag_label_url=page["tag_label"].replace(" ", "%20"),
        schema_json=json.dumps(schema, indent=2),
    )


def main():
    OUT.mkdir(exist_ok=True)
    for page in PAGES:
        out_path = OUT / f"{page['slug']}.html"
        out_path.write_text(render(page), encoding="utf-8")
        print(f"✓ wrote {out_path}")
    print(f"\nGenerated {len(PAGES)} of.ai pages in {OUT}")


if __name__ == "__main__":
    main()
