import re

# === YOUR red REPLACEMENTS ===
# === BOLDER / #e000e0 inspired replacements ===
replacements = {
    # Core light foreground → very bright reds

    '#eeeeec'     : '#ffdddd',
    'white'       : '#ffeeee',
    '#ffffff'     : '#ffeeee',
    '#e6e6e6'     : '#ffcccc',

    # Strong / selected / active / focus
    '#ff6666'     : '#ff3333',
    '#d32f2f'     : '#ff1a1a',
    '#ff4444'     : '#ff0000',     # pure red for the most important states

    # Secondary / disabled / meta / hints
    'rgba(255, 255, 255, 0.8)'  : 'rgba(255, 120, 120, 0.85)',
    'rgba(255, 255, 255, 0.7)'  : 'rgba(255, 100, 100, 0.75)',
    'rgba(255, 255, 255, 0.5)'  : 'rgba(255,  90,  90, 0.55)',
    'rgba(255, 255, 255, 0.3)'  : 'rgba(255,  80,  80, 0.35)',
    'rgba(255, 255, 255, 0.1)'  : 'rgba(200,  40,  40, 0.15)',

    # Some mid-dark elements get slight red tint
    '#4d4d4d'     : '#440000',

    # Option C – stronger red presence in dark areas
    '#23252e'     : '#2c0000',
    '#272a34'     : '#320000',
    '#303340'     : '#3a0000',
}

with open('colors.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Hex + named color replacements
for old, new in replacements.items():
    css = css.replace(old, new)

# RGBA white-ish → RGBA red (preserves opacity)
css = re.sub(r'rgba?\(244,\s*245,\s*246,\s*([\d.]+)\)', r'rgba(232, 184, 255, \1)', css)
css = re.sub(r'rgba?\(255,\s*255,\s*255,\s*([\d.]+)\)', r'rgba(240, 207, 255, \1)', css)

with open('colors-red.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("✅ Done! New red theme saved as colors-red.css")