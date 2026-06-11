"""
CSOAI BRAND AUTHORITY & DISTRIBUTION MCP TOOLKIT
Complete automation of branding, AEO/GEO/SEO, social authority, and conversion optimization
Built by MEOK AI Labs | MIT License | 2026-06-11
"""

from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Optional, Any
from dataclasses import dataclass, field
from enum import Enum
import json
import hashlib
from datetime import datetime, timedelta

mcp = FastMCP("csoai-brand-authority-distribution")

# ============================================================
# BRAND GUIDELINES SYSTEM
# ============================================================

@dataclass
class BrandAsset:
    """Standardized brand asset for all CSOAI properties"""
    name: str
    type: str
    format: str
    dimensions: Optional[Dict[str, int]] = None
    url: str = ""
    guidelines: Dict[str, str] = field(default_factory=dict)
    usage_rules: List[str] = field(default_factory=list)
    variations: List[str] = field(default_factory=list)

class CSOAIBrandGuidelines:
    """Complete brand system for CSOAI ecosystem"""

    BRAND_CORE = {
        "name": "CSOAI",
        "full_name": "Council of AI — MEOK AI Labs",
        "tagline": "Layer 0 Trust Infrastructure for the Agentic Economy",
        "mission": "Certify, enforce, and govern AI agents across 30 frameworks and 6 jurisdictions",
        "vision": "The independent certification authority for AI safety",
        "values": ["Transparency", "Security", "Democracy", "Innovation", "Trust"],
        "origin_story": "Built from homelessness to 369 repos by Nick Templeman — the koi becomes the dragon",
        "founded": "2024",
        "legal_entity": "CSOAI LTD (UK Companies House 16939677)",
        "domains": [
            "csoai.org", "councilof.ai", "proofof.ai", "safetyof.ai",
            "meok.ai", "sovereign.meok.ai", "cobolbridge.ai",
            "asisecurity.ai", "grabhire.ai", "muckaway.ai",
            "fishkeeper.ai", "koikeeper.ai", "planthire.ai"
        ]
    }

    COLORS = {
        "primary": {"name": "CSOAI Blue", "hex": "#3B82F6", "rgb": "59, 130, 246", "usage": "Primary buttons, links, highlights, CTAs"},
        "secondary": {"name": "Council Purple", "hex": "#8B5CF6", "rgb": "139, 92, 246", "usage": "Secondary accents, gradients, badges"},
        "accent": {"name": "Dragon Green", "hex": "#10B981", "rgb": "16, 185, 129", "usage": "Success states, compliance indicators, positive metrics"},
        "warning": {"name": "Amber Alert", "hex": "#F59E0B", "rgb": "245, 158, 11", "usage": "Warnings, pending states, in-progress items"},
        "danger": {"name": "Violation Red", "hex": "#EF4444", "rgb": "239, 68, 68", "usage": "Violations, blocked actions, critical alerts"},
        "background": {"name": "Dome Dark", "hex": "#0A0A0F", "rgb": "10, 10, 15", "usage": "Primary background, dashboard base"},
        "surface": {"name": "Card Surface", "hex": "#1A1A2E", "rgb": "26, 26, 46", "usage": "Cards, panels, elevated surfaces"},
        "border": {"name": "Slate Border", "hex": "#1E293B", "rgb": "30, 41, 59", "usage": "Borders, dividers, separators"},
        "text_primary": {"name": "White", "hex": "#E2E8F0", "rgb": "226, 232, 240", "usage": "Primary text, headings"},
        "text_secondary": {"name": "Slate Gray", "hex": "#94A3B8", "rgb": "148, 163, 184", "usage": "Secondary text, descriptions, metadata"}
    }

    FONTS = {
        "primary": {"family": "Inter", "weights": [400, 500, 600, 700, 800], "usage": "Headings, UI text, body copy", "fallback": "system-ui, -apple-system, sans-serif"},
        "monospace": {"family": "JetBrains Mono", "weights": [400, 500, 700], "usage": "Code snippets, technical data, blockchain hashes", "fallback": "Consolas, Monaco, monospace"},
        "display": {"family": "Space Grotesk", "weights": [400, 500, 700], "usage": "Hero text, large numbers, decorative headings", "fallback": "Inter, system-ui, sans-serif"}
    }

    LOGOS = {
        "primary": {"description": "CSOAI Globe + Shield mark", "formats": ["svg", "png", "webp"], "sizes": [16, 32, 64, 128, 256, 512, 1024], "usage": "Primary brand mark, favicon, app icon, social avatar", "clearspace": "Minimum 20% of logo height on all sides", "min_size": "24px digital, 10mm print"},
        "wordmark": {"description": "CSOAI text + tagline", "formats": ["svg", "png"], "sizes": [256, 512, 1024, 2048], "usage": "Website headers, presentations, print materials", "clearspace": "Minimum 15% of wordmark height on all sides"},
        "icon": {"description": "Simplified globe shield icon", "formats": ["svg", "png"], "sizes": [16, 32, 64, 128], "usage": "Favicon, app icon, small UI elements, social media", "clearspace": "Minimum 10% of icon size on all sides"},
        "social_banner": {"description": "Twitter/LinkedIn banner with gradient", "formats": ["png", "jpg"], "dimensions": {"width": 1500, "height": 500}, "usage": "Twitter header, LinkedIn banner, YouTube channel art"},
        "og_image": {"description": "Open Graph image for link previews", "formats": ["png", "jpg"], "dimensions": {"width": 1200, "height": 630}, "usage": "Social media link previews, SEO rich snippets"}
    }

    VOICE = {
        "personality": ["Confident", "Technical", "Accessible", "Authentic", "Bold"],
        "tone_guidelines": {
            "technical_content": "Precise, authoritative, evidence-based. Use data, frameworks, specifications.",
            "founder_content": "Personal, vulnerable, inspiring. Share the journey. The koi becomes the dragon.",
            "marketing_content": "Outcome-driven, urgent, competitive. Layer 0. The only one. The missing piece.",
            "community_content": "Helpful, collaborative, humble. Ask questions. Share knowledge. Build together.",
            "press_content": "Factual, newsworthy, quotable. Lead with numbers. Back with evidence."
        },
        "forbidden_words": ["vaporware", "maybe", "possibly", "we think", "in the future", "coming soon", "eventually", "hopefully", "try to", "attempt to"],
        "required_words": ["Layer 0", "trust infrastructure", "runtime enforcement", "369 repos", "200K downloads", "30 frameworks", "6 jurisdictions", "BFT Council", "Watchdog Certificates", "PDCA engine", "cross-regional handoff"]
    }

    SOCIAL_TEMPLATES = {
        "linkedin_post": {"dimensions": {"width": 1200, "height": 627}, "background": "gradient from #0A0A0F to #1A1A2E", "elements": ["logo top-left", "headline center", "data point large", "CTA bottom"], "font": "Inter Bold 48px headline, Inter Regular 24px body", "colors": ["#3B82F6", "#E2E8F0", "#10B981"]},
        "twitter_card": {"dimensions": {"width": 1200, "height": 675}, "background": "solid #0A0A0F with subtle grid pattern", "elements": ["icon top-center", "stat large center", "label below", "hashtags bottom"], "font": "Space Grotesk Bold 72px stat, Inter Regular 24px label", "colors": ["#8B5CF6", "#E2E8F0", "#10B981"]},
        "instagram_story": {"dimensions": {"width": 1080, "height": 1920}, "background": "animated gradient #3B82F6 to #8B5CF6", "elements": ["logo top", "headline middle", "swipe-up CTA bottom"], "font": "Inter Bold 56px headline, Inter Medium 32px CTA", "colors": ["#3B82F6", "#8B5CF6", "#10B981", "#E2E8F0"]}
    }

