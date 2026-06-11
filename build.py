#!/usr/bin/env python3
import re, glob, os
from pathlib import Path

with open('fragments/nav.html') as f:
    nav = f.read()
with open('fragments/footer.html') as f:
    footer = f.read()

# Target all HTML files in root and subdirectories
files = []
for pattern in ['*.html', 'public/*.html', 'sectors/*.html', 'public/sectors/*.html', 'public/frameworks/*.html']:
    files.extend(glob.glob(pattern))

for fname in sorted(set(files)):
    with open(fname) as f:
        text = f.read()
    
    # Replace nav
    new_text = re.sub(r'<!-- ═══ MEGA NAV ═══ -->.*?<\/script>\s*(?=\n\s*<)', nav, text, count=1, flags=re.DOTALL)
    if new_text == text:
        # Try a simpler match if the first one fails
        new_text = re.sub(r'<!-- ═══ MEGA NAV ═══ -->.*?<\/script>', nav, text, count=1, flags=re.DOTALL)
    
    if new_text == text:
        # Fallback for Next.js exported files: find the sticky nav or common header
        new_text = re.sub(r'<nav class="sticky top-0.+?<\/nav>', nav, text, count=1, flags=re.DOTALL)
        
    if new_text == text:
        print(f'SKIPPED nav {fname} (no match)')
    
    # Replace footer
    final_text = re.sub(r'<footer style="background:var\(--dark\);.+?<\/footer>', footer, new_text, count=1, flags=re.DOTALL)
    if final_text == new_text:
        # Try a simpler footer match
        final_text = re.sub(r'<footer.*?<\/footer>', footer, new_text, count=1, flags=re.DOTALL)
        
    if final_text == new_text:
        print(f'SKIPPED footer {fname} (no match)')

    
    with open(fname, 'w') as f:
        f.write(final_text)
    print(f'Updated {fname}')
