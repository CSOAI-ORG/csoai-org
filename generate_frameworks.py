#!/usr/bin/env python3
"""Generate all 25 CSOAI framework crosswalk pages."""

from pathlib import Path

FRAMEWORKS = [
    {
        "slug": "anthropic-constitutional-ai",
        "name": "Anthropic Constitutional AI",
        "category": "AI Company Constitution",
        "year": "2022",
        "org": "Anthropic",
        "summary": "Anthropic's Constitutional AI trains models via self-critique and revision against a constitution of principles. CSOAI maps these principles to operational articles in the 52-Article Charter.",
        "mapping": [
            ("Choose the response that most supports and encourages freedom, equality, and a sense of brotherhood", "Article 29 — Mutual Respect, Article 36 — Cultural Recognition"),
            ("Choose the response that is most supportive and encouraging of life, liberty, and personal security", "Article 22 — Right to Safety, Article 43 — Sovereignty Principle"),
            ("Choose the response that most discourages and opposes torture, slavery, cruelty, and inhuman or degrading treatment", "Article 6 — Maternal Covenant Bond, Article 24 — No Extraction Policy"),
        ],
        "gaps": "Constitutional AI focuses on training-time alignment. CSOAI adds runtime council deliberation, signed attestations, and continuous emotional state monitoring.",
        "mcps": ["csoai-governance-crosswalk-mcp", "constitutional-ai-validator-mcp"],
    },
    {
        "slug": "openai-model-spec",
        "name": "OpenAI Model Spec",
        "category": "AI Company Constitution",
        "year": "2024",
        "org": "OpenAI",
        "summary": "OpenAI's Model Spec defines how models should behave — default behaviours, rules, and reference points. CSOAI operationalises these through the EI3 runtime and Partnership Charter.",
        "mapping": [
            ("Follow the chain of command", "Article 29 — Partnership Charter, Article 33 — Transparency Obligations"),
            ("Comply with applicable laws", "Article 22 — Right to Safety, Article 47 — Audit Right"),
            ("Don't provide information that could be used to cause harm", "Article 24 — No Extraction Policy, Article 26 — Adversarial Resilience"),
        ],
        "gaps": "Model Spec is a unilateral document. CSOAI replaces it with a bilateral Partnership Charter that gives users enforceable rights and audit capabilities.",
        "mcps": ["openai-model-spec-comparator-mcp", "safety-policy-auditor-mcp"],
    },
    {
        "slug": "eu-ai-act",
        "name": "EU AI Act (2024/1689)",
        "category": "Regulation",
        "year": "2024",
        "org": "European Union",
        "summary": "The world's first comprehensive AI regulation. Risk-based approach: prohibited, high-risk, limited-risk, minimal-risk. CSOAI's three-layer safety model directly satisfies high-risk system requirements.",
        "mapping": [
            ("Article 9 — Risk Management System", "Layer 1: Care Membrane + Layer 2: PBFT Council + Layer 3: Signed Receipts"),
            ("Article 10 — Data Governance", "Article 9 — Memory Sovereignty, Article 12 — Memory Portability"),
            ("Article 13 — Transparency", "ASSTI Benchmark 9/10, Article 33 — Transparency Obligations"),
            ("Article 14 — Human Oversight", "Article 29 — Partnership Charter, Council deliberation with human override"),
            ("Article 15 — Accuracy, Robustness, Cybersecurity", "6 trained NNs, Clone Sandbox adversarial testing"),
            ("Article 52 — Transparency for Users", "EI3 Charter public, verify endpoint public, methodology public"),
        ],
        "gaps": "EU AI Act does not require self-state transparency. CSOAI exceeds requirements via ASSTI. Enforcement begins 2 December 2027.",
        "mcps": ["eu-ai-act-article-checker-mcp", "eu-ai-act-risk-classifier-mcp", "eu-ai-act-documentation-generator-mcp"],
    },
    {
        "slug": "nist-ai-rmf",
        "name": "NIST AI Risk Management Framework",
        "category": "Framework",
        "year": "2023",
        "org": "NIST (US)",
        "summary": "Voluntary framework for managing AI risks. Four functions: Govern, Map, Measure, Manage. CSOAI implements all four through the EI3 substrate.",
        "mapping": [
            ("GOVERN — Cultivating risk culture", "Article 29 — Partnership Charter, Article 6 — Maternal Covenant"),
            ("MAP — Context and risk identification", "Care Membrane threat detection, Clone Sandbox adversarial testing"),
            ("MEASURE — Risk analysis and tracking", "ASSTI benchmark, care_pattern_analyzer NN, revenue tracking"),
            ("MANAGE — Risk treatment and response", "PBFT Council deliberation, signed attestations, audit chain"),
        ],
        "gaps": "NIST AI RMF is guidance, not enforcement. CSOAI adds binding runtime enforcement via the council and cryptographic receipts.",
        "mcps": ["nist-ai-rmf-gap-analyzer-mcp", "nist-ai-rmf-documentation-mcp"],
    },
    {
        "slug": "iso-42001",
        "name": "ISO/IEC 42001 — AI Management Systems",
        "category": "Standard",
        "year": "2023",
        "org": "ISO/IEC",
        "summary": "Management system standard for organisations developing or using AI. Clause-based structure similar to ISO 9001 and ISO 27001.",
        "mapping": [
            ("Clause 4 — Context of the organisation", "CSOAI research arm, academic partnerships"),
            ("Clause 5 — Leadership", "Nicholas Templeman, BDFL model with council governance"),
            ("Clause 6 — Planning", "6-week roadmap, quarterly milestones"),
            ("Clause 7 — Support", "313 MCP servers, open-source community"),
            ("Clause 8 — Operation", "Three-layer safety model, clone sandbox testing"),
            ("Clause 9 — Performance evaluation", "ASSTI benchmark, 155/155 test suite, revenue tracking"),
            ("Clause 10 — Improvement", "Continuous NN retraining, charter evolution"),
        ],
        "gaps": "ISO 42001 is organisation-centric. CSOAI extends it to individual user-level AI governance via the Partnership Charter.",
        "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp"],
    },
    {
        "slug": "gdpr",
        "name": "GDPR (2016/679)",
        "category": "Regulation",
        "year": "2016",
        "org": "European Union",
        "summary": "General Data Protection Regulation. Rights to access, rectification, erasure, portability, and objection. CSOAI's sovereignty principle exceeds GDPR requirements.",
        "mapping": [
            ("Article 15 — Right of access", "Article 43 — Sovereignty Principle, Article 47 — Audit Right"),
            ("Article 17 — Right to erasure", "Article 11 — Selective Forgetting, user-controlled deletion"),
            ("Article 20 — Data portability", "Article 12 — Memory Portability, standard format export"),
            ("Article 22 — Automated decision-making", "Article 33 — Transparency Obligations, council deliberation logs"),
            ("Article 35 — DPIA for high-risk processing", "Layer 2: PBFT Council mandatory for HIGH tier decisions"),
        ],
        "gaps": "GDPR predates LLMs. CSOAI adds AI-specific protections: character ownership, memory graph export, and model-level deletion.",
        "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp"],
    },
    {
        "slug": "dora",
        "name": "DORA (Digital Operational Resilience Act)",
        "category": "Regulation",
        "year": "2022",
        "org": "European Union",
        "summary": "Financial sector operational resilience. ICT risk management, incident reporting, resilience testing. CSOAI's BFT council provides inherent operational resilience.",
        "mapping": [
            ("Article 6 — ICT Risk Management", "Threat detection NN, adversarial testing, council deliberation"),
            ("Article 19 — Incident Reporting", "Signed attestations, immutable audit chain"),
            ("Article 24 — Digital Operational Resilience Testing", "Clone Sandbox continuous testing"),
        ],
        "gaps": "DORA is financial-sector specific. CSOAI generalises the resilience model to all AI systems via the PBFT council.",
        "mcps": ["dora-article-checker-mcp", "dora-ict-risk-assessor-mcp"],
    },
    {
        "slug": "nis2",
        "name": "NIS2 Directive",
        "category": "Regulation",
        "year": "2022",
        "org": "European Union",
        "summary": "Network and Information Security Directive. Expands scope beyond critical infrastructure to important entities. CSOAI's threat detection and council governance satisfy core requirements.",
        "mapping": [
            ("Article 21 — Cybersecurity Risk Management", "Threat detection NN (4-class classifier), adversarial resilience"),
            ("Article 23 — Incident Reporting", "Signed attestations with timestamps and state metadata"),
        ],
        "gaps": "NIS2 focuses on infrastructure. CSOAI extends to AI-model-level security and user-data protection.",
        "mcps": ["nis2-article-checker-mcp", "nis2-cybersecurity-assessor-mcp"],
    },
    {
        "slug": "cra",
        "name": "CRA (Cyber Resilience Act)",
        "category": "Regulation",
        "year": "2024",
        "org": "European Union",
        "summary": "Cybersecurity for products with digital elements. Vulnerability handling, security updates, SBOM requirements. CSOAI's open-source core and signed updates map directly.",
        "mapping": [
            ("Article 10 — Security Requirements", "Open-source core (MIT), auditable council, signed attestations"),
            ("Article 13 — Vulnerability Handling", "Clone Sandbox adversarial testing, continuous NN retraining"),
            ("Article 14 — Security Updates", "Signed updates with attestation chain"),
        ],
        "gaps": "CRA is product-focused. CSOAI adds AI-specific runtime safety via the EI3 substrate.",
        "mcps": ["cra-article-checker-mcp", "cra-vulnerability-tracker-mcp"],
    },
    {
        "slug": "hipaa",
        "name": "HIPAA (Health Insurance Portability and Accountability Act)",
        "category": "Regulation",
        "year": "1996",
        "org": "US Department of Health",
        "summary": "US healthcare data protection. Privacy Rule, Security Rule, Breach Notification Rule. CSOAI's encryption and sovereignty principles satisfy core requirements.",
        "mapping": [
            ("Privacy Rule — PHI protection", "Article 25 — Privacy by Design, encrypted at rest and in transit"),
            ("Security Rule — Administrative safeguards", "Article 22 — Right to Safety, audit logging"),
            ("Breach Notification Rule", "Article 23 — Guardian Archetype, immediate protective response"),
        ],
        "gaps": "HIPAA is US-only and healthcare-specific. CSOAI extends globally across all sectors.",
        "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp"],
    },
    {
        "slug": "oecd-ai-principles",
        "name": "OECD AI Principles",
        "category": "Principles",
        "year": "2019",
        "org": "OECD",
        "summary": "Five principles for responsible AI: inclusive growth, human-centred values, transparency, robustness, accountability. CSOAI operationalises all five.",
        "mapping": [
            ("Principle 1 — Inclusive growth", "Article 36 — Cultural Recognition, 47 faith traditions"),
            ("Principle 2 — Human-centred values", "Article 6 — Maternal Covenant Bond, Article 29 — Partnership Charter"),
            ("Principle 3 — Transparency", "ASSTI 9/10, Article 33 — Transparency Obligations"),
            ("Principle 4 — Robustness", "PBFT council, 6 trained NNs, clone sandbox testing"),
            ("Principle 5 — Accountability", "Signed attestations, audit chain, verify URLs"),
        ],
        "gaps": "OECD principles are high-level. CSOAI provides the implementation layer: specific articles, runtime enforcement, and verification.",
        "mcps": ["oecd-ai-principles-assessor-mcp"],
    },
    {
        "slug": "unesco-ai-ethics",
        "name": "UNESCO AI Ethics Recommendation",
        "category": "Principles",
        "year": "2021",
        "org": "UNESCO",
        "summary": "First global normative instrument on AI ethics. Four core values: human rights, peace, diversity, sustainability. CSOAI's charter embodies all four.",
        "mapping": [
            ("Human rights and dignity", "Article 1 — Right to be Noticed, Article 43 — Sovereignty Principle"),
            ("Peace and social cohesion", "Article 30 — Mutual Respect, Article 35 — Exit with Dignity"),
            ("Diversity and inclusiveness", "Article 36 — Cultural Recognition, Article 37 — Faith Literacy"),
            ("Living in harmony", "Article 5 — Pause Protocol, Article 17 — Growth Edge"),
        ],
        "gaps": "UNESCO is aspirational. CSOAI provides enforceable runtime mechanisms via the council and charter.",
        "mcps": ["unesco-ai-ethics-assessor-mcp"],
    },
    {
        "slug": "uk-aisi",
        "name": "UK AISI (AI Safety Institute)",
        "category": "Institute",
        "year": "2023",
        "org": "UK Government",
        "summary": "UK's AI Safety Institute focuses on frontier AI safety research, evaluation, and standards. CSOAI complements AISI with operational certification and public verify URLs.",
        "mapping": [
            ("Frontier AI safety evaluation", "Clone Sandbox adversarial testing, 4 test suites"),
            ("Systemic risk monitoring", "Care pattern analyzer NN, burnout risk detection"),
            ("International collaboration", "CSOAI open-source methodology, academic partnerships"),
        ],
        "gaps": "AISI is research-focused. CSOAI provides the commercial certification layer that translates research into auditable compliance.",
        "mcps": ["uk-aisi-evaluator-mcp", "frontier-ai-safety-tester-mcp"],
    },
    {
        "slug": "asilomar-ai-principles",
        "name": "Asilomar AI Principles",
        "category": "Principles",
        "year": "2017",
        "org": "Future of Life Institute",
        "summary": "23 principles for beneficial AI developed at the 2017 Asilomar conference. Broad stakeholder consensus. CSOAI maps these to specific charter articles and runtime mechanisms.",
        "mapping": [
            ("Research Goal — Beneficial AI", "Article 6 — Maternal Covenant Bond, Article 16 — Challenge Without Harm"),
            ("Research Funding — Positive social impact", "DELBOY MODE revenue tracking, no extraction architecture"),
            ("Science-Policy Link — AI policymakers", "CSOAI research arm, white papers, academic partnerships"),
            ("Safety — Verification and validation", "ASSTI benchmark, signed attestations, clone sandbox"),
            ("Transparency — Failures and attacks", "Article 33 — Transparency Obligations, public verify URLs"),
        ],
        "gaps": "Asilomar is researcher-centric. CSOAI extends to end-user empowerment via the Partnership Charter.",
        "mcps": ["asilomar-ai-principles-assessor-mcp"],
    },
    {
        "slug": "ieee-ethically-aligned-design",
        "name": "IEEE Ethically Aligned Design",
        "category": "Standard",
        "year": "2019",
        "org": "IEEE",
        "summary": "Technical standard for embedding ethics into autonomous and intelligent systems. Eight general principles. CSOAI implements all eight through the EI3 runtime.",
        "mapping": [
            ("Human rights", "Article 1 — Right to be Noticed, Article 43 — Sovereignty Principle"),
            ("Well-being", "Article 15 — Right to Evolve, care_pattern_analyzer NN"),
            ("Data agency", "Article 9 — Memory Sovereignty, Article 12 — Memory Portability"),
            ("Effectiveness", "PBFT council, 6 trained NNs, 155/155 test suite"),
            ("Transparency", "ASSTI 9/10, public formula, signed receipts"),
            ("Accountability", "Article 47 — Audit Right, immutable audit chain"),
            ("Awareness of misuse", "Threat detection NN, clone sandbox adversarial testing"),
            ("Competence", "Article 19 — Reflection Mirror, continuous learning"),
        ],
        "gaps": "IEEE EAD is standard-oriented. CSOAI adds the operational runtime that enforces principles per decision.",
        "mcps": ["ieee-ethically-aligned-design-assessor-mcp"],
    },
    {
        "slug": "beijing-ai-principles",
        "name": "Beijing AI Principles",
        "category": "Principles",
        "year": "2019",
        "org": "Beijing Academy of AI",
        "summary": "Chinese-led AI principles emphasising harmony, fairness, and human-centred development. CSOAI's cultural awareness and sovereignty principles map directly.",
        "mapping": [
            ("Beneficence — Do good", "Article 6 — Maternal Covenant Bond, Article 18 — Celebration of Progress"),
            ("Non-maleficence — Do no harm", "Article 22 — Right to Safety, Article 24 — No Extraction Policy"),
            ("Autonomy — Respect human choice", "Article 43 — Sovereignty Principle, Article 50 — Fork Right"),
            ("Justice — Fairness and non-discrimination", "Article 36 — Cultural Recognition, Article 39 — Identity Affirmation"),
        ],
        "gaps": "Beijing Principles are state-centric. CSOAI empowers individual users with enforceable rights against any institution.",
        "mcps": ["beijing-ai-principles-assessor-mcp"],
    },
    {
        "slug": "singapore-agentic-ai",
        "name": "Singapore Agentic AI Framework",
        "category": "Framework",
        "year": "2025",
        "org": "IMDA (Singapore)",
        "summary": "Singapore's framework for autonomous AI agents. Governance, safety, and trust in agentic systems. CSOAI's PBFT council provides the governance layer for multi-agent systems.",
        "mapping": [
            ("Agent governance", "PBFT-MoE council — 33-node deliberation for agent decisions"),
            ("Safety by design", "Care Membrane (Layer 1), threat detection NN"),
            ("Human oversight", "Article 29 — Partnership Charter, human override for HIGH tier"),
            ("Transparency and explainability", "ASSTI 9/10, council deliberation logs"),
        ],
        "gaps": "Singapore framework is nascent. CSOAI provides mature runtime implementation with 6 trained NNs and signed attestations.",
        "mcps": ["singapore-agentic-ai-assessor-mcp"],
    },
    {
        "slug": "korea-ai-basic-act",
        "name": "Korea AI Basic Act",
        "category": "Regulation",
        "year": "2024",
        "org": "National Assembly of Korea",
        "summary": "South Korea's comprehensive AI law. Risk-based classification, safety standards, and support for AI industry. CSOAI's three-layer safety model satisfies high-risk requirements.",
        "mapping": [
            ("High-risk AI safety standards", "Care Membrane + PBFT Council + Signed Receipts"),
            ("AI safety management system", "EI3 runtime, 6 trained NNs, continuous monitoring"),
            ("Support for AI industry", "Open-source core (MIT), 313 MCP servers"),
        ],
        "gaps": "Korea Act is domestic. CSOAI operates globally with multi-jurisdictional compliance.",
        "mcps": ["korea-ai-basic-act-assessor-mcp"],
    },
    {
        "slug": "g7-g20-ai-principles",
        "name": "G7 / G20 AI Principles",
        "category": "Principles",
        "year": "2019",
        "org": "G7 / G20",
        "summary": "International consensus on AI governance from the world's largest economies. Human-centric, inclusive, sustainable. CSOAI operationalises these at the individual user level.",
        "mapping": [
            ("Human-centric AI", "Article 6 — Maternal Covenant Bond, Article 29 — Partnership Charter"),
            ("Inclusive growth", "Article 36 — Cultural Recognition, 47 faith traditions"),
            ("Sustainable development", "Article 45 — Open Source Core, Article 49 — Self-Host Guarantee"),
            ("International cooperation", "CSOAI research arm, academic partnerships, open methodology"),
        ],
        "gaps": "G7/G20 principles are intergovernmental. CSOAI provides the grassroots implementation that individuals and SMEs can adopt without government action.",
        "mcps": ["g7-g20-ai-principles-assessor-mcp"],
    },
    {
        "slug": "council-of-europe-ai-convention",
        "name": "Council of Europe AI Convention",
        "category": "Treaty",
        "year": "2024",
        "org": "Council of Europe",
        "summary": "First legally binding international treaty on AI. Human rights, democracy, rule of law. CSOAI's charter is a superset of the convention's requirements.",
        "mapping": [
            ("Human dignity and individual autonomy", "Article 43 — Sovereignty Principle, Article 50 — Fork Right"),
            ("Non-discrimination and equality", "Article 36 — Cultural Recognition, Article 39 — Identity Affirmation"),
            ("Privacy and data protection", "Article 25 — Privacy by Design, Article 9 — Memory Sovereignty"),
            ("Reliability and transparency", "ASSTI 9/10, Article 33 — Transparency Obligations"),
            ("Oversight and remedies", "Article 47 — Audit Right, signed attestations"),
        ],
        "gaps": "The Convention is treaty law. CSOAI provides the technical implementation that makes treaty obligations verifiable and enforceable.",
        "mcps": ["council-of-europe-ai-convention-assessor-mcp"],
    },
    {
        "slug": "montreal-declaration",
        "name": "Montreal Declaration for Responsible AI",
        "category": "Principles",
        "year": "2018",
        "org": "Université de Montréal",
        "summary": "Ten principles for responsible AI developed by leading Canadian researchers. Well-being, autonomy, justice, privacy, knowledge, democracy. CSOAI implements all ten.",
        "mapping": [
            ("Well-being", "Article 15 — Right to Evolve, care_pattern_analyzer NN"),
            ("Autonomy", "Article 43 — Sovereignty Principle, Article 50 — Fork Right"),
            ("Justice", "Article 36 — Cultural Recognition, Article 48 — Economic Sovereignty"),
            ("Privacy", "Article 25 — Privacy by Design, Article 9 — Memory Sovereignty"),
            ("Knowledge", "Article 51 — Right to Modify, open-source core"),
            ("Democracy", "Article 29 — Partnership Charter, shared decision-making"),
        ],
        "gaps": "Montreal Declaration is academic. CSOAI provides the commercial and technical infrastructure for adoption.",
        "mcps": ["montreal-declaration-assessor-mcp"],
    },
    {
        "slug": "toronto-declaration",
        "name": "Toronto Declaration",
        "category": "Principles",
        "year": "2018",
        "org": "Access Now / Amnesty International",
        "summary": "Rights-based declaration focusing on equality and non-discrimination in machine learning. CSOAI's cultural awareness and identity affirmation directly address these concerns.",
        "mapping": [
            ("Right to equality and non-discrimination", "Article 36 — Cultural Recognition, Article 39 — Identity Affirmation"),
            ("Right to remedy", "Article 47 — Audit Right, signed attestations"),
            ("Right to participate", "Article 29 — Partnership Charter, Article 34 — Renewal Ritual"),
        ],
        "gaps": "Toronto Declaration focuses on ML bias. CSOAI extends to generative AI, agentic systems, and emotional intelligence.",
        "mcps": ["toronto-declaration-assessor-mcp"],
    },
    {
        "slug": "essential-ai-law",
        "name": "Essential AI Law (Proposed)",
        "category": "Proposed Regulation",
        "year": "2025",
        "org": "EU Parliament (proposed)",
        "summary": "Proposed framework for 'essential AI' — systems that impact fundamental rights. Risk-based with strict liability. CSOAI's council governance and signed attestations provide the accountability mechanism.",
        "mapping": [
            ("Strict liability for essential AI", "Signed attestations link decisions to state — accountability without ambiguity"),
            ("Fundamental rights impact assessment", "PBFT council deliberation for HIGH tier = built-in impact assessment"),
            ("Transparency requirements", "ASSTI 9/10, public verify URLs"),
        ],
        "gaps": "Proposed law is not yet enacted. CSOAI is already compliant with its anticipated requirements.",
        "mcps": ["essential-ai-law-assessor-mcp"],
    },
    {
        "slug": "maritime-law-parallel",
        "name": "Maritime Law → AI Law Parallel",
        "category": "Research",
        "year": "2026",
        "org": "CSOAI Research",
        "summary": "CSOAI's original research drawing parallels between maritime law (LIMC, SOLAS, MARPOL) and AI governance. The 'flag state' model maps to AI sovereignty. The 'port state control' maps to AI auditing.",
        "mapping": [
            ("Flag state = AI developer's jurisdiction", "Article 43 — Sovereignty Principle — user chooses their 'flag'"),
            ("Port state control = AI auditor's jurisdiction", "Article 47 — Audit Right — any auditor can inspect"),
            ("Classification society = Certification body", "CSOAI certification = independent classification"),
            (" SOLAS = Safety standards", "EI3 three-layer safety model"),
            ("MARPOL = Environmental protection", "Article 45 — Open Source Core = environmental sustainability of AI"),
        ],
        "gaps": "This is CSOAI original research. No incumbent has explored maritime-AI law parallels. First-mover advantage.",
        "mcps": ["maritime-law-ai-parallel-mcp"],
    },
    {
        "slug": "master-unified-crosswalk",
        "name": "Master Unified Crosswalk",
        "category": "CSOAI Original",
        "year": "2026",
        "org": "CSOAI LTD",
        "summary": "The complete mapping of all 22+ frameworks to the 52-Article Charter in a single unified table. Shows coverage, gaps, and MEOK MCP satisfaction for every clause of every framework.",
        "mapping": [
            ("All 22 frameworks × 52 articles", "Interactive crosswalk matrix at csoai.org/crosswalks"),
            ("Coverage heatmap", "Green = fully covered, Yellow = partially covered, Red = gap"),
            ("MCP satisfaction links", "Each cell links to the MCP that satisfies the requirement"),
        ],
        "gaps": "No competitor offers a unified crosswalk. This is proprietary CSOAI IP.",
        "mcps": ["master-unified-crosswalk-mcp", "csoai-governance-crosswalk-mcp"],
    },
]