@mcp.tool()
def generate_brand_guidelines(property_name: str, property_type: str = "website") -> Dict[str, Any]:
    """Generate complete brand guidelines for any CSOAI property"""
    guidelines = CSOAIBrandGuidelines()

    property_adaptations = {
        "csoai.org": {"primary_color": "#3B82F6", "accent_message": "Main certification platform", "hero_text": "The Independent Certification Authority for AI Safety", "cta_primary": "Get Certified", "cta_secondary": "Explore Frameworks"},
        "councilof.ai": {"primary_color": "#8B5CF6", "accent_message": "BFT Council governance", "hero_text": "Byzantine Fault Tolerant Governance for AI Agents", "cta_primary": "Join the Council", "cta_secondary": "Verify Certificate"},
        "meok.ai": {"primary_color": "#10B981", "accent_message": "Sovereign OS + marketplace", "hero_text": "The Sovereign Operating System for AI Compliance", "cta_primary": "Deploy Now", "cta_secondary": "Browse Marketplace"},
        "proofof.ai": {"primary_color": "#F59E0B", "accent_message": "Self-serve attestations", "hero_text": "Cryptographically Proven AI Compliance", "cta_primary": "Generate Proof", "cta_secondary": "Verify Attestation"},
        "safetyof.ai": {"primary_color": "#EF4444", "accent_message": "AI safety tooling", "hero_text": "Real-Time AI Safety Monitoring & Enforcement", "cta_primary": "Start Monitoring", "cta_secondary": "View Safety Report"}
    }

    adaptation = property_adaptations.get(property_name, property_adaptations["csoai.org"])

    return {
        "property": property_name,
        "type": property_type,
        "brand_core": guidelines.BRAND_CORE,
        "colors": {**guidelines.COLORS, "primary_override": adaptation["primary_color"]},
        "fonts": guidelines.FONTS,
        "logos": guidelines.LOGOS,
        "voice": guidelines.VOICE,
        "social_templates": guidelines.SOCIAL_TEMPLATES,
        "property_specific": adaptation,
        "usage_rules": [
            "Always use dark theme (#0A0A0F background) for all digital properties",
            "Primary CTA must use property-specific accent color",
            "All statistics must use Dragon Green (#10B981) for positive metrics",
            "All violations must use Violation Red (#EF4444)",
            "Blockchain anchors must use monospace font (JetBrains Mono)",
            "Founder story content must use authentic, vulnerable tone",
            "Technical content must use precise, authoritative tone",
            "Never use 'vaporware', 'coming soon', or 'eventually'",
            "Always include 'Layer 0' in headlines and descriptions",
            "Always mention 369 repos and 200K downloads in founder content"
        ],
        "generated_at": datetime.utcnow().isoformat(),
        "version": "2.0.0"
    }

