#!/usr/bin/env python3
"""Add MEOK favicon, apple-touch-icon and OG/Twitter meta tags to csoai-org pages."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
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
    "meok-ai.html",
]

LINK_BLOCK = '''  <link rel="icon" type="image/svg+xml" href="/assets/favicon.svg">
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/apple-touch-icon.png">
  <meta name="theme-color" content="#F7F3EE">'''


def add_meta(path: Path) -> None:
    text = path.read_text(encoding="utf-8")
    if '/assets/favicon.svg' in text:
        print(f"Skip {path.name}: already has favicon")
        return

    title_match = re.search(r'<title>(.*?)</title>', text, re.IGNORECASE)
    title = title_match.group(1) if title_match else "CSOAI"
    desc_match = re.search(r'<meta name="description" content="([^"]*)"', text, re.IGNORECASE)
    description = desc_match.group(1) if desc_match else "Sovereign AI governance by CSOAI."

    og_block = f'''{LINK_BLOCK}
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://csoai.org/{path.name}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:image" content="https://csoai.org/assets/og-image.png">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:image" content="https://csoai.org/assets/og-image.png">'''

    # Insert after the first </title>
    text = re.sub(
        r'(</title>\s*)',
        r'\1\n  ' + og_block.replace('\n', '\n  ') + '\n',
        text,
        count=1,
        flags=re.IGNORECASE,
    )
    path.write_text(text, encoding="utf-8")
    print(f"Updated {path.name}")


def main() -> int:
    for name in PAGES:
        path = ROOT / name
        if not path.exists():
            print(f"Skip {name}: not found")
            continue
        add_meta(path)
    return 0


if __name__ == "__main__":
    sys.exit(main())