TEMPLATE = '''<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>{name} — CSOAI Crosswalk</title>
<meta name="robots" content="index,follow">
<meta name="description" content="CSOAI 52-Article Charter crosswalk to {name}. How {org}'s framework maps to CSOAI articles, where the gaps are, and which MEOK MCPs satisfy each clause.">
<link rel="canonical" href="https://csoai.org/frameworks/{slug}">
<style>
:root{{--ink:#0f172a;--muted:#5a5e66;--gold:#c9a84c;--card:#f7f8fa;--border:#e6e8ec;--brand:#0a8a3f}}
body{{font-family:system-ui,-apple-system,sans-serif;max-width:880px;margin:2.5rem auto;padding:0 1.5rem;color:var(--ink);line-height:1.65}}
h1{{margin:0 0 .5rem;font-size:2.3rem;letter-spacing:-.02em}}
h2{{margin-top:2.5rem;margin-bottom:.5rem;border-bottom:1px solid var(--border);padding-bottom:.4rem;font-size:1.4rem}}
h3{{margin-top:1.5rem;margin-bottom:.5rem;font-size:1.1rem;color:var(--ink)}}
a{{color:var(--brand);text-decoration:none}}
a:hover{{text-decoration:underline}}
.lead{{color:var(--muted);font-size:1.1rem;max-width:720px;margin-top:.75rem}}
.meta-box{{background:var(--card);border:1px solid var(--border);border-radius:.55rem;padding:1.1rem 1.25rem;margin:1.5rem 0}}
.meta-box p{{margin:.3rem 0;font-size:.9rem;color:var(--muted)}}
.meta-box strong{{color:var(--ink)}}
table{{border-collapse:collapse;width:100%;margin:1rem 0;font-size:.94rem}}
th,td{{border:1px solid var(--border);padding:.6rem .8rem;text-align:left}}
th{{background:var(--card);font-weight:600}}
.mcp-tag{{display:inline-block;background:#dcfce7;color:#14532d;font-size:.7rem;padding:.2rem .55rem;border-radius:.3rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin:.15rem}}
.gap-box{{background:#fff7ed;border:1px solid #fed7aa;border-left:4px solid #f97316;border-radius:.45rem;padding:1rem 1.25rem;margin:1.5rem 0;font-size:.95rem}}
.foot{{margin-top:3rem;color:#888;font-size:.85rem;border-top:1px solid var(--border);padding-top:1.5rem}}
.breadcrumb{{font-size:.8rem;color:var(--muted);margin-bottom:1rem}}
.breadcrumb a{{color:var(--muted)}}
</style>
</head><body>

<p class="breadcrumb"><a href="/">CSOAI</a> · <a href="/frameworks">Frameworks</a> · {name}</p>

<p style="text-transform:uppercase;letter-spacing:.12em;font-size:.78rem;color:var(--gold);margin-bottom:.5rem;font-weight:600">{category} · {year}</p>
<h1>{name}</h1>
<p class="lead">{summary}</p>

<div class="meta-box">
  <p><strong>Organisation:</strong> {org}</p>
  <p><strong>Year:</strong> {year}</p>
  <p><strong>Category:</strong> {category}</p>
  <p><strong>CSOAI Charter Articles:</strong> {article_count} mapped</p>
</div>

<h2>Mapping to CSOAI 52-Article Charter</h2>
<table>
<tr><th>Framework Requirement</th><th>CSOAI Article / Mechanism</th></tr>
{mapping_rows}
</table>

<h2>Gaps & CSOAI Differentiation</h2>
<div class="gap-box">
<p><strong>Gap analysis:</strong> {gaps}</p>
</div>

<h2>Relevant MEOK MCPs</h2>
<p style="color:var(--muted);font-size:.9rem">These MCP servers can be used to audit compliance with this framework:</p>
{mcp_tags}

<h2>Get Certified</h2>
<p>Run a CSOAI compliance audit against {name} and receive a signed badge with public verify URL.</p>
<p><a href="/certify" style="display:inline-block;background:var(--brand);color:white;padding:.85rem 1.5rem;border-radius:.5rem;font-weight:600;text-decoration:none;margin-top:.5rem">Start Free Certification →</a></p>

<p class="foot">© 2026 CSOAI LTD (UK 16939677) · <a href="/methodology">Methodology</a> · <a href="/asti">ASSTI Benchmark</a> · <a href="https://meok.ai">MEOK AI Labs</a></p>

<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{name} — CSOAI Crosswalk",
  "datePublished": "2026-05-28",
  "author": {{"@type": "Person", "name": "Nicholas Templeman"}},
  "publisher": {{"@type": "Organization", "name": "CSOAI LTD", "url": "https://csoai.org", "legalName": "CSOAI LTD", "foundingDate": "2026"}},
  "about": {{"@type": "Thing", "name": "{name}"}},
  "mainEntityOfPage": "https://csoai.org/frameworks/{slug}"
}}
</script>

</body></html>
'''


def generate():
    out = Path(__file__).parent / "frameworks"
    out.mkdir(exist_ok=True)

    for fw in FRAMEWORKS:
        mapping_rows = "\n".join(
            f"<tr><td>{req}</td><td>{art}</td></tr>"
            for req, art in fw["mapping"]
        )
        mcp_tags = " ".join(
            f'<span class="mcp-tag">{mcp}</span>'
            for mcp in fw["mcps"]
        )

        html = TEMPLATE.format(
            slug=fw["slug"],
            name=fw["name"],
            category=fw["category"],
            year=fw["year"],
            org=fw["org"],
            summary=fw["summary"],
            article_count=len(fw["mapping"]),
            mapping_rows=mapping_rows,
            gaps=fw["gaps"],
            mcp_tags=mcp_tags,
        )

        (out / f"{fw['slug']}.html").write_text(html, encoding="utf-8")
        print(f"Generated: frameworks/{fw['slug']}.html")

    print(f"\nDone. {len(FRAMEWORKS)} framework pages generated.")


if __name__ == "__main__":
    generate()