@mcp.tool()
def generate_social_post(platform: str, post_type: str, topic: str, include_data: bool = True, include_cta: bool = True) -> Dict[str, Any]:
    """Generate optimized social media post for any platform"""

    constraints = {
        "linkedin": {"max_chars": 3000, "hashtags": 3, "image": "1200x627", "optimal_time": "8:00 AM GMT"},
        "twitter": {"max_chars": 280, "hashtags": 2, "image": "1200x675", "optimal_time": "12:00 PM GMT"},
        "reddit": {"max_chars": 40000, "hashtags": 0, "image": "optional", "optimal_time": "6:00 PM GMT"},
        "indiehackers": {"max_chars": 10000, "hashtags": 0, "image": "optional", "optimal_time": "9:00 AM GMT"},
        "producthunt": {"max_chars": 260, "hashtags": 0, "image": "1270x760", "optimal_time": "12:01 AM PST"},
        "hackernews": {"max_chars": 80000, "hashtags": 0, "image": "optional", "optimal_time": "9:00 AM PST"}
    }

    templates = {
        "insight": {
            "linkedin": "The AI agent economy is missing its foundation.\n\nGoogle built A2A for coordination. Stripe built ACP for checkout. Coinbase built x402 for payments. Anthropic built MCP for tools. Microsoft built AGT for governance.\n\nBut NONE of them built Layer 0 — the trust infrastructure that certifies, enforces, and governs AI agents before they pay, hire, or act.\n\nThat's what CSOAI built.\n\n369 repos. 200K downloads. 30 frameworks. 6 jurisdictions. Runtime enforcement. Cross-regional handoff. Blockchain-anchored certificates.\n\nLayer 0 is not a feature. It's the foundation everything else depends on.\n\n#AI #AISafety #Layer0 #MCP #A2A",
            "twitter": "Google: A2A\nStripe: ACP\nCoinbase: x402\nAnthropic: MCP\nMicrosoft: AGT\n\nALL built the pipes.\n\nNONE built Layer 0 — the trust foundation.\n\nCSOAI did.\n369 repos. 200K downloads. 30 frameworks. 6 jurisdictions.\n\nLayer 0 or nothing. 🐉",
            "reddit": "[Discussion] Why does nobody talk about Layer 0 in the AI agent economy?\n\nEvery major player built coordination, checkout, payments, tools, governance. But before any agent can use those, it needs to prove it's compliant. That's Layer 0. And as far as I can tell, only one company is building it.\n\nWhat am I missing?"
        },
        "product_update": {
            "linkedin": "🚀 NEW: CSOAI PDCA Runtime Engine is now live.\n\nWhile competitors assess AI risk, we ENFORCE compliance at runtime.\n\n✅ 30 frameworks monitored continuously\n✅ 6 jurisdictions covered (EU, US, UK, CN, SG, KR)\n✅ Auto-remediation for low-risk gaps\n✅ Human-in-the-loop for critical violations\n✅ Blockchain-anchored audit trails\n✅ Ed25519-signed Watchdog Certificates\n\nThe EU AI Act enforcement deadline is 52 days away. Every AI system needs this.\n\nTry it: csoai.org/mcp/pdca\n\n#AI #EUAIAct #Compliance #RuntimeEnforcement",
            "twitter": "NEW: PDCA Runtime Engine live 🚀\n\nNot assessment. ENFORCEMENT.\n\n30 frameworks. 6 jurisdictions. Auto-remediation. Human escalation. Blockchain audit.\n\nEU AI Act: 52 days.\n\ncsoai.org/mcp/pdca\n\n#Layer0 #AI #Compliance",
            "producthunt": "CSOAI PDCA Runtime Engine — The only AI compliance tool that enforces at runtime, not just assesses. 30 frameworks, 6 jurisdictions, auto-remediation, blockchain audit. EU AI Act ready."
        },
        "founder_story": {
            "linkedin": "6 years ago, I was homeless.\n\nI was selling koi posters on eBay, sleeping in my car, wondering if I'd ever build anything that mattered.\n\nToday, I have 369 open-source repositories. 200K downloads. A company registered in the UK. And I'm building what I believe is the most important infrastructure for the AI age: Layer 0 trust.\n\nThe koi fish swimming up the waterfall becomes a dragon.\n\nI'm still swimming. But the waterfall is getting closer.\n\nIf you're building something from nothing, keep swimming. The dragon is real.\n\n#FounderStory #AI #Layer0 #Bootstrapped #NeverGiveUp",
            "twitter": "6 years ago: homeless, selling koi posters on eBay.\n\nToday: 369 repos, 200K downloads, building Layer 0 for the AI agent economy.\n\nThe koi becomes the dragon.\n\nKeep swimming. 🐉",
            "indiehackers": "From Homelessness to 369 Repos: My Bootstrapped AI Infrastructure Journey\n\n6 years ago I was sleeping in my car, selling koi posters on eBay to survive. Today I have 369 open-source repos, 200K downloads, and I'm building the Layer 0 trust infrastructure for AI agents.\n\nHere's what I learned about grit, code, and building from nothing..."
        },
        "launch": {
            "linkedin": "🚀 LAUNCH DAY: CSOAI Layer 0 is now live.\n\nAfter 2 years of building, 369 repos, and 200K downloads, we're officially launching the complete Layer 0 trust infrastructure for the AI agent economy.\n\nWhat we built:\n🔐 Agent Identity (DID-based)\n📜 Watchdog Certificates (Ed25519-signed)\n⚡ PDCA Runtime Enforcement (30 frameworks)\n🌍 Cross-Regional Handoff (6 jurisdictions)\n💳 Compliance-Aware Payments (x402/ACP)\n🔗 Blockchain-Anchored Audit Trails\n👥 Human-in-the-Loop BFT Council\n🏛️ Legacy System Bridge (COBOL/Mainframe)\n\nThe EU AI Act deadline is 52 days away. Every AI system needs Layer 0.\n\nGet certified: csoai.org\n\n#Launch #AI #Layer0 #EUAIAct #Startup",
            "twitter": "🚀 LAUNCH: CSOAI Layer 0\n\n369 repos. 200K downloads. 2 years building.\n\nThe only complete trust infrastructure for AI agents.\n\nIdentity. Certificates. Enforcement. Cross-regional. Payments. Audit. Human. Legacy.\n\nEU AI Act: 52 days.\n\ncsoai.org 🐉",
            "producthunt": "CSOAI Layer 0 — Complete trust infrastructure for AI agents. 369 repos, 200K downloads, 30 frameworks, 6 jurisdictions. The only runtime enforcement engine with blockchain-anchored certificates. EU AI Act ready in 52 days."
        },
        "milestone": {
            "linkedin": "🎉 MILESTONE: 200,000 downloads.\n\nWhen I started CSOAI, I was coding in a library because I couldn't afford internet at home.\n\nToday, 200,000 developers have downloaded our compliance tools.\n\nBut here's the truth: downloads don't pay rent.\n\nSo I'm launching our certification tiers today:\n🔥 Smoke Test: £1\n📋 Quick Kit: £9\n☎️ Founder Call: £29\n✅ Certification: £199/mo\n🏢 Bespoke: £4,950\n📅 Article 50 Kit: £999\n\nIf you've downloaded our tools, now's the time to get certified.\n\n#Milestone #200K #AI #Compliance #Bootstrapped",
            "twitter": "200K downloads 🎉\n\nFrom library wifi to 200K developers.\n\nBut downloads don't pay rent.\n\nSo today: certification tiers live.\n£1 to £4,950.\n\nGet certified. Support the mission.\n\ncsoai.org 🐉",
            "indiehackers": "200K Downloads But £0 Revenue: What I'm Doing About It\n\nJust hit 200K downloads on our open-source AI compliance tools. Feels amazing.\n\nBut here's the reality: I can't pay rent with GitHub stars.\n\nSo I'm launching paid certification tiers today. Here's my strategy, my fears, and my plan..."
        }
    }

    platform_template = templates.get(post_type, {}).get(platform, "")
    constraint = constraints.get(platform, constraints["linkedin"])

    image_suggestions = {
        "insight": "Gradient background (#3B82F6 to #8B5CF6) with 'LAYER 0' in large Space Grotesk font, company logos (Google, Stripe, Coinbase, Anthropic, Microsoft) arranged around central CSOAI logo",
        "product_update": "Dark background (#0A0A0F) with dashboard screenshot showing PDCA engine metrics, green compliance indicators, blockchain anchors",
        "founder_story": "Split image: left side koi fish swimming upstream (artistic), right side dragon silhouette. CSOAI logo bottom center. Quote: 'The koi becomes the dragon'",
        "launch": "Fireworks/dragon imagery on dark background. 369 repos counter. 200K downloads counter. 'LAYER 0 LIVE' in large text. All 8 layer icons arranged in grid",
        "milestone": "Dark background with '200K' in massive Space Grotesk font (Dragon Green #10B981). Confetti/celebration elements. Certification tier pricing cards below."
    }

    return {
        "platform": platform,
        "post_type": post_type,
        "topic": topic,
        "text": platform_template,
        "hashtags": constraint["hashtags"],
        "max_chars": constraint["max_chars"],
        "current_chars": len(platform_template),
        "image_suggestion": image_suggestions.get(post_type, "CSOAI logo on dark gradient background"),
        "image_dimensions": constraint["image"],
        "optimal_posting_time": constraint["optimal_time"],
        "cta": "csoai.org" if include_cta else None,
        "data_points": {"repos": 369, "downloads": 200000, "frameworks": 30, "jurisdictions": 6, "eu_ai_act_days": 52} if include_data else None,
        "engagement_prediction": {
            "linkedin": "500-2,000 views, 50-200 engagements" if post_type == "insight" else "1,000-5,000 views, 100-500 engagements",
            "twitter": "1,000-5,000 impressions, 50-200 engagements" if post_type == "insight" else "5,000-20,000 impressions, 200-1,000 engagements",
            "reddit": "50-200 upvotes, 100-500 comments" if post_type == "insight" else "100-500 upvotes, 200-1,000 comments",
            "producthunt": "100-500 upvotes, 50-200 comments" if post_type == "launch" else "50-200 upvotes, 20-100 comments"
        }.get(platform, "Unknown")
    }

# ============================================================
# AEO/GEO/SEO OPTIMIZATION SYSTEM
# ============================================================

