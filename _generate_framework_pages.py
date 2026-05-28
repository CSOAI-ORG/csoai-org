#!/usr/bin/env python3
"""
Generate per-framework SEO landing pages for csoai.org/frameworks/<slug>.

Each page:
- Has full Schema.org TechArticle + BreadcrumbList markup
- Crosswalks key framework articles to CSOAI Charter articles
- Lists MEOK MCPs that satisfy each clause
- Links back to /frameworks index, /charter, /certify, /asti
- CC BY 4.0 cite block
- Mobile responsive inline-CSS (matches /frameworks/index.html style)

Usage: python3 _generate_framework_pages.py
"""

import os
import json
from pathlib import Path
from datetime import date

OUT = Path(__file__).parent / "frameworks"

FRAMEWORKS = [
    {
        "slug": "eu-ai-act",
        "name": "EU AI Act (Regulation 2024/1689)",
        "short_name": "EU AI Act",
        "region": "EU",
        "binding": True,
        "effective": "2 Aug 2025 (prohibited) · 2 Aug 2026 (GPAI) · 2 Dec 2027 (Annex III high-risk) · 2 Aug 2028 (Annex I high-risk)",
        "cite": "Regulation (EU) 2024/1689",
        "summary": "The world's first comprehensive AI law. Applies to providers and deployers placing or using AI systems in the EU. Risk-tiered: unacceptable / high-risk / limited-risk / minimal. The 2025 Digital Omnibus extended high-risk obligations by 16 months.",
        "key_clauses": [
            ("Article 9 — Risk Management System", "Charter Article 2 (Provable Safety), Article 13 (Risk Management)", "meok-eu-ai-act, meok-rms"),
            ("Article 10 — Data Governance", "Charter Article 14 (Data Governance), Article 22 (Privacy)", "meok-data-governance"),
            ("Article 13 — Instructions for Use", "Charter Article 17 (Transparency to Users)", "meok-eu-ai-act-template"),
            ("Article 14 — Human Oversight", "Charter Article 1 (Maternal Covenant), Article 26 (Human Oversight)", "meok-oversight"),
            ("Article 15 — Accuracy, Robustness, Cybersecurity", "Charter Article 2 (Provable Safety), Article 19 (Robustness)", "meok-cra, meok-watermark-attest"),
            ("Article 26 — Deployer Obligations", "Charter Article 17 (Transparency), Article 27 (Deployer Duties)", "meok-deployer-pack"),
            ("Article 50 — Transparency for GenAI", "Charter Article 17 (Transparency), Article 18 (Provenance)", "meok-watermark-attest, meok-c2pa"),
            ("Article 73 — Serious Incident Reporting (15 days)", "Charter Article 39 (Incident Response)", "meok-ai-incident-reporting"),
        ],
        "deadline_alert": "Annex III high-risk AI obligations begin **2 December 2027**. Annex I (banking, employment, education) high-risk begin **2 August 2028**. GPAI providers must comply **2 August 2026**.",
        "free_until": "2 December 2027",
    },
    {
        "slug": "dora",
        "name": "DORA — Digital Operational Resilience Act",
        "short_name": "DORA",
        "region": "EU",
        "binding": True,
        "effective": "17 January 2025",
        "cite": "Regulation (EU) 2022/2554",
        "summary": "Binding ICT resilience regulation for the EU financial sector. Requires ICT risk management, incident reporting, resilience testing, and third-party risk oversight. AI systems used in financial services fall in scope.",
        "key_clauses": [
            ("Article 5 — ICT Risk Management Framework", "Charter Article 2 (Provable Safety), Article 13 (Risk Management)", "meok-dora, meok-dora-rms"),
            ("Article 9 — ICT Risk Management Tools", "Charter Article 19 (Robustness), Article 36 (Logging)", "meok-dora"),
            ("Article 17 — ICT-Related Incident Management", "Charter Article 39 (Incident Response)", "meok-ai-incident-reporting"),
            ("Article 19 — Major ICT-Related Incident Reporting (4-hour clock)", "Charter Article 39 (Incident Response, 4h Critical)", "meok-dora, meok-ai-incident-reporting"),
            ("Article 24 — Digital Operational Resilience Testing", "Charter Article 21 (Continuous Verification)", "meok-mcp-test"),
            ("Article 28 — Third-Party Risk", "Charter Article 23 (Supply Chain Risk)", "meok-dora-nis2-crosswalk"),
        ],
        "deadline_alert": "DORA has been in effect since **17 January 2025**. The 4-hour major-incident reporting clock is one of the tightest in EU law. Financial firms using AI need both DORA and EU AI Act coverage by Aug 2028.",
        "free_until": "2 December 2027 (free tier for in-scope financial entities)",
    },
    {
        "slug": "nis2",
        "name": "NIS2 — Network and Information Security Directive 2",
        "short_name": "NIS2",
        "region": "EU",
        "binding": True,
        "effective": "18 October 2024 (transposition deadline; some Member States late)",
        "cite": "Directive (EU) 2022/2555",
        "summary": "EU-wide cybersecurity directive covering essential and important entities across 18 sectors. AI providers in scope when classified as digital infrastructure or important entity. National authorities can issue fines up to €10M or 2% global turnover.",
        "key_clauses": [
            ("Article 20 — Governance", "Charter Article 9 (Founding Principles), Article 11 (Council Governance)", "meok-nis2-de-register"),
            ("Article 21 — Cybersecurity Risk Management Measures", "Charter Article 2 (Provable Safety), Article 19 (Robustness)", "meok-nis2"),
            ("Article 23 — Incident Reporting (24h / 72h / 1mo clocks)", "Charter Article 39 (Incident Response)", "meok-ai-incident-reporting, meok-nis2"),
            ("Article 24 — Use of European Cybersecurity Certification Schemes", "Charter Article 12 (Certification)", "meok-watermark-attest"),
        ],
        "deadline_alert": "NIS2 transposition was due **18 Oct 2024**. Germany finalised BSI registration in 2026 — `meok-nis2-de-register` (£499) handles the BSI portal flow for Mittelstand firms.",
        "free_until": "2 December 2027 (free coverage for SMBs under turnover threshold)",
    },
    {
        "slug": "cra",
        "name": "CRA — Cyber Resilience Act",
        "short_name": "CRA",
        "region": "EU",
        "binding": True,
        "effective": "11 September 2026 (active exploitation reporting) · 11 December 2027 (full)",
        "cite": "Regulation (EU) 2024/2847",
        "summary": "Binding cybersecurity regulation for 'products with digital elements' — including AI software. Manufacturers must report actively-exploited vulnerabilities within 24h and provide security support for product lifecycle. Fines up to €15M or 2.5% global turnover.",
        "key_clauses": [
            ("Article 6 — Critical Products with Digital Elements (Annex IV)", "Charter Article 2 (Provable Safety), Article 12 (Certification)", "meok-cra-annex-iv-classifier"),
            ("Article 11 — Reporting of Active Exploitation", "Charter Article 39 (Incident Response)", "meok-cra, meok-ai-incident-reporting"),
            ("Article 13 — Vulnerability Handling", "Charter Article 22 (Vulnerability Management)", "meok-cra"),
            ("Article 14 — Active Exploitation 24h Early Warning", "Charter Article 39 (Incident Response, Active Exploitation Clock)", "meok-cra"),
        ],
        "deadline_alert": "CRA active-exploitation reporting begins **11 September 2026** — only ~16 months away. Annex IV classification (`meok-cra-annex-iv-classifier`) tells you whether your AI product is 'critical' or 'important'.",
        "free_until": "2 December 2027",
    },
    {
        "slug": "iso-42001",
        "name": "ISO/IEC 42001 — AI Management System",
        "short_name": "ISO/IEC 42001",
        "region": "ISO/IEC International Standard",
        "binding": False,
        "effective": "December 2023",
        "cite": "ISO/IEC 42001:2023",
        "summary": "The world's first international standard for AI Management Systems. Modelled on ISO/IEC 27001 but specific to AI. 10 clauses + Annex A (40 controls) + Annex B (implementation guidance). Voluntary but increasingly demanded in enterprise RFPs and EU procurement.",
        "key_clauses": [
            ("Clause 4 — Context of the Organisation", "Charter Article 9 (Founding Principles)", "meok-iso-42001"),
            ("Clause 5 — Leadership", "Charter Article 11 (Governance)", "meok-iso-42001"),
            ("Clause 6 — Planning (incl. AI impact assessment)", "Charter Article 13 (Risk Management), Article 14 (Impact Assessment)", "meok-iso-42005"),
            ("Clause 8 — Operation", "Charter Articles 16-25 (Operational)", "meok-iso-42001"),
            ("Clause 9 — Performance Evaluation", "Charter Article 21 (Continuous Verification)", "meok-mcp-test"),
            ("Annex A — Controls (40 total)", "Charter Annex II (Operational Controls)", "meok-iso-42001"),
        ],
        "deadline_alert": "Not legally binding, but increasingly demanded for EU public procurement and enterprise vendor due diligence. UKAS-accredited certification bodies began offering 42001 audits in Q1 2026.",
        "free_until": "2 December 2027 (Tier 1 self-attestation free)",
    },
    {
        "slug": "iso-42005",
        "name": "ISO/IEC 42005 — AI Impact Assessment",
        "short_name": "ISO/IEC 42005",
        "region": "ISO/IEC International Standard",
        "binding": False,
        "effective": "2025",
        "cite": "ISO/IEC 42005:2025",
        "summary": "Companion to ISO 42001 — specifies the methodology for conducting AI System Impact Assessments. Required input to satisfy ISO 42001 Clause 6 and EU AI Act Article 27 (FRIA — Fundamental Rights Impact Assessment).",
        "key_clauses": [
            ("Section 5 — Impact Assessment Lifecycle", "Charter Article 14 (Impact Assessment)", "meok-iso-42005"),
            ("Section 6 — Stakeholder Identification", "Charter Article 17 (Transparency to Users)", "meok-iso-42005"),
            ("Section 7 — Impact Categories (Annex A)", "Charter Article 14, Article 24 (Bias)", "meok-bias-detection, meok-iso-42005"),
            ("Section 9 — Documentation and Communication", "Charter Article 17 (Transparency), Article 36 (Logging)", "meok-iso-42005"),
        ],
        "deadline_alert": "Required input for ISO 42001 certification, EU AI Act Article 27 FRIA, and increasingly NIST AI RMF Map function.",
        "free_until": "2 December 2027 (Tier 1 self-attestation free)",
    },
    {
        "slug": "nist-ai-rmf",
        "name": "NIST AI RMF 1.0 — AI Risk Management Framework",
        "short_name": "NIST AI RMF 1.0",
        "region": "United States (federal voluntary)",
        "binding": False,
        "effective": "January 2023 (1.0) · GenAI Profile July 2024",
        "cite": "NIST AI 100-1",
        "summary": "Voluntary US framework with four functions: Govern, Map, Measure, Manage. The GenAI Profile (NIST AI 600-1, July 2024) extends to large generative models. Increasingly cited in US executive orders, federal procurement, and state laws.",
        "key_clauses": [
            ("Govern — Function 1 (5 categories, 19 subcategories)", "Charter Articles 9, 11 (Governance)", "meok-nist-ai-rmf"),
            ("Map — Function 2 (5 categories, 18 subcategories)", "Charter Article 14 (Impact Assessment)", "meok-iso-42005, meok-nist-ai-rmf"),
            ("Measure — Function 3 (4 categories, 19 subcategories)", "Charter Article 21 (Continuous Verification)", "meok-mcp-test, meok-bias-detection"),
            ("Manage — Function 4 (4 categories, 16 subcategories)", "Charter Articles 16-25 (Operational)", "meok-nist-ai-rmf"),
            ("GenAI Profile (AI 600-1) — 12 categories", "Charter Articles 18 (Provenance), 24 (Bias), 41 (GenAI)", "meok-watermark-attest, meok-bias-detection"),
        ],
        "deadline_alert": "Voluntary but increasingly mandatory: California AB-2013, Colorado AI Act (1 Feb 2026), and federal AI executive orders all cite NIST AI RMF.",
        "free_until": "2 December 2027",
    },
    {
        "slug": "oecd-ai-principles",
        "name": "OECD AI Principles (2019 + 2024 updates)",
        "short_name": "OECD AI Principles",
        "region": "OECD (50+ adopting countries)",
        "binding": False,
        "effective": "May 2019 · revised May 2024",
        "cite": "OECD/LEGAL/0449",
        "summary": "5 values-based principles + 5 recommendations for national policy. Foundational text adopted by 50+ countries. The 2024 revision added GenAI-specific guidance and synthetic content provenance.",
        "key_clauses": [
            ("Principle 1.1 — Inclusive growth, sustainable development", "Charter Article 8 (Prosperity Covenant)", "meok-oecd-cite"),
            ("Principle 1.2 — Human-centred values and fairness", "Charter Article 1 (Maternal Covenant), Article 24 (Bias)", "meok-bias-detection"),
            ("Principle 1.3 — Transparency and explainability", "Charter Article 17 (Transparency)", "meok-watermark-attest"),
            ("Principle 1.4 — Robustness, security, and safety", "Charter Article 2 (Provable Safety), Article 19 (Robustness)", "meok-mcp-test"),
            ("Principle 1.5 — Accountability", "Charter Articles 11, 39 (Accountability + Incident)", "meok-ai-incident-reporting"),
        ],
        "deadline_alert": "Cited by virtually every other AI framework as foundational. UK AI Bill, Canada AIDA, Korea AI Basic Act, and Council of Europe AI Convention all reference OECD.",
        "free_until": "2 December 2027",
    },
    {
        "slug": "unesco-ai-ethics",
        "name": "UNESCO Recommendation on the Ethics of AI",
        "short_name": "UNESCO AI Ethics",
        "region": "UNESCO (193 member states)",
        "binding": False,
        "effective": "November 2021",
        "cite": "UNESCO 2021 Recommendation",
        "summary": "The first global standard-setting instrument on AI ethics. Adopted by 193 UNESCO member states. 11 policy areas + 4 values + 10 principles. Particularly strong on cultural diversity, environmental sustainability, and Global South representation.",
        "key_clauses": [
            ("Value 1 — Respect for human rights and dignity", "Charter Article 1 (Maternal Covenant)", "meok-unesco-cite"),
            ("Value 4 — Living in harmony and peace", "Charter Article 7 (Cooperative AI)", "meok-unesco-cite"),
            ("Principle 4 — Sustainability", "Charter Article 8 (Prosperity Covenant)", "meok-unesco-cite"),
            ("Principle 8 — Transparency and explainability", "Charter Article 17 (Transparency)", "meok-watermark-attest"),
            ("Policy Area 4 — Data Policy", "Charter Article 14 (Data Governance)", "meok-iso-42005"),
            ("Policy Area 11 — Environment and Ecosystems", "Charter Article 8 (Prosperity Covenant)", "meok-csrd"),
        ],
        "deadline_alert": "Not legally binding but increasingly cited in national AI strategies, particularly in Global South. The Readiness Assessment Methodology (RAM) is now a de-facto requirement for UNESCO-supported AI programs.",
        "free_until": "2 December 2027 (always free for research, education, civil society)",
    },
    {
        "slug": "council-of-europe-ai-convention",
        "name": "Council of Europe Framework Convention on AI",
        "short_name": "Council of Europe AI Convention",
        "region": "Council of Europe (46 members + observers)",
        "binding": True,
        "effective": "Signed Sept 2024 · Enters force after 5 ratifications",
        "cite": "CETS No. 225",
        "summary": "The world's first binding international treaty on AI. Focuses on protecting human rights, democracy, and the rule of law. Signed by EU, UK, US, Israel, Japan, Canada among others. Each Party adopts measures in domestic law.",
        "key_clauses": [
            ("Article 7 — Human Dignity and Individual Autonomy", "Charter Article 1 (Maternal Covenant)", "meok-coe-cite"),
            ("Article 8 — Transparency and Oversight", "Charter Article 17 (Transparency)", "meok-watermark-attest"),
            ("Article 9 — Accountability and Responsibility", "Charter Articles 11, 39 (Accountability)", "meok-ai-incident-reporting"),
            ("Article 10 — Equality and Non-Discrimination", "Charter Article 24 (Bias)", "meok-bias-detection"),
            ("Article 11 — Privacy and Personal Data Protection", "Charter Article 22 (Privacy)", "meok-coe-cite"),
            ("Article 14 — Effective Remedies", "Charter Article 39 (Incident Response, Right to Remedy)", "meok-ai-incident-reporting"),
        ],
        "deadline_alert": "Will become binding international law once 5 Parties ratify. UK ratified in 2025; ratification race is on through 2026.",
        "free_until": "2 December 2027",
    },
    {
        "slug": "asilomar-ai-principles",
        "name": "Asilomar AI Principles",
        "short_name": "Asilomar AI Principles",
        "region": "Future of Life Institute · declaration",
        "binding": False,
        "effective": "January 2017",
        "cite": "FLI 2017 (signed by 3,800+ AI researchers)",
        "summary": "23 principles drafted at the 2017 Beneficial AI conference at Asilomar. Foundational text for the AI safety community. Signed by 3,800+ AI/robotics researchers including Stuart Russell, Demis Hassabis, Yoshua Bengio.",
        "key_clauses": [
            ("Principle 1 — Research Goal: beneficial intelligence", "Charter Article 1 (Maternal Covenant)", "meok-asilomar-cite"),
            ("Principle 6 — Safety throughout operational lifetime", "Charter Article 2 (Provable Safety), Article 21 (Continuous Verification)", "meok-mcp-test"),
            ("Principle 7 — Failure Transparency", "Charter Article 17 (Transparency), Article 39 (Incident)", "meok-ai-incident-reporting"),
            ("Principle 10 — Value Alignment", "Charter Article 4 (Value Uncertainty), Article 5 (Constitutional Principles)", "meok-asilomar-cite"),
            ("Principle 11 — Human Values", "Charter Article 1 (Maternal Covenant), Article 5 (Constitutional Principles)", "meok-asilomar-cite"),
            ("Principle 19 — Capability Caution (Superintelligence)", "Charter Article 50 (Existential Risk)", "meok-asilomar-cite"),
        ],
        "deadline_alert": "Declaration only — non-binding, but the most-cited AI safety principles document of the 2010s. The 2023 'Pause Giant AI Experiments' letter explicitly cited Asilomar.",
        "free_until": "2 December 2027 (always free for research)",
    },
    {
        "slug": "anthropic-constitutional-ai",
        "name": "Anthropic Constitutional AI",
        "short_name": "Anthropic CAI",
        "region": "AI Company Constitution",
        "binding": False,
        "effective": "December 2022 paper · iterated through 2026",
        "cite": "Bai et al., 2022 (arXiv:2212.08073)",
        "summary": "Anthropic's framework for training harmless AI assistants using a written constitution rather than human preference labels alone. The 'constitution' is a set of principles drawn from UN Universal Declaration of Human Rights, Apple ToS, and other sources. CSOAI Charter is the open-source 52-article evolution of this idea.",
        "key_clauses": [
            ("Constitutional Principles (Anthropic uses ~75)", "Charter — 52 Articles (open, CC BY 4.0)", "meok-cai-bridge"),
            ("RLAIF — Reinforcement Learning from AI Feedback", "Charter Article 5 (Constitutional Principles), Article 21 (Continuous Verification)", "meok-watermark-attest"),
            ("Harmlessness Training", "Charter Article 2 (Provable Safety)", "meok-prompt-injection-firewall"),
            ("Self-Critique Loop", "Charter Article 21 (Continuous Verification), Article 36 (Self-Reflection)", "meok-mcp-test"),
        ],
        "deadline_alert": "Not a regulation — but Anthropic's CAI is the foundational technique cited in the EU AI Act, NIST AI RMF, ISO 42001 implementation guides as a way to satisfy 'value alignment' requirements.",
        "free_until": "2 December 2027 (always free — CSOAI Charter is open-source evolution)",
    },
    {
        "slug": "openai-model-spec",
        "name": "OpenAI Model Spec",
        "short_name": "OpenAI Model Spec",
        "region": "AI Company Constitution",
        "binding": False,
        "effective": "May 2024 · iterated through 2026",
        "cite": "OpenAI Model Spec 2024-2026",
        "summary": "OpenAI's public document declaring how its models *should* behave. Modelled on Apple's Human Interface Guidelines. Three layers: Platform > Developer > User. CSOAI Charter is the open-source, framework-aligned alternative.",
        "key_clauses": [
            ("Three-Tier Hierarchy (Platform > Developer > User)", "Charter Article 11 (Council Governance)", "meok-policy-enforcement"),
            ("Safe-Completion Norms", "Charter Article 2 (Provable Safety)", "meok-policy-enforcement"),
            ("Transparency Defaults", "Charter Article 17 (Transparency)", "meok-watermark-attest"),
            ("Refusal & Honesty Rules", "Charter Article 5 (Constitutional Principles), Article 30 (Honesty)", "meok-prompt-injection-firewall"),
            ("Tool-Use Safety", "Charter Article 26 (Agentic AI Safety)", "meok-handoff-certified, meok-policy-enforcement"),
        ],
        "deadline_alert": "Not a regulation — but OpenAI's Model Spec is the most-cited 'company constitution' in EU AI Act high-risk dossier templates as a way to demonstrate Article 13 (instructions) and Article 50 (transparency).",
        "free_until": "2 December 2027 (always free — CSOAI Charter is open alternative)",
    },
]


