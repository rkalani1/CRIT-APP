import os, glob
path = r"C:\Users\rkala\CRIT-APP\docs\curriculum\*.md"
files = glob.glob(path)
for f in files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
        words = len(content.split())
        if words < 2500:
            print(f"THIN: {os.path.basename(f)}: {words} words")
        else:
            print(f"OK: {os.path.basename(f)}: {words} words")
