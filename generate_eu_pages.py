#!/usr/bin/env python3
"""Generate the four missing EU AI Act compliance pages for csoai.org.

Uses public/article-50-kit.html as the template so header, nav, footer,
Stripe buy-buttons and countdown banner stay identical.
"""
import json
from pathlib import Path

ROOT = Path(__file__).parent
TEMPLATE = ROOT / "public" / "article-50-kit.html"
OUT_DIR = ROOT / "public"

PAGES = {
    "eu-code-of-practice": {
        "title": "EU AI Act Code of Practice — CSOAI",
        "description": "What the EU AI Act Code of Practice means for GPAI providers and deployers. Second-draft obligations, risk taxonomy, and CSOAI's compliance route.",
        "h1": "EU AI Act Code of Practice",
        "countdown": "Deadline: August 2, 2026 — Act Now",
        "schema_type": "Article",
        "schema_headline": "EU AI Act Code of Practice Explained",
        "body": """
        <section class="problem-section">
            <h2>What is the Code of Practice?</h2>
            <p>The EU AI Act Code of Practice is the practical rulebook that general-purpose AI (GPAI) model providers must follow to meet their obligations under Articles 52–56. It translates high-level legal requirements into concrete technical and governance measures.</p>
        </section>

        <section class="problem-section">
            <h2>Who it applies to</h2>
            <ul style="color: var(--muted); margin-left: 1.5rem; line-height: 2;">
                <li>Providers of GPAI models released in the EU market</li>
                <li>Model providers with systemic risk above 10^25 FLOP</li>
                <li>Downstream deployers of high-risk AI systems</li>
                <li>Any organisation distributing AI-generated content to EU users</li>
            </ul>
        </section>

        <section class="problem-section">
            <h2>Key obligations</h2>
            <div class="kit-grid">
                <div class="feature-card"><h3>Transparency reporting</h3><p>Publish model capabilities, limitations, and risk mitigations in standardised templates.</p></div>
                <div class="feature-card"><h3>Copyright & data governance</h3><p>Document training-data sourcing, opt-outs, and reservation-of-rights compliance.</p></div>
                <div class="feature-card"><h3>Systemic-risk management</h3><p>Conduct red-teaming, adversarial testing, and incident reporting for high-impact models.</p></div>
                <div class="feature-card"><h3>Third-party evaluation</h3><p>Allow independent assessors to verify claims against the Code of Practice.</p></div>
            </div>
        </section>

        <section class="problem-section">
            <h2>Second-draft changes</h2>
            <p>The June 2025 second draft tightens systemic-risk thresholds, adds qualitative criteria for dangerous capabilities, and requires documented down-streaming of safety mitigations through the value chain.</p>
        </section>

        <div class="cta-box">
            <h2 style="font-size: 2rem; margin-bottom: 1rem; color: var(--primary);">Map the Code to your systems</h2>
            <p style="margin-bottom: 2rem; color: var(--muted);">CSOAI's Article 50 Emergency Kit converts Code-of-Practice obligations into filed documentation, checklists, and a public attestation chain.</p>
            <a href="article-50-kit.html" class="btn">GET THE ARTICLE 50 KIT</a>
        </div>
        """,
    },
    "article-50-transparency": {
        "title": "Article 50 Transparency Obligations — CSOAI",
        "description": "Plain-language guide to EU AI Act Article 50 transparency requirements for AI-generated content, chatbots, and deepfakes.",
        "h1": "Article 50 Transparency",
        "countdown": "Synthetic content must be disclosed by August 2, 2026",
        "schema_type": "Article",
        "schema_headline": "EU AI Act Article 50 Transparency Obligations",
        "body": """
        <section class="problem-section">
            <h2>What Article 50 requires</h2>
            <p>Article 50 of the EU AI Act mandates that providers and deployers make it clear when users are interacting with an AI system, when content is AI-generated, and when material constitutes a deepfake.</p>
        </section>

        <section class="problem-section">
            <h2>Four disclosure triggers</h2>
            <div class="kit-grid">
                <div class="feature-card"><h3>Chatbots & bots</h3><p>Inform users they are communicating with an AI unless obvious from context.</p></div>
                <div class="feature-card"><h3>Emotion recognition</h3><p>Notify people when AI is analysing their emotions or biometric categorisation.</p></div>
                <div class="feature-card"><h3>AI-generated content</h3><p>Mark text, image, audio, or video produced by AI in a machine-readable way.</p></div>
                <div class="feature-card"><h3>Deepfakes</h3><p>Disclose synthetic media that resembles real persons, places, or events.</p></div>
            </div>
        </section>

        <section class="problem-section">
            <h2>Technical documentation</h2>
            <p>Providers must maintain and publish documentation describing training data, model architecture, evaluation results, known limitations, and risk-mitigation measures. The Article 50 Kit templates this into a regulator-ready pack.</p>
        </section>

        <section class="problem-section">
            <h2>Penalties</h2>
            <p>Non-compliance can trigger fines of up to 7% of global annual turnover or €35 million, whichever is higher. Transparency is the lowest-cost defence.</p>
        </section>

        <div class="cta-box">
            <h2 style="font-size: 2rem; margin-bottom: 1rem; color: var(--primary);">Prove transparency in 48 hours</h2>
            <p style="margin-bottom: 2rem; color: var(--muted);">The Article 50 Emergency Kit gives you filed disclosure templates, a public attestation, and a post-market monitoring plan.</p>
            <a href="article-50-kit.html" class="btn">SECURE COMPLIANCE NOW</a>
        </div>
        """,
    },
    "article-50-marking": {
        "title": "Article 50 Marking & Watermarking — CSOAI",
        "description": "EU AI Act Article 50 marking requirements for synthetic content. C2PA, watermarking, metadata, and automated compliance tooling.",
        "h1": "Article 50 Marking",
        "countdown": "Machine-readable disclosure is mandatory from August 2, 2026",
        "schema_type": "Article",
        "schema_headline": "EU AI Act Article 50 Marking and Watermarking Guide",
        "body": """
        <section class="problem-section">
            <h2>Marking obligations</h2>
            <p>Article 50 requires AI-generated or AI-manipulated content to carry machine-readable markers so platforms, regulators, and downstream users can identify its synthetic origin.</p>
        </section>

        <section class="problem-section">
            <h2>Standards & techniques</h2>
            <div class="kit-grid">
                <div class="feature-card"><h3>C2PA metadata</h3><p>Content Credentials bind provenance, model identity, and editing history to media files.</p></div>
                <div class="feature-card"><h3>Robust watermarking</h3><p>Imperceptible signals embedded in images, audio, and video survive compression and cropping.</p></div>
                <div class="feature-card"><h3>Text provenance</h3><p>Statistical signatures and metadata tags for LLM-generated text and code.</p></div>
                <div class="feature-card"><h3>API signalling</h3><p>Structured headers and manifests that declare AI origin at the point of generation.</p></div>
            </div>
        </section>

        <section class="problem-section">
            <h2>Implementation checklist</h2>
            <ul style="color: var(--muted); margin-left: 1.5rem; line-height: 2;">
                <li>Inventory all AI-generated output surfaces</li>
                <li>Choose marking methods appropriate to each media type</li>
                <li>Validate markers survive common transformations</li>
                <li>Publish a transparency policy explaining your approach</li>
                <li>Attest compliance via a public Watchdog Certificate</li>
            </ul>
        </section>

        <div class="cta-box">
            <h2 style="font-size: 2rem; margin-bottom: 1rem; color: var(--primary);">Automate Article 50 marking</h2>
            <p style="margin-bottom: 2rem; color: var(--muted);">CSOAI's kits include C2PA policy templates, watermarking vendor criteria, and a public attestation chain.</p>
            <a href="article-50-kit.html" class="btn">GET THE MARKING KIT</a>
        </div>
        """,
    },
    "code-of-practice-2nd-draft": {
        "title": "EU AI Act Code of Practice 2nd Draft — CSOAI",
        "description": "Analysis of the second draft EU AI Act Code of Practice for general-purpose AI models. What changed and how to comply before August 2026.",
        "h1": "Code of Practice 2nd Draft",
        "countdown": "Final deadline: August 2, 2026",
        "schema_type": "Article",
        "schema_headline": "EU AI Act Code of Practice Second Draft Analysis",
        "body": """
        <section class="problem-section">
            <h2>Overview</h2>
            <p>The second draft of the EU AI Act Code of Practice, published in June 2025, refines the obligations for general-purpose AI model providers. It is the final shape of the rules most GPAI builders will follow until harmonised standards arrive.</p>
        </section>

        <section class="problem-section">
            <h2>Major changes from the first draft</h2>
            <div class="kit-grid">
                <div class="feature-card"><h3>Systemic-risk criteria</h3><p>Quantitative FLOP threshold plus qualitative dangerous-capability and impact indicators.</p></div>
                <div class="feature-card"><h3>Value-chain accountability</h3><p>Providers must document how safety mitigations flow to downstream deployers.</p></div>
                <div class="feature-card"><h3>Red-teaming depth</h3><p>Expanded adversarial testing, including cyber-offence, CBRN, and social-engineering vectors.</p></div>
                <div class="feature-card"><h3>Incident reporting</h3><p>Clear timelines and content requirements for reporting serious incidents to the AI Office.</p></div>
            </div>
        </section>

        <section class="problem-section">
            <h2>What providers must do now</h2>
            <ul style="color: var(--muted); margin-left: 1.5rem; line-height: 2;">
                <li>Assess whether your model meets systemic-risk thresholds</li>
                <li>Publish a transparency report aligned with the template</li>
                <li>Commission independent red-teaming and publish summary results</li>
                <li>Implement training-data governance and copyright-due-diligence records</li>
                <li>Prepare an incident-response and notification procedure</li>
            </ul>
        </section>

        <div class="cta-box">
            <h2 style="font-size: 2rem; margin-bottom: 1rem; color: var(--primary);">Close the gap before enforcement</h2>
            <p style="margin-bottom: 2rem; color: var(--muted);">CSOAI maps the second-draft Code of Practice to filed documentation, BFT-attested checklists, and a public compliance certificate.</p>
            <a href="article-50-kit.html" class="btn">START COMPLIANCE</a>
        </div>
        """,
    },
}


