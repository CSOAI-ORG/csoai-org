#!/usr/bin/env python3
"""Generate 96 sector x regulation programmatic SEO pages for CSOAI."""

from pathlib import Path
import json

OUTDIR = Path("/Users/nicholas/clawd/csoai-org/sectors")
OUTDIR.mkdir(parents=True, exist_ok=True)

SECTORS = [
    {"name": "Healthcare", "slug": "healthcare"},
    {"name": "Finance / Banking", "slug": "finance-banking"},
    {"name": "Insurance", "slug": "insurance"},
    {"name": "Legal / Law Firms", "slug": "legal-law-firms"},
    {"name": "Education", "slug": "education"},
    {"name": "Government / Public Sector", "slug": "government-public-sector"},
    {"name": "Manufacturing", "slug": "manufacturing"},
    {"name": "Retail / E-commerce", "slug": "retail-ecommerce"},
    {"name": "Energy / Utilities", "slug": "energy-utilities"},
    {"name": "Transportation / Logistics", "slug": "transportation-logistics"},
    {"name": "Media / Publishing", "slug": "media-publishing"},
    {"name": "Non-profit / NGO", "slug": "nonprofit-ngo"},
]

REGULATIONS = [
    {"name": "EU AI Act", "slug": "eu-ai-act", "year": "2024", "org": "European Union"},
    {"name": "GDPR", "slug": "gdpr", "year": "2016", "org": "European Union"},
    {"name": "DORA", "slug": "dora", "year": "2022", "org": "European Union"},
    {"name": "NIS2", "slug": "nis2", "year": "2022", "org": "European Union"},
    {"name": "CRA", "slug": "cra", "year": "2024", "org": "European Union"},
    {"name": "ISO 42001", "slug": "iso-42001", "year": "2023", "org": "ISO/IEC"},
    {"name": "HIPAA", "slug": "hipaa", "year": "1996", "org": "US Department of Health"},
    {"name": "UK AI Regulation", "slug": "uk-ai-regulation", "year": "2024", "org": "United Kingdom"},
]