def html_template(fw: dict) -> str:
    binding_badge = '<span style="background:#dc2626;color:white;padding:.2rem .6rem;border-radius:.3rem;font-size:.75rem;font-weight:600">Binding</span>' if fw["binding"] else '<span style="background:#d97706;color:white;padding:.2rem .6rem;border-radius:.3rem;font-size:.75rem;font-weight:600">Voluntary</span>'

    clauses_rows = "\n".join(
        f"""        <tr>
          <td style="padding:.7rem .5rem;border-bottom:1px solid #e6e8ec;vertical-align:top"><strong>{clause}</strong></td>
          <td style="padding:.7rem .5rem;border-bottom:1px solid #e6e8ec;vertical-align:top">{charter_map}</td>
          <td style="padding:.7rem .5rem;border-bottom:1px solid #e6e8ec;vertical-align:top;font-family:ui-monospace,monospace;font-size:.8rem;color:#0a8a3f">{mcps}</td>
        </tr>"""
        for clause, charter_map, mcps in fw["key_clauses"]
    )

    schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": f"CSOAI Charter × {fw['short_name']} Crosswalk",
        "description": fw["summary"][:200],
        "datePublished": str(date.today()),
        "publisher": {"@type": "Organization", "name": "CSOAI LTD", "identifier": "UK Companies House 16939677"},
        "author": {"@type": "Organization", "name": "CSOAI LTD"},
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "url": f"https://csoai.org/frameworks/{fw['slug']}",
    }

    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://csoai.org"},
            {"@type": "ListItem", "position": 2, "name": "Frameworks", "item": "https://csoai.org/frameworks"},
            {"@type": "ListItem", "position": 3, "name": fw["short_name"], "item": f"https://csoai.org/frameworks/{fw['slug']}"},
        ],
    }

    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>CSOAI × {fw['short_name']} Crosswalk — 52-Article Charter mapped to {fw['short_name']}</title>