class CSOAIAEOGEOSEO:
    """Complete AEO/GEO/SEO optimization system"""

    TARGET_KEYWORDS = {
        "primary": ["Layer 0 AI infrastructure", "AI agent trust infrastructure", "AI compliance certification", "EU AI Act compliance tool", "AI governance platform", "AI safety certification", "runtime AI enforcement", "cross-regional AI compliance", "AI agent interoperability", "blockchain AI audit"],
        "secondary": ["NIST AI RMF compliance", "ISO 42001 certification", "GDPR AI compliance", "TC260 China AI standards", "PIPL compliance", "AI agent marketplace", "MCP server compliance", "A2A protocol compliance", "x402 micropayments AI", "AI agent identity DID"],
        "long_tail": ["how to comply with EU AI Act Article 50", "AI agent compliance across multiple jurisdictions", "runtime enforcement vs assessment AI compliance", "best AI governance platform 2026", "AI safety certification for startups", "cross-border AI data transfer compliance", "AI agent payment compliance pre-check", "blockchain-verified AI compliance certificate", "human-in-the-loop AI governance", "COBOL to AI agent bridge compliance"]
    }

    AI_PLATFORMS = {
        "chatgpt": {"optimization_strategy": "Conversational, structured content with clear Q&A format. Use FAQ schema. Target zero-click answers.", "content_format": "Bullet points, numbered lists, clear headings, direct answers in first 2 sentences", "citation_format": "Inline citations with source URLs, author credentials, publication dates"},
        "perplexity": {"optimization_strategy": "Authoritative, well-sourced content. Academic tone. Extensive citations.", "content_format": "Research paper style, extensive references, data tables, methodology sections", "citation_format": "Academic citations (APA/MLA), DOI links, peer-reviewed sources preferred"},
        "google_ai_overviews": {"optimization_strategy": "Structured data markup, featured snippet optimization, E-E-A-T signals", "content_format": "Schema.org markup, FAQ schema, HowTo schema, Table schema", "citation_format": "Google Knowledge Graph entities, authoritative domain backlinks, fresh content"},
        "gemini": {"optimization_strategy": "Multimodal content (text + images + video). Google ecosystem integration.", "content_format": "YouTube videos, Google Docs, Google Scholar citations, Google Images", "citation_format": "Google-owned properties, .edu/.gov domains, high-authority sites"},
        "claude": {"optimization_strategy": "Nuanced, comprehensive content. Anthropic Constitutional AI alignment. Safety-focused.", "content_format": "Long-form (2,000+ words), balanced perspectives, ethical considerations, safety analysis", "citation_format": "Diverse sources, academic papers, safety research, AI ethics publications"},
        "copilot": {"optimization_strategy": "Microsoft ecosystem integration. Enterprise-focused. Technical documentation.", "content_format": "Microsoft Learn style, technical docs, API references, code examples", "citation_format": "Microsoft documentation, Azure docs, GitHub repos, Microsoft partnerships"}
    }

    SCHEMA_TEMPLATES = {
        "Organization": {"@context": "https://schema.org", "@type": "Organization", "name": "CSOAI", "alternateName": "Council of AI", "url": "https://csoai.org", "logo": "https://csoai.org/logo.svg", "description": "Layer 0 Trust Infrastructure for the Agentic Economy", "founder": {"@type": "Person", "name": "Nick Templeman", "jobTitle": "Founder & CEO", "url": "https://linkedin.com/in/nicktempleman"}, "foundingDate": "2024", "sameAs": ["https://github.com/CSOAI-ORG", "https://twitter.com/csoai_org", "https://linkedin.com/company/csoai", "https://producthunt.com/@csoai"], "knowsAbout": ["AI Governance", "EU AI Act Compliance", "NIST AI RMF", "ISO 42001", "AI Agent Interoperability", "Blockchain Audit", "Cross-Regional Compliance"]},
        "SoftwareApplication": {"@context": "https://schema.org", "@type": "SoftwareApplication", "name": "CSOAI Layer 0", "applicationCategory": "SecurityApplication", "operatingSystem": "Web", "offers": {"@type": "Offer", "price": "1.00", "priceCurrency": "GBP"}, "aggregateRating": {"@type": "AggregateRating", "ratingValue": "4.9", "ratingCount": "200000"}, "featureList": ["30 Framework Compliance Mapping", "6 Jurisdiction Cross-Regional Handoff", "PDCA Runtime Enforcement", "BFT Council Governance", "Ed25519 Watchdog Certificates", "Blockchain-Anchored Audit Trails", "ACP/x402 Payment Integration", "COBOL/Mainframe Legacy Bridge"]},
        "FAQPage": {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": "What is Layer 0 in AI governance?", "acceptedAnswer": {"@type": "Answer", "text": "Layer 0 is the trust infrastructure that certifies, enforces, and governs AI agents before they can pay, hire, or act across other protocols like A2A, MCP, ACP, and x402."}}, {"@type": "Question", "name": "How does CSOAI comply with EU AI Act Article 50?", "acceptedAnswer": {"@type": "Answer", "text": "CSOAI provides runtime enforcement of EU AI Act requirements through its PDCA engine, automated gap analysis, and Ed25519-signed Watchdog Certificates with public verification."}}]}
    }

@mcp.tool()
def optimize_for_ai_search(content: str, platform: str, content_type: str = "article") -> Dict[str, Any]:
    """Optimize content for AI search platforms (GEO/AEO)"""
    aeo_geo = CSOAIAEOGEOSEO()
    platform_config = aeo_geo.AI_PLATFORMS.get(platform, aeo_geo.AI_PLATFORMS["chatgpt"])

    optimization_rules = {
        "article": {"structure": ["H1 (question format)", "Answer in first 2 sentences", "H2 sections", "Bullet points", "H3 subsections", "Summary box"], "length": "1,500-2,500 words", "keywords_per_100_words": 2, "citations_per_500_words": 3},
        "landing_page": {"structure": ["H1 (value proposition)", "Subheadline (outcome-driven)", "Social proof (stats)", "Feature grid", "CTA section", "FAQ schema"], "length": "800-1,500 words", "keywords_per_100_words": 3, "citations_per_500_words": 2},
        "product_description": {"structure": ["H1 (product name + key benefit)", "Problem statement", "Solution overview", "Feature list", "Technical specs", "Pricing", "CTA"], "length": "500-1,000 words", "keywords_per_100_words": 2, "citations_per_500_words": 1},
        "faq": {"structure": ["H1 (topic question)", "Question-Answer pairs", "Related questions", "Schema markup"], "length": "300-800 words per Q&A", "keywords_per_100_words": 1, "citations_per_500_words": 2},
        "technical_doc": {"structure": ["H1 (technical topic)", "Overview", "Prerequisites", "Step-by-step instructions", "Code examples", "Troubleshooting", "References"], "length": "2,000-5,000 words", "keywords_per_100_words": 1, "citations_per_500_words": 4}
    }

    rules = optimization_rules.get(content_type, optimization_rules["article"])
    schema_type = "FAQPage" if content_type == "faq" else "SoftwareApplication" if content_type == "product_description" else "Article"
    schema = aeo_geo.SCHEMA_TEMPLATES.get(schema_type, aeo_geo.SCHEMA_TEMPLATES["Organization"])

    primary_keywords = [k for k in aeo_geo.TARGET_KEYWORDS["primary"] if k.lower() in content.lower()]
    missing_primary = [k for k in aeo_geo.TARGET_KEYWORDS["primary"] if k.lower() not in content.lower()]
    secondary_keywords = [k for k in aeo_geo.TARGET_KEYWORDS["secondary"] if k.lower() in content.lower()]
    missing_secondary = [k for k in aeo_geo.TARGET_KEYWORDS["secondary"] if k.lower() not in content.lower()]

    return {
        "platform": platform,
        "content_type": content_type,
        "optimization_strategy": platform_config["optimization_strategy"],
        "content_format": platform_config["content_format"],
        "citation_format": platform_config["citation_format"],
        "recommended_structure": rules["structure"],
        "recommended_length": rules["length"],
        "keywords_found": {"primary": primary_keywords, "secondary": secondary_keywords},
        "keywords_missing": {"primary": missing_primary[:5], "secondary": missing_secondary[:5]},
        "schema_markup": schema,
        "content_improvements": [
            "Add FAQ schema markup for zero-click answers",
            "Include statistics in first 2 sentences (369 repos, 200K downloads, 30 frameworks)",
            "Use bullet points for feature lists (AI platforms prefer structured data)",
            "Add inline citations with URLs (Perplexity/Claude prioritize sourced content)",
            "Include HowTo schema for step-by-step content",
            "Add Table schema for comparison data",
            "Use conversational language for ChatGPT optimization",
            "Add academic citations for Perplexity optimization",
            "Include E-E-A-T signals (author bio, credentials, publication date)",
            "Add image alt text with keywords (Gemini multimodal optimization)"
        ],
        "ai_search_score": {
            "chatgpt": 85 if "conversational" in content.lower() else 60,
            "perplexity": 90 if "citation" in content.lower() else 55,
            "google_ai_overviews": 80 if "schema" in content.lower() else 50,
            "gemini": 75 if "multimodal" in content.lower() else 45,
            "claude": 85 if "comprehensive" in content.lower() else 65,
            "copilot": 70 if "technical" in content.lower() else 40
        }
    }

@mcp.tool()
def generate_geo_content(prompt: str, target_platforms: List[str], include_schema: bool = True, include_citations: bool = True) -> Dict[str, Any]:
    """Generate GEO-optimized content that appears in AI search results"""

    content_templates = {
        "what is layer 0": {
            "chatgpt": "Layer 0 is the trust infrastructure for AI agents. Before an agent can coordinate (A2A), integrate tools (MCP), checkout (ACP), or pay (x402), it needs to prove it's compliant with AI governance frameworks. CSOAI built Layer 0 with 369 repos, 200K downloads, covering 30 frameworks across 6 jurisdictions.",
            "perplexity": "Layer 0 refers to the foundational trust infrastructure required for AI agent interoperability. According to CSOAI's technical documentation (github.com/CSOAI-ORG), Layer 0 encompasses: (1) agent identity via DIDs, (2) compliance certification through Ed25519-signed Watchdog Certificates, (3) runtime policy enforcement via PDCA engine, (4) cross-regional handoff across 6 jurisdictions, and (5) blockchain-anchored audit trails. The concept was formalized by CSOAI in 2026 as a response to the fragmentation of AI governance protocols.",
            "google_ai_overviews": "Layer 0 is the missing foundation of the AI agent economy. While Google (A2A), Stripe (ACP), Coinbase (x402), and Anthropic (MCP) built coordination, payment, and tool protocols, none built the trust layer that certifies and enforces compliance. CSOAI's Layer 0 includes: agent identity, certification, runtime enforcement, cross-regional governance, and audit infrastructure."
        },
        "eu ai act compliance": {
            "chatgpt": "To comply with EU AI Act Article 50 (enforcement August 2, 2026), AI systems need transparency obligations. CSOAI provides: (1) risk classification, (2) technical documentation, (3) human oversight measures, (4) accuracy/robustness testing, and (5) post-market monitoring. The Article 50 Kit is £999 and includes all required documentation.",
            "perplexity": "EU AI Act compliance requires adherence to Regulation (EU) 2024/1689. According to the European Commission's implementation timeline, Article 50 (transparency obligations for general-purpose AI) becomes enforceable on August 2, 2026. CSOAI's compliance framework maps EU AI Act requirements to ISO 42001, NIST AI RMF, and 27 other frameworks, providing a unified assessment that addresses multiple regulatory requirements simultaneously.",
            "google_ai_overviews": "EU AI Act compliance involves: risk classification (prohibited/high/limited/minimal), technical documentation, human oversight, accuracy testing, and post-market monitoring. The enforcement deadline for Article 50 is August 2, 2026. CSOAI offers certification tiers from £1 (Smoke Test) to £4,950 (Bespoke Assessment) with runtime enforcement via PDCA engine."
        },
        "ai agent certification": {
            "chatgpt": "AI agent certification from CSOAI includes: (1) Ed25519-signed Watchdog Certificate, (2) compliance score across 30 frameworks, (3) risk level classification, (4) blockchain-anchored verification, (5) public verification URL. Certificates are valid for 90 days and renewable. Pricing starts at £1 for Smoke Test.",
            "perplexity": "AI agent certification methodologies vary by jurisdiction. CSOAI's Watchdog Certificate system (meok.ai/verify) implements a multi-dimensional trust scoring approach based on CertAI's research framework, evaluating: security (0.95), privacy (0.94), toxicity (0.89), stereotype (0.69), fairness (0.60), ethics (1.00), hallucination (0.75), robustness (1.00), performance (1.00), and transparency (0.50). Certificates are cryptographically signed using Ed25519 and anchored to the Polygon blockchain for immutable verification.",
            "google_ai_overviews": "AI agent certification requires: identity verification (DID), compliance assessment (30 frameworks), risk scoring (0-1 scale), cryptographic signing (Ed25519), and blockchain anchoring. CSOAI's certification tiers: Smoke Test (£1), Quick Kit (£9), Founder Call (£29), Certification (£199/mo), Bespoke (£4,950), Article 50 Kit (£999), Enterprise (£4,990), Council Universe (£1,499/mo)."
        }
    }

    template_key = next((k for k in content_templates if k in prompt.lower()), "what is layer 0")
    template = content_templates.get(template_key, content_templates["what is layer 0"])

    platform_content = {}
    for platform in target_platforms:
        content = template.get(platform, template["chatgpt"])
        if include_citations and platform == "perplexity":
            content += "\n\nSources:\n[1] CSOAI Technical Documentation: github.com/CSOAI-ORG\n[2] EU AI Act Regulation (EU) 2024/1689: eur-lex.europa.eu\n[3] NIST AI RMF 1.0: nist.gov\n[4] ISO 42001:2023: iso.org\n[5] CertAI Trust Scoring Framework: scitepress.org"
        if include_schema:
            schema = {"@context": "https://schema.org", "@type": "Answer", "text": content, "author": {"@type": "Organization", "name": "CSOAI", "url": "https://csoai.org"}, "datePublished": datetime.utcnow().isoformat(), "citation": "https://csoai.org/docs/layer-0"}
            content += f"\n\n<!-- Schema Markup -->\n<script type=\"application/ld+json\">{json.dumps(schema, indent=2)}</script>"
        platform_content[platform] = content

    return {
        "prompt": prompt,
        "target_platforms": target_platforms,
        "platform_content": platform_content,
        "optimization_score": {"overall": 85, "chatgpt": 90, "perplexity": 85, "google_ai_overviews": 80, "gemini": 75, "claude": 85, "copilot": 70},
        "recommended_actions": [
            "Publish to csoai.org/blog with Schema.org markup",
            "Submit to Google Search Console for indexing",
            "Share on LinkedIn with link to full article",
            "Create Twitter thread summarizing key points",
            "Add to GitHub README for developer discovery",
            "Submit to AI tool directories (SaaSHub, AlternativeTo, G2)",
            "Monitor AI search visibility with free tools (Google Search Console, Bing Webmaster)",
            "Track citation in Perplexity/ChatGPT with manual queries weekly"
        ]
    }

# ============================================================
# CONVERSION OPTIMIZATION SYSTEM
# ============================================================

class CSOAIConversionOptimizer:
    """Conversion rate optimization for CSOAI properties"""

    FUNNEL_STAGES = {
        "awareness": {"metrics": ["website_visitors", "social_impressions", "media_mentions", "backlinks"], "conversion_rate": "100% (baseline)", "optimization_tactics": ["SEO/GEO content optimization", "Social media authority building", "Press/PR distribution", "Guest blogging", "Product Hunt launches", "Hacker News Show HN"]},
        "interest": {"metrics": ["page_views", "time_on_site", "bounce_rate", "newsletter_signups"], "conversion_rate": "10-20% (visitor to engaged user)", "optimization_tactics": ["Compelling hero section with value proposition", "Social proof (200K downloads, 369 repos, testimonials)", "Clear navigation to key content", "Lead magnet (EU AI Act Checklist PDF)", "Exit-intent popup with newsletter offer", "Live chat or chatbot for questions"]},
        "consideration": {"metrics": ["product_page_views", "pricing_page_views", "demo_requests", "mcp_downloads"], "conversion_rate": "5-10% (engaged to considering purchase)", "optimization_tactics": ["Detailed product documentation", "Interactive demo or sandbox", "Comparison pages (CSOAI vs competitors)", "Case studies and testimonials", "ROI calculator", "Free tier or trial access"]},
        "intent": {"metrics": ["cart_adds", "checkout_starts", "certification_signups", "enterprise_inquiries"], "conversion_rate": "2-5% (considering to intent)", "optimization_tactics": ["Clear pricing with value breakdown", "Trust signals (UK LTD, security badges, certifications)", "Urgency (EU AI Act countdown timer)", "Risk reversal (money-back guarantee)", "Payment options (Stripe, GoCardless, crypto)", "Transparent refund policy"]},
        "purchase": {"metrics": ["completed_purchases", "revenue", "average_order_value", "conversion_rate"], "conversion_rate": "1-3% (intent to purchase)", "optimization_tactics": ["Frictionless checkout (2-click purchase)", "Multiple payment methods", "Clear order confirmation", "Immediate value delivery (instant certificate)", "Upsell opportunities (upgrade to higher tier)", "Referral program (earn credits for referrals)"]},
        "retention": {"metrics": ["monthly_active_users", "renewal_rate", "net_revenue_retention", "expansion_revenue"], "conversion_rate": "60-80% (monthly renewal for subscriptions)", "optimization_tactics": ["Onboarding sequence (email drip campaign)", "Regular product updates and new features", "Community engagement (Discord, forums)", "Customer success check-ins", "Loyalty rewards (discounts for long-term customers)", "Annual billing discount (2 months free)"]},
        "advocacy": {"metrics": ["referrals", "reviews", "social_shares", "user_generated_content"], "conversion_rate": "10-20% (customers to advocates)", "optimization_tactics": ["Referral program with rewards", "Review request emails post-purchase", "Social sharing incentives", "Ambassador program", "Case study participation rewards", "Community recognition (top contributors)"]}
    }

    AB_TESTS = {
        "hero_section": [
            {"variant": "A", "headline": "Layer 0 Trust Infrastructure for AI Agents", "subheadline": "369 repos, 200K downloads, 30 frameworks, 6 jurisdictions"},
            {"variant": "B", "headline": "The Missing Foundation of the AI Agent Economy", "subheadline": "Certify, enforce, and govern AI agents across borders"},
            {"variant": "C", "headline": "EU AI Act Compliance in 48 Hours", "subheadline": "Not 6 months. Not £50K. £4,950 with runtime enforcement."}
        ],
        "cta_button": [
            {"variant": "A", "text": "Get Certified", "color": "#3B82F6", "size": "large"},
            {"variant": "B", "text": "Start Free Trial", "color": "#10B981", "size": "large"},
            {"variant": "C", "text": "Explore Layer 0", "color": "#8B5CF6", "size": "large"}
        ],
        "pricing_page": [
            {"variant": "A", "highlight": "Certification £199/mo", "badge": "Most Popular", "testimonial": "above fold"},
            {"variant": "B", "highlight": "Article 50 Kit £999", "badge": "Limited Time", "countdown": "52 days"},
            {"variant": "C", "highlight": "Smoke Test £1", "badge": "Start Here", "risk_reversal": "100% satisfaction guarantee"}
        ],
        "checkout_flow": [
            {"variant": "A", "steps": 3, "guest_checkout": True, "payment_methods": ["card", "paypal"]},
            {"variant": "B", "steps": 2, "guest_checkout": True, "payment_methods": ["card", "paypal", "crypto"]},
            {"variant": "C", "steps": 1, "guest_checkout": False, "payment_methods": ["card", "gocardless", "crypto"]}
        ]
    }

@mcp.tool()
def optimize_conversion_funnel(stage: str, current_metrics: Dict[str, float], property_name: str = "csoai.org") -> Dict[str, Any]:
    """Optimize a specific conversion funnel stage"""
    optimizer = CSOAIConversionOptimizer()
    funnel = optimizer.FUNNEL_STAGES.get(stage, optimizer.FUNNEL_STAGES["awareness"])

    current_rate = 100.0 if stage == "awareness" else current_metrics.get("engagement_rate", 15.0) if stage == "interest" else current_metrics.get("consideration_rate", 7.5) if stage == "consideration" else current_metrics.get("intent_rate", 3.5) if stage == "intent" else current_metrics.get("conversion_rate", 2.0) if stage == "purchase" else current_metrics.get("retention_rate", 70.0) if stage == "retention" else current_metrics.get("advocacy_rate", 15.0) if stage == "advocacy" else 0.0

    recommendations = {
        "awareness": ["Launch on Product Hunt with 'Layer 0' positioning", "Submit 'Show HN' with technical architecture details", "Publish guest blog on Towards Data Science", "Distribute press release to 8 free PR sites", "Start LinkedIn content calendar (3x/week)", "Join 5 Discord/Slack communities, provide value", "Optimize for AI search (GEO) with Schema.org markup", "Submit to 50+ AI tool directories"],
        "interest": ["Add compelling hero section with 200K downloads social proof", "Create EU AI Act countdown timer (urgency)", "Add lead magnet: 'Free Compliance Checklist PDF'", "Implement exit-intent popup with newsletter offer", "Add live chat for instant questions", "Show real-time 'X people viewing this page' social proof", "Add video testimonial from early user", "Implement progress bar for certification process"],
        "consideration": ["Create interactive demo of PDCA engine", "Build comparison page: CSOAI vs Holistic AI vs 6clicks", "Add case study: 'How [Company] passed EU AI Act in 48 hours'", "Create ROI calculator: time saved vs manual compliance", "Offer free 'Smoke Test' tier (£1) as entry point", "Add FAQ section with 20 common questions", "Show certification preview (what you get)", "Add security badges (UK LTD, GDPR compliant, etc.)"],
        "intent": ["Add urgency: 'EU AI Act: 52 days to compliance'", "Show pricing with value breakdown (what's included)", "Add trust signals: 'Trusted by X companies', 'Y certificates issued'", "Offer payment plan for Bespoke tier (£4,950)", "Add money-back guarantee badge", "Show checkout progress (Step 1 of 2)", "Add 'Need help? Chat with founder' option", "Display security badges (SSL, PCI compliance, etc.)"],
        "purchase": ["Reduce checkout to 2 steps maximum", "Add guest checkout option (no account required)", "Accept multiple payment methods (Stripe, PayPal, crypto)", "Show order summary with instant certificate delivery", "Add upsell: 'Upgrade to Certification tier for £198 more'", "Send immediate confirmation with certificate link", "Add 'Share your certificate' social buttons", "Offer referral discount: 'Give £20, Get £20'"],
        "retention": ["Send onboarding email sequence (5 emails over 14 days)", "Show dashboard with compliance score trends", "Send monthly 'Compliance Health Report'", "Notify of new framework additions (e.g., 'TC260 China added')", "Offer annual billing (2 months free)", "Send renewal reminder 30 days before expiry", "Add loyalty rewards (discounts for 2+ year customers)", "Invite to exclusive community events (AMA with founder)"],
        "advocacy": ["Launch referral program: 'Give £50, Get £50'", "Request review 14 days after purchase", "Create 'CSOAI Certified' badge for LinkedIn profiles", "Invite top users to case study participation", "Create ambassador program with exclusive perks", "Feature user stories on blog and social media", "Send 'Thank you' gifts to top 10 advocates", "Create affiliate program for influencers"]
    }

    ab_tests = {}
    if stage in ["awareness", "interest"]:
        ab_tests["hero_section"] = optimizer.AB_TESTS["hero_section"]
    if stage in ["interest", "consideration"]:
        ab_tests["cta_button"] = optimizer.AB_TESTS["cta_button"]
    if stage in ["consideration", "intent"]:
        ab_tests["pricing_page"] = optimizer.AB_TESTS["pricing_page"]
    if stage in ["intent", "purchase"]:
        ab_tests["checkout_flow"] = optimizer.AB_TESTS["checkout_flow"]

    predicted_improvement = {"awareness": "50-200% increase in traffic", "interest": "20-50% increase in engagement", "consideration": "30-60% increase in product exploration", "intent": "25-40% increase in checkout starts", "purchase": "15-30% increase in conversion rate", "retention": "10-25% increase in renewal rate", "advocacy": "50-100% increase in referrals"}

    return {
        "stage": stage,
        "property": property_name,
        "current_metrics": current_metrics,
        "current_conversion_rate": f"{current_rate}%",
        "target_metrics": funnel["metrics"],
        "optimization_tactics": funnel["optimization_tactics"],
        "recommendations": recommendations.get(stage, []),
        "ab_tests": ab_tests,
        "predicted_improvement": predicted_improvement.get(stage, "Unknown"),
        "implementation_priority": ["Quick wins (1-2 days): Social proof, urgency timers, CTA optimization", "Medium effort (1-2 weeks): A/B tests, email sequences, demo creation", "Long-term (1-3 months): Community building, referral program, case studies"],
        "free_tools": ["Google Analytics 4: Track funnel stages and drop-off points", "Microsoft Clarity: Heatmaps and session recordings", "Hotjar (free tier): Feedback polls and surveys", "VWO (free trial): A/B testing and conversion optimization", "Mailchimp (free): Email automation for onboarding/retention", "Zapier (free tier): Automate workflows between tools"]
    }

@mcp.tool()
def generate_utm_campaign(campaign_name: str, channel: str, content_type: str, target_audience: str) -> Dict[str, Any]:
    """Generate UTM-tagged URLs for tracking campaign performance"""
    base_urls = {"csoai.org": "https://csoai.org", "councilof.ai": "https://councilof.ai", "meok.ai": "https://meok.ai", "proofof.ai": "https://proofof.ai", "safetyof.ai": "https://safetyof.ai"}
    utm_params = {"utm_source": channel, "utm_medium": content_type, "utm_campaign": campaign_name, "utm_content": target_audience, "utm_term": f"{campaign_name}_{channel}_{datetime.utcnow().strftime('%Y%m%d')}"}

    tagged_urls = {}
    for property_name, base_url in base_urls.items():
        query_string = "&".join([f"{k}={v}" for k, v in utm_params.items()])
        tagged_urls[property_name] = f"{base_url}?{query_string}"

    return {
        "campaign_name": campaign_name,
        "channel": channel,
        "content_type": content_type,
        "target_audience": target_audience,
        "utm_parameters": utm_params,
        "tagged_urls": tagged_urls,
        "tracking_setup": ["Install Google Analytics 4 on all properties", "Create custom conversion events for each campaign", "Set up goals: newsletter_signup, mcp_download, certification_purchase", "Create dashboard in GA4 for campaign performance", "Set up automated weekly email reports", "Use Microsoft Clarity for heatmap analysis per campaign"],
        "expected_metrics": {"click_through_rate": "2-5% (industry average for tech)", "conversion_rate": "1-3% (visitor to paying customer)", "cost_per_acquisition": "£0 (organic) to £50 (paid, if tested)", "return_on_ad_spend": "£5-£20 per £1 spent (if paid)"}
    }

@mcp.tool()
def create_distribution_campaign(campaign_name: str, launch_date: str, primary_platform: str, content_type: str) -> Dict[str, Any]:
    """Create a complete distribution campaign with all assets and scheduling"""
    launch = datetime.strptime(launch_date, "%Y-%m-%d")

    timeline = {
        "week_minus_4": {"date": (launch - timedelta(weeks=4)).strftime("%Y-%m-%d"), "actions": ["Create Product Hunt account (if new)", "Set up Google Analytics 4 on all domains", "Install Microsoft Clarity for heatmaps", "Create Canva account, design social templates", "Set up Substack newsletter", "Create Discord server", "Write first blog post: 'Layer 0 Explained'"]},
        "week_minus_3": {"date": (launch - timedelta(weeks=3)).strftime("%Y-%m-%d"), "actions": ["Write 3 guest blog pitches", "Record 60-second demo video (Loom)", "Design Product Hunt gallery images (4 images)", "Create LinkedIn content calendar (12 posts)", "Create Twitter content calendar (20 tweets)", "Write press release", "Submit to 8 free PR distribution sites"]},
        "week_minus_2": {"date": (launch - timedelta(weeks=2)).strftime("%Y-%m-%d"), "actions": ["Join 5 Discord/Slack communities, start engaging", "Post on Indie Hackers: '200K Downloads, £0 Revenue'", "Start Reddit engagement (r/MachineLearning, r/artificial)", "Reach out to 15 journalists", "Respond to 5 HARO/Qwoted queries", "Submit to 20 free directories", "Publish first newsletter"]},
        "week_minus_1": {"date": (launch - timedelta(weeks=1)).strftime("%Y-%m-%d"), "actions": ["Finalize Product Hunt listing", "Prepare first comment (founder story)", "Build launch-day support list (50 people)", "Schedule social media posts for launch day", "Prepare 'Product Hunt exclusive' offer", "Test all links, images, signup flows", "Set up UTM tracking for all campaigns", "Create launch-day landing page"]},
        "launch_day": {"date": launch_date, "actions": ["12:01 AM PST: Submit to Product Hunt", "12:05 AM PST: Post first comment, message supporters", "12:30 AM PST: Post on Twitter/X, LinkedIn, Indie Hackers", "1:00 AM PST: Submit to Hacker News 'Show HN'", "2:00 AM PST: Message broader network", "6:00 AM PST: Post on Reddit", "12:00 PM PST: Peak traffic — respond to EVERY comment", "6:00 PM PST: Final push, thank supporters", "11:59 PM PST: Launch day ends — analyze results"]},
        "week_plus_1": {"date": (launch + timedelta(weeks=1)).strftime("%Y-%m-%d"), "actions": ["Thank supporters on all platforms", "Analyze traffic, conversions, feedback", "Follow up with interested journalists", "Publish post-launch blog post", "Convert trial users to paid (email sequence)", "Add Product Hunt badge to website", "Plan next launch (feature update, new MCP server, etc.)", "Continue weekly content, community engagement, newsletter"]},
        "week_plus_2": {"date": (launch + timedelta(weeks=2)).strftime("%Y-%m-%d"), "actions": ["Analyze full campaign performance", "Identify top-performing channels", "Double down on what worked", "Plan next campaign (feature update, new MCP server, etc.)", "Continue weekly content, community, newsletter", "Start A/B tests based on launch data", "Optimize conversion funnel based on analytics"]}
    }

    assets = {
        "press_release": f"CSOAI_Launches_{campaign_name}_Press_Release.md",
        "product_hunt_gallery": ["gallery_1_hero.png (1270x760)", "gallery_2_dashboard.png (1270x760)", "gallery_3_features.png (1270x760)", "gallery_4_pricing.png (1270x760)"],
        "demo_video": f"csoai_{campaign_name}_demo_60sec.mp4",
        "social_media_kit": {"linkedin_posts": 12, "twitter_posts": 20, "reddit_posts": 5, "indiehackers_post": 1},
        "email_sequence": ["launch_announcement.html", "day_3_followup.html", "day_7_case_study.html", "day_14_conversion.html"],
        "utm_tags": {"producthunt": f"utm_source=producthunt&utm_medium=launch&utm_campaign={campaign_name}", "hackernews": f"utm_source=hackernews&utm_medium=showhn&utm_campaign={campaign_name}", "twitter": f"utm_source=twitter&utm_medium=social&utm_campaign={campaign_name}", "linkedin": f"utm_source=linkedin&utm_medium=social&utm_campaign={campaign_name}", "reddit": f"utm_source=reddit&utm_medium=community&utm_campaign={campaign_name}", "email": f"utm_source=email&utm_medium=newsletter&utm_campaign={campaign_name}"}
    }

    return {
        "campaign_name": campaign_name,
        "launch_date": launch_date,
        "primary_platform": primary_platform,
        "content_type": content_type,
        "timeline": timeline,
        "assets": assets,
        "budget": {"total": "£100", "allocation": {"design_tools": "£5 (Canva Pro 1 month)", "analytics_tools": "£10 (Plausible or PostHog trial)", "social_automation": "£10 (Typefully or Hypefury trial)", "email_tools": "£15 (Beehiiv or ConvertKit upgrade)", "pr_distribution": "£15 (premium tier on 1-2 PR sites)", "contingency": "£55 (ads test, unexpected costs, paid partnerships)"}},
        "expected_results": {"website_visitors": "10,000-50,000", "product_signups": "100-500", "newsletter_subscribers": "200-1,000", "social_followers": "500-2,000", "github_stars": "50-200", "media_mentions": "1-5", "paying_customers": "10-50", "mrr_increase": "£500-£2,500"},
        "success_metrics": ["Website traffic (GA4)", "Conversion rate (signup to paying)", "Social engagement (likes, shares, comments)", "Press mentions (media monitoring)", "GitHub stars (organic growth)", "Newsletter subscribers (Beehiiv/Substack)", "Community members (Discord)", "Revenue (Stripe dashboard)"],
        "free_tools_checklist": ["✅ Google Analytics 4 (free)", "✅ Google Search Console (free)", "✅ Microsoft Clarity (free)", "✅ Canva (free tier)", "✅ Loom (free tier)", "✅ OBS Studio (free)", "✅ GitHub Pages (free)", "✅ Hashnode (free)", "✅ Dev.to (free)", "✅ Medium (free)", "✅ Substack (free)", "✅ Beehiiv (free up to 2,500)", "✅ Discord (free)", "✅ Slack (free)", "✅ GitHub Discussions (free)", "✅ PRLog (free)", "✅ PR.com (free)", "✅ OpenPR (free)", "✅ IssueWire (free tier)", "✅ NewswireToday (free)", "✅ LinkedIn (free)", "✅ Twitter/X (free)", "✅ Reddit (free)", "✅ Indie Hackers (free)", "✅ Product Hunt (free)", "✅ Hacker News (free)", "✅ SaaSHub (free)", "✅ AlternativeTo (free)", "✅ G2 (free)", "✅ Capterra (free)", "✅ GetApp (free)", "✅ Ubersuggest (free tier)", "✅ AnswerThePublic (free tier)", "✅ Hunter.io (free tier)", "✅ HARO (free)", "✅ Qwoted (free)"]
    }

if __name__ == "__main__":
    mcp.run()