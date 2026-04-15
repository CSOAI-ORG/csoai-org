import re
import html

articles = [
    (
        "blog-eu-ai-act-compliance",
        "EU AI Act Compliance: What Organizations Must Know by August 2026",
        "Regulation",
        "February 18, 2026",
        "8 min read",
        "The EU AI Act compliance deadline is approaching. We break down the key requirements, certification pathways, and critical timelines for organizations operating AI systems in European markets.",
        """<p>The European Union Artificial Intelligence Act represents the world's first comprehensive legal framework for AI systems. With full enforcement beginning in August 2026, organizations deploying AI in EU markets must understand their obligations and prepare accordingly.</p>
        <h2>Risk-Based Classification</h2>
        <p>The EU AI Act categorizes AI systems into four tiers: minimal risk, limited risk, high risk, and unacceptable risk. High-risk systems—those used in critical infrastructure, education, employment, and law enforcement—face the most stringent requirements, including conformity assessments, risk management systems, and post-market monitoring.</p>
        <h2>Compliance Timeline</h2>
        <p>Organizations should begin their compliance journey immediately. Key steps include conducting an AI inventory, classifying each system by risk level, implementing governance frameworks, and pursuing third-party certification. The CSOAI CASA certification aligns directly with EU AI Act requirements, providing a streamlined path to compliance.</p>
        <h2>Penalties and Enforcement</h2>
        <p>Non-compliance carries severe penalties: up to €35 million or 7% of global annual turnover, whichever is higher. National supervisory authorities will have powers to conduct audits, issue fines, and mandate corrective actions. Early preparation is not just advisable—it is essential.</p>
        <p>For organizations seeking a structured compliance pathway, CSOAI offers implementation guides, audit checklists, and CASA certification services designed specifically for EU AI Act readiness.</p>"""
    ),
    (
        "blog-casa-certification-levels",
        "CASA Certification Levels Explained: Commercial vs Government vs Defense",
        "Certification",
        "February 15, 2026",
        "10 min read",
        "Choosing the right certification tier depends on your organizational needs and risk profile. This comprehensive guide explains Level 1, 2, and 3 certifications and their practical applications.",
        """<p>The CSOAI AI Safety Accreditation (CASA) framework provides three certification levels, each designed for different operational contexts and risk exposures. Understanding these tiers is essential for selecting the right certification pathway.</p>
        <h2>Level 1: Commercial Certification</h2>
        <p>CASA Level 1 is designed for businesses deploying AI in consumer-facing or internal applications. It covers fundamental governance requirements, risk assessment protocols, and transparency obligations. This level is ideal for startups, SMEs, and enterprises operating in regulated but non-critical sectors.</p>
        <h2>Level 2: Government Certification</h2>
        <p>Level 2 addresses the needs of public sector organizations and government contractors. It incorporates additional requirements for algorithmic accountability, bias auditing, and citizen rights protection. Organizations achieving Level 2 certification demonstrate compliance with public procurement standards and international governance frameworks.</p>
        <h2>Level 3: Defense Certification</h2>
        <p>The most rigorous tier, CASA Level 3, is reserved for defense, national security, and critical infrastructure applications. It includes adversarial testing, red teaming, supply chain verification, and continuous monitoring. Level 3 certification is often a prerequisite for defense contracts and strategic AI partnerships.</p>
        <p>Each level builds upon the previous, creating a scalable governance maturity model. CSOAI's certification process includes documentation review, system testing, and ongoing surveillance to ensure maintained compliance.</p>"""
    ),
    (
        "blog-byzantine-consensus",
        "Byzantine Consensus Explained: How Distributed AI Governance Works",
        "Governance",
        "February 12, 2026",
        "12 min read",
        "Understanding Byzantine Fault Tolerance is crucial to CSOAI governance. Learn how distributed AI agents reach consensus using threshold voting to ensure secure decision-making.",
        """<p>At the heart of CSOAI's governance architecture lies a novel application of Byzantine Fault Tolerance (BFT)—a consensus mechanism designed to function correctly even when some participants fail or act maliciously. This approach ensures that AI governance decisions are resilient, transparent, and tamper-proof.</p>
        <h2>The Byzantine Generals Problem</h2>
        <p>Originally formulated in computer science, the Byzantine Generals Problem asks how distributed systems can agree on a single course of action when some nodes may be compromised. In the context of AI governance, this translates to ensuring that no single actor—human or machine—can unilaterally alter governance outcomes.</p>
        <h2>CSOAI's 33-Agent Council</h2>
        <p>CSOAI deploys a council of 33 distributed AI agents, each trained on different governance frameworks, regional regulations, and ethical principles. Decisions require a 22-of-33 supermajority, making it computationally infeasible for adversaries to corrupt the consensus process. This threshold is derived from rigorous cryptographic analysis of fault tolerance bounds.</p>
        <h2>Real-World Applications</h2>
        <p>Byzantine consensus governs critical CSOAI functions: charter amendments, certification appeals, cross-border reciprocity agreements, and emergency safety protocols. Every vote is recorded on an immutable ledger, providing full auditability for regulators and stakeholders.</p>
        <p>By combining classical distributed systems theory with modern AI, CSOAI creates a governance infrastructure that is both autonomous and accountable—a critical requirement for the next generation of artificial intelligence.</p>"""
    ),
    (
        "blog-iso-42001-nist-ai-rmf",
        "ISO 42001 and NIST AI RMF: Aligning Your Systems with Global Standards",
        "Standards",
        "February 10, 2026",
        "9 min read",
        "Multiple AI governance frameworks exist globally. We explain how ISO 42001, NIST AI RMF, and CSOAI standards complement each other and create a comprehensive governance approach.",
        """<p>Organizations navigating AI governance today face a landscape of overlapping standards and frameworks. ISO 42001, the NIST AI Risk Management Framework (AI RMF), and CSOAI's charter each offer valuable guidance. The key to effective governance is understanding how they interrelate.</p>
        <h2>ISO 42001: The Management System Standard</h2>
        <p>ISO 42001 provides a certifiable management system for AI, analogous to ISO 27001 for information security. It defines requirements for establishing, implementing, maintaining, and continually improving an AI management system within an organization. Certification to ISO 42001 demonstrates systematic governance to customers, regulators, and partners.</p>
        <h2>NIST AI RMF: The Risk-Focused Approach</h2>
        <p>The NIST AI RMF offers a voluntary, risk-based framework organized around four functions: Govern, Map, Measure, and Manage. It is particularly valuable for U.S. organizations and those seeking to align with federal procurement guidelines. Unlike ISO 42001, NIST AI RMF is not a certifiable standard but a practical methodology.</p>
        <h2>CSOAI: Certification and Implementation</h2>
        <p>CSOAI's standards and CASA certification program integrate both ISO 42001 and NIST AI RMF requirements. Our crosswalk documentation maps each CSOAI charter article to corresponding ISO and NIST controls, enabling organizations to achieve multiple alignments through a single certification process.</p>
        <p>For organizations operating globally, a unified approach to ISO 42001, NIST AI RMF, and CSOAI certification provides the strongest foundation for trustworthy, compliant AI deployment.</p>"""
    ),
    (
        "blog-ai-governance-trends-2026",
        "AI Governance Trends 2026: What's Changing in Regulation",
        "Governance",
        "February 8, 2026",
        "7 min read",
        "From mandatory auditing to algorithmic transparency requirements, AI governance is rapidly evolving. Here are the top trends shaping regulation in 2026 and beyond.",
        """<p>As artificial intelligence systems become more powerful and pervasive, regulators worldwide are accelerating their governance agendas. 2026 marks a pivotal year, with several major trends reshaping how organizations must approach AI compliance.</p>
        <h2>Mandatory Third-Party Auditing</h2>
        <p>Gone are the days of self-assessment sufficiency. The EU AI Act, emerging U.S. federal requirements, and sectoral regulations in finance and healthcare now mandate independent third-party audits for high-risk AI systems. Certification bodies like CSOAI are seeing unprecedented demand for CASA assessments.</p>
        <h2>Algorithmic Transparency and Explainability</h2>
        <p>Regulators and courts are increasingly demanding that organizations explain how their AI systems arrive at decisions. The "black box" defense is no longer acceptable in high-stakes domains. Organizations must invest in interpretability tools, documentation practices, and stakeholder communication.</p>
        <h2>Supply Chain Accountability</h2>
        <p>2026 brings expanded liability for AI supply chains. Organizations using third-party models, APIs, or training data must verify the governance practices of their vendors. Contractual AI safety clauses and vendor certification requirements are becoming standard.</p>
        <h2>Global Harmonization Efforts</h2>
        <p>While regional regulations differ, there is growing momentum toward mutual recognition of AI governance standards. Initiatives led by BSI, ISO, and CSOAI are creating pathways for certified systems to operate across jurisdictions with reduced friction.</p>
        <p>Organizations that stay ahead of these trends will not only avoid penalties but also gain competitive advantage through demonstrated trustworthiness.</p>"""
    ),
    (
        "blog-casa-certification-launch",
        "CASA Certification Launch: First Organizations Achieve AI Safety Certification",
        "Certification",
        "February 5, 2026",
        "6 min read",
        "CASA has certified the first wave of organizations across commercial, government, and defense sectors. Read the success stories and lessons learned from early adopters.",
        """<p>The launch of the CSOAI AI Safety Accreditation (CASA) program represents a milestone in operationalizing AI governance. The first cohort of certified organizations has completed the rigorous assessment process, setting benchmarks for the industry.</p>
        <h2>Early Adopter Profile</h2>
        <p>The inaugural certified organizations span healthcare diagnostics, financial services, defense contracting, and public sector AI deployment. Despite differing sectors, all shared a commitment to embedding governance into their AI development lifecycle rather than treating it as an afterthought.</p>
        <h2>Common Success Factors</h2>
        <p>Organizations that achieved certification most efficiently had three characteristics in common: executive sponsorship for AI governance, documented risk management processes, and cross-functional teams involving legal, technical, and operational stakeholders.</p>
        <h2>Lessons Learned</h2>
        <p>Early adopters reported that the most challenging aspects of certification were not technical but organizational: establishing clear accountability chains, maintaining documentation across iterative development, and aligning internal teams with external standards.</p>
        <p>CSOAI has incorporated these insights into updated implementation guides and streamlined audit protocols. For organizations considering CASA certification, the path is now clearer than ever.</p>"""
    ),
    (
        "blog-cmmc-for-ai",
        "CMMC for AI: Integrating Cybersecurity with AI Governance",
        "Regulation",
        "February 1, 2026",
        "8 min read",
        "The intersection of cybersecurity compliance and AI governance is becoming critical. Learn how CMMC applies to AI systems and organizations.",
        """<p>The Cybersecurity Maturity Model Certification (CMMC) is transforming how defense contractors and their supply chains approach information security. As AI systems increasingly handle controlled unclassified information (CUI) and support defense operations, integrating CMMC with AI governance has become essential.</p>
        <h2>CMMC Levels and AI Systems</h2>
        <p>CMMC defines three levels of cybersecurity maturity. AI systems processing defense-related data must meet the same controls as any other information system—plus additional considerations for model security, training data protection, and adversarial robustness. CMMC Level 2, aligned with NIST SP 800-171, is the baseline for most contractors.</p>
        <h2>AI-Specific Security Controls</h2>
        <p>Beyond standard cybersecurity practices, AI systems require specialized controls: protection of training datasets from poisoning, defense against model extraction attacks, monitoring for anomalous inference requests, and secure model deployment pipelines. CSOAI's CASA Level 3 certification explicitly addresses these requirements.</p>
        <h2>Integrated Compliance Strategy</h2>
        <p>Organizations pursuing both CMMC and CASA certification can benefit from significant overlap in documentation, risk assessment, and auditing processes. CSOAI offers integrated assessment pathways that reduce duplication and accelerate time-to-certification.</p>
        <p>For defense contractors and their AI vendors, the message is clear: cybersecurity and AI governance are no longer separate domains. Integrated compliance is the new standard.</p>"""
    ),
    (
        "blog-red-teaming-adversarial-testing",
        "Red Teaming and Adversarial Testing: Essential for AI Certification",
        "Standards",
        "January 29, 2026",
        "11 min read",
        "Robust security testing is non-negotiable for AI governance. This guide explains red teaming methodologies, adversarial testing approaches, and how AIdome conducts comprehensive vulnerability assessments.",
        """<p>As AI systems are deployed in high-stakes environments, traditional software testing is no longer sufficient. Red teaming and adversarial testing have emerged as critical disciplines for identifying vulnerabilities that conventional quality assurance misses.</p>
        <h2>What is AI Red Teaming?</h2>
        <p>AI red teaming involves simulating sophisticated attacks against AI systems to uncover failure modes, biases, security vulnerabilities, and harmful outputs. Unlike penetration testing, which focuses on infrastructure, red teaming probes the behavior of the model itself—its reasoning, its edge cases, and its potential for misuse.</p>
        <h2>Adversarial Testing Techniques</h2>
        <p>Adversarial testing includes prompt injection attacks, jailbreak attempts, data poisoning simulations, model inversion probes, and bias amplification tests. Each technique seeks to push the model outside its intended operating envelope and document the consequences.</p>
        <h2>The AIdome Assessment Framework</h2>
        <p>CSOAI's AIdome laboratory conducts standardized adversarial assessments as part of CASA certification. Tests are tailored to the system's deployment context: a customer service chatbot faces different threats than a medical diagnosis assistant. Results feed directly into risk registers and remediation plans.</p>
        <p>For organizations seeking CASA Level 2 or 3 certification, red teaming is not optional—it is a core requirement. The investment pays dividends in reduced liability, improved system robustness, and stakeholder confidence.</p>"""
    ),
    (
        "blog-ai-audit-best-practices",
        "AI Audit Best Practices: Preparing Your Organization for Compliance Assessments",
        "Governance",
        "January 26, 2026",
        "9 min read",
        "Pre-audit preparation can significantly improve certification outcomes. Discover the documentation, evidence collection, and stakeholder alignment needed for successful AI audits.",
        """<p>AI audits are becoming a routine part of operating in regulated markets. Whether pursuing CASA certification, EU AI Act conformity, or sector-specific compliance, preparation is the single greatest determinant of audit success.</p>
        <h2>Documentation Requirements</h2>
        <p>Auditors will expect comprehensive documentation covering your AI system's purpose, design, training data, model architecture, performance metrics, risk assessments, and governance controls. Documentation should be version-controlled, traceable, and accessible to non-technical reviewers.</p>
        <h2>Evidence Collection</h2>
        <p>Beyond documents, auditors seek evidence that controls are actually operating. This includes logs of model monitoring, incident response records, bias testing results, user feedback mechanisms, and management review meeting minutes. The strongest audit candidates can produce evidence on demand.</p>
        <h2>Stakeholder Alignment</h2>
        <p>Successful audits require coordination across legal, engineering, product, security, and executive teams. Designate a single point of contact for the audit, brief all interviewees on the scope and objectives, and ensure that answers are consistent across departments.</p>
        <h2>Common Pitfalls</h2>
        <p>The most common audit failures stem from gaps between stated policies and actual practices, incomplete risk assessments, and inability to explain model behavior. Addressing these gaps before the auditor arrives is far more cost-effective than remediating findings afterward.</p>
        <p>CSOAI provides pre-audit readiness assessments to help organizations identify and close gaps before formal certification audits begin.</p>"""
    ),
    (
        "blog-algorithmic-accountability",
        "Algorithmic Accountability and Transparency: Core Principles of AI Governance",
        "Standards",
        "January 23, 2026",
        "7 min read",
        "Accountability and transparency aren't optional—they're foundational to responsible AI. Learn how to implement explainability, audit trails, and accountability mechanisms in your AI systems.",
        """<p>The era of opaque AI decision-making is ending. Regulators, courts, and the public are demanding that organizations be accountable for the outputs of their AI systems. Transparency and accountability have moved from ethical aspirations to legal requirements.</p>
        <h2>Explainability by Design</h2>
        <p>Organizations must be able to explain how their AI systems arrive at consequential decisions. This does not always mean full technical interpretability—sometimes a clear description of the decision logic, data inputs, and known limitations is sufficient. The key is matching the level of explanation to the stakes of the decision.</p>
        <h2>Audit Trails and Logging</h2>
        <p>Every significant AI decision should be traceable to the version of the model, the input data, the environmental conditions, and the human oversight applied. Immutable audit trails provide the foundation for post-incident analysis, regulatory inquiries, and continuous improvement.</p>
        <h2>Accountability Mechanisms</h2>
        <p>Accountability requires more than documentation. It requires clear ownership: a designated individual or team responsible for AI system performance and compliance. It requires escalation paths for anomalies and harms. And it requires consequences for failures, just as there are for other operational risks.</p>
        <p>CSOAI's charter devotes multiple articles to algorithmic accountability, and CASA certification verifies that certified organizations have implemented robust transparency and accountability frameworks.</p>"""
    ),
    (
        "blog-proof-of-ai",
        "Proof of AI: Tokenizing Certification for Transparent Verification",
        "Certification",
        "January 20, 2026",
        "8 min read",
        "Blockchain-based Proof of AI tokens provide immutable verification of CASA certification. Understand how tokenization enhances transparency and enables secure third-party verification.",
        """<p>CSOAI is pioneering a new approach to certification verification: Proof of AI tokens. By recording CASA certifications on a distributed ledger, we create an immutable, publicly verifiable record of an organization's AI governance credentials.</p>
        <h2>The Problem with Traditional Certificates</h2>
        <p>Traditional certification documents can be forged, misrepresented, or silently revoked. Verifying a certificate typically requires contacting the issuing body, introducing delays and friction into procurement and partnership processes.</p>
        <h2>How Proof of AI Works</h2>
        <p>When an organization achieves CASA certification, CSOAI mints a unique Proof of AI token containing a cryptographic hash of the certification record. This token is stored on a public blockchain, while sensitive details remain off-chain. Anyone can verify the certification status by checking the token against CSOAI's registry.</p>
        <h2>Benefits for Organizations</h2>
        <p>Proof of AI enables instant verification by customers, regulators, and partners. It supports automated compliance checking in procurement systems. And it creates a transparent history of an organization's governance journey, including renewals, upgrades, and scope expansions.</p>
        <p>As AI supply chains become more complex, the ability to instantly verify a vendor's certification status will be a critical enabler of trust and efficiency.</p>"""
    ),
    (
        "blog-global-ai-governance-harmonization",
        "Global AI Governance Harmonization: BSI's Role in Mutual Recognition",
        "Regulation",
        "January 17, 2026",
        "10 min read",
        "International AI governance alignment is essential for global deployment. BSI coordinates standards reciprocity agreements that enable certified AI systems to operate across borders seamlessly.",
        """<p>For AI systems deployed across multiple jurisdictions, navigating a patchwork of national regulations is a major challenge. Global governance harmonization—through mutual recognition agreements and aligned standards—is essential for the next wave of AI adoption.</p>
        <h2>The Fragmentation Challenge</h2>
        <p>Today, organizations face differing requirements in the EU, United States, United Kingdom, China, and other major markets. Complying with each regime separately creates duplication, cost, and uncertainty. Harmonization reduces this burden by allowing a single compliance effort to satisfy multiple jurisdictions.</p>
        <h2>BSI and Mutual Recognition</h2>
        <p>The British Standards Institution (BSI) plays a leading role in coordinating mutual recognition agreements for AI governance standards. Through BSI-facilitated reciprocity, CASA-certified organizations can more easily demonstrate compliance with UK, Commonwealth, and aligned international requirements.</p>
        <h2>CSOAI's Cross-Border Framework</h2>
        <p>CSOAI actively participates in harmonization initiatives, mapping CASA requirements to the EU AI Act, NIST AI RMF, ISO 42001, and emerging standards in the Asia-Pacific region. Our crosswalks and joint audit programs help organizations achieve multi-jurisdictional compliance efficiently.</p>
        <p>For globally operating organizations, investing in harmonized certification is not just a compliance strategy—it is a competitive advantage.</p>"""
    ),
    (
        "blog-ai-risk-register",
        "Building Your AI Risk Register: A Step-by-Step Framework",
        "Governance",
        "January 14, 2026",
        "6 min read",
        "Risk identification and management are central to AI governance. Learn how to develop a comprehensive AI risk register that aligns with ISO 42001 and CSOAI standards.",
        """<p>A well-maintained AI risk register is the cornerstone of effective AI governance. It provides a structured record of identified risks, their likelihood and impact, mitigation strategies, and accountability assignments. For organizations pursuing ISO 42001 or CASA certification, the risk register is a critical audit artifact.</p>
        <h2>Step 1: Inventory Your AI Systems</h2>
        <p>Before you can assess risks, you need to know what AI systems your organization operates. Create an inventory that includes internal tools, customer-facing applications, embedded AI in products, and third-party services. For each system, document its purpose, data inputs, decision authority, and stakeholders.</p>
        <h2>Step 2: Identify and Assess Risks</h2>
        <p>For each system, identify risks across categories: accuracy and performance, bias and fairness, security and privacy, transparency and explainability, and operational resilience. Assess each risk by likelihood and impact, using a consistent scoring methodology.</p>
        <h2>Step 3: Define Controls and Owners</h2>
        <p>For each significant risk, define mitigation controls and assign clear ownership. Controls should be specific, measurable, and time-bound. Owners should have the authority and resources to implement and maintain the controls.</p>
        <h2>Step 4: Review and Update</h2>
        <p>A risk register is a living document. Schedule regular reviews—at least quarterly—and update the register whenever systems change, incidents occur, or regulations evolve. Auditors will expect to see evidence of ongoing maintenance.</p>
        <p>CSOAI provides a free AI risk register template and detailed guidance to help organizations get started.</p>"""
    ),
]

