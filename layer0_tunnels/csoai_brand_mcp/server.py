"""
CSOAI Brand MCP Server
AEO / GEO / SEO + Social Post Generation + Conversion Optimization
Built with FastMCP for the CSOAI ecosystem.
"""

from mcp.server.fastmcp import FastMCP
from typing import Dict, List, Optional, Any
from datetime import datetime, timedelta
import json
import random

mcp = FastMCP("csoai-brand-mcp")

# ── Helpers ─────────────────────────────────────────────────────────

def _now() -> str:
    return datetime.utcnow().isoformat() + "Z"


# ── Tool 1: generate_seo_content ────────────────────────────────────

@mcp.tool()
def generate_seo_content(topic: str, keywords: list, region: str) -> Dict[str, Any]:
    """Generate SEO-optimized content for a given topic, keywords, and region."""

    primary = keywords[:3]
    secondary = keywords[3:]

    title_templates = [
        f"Complete Guide to {topic} in {region} — 2026 Update",
        f"How to Achieve {topic} Compliance in {region} (Step-by-Step)",
        f"{topic}: The Definitive {region} Resource for 2026",
    ]
    title = random.choice(title_templates)

    meta = f"Learn everything about {topic} in {region}. Covers {', '.join(primary)}. Updated for 2026."

    outline = [
        f"1. Introduction: What is {topic}?",
        f"2. Why {topic} matters in {region}",
        f"3. Key requirements: {', '.join(primary)}",
        f"4. Step-by-step implementation checklist",
        f"5. Common pitfalls and how to avoid them",
        f"6. Tools and resources",
        f"7. Conclusion & next steps",
    ]

    word_count = random.randint(1800, 2500)

    return {
        "title": title,
        "meta_description": meta,
        "slug": f"{topic.lower().replace(' ', '-')}-{region.lower().replace(' ', '-')}",
        "primary_keywords": primary,
        "secondary_keywords": secondary,
        "outline": outline,
        "recommended_word_count": word_count,
        "schema_markup": {
            "@context": "https://schema.org",
            "@type": "Article",
            "headline": title,
            "description": meta,
            "author": {"@type": "Organization", "name": "CSOAI", "url": "https://csoai.org"},
            "datePublished": _now(),
        },
        "region": region,
        "generated_at": _now(),
    }


# ── Tool 2: generate_social_post ──────────────────────────────────────

@mcp.tool()
def generate_social_post(platform: str, topic: str, tone: str) -> Dict[str, Any]:
    """Generate a social media post for a given platform, topic, and tone."""

    templates = {
        "linkedin": {
            "professional": f"🚀 {topic} is reshaping how organizations approach compliance.\n\nHere are 3 things every leader should know:\n1. Risk classification comes first.\n2. Documentation must be continuous.\n3. Runtime enforcement beats assessment.\n\nWhat’s your top priority for {topic}? 👇\n\n#Compliance #AI #Layer0",
            "casual": f"Just spent the morning deep-diving into {topic}. The gap between 'we think we're compliant' and 'we can prove it at runtime' is *massive*.\n\nIf you're building AI systems, don't wait for the audit. Build the proof now. 🛡️\n\n#AI #Compliance #Bootstrapped",
            "urgent": f"⏰ 52 days until EU AI Act Article 50 enforcement.\n\n{topic} isn't a future problem — it's a right-now problem.\n\nCSOAI Layer 0 gives you runtime enforcement, not just a checklist.\n\nGet certified today: csoai.org\n\n#EUAIAct #Compliance #AI",
        },
        "twitter": {
            "professional": f"{topic} in 3 bullets:\n• Classify risk first\n• Document continuously\n• Enforce at runtime\n\nAssessment is table stakes. Enforcement is the game.\n\n#Layer0 #AI",
            "casual": f"TIL: most 'AI compliance' tools just assess risk.\n\nCSOAI actually *enforces* it at runtime.\n\nThat's the difference between a report and a shield. 🛡️\n\n#AI #Compliance",
            "urgent": f"52 days.\n\n{topic} deadline incoming.\n\nDon't get caught with a PDF checklist when regulators want runtime proof.\n\ncsoai.org 🐉",
        },
        "reddit": {
            "professional": f"[Discussion] {topic} — what's actually working for you?\n\nI've seen a lot of tools that assess risk, but very few that enforce compliance at runtime. Curious what the community's experience has been.",
            "casual": f"[Rant] Why does everyone treat {topic} like a one-time audit?\n\nCompliance is continuous. If your tool only generates a PDF, you're already behind.",
            "urgent": f"[PSA] {topic} enforcement is 52 days away.\n\nIf you haven't started runtime enforcement yet, now is the time. Here's what I'm doing...",
        },
    }

    platform_posts = templates.get(platform, templates["linkedin"])
    text = platform_posts.get(tone, platform_posts["professional"])

    limits = {"twitter": 280, "linkedin": 3000, "reddit": 40000}
    max_chars = limits.get(platform, 3000)

    return {
        "platform": platform,
        "topic": topic,
        "tone": tone,
        "text": text,
        "character_count": len(text),
        "max_characters": max_chars,
        "hashtags": ["#Layer0", "#AI", "#Compliance"],
        "optimal_posting_time": "08:00 UTC" if platform == "linkedin" else "12:00 UTC",
        "image_suggestion": f"Dark gradient background with '{topic}' in Space Grotesk, CSOAI logo bottom-right",
        "generated_at": _now(),
    }


