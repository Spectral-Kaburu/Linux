# This script extracts colors(No descritpion)

import re
suffix = input("File suffix? (leave empty if none): ").strip()

if not suffix:                                   # covers empty string or whitespace
    INPUT_FILE = "gnome-shell.css"
    OUTPUT_FILE = "analyze/colors.txt"
else:
    if suffix == "bak":
        INPUT_FILE = f"gnome-shell.css.{suffix}"
    else:
        INPUT_FILE = f"gnome-shell-{suffix}.css"
    
    OUTPUT_FILE = f"analyze/colors-{suffix}.txt"
# Variables!!
ALL_COLORS = []                 # sorted list of all colors
TOTAL_COLORS = {}               # dictionary of colors and their occurrence count!
COLORS = []                     # list of [color, occurrence count]
REPLACEMENTS = []               # list of colors with higher than LIMIT occurence count
SEEN = set()                    # set of distinct colors found i INPUT_FILE
LIMIT = 10                      # Occurrence count limit for replacements

# Read the CSS file
with open(INPUT_FILE, 'r', encoding='utf-8') as f:
    content = f.read()

# Regex for hex colors: # followed by 3, 4, 6, or 8 hex digits
hex_pattern = r'#([0-9a-fA-F]{3,4}|[0-9a-fA-F]{6}|[0-9a-fA-F]{8})\b'

# Regex for rgba() and rgb() values
rgba_pattern = r'rgba?\s*\(\s*\d+\s*,\s*\d+\s*,\s*\d+\s*(?:,\s*[\d.]+\s*)?\)'

# Find all matches
hex_colors = re.findall(hex_pattern, content)
rgba_colors = re.findall(rgba_pattern, content)

# Reconstruct full hex colors (add # back)
full_hex = ['#' + h for h in hex_colors]

# Combine and remove duplicates while preserving order
for color in full_hex + rgba_colors:
    color = color.lower()
    if color in SEEN:
        TOTAL_COLORS[color] += 1
        continue
    else:
        SEEN.add(color)
        ALL_COLORS.append(color)
        TOTAL_COLORS.__setitem__(color, 1)

# Output one color per line, sorted for easier reading
ALL_COLORS.sort(key=lambda x: x)

for finder in ALL_COLORS:
    namba = TOTAL_COLORS.get(finder)
    COLORS.append([namba, finder])
    # if namba >= LIMIT:
    REPLACEMENTS.append((finder, namba))
COLORS.sort()

with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
    f.write(f"=== EXTRACTED COLORS FROM {INPUT_FILE} IN ORDER OF OCCURRENCE ===\n\n")
    for i in range(len(ALL_COLORS)):
        color = ALL_COLORS[i]
        count = TOTAL_COLORS.get(color)
        space = "       |       "
        f.write(f"{color}{space}{count}" + "\n")
    f.write(f"\nTotal unique colors found: {len(ALL_COLORS)}\n")

    """f.write(f"=== EXTRACTED COLORS FROM {INPUT_FILE} IN ASCENDING ORDER ===\n\n")
    for set in ALL_COLORS:
        f.write(f"{set}" + "\n")
    f.write(f"\nTotal unique colors found: {len(ALL_COLORS)}\n")"""

    f.write("\n===The replacements list is limited by the set LIMIT ===\n")
    f.write("\nreplacements = {\n")
    for color, namba in REPLACEMENTS:
        f.write(f"    '{color}' : '',       # Appeared [ {namba} ] times\n")
    f.write("}\n")

print(f"\nTotal unique colors found: {len(ALL_COLORS)}"+"\n")
