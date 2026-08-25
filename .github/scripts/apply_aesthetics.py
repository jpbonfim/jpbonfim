import os
import re

def patch_file(filepath, patches):
    if not os.path.exists(filepath):
        print(f"File {filepath} not found. Skipping.")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    for pattern, replacement in patches:
        content = re.sub(pattern, replacement, content)

    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Successfully patched {filepath}")
    else:
        print(f"No changes made to {filepath}")

def main():
    # 1. Patch stats.svg
    patch_file('profile/stats.svg', [
        (r'stroke-opacity="0"', r'stroke-opacity="1"')
    ])

    # 2. Patch top-langs.svg
    patch_file('profile/top-langs.svg', [
        # Fix dimensions
        (r'<svg width="300" height="285" viewBox="0 0 300 285"', r'<svg width="350" height="285" viewBox="0 0 350 285"'),
        (r'width="299" fill="#000000" stroke-opacity="0"', r'width="349" fill="#000000" stroke-opacity="1"'),
        (r'width="299" fill="#000000" stroke-opacity="1"', r'width="349" fill="#000000" stroke-opacity="1"'),
        
        # In case stroke-opacity wasn't bundled with width="299" in the regex match:
        (r'stroke-opacity="0"', r'stroke-opacity="1"'),
        
        # Fix font sizes
        (r'\.lang-name\s*\{\s*font:\s*400\s*11px', r'.lang-name { font: 600 14px'),
        
        # Shift second column
        (r'<g transform="translate\(150,\s*0\)">', r'<g transform="translate(180, 0)">')
    ])

    # 3. Patch activity-graph.svg
    patch_file('profile/activity-graph.svg', [
        # Fix dot colors
        (r'stroke:\s*#000000;\s*animation:\s*blink\s*1s', r'stroke: #ff9900;\n      animation: blink 1s'),
        
        # Fix background card (corners and stroke)
        (r'<rect xmlns="http://www\.w3\.org/2000/svg" data-testid="card_bg" id="cardBg"\s*x="0" y="0" rx="0" height="100%" stroke="#E4E2E2" fill-opacity="1"\s*width="100%" fill="#000000" stroke-opacity="1" style="stroke:#0000; stroke-width:1;"/>', 
         r'<rect xmlns="http://www.w3.org/2000/svg" data-testid="card_bg" id="cardBg"\n            x="0.5" y="0.5" rx="4.5" height="99%" stroke="#ff9900" fill-opacity="1"\n            width="1199" fill="#000000" stroke-opacity="1" style="stroke:#ff9900; stroke-width:1;"/>')
    ])

if __name__ == "__main__":
    main()