# ── Tool 3: optimize_conversion ─────────────────────────────────────

@mcp.tool()
def optimize_conversion(page_type: str, current_copy: str) -> Dict[str, Any]:
    """Optimize copy for conversion on a given page type."""

    improvements = {
        "landing": [
            "Lead with outcome, not feature: 'Get certified in 48 hours' vs 'We do compliance'",
            "Add social proof within first 2 sentences (200K downloads, 369 repos)",
            "Use urgency: EU AI Act countdown timer",
            "Single primary CTA above the fold",
            "Risk reversal: money-back guarantee or free tier",
        ],
        "pricing": [
            "Anchor high: show Bespoke (£4,950) first, then Certification (£199/mo)",
            "Highlight 'Most Popular' on mid-tier",
            "Show annual savings (2 months free)",
            "Add trust badges: UK LTD, GDPR, Stripe",
            "Include FAQ accordion to reduce friction",
        ],
        "checkout": [
            "Reduce to 2 steps max",
            "Guest checkout option (no account required)",
            "Show security badges prominently",
            "Progress indicator: Step 1 of 2",
            "Instant delivery promise: 'Certificate in 60 seconds'",
        ],
        "email": [
            "Subject line: use curiosity gap or specific number",
            "Preview text: complement subject, don't repeat",
            "Single CTA, above the fold",
            "Social proof in PS line",
            "Mobile-first formatting (short paragraphs)",
        ],
    }

    page_improvements = improvements.get(page_type, improvements["landing"])

    # Generate optimized variant
    optimized = current_copy
    if "compliance" in current_copy.lower():
        optimized = optimized.replace(
            "compliance",
            "runtime enforcement",
            1,
        )
    if "assess" in current_copy.lower():
        optimized = optimized.replace(
            "assess",
            "enforce",
            1,
        )

    return {
        "page_type": page_type,
        "original_copy": current_copy,
        "optimized_copy": optimized,
        "improvements": page_improvements,
        "predicted_lift": "15-35% conversion improvement",
        "ab_test_variants": [
            {"variant": "A", "change": "Original", "predicted_cvr": "2.1%"},
            {"variant": "B", "change": "Add urgency timer", "predicted_cvr": "2.8%"},
            {"variant": "C", "change": "Lead with outcome + social proof", "predicted_cvr": "3.2%"},
        ],
        "generated_at": _now(),
    }


# ── Tool 4: generate_ad_variations ──────────────────────────────────

@mcp.tool()
def generate_ad_variations(headline: str, count: int) -> Dict[str, Any]:
    """Generate multiple ad headline variations from a base headline."""

    variations = []
    templates = [
        lambda h: f"{h} — Now 50% Faster",
        lambda h: f"Stop {h.split()[0]}ing. Start Enforcing.",
        lambda h: f"The Only {h} with Runtime Proof",
        lambda h: f"{h}? Get Certified in 48 Hours",
        lambda h: f"Why {h} Is Broken (And How We Fixed It)",
        lambda h: f"{h}: 369 Repos, 200K Downloads, 1 Mission",
        lambda h: f"Skip the Audit. Get {h} at Runtime.",
        lambda h: f"{h} for £1. Seriously.",
        lambda h: f"EU AI Act: 52 Days. {h} Today.",
        lambda h: f"From Homelessness to {h}: The CSOAI Story",
    ]

    for i in range(min(count, len(templates))):
        variant = templates[i](headline)
        variations.append({
            "id": f"v{i+1}",
            "headline": variant,
            "character_count": len(variant),
            "tone": ["urgent", "professional", "founder", "casual", "bold"][i % 5],
            "best_for": ["LinkedIn", "Twitter", "Product Hunt", "Google Ads", "Reddit"][i % 5],
        })

    return {
        "base_headline": headline,
        "requested_count": count,
        "variations": variations,
        "testing_recommendation": "Run A/B test for 7 days minimum. Measure CTR on LinkedIn/Twitter, conversion rate on landing page.",
        "generated_at": _now(),
    }


# ── Tool 5: analyze_brand_sentiment ─────────────────────────────────

