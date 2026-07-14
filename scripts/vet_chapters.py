import os, glob, json, re

path = r"C:\Users\rkala\CRIT-APP\docs\curriculum\*.md"
files = glob.glob(path)
checklist = {}

for f in files:
    filename = os.path.basename(f)
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        
    words = len(content.split())
    issues = []
    fixes = []
    pass_status = True
    
    # 1. Thoroughness check
    if words < 2500:
        issues.append("Thin chapter (< 2.5k words). Lacks thoroughness.")
        fixes.append("Expand with original prose, clinical examples, and deep-dives.")
        pass_status = False
        
    # 2. Safety / Guidelines check
    if "copyright " in content.lower() or "all rights reserved" in content.lower():
        issues.append("Potential commercial handbook paste detected.")
        fixes.append("Rewrite content in original prose.")
        pass_status = False
        
    if "abstract:" in content.lower() or ("background:" in content.lower() and "methods:" in content.lower()):
        issues.append("Contains raw paper abstracts.")
        fixes.append("Remove abstract text and summarize findings natively.")
        pass_status = False
        
    # 3. Structure / Clarity
    headings = re.findall(r'^#+ ', content, flags=re.MULTILINE)
    if len(headings) < 3:
        issues.append("Poor heading hierarchy (too few headings).")
        fixes.append("Add structured H2 and H3 headings to improve readability.")
        pass_status = False
        
    # 4. Figures check
    images = re.findall(r'!\[.*?\]\(.*?\)', content)
    if len(images) == 0:
        issues.append("Missing visual/figure.")
        fixes.append("Add at least one strong visual diagram or figure.")
        pass_status = False

    checklist[filename] = {
        "pass": pass_status,
        "issues": issues,
        "fixes": fixes
    }

with open(r"C:\Users\rkala\CRIT-APP\_meta\VET_CHECKLIST.json", 'w', encoding='utf-8') as out:
    json.dump(checklist, out, indent=4)
print("VET_CHECKLIST.json generated.")
