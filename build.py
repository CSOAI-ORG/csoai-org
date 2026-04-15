#!/usr/bin/env python3
import re, glob, os

with open('fragments/nav.html') as f:
    nav = f.read()
with open('fragments/footer.html') as f:
    footer = f.read()

files = sorted(glob.glob('*.html'))
for fname in files:
    with open(fname) as f:
        text = f.read()
    
    # Replace nav
    new_text = re.sub(r'<!-- ═══ MEGA NAV ═══ -->.*?<\/script>\s*(?=\n\s*<)', nav, text, count=1, flags=re.DOTALL)
    if new_text == text:
        print(f'SKIPPED nav {fname} (no match)')
    
    # Replace footer
    final_text = re.sub(r'<footer style="background:var\(--dark\);.+?<\/footer>', footer, new_text, count=1, flags=re.DOTALL)
    if final_text == new_text:
        print(f'SKIPPED footer {fname} (no match)')
    
    with open(fname, 'w') as f:
        f.write(final_text)
    print(f'Updated {fname}')