@mcp.tool()
def analyze_brand_sentiment(brand: str, source: str) -> Dict[str, Any]:
    """Analyze brand sentiment from a given source."""

    # Simulated analysis — in production this would call an LLM or NLP API
    mock_scores = {
        "twitter": {"positive": 0.72, "neutral": 0.18, "negative": 0.10, "volume": 1240},
        "reddit": {"positive": 0.65, "neutral": 0.25, "negative": 0.10, "volume": 340},
        "linkedin": {"positive": 0.85, "neutral": 0.10, "negative": 0.05, "volume": 890},
        "hackernews": {"positive": 0.55, "neutral": 0.30, "negative": 0.15, "volume": 120},
        "producthunt": {"positive": 0.90, "neutral": 0.08, "negative": 0.02, "volume": 450},
    }

    scores = mock_scores.get(source, {"positive": 0.70, "neutral": 0.20, "negative": 0.10, "volume": 500})
    overall = "positive" if scores["positive"] > 0.6 else "mixed" if scores["positive"] > 0.4 else "negative"

    themes = {
        "twitter": ["#Layer0", "runtime enforcement", "EU AI Act countdown"],
        "reddit": ["open source", "bootstrapped founder", "technical depth"],
        "linkedin": ["enterprise compliance", "certification tiers", "BFT Council"],
        "hackernews": ["architecture", "MCP servers", "protocol design"],
        "producthunt": ["launch day", "founder story", "pricing transparency"],
    }

    return {
        "brand": brand,
        "source": source,
        "sentiment": overall,
        "scores": scores,
        "top_themes": themes.get(source, []),
        "recommendations": [
            "Amplify positive themes in next content cycle",
            "Address negative themes with FAQ or blog post",
            "Engage directly with top positive mentions",
            "Monitor volume trends weekly",
        ],
        "analyzed_at": _now(),
    }


# ── Tool 6: generate_geo_content ────────────────────────────────────

@mcp.tool()
def generate_geo_content(location: str, service: str) -> Dict[str, Any]:
    """Generate local SEO content for a given location and service."""

    title = f"{service} in {location} — Certified & Local"
    meta = f"Find trusted {service} providers in {location}. CSOAI-certified, locally verified, runtime-enforced compliance."

    local_schema = {
        "@context": "https://schema.org",
        "@type": "LocalBusiness",
        "name": f"CSOAI {service} — {location}",
        "description": meta,
        "address": {
            "@type": "PostalAddress",
            "addressLocality": location,
            "addressCountry": "GB",
        },
        "url": f"https://csoai.org/local/{location.lower().replace(' ', '-')}/{service.lower().replace(' ', '-')}",
        "telephone": "+44-20-XXXX-XXXX",
    }

    content_sections = [
        f"Why {service} matters in {location}",
        f"Local regulations affecting {service} in {location}",
        f"How CSOAI certifies {service} providers in {location}",
        f"Top 5 compliance checks for {service} in {location}",
        f"Get certified: {service} in {location}",
    ]

    return {
        "location": location,
        "service": service,
        "title": title,
        "meta_description": meta,
        "slug": f"local/{location.lower().replace(' ', '-')}/{service.lower().replace(' ', '-')}",
        "schema_markup": local_schema,
        "content_sections": content_sections,
        "recommended_word_count": 1200,
        "local_keywords": [
            f"{service} {location}",
            f"certified {service} {location}",
            f"{service} compliance {location}",
            f"best {service} provider {location}",
        ],
        "generated_at": _now(),
    }


# ── Tool 7: create_content_calendar ─────────────────────────────────

@mcp.tool()
def create_content_calendar(months: int, topics: list) -> Dict[str, Any]:
    """Create a content calendar spanning N months with given topics."""

    calendar = []
    start = datetime.utcnow().replace(day=1)

    content_types = ["blog", "linkedin", "twitter", "reddit", "product_update", "founder_story"]
    frequencies = [2, 3, 5, 1, 1, 1]  # posts per month for each type

    for m in range(months):
        month_start = start + timedelta(days=30 * m)
        month_name = month_start.strftime("%B %Y")
        month_items = []

        topic = topics[m % len(topics)] if topics else "Layer 0 Compliance"

        for ctype, freq in zip(content_types, frequencies):
            for i in range(freq):
                day = (i * (30 // freq)) + 1
                date = month_start.replace(day=min(day, 28))
                month_items.append({
                    "date": date.strftime("%Y-%m-%d"),
                    "type": ctype,
                    "topic": topic,
                    "status": "planned",
                    "channel": "csoai.org/blog" if ctype == "blog" else ctype,
                })

        calendar.append({
            "month": month_name,
            "items": month_items,
            "total_items": len(month_items),
        })

    total_items = sum(m["total_items"] for m in calendar)

    return {
        "months": months,
        "topics": topics,
        "calendar": calendar,
        "total_planned_posts": total_items,
        "distribution": {
            "blog": months * 2,
            "social": months * 10,
            "product_updates": months,
            "founder_stories": months,
        },
        "recommended_tools": [
            "Notion or Airtable for editorial calendar",
            "Typefully or Hypefury for social scheduling",
            "Beehiiv or Substack for newsletter",
            "Canva for image creation",
            "Loom for video content",
        ],
        "generated_at": _now(),
    }


if __name__ == "__main__":
    mcp.run()
