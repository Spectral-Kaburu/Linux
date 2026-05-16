import re

replacements = {
    # Core light foreground → very bright purples

    '#ffdddd'     : "#ed1616",
    '#ffeeee'     : '#de1616',
    '#ffcccc'     : "#cf1616",
}

with open('colors-red.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Hex + named color replacements
for old, new in replacements.items():
    css = css.replace(old, new)

"""# RGBA white-ish → RGBA red (preserves opacity)
css = re.sub(r'rgba?\(244,\s*245,\s*246,\s*([\d.]+)\)', r'rgba(232, 184, 255, \1)', css)
css = re.sub(r'rgba?\(255,\s*255,\s*255,\s*([\d.]+)\)', r'rgba(240, 207, 255, \1)', css)"""

with open('colors-red.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✅ Done! New red theme saved as colors-red.css")