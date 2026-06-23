#!/usr/bin/env python3
"""
Apply MEOK.AI warm sovereign palette to legacy csoai-org static HTML pages.
- Replaces dark navy/teal/gold hex colors inside <style> blocks and inline styles.
- Injects the shared csoai-org-theme.css override before </head>.
- Adds a MEOK orb to the homepage hero.
- Tags the Stripe pricing section for styling.
"""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
THEME_LINK = '<link rel="stylesheet" href="/assets/design-system/csoai-org-theme.css">'

# Files to process
PAGES = [
    "index.html",
    "about.html",
    "charter.html",
    "pricing.html",
    "contact.html",
    "os.html",
    "mcp-infrastructure.html",
    "legal.html",
    "privacy.html",
    "terms.html",
    "cookies.html",
    "checkout.html",
    "verify.html",
    "switch.html",
]

# Old hex -> new MEOK hex (case-insensitive)
COLOR_MAP = {
    # dark navy backgrounds -> warm cream
    "#1B2A4A": "#F7F3EE",
    "#0F1A2E": "#EDE8E1",
    "#0A1428": "#F7F3EE",
    "#050A15": "#EDE8E1",
    "#273548": "#F7F3EE",
    "#243548": "#EDE8E1",
    "#1F3550": "#EDE8E1",
    "#2A4A6A": "#F7F3EE",
    "#1A3A4A": "#EDE8E1",
    "#111111": "#EDE8E1",
    "#111": "#EDE8E1",
    # light text on dark -> dark ink
    "#FFFFFF": "#1A1816",
    "#ffffff": "#1A1816",
    "#FFF": "#1A1816",
    "#fff": "#1A1816",
    # muted grays
    "#B0B8C8": "#6B6560",
    "#8A92A2": "#6B6560",
    "#A8B0C0": "#6B6560",
    "#E8E8E8": "#D9CFC3",
    "#666666": "#6B6560",
    "#666": "#6B6560",
    "#2A3F5F": "#4A4540",
    # teal -> sage
    "#0D7377": "#7D8C7E",
    "#14919B": "#A8B6A9",
    # gold -> champagne
    "#D4A843": "#C8A873",
    "#B8912E": "#B08D52",
    "#c9a84c": "#C8A873",
}


def replace_colors(text: str) -> str:
    def sub_css(css: str) -> str:
        for old, new in COLOR_MAP.items():
            css = re.sub(re.escape(old), new, css, flags=re.IGNORECASE)
        return css

    # Replace inside <style>...</style>
    def style_repl(m: re.Match) -> str:
        return m.group(1) + sub_css(m.group(2)) + m.group(3)

    text = re.sub(
        r"(<style[^>]*>)(.*?)(</style>)",
        style_repl,
        text,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Replace inside style="..."
    def inline_repl(m: re.Match) -> str:
        return 'style="' + sub_css(m.group(1)) + '"'

    text = re.sub(r'style="([^"]*)"', inline_repl, text, flags=re.IGNORECASE)
    return text


def inject_theme_link(text: str) -> str:
    if THEME_LINK in text:
        return text
    # Insert before </head>
    head_close = re.search(r"</head>", text, flags=re.IGNORECASE)
    if head_close:
        pos = head_close.start()
        return text[:pos] + "  " + THEME_LINK + "\n" + text[pos:]
    return text


def add_orb_to_index(text: str) -> str:
    if 'class="meok-orb"' in text:
        return text
    # Insert an orb after the hero-bg-animated div
    return re.sub(
        r'(<div class="hero-bg-animated">.*?</div>)(\s*)(<div class="hero-content">)',
        r'\1\2<div class="meok-orb" style="position:absolute;right:8%;top:50%;transform:translateY(-50%);z-index:1;opacity:0.9;"></div>\2\3',
        text,
        flags=re.DOTALL,
    )


def tag_stripe_section(text: str) -> str:
    # The Stripe section is a <section style="background:linear-gradient..."> near the end.
    # Add class="stripe-section" if it exists and doesn't already have it.
    return re.sub(
        r'<section style="background:linear-gradient\(135deg,#1B2A4A,#0F1A2E\);',
        '<section class="stripe-section" style="background:linear-gradient(135deg,#EDE8E1,#F7F3EE);',
        text,
        flags=re.IGNORECASE,
    )


def update_theme_color(text: str) -> str:
    return re.sub(
        r'<meta name="theme-color" content="[^"]*">',
        '<meta name="theme-color" content="#F7F3EE">',
        text,
        flags=re.IGNORECASE,
    )


def process_file(path: Path, is_index: bool = False) -> None:
    text = path.read_text(encoding="utf-8")
    text = replace_colors(text)
    text = inject_theme_link(text)
    text = tag_stripe_section(text)
    text = update_theme_color(text)
    if is_index:
        text = add_orb_to_index(text)
    path.write_text(text, encoding="utf-8")
    print(f"Updated {path.relative_to(ROOT)}")


def main() -> int:
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            print(f"Skip {name}: not found")
            continue
        process_file(path, is_index=(name == "index.html"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