# We use string.Template-style replacement for footer to avoid brace conflicts
from string import Template

TEMPLATE_HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>''' + html.escape("{title}") + ''' | CSOAI Blog</title>
    <meta name="description" content="''' + html.escape("{description}") + '''">
    <meta name="theme-color" content="#0D0B21">
    <meta property="og:title" content="''' + html.escape("{title}") + '''">
    <meta property="og:description" content="''' + html.escape("{description}") + '''">
    <meta property="og:type" content="article">
    <meta property="og:url" content="https://csoai.org/''' + "{slug}" + '''.html">
    <meta name="twitter:card" content="summary_large_image">
    <meta property="og:image" content="https://csoai.org/assets/og-image.png">
    <link rel="canonical" href="https://csoai.org/''' + "{slug}" + '''.html">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap" rel="stylesheet">

    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root {
            --color-dark: #0D0B21;
            --color-dark-light: #1A1145;
            --color-accent: #D4A843;
            --color-accent-bright: #E8B76D;
            --color-text: #E8E4F0;
            --color-white: #FFFFFF;
            --color-glass-bg: rgba(255, 255, 255, 0.03);
            --color-glass-border: rgba(255, 255, 255, 0.08);
            --easing: cubic-bezier(0.16, 1, 0.3, 1);
        }
        html { scroll-behavior: smooth; }
        body {
            font-family: 'Inter', sans-serif;
            background: linear-gradient(135deg, var(--color-dark) 0%, var(--color-dark-light) 100%);
            color: var(--color-text);
            line-height: 1.7;
            overflow-x: hidden;
        }
        body::before {
            content: '';
            position: fixed;
            top: 0; left: 0; width: 100%; height: 100%;
            background-image: radial-gradient(circle, rgba(212, 168, 67, 0.15) 1px, transparent 1px);
            background-size: 50px 50px;
            pointer-events: none;
            z-index: 0;
            animation: drift 20s ease-in-out infinite;
        }
        @keyframes drift { 0%,100%{background-position:0 0} 50%{background-position:20px 20px} }
        @keyframes fadeUp { from{opacity:0;transform:translateY(60px)} to{opacity:1;transform:translateY(0)} }
        @keyframes slideDown { from{opacity:0;transform:translateY(-30px)} to{opacity:1;transform:translateY(0)} }
        main { position: relative; z-index: 1; }
        h1 { font-size: clamp(2rem, 5vw, 3.5rem); font-weight: 800; line-height: 1.2; color: var(--color-white); margin-bottom: 1.5rem; }
        h2 { font-size: clamp(1.5rem, 3vw, 2rem); font-weight: 700; color: var(--color-white); margin: 2.5rem 0 1rem; }
        h3 { font-size: 1.25rem; font-weight: 600; color: var(--color-white); margin: 1.5rem 0 0.75rem; }
        p { font-size: 1.05rem; line-height: 1.8; color: var(--color-text); margin-bottom: 1.25rem; }
        ul, ol { margin: 1rem 0 1.5rem 1.5rem; color: var(--color-text); }
        li { margin-bottom: 0.5rem; line-height: 1.7; }
        .btn {
            display: inline-flex; align-items: center; justify-content: center; gap: 0.5rem;
            padding: 1rem 2rem;
            background: linear-gradient(135deg, var(--color-accent) 0%, var(--color-accent-bright) 100%);
            color: var(--color-dark); border: none; border-radius: 12px; font-weight: 600; font-size: 1rem;
            cursor: pointer; transition: all 0.3s ease;
            box-shadow: 0 10px 30px rgba(212, 168, 67, 0.25); text-decoration: none; position: relative; overflow: hidden;
        }
        .btn:hover { transform: scale(1.02); box-shadow: 0 15px 45px rgba(212, 168, 67, 0.4); }
        .btn-secondary { background: transparent; color: var(--color-accent); border: 2px solid var(--color-accent); box-shadow: none; }
        .btn-secondary:hover { background: rgba(212, 168, 67, 0.1); box-shadow: 0 0 20px rgba(212, 168, 67, 0.2); }
        section { max-width: 1400px; margin: 0 auto; padding: 80px 2rem; position: relative; z-index: 1; }
        .article-content { max-width: 800px; margin: 0 auto; }
        .article-meta-bar {
            display: flex; gap: 1.5rem; align-items: center; flex-wrap: wrap;
            margin-bottom: 2rem; padding-bottom: 1.5rem; border-bottom: 1px solid var(--color-glass-border);
        }
        .article-category {
            display: inline-block; padding: 0.4rem 1rem; background: rgba(212, 168, 67, 0.15);
            color: var(--color-accent); border-radius: 20px; font-size: 0.75rem; font-weight: 600;
        }
        .article-date { font-size: 0.9rem; color: rgba(232, 228, 240, 0.7); }
        .article-readtime { font-size: 0.9rem; color: rgba(232, 228, 240, 0.7); }
        .newsletter {
            background: var(--color-glass-bg); border: 1px solid var(--color-glass-border);
            backdrop-filter: blur(20px); border-radius: 16px; padding: 3rem; text-align: center;
            margin-top: 4rem; max-width: 600px; margin-left: auto; margin-right: auto;
        }
        .newsletter h3 { margin-bottom: 1rem; }
        .newsletter-form { display: flex; gap: 1rem; margin-top: 1.5rem; flex-wrap: wrap; }
        .newsletter-form input {
            flex: 1; min-width: 200px; padding: 0.875rem 1.5rem;
            background: rgba(255, 255, 255, 0.08); border: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 8px; color: var(--color-white); font-family: inherit; font-size: 1rem;
        }
        .newsletter-form input::placeholder { color: rgba(232, 228, 240, 0.5); }
        .newsletter-form input:focus { outline: none; background: rgba(255, 255, 255, 0.12); border-color: var(--color-accent); }
        .sticky-bar {
            position: fixed; bottom: 0; left: 0; right: 0; z-index: 99; padding: 1.5rem 2rem;
            background: rgba(13, 11, 33, 0.8); backdrop-filter: blur(10px);
            border-top: 1px solid rgba(255, 255, 255, 0.08);
            display: flex; justify-content: space-between; align-items: center; gap: 2rem; flex-wrap: wrap;
        }
        .sticky-message { font-size: 1rem; font-weight: 500; color: var(--color-text); flex: 1; min-width: 200px; }
        .cookie-banner {
            position: fixed; bottom: 80px; left: 2rem; z-index: 98;
            background: var(--color-glass-bg); border: 1px solid var(--color-glass-border);
            backdrop-filter: blur(20px); border-radius: 16px; padding: 1.5rem; max-width: 300px;
            animation: slideUp 0.5s ease;
        }
        @keyframes slideUp { from{transform: translateY(100px); opacity: 0} to{transform: translateY(0); opacity: 1} }
        .cookie-text { font-size: 0.85rem; color: var(--color-text); margin-bottom: 1rem; }
        .cookie-buttons { display: flex; gap: 0.75rem; flex-direction: column; }
        .cookie-buttons button { padding: 0.5rem 1rem; border: none; border-radius: 6px; font-weight: 600; font-size: 0.85rem; cursor: pointer; transition: all 0.3s ease; }
        .cookie-accept { background: var(--color-accent); color: var(--color-dark); }
        .cookie-accept:hover { transform: scale(1.02); }
        .cookie-decline { background: transparent; color: var(--color-accent); border: 1px solid var(--color-accent); }
        footer { background: linear-gradient(135deg, #0A0820 0%, #0D0B21 100%); padding: 4rem 2rem 2rem; margin-top: 6rem; border-top: 1px solid rgba(255, 255, 255, 0.05); position: relative; z-index: 2; }
        .footer-content { max-width: 1400px; margin: 0 auto; display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 3rem; margin-bottom: 3rem; }
        .footer-section h4 { color: var(--color-accent); font-size: 0.9rem; text-transform: uppercase; letter-spacing: 1px; margin-bottom: 1.5rem; font-weight: 700; }
        .footer-section ul { list-style: none; }
        .footer-section a { color: var(--color-text); text-decoration: none; font-size: 0.95rem; display: block; margin-bottom: 0.75rem; transition: color 0.3s ease; }
        .footer-section a:hover { color: var(--color-accent); }
        .footer-bottom { border-top: 1px solid rgba(255, 255, 255, 0.05); padding-top: 2rem; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 1rem; font-size: 0.9rem; color: var(--color-text); max-width: 1400px; margin: 0 auto; }
        .social-links { display: flex; gap: 1.5rem; }
        .social-links a { color: var(--color-text); text-decoration: none; transition: color 0.3s ease; }
        .social-links a:hover { color: var(--color-accent); }
        @media (max-width: 1024px) {
            .sticky-bar { flex-direction: column; padding: 1rem; }
            .sticky-bar .btn { width: 100%; }
            .footer-content { grid-template-columns: repeat(2, 1fr); }
        }
        @media (max-width: 768px) {
            section { padding: 60px 1.5rem; }
            h1 { font-size: 1.75rem; }
            h2 { font-size: 1.5rem; }
            .sticky-bar { bottom: 60px; }
            .cookie-banner { left: 1rem; right: 1rem; max-width: none; bottom: 70px; }
            .footer-content { grid-template-columns: 1fr; }
        }
        @media (max-width: 480px) {
            section { padding: 50px 1rem; }
            .btn { width: 100%; }
            .sticky-bar { bottom: 50px; padding: 0.75rem; gap: 1rem; }
            .sticky-message { text-align: center; font-size: 0.9rem; }
            .cookie-banner { left: 0.5rem; right: 0.5rem; bottom: 60px; padding: 1rem; }
        }
    </style>
</head>
<body>
    <main>
'''

TEMPLATE_NAV = '''
<!-- ═══ MEGA NAV ═══ -->
<header style="position:sticky;top:0;z-index:1000;background:rgba(13,11,33,.97);backdrop-filter:blur(16px);border-bottom:1px solid rgba(212,168,67,.15);padding:.75rem 2rem;display:flex;justify-content:space-between;align-items:center">
  <a href="index.html" style="font-family:'Space Grotesk',sans-serif;font-size:1.5rem;font-weight:800;background:linear-gradient(135deg,#D4A843,#E8B76D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-decoration:none">CSOAI</a>
  <div style="display:flex;align-items:center;gap:.25rem" class="nav-links">
    <div class="mega-wrap" style="position:relative">
      <button onclick="toggleMega(this)" style="background:none;border:none;color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;cursor:pointer;font-family:inherit">Standards ▾</button>
      <div class="mega-panel" style="display:none;position:absolute;top:100%;left:-100px;width:520px;background:rgba(13,11,33,.98);border:1px solid rgba(212,168,67,.2);border-radius:12px;padding:1.5rem;margin-top:.5rem;box-shadow:0 20px 60px rgba(0,0,0,.5);backdrop-filter:blur(20px);z-index:999">
        <div style="color:var(--accent);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:.75rem">Governance Frameworks</div>
        <a href="charter.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">📜</span><span><strong style="display:block;font-size:.9rem">52-Article Charter</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Complete governance framework</small></span></a>
        <a href="crosswalks.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🔄</span><span><strong style="display:block;font-size:.9rem">Framework Crosswalks</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">ISO 42001, NIST, EU AI Act, IEEE</small></span></a>
        <a href="guides.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">📖</span><span><strong style="display:block;font-size:.9rem">Implementation Guides</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">8 step-by-step modules</small></span></a>
        <a href="glossary.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">📚</span><span><strong style="display:block;font-size:.9rem">AI Safety Glossary</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">250+ terms defined</small></span></a>
      </div>
    </div>
    <div class="mega-wrap" style="position:relative">
      <button onclick="toggleMega(this)" style="background:none;border:none;color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;cursor:pointer;font-family:inherit">Products ▾</button>
      <div class="mega-panel" style="display:none;position:absolute;top:100%;left:-100px;width:520px;background:rgba(13,11,33,.98);border:1px solid rgba(212,168,67,.2);border-radius:12px;padding:1.5rem;margin-top:.5rem;box-shadow:0 20px 60px rgba(0,0,0,.5);backdrop-filter:blur(20px);z-index:999">
        <div style="color:var(--accent);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:.75rem">CSOAI Products & Services</div>
        <a href="certification.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🏅</span><span><strong style="display:block;font-size:.9rem">CASA Certification</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Industry-standard AI safety certification</small></span></a>
        <a href="enterprise.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🏢</span><span><strong style="display:block;font-size:.9rem">Enterprise Governance</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Turnkey compliance for organisations</small></span></a>
        <a href="advisory.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🎯</span><span><strong style="display:block;font-size:.9rem">Advisory Services</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Expert AI governance consultancy</small></span></a>
        <a href="pricing.html" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">💰</span><span><strong style="display:block;font-size:.9rem">Pricing & Plans</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">From startup to government scale</small></span></a>
      </div>
    </div>
    <div class="mega-wrap" style="position:relative">
      <button onclick="toggleMega(this)" style="background:none;border:none;color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;cursor:pointer;font-family:inherit">Ecosystem ▾</button>
      <div class="mega-panel" style="display:none;position:absolute;top:100%;right:0;width:520px;background:rgba(13,11,33,.98);border:1px solid rgba(212,168,67,.2);border-radius:12px;padding:1.5rem;margin-top:.5rem;box-shadow:0 20px 60px rgba(0,0,0,.5);backdrop-filter:blur(20px);z-index:999">
        <div style="color:var(--accent);font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:2px;margin-bottom:.75rem">CSOAI Group Network</div>
        <a href="https://meok.ai" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🧠</span><span><strong style="display:block;font-size:.9rem">MEOK.AI</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Sovereign AI OS &amp; agent marketplace</small></span></a>
        <a href="https://csga-global.vercel.app" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🌐</span><span><strong style="display:block;font-size:.9rem">CSGA Global</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Education & workforce development</small></span></a>
        <a href="https://csga-ai.vercel.app" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🔬</span><span><strong style="display:block;font-size:.9rem">CSGA AI Research</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">150+ peer-reviewed publications</small></span></a>
        <a href="https://bmcc-cyber.vercel.app" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🎓</span><span><strong style="display:block;font-size:.9rem">BMCC Cybersecurity</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">US education partner</small></span></a>
        <a href="https://terranova-secdef.vercel.app" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🛡️</span><span><strong style="display:block;font-size:.9rem">Terranova SecDef</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">Defence & government AI safety</small></span></a>
        <a href="https://orbit-q.vercel.app" style="display:flex;align-items:flex-start;gap:.75rem;padding:.6rem;border-radius:8px;text-decoration:none;color:var(--text);transition:background .2s" onmouseover="this.style.background='rgba(212,168,67,.1)'" onmouseout="this.style.background='transparent'"><span style="font-size:1.2rem">🔮</span><span><strong style="display:block;font-size:.9rem">Orbit-Q</strong><small style="color:rgba(232,228,240,.5);font-size:.8rem">QA testing & red team ops</small></span></a>
      </div>
    </div>
    <a href="about.html" style="color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='var(--text)'">About</a>
    <a href="blog.html" style="color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='var(--text)'">Blog</a>
    <a href="contact.html" style="color:var(--text);padding:.5rem 1rem;font-size:.9rem;font-weight:500;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='var(--text)'">Contact</a>
    <a href="dashboard.html" style="background:linear-gradient(135deg,#D4A843,#E8B76D);color:#0D0B21;padding:.5rem 1.25rem;border-radius:8px;font-size:.85rem;font-weight:700;text-decoration:none;margin-left:.5rem;transition:transform .2s,box-shadow .2s;box-shadow:0 4px 15px rgba(212,168,67,.3)" onmouseover="this.style.transform='translateY(-1px)';this.style.boxShadow='0 6px 20px rgba(212,168,67,.5)'" onmouseout="this.style.transform='none';this.style.boxShadow='0 4px 15px rgba(212,168,67,.3)'">Dashboard</a>
  </div>
  <button class="hamburger" onclick="document.querySelector('.nav-links').classList.toggle('mobile-open');this.classList.toggle('active')" style="display:none;flex-direction:column;gap:5px;background:none;border:none;cursor:pointer;padding:8px;z-index:1001"><span style="width:24px;height:2px;background:var(--accent);border-radius:2px;transition:all .3s"></span><span style="width:24px;height:2px;background:var(--accent);border-radius:2px;transition:all .3s"></span><span style="width:24px;height:2px;background:var(--accent);border-radius:2px;transition:all .3s"></span></button>
</header>
<script>
function toggleMega(btn){
  const panel=btn.nextElementSibling;
  const wasOpen=panel.style.display==='block';
  document.querySelectorAll('.mega-panel').forEach(p=>p.style.display='none');
  if(!wasOpen)panel.style.display='block';
}
document.addEventListener('click',e=>{if(!e.target.closest('.mega-wrap'))document.querySelectorAll('.mega-panel').forEach(p=>p.style.display='none')});
</script>
'''

# Use simple string replacement for footer
FOOTER_BEFORE_JSON = '''
        <div class="newsletter">
            <h3>Stay Updated on AI Governance</h3>
            <p>Get weekly articles on certification, regulation, and AI safety best practices delivered to your inbox.</p>
            <form class="newsletter-form" onsubmit="event.preventDefault(); alert('Thank you for subscribing!');">
                <input type="email" placeholder="your@email.com" required>
                <button type="submit" class="btn">Subscribe</button>
            </form>
        </div>
    </section>
</main>

<div class="sticky-bar">
    <span class="sticky-message">Get your organization AI-certified before the August 2026 deadline.</span>
    <a href="contact.html" class="btn">Get Started →</a>
</div>

<div class="cookie-banner" id="cookieBanner">
    <p class="cookie-text">We use cookies to enhance your experience and analyze site performance.</p>
    <div class="cookie-buttons">
        <button class="cookie-accept" onclick="closeCookieBanner()">Accept All</button>
        <button class="cookie-decline" onclick="closeCookieBanner()">Decline</button>
    </div>
</div>

<footer style="background:var(--dark);border-top:3px solid var(--accent);padding:4rem 0 2rem;margin-top:4rem;position:relative;z-index:1">
<div class="container">
  <div style="display:grid;grid-template-columns:2fr 1fr 1fr 1fr 1fr 1fr;gap:2rem;margin-bottom:3rem">
    <div>
      <div style="font-family:'Space Grotesk',sans-serif;font-size:1.4rem;font-weight:800;background:linear-gradient(135deg,#D4A843,#E8B76D);-webkit-background-clip:text;-webkit-text-fill-color:transparent;margin-bottom:.75rem">CSOAI</div>
      <p style="color:rgba(232,228,240,.6);font-size:.9rem;line-height:1.6;margin-bottom:1rem">The global standard for AI safety. Institutional governance through the 52-article charter and Byzantine consensus.</p>
      <div style="display:flex;gap:.75rem"><a href="#" style="color:rgba(232,228,240,.5);font-size:1.2rem;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.5)'">𝕏</a><a href="#" style="color:rgba(232,228,240,.5);font-size:1.2rem;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.5)'">in</a><a href="#" style="color:rgba(232,228,240,.5);font-size:1.2rem;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.5)'">▶</a></div>
    </div>
    <div><h4 style="color:var(--accent);font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem;font-family:'Space Grotesk',sans-serif">Standards</h4><a href="charter.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Charter</a><a href="crosswalks.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Crosswalks</a><a href="guides.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Guides</a><a href="glossary.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Glossary</a></div>
    <div><h4 style="color:var(--accent);font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem;font-family:'Space Grotesk',sans-serif">Products</h4><a href="certification.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Certification</a><a href="enterprise.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Enterprise</a><a href="advisory.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Advisory</a><a href="pricing.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Pricing</a></div>
    <div><h4 style="color:var(--accent);font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem;font-family:'Space Grotesk',sans-serif">Ecosystem</h4><a href="https://meok.ai" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">MEOK.AI</a><a href="https://csga-global.vercel.app" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">CSGA Global</a><a href="https://csga-ai.vercel.app" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">CSGA AI Research</a><a href="https://bmcc-cyber.vercel.app" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">BMCC Cyber</a><a href="https://terranova-secdef.vercel.app" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Terranova SecDef</a></div>
    <div><h4 style="color:var(--accent);font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem;font-family:'Space Grotesk',sans-serif">Company</h4><a href="about.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">About</a><a href="case-studies.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Case Studies</a><a href="blog.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Blog</a><a href="contact.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Contact</a></div>
    <div><h4 style="color:var(--accent);font-size:.8rem;text-transform:uppercase;letter-spacing:2px;margin-bottom:1rem;font-family:'Space Grotesk',sans-serif">Account</h4><a href="dashboard.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Dashboard</a><a href="faq.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">FAQ</a><a href="resources.html" style="display:block;color:rgba(232,228,240,.6);font-size:.85rem;padding:.3rem 0;text-decoration:none;transition:color .2s" onmouseover="this.style.color='#D4A843'" onmouseout="this.style.color='rgba(232,228,240,.6)'">Resources</a></div>
  </div>
  <div style="border-top:1px solid rgba(212,168,67,.1);padding-top:1.5rem;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:1rem">
    <p style="color:rgba(232,228,240,.4);font-size:.8rem">&copy; 2026 CSOAI — The Global Standard for AI Safety. All rights reserved.</p>
    <div style="display:flex;gap:1.5rem"><a href="privacy.html" style="color:rgba(232,228,240,.4);font-size:.8rem;text-decoration:none">Privacy</a><a href="terms.html" style="color:rgba(232,228,240,.4);font-size:.8rem;text-decoration:none">Terms</a><a href="cookies.html" style="color:rgba(232,228,240,.4);font-size:.8rem;text-decoration:none">Cookies</a></div>
  </div>
</div>
</footer>

<script>
function closeCookieBanner() {
    const banner = document.getElementById('cookieBanner');
    banner.style.animation = 'slideUp 0.5s ease forwards';
    setTimeout(() => banner.remove(), 500);
    localStorage.setItem('csoai-cookie-consent', 'true');
}
if (localStorage.getItem('csoai-cookie-consent') === 'true') {
    const banner = document.getElementById('cookieBanner');
    if (banner) banner.style.display = 'none';
}
</script>

<script type="application/ld+json">
'''

def iso_date(date_str):
    months = {
        'January': '01', 'February': '02', 'March': '03', 'April': '04',
        'May': '05', 'June': '06', 'July': '07', 'August': '08',
        'September': '09', 'October': '10', 'November': '11', 'December': '12'
    }
    parts = date_str.replace(',', '').split()
    return f"{parts[2]}-{months[parts[0]]}-{int(parts[1]):02d}"

def generate():
    base = '/Users/nicholas/CSOAI-CORP/vercel-sites/csoai-org/'
    
    for slug, title, category, date, read_time, excerpt, content in articles:
        desc = html.escape(excerpt)
        date_iso = iso_date(date)
        
        head = TEMPLATE_HEAD.replace("{title}", html.escape(title)).replace("{description}", desc).replace("{slug}", slug)
        body = f'''
{TEMPLATE_NAV}
<section style="animation:fadeUp 0.8s var(--easing) backwards;">
    <div class="article-content">
        <span class="article-category">{category}</span>
        <h1>{html.escape(title)}</h1>
        <div class="article-meta-bar">
            <span class="article-date">{date}</span>
            <span class="article-readtime">{read_time}</span>
        </div>
        {content}
    </div>
'''
        json_ld = f'''{{
    "@context": "https://schema.org",
    "@type": "BlogPosting",
    "headline": "{html.escape(title)}",
    "description": "{desc}",
    "url": "https://csoai.org/{slug}.html",
    "datePublished": "{date_iso}",
    "author": {{
        "@type": "Organization",
        "name": "CSOAI"
    }},
    "publisher": {{
        "@type": "Organization",
        "name": "CSOAI",
        "logo": {{
            "@type": "ImageObject",
            "url": "https://csoai.org/assets/og-image.png"
        }}
    }}
}}
</script>
</body>
</html>
'''
        
        with open(base + slug + '.html', 'w', encoding='utf-8') as f:
            f.write(head + body + FOOTER_BEFORE_JSON + json_ld)
        print(f"Created {slug}.html")
    
    # Update blog.html
    with open(base + 'blog.html', 'r', encoding='utf-8') as f:
        blog_html = f.read()
    
    for slug, title, category, date, read_time, excerpt, content in articles:
        old_href = 'contact.html?inquiry=blog-subscribe'
        escaped_title = re.escape(title)
        pattern = re.compile(
            r'(<h3 class="article-title">' + escaped_title + r'</h3>.*?<a href=")' + re.escape(old_href) + r'(" class="read-more">Read More →</a>)',
            re.DOTALL
        )
        replacement = r'\1' + slug + '.html' + r'\2'
        blog_html, count = pattern.subn(replacement, blog_html)
        if count == 0:
            print(f"WARNING: Could not find link for {title}")
        else:
            print(f"Updated blog.html link for {title}")
    
    with open(base + 'blog.html', 'w', encoding='utf-8') as f:
        f.write(blog_html)
    print("Updated blog.html")

if __name__ == '__main__':
    generate()
