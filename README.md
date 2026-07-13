# CRIT-APP

**Critical Appraisal for Neurologists — Web Edition**

Free, original teaching curriculum for stroke-aware critical appraisal.

- Live: https://rkalani1.github.io/CRIT-APP/
- Sibling: https://rkalani1.github.io/ML/

## Safety / originality

This is **not** a reprint of commercial EBM handbooks, journal PDFs, paper abstracts, or guideline instruments. Teaching figures are original (code-drawn). Content is CC BY 4.0; site code is ISC. Educational only — not medical advice.

See `docs/about.md` and `docs/ORIGINALITY.md`.

## Develop

```bash
pip install mkdocs-material pymdown-extensions
python scripts/originality_scan.py
mkdocs serve
```

## Update a chapter

Edit `docs/curriculum/*.md` → PR → CI deploys Pages.