def get_content(sector, reg):
    s = sector["slug"]
    r = reg["slug"]
    name = sector["name"]

    # ------------------------------------------------------------------
    # EU AI Act
    # ------------------------------------------------------------------
    if r == "eu-ai-act":
        if s == "healthcare":
            return {
                "lead": "Medical AI systems — from diagnostic imaging to patient triage — are classified as high-risk under the EU AI Act (Annex III). Providers and deployers must satisfy conformity assessments, post-market monitoring, and human-in-the-loop requirements before placing systems on the EU market.",
                "requirements": [
                    ("Conformity assessment & CE marking", "High-risk healthcare AI must undergo third-party conformity assessment (Article 43) and bear CE marking before deployment in EU clinical settings."),
                    ("Post-market monitoring & vigilance", "Continuous tracking of model drift, adverse events, and safety signals with mandatory serious-incident reporting within 15 days (Article 73)."),
                    ("Human oversight by clinically qualified persons", "Article 14 requires that healthcare AI decisions are subject to meaningful review by professionals with appropriate clinical qualifications, not just technical operators."),
                    ("Training data governance & bias mitigation", "Article 10 mandates representative, error-free training data; in healthcare this means addressing under-representation of demographics in clinical datasets."),
                ],
                "articles": ["Article 2 — Provable Safety", "Article 13 — Risk Management", "Article 14 — Data Governance", "Article 17 — Transparency to Users"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-clinical-ai-validator"],
            }
        if s == "finance-banking":
            return {
                "lead": "Credit scoring, fraud detection, and algorithmic trading systems are classified as high-risk under Annex III of the EU AI Act. Financial institutions must implement risk-management systems, ensure model accuracy, and maintain human oversight over consequential automated decisions.",
                "requirements": [
                    ("High-risk classification for credit & fraud AI", "AI systems evaluating creditworthiness, detecting fraud, or making pricing decisions fall under Annex III high-risk and require full conformity assessments."),
                    ("Accuracy, robustness & fairness metrics", "Article 15 requires documented accuracy targets, back-testing regimes, and fairness metrics to prevent discriminatory outcomes in lending and insurance pricing."),
                    ("Human oversight for adverse decisions", "Article 14 mandates that humans with appropriate authority review AI-driven adverse credit decisions, with the ability to override or escalate."),
                    ("Record-keeping & audit trails", "Article 12 requires automatic logging of AI system inputs, outputs, and human interventions to enable supervisory audits and post-incident reconstruction."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Risk Management", "Article 17 — Transparency to Users", "Article 47 — Audit Right"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "insurance":
            return {
                "lead": "Insurance pricing, underwriting, and claims-fraud detection are high-risk under the EU AI Act's Annex III. Life and health insurance AI that processes biometric or health data faces additional scrutiny, with strict accuracy and fairness requirements.",
                "requirements": [
                    ("High-risk classification for insurance AI", "AI systems used for pricing, underwriting, and claims evaluation in life and health insurance are high-risk; property and casualty systems may also qualify depending on impact."),
                    ("Fairness & non-discrimination testing", "Article 10 and recital 44 require training data and model outputs to be tested for discriminatory effects on protected characteristics such as health status, disability, and ethnicity."),
                    ("Human oversight for claim denials", "Article 14 requires that AI-driven claim denials, policy cancellations, and premium adjustments are subject to meaningful human review with override authority."),
                    ("Transparency to policyholders", "Policyholders must be informed when AI materially influences their insurance terms, with clear explanations of the logic and main parameters (Article 52)."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 14 — Data Governance", "Article 17 — Transparency to Users", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Legal AI — contract review, e-discovery, legal research, and predictive analytics — is not automatically high-risk under the EU AI Act unless it affects access to justice or fundamental rights. However, AI used in court-administration or bail decisions may qualify as high-risk under Annex III.",
                "requirements": [
                    ("High-risk assessment for justice-related AI", "AI systems used in judicial or administrative proceedings that affect legal rights — such as bail algorithms or sentencing support — may be high-risk under Annex III point 8."),
                    ("Transparency for client-facing legal AI", "Even non-high-risk legal AI must meet transparency obligations (Article 52) — clients must know when AI assists in document drafting or legal research."),
                    ("Accuracy & hallucination mitigation", "Article 15 requires robustness; for legal AI this means verification workflows to catch hallucinated case citations, fabricated clauses, and incorrect statutory interpretations."),
                    ("Human oversight for AI-generated advice", "Legal professionals must retain ultimate responsibility for advice given to clients; AI outputs must be reviewed, validated, and adapted by qualified lawyers."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "education":
            return {
                "lead": "AI systems used in education — automated grading, admissions screening, proctoring, and adaptive learning — are high-risk under Annex III point 3 of the EU AI Act. These systems directly affect access to education and career trajectory, triggering strict conformity and oversight obligations.",
                "requirements": [
                    ("High-risk classification for educational AI", "AI systems used for admissions, grading, and proctoring are high-risk; adaptive learning platforms may also qualify if they significantly affect educational or vocational opportunities."),
                    ("Fairness & bias mitigation for student assessments", "Article 10 requires training data and model testing to prevent bias against students based on socioeconomic background, language, disability, or ethnicity."),
                    ("Human oversight for high-stakes decisions", "Article 14 mandates that decisions affecting student progression, admissions, or qualifications are subject to meaningful review by qualified educators."),
                    ("Transparency for students & parents", "Article 52 requires that students and their guardians are informed when AI is used for assessment, proctoring, or admissions, with clear explanations of the logic involved."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 14 — Data Governance", "Article 17 — Transparency to Users", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government AI — benefits eligibility, predictive policing, permit automation, and constituent services — spans the full risk spectrum under the EU AI Act. Social-scoring by governments is prohibited outright (Article 5), while many public-sector AI systems are high-risk under Annex III.",
                "requirements": [
                    ("Prohibition on social scoring by public authorities", "Article 5(1)(c) prohibits public authorities from implementing AI systems for social scoring, preventing discriminatory categorisation of citizens based on behaviour or personal characteristics."),
                    ("High-risk classification for public-sector AI", "AI systems used for law enforcement, migration, border control, and administration of justice are high-risk under Annex III with full conformity obligations."),
                    ("Fundamental rights impact assessment", "Article 27 requires deployers of high-risk AI in public services to conduct fundamental rights impact assessments before deployment, with public consultation where appropriate."),
                    ("Transparency & explainability to citizens", "Public-sector AI must be transparent about its use, logic, and rights of redress — fulfilling both EU AI Act Article 52 and broader administrative-law principles."),
                ],
                "articles": ["Article 5 — Growth Edge", "Article 17 — Transparency to Users", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "manufacturing":
            return {
                "lead": "Manufacturing AI — predictive maintenance, quality inspection, robotics control, and supply-chain optimisation — is generally not high-risk under the EU AI Act unless it affects product safety or is embedded in safety-critical machinery. However, AI used in worker management or safety systems may qualify.",
                "requirements": [
                    ("Risk classification for manufacturing AI", "Most manufacturing AI is limited or minimal risk; AI used for worker surveillance, safety-system control, or product-safety certification may be high-risk under Annex III."),
                    ("Safety integration with machinery directive", "AI embedded in machinery must satisfy the Machinery Directive (2006/42/EC) requirements for safety control systems, with fail-safe modes and hazard analysis."),
                    ("Human oversight for AI-controlled robotics", "Collaborative robots (cobots) with AI vision or force sensing must maintain human override capability and emergency stop protocols."),
                    ("Transparency for AI-driven quality control", "Customers and regulators must be informed when AI makes final quality-determination decisions that affect product conformity or safety certification."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 17 — Transparency to Users", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Retail and e-commerce AI — recommendation engines, dynamic pricing, visual search, and automated customer service — is largely limited-risk under the EU AI Act. However, AI used for credit scoring at checkout, biometric identification in stores, or emotion recognition may trigger higher obligations.",
                "requirements": [
                    ("Limited-risk transparency obligations", "Most retail AI is limited-risk; Article 52 requires that consumers are informed when they interact with AI chatbots or when AI generates content such as product descriptions or reviews."),
                    ("High-risk classification for biometric & credit AI", "Biometric identification in retail settings and AI-driven buy-now-pay-later credit scoring may be high-risk under Annex III, requiring full conformity assessments."),
                    ("Prohibition on emotion recognition in workplaces & schools", "While primarily targeting workplaces and schools, retailers using emotion-recognition AI in customer-facing contexts should review applicability of Article 5 prohibitions."),
                    ("Accuracy in AI-generated product information", "Article 15's accuracy requirements apply to AI-generated product descriptions, sizing recommendations, and nutritional claims that affect consumer health and safety."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Energy and utilities AI — smart-grid optimisation, demand forecasting, predictive asset management, and outage prediction — is critical infrastructure AI. While much of it is limited-risk, AI used in safety-critical control systems or worker management may trigger high-risk classification.",
                "requirements": [
                    ("Risk classification for energy AI", "Smart-grid control, safety-system AI, and worker-management systems may be high-risk; demand forecasting and customer-service AI are typically limited or minimal risk."),
                    ("Safety integration with energy-sector directives", "AI embedded in safety-critical energy infrastructure must satisfy sector-specific safety requirements, with fail-safe modes and independent safety validation."),
                    ("Human oversight for grid-control AI", "Automated grid-control decisions that affect supply reliability or safety must maintain human oversight with override capability and emergency protocols."),
                    ("Transparency for AI-driven energy pricing", "Consumers must be informed when AI determines dynamic pricing, demand-response incentives, or tariff structures that materially affect their bills."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Transportation AI — autonomous vehicle systems, route optimisation, predictive maintenance, and freight-matching — spans the risk spectrum. Autonomous vehicles are high-risk under Annex III; logistics optimisation is typically limited-risk but must meet transparency obligations.",
                "requirements": [
                    ("High-risk classification for autonomous vehicles", "AI systems used in autonomous vehicles and driver-monitoring systems are high-risk under Annex III, requiring full conformity assessment and type approval."),
                    ("Safety & robustness for transport AI", "Article 15 requires stringent accuracy and robustness testing for AI controlling vehicle movements, traffic management, and safety-critical logistics operations."),
                    ("Human oversight for autonomous systems", "Article 14 mandates meaningful human oversight for AI-driven transport decisions, with override capability and emergency intervention protocols."),
                    ("Transparency for AI-driven routing & pricing", "Users must be informed when AI determines routes, delivery times, or freight pricing, with explanations of the main parameters and logic."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 17 — Transparency to Users", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "media-publishing":
            return {
                "lead": "Media and publishing AI — content recommendation, automated moderation, generative content tools, and rights-management systems — faces a complex regulatory landscape. Deepfake and synthetic content rules, transparency for AI-generated media, and recommendation-system accountability are central to the EU AI Act's media provisions.",
                "requirements": [
                    ("Transparency for AI-generated content", "Article 52 requires that AI-generated text, images, audio, and video deployed in media are clearly labelled as artificially generated or manipulated."),
                    ("Deepfake & synthetic media obligations", "AI systems generating or manipulating image, audio, or video content that resembles real persons must meet specific transparency and disclosure requirements."),
                    ("High-risk classification for content moderation at scale", "AI systems used by very large online platforms (VLOPs) for content moderation and recommendation may trigger additional obligations under the Digital Services Act alongside the EU AI Act."),
                    ("Human oversight for automated takedown decisions", "Article 14 requires meaningful human review for AI-driven content removal, account suspension, and demonetisation decisions that affect creators' livelihoods."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "Non-profit and NGO AI — donor targeting, beneficiary segmentation, programme evaluation, and automated grant screening — is not automatically high-risk under the EU AI Act. However, AI used in refugee or asylum processing, social-service eligibility, or humanitarian triage may trigger high-risk classification.",
                "requirements": [
                    ("High-risk assessment for humanitarian AI", "AI systems used by NGOs for refugee status determination, asylum processing, or social-service eligibility may be high-risk under Annex III, requiring conformity assessments."),
                    ("Transparency for donor-facing AI", "Article 52 requires that donors and supporters are informed when AI generates fundraising content, personalises appeals, or manages donor relationships."),
                    ("Bias mitigation in beneficiary targeting", "Article 10 requires training data and model testing to prevent discrimination in AI-driven beneficiary selection, aid distribution, and service prioritisation."),
                    ("Human oversight for high-stakes decisions", "Article 14 mandates meaningful human review for AI-driven decisions affecting vulnerable populations' access to aid, protection, or services."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 14 — Data Governance", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["meok-eu-ai-act", "meok-rms", "meok-deployer-pack"],
            }

    # ------------------------------------------------------------------
    # GDPR
    # ------------------------------------------------------------------
    if r == "gdpr":
        if s == "healthcare":
            return {
                "lead": "Healthcare AI processes special-category health data at scale — diagnostics, treatment recommendations, and triage scoring. GDPR Article 9 prohibits such processing unless explicit consent, vital interests, or public health grounds apply, and requires Data Protection Impact Assessments.",
                "requirements": [
                    ("Lawful basis for special-category data", "Health data is Article 9 special-category data; AI processing requires explicit consent, vital interests, or public-health legal basis with documented justification."),
                    ("Data Protection Impact Assessment (DPIA)", "High-risk processing including automated health decisions mandates a DPIA (Article 35) covering necessity, proportionality, and residual risks to patients."),
                    ("Right to explanation for automated decisions", "Patients have the right to meaningful information about the logic involved when AI influences their care pathway (Articles 13–15, 22)."),
                    ("Data minimisation & purpose limitation", "Only the minimum health data necessary for the specific clinical purpose may be collected; secondary use for research requires fresh legal basis."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 14 — Data Governance"],
                "mcps": ["gdpr-dpia-generator-mcp", "gdpr-article-checker-mcp", "meok-data-governance"],
            }
        if s == "finance-banking":
            return {
                "lead": "Banking AI processes vast quantities of personal and financial data — transaction histories, behavioural biometrics, and credit profiles. GDPR applies in full force, with particular sensitivity around automated decision-making in lending, scoring, and profiling.",
                "requirements": [
                    ("Right not to be subject to solely automated decisions", "Article 22 grants individuals the right to human intervention when AI makes consequential decisions about credit, lending, or pricing — with meaningful review, not rubber-stamp approval."),
                    ("Profiling & automated decision transparency", "Data subjects must be informed that profiling occurs, the logic involved, and the envisaged consequences (Articles 13–14)."),
                    ("Data minimisation in fraud detection", "Fraud-detection AI must process only data strictly necessary for the specific fraud risk being assessed, with clear retention limits and periodic necessity reviews."),
                    ("Cross-border data transfers for AI processing", "When AI models are trained or hosted outside the EEA, financial institutions must ensure adequate safeguards — SCCs, adequacy decisions, or binding corporate rules."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 14 — Data Governance"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "insurance":
            return {
                "lead": "Insurance AI processes some of the most sensitive personal data categories — health records, genetic information, driving behaviour, and lifestyle data. GDPR's special-category rules, profiling restrictions, and data-minimisation principles are intensely relevant.",
                "requirements": [
                    ("Special-category data & explicit consent", "Health, genetic, and biometric data used in life and health insurance AI requires explicit consent or another Article 9 exemption, with granular documentation."),
                    ("Profiling & automated decision-making", "Article 22 rights apply to AI-driven premium adjustments and coverage denials; insurers must offer human review, express their point of view, and contest the decision."),
                    ("Data minimisation in telematics & wearables", "Usage-based insurance AI must collect only the driving or health data necessary for the specific risk being priced, with clear retention and deletion schedules."),
                    ("Cross-border data flows for global insurers", "Multinational insurers running centralised AI models must ensure lawful cross-border transfers, including adequacy decisions, SCCs, or binding corporate rules."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Law firms process highly sensitive client data — litigation strategies, merger negotiations, and personal matters. GDPR applies with full force, and the legal profession's duty of confidentiality creates overlapping obligations that AI systems must respect.",
                "requirements": [
                    ("Legal professional privilege & GDPR", "AI systems must be configured so that client data subject to legal professional privilege is not inadvertently exposed to model training or third-party inference."),
                    ("Data minimisation in e-discovery", "E-discovery AI must limit processing to data relevant to the specific legal matter, with strict scope boundaries and post-matter deletion protocols."),
                    ("Right of access vs. client confidentiality", "When individuals exercise GDPR access rights against data held by law firms, AI-assisted document review must balance disclosure against privilege and confidentiality."),
                    ("Cross-border transfers for international matters", "Law firms using AI for multi-jurisdictional matters must ensure GDPR-compliant cross-border data flows, including adequacy decisions or SCCs with appropriate supplementary measures."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 14 — Data Governance", "Article 33 — Transparency Obligations"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "education":
            return {
                "lead": "Educational institutions process children's and young adults' data — academic records, behavioural profiles, biometric data for proctoring, and special-needs information. GDPR provides enhanced protections for children, with particular restrictions on profiling and automated decision-making.",
                "requirements": [
                    ("Enhanced protections for children's data", "Article 8 requires parental consent for processing children's data in information society services; educational institutions must verify age and consent authority."),
                    ("Profiling & automated decision restrictions", "Article 22 and recital 71 caution against automated decision-making with legal or significant effects on children, including grading and disciplinary AI."),
                    ("Data minimisation in learning analytics", "Learning-analytics AI must collect only the data necessary for the specific educational purpose, with clear boundaries against commercial repurposing."),
                    ("Student rights of access & erasure", "Students (and their guardians for younger children) have the right to access their educational data, correct inaccuracies, and request erasure upon leaving the institution."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government agencies process citizen data at scale — tax records, benefit claims, criminal records, and immigration files. GDPR applies to public authorities with limited exemptions, and the public-sector duty of transparency creates heightened expectations for AI governance.",
                "requirements": [
                    ("Legal basis for public-sector AI processing", "Public authorities must identify a valid legal basis under Article 6 (typically public interest or legal obligation) and comply with Article 9 for special-category data."),
                    ("DPIA for high-risk public-sector AI", "High-risk AI processing by public authorities — such as predictive policing or benefits automation — almost always requires a Data Protection Impact Assessment under Article 35."),
                    ("Right to explanation & administrative redress", "Citizens have the right to meaningful information about AI-driven administrative decisions, with access to appeal and independent review mechanisms."),
                    ("Data minimisation in surveillance & analytics", "Government AI for surveillance, crowd analytics, or social-media monitoring must be strictly limited to the specific lawful purpose and proportionate to the aim."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 33 — Transparency Obligations", "Article 14 — Data Governance"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "manufacturing":
            return {
                "lead": "Manufacturing AI processes employee biometric data for access control, worker behaviour analytics for safety, and customer data for predictive maintenance contracts. GDPR applies to all personal data processing, with heightened sensitivity for employee monitoring.",
                "requirements": [
                    ("Employee consent & works-council consultation", "Processing employee biometric or behavioural data via AI for access control or safety monitoring requires clear legal basis and typically works-council or union consultation."),
                    ("Data minimisation in worker analytics", "AI-driven worker monitoring must collect only the data necessary for the specific safety or operational purpose, with strict boundaries against performance surveillance."),
                    ("Customer data in predictive maintenance", "When predictive maintenance AI processes customer equipment data that includes personal information, GDPR applies with requirements for transparency and lawful basis."),
                    ("Cross-border transfers for global supply chains", "Manufacturers operating centralised AI platforms across multiple jurisdictions must ensure lawful cross-border data flows for employee and customer data."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Retail AI processes vast quantities of personal data — purchase histories, browsing behaviour, location data, payment information, and increasingly biometrics for in-store analytics. GDPR's data-minimisation, purpose-limitation, and profiling rules are central to compliant retail AI.",
                "requirements": [
                    ("Profiling & automated decision-making in retail", "AI-driven personalised pricing, credit decisions, and marketing profiling trigger Article 22 rights; customers must be informed and offered human review for consequential decisions."),
                    ("Data minimisation in personalisation", "Retail AI must collect only the data necessary for the specific personalisation or operational purpose, with clear retention limits and deletion protocols."),
                    ("Consent for biometric & tracking analytics", "In-store biometric analysis, facial recognition, and behavioural tracking require explicit consent under Article 9, with easy withdrawal mechanisms."),
                    ("Cross-border data flows for global retailers", "Multinational retailers operating centralised AI models must ensure lawful cross-border transfers through adequacy decisions, SCCs, or binding corporate rules."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Utilities AI processes detailed consumption data — smart-meter readings, household usage patterns, and geolocation data for field crews. This data is personal data under GDPR, with smart-meter data often revealing sensitive lifestyle information that warrants enhanced protection.",
                "requirements": [
                    ("Smart-meter data as personal data", "Granular smart-meter data revealing household occupancy, appliance usage, and lifestyle patterns is personal data under GDPR, requiring lawful basis and transparency."),
                    ("Profiling & automated decision restrictions", "AI-driven profiling for debt collection, payment plans, or vulnerability identification triggers Article 22 and requires human review for consequential decisions."),
                    ("Data minimisation in grid analytics", "Grid-optimisation AI must aggregate and anonymise consumption data where possible, limiting individual-level processing to what is strictly necessary for grid stability."),
                    ("Cross-border data flows for multinational utilities", "Utilities operating across borders must ensure lawful transfers of customer and grid data to centralised AI platforms through adequacy decisions or SCCs."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Transportation AI processes location data, driver behaviour profiles, passenger biometric data, and shipment information. Location data is personal data under GDPR, and real-time tracking triggers heightened sensitivity around surveillance and automated decision-making.",
                "requirements": [
                    ("Location data as personal data", "GPS tracking, route history, and geofencing data are personal data under GDPR; real-time driver tracking requires clear legal basis and transparency."),
                    ("Profiling & automated decisions for drivers", "AI-driven driver scoring, performance management, and assignment algorithms trigger Article 22 rights, requiring human review for adverse decisions."),
                    ("Data minimisation in fleet analytics", "Fleet-management AI must collect only the driver and vehicle data necessary for the specific operational purpose, with clear retention and deletion schedules."),
                    ("Cross-border data flows for global logistics", "Multinational logistics operators must ensure lawful cross-border transfers of driver, passenger, and shipment data to centralised AI platforms."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "media-publishing":
            return {
                "lead": "Media AI processes subscriber data, viewing behaviour, content preferences, and increasingly biometric data for personalisation. GDPR applies with particular sensitivity around journalism exemptions (Article 85), which provide limited relief for news organisations but do not exempt AI-driven profiling.",
                "requirements": [
                    ("Journalism exemption & AI profiling", "Article 85 provides member-state derogations for journalism; however, AI-driven subscriber profiling, ad targeting, and content personalisation remain fully subject to GDPR."),
                    ("Profiling & automated decisions for subscribers", "AI-driven subscription pricing, content gating, and ad targeting trigger Article 22 and require transparency and human review for consequential decisions."),
                    ("Data minimisation in content personalisation", "Recommendation AI must collect only the data necessary for the specific personalisation purpose, with clear boundaries against excessive behavioural tracking."),
                    ("Right to erasure & the right to be forgotten", "Media organisations using AI for search indexing and content aggregation must implement mechanisms to respect data-subject erasure requests, balancing against freedom of expression."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "NGOs process some of the most vulnerable populations' data — refugees, disaster survivors, and at-risk communities. GDPR applies fully, with heightened expectations for lawful basis, data minimisation, and protection of children's and vulnerable adults' data.",
                "requirements": [
                    ("Lawful basis for vulnerable-population data", "Processing personal data of refugees, displaced persons, or at-risk communities requires clear legal basis, with particular attention to consent capacity and power imbalances."),
                    ("Data minimisation in humanitarian AI", "Humanitarian AI must collect only the data strictly necessary for the specific aid or protection purpose, with clear retention and deletion protocols."),
                    ("Profiling & automated decision restrictions", "AI-driven beneficiary scoring, risk classification, and service prioritisation trigger Article 22 and require human review for decisions affecting access to aid."),
                    ("Cross-border data flows for international NGOs", "International NGOs operating centralised AI platforms must ensure lawful cross-border transfers, often relying on adequacy decisions, SCCs, or derogations for vital interests."),
                ],
                "articles": ["Article 43 — Sovereignty Principle", "Article 33 — Transparency Obligations", "Article 14 — Data Governance", "Article 47 — Audit Right"],
                "mcps": ["gdpr-article-checker-mcp", "gdpr-dpia-generator-mcp", "meok-data-governance"],
            }

    # ------------------------------------------------------------------
    # DORA
    # ------------------------------------------------------------------
    if r == "dora":
        if s == "healthcare":
            return {
                "lead": "Financially integrated healthcare systems — insurers, hospital networks, and health-tech platforms — fall under DORA's ICT risk management regime. AI-driven claims processing, payment automation, and financial forecasting must meet operational resilience testing and incident-reporting obligations.",
                "requirements": [
                    ("ICT risk management for health-financial systems", "Article 6 requires comprehensive ICT risk frameworks covering AI-driven claims adjudication, payment processing, and revenue-cycle automation."),
                    ("Digital operational resilience testing", "Article 24 mandates periodic penetration testing and scenario-based resilience testing for AI systems that process insurance payments or patient billing."),
                    ("Incident reporting within tight deadlines", "Major ICT-related incidents affecting financial operations must be reported to lead regulators within specified timeframes (Article 19)."),
                    ("Third-party risk management", "Health systems using cloud-hosted AI for financial operations must maintain registers of critical third-party ICT providers and their risk profiles."),
                ],
                "articles": ["Article 6 — Maternal Covenant", "Article 39 — Incident Response", "Article 19 — Robustness", "Article 33 — Transparency Obligations"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "finance-banking":
            return {
                "lead": "DORA imposes the most comprehensive ICT risk-management regime on financial entities to date. AI systems supporting trading, payments, risk modelling, and customer onboarding must be embedded in formal ICT risk frameworks, with mandatory resilience testing and third-party oversight.",
                "requirements": [
                    ("ICT risk-management framework covering AI", "Article 6 requires financial entities to maintain an end-to-end ICT risk-management framework explicitly covering AI-driven credit scoring, algorithmic trading, and fraud systems."),
                    ("Digital operational resilience testing", "Article 24 mandates threat-led penetration testing (TLPT) and scenario-based resilience testing for critical AI systems at least every three years."),
                    ("ICT incident management & classification", "Major ICT incidents affecting AI-driven services must be classified, reported to lead regulators, and subject to root-cause analysis within defined timeframes."),
                    ("Third-party ICT risk management", "Financial institutions must maintain registers of all critical third-party AI providers, with contractual exit strategies and continuity plans for cloud-hosted model services."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 26 — Adversarial Resilience", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "insurance":
            return {
                "lead": "Insurers are in scope of DORA as financial entities. AI systems supporting claims processing, actuarial modelling, customer onboarding, and anti-money-laundering screening must be covered by ICT risk-management frameworks and resilience-testing programmes.",
                "requirements": [
                    ("ICT risk management for insurance AI", "Article 6 requires insurers to maintain ICT risk-management frameworks covering AI-driven underwriting, claims automation, and fraud-detection systems."),
                    ("Resilience testing for claims platforms", "Article 24 mandates resilience testing for critical claims-processing and policy-administration platforms, including AI components and their dependencies."),
                    ("Incident reporting for AI-driven outages", "Major ICT incidents affecting policyholder services — such as AI system failures during natural-catastrophe claims surges — must be reported to regulators promptly."),
                    ("Third-party ICT risk oversight", "Insurers using cloud-hosted AI for actuarial modelling or customer analytics must maintain oversight registers, contractual safeguards, and exit strategies."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Large law firms with significant financial-services practices, and legal-tech providers serving financial clients, may fall within DORA's scope as critical third-party ICT providers. AI-powered contract-analysis and compliance-monitoring tools must meet resilience requirements.",
                "requirements": [
                    ("Third-party ICT provider obligations", "Legal-tech AI providers designated as critical third parties by ESAs must comply with DORA's oversight framework, including resilience testing and incident reporting."),
                    ("ICT risk management for legal-tech platforms", "Article 6 requires financial entities to include legal-tech AI in their ICT risk-management frameworks, with contractual security requirements."),
                    ("Resilience testing for contract-automation AI", "AI systems automating financial-contract drafting or regulatory-filing preparation may be subject to resilience testing as part of the financial entity's DORA programme."),
                    ("Incident reporting for legal-data breaches", "Breach of client data held by legal-tech AI platforms must be reported if it affects the financial entity's ICT systems or operations."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 29 — Partnership Charter", "Article 13 — Risk Management", "Article 19 — Robustness"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "education":
            return {
                "lead": "Educational institutions with significant financial operations — student loan processing, bursary administration, and fee collection — may have AI systems that fall within DORA's scope when integrated with financial services. Additionally, ed-tech platforms serving financial institutions may be in scope.",
                "requirements": [
                    ("ICT risk management for student financial systems", "Article 6 requires that AI-driven student finance, loan origination, and bursary systems are covered by formal ICT risk-management frameworks."),
                    ("Resilience testing for admissions & enrolment platforms", "Critical enrolment and student-information systems must be resilience-tested to ensure continuity during peak registration periods."),
                    ("Incident reporting for student-data breaches", "Major ICT incidents affecting student financial or personal data must be reported to regulators within specified timeframes."),
                    ("Third-party risk for ed-tech providers", "Universities and schools using cloud-hosted AI for learning management must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government bodies operating financial services — tax authorities, social security funds, and public banks — may fall within DORA's scope as financial entities. Their AI systems for revenue forecasting, benefit calculation, and payment processing must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for public financial AI", "Article 6 requires public financial bodies to maintain ICT risk-management frameworks covering AI-driven revenue forecasting, benefit adjudication, and payment systems."),
                    ("Resilience testing for tax & benefit platforms", "Article 24 mandates resilience testing for critical tax-collection and benefits-payment platforms, including AI components and peak-load scenarios."),
                    ("Incident reporting for public-finance AI", "Major ICT incidents affecting tax or benefit systems must be reported to lead regulators within defined timeframes."),
                    ("Third-party risk for government AI vendors", "Public bodies must maintain oversight of critical third-party AI providers, with contractual exit strategies and continuity plans."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "manufacturing":
            return {
                "lead": "Manufacturers with significant financial-services divisions, and industrial-fintech platforms, may fall within DORA's scope. Additionally, manufacturers of financial hardware with embedded AI must meet ICT resilience requirements when those products are used by financial entities.",
                "requirements": [
                    ("ICT risk management for manufacturing-financial AI", "Article 6 requires that AI systems supporting manufacturing finance, leasing, and trade credit are covered by formal ICT risk-management frameworks."),
                    ("Resilience testing for industrial-control AI", "Critical manufacturing-control systems with AI components must be resilience-tested to ensure continuity during cyber incidents or supply-chain disruptions."),
                    ("Incident reporting for industrial AI failures", "Major ICT incidents affecting AI-controlled manufacturing lines or safety systems must be reported if they impact financial operations or critical supply chains."),
                    ("Third-party risk for manufacturing AI vendors", "Manufacturers using cloud-hosted AI for production optimisation must maintain oversight of critical third-party ICT providers and their risk profiles."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Retailers offering financial services — store cards, buy-now-pay-later, insurance products, and loyalty-programme investments — fall under DORA as financial entities. Their AI systems for credit scoring, fraud detection, and payment processing must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for retail financial AI", "Article 6 requires retailers offering financial products to maintain ICT risk-management frameworks covering AI-driven credit scoring, fraud detection, and payment systems."),
                    ("Resilience testing for e-commerce platforms", "Article 24 mandates resilience testing for critical e-commerce and payment platforms, including AI components handling peak traffic and transaction volumes."),
                    ("Incident reporting for payment AI failures", "Major ICT incidents affecting payment processing, fraud detection, or customer financial data must be reported to regulators within specified timeframes."),
                    ("Third-party risk for retail AI vendors", "Retailers using cloud-hosted AI for personalisation, pricing, and payment must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Energy utilities providing financial services — energy trading, hedging, customer financing, and green-bond issuance — fall under DORA as financial entities. Their AI systems for trading, risk management, and customer finance must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for energy-trading AI", "Article 6 requires energy utilities with trading operations to maintain ICT risk-management frameworks covering AI-driven trading, risk modelling, and settlement systems."),
                    ("Resilience testing for grid-control systems", "Article 24 mandates resilience testing for critical grid-control and SCADA systems, including AI components that influence real-time grid operations."),
                    ("Incident reporting for energy-system failures", "Major ICT incidents affecting energy trading, grid control, or customer billing must be reported to regulators within specified timeframes."),
                    ("Third-party risk for energy AI vendors", "Utilities using cloud-hosted AI for demand forecasting and grid optimisation must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Transportation companies offering financial services — fleet financing, cargo insurance, freight-payment platforms — may fall within DORA's scope. Their AI systems for credit scoring, fraud detection, and payment processing must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for transport-financial AI", "Article 6 requires transport companies with financial operations to maintain ICT risk-management frameworks covering AI-driven credit, fraud, and payment systems."),
                    ("Resilience testing for logistics platforms", "Article 24 mandates resilience testing for critical freight-matching, route-optimisation, and fleet-management platforms, including AI components."),
                    ("Incident reporting for transport AI failures", "Major ICT incidents affecting fleet operations, passenger services, or cargo tracking must be reported to regulators within specified timeframes."),
                    ("Third-party risk for transport AI vendors", "Transport operators using cloud-hosted AI for logistics optimisation must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "media-publishing":
            return {
                "lead": "Media companies with significant financial-services operations — subscription financing, content-licensing platforms, and advertising-tech financial products — may fall within DORA's scope. Their AI systems must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for media-financial AI", "Article 6 requires media companies with financial operations to maintain ICT risk-management frameworks covering AI-driven subscription, licensing, and payment systems."),
                    ("Resilience testing for content platforms", "Article 24 mandates resilience testing for critical content-delivery, streaming, and publishing platforms, including AI recommendation and moderation components."),
                    ("Incident reporting for media AI failures", "Major ICT incidents affecting content distribution, subscriber data, or advertising operations must be reported to regulators within specified timeframes."),
                    ("Third-party risk for media AI vendors", "Media companies using cloud-hosted AI for content generation, moderation, and recommendation must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "Non-profits with significant financial operations — microfinance institutions, social-investment platforms, and grant-making foundations — may fall within DORA's scope as financial entities. Their AI systems must meet ICT resilience requirements.",
                "requirements": [
                    ("ICT risk management for non-profit financial AI", "Article 6 requires non-profit financial institutions to maintain ICT risk-management frameworks covering AI-driven lending, grants, and payment systems."),
                    ("Resilience testing for humanitarian platforms", "Article 24 mandates resilience testing for critical beneficiary-registration, aid-distribution, and fundraising platforms, including AI components."),
                    ("Incident reporting for NGO AI failures", "Major ICT incidents affecting beneficiary data, donor information, or financial operations must be reported to regulators within specified timeframes."),
                    ("Third-party risk for NGO AI vendors", "Non-profits using cloud-hosted AI for programme management must maintain oversight of critical third-party ICT providers."),
                ],
                "articles": ["Article 39 — Incident Response", "Article 19 — Robustness", "Article 13 — Risk Management", "Article 29 — Partnership Charter"],
                "mcps": ["dora-ict-risk-assessor-mcp", "dora-article-checker-mcp", "meok-ai-incident-reporting"],
            }

    # ------------------------------------------------------------------
    # NIS2
    # ------------------------------------------------------------------
    if r == "nis2":
        if s == "healthcare":
            return {
                "lead": "Hospitals, medical laboratories, and health-tech platforms qualify as important or critical entities under NIS2. AI systems managing patient records, connected medical devices, and telemedicine platforms must embed cybersecurity-by-design and report significant incidents.",
                "requirements": [
                    ("Cybersecurity risk management for healthcare entities", "Article 21 requires hospitals and health-tech operators to implement risk-based cybersecurity measures covering AI-driven diagnostic devices and EHR systems."),
                    ("Supply-chain security for medical AI", "Security requirements must flow down to AI vendors, imaging-software providers, and connected-device manufacturers in the healthcare supply chain."),
                    ("Incident reporting for medical device compromises", "Significant incidents affecting patient data or device integrity must be reported within 24 hours to CSIRT and sector regulators."),
                    ("Crisis management & business continuity", "Healthcare AI operators must maintain crisis-response plans ensuring continuity of critical clinical services during cyber incidents."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 13 — Risk Management"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "finance-banking":
            return {
                "lead": "Banks, payment institutions, and trading venues are designated as critical entities under NIS2. Their AI systems — from real-time fraud detection to market-surveillance algorithms — must satisfy enhanced cybersecurity risk-management and incident-reporting obligations.",
                "requirements": [
                    ("Cybersecurity risk management for critical entities", "Article 21 mandates proportionate risk-based measures including network segmentation, encryption, and multi-factor authentication for AI training and inference environments."),
                    ("Supply-chain security for AI vendors", "Financial institutions must assess and document cybersecurity practices of AI model vendors, data providers, and cloud infrastructure suppliers."),
                    ("Incident reporting timelines", "Significant incidents must be reported within 24 hours of becoming aware, with updates as investigation proceeds — covering AI system compromises that affect payment or trading integrity."),
                    ("Crisis management & cooperation", "Financial entities must participate in sector-specific crisis-management exercises and share threat intelligence on AI-targeted attacks with national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 33 — Transparency Obligations"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "insurance":
            return {
                "lead": "Large insurers and reinsurers qualify as important or critical entities under NIS2. Their AI infrastructure — covering catastrophe modelling, portfolio optimisation, and cyber-risk underwriting — must meet strengthened cybersecurity risk-management requirements.",
                "requirements": [
                    ("Cybersecurity risk management for insurers", "Article 21 requires proportionate risk-based measures for AI systems handling sensitive policyholder data and catastrophe-modelling workloads."),
                    ("Supply-chain security for catastrophe models", "Insurers must assess the cybersecurity posture of third-party catastrophe-modelling vendors and cloud providers hosting AI risk models."),
                    ("Incident reporting for data breaches", "Significant cyber incidents affecting policyholder data or AI model integrity must be reported within 24 hours, with follow-up reports as investigation proceeds."),
                    ("Crisis management for cyber insurance AI", "Insurers offering cyber insurance with AI-driven risk scoring must maintain crisis-management plans that ensure continuity during systemic cyber events."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 33 — Transparency Obligations"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Large law firms and legal-service providers may qualify as important entities under NIS2, particularly if they provide essential services to critical infrastructure clients. Their AI systems must satisfy cybersecurity risk-management and incident-reporting requirements.",
                "requirements": [
                    ("Entity classification for legal services", "Member States may designate large law firms or legal-service providers as important entities if they provide essential services to critical infrastructure operators."),
                    ("Cybersecurity risk management", "Article 21 requires proportionate measures for AI systems handling sensitive client data, including access control, encryption, and network segmentation."),
                    ("Supply-chain security for legal AI vendors", "Law firms must assess cybersecurity practices of AI document-review, e-discovery, and contract-analysis vendors."),
                    ("Incident reporting for client-data breaches", "Significant cyber incidents affecting client confidentiality or case integrity must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "education":
            return {
                "lead": "Universities, research institutions, and large examination bodies may qualify as important entities under NIS2. Their AI systems — from admissions algorithms to exam-proctoring platforms — must satisfy cybersecurity risk-management and incident-reporting obligations.",
                "requirements": [
                    ("Entity classification for educational institutions", "Member States may designate universities, research institutes, and large examination bodies as important entities based on their societal role and scale."),
                    ("Cybersecurity risk management for academic AI", "Article 21 requires proportionate measures for AI systems handling student records, research data, and examination materials."),
                    ("Supply-chain security for ed-tech vendors", "Educational institutions must assess the cybersecurity practices of AI proctoring, LMS, and adaptive-learning vendors."),
                    ("Incident reporting for exam-security breaches", "Significant cyber incidents affecting examination integrity or student data must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government bodies and public administrative agencies are explicitly included in NIS2's scope as critical or important entities. Their AI systems — from emergency-response optimisation to infrastructure monitoring — must meet enhanced cybersecurity requirements.",
                "requirements": [
                    ("Mandatory entity classification for public bodies", "Central government, regional authorities, and public administrative bodies are designated as critical or important entities under NIS2 Annex I and II."),
                    ("Cybersecurity risk management for government AI", "Article 21 requires proportionate measures for AI systems supporting public services, emergency response, and critical infrastructure oversight."),
                    ("Supply-chain security for public-sector AI", "Government agencies must assess cybersecurity practices of AI vendors, cloud providers, and system integrators delivering public services."),
                    ("Incident reporting for citizen-service breaches", "Significant cyber incidents affecting citizen data or public-service delivery must be reported within 24 hours to national CSIRTs and sector regulators."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "manufacturing":
            return {
                "lead": "Large manufacturers, particularly those producing critical components for energy, transport, health, and digital infrastructure, may qualify as important or critical entities under NIS2. Their AI systems must satisfy enhanced cybersecurity requirements.",
                "requirements": [
                    ("Entity classification for critical manufacturers", "Manufacturers of essential components for critical sectors may be designated as important or critical entities under NIS2 Annex II."),
                    ("Cybersecurity risk management for OT/AI convergence", "Article 21 requires proportionate measures for AI systems at the intersection of operational technology and IT, including network segmentation and secure protocols."),
                    ("Supply-chain security for manufacturing AI", "Manufacturers must assess cybersecurity practices of AI vendors, robotics suppliers, and industrial-IoT platform providers."),
                    ("Incident reporting for industrial cyber incidents", "Significant cyber incidents affecting production lines, safety systems, or supply-chain integrity must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Large e-commerce platforms, digital marketplaces, and retailers operating critical supply-chain infrastructure may qualify as important entities under NIS2. Their AI systems — from demand forecasting to logistics optimisation — must satisfy enhanced cybersecurity requirements.",
                "requirements": [
                    ("Entity classification for large retailers", "Large e-commerce platforms and digital marketplaces may be designated as important entities under NIS2 Annex II based on their scale and societal role."),
                    ("Cybersecurity risk management for retail AI", "Article 21 requires proportionate measures for AI systems handling customer data, payment information, and supply-chain operations."),
                    ("Supply-chain security for retail AI vendors", "Retailers must assess cybersecurity practices of AI personalisation, demand-forecasting, and logistics-optimisation vendors."),
                    ("Incident reporting for customer-data breaches", "Significant cyber incidents affecting customer personal or payment data must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Energy utilities are explicitly designated as critical entities under NIS2 Annex I. Their AI systems — from smart-grid optimisation to predictive maintenance for generation assets — must satisfy the highest tier of cybersecurity risk-management and incident-reporting obligations.",
                "requirements": [
                    ("Mandatory critical-entity status for energy utilities", "Electricity, gas, oil, and district-heating operators are critical entities under NIS2 Annex I, with mandatory cybersecurity risk-management obligations."),
                    ("Cybersecurity risk management for OT/AI systems", "Article 21 requires comprehensive measures for AI systems at the OT/IT boundary, including network segmentation, encryption, and secure protocols."),
                    ("Supply-chain security for energy AI vendors", "Utilities must assess cybersecurity practices of AI vendors, industrial-control suppliers, and cloud providers supporting grid operations."),
                    ("Incident reporting for critical infrastructure", "Significant cyber incidents affecting energy generation, transmission, or distribution must be reported within 24 hours to national CSIRTs and sector regulators."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Transport operators — rail, air, maritime, and road — are explicitly designated as critical or important entities under NIS2. Their AI systems for traffic management, safety monitoring, and logistics optimisation must satisfy enhanced cybersecurity requirements.",
                "requirements": [
                    ("Mandatory entity status for transport operators", "Air, rail, water, and road transport operators are critical or important entities under NIS2 Annex I and II, with mandatory cybersecurity obligations."),
                    ("Cybersecurity risk management for transport AI", "Article 21 requires comprehensive measures for AI systems supporting traffic management, safety systems, and logistics operations."),
                    ("Supply-chain security for transport AI vendors", "Transport operators must assess cybersecurity practices of AI vehicle-system vendors, logistics-platform providers, and cloud infrastructure suppliers."),
                    ("Incident reporting for transport cyber incidents", "Significant cyber incidents affecting safety systems, traffic management, or passenger data must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "media-publishing":
            return {
                "lead": "Large media platforms, broadcasters, and digital infrastructure providers may qualify as important entities under NIS2. Their AI systems — from content delivery to automated moderation — must satisfy enhanced cybersecurity requirements.",
                "requirements": [
                    ("Entity classification for media platforms", "Large digital platforms, broadcasters, and content-delivery networks may be designated as important entities under NIS2 Annex II."),
                    ("Cybersecurity risk management for media AI", "Article 21 requires proportionate measures for AI systems handling content, subscriber data, and advertising operations."),
                    ("Supply-chain security for media AI vendors", "Media companies must assess cybersecurity practices of AI content-generation, moderation, and recommendation vendors."),
                    ("Incident reporting for content-platform breaches", "Significant cyber incidents affecting content integrity, subscriber data, or platform availability must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "Large NGOs and humanitarian organisations operating critical infrastructure or essential services may qualify as important entities under NIS2. Their AI systems must satisfy cybersecurity risk-management and incident-reporting obligations.",
                "requirements": [
                    ("Entity classification for large NGOs", "Member States may designate large NGOs providing essential services as important entities under NIS2 Annex II."),
                    ("Cybersecurity risk management for NGO AI", "Article 21 requires proportionate measures for AI systems handling beneficiary data, programme information, and operational logistics."),
                    ("Supply-chain security for humanitarian AI vendors", "NGOs must assess cybersecurity practices of AI platform providers, especially those handling data from conflict or disaster zones."),
                    ("Incident reporting for beneficiary-data breaches", "Significant cyber incidents affecting vulnerable-population data must be reported within 24 hours to national CSIRTs."),
                ],
                "articles": ["Article 22 — Right to Safety", "Article 26 — Adversarial Resilience", "Article 39 — Incident Response", "Article 47 — Audit Right"],
                "mcps": ["nis2-cybersecurity-assessor-mcp", "nis2-article-checker-mcp", "meok-cra"],
            }

    # ------------------------------------------------------------------
    # CRA
    # ------------------------------------------------------------------
    if r == "cra":
        if s == "healthcare":
            return {
                "lead": "Medical devices with digital elements — from AI-enabled imaging hardware to patient-monitoring wearables — fall under the Cyber Resilience Act. Manufacturers must embed security-by-design, maintain SBOMs, and provide security updates throughout the product lifecycle.",
                "requirements": [
                    ("Security-by-design for medical devices", "Article 10 mandates that AI-enabled medical hardware is designed with essential cybersecurity requirements, secure defaults, and data confidentiality."),
                    ("Vulnerability handling & coordinated disclosure", "Article 13 requires manufacturers to establish vulnerability-handling processes and report unpatched exploitable vulnerabilities within specified deadlines."),
                    ("Software Bill of Materials (SBOM)", "Healthcare device manufacturers must provide SBOMs for embedded AI software to enable downstream vulnerability tracking and patch management."),
                    ("Security updates over product lifetime", "Article 14 obliges manufacturers to provide security updates for the expected product lifetime, covering AI model retraining and security patch deployment."),
                ],
                "articles": ["Article 2 — Provable Safety", "Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "finance-banking":
            return {
                "lead": "Trading terminals, payment hardware, and ATM networks with embedded AI software are products with digital elements under the CRA. Banks and fintechs must ensure these products meet essential security requirements, carry SBOMs, and receive security updates.",
                "requirements": [
                    ("Security requirements for financial hardware", "Article 10 applies to smart ATMs, POS terminals, and trading-floor hardware running embedded AI — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for fintech products", "Article 13 requires financial-hardware manufacturers to establish vulnerability-handling processes and report unpatched critical vulnerabilities within defined deadlines."),
                    ("SBOM for embedded financial AI", "Manufacturers and importers must provide SBOMs for embedded AI software in financial hardware to enable downstream risk management."),
                    ("Security-update obligations", "Security updates must be provided for the expected product lifetime or for a minimum of five years, whichever is longer."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "insurance":
            return {
                "lead": "Connected insurance hardware — telematics devices, smart-home sensors, and wearable health trackers — are products with digital elements under the CRA. Manufacturers must ensure these devices meet essential security requirements and receive ongoing security updates.",
                "requirements": [
                    ("Security-by-design for connected insurance devices", "Article 10 applies to telematics black boxes, smart-home leak detectors, and health wearables — requiring secure boot, encryption, and tamper evidence."),
                    ("Vulnerability handling for IoT insurance hardware", "Article 13 requires manufacturers to establish vulnerability-handling processes and report exploitable vulnerabilities within defined deadlines."),
                    ("SBOM for embedded insurance AI", "Manufacturers must provide SBOMs for firmware and embedded AI software in connected insurance devices."),
                    ("Security-update lifetime", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring long-term protection of policyholder data."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Legal-tech hardware — secure document scanners, court-room presentation systems, and client-access kiosks — with embedded digital elements falls under the CRA. Manufacturers must ensure security-by-design and ongoing security updates.",
                "requirements": [
                    ("Security requirements for legal-tech hardware", "Article 10 applies to secure document-imaging devices, court audio-visual systems with embedded AI transcription, and client-access terminals."),
                    ("Vulnerability handling", "Article 13 requires manufacturers of legal-tech hardware to establish vulnerability-handling processes and report critical vulnerabilities."),
                    ("SBOM for embedded legal AI", "SBOMs must be provided for firmware and embedded AI software in legal-tech products to enable vulnerability management."),
                    ("Security-update obligations", "Security updates must be provided for the expected product lifetime or a minimum of five years."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "education":
            return {
                "lead": "Educational technology hardware — interactive whiteboards, student tablets, lab equipment with embedded AI, and campus access devices — are products with digital elements under the CRA. Manufacturers must ensure security-by-design and ongoing updates.",
                "requirements": [
                    ("Security-by-design for ed-tech hardware", "Article 10 applies to student devices, smart-lab equipment, and campus access systems — requiring secure boot, encryption, and access control."),
                    ("Vulnerability handling for educational devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report exploitable vulnerabilities in educational hardware."),
                    ("SBOM for embedded ed-tech AI", "SBOMs must be provided for firmware and embedded AI in educational devices to enable school and university IT departments to manage risk."),
                    ("Security-update obligations", "Security updates must be provided for the expected product lifetime or a minimum of five years, protecting student data across device generations."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government-deployed digital products — smart-city sensors, voting terminals, public-access kiosks, and emergency-communication devices — are products with digital elements under the CRA. Security-by-design and update obligations apply to protect citizen trust.",
                "requirements": [
                    ("Security-by-design for government digital products", "Article 10 applies to smart-city IoT, public-transport sensors, and government-issued devices — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for public-sector devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities affecting government-deployed products."),
                    ("SBOM for government AI systems", "SBOMs must be provided for embedded AI in government digital products to enable centralised vulnerability management and supply-chain transparency."),
                    ("Security-update obligations for public infrastructure", "Security updates must be provided for the expected product lifetime, ensuring continued protection of citizen-facing government technology."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "manufacturing":
            return {
                "lead": "Manufactured products with digital elements — industrial IoT sensors, smart machinery, robotics controllers, and connected safety equipment — are squarely within the CRA's scope. Security-by-design, SBOMs, and update obligations apply throughout the product lifecycle.",
                "requirements": [
                    ("Security-by-design for industrial products", "Article 10 applies to smart manufacturing equipment, industrial IoT sensors, and robotics controllers — requiring secure boot, encryption, and access control."),
                    ("Vulnerability handling for industrial devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report exploitable vulnerabilities in industrial control systems."),
                    ("SBOM for manufacturing AI", "SBOMs must be provided for firmware and embedded AI in manufactured products to enable downstream risk management by industrial customers."),
                    ("Security-update obligations for industrial equipment", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring long-term protection of industrial systems."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Retail technology products — smart point-of-sale terminals, inventory robots, customer-facing kiosks, and connected fitting-room devices — are products with digital elements under the CRA. Security-by-design and update obligations protect consumer trust and payment security.",
                "requirements": [
                    ("Security-by-design for retail hardware", "Article 10 applies to POS terminals, smart shelves, inventory robots, and customer kiosks — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for retail devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities in retail technology products."),
                    ("SBOM for retail AI systems", "SBOMs must be provided for firmware and embedded AI in retail devices to enable vulnerability management by retailers and their IT partners."),
                    ("Security-update obligations for retail tech", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring continued protection of customer data."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Energy infrastructure products with digital elements — smart meters, grid sensors, EV chargers, and industrial control systems — are within the CRA's scope. Security-by-design, SBOMs, and update obligations are essential for protecting critical national infrastructure.",
                "requirements": [
                    ("Security-by-design for energy infrastructure", "Article 10 applies to smart meters, grid sensors, EV chargers, and control-system hardware — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for energy devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities in energy infrastructure products."),
                    ("SBOM for energy AI systems", "SBOMs must be provided for firmware and embedded AI in energy devices to enable centralised vulnerability management by utilities and regulators."),
                    ("Security-update obligations for energy infrastructure", "Security updates must be provided for the expected product lifetime, ensuring long-term protection of critical energy systems."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Transportation products with digital elements — vehicle telematics, autonomous driving hardware, traffic sensors, and fleet-management devices — are within the CRA's scope. Security-by-design and update obligations protect road safety and passenger data.",
                "requirements": [
                    ("Security-by-design for automotive AI", "Article 10 applies to vehicle ECUs, ADAS hardware, telematics units, and traffic sensors — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for transport devices", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities in vehicle and transport infrastructure products."),
                    ("SBOM for transport AI systems", "SBOMs must be provided for firmware and embedded AI in vehicle and transport devices to enable fleet-wide vulnerability management."),
                    ("Security-update obligations for vehicles", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring continued protection of vehicle systems and passenger data."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "media-publishing":
            return {
                "lead": "Media technology products — smart TVs, streaming devices, broadcast equipment, and content-creation hardware — with embedded digital elements fall under the CRA. Security-by-design and update obligations protect viewer data and content integrity.",
                "requirements": [
                    ("Security-by-design for media devices", "Article 10 applies to smart TVs, streaming sticks, broadcast encoders, and content-creation hardware — requiring secure boot, encryption, and access control."),
                    ("Vulnerability handling for media hardware", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities in media technology products."),
                    ("SBOM for media AI systems", "SBOMs must be provided for firmware and embedded AI in media devices to enable vulnerability management by broadcasters and consumers."),
                    ("Security-update obligations for media tech", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring continued protection of viewer data and content systems."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "Non-profit technology products — beneficiary registration tablets, field sensors, communication devices, and aid-distribution hardware — with embedded digital elements fall under the CRA. Security-by-design and update obligations protect vulnerable populations' data.",
                "requirements": [
                    ("Security-by-design for humanitarian devices", "Article 10 applies to beneficiary-registration tablets, field sensors, and communication devices — requiring secure boot, encryption, and tamper resistance."),
                    ("Vulnerability handling for NGO hardware", "Article 13 requires manufacturers to establish vulnerability-handling processes and report critical vulnerabilities in devices deployed in humanitarian contexts."),
                    ("SBOM for NGO AI systems", "SBOMs must be provided for firmware and embedded AI in humanitarian devices to enable field-based vulnerability management."),
                    ("Security-update obligations for field devices", "Security updates must be provided for the expected product lifetime or a minimum of five years, ensuring continued protection in low-connectivity environments."),
                ],
                "articles": ["Article 15 — Accuracy, Robustness, Cybersecurity", "Article 13 — Vulnerability Handling", "Article 19 — Robustness", "Article 2 — Provable Safety"],
                "mcps": ["cra-vulnerability-tracker-mcp", "cra-article-checker-mcp", "meok-watermark-attest"],
            }

    # ------------------------------------------------------------------
    # ISO 42001
    # ------------------------------------------------------------------
    if r == "iso-42001":
        if s == "healthcare":
            return {
                "lead": "ISO/IEC 42001 provides the management-system backbone for healthcare organisations deploying AI in clinical, operational, and research settings. The standard's clause structure aligns with existing ISO 9001 and ISO 27001 certifications common in health systems.",
                "requirements": [
                    ("AI management system scope & context", "Clause 4 requires healthcare organisations to define the scope of their AI management system, covering clinical decision support, operational automation, and research analytics."),
                    ("Leadership commitment & AI policy", "Clause 5 mandates executive ownership of AI governance, including board-level accountability for patient-safety outcomes and ethical AI use."),
                    ("AI risk assessment & treatment", "Clause 6 requires systematic risk assessment specific to healthcare AI — clinical error modes, data-quality risks, and patient-harm scenarios — with documented treatment plans."),
                    ("Performance evaluation & continual improvement", "Clause 9 mandates monitoring of AI system performance against clinical safety KPIs, with feedback loops into model retraining and policy updates."),
                ],
                "articles": ["Article 5 — Growth Edge", "Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "finance-banking":
            return {
                "lead": "ISO/IEC 42001 offers financial institutions a structured management-system approach to AI governance. Banks already certified to ISO 27001 and ISO 9001 can integrate AI management into existing frameworks, reducing duplication and audit burden.",
                "requirements": [
                    ("Context of the organisation — AI in banking", "Clause 4 requires mapping AI use cases across retail, commercial, and investment banking, identifying regulatory interfaces and stakeholder expectations."),
                    ("Leadership & AI policy", "Clause 5 mandates board-level AI policy covering fairness in lending, model risk management, and customer transparency — aligned with prudential expectations."),
                    ("AI risk assessment & treatment", "Clause 6 requires documented risk assessment covering model drift, adversarial attacks, data-poisoning risks, and discriminatory outcomes in credit decisions."),
                    ("Operation & model lifecycle management", "Clause 8 covers model development, validation, deployment, and retirement — mirroring SR 11-7 and ECB guidance on model risk."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "insurance":
            return {
                "lead": "ISO/IEC 42001 provides insurers with a management-system framework for AI governance across underwriting, claims, customer service, and actuarial functions. Integration with existing ISO 27001 and actuarial control cycles is straightforward.",
                "requirements": [
                    ("Scope & context for insurance AI", "Clause 4 requires insurers to define the scope of their AI management system across lines of business, identifying regulatory and stakeholder requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy, covering fairness in pricing, transparency in claims, and ethical use of health and behavioural data."),
                    ("AI risk assessment for underwriting models", "Clause 6 requires documented risk assessment of AI underwriting models — covering data bias, model drift, adversarial manipulation, and unfair discrimination."),
                    ("Performance evaluation & model monitoring", "Clause 9 mandates ongoing monitoring of model performance against fairness and accuracy KPIs, with feedback into model retraining and governance."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "ISO/IEC 42001 provides law firms with a structured approach to AI governance. Given the profession's existing quality-management and risk-management disciplines, integration with ISO 42001 is natural and supports client confidence.",
                "requirements": [
                    ("Scope & context for legal AI", "Clause 4 requires law firms to map AI use cases — research, drafting, e-discovery, due diligence — and identify client, regulatory, and ethical expectations."),
                    ("Leadership & AI policy", "Clause 5 mandates that firm leadership owns AI policy, covering confidentiality, accuracy verification, professional indemnity, and client transparency."),
                    ("AI risk assessment for legal practice", "Clause 6 requires documented risk assessment covering hallucination risks, data-breach exposure, privilege waiver, and regulatory non-compliance."),
                    ("Performance evaluation & quality control", "Clause 9 mandates monitoring of AI output quality against professional standards, with feedback into training, supervision, and technology selection."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "education":
            return {
                "lead": "ISO/IEC 42001 helps educational institutions establish systematic AI governance across learning management, student analytics, admissions, and research. The standard aligns with existing quality-assurance and data-governance frameworks common in academia.",
                "requirements": [
                    ("Scope & context for educational AI", "Clause 4 requires institutions to map AI use cases across teaching, research, administration, and student services, identifying stakeholder expectations."),
                    ("Leadership & AI policy", "Clause 5 mandates that institutional leadership owns AI policy, covering academic integrity, student privacy, fairness in admissions, and research ethics."),
                    ("AI risk assessment for student-facing systems", "Clause 6 requires documented risk assessment for admissions AI, grading automation, and proctoring — covering bias, error, privacy, and psychological impact."),
                    ("Performance evaluation & pedagogical review", "Clause 9 mandates monitoring of AI effectiveness against educational outcomes, with feedback into curriculum design and technology procurement."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "government-public-sector":
            return {
                "lead": "ISO/IEC 42001 offers public-sector organisations a management-system framework for AI governance that aligns with existing public-administration quality and risk standards. It supports transparency, accountability, and citizen trust in government AI.",
                "requirements": [
                    ("Scope & context for public-sector AI", "Clause 4 requires mapping AI use cases across citizen services, law enforcement, infrastructure, and policy analysis, identifying public-interest and legal requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates that senior public leadership owns AI policy, covering transparency, non-discrimination, administrative-law compliance, and citizen redress."),
                    ("AI risk assessment for public services", "Clause 6 requires documented risk assessment for AI affecting citizen rights — covering bias, error, privacy, security, and democratic legitimacy."),
                    ("Performance evaluation & public accountability", "Clause 9 mandates monitoring of AI outcomes against public-service KPIs, with public reporting and feedback mechanisms for citizens and oversight bodies."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "manufacturing":
            return {
                "lead": "ISO/IEC 42001 helps manufacturers integrate AI governance into existing quality-management and operational-excellence frameworks. The standard supports safe deployment of AI in production, maintenance, and supply-chain contexts.",
                "requirements": [
                    ("Scope & context for manufacturing AI", "Clause 4 requires manufacturers to map AI use cases across production, quality, maintenance, and supply chain, identifying safety and regulatory requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy covering safety integration, worker protection, product conformity, and environmental impact."),
                    ("AI risk assessment for production systems", "Clause 6 requires documented risk assessment for AI-controlled robotics, quality inspection, and predictive maintenance — covering safety, error, and cyber risks."),
                    ("Performance evaluation & continuous improvement", "Clause 9 mandates monitoring of AI system performance against production KPIs, with feedback into maintenance schedules and model retraining."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "ISO/IEC 42001 provides retailers with a management-system framework for AI governance across e-commerce, in-store operations, supply chain, and customer service. Integration with existing ISO 9001 quality certifications supports consistent implementation.",
                "requirements": [
                    ("Scope & context for retail AI", "Clause 4 requires retailers to map AI use cases across online, in-store, supply chain, and customer service, identifying consumer-protection and operational requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy covering customer fairness, data ethics, product safety, and supply-chain transparency."),
                    ("AI risk assessment for customer-facing systems", "Clause 6 requires documented risk assessment for recommendation engines, dynamic pricing, and customer service AI — covering bias, error, privacy, and consumer harm."),
                    ("Performance evaluation & customer-outcome monitoring", "Clause 9 mandates monitoring of AI outcomes against customer-satisfaction, fairness, and safety KPIs, with feedback into model and policy updates."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "energy-utilities":
            return {
                "lead": "ISO/IEC 42001 supports energy utilities in establishing systematic AI governance for grid operations, asset management, customer service, and energy trading. The standard aligns with existing operational-excellence and safety-management frameworks.",
                "requirements": [
                    ("Scope & context for energy AI", "Clause 4 requires utilities to map AI use cases across generation, transmission, distribution, trading, and customer service, identifying safety and regulatory requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy covering grid safety, supply reliability, environmental impact, and customer fairness."),
                    ("AI risk assessment for critical systems", "Clause 6 requires documented risk assessment for AI controlling grid operations, safety systems, and critical infrastructure — covering cyber, safety, and operational risks."),
                    ("Performance evaluation & grid monitoring", "Clause 9 mandates monitoring of AI performance against grid-stability, safety, and efficiency KPIs, with feedback into operations and maintenance."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "ISO/IEC 42001 provides transport operators with a management-system framework for AI governance across fleet operations, traffic management, safety systems, and customer service. Integration with ISO 9001 and sector safety standards supports consistent implementation.",
                "requirements": [
                    ("Scope & context for transport AI", "Clause 4 requires operators to map AI use cases across fleet, traffic, safety, maintenance, and customer service, identifying regulatory and safety requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy covering road safety, passenger protection, driver welfare, and environmental impact."),
                    ("AI risk assessment for safety-critical systems", "Clause 6 requires documented risk assessment for autonomous systems, driver-monitoring AI, and traffic-control AI — covering safety, cyber, and operational risks."),
                    ("Performance evaluation & safety monitoring", "Clause 9 mandates monitoring of AI performance against safety, efficiency, and customer-satisfaction KPIs, with feedback into operations and policy."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "media-publishing":
            return {
                "lead": "ISO/IEC 42001 provides media organisations with a management-system framework for AI governance across content creation, distribution, moderation, recommendation, and rights management. The standard supports editorial integrity and audience trust.",
                "requirements": [
                    ("Scope & context for media AI", "Clause 4 requires media organisations to map AI use cases across content generation, curation, moderation, recommendation, and rights management, identifying editorial and regulatory requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates executive ownership of AI policy covering editorial integrity, creator fairness, audience transparency, and information accuracy."),
                    ("AI risk assessment for content systems", "Clause 6 requires documented risk assessment for generative AI, recommendation algorithms, and automated moderation — covering misinformation, bias, harm, and rights infringement."),
                    ("Performance evaluation & editorial review", "Clause 9 mandates monitoring of AI outcomes against accuracy, fairness, and editorial-quality KPIs, with feedback into content policies and technology selection."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "ISO/IEC 42001 provides NGOs with a management-system framework for AI governance across programme delivery, fundraising, advocacy, and operations. The standard supports mission alignment, donor accountability, and beneficiary protection.",
                "requirements": [
                    ("Scope & context for NGO AI", "Clause 4 requires NGOs to map AI use cases across programmes, fundraising, advocacy, and operations, identifying mission, ethical, and regulatory requirements."),
                    ("Leadership & AI policy", "Clause 5 mandates that organisational leadership owns AI policy covering do-no-harm principles, beneficiary dignity, donor transparency, and staff accountability."),
                    ("AI risk assessment for beneficiary-facing systems", "Clause 6 requires documented risk assessment for AI affecting beneficiary selection, aid distribution, and protection — covering bias, error, privacy, and dignity risks."),
                    ("Performance evaluation & mission alignment", "Clause 9 mandates monitoring of AI outcomes against programme-effectiveness and beneficiary-welfare KPIs, with feedback into strategy and partnerships."),
                ],
                "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right"],
                "mcps": ["iso-42001-gap-analyzer-mcp", "iso-42001-documentation-generator-mcp", "meok-rms"],
            }

    # ------------------------------------------------------------------
    # HIPAA
    # ------------------------------------------------------------------
    if r == "hipaa":
        if s == "healthcare":
            return {
                "lead": "HIPAA's Privacy Rule, Security Rule, and Breach Notification Rule form the cornerstone of US healthcare data protection. Any AI system processing protected health information (PHI) — whether hosted on-premise or in the cloud — must satisfy administrative, physical, and technical safeguards.",
                "requirements": [
                    ("Minimum necessary standard for PHI access", "The Privacy Rule requires that AI systems access only the minimum PHI necessary for their function, with role-based restrictions and automatic de-identification where possible."),
                    ("Technical safeguards — access control & audit", "The Security Rule mandates unique user identification, emergency access procedures, and automatic audit logs for all AI-driven access to electronic PHI."),
                    ("Business Associate Agreements (BAAs)", "Cloud AI providers, analytics vendors, and model-hosting platforms that process PHI must sign BAAs accepting direct liability for HIPAA compliance."),
                    ("Breach notification & risk assessment", "Covered entities must assess the probability that impermissible PHI disclosure compromises security or privacy, and notify affected individuals and HHS when thresholds are met."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 22 — Right to Safety", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "finance-banking":
            return {
                "lead": "While HIPAA is healthcare-specific, banking AI that processes health-related financial data — such as health savings accounts, medical debt collections, or wellness-programme incentives — may trigger HIPAA obligations when operating as a business associate of a covered entity.",
                "requirements": [
                    ("Business Associate Agreement for health-financial AI", "If a bank's AI processes PHI on behalf of a health plan or provider, it must sign a BAA and implement HIPAA administrative, physical, and technical safeguards."),
                    ("Minimum necessary access to health-related financial data", "AI systems must limit access to health-related financial information to the minimum necessary for the specific banking function being performed."),
                    ("Audit controls for health-financial processing", "All access to health-related financial data by AI systems must be logged and auditable, with regular review of access patterns for anomalies."),
                    ("Breach notification for health-financial data", "Unauthorised access to health-related financial data must be assessed under the Breach Notification Rule, with notifications to affected individuals and HHS where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "insurance":
            return {
                "lead": "Health insurers, long-term care insurers, and wellness-programme administrators are HIPAA-covered entities. Their AI systems — from pre-authorisation automation to fraud detection in medical claims — must comply with the Privacy Rule, Security Rule, and Breach Notification Rule.",
                "requirements": [
                    ("Privacy Rule for health insurance AI", "AI systems processing PHI for pre-authorisation, claims adjudication, or care management must respect the Minimum Necessary Standard and patient access rights."),
                    ("Security Rule technical safeguards", "Access controls, audit controls, integrity controls, and transmission security must be implemented for all AI-driven access to electronic PHI."),
                    ("Business Associate Agreements for AI vendors", "Third-party AI providers processing PHI on behalf of health insurers must sign BAAs and implement equivalent safeguards."),
                    ("Breach Notification for PHI incidents", "Unauthorised access to PHI by AI systems or their operators must be assessed under the Breach Notification Rule and reported where thresholds are met."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "Law firms handling healthcare litigation, medical malpractice defence, or HIPAA compliance advisory work may process protected health information. When acting as business associates of covered entities, these firms and their AI tools become subject to HIPAA.",
                "requirements": [
                    ("Business Associate Agreement for health-law AI", "Law firms processing PHI on behalf of healthcare clients must sign BAAs and ensure their AI systems comply with HIPAA safeguards."),
                    ("Minimum necessary for health litigation AI", "AI-assisted document review in healthcare litigation must limit PHI access to the minimum necessary for the specific legal matter."),
                    ("Audit controls for PHI access", "All AI-driven access to PHI must be logged and auditable, with regular review of access patterns and anomaly detection."),
                    ("Breach notification for health-law data", "Unauthorised access to PHI in health-law matters must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "education":
            return {
                "lead": "School-based health clinics, university health centres, and educational institutions with nursing or medical programmes process protected health information. Their AI systems — from appointment scheduling to health-record analytics — must comply with HIPAA when operating as covered entities or business associates.",
                "requirements": [
                    ("Covered entity status for school health services", "School-based health centres and university medical services that transmit health information electronically are HIPAA-covered entities."),
                    ("Privacy Rule for student health AI", "AI systems processing student health records must respect the Minimum Necessary Standard and provide students with access to their PHI."),
                    ("Security Rule for campus health systems", "Technical safeguards including access control, audit controls, and transmission security must protect electronic PHI in campus health AI systems."),
                    ("Breach Notification for student health data", "Unauthorised access to student health data by AI systems or operators must be assessed and reported under the Breach Notification Rule."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "government-public-sector":
            return {
                "lead": "Government health agencies — Medicare/Medicaid services, NHS bodies, public health departments, and veterans' health administrations — are covered entities or their equivalents under HIPAA (or analogous national health-privacy laws). Their AI systems must satisfy health-data safeguards.",
                "requirements": [
                    ("Covered entity status for government health bodies", "Government agencies operating health programmes are HIPAA-covered entities and must comply with the Privacy Rule, Security Rule, and Breach Notification Rule."),
                    ("Privacy Rule for public health AI", "AI systems processing PHI for public health surveillance, benefit administration, or clinical services must respect the Minimum Necessary Standard and individual rights."),
                    ("Security Rule for government health systems", "Technical safeguards must protect electronic PHI in government health AI systems, with audit trails and access controls aligned with public-sector accountability."),
                    ("Breach Notification for government health data", "Unauthorised access to PHI in government health systems must be assessed and reported, with additional public disclosure obligations for public-sector bodies."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "manufacturing":
            return {
                "lead": "Manufacturers of medical devices, pharmaceutical packaging, and healthcare equipment may process health-related data in their AI systems. When acting as business associates of covered entities or handling device-generated PHI, HIPAA obligations apply.",
                "requirements": [
                    ("Business Associate Agreements for med-tech AI", "Medical-device manufacturers processing PHI through AI-powered remote monitoring or diagnostic systems must sign BAAs with covered entities."),
                    ("Privacy Rule for device-generated health data", "AI systems processing PHI from connected medical devices must respect the Minimum Necessary Standard and individual access rights."),
                    ("Security Rule for med-tech manufacturing", "Technical safeguards must protect electronic PHI in AI systems embedded in medical devices or their supporting cloud platforms."),
                    ("Breach Notification for medical-device data", "Unauthorised access to PHI from connected medical devices must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "Retailers selling health products, pharmacies, and wellness brands may process health-related data through their AI systems. When operating as business associates of covered entities or handling protected health information, HIPAA obligations apply.",
                "requirements": [
                    ("Business Associate Agreements for pharmacy AI", "Pharmacies and health retailers using AI for prescription management, adherence programmes, or health recommendations must sign BAAs where applicable."),
                    ("Privacy Rule for health-retail AI", "AI systems processing health-related purchase data or wellness-programme information must respect the Minimum Necessary Standard and individual rights."),
                    ("Security Rule for health-retail systems", "Technical safeguards must protect electronic health data in retail AI systems, with access controls and audit trails."),
                    ("Breach Notification for health-retail data", "Unauthorised access to health-related customer data must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "energy-utilities":
            return {
                "lead": "Utilities operating health-related programmes — wellness incentives, home-health monitoring partnerships, or medical-device power services — may process protected health information. When acting as business associates or handling PHI, HIPAA obligations apply.",
                "requirements": [
                    ("Business Associate Agreements for health-utility AI", "Utilities partnering with healthcare providers for remote monitoring or wellness programmes must sign BAAs and implement HIPAA safeguards."),
                    ("Privacy Rule for health-utility AI", "AI systems processing health-related data from smart-home health devices or wellness programmes must respect the Minimum Necessary Standard."),
                    ("Security Rule for health-utility systems", "Technical safeguards must protect electronic PHI in utility AI systems, with access controls and audit trails."),
                    ("Breach Notification for health-utility data", "Unauthorised access to health-related data must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "Medical transport operators, air ambulance services, and logistics companies handling pharmaceutical shipments may process protected health information. When acting as business associates or handling PHI, HIPAA obligations apply.",
                "requirements": [
                    ("Business Associate Agreements for medical transport AI", "Medical transport and pharmaceutical logistics operators processing PHI must sign BAAs and implement HIPAA safeguards."),
                    ("Privacy Rule for medical transport AI", "AI systems scheduling medical transport or tracking pharmaceutical shipments must respect the Minimum Necessary Standard and individual rights."),
                    ("Security Rule for medical transport systems", "Technical safeguards must protect electronic PHI in transport AI systems, with access controls and audit trails."),
                    ("Breach Notification for medical transport data", "Unauthorised access to PHI in medical transport or pharmaceutical logistics must be assessed under the Breach Notification Rule."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "media-publishing":
            return {
                "lead": "Health publishers, medical journal platforms, and wellness content providers may process protected health information through their AI systems. When acting as business associates or handling PHI from contributors or research subjects, HIPAA obligations apply.",
                "requirements": [
                    ("Business Associate Agreements for health-media AI", "Health publishers and medical platforms processing PHI must sign BAAs and implement HIPAA safeguards where applicable."),
                    ("Privacy Rule for health-media AI", "AI systems processing health-related contributor data or research subject information must respect the Minimum Necessary Standard and individual rights."),
                    ("Security Rule for health-media systems", "Technical safeguards must protect electronic PHI in health-media AI systems, with access controls and audit trails."),
                    ("Breach Notification for health-media data", "Unauthorised access to PHI in health publishing must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "Health-focused NGOs, medical missions, and humanitarian health providers may process protected health information through their AI systems. When operating as covered entities or business associates, these organisations must comply with HIPAA.",
                "requirements": [
                    ("Covered entity status for health NGOs", "NGOs operating clinics, mobile health units, or health programmes that transmit health information electronically may be HIPAA-covered entities."),
                    ("Privacy Rule for humanitarian health AI", "AI systems processing PHI in refugee health, epidemic response, or mobile clinics must respect the Minimum Necessary Standard and individual rights."),
                    ("Security Rule for field health systems", "Technical safeguards must protect electronic PHI in NGO health AI systems, even in low-resource or conflict-zone deployments."),
                    ("Breach Notification for NGO health data", "Unauthorised access to PHI in NGO health programmes must be assessed under the Breach Notification Rule and reported where required."),
                ],
                "articles": ["Article 25 — Privacy by Design", "Article 43 — Sovereignty Principle", "Article 47 — Audit Right", "Article 22 — Right to Safety"],
                "mcps": ["hipaa-privacy-rule-checker-mcp", "hipaa-security-rule-assessor-mcp", "meok-data-governance"],
            }

    # ------------------------------------------------------------------
    # UK AI Regulation
    # ------------------------------------------------------------------
    if r == "uk-ai-regulation":
        if s == "healthcare":
            return {
                "lead": "The UK's pro-innovation AI regulation relies on existing sector regulators — the MHRA for medical devices, the CQC for care quality, and the ICO for data protection. Healthcare AI developers must navigate overlapping guidance rather than a single statutory framework.",
                "requirements": [
                    ("MHRA guidance on AI-as-medical-device", "Software including AI that meets the medical-device definition must obtain UKCA marking and satisfy Essential Requirements under UK Medical Devices Regulations 2002."),
                    ("ICO guidance on health data & AI", "The ICO expects healthcare AI deployers to conduct DPIAs, ensure fairness in automated decision-making, and provide transparency about how AI influences patient care."),
                    ("CQC expectations on safe AI use in care settings", "Care providers using AI for patient monitoring or care planning must demonstrate to CQC inspectors that systems are safe, effective, and subject to human oversight."),
                    ("NHS AI Lab standards & best practice", "NHS England provides additional assurance requirements including algorithmic impact assessments, bias audits, and real-world performance monitoring for NHS-deployed AI."),
                ],
                "articles": ["Article 17 — Transparency to Users", "Article 13 — Risk Management", "Article 33 — Transparency Obligations", "Article 29 — Partnership Charter"],
                "mcps": ["meok-uk-ai-reg", "meok-clinical-ai-validator", "meok-rms"],
            }
        if s == "finance-banking":
            return {
                "lead": "The UK's sector-based approach places AI oversight for financial services primarily with the FCA and the Bank of England / PRA. Firms must demonstrate safe and responsible AI use through existing regulatory frameworks, with escalating supervisory expectations.",
                "requirements": [
                    ("FCA guidance on AI & machine learning", "The FCA expects firms to ensure AI systems are safe, fair, and transparent, with governance frameworks that identify and mitigate conduct risks to consumers."),
                    ("PRA expectations on model risk management", "The PRA's SS3/18 and related guidance on model risk management apply directly to AI models used for capital calculation, credit risk, and stress testing."),
                    ("Consumer Duty & AI fairness", "The Consumer Duty requires firms to act to deliver good outcomes for retail customers — including testing AI-driven pricing and advice for fairness and understanding."),
                    ("SMCR accountability for AI decisions", "Senior managers under the Senior Managers and Certification Regime (SMCR) remain personally accountable for AI-driven decisions within their areas of responsibility."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "insurance":
            return {
                "lead": "UK insurance AI falls under the FCA's and PRA's remit, with additional ICO oversight for data protection. The sector-based approach means insurers must align AI governance with existing conduct, prudential, and financial-promotion rules.",
                "requirements": [
                    ("FCA guidance on AI in insurance", "The FCA expects insurers to ensure AI-driven pricing and claims decisions are fair, transparent, and do not produce unfairly discriminatory outcomes for protected groups."),
                    ("Consumer Duty & AI fairness", "The Consumer Duty requires insurers to demonstrate that AI systems deliver fair value and good outcomes for retail customers, with evidence of testing and monitoring."),
                    ("SMCR accountability for AI models", "Senior managers remain accountable for AI-driven decisions in their areas, including model risk, data ethics, and customer outcomes."),
                    ("ICO guidance on insurance data & AI", "The ICO expects DPIAs for AI processing sensitive personal data, with transparency about automated decisions and provision for human review."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "legal-law-firms":
            return {
                "lead": "UK legal AI is overseen by the SRA, the Bar Standards Board, and the ICO. The sector-based approach means AI governance must align with existing professional conduct rules, including duties of confidentiality, competence, and transparency.",
                "requirements": [
                    ("SRA guidance on technology & AI", "The SRA expects solicitors to understand the limitations of AI tools, maintain competence in their use, and ensure that client confidentiality is not compromised."),
                    ("Professional indemnity & AI-generated advice", "Solicitors remain personally responsible for advice given to clients; reliance on AI without adequate review may expose firms to professional indemnity claims and regulatory sanction."),
                    ("ICO guidance on legal data & AI", "The ICO expects law firms using AI to conduct DPIAs for high-risk processing, ensure transparency, and respect data-subject rights without breaching client confidentiality."),
                    ("Bar Standards Board on AI in litigation", "Barristers using AI for case preparation must ensure accuracy, verify citations, and maintain independence of professional judgment."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "education":
            return {
                "lead": "UK educational AI is overseen by the DfE, Ofsted, the Office for Students, and the ICO. The sector-based approach means AI governance must align with existing safeguarding, equality, and data-protection obligations across schools, colleges, and universities.",
                "requirements": [
                    ("DfE guidance on AI in education", "The Department for Education expects schools and colleges to use AI safely, transparently, and in ways that support — not replace — professional educator judgment."),
                    ("Ofsted & Office for Students expectations", "Inspectors may ask how institutions ensure AI-driven admissions, assessment, and student support are fair, accurate, and subject to human oversight."),
                    ("Safeguarding & AI", "AI systems used for student monitoring or behavioural analytics must align with Keeping Children Safe in Education (KCSIE) and local safeguarding partnership expectations."),
                    ("ICO guidance on student data & AI", "The ICO expects DPIAs for high-risk educational AI processing, with transparency for students and parents and respect for children's enhanced data rights."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "government-public-sector":
            return {
                "lead": "UK public-sector AI is governed by the Central Digital and Data Office (CDDO) AI guidance, Cabinet Office spend controls, and sector regulators. The pro-innovation approach emphasises responsible adoption through existing governance rather than a dedicated AI statute.",
                "requirements": [
                    ("CDDO Algorithmic Transparency Recording Standard", "Central government departments must publish algorithmic transparency records for AI used in decision-making, including purpose, data sources, and human oversight."),
                    ("Cabinet Office spend controls for AI", "High-risk or high-value AI procurements require approval through the Cabinet Office spend-control process, with scrutiny of ethics, data, and security."),
                    ("Sector regulator guidance", "Public-sector AI in health, policing, education, and transport must comply with guidance from the relevant sector regulator — MHRA, College of Policing, DfE, ORR, etc."),
                    ("Data ethics framework", "Government departments are expected to apply the UK Government Data Ethics Framework to AI projects, ensuring fairness, accountability, and transparency in public-service AI."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "manufacturing":
            return {
                "lead": "UK manufacturing AI is overseen by the HSE for health and safety, BEIS for product safety, and sector regulators for critical infrastructure. The pro-innovation approach means AI governance must align with existing health-and-safety and product-conformity frameworks.",
                "requirements": [
                    ("HSE guidance on AI & workplace safety", "The Health and Safety Executive expects manufacturers to assess AI-controlled machinery and robotics through existing risk-assessment frameworks, ensuring safe integration with human workers."),
                    ("Product safety & UKCA marking", "AI-enabled products placed on the UK market must satisfy relevant product-safety regulations and bear UKCA marking where required."),
                    ("BEIS & sector regulator expectations", "Manufacturers in critical sectors must align AI governance with sector-specific resilience and security guidance from relevant regulators."),
                    ("ICO guidance on employee data & AI", "The ICO expects DPIAs for AI processing employee biometric or behavioural data, with transparency and proportionality in worker monitoring."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "retail-ecommerce":
            return {
                "lead": "UK retail AI is overseen by the CMA for competition and consumer protection, the FCA for retail financial services, and the ICO for data protection. The sector-based approach requires alignment with existing consumer-rights and competition frameworks.",
                "requirements": [
                    ("CMA guidance on AI & consumer protection", "The Competition and Markets Authority expects retailers to ensure AI-driven pricing, recommendations, and advertising do not mislead consumers or engage in unfair commercial practices."),
                    ("FCA expectations for retail financial AI", "Retailers offering credit, insurance, or investment products must ensure AI systems comply with FCA conduct rules, including fairness and transparency."),
                    ("Consumer Duty & AI fairness", "The Consumer Duty requires retailers to demonstrate that AI systems deliver fair value and good outcomes for retail customers."),
                    ("ICO guidance on retail data & AI", "The ICO expects DPIAs for high-risk retail AI processing, with transparency about profiling and automated decisions and provision for human review."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "energy-utilities":
            return {
                "lead": "UK energy AI is overseen by Ofgem for gas and electricity, Ofwat for water, and the HSE for health and safety. The sector-based approach means AI governance must align with existing licence conditions, safety frameworks, and consumer-protection rules.",
                "requirements": [
                    ("Ofgem guidance on AI in energy", "Ofgem expects licensees to ensure AI systems supporting trading, billing, and customer service comply with licence conditions and do not produce unfairly discriminatory outcomes."),
                    ("HSE expectations for AI in safety-critical systems", "AI embedded in safety-critical energy infrastructure must be assessed through existing health-and-safety risk-assessment frameworks."),
                    ("Consumer Duty & vulnerable customers", "Energy suppliers must ensure AI-driven debt collection, payment-plan offers, and tariff recommendations do not harm vulnerable customers."),
                    ("ICO guidance on smart-meter data & AI", "The ICO expects DPIAs for high-risk processing of smart-meter data, with transparency and data-minimisation in AI-driven analytics."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "transportation-logistics":
            return {
                "lead": "UK transport AI is overseen by the DVSA for road vehicles, the ORR for rail, the CAA for aviation, and the MCA for maritime. The sector-based approach means AI governance must align with existing safety, licensing, and operational frameworks.",
                "requirements": [
                    ("DVSA guidance on AI in road vehicles", "The Driver and Vehicle Standards Agency expects AI-enabled vehicles and driver-monitoring systems to meet type-approval and safety-assessment requirements."),
                    ("ORR expectations for AI in rail", "The Office of Rail and Road requires AI systems supporting rail operations to satisfy safety-management system requirements and independent safety assessment."),
                    ("CAA guidance on AI in aviation", "The Civil Aviation Authority expects AI systems in aviation to meet airworthiness and operational-safety standards, with human oversight and redundancy."),
                    ("ICO guidance on transport data & AI", "The ICO expects DPIAs for high-risk processing of driver and passenger data, with transparency and data-minimisation in AI-driven analytics."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "media-publishing":
            return {
                "lead": "UK media AI is overseen by Ofcom for broadcast and online safety, the ICO for data protection, and the CMA for competition. The sector-based approach means AI governance must align with existing content standards, broadcasting codes, and online safety duties.",
                "requirements": [
                    ("Ofcom guidance on AI in broadcasting", "Ofcom expects broadcasters using AI for content generation, moderation, or scheduling to maintain editorial responsibility and comply with the Broadcasting Code."),
                    ("Online Safety Bill & AI moderation", "Under the Online Safety regime, platforms using AI for content moderation must demonstrate proportionate, accurate, and transparent systems that protect users from harm."),
                    ("CMA expectations for algorithmic transparency", "The Competition and Markets Authority expects media platforms to ensure AI-driven recommendations and advertising do not distort competition or mislead consumers."),
                    ("ICO guidance on audience data & AI", "The ICO expects DPIAs for high-risk processing of subscriber and viewer data, with transparency about profiling and automated decisions."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }
        if s == "nonprofit-ngo":
            return {
                "lead": "UK non-profit AI is overseen by the Charity Commission for charitable organisations, the ICO for data protection, and sector regulators for specific activities. The pro-innovation approach means AI governance must align with existing charitable-law and fiduciary obligations.",
                "requirements": [
                    ("Charity Commission guidance on AI", "The Charity Commission expects charities using AI to ensure it supports charitable purposes, does not harm beneficiaries, and maintains public trust and confidence."),
                    ("Fiduciary duties & AI governance", "Charity trustees remain personally responsible for AI-driven decisions affecting charitable operations, beneficiary welfare, and organisational reputation."),
                    ("Fundraising Regulator expectations", "Charities using AI for donor targeting and fundraising must comply with the Code of Fundraising Practice, ensuring transparency and respecting donor preferences."),
                    ("ICO guidance on beneficiary data & AI", "The ICO expects DPIAs for high-risk processing of beneficiary and donor data, with transparency and data-minimisation in AI-driven analytics."),
                ],
                "articles": ["Article 29 — Partnership Charter", "Article 33 — Transparency Obligations", "Article 47 — Audit Right", "Article 13 — Risk Management"],
                "mcps": ["meok-uk-ai-reg", "meok-deployer-pack", "meok-rms"],
            }

    # Fallback
    return {
        "lead": name + " organisations deploying AI must navigate " + reg["name"] + " requirements with sector-specific controls and governance.",
        "requirements": [
            ("Regulatory alignment", "Map " + reg["name"] + " obligations to " + name + " AI use cases and risk profiles."),
            ("Governance & oversight", "Establish accountable governance with documented human oversight for AI-driven decisions."),
            ("Risk management", "Implement continuous risk assessment, monitoring, and incident response tailored to " + name + " operations."),
        ],
        "articles": ["Article 13 — Risk Management", "Article 29 — Partnership Charter", "Article 33 — Transparency Obligations"],
        "mcps": ["meok-rms", "meok-deployer-pack"],
    }


def build_page(sector, reg, data):
    title = sector["name"] + " AI Compliance — " + reg["name"] + " | CSOAI"
    meta_desc = sector["name"] + " AI compliance under " + reg["name"] + ". Specific requirements, CSOAI Charter mappings, and relevant MEOK MCPs."
    h1 = sector["name"] + " AI Compliance: " + reg["name"]
    canonical = "https://csoai.org/sectors/" + sector["slug"] + "-" + reg["slug"]

    req_html = ""
    for req_title, req_desc in data.get("requirements", []):
        req_html += "<div class='requirement-box'><h3>" + req_title + "</h3><p>" + req_desc + "</p></div>\n"

    articles_html = ""
    for art in data.get("articles", []):
        articles_html += "<li>" + art + "</li>\n"

    mcps_html = ""
    for mcp in data.get("mcps", []):
        mcps_html += "<span class='mcp-tag'>" + mcp + "</span> "

    schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "headline": h1,
        "description": meta_desc,
        "datePublished": "2026-05-28",
        "publisher": {
            "@type": "Organization",
            "name": "CSOAI LTD",
            "identifier": "UK Companies House 16939677"
        },
        "author": {
            "@type": "Organization",
            "name": "CSOAI LTD"
        },
        "license": "https://creativecommons.org/licenses/by/4.0/",
        "url": canonical
    }

    breadcrumb_schema = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": "https://csoai.org"},
            {"@type": "ListItem", "position": 2, "name": "Sectors", "item": "https://csoai.org/sectors"},
            {"@type": "ListItem", "position": 3, "name": h1, "item": canonical}
        ]
    }

    html = """<!DOCTYPE html>
<html lang='en'><head><meta charset='utf-8'>
<title>""" + title + """</title>
<meta name='robots' content='index,follow'>
<meta name='description' content='""" + meta_desc + """'>
<link rel='canonical' href='""" + canonical + """'>
<meta property='og:title' content='""" + title + """'>
<meta property='og:description' content='""" + meta_desc + """'>
<meta property='og:type' content='article'>
<meta property='og:url' content='""" + canonical + """'>
<meta name='twitter:card' content='summary_large_image'>
<script type='application/ld+json'>""" + json.dumps(schema) + """</script>
<script type='application/ld+json'>""" + json.dumps(breadcrumb_schema) + """</script>
<style>
:root{--ink:#0f172a;--muted:#5a5e66;--gold:#c9a84c;--card:#f7f8fa;--border:#e6e8ec;--brand:#0a8a3f;--warn:#dc2626;--accent:#fef3c7}
*{box-sizing:border-box}
body{font-family:system-ui,-apple-system,sans-serif;max-width:980px;margin:2.5rem auto;padding:0 1.5rem;color:var(--ink);line-height:1.65}
nav.crumbs{font-size:.85rem;color:var(--muted);margin-bottom:1.5rem}
nav.crumbs a{color:var(--brand);text-decoration:none}
h1{margin:0 0 .5rem;font-size:2.1rem;letter-spacing:-.02em;line-height:1.2}
h2{margin-top:2.5rem;margin-bottom:.5rem;border-bottom:2px solid var(--brand);padding-bottom:.4rem;font-size:1.4rem}
h3{margin-top:1.5rem;margin-bottom:.3rem;font-size:1.05rem;color:var(--ink)}
a{color:var(--brand);text-decoration:none}
a:hover{text-decoration:underline}
.lead{color:var(--muted);font-size:1.1rem;max-width:760px;margin-top:.75rem}
.meta-bar{display:flex;flex-wrap:wrap;gap:.5rem;margin:1rem 0 0;align-items:center}
.tag{background:var(--card);color:var(--muted);padding:.25rem .7rem;border-radius:.3rem;font-size:.78rem;font-weight:500;border:1px solid var(--border)}
.alert{background:#fef3c7;border-left:4px solid #d97706;padding:1rem 1.25rem;margin:1.5rem 0;border-radius:.35rem;color:#78350f}
.alert strong{color:#92400e}
.mcp-tag{display:inline-block;background:#dcfce7;color:#14532d;font-size:.72rem;padding:.2rem .55rem;border-radius:.3rem;font-weight:600;text-transform:uppercase;letter-spacing:.05em;margin:.15rem .15rem .15rem 0}
.requirement-box{background:var(--card);border:1px solid var(--border);border-radius:.55rem;padding:1.1rem 1.25rem;margin:1rem 0}
.requirement-box h3{margin-top:0;font-size:1rem}
.requirement-box p{margin:.3rem 0;font-size:.92rem;color:var(--muted)}
.cta{background:linear-gradient(135deg,var(--brand) 0%,#076a30 100%);color:white;padding:1.5rem;border-radius:.55rem;margin:2rem 0;text-align:center}
.cta h2{color:white;border:none;margin-top:0;padding-bottom:.3rem}
.cta a{background:white;color:var(--brand);padding:.55rem 1.25rem;border-radius:.35rem;display:inline-block;margin:.3rem;font-weight:600;text-decoration:none}
.cta a:hover{background:#f0fdf4;text-decoration:none}
.foot{margin-top:3rem;color:#888;font-size:.85rem;border-top:1px solid var(--border);padding-top:1.5rem}
ul.articles{margin:.5rem 0 1rem;padding-left:1.2rem}
ul.articles li{margin:.35rem 0;font-size:.95rem}
</style>
</head><body>

<nav class='crumbs'><a href='/'>CSOAI</a> &middot; <a href='/sectors'>Sectors</a> &middot; <strong>""" + sector["name"] + """</strong> &middot; <strong>""" + reg["name"] + """</strong></nav>

<div style='display:flex;gap:.5rem;margin-bottom:.5rem'><span class='tag'>""" + reg["org"] + """</span> <span class='tag'>""" + reg["year"] + """</span></div>
<h1>""" + h1 + """</h1>
<p class='lead'>""" + data.get("lead", "") + """</p>

<div class='meta-bar'>
  <span class='tag'><strong>Sector:</strong> """ + sector["name"] + """</span>
  <span class='tag'><strong>Regulation:</strong> """ + reg["name"] + """</span>
  <span class='tag'><strong>CSOAI Articles:</strong> """ + str(len(data.get("articles", []))) + """ mapped</span>
</div>

<h2>Key Compliance Requirements</h2>
""" + req_html + """
<h2>CSOAI Charter Articles</h2>
<ul class='articles'>
""" + articles_html + """</ul>

<h2>Relevant MEOK MCPs</h2>
<p style='color:var(--muted);font-size:.9rem'>These MCP servers operationalise compliance for this sector and regulation:</p>
""" + mcps_html + """

<h2>Framework Reference</h2>
<p>See the full <a href='/frameworks/""" + reg["slug"] + """'>""" + reg["name"] + """ crosswalk</a> for clause-by-clause mappings to the CSOAI 52-Article Charter.</p>

<div class='cta'>
  <h2>Get CSOAI Certified</h2>
  <p style='color:#e6f7ec;margin:.5rem 0'>Free certification covers all 8 regulations across 12 sectors. Receive a signed badge with public verify URL.</p>
  <a href='/certify'>Get Free Certified &rarr;</a>
  <a href='/asti'>See AI Self-State Index</a>
  <a href='/frameworks'>All Frameworks</a>
</div>

<p class='foot'>&copy; 2026 CSOAI LTD (trading as MEOK AI Labs) &middot; UK Companies House <strong>16939677</strong><br>
Sector crosswalk &middot; CC BY 4.0 &middot; <a href='/methodology'>Methodology</a> &middot; <a href='mailto:nicholas@csoai.org'>Contact</a><br>
<em>"The ISO for AI safety."</em></p>

</body></html>"""
    return html


def main():
    count = 0
    for sector in SECTORS:
        for reg in REGULATIONS:
            data = get_content(sector, reg)
            html = build_page(sector, reg, data)
            filename = sector["slug"] + "-" + reg["slug"] + ".html"
            (OUTDIR / filename).write_text(html, encoding="utf-8")
            count += 1
            print("Wrote " + filename)
    print("\nDone: " + str(count) + " pages written to " + str(OUTDIR))


if __name__ == "__main__":
    main()