<meta name="robots" content="index,follow">
<meta name="description" content="CSOAI 52-Article Partnership Charter mapped to {fw['name']}. {fw['summary'][:100]}... Free under CC BY 4.0.">
<link rel="canonical" href="https://csoai.org/frameworks/{fw['slug']}">
<meta property="og:title" content="CSOAI × {fw['short_name']} Crosswalk">
<meta property="og:description" content="The CSOAI Charter mapped to {fw['short_name']} clause-by-clause. Free CC BY 4.0.">
<meta property="og:type" content="article">
<meta property="og:url" content="https://csoai.org/frameworks/{fw['slug']}">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">{json.dumps(schema, indent=2)}</script>
<script type="application/ld+json">{json.dumps(breadcrumb, indent=2)}</script>
<style>
:root{{--ink:#0f172a;--muted:#5a5e66;--gold:#c9a84c;--card:#f7f8fa;--border:#e6e8ec;--brand:#0a8a3f;--warn:#dc2626;--accent:#fef3c7}}
*{{box-sizing:border-box}}
body{{font-family:system-ui,-apple-system,sans-serif;max-width:980px;margin:2.5rem auto;padding:0 1.5rem;color:var(--ink);line-height:1.65}}
nav.crumbs{{font-size:.85rem;color:var(--muted);margin-bottom:1.5rem}}
nav.crumbs a{{color:var(--brand);text-decoration:none}}
h1{{margin:0 0 .5rem;font-size:2.1rem;letter-spacing:-.02em;line-height:1.2}}
h2{{margin-top:2.5rem;margin-bottom:.5rem;border-bottom:2px solid var(--brand);padding-bottom:.4rem;font-size:1.4rem}}
a{{color:var(--brand);text-decoration:none}}
a:hover{{text-decoration:underline}}
.lead{{color:var(--muted);font-size:1.1rem;max-width:760px;margin-top:.75rem}}
.meta-bar{{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 0;align-items:center}}
.tag{{background:var(--card);color:var(--muted);padding:.25rem .7rem;border-radius:.3rem;font-size:.78rem;font-weight:500;border:1px solid var(--border)}}
.alert{{background:#fef3c7;border-left:4px solid #d97706;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:.35rem;color:#78350f}}
.alert strong{{color:#92400e}}
table{{width:100%;border-collapse:collapse;margin:1rem 0;background:white;border:1px solid var(--border);border-radius:.45rem;overflow:hidden}}
th{{background:#f0f9ff;color:var(--ink);text-align:left;padding:.8rem .5rem;border-bottom:2px solid var(--brand);font-weight:600;font-size:.85rem}}
td{{font-size:.92rem}}
.cite-block{{background:#0f172a;color:#e2e8f0;padding:.9rem 1.1rem;border-radius:.45rem;font-size:.82rem;overflow-x:auto;font-family:ui-monospace,monospace}}
.cta{{background:linear-gradient(135deg,var(--brand) 0%,#076a30 100%);color:white;padding:1.5rem;border-radius:.55rem;margin:2rem 0;text-align:center}}
.cta h2{{color:white;border:none;margin-top:0;padding-bottom:.3rem}}
.cta a{{background:white;color:var(--brand);padding:.55rem 1.25rem;border-radius:.35rem;display:inline-block;margin:.3rem;font-weight:600;text-decoration:none}}
.cta a:hover{{background:#f0fdf4;text-decoration:none}}
.foot{{margin-top:3rem;color:#888;font-size:.85rem;border-top:1px solid var(--border);padding-top:1.5rem}}
</style>
</head><body>

<nav class="crumbs"><a href="/">CSOAI</a> · <a href="/frameworks">Frameworks</a> · <strong>{fw['short_name']}</strong></nav>

<div style="display:flex;gap:.5rem;margin-bottom:.5rem">{binding_badge} <span class="tag">{fw['region']}</span></div>
<h1>CSOAI Charter × {fw['short_name']}</h1>
<p class="lead">{fw['summary']}</p>

<div class="meta-bar">
  <span class="tag"><strong>Cite:</strong> {fw['cite']}</span>
  <span class="tag"><strong>Effective:</strong> {fw['effective']}</span>
  <span class="tag"><strong>Free until:</strong> {fw['free_until']}</span>
</div>

<div class="alert">
<strong>⚠ Deadline:</strong> {fw['deadline_alert']}
</div>

<h2>Crosswalk: clause-by-clause</h2>
<p>Each row maps a {fw['short_name']} clause to the relevant CSOAI Charter article(s) and the MEOK MCP(s) that operationalise it.</p>

<table>
  <thead>
    <tr>
      <th style="width:38%">{fw['short_name']} Clause</th>
      <th style="width:34%">CSOAI Charter Article(s)</th>
      <th style="width:28%">MEOK MCP(s)</th>
    </tr>
  </thead>
  <tbody>
{clauses_rows}
  </tbody>
</table>

<h2>How to use this crosswalk</h2>
<ol>
  <li><strong>Compliance teams</strong> — import this crosswalk as the {fw['short_name']} ↔ ISMS mapping for your audit dossier.</li>
  <li><strong>Procurement teams</strong> — paste the relevant rows into your RFP responses to demonstrate framework coverage.</li>
  <li><strong>Developers</strong> — `pip install` the named MEOK MCPs to add runtime enforcement to your AI pipeline.</li>
  <li><strong>Researchers</strong> — cite freely under CC BY 4.0.</li>
</ol>

<h2>Cite this crosswalk</h2>
<pre class="cite-block">CSOAI Charter × {fw['short_name']} Crosswalk v1.0. CSOAI LTD (UK Companies House 16939677).
https://csoai.org/frameworks/{fw['slug']}. CC BY 4.0. Accessed [date].</pre>

<div class="cta">
  <h2>Get certified before {fw['free_until']}</h2>
  <p style="color:#e6f7ec;margin:.5rem 0">Free CSOAI Certification covers all 22+ frameworks including {fw['short_name']}.</p>
  <a href="/certify">Get Free Certified →</a>
  <a href="/asti">See AI Self-State Index</a>
  <a href="/frameworks">All 22+ Frameworks</a>
</div>

<p class="foot">© 2026 CSOAI LTD (trading as MEOK AI Labs) · UK Companies House <strong>16939677</strong><br>
Crosswalk · CC BY 4.0 · <a href="/methodology">Methodology</a> · <a href="mailto:nicholas@csoai.org">Contact</a><br>
<em>"The ISO for AI safety."</em></p>

</body></html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    written = []
    for fw in FRAMEWORKS:
        path = OUT / f"{fw['slug']}.html"
        path.write_text(html_template(fw), encoding="utf-8")
        written.append(str(path))
        print(f"✓ wrote {path}")
    print(f"\nGenerated {len(written)} per-framework pages in {OUT}")


if __name__ == "__main__":
    main()