def find_container(html: str) -> tuple[int, int]:
    """Return (start, end) indices of the first <div class="container"> block."""
    start = html.find('<div class="container">')
    if start == -1:
        raise ValueError("container div not found")
    # Walk through tags to find matching close.
    i = html.find(">", start) + 1
    depth = 1
    while i < len(html) and depth > 0:
        open_tag = html.find("<div", i)
        close_tag = html.find("</div>", i)
        if close_tag == -1:
            raise ValueError("unclosed container")
        if open_tag != -1 and open_tag < close_tag:
            depth += 1
            i = open_tag + 4
        else:
            depth -= 1
            if depth == 0:
                return start, close_tag + 6
            i = close_tag + 6
    raise ValueError("could not match container")


def replace_once(html: str, old: str, new: str) -> str:
    if old not in html:
        raise ValueError(f"pattern not found: {old[:60]}")
    return html.replace(old, new, 1)


def main() -> None:
    template = TEMPLATE.read_text(encoding="utf-8")
    container_start, container_end = find_container(template)
    before = template[:container_start]
    after = template[container_end:]

    for slug, data in PAGES.items():
        head = before
        body = after

        # Head replacements
        head = replace_once(head, "<title>Article 50 Emergency Kit — CSOAI</title>", f"<title>{data['title']}</title>")
        head = replace_once(
            head,
            '<meta name="description" content="Secure EU AI Act Article 50 compliance before the August 2nd deadline. Complete transparency, risk classification, and post-market monitoring documentation.">',
            f'<meta name="description" content="{data["description"]}">',
        )
        head = replace_once(
            head,
            '<link rel="canonical" href="https://csoai.org/article-50-kit">',
            f'<link rel="canonical" href="https://csoai.org/{slug}">',
        )
        head = replace_once(
            head,
            '<meta property="og:title" content="Article 50 Emergency Kit — CSOAI">',
            f'<meta property="og:title" content="{data["title"]}">',
        )
        head = replace_once(
            head,
            '<meta property="og:description" content="Secure EU AI Act Article 50 compliance before the 2 August 2026 deadline. Transparency, risk classification, and post-market monitoring documentation.">',
            f'<meta property="og:description" content="{data["description"]}">',
        )
        head = replace_once(
            head,
            '<meta property="og:url" content="https://csoai.org/article-50-kit">',
            f'<meta property="og:url" content="https://csoai.org/{slug}">',
        )

        # Schema replacement
        old_schema = '{"@context":"https://schema.org","@type":"Product","name":"EU AI Act Article 50 Emergency Kit","description":"Complete EU AI Act Article 50 compliance bundle: transparency documentation, risk classification, human oversight plan, and audit log setup. Deadline guarantee for the 2 August 2026 cliff.","brand":{"@type":"Organization","name":"Council for the Safety of AI","url":"https://csoai.org"},"offers":{"@type":"Offer","price":"999","priceCurrency":"GBP","url":"https://csoai.org/article-50-kit","availability":"https://schema.org/InStock"}}'
        new_schema = json.dumps(
            {
                "@context": "https://schema.org",
                "@type": data["schema_type"],
                "headline": data["schema_headline"],
                "description": data["description"],
                "author": {"@type": "Organization", "name": "Council for the Safety of AI", "url": "https://csoai.org"},
                "publisher": {"@type": "Organization", "name": "CSOAI", "url": "https://csoai.org"},
                "url": f"https://csoai.org/{slug}",
                "datePublished": "2026-06-22",
                "dateModified": "2026-06-22",
            },
            separators=(",", ":"),
        )
        head = replace_once(head, old_schema, new_schema)

        # Container content
        container_html = f'''<div class="container">
        <div class="emergency-header">
            <span style="display:inline-block;margin-bottom:1rem;padding:.4rem 1rem;border-radius:999px;background:var(--primary);color:#fff;font-size:.75rem;font-weight:800;text-transform:uppercase;letter-spacing:.1em;">EU AI Act Compliance</span>
            <h1>{data['h1']}</h1>
            <div class="countdown">{data['countdown']}</div>
        </div>

        {data['body'].strip()}
    </div>'''

        page = head + container_html + body
        out_path = OUT_DIR / f"{slug}.html"
        out_path.write_text(page, encoding="utf-8")
        print(f"Wrote {out_path}")


if __name__ == "__main__":
    main()
