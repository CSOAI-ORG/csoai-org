import re, os

with open('about.html') as f:
    text = f.read()

nav_match = re.search(r'(<!-- ═══ MEGA NAV ═══ -->.*?<\/script>)\s*(?=\n\s*<)', text, re.DOTALL)
nav = nav_match.group(1) if nav_match else ''

footer_match = re.search(r'(<footer style="background:var\(--dark\);.+?<\/footer>)', text, re.DOTALL)
footer = footer_match.group(1) if footer_match else ''

print('Nav chars:', len(nav))
print('Footer chars:', len(footer))

os.makedirs('fragments', exist_ok=True)
with open('fragments/nav.html', 'w') as f:
    f.write(nav)
with open('fragments/footer.html', 'w') as f:
    f.write(footer)
