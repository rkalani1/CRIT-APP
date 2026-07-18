# CRIT-APP content & design review — 2026-07-18

Private editorial note. Not in the public nav. Scope: accuracy, currency, minimalism, design, and quiet machine-consumability of the public MkDocs ebook. Baseline at session start: all gates green (21 structural tests, originality, figure coverage, asset manifest, math examples, accuracy figures, `mkdocs build --strict`, postprocess, validate_rendered_site).

## 1.1 Inventory

- **Nav**: Introduction (`index.md`) → Evidence register → Book (28 chapters, five parts). `use_directory_urls: false`, so public URLs are `.../curriculum/NN-...html`.
- **Shared chapter pattern**: `## Opening` → teaching figure(s) → one-sentence italic hook → named-framework sections → worked (synthetic) example → pitfalls → clinical/epi notes → cross-links → summary → practice questions → footer disclaimer.
- **Figure system**: raster PNGs under `docs/assets/figures/` (93 files) + `manifest.json` with hashes/software metadata. Postprocess collapses opening figures 2+ into a `<details class="opening-figure-gallery">` and forces intrinsic sizes, lazy/eager loading, and semantic `<figure>`/`<figcaption>`.
- **Prior audits**: evidence register spot-checks dated 2026-07-15 (10 trial rows) and 2026-07-16 (AHA/ASA 2026 guideline); originality swarm verdict under `_meta/`. Learning-objective sections intentionally removed and guarded by `test_ebook_site.py`.

## 1.2 Surface scores (1–5: Accuracy · Currency · Clarity · Density · Pedagogy · Citation · Figure utility)

| Surface | A | Cur | Clr | Den | Ped | Cit | Fig | Note |
|---|---|---|---|---|---|---|---|---|
| Landing (`index.md`) | 5 | 5 | 5 | 5 | 5 | 4 | 4 | Tight, decision-first; synthetic figure labeled. |
| Evidence register | 5 | 4→5 | 5 | 5 | 5 | 5 | — | Bounded contract is exemplary; now dated 2026-07-18. |
| Ch 1 | 5 | 5 | 4 | 2→3 | 5 | 4 | 3→4 | Worst density; opening figure stack + repeated scene. |
| Ch 2 | 5 | 5 | 4→5 | 3→4 | 5 | 4 | 3→4 | Throat-clearing trimmed; opening caption now teaches. |
| Core methods 3–7 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | Solid. Echo captions only weakness. |
| Effect sizes 11–13 | 5 | 5 | 5 | 4 | 5 | 5 | 4 | Ch 12 numbers grounded (C-08/09); Ch 13 exercise softened. |
| AI/ML (14) | 5 | 5 | 5 | 4 | 5 | 4 | 3→5 | Opening captions now teach leakage/site-shift. |
| Journal club / autopsies (15–16) | 5 | 5 | 4 | 3 | 5 | 4 | 3→4 | Ch 16 duplicate alt text fixed; Ch 15 padded (open). |
| Advanced epi 17–28 | 5 | 5 | 5 | 4 | 5 | 4 | 4 | No new quantitative landmines; Ch 17 footer normalized. |
| CSS/JS/print | 5 | 5 | 5 | 5 | — | — | 5 | Multi-device + print contracts tested and green. |

## 1.3 Accuracy & currency verifications (this session)

- **C-11 (AHA/ASA 2026 AIS guideline)** — VERIFIED/KEEP. "2026 Guideline for the Early Management of Patients With Acute Ischemic Stroke," AHA/ASA, published online 26 Jan 2026 in *Stroke*, DOI `10.1161/STR.0000000000000513`; replaces the 2018 guideline + 2019 update. Citation and DOI match the chapter and register. Register status updated with the confirmation.
- **C-09 (HERMES)** — VERIFIED/KEEP. Pooled mRS 0–2 46.0% vs 26.5%; common OR 2.49; NNT 2.6 for a ≥1-category mRS improvement (Goyal et al., Lancet 2016). Matches the register extraction. Status re-confirmed 2026-07-18.
- No numeric claim was changed; no new row promoted to "checked." Currency note added to the register with explicit bounded scope.

## 1.4 Findings

| ID | Sev | Category | Surface | Evidence | Recommendation | Status |
|---|---|---|---|---|---|---|
| CRIT-001 | P2 | Density | Ch 1 opening | Three stacked opening figures whose captions echo alt text; the reading-flow figure duplicates Ch 2's, prediction/causation duplicates Ch 3's | Reduce opening to one focused figure (rel-vs-abs), move prediction/causation figure to its own section, de-echo captions | FIXED |
| CRIT-002 | P2 | Density | Ch 1 intro | The three-PDF scene is narrated three times (opening hook, intro paragraph, worked example) | Compress the intro re-narration; keep the hook and the worked example | FIXED |
| CRIT-003 | P2 | Density/clarity | Ch 2 | Four-paragraph "Conceptual Core" restates one idea; opening caption echoes alt | Tighten to two paragraphs (keep the advertisement/product metaphor and the pinned HR line); teaching caption | FIXED |
| CRIT-004 | P2 | Accuracy overclaim | Ch 13 Q7 | Exercise asserts a settled "optimal 21-day duration" of DAPT as fact, presupposing the conclusion | Reframe as open analysis tied to trial regimens and current guidance | FIXED |
| CRIT-005 | P3 | Consistency | Ch 17 footer | Footer variant ("original teaching materials", lowercase, line-wrapped) diverges from the 27 other chapters | Normalize to the standard footer | FIXED |
| CRIT-006 | P2 | Figure a11y | Ch 14/24/25 openings | Landing-route chapters open with captions that merely echo alt text | Teaching captions grounded in each chapter's prose | FIXED |
| CRIT-007 | P2 | Figure a11y | Ch 16 opening | Two of three opening figures share identical alt text "Paper autopsy sequence." | Distinct alt + teaching captions | FIXED |
| CRIT-008 | P2 | Machine-readability | Site root | No `llms.txt`; machine consumers must parse HTML nav | Add quiet, non-promotional `llms.txt` listing real chapter URLs + bounded evidence-register purpose | FIXED |
| CRIT-009 | P1 | Currency | Evidence register | Register undated for today; freshest guideline claim unverified this cycle | Verify C-11/C-09 against primary sources; add dated 2026-07-18 currency note | FIXED |

## 1.5 Follow-up items — completed 2026-07-18 (second pass)

- **CRIT-010 (P2, density)**: DONE. Tightened the chapter-preview throat-clearing in Ch 15, 18, and 23 (removed "This chapter provides/introduces/delineates…" table-of-contents sentences, kept the substantive content). Ch 22's opener was re-read and left as-is: it is substantive teaching (detection ≠ benefit), not filler.
- **CRIT-011 (P2, figure a11y)**: DONE across the whole book. Every opening figure caption that merely echoed its alt text now teaches a distinct point grounded in the chapter's own prose (Ch 03–13, 15, 17–20, 22, 23, 26, 27, 28, in addition to 01/02/14/16/24/25 from the first pass). Also fixed malformed caption/image spacing in several openers, so those figures now render as clean semantic `<figure>` elements (rendered semantic figures 84 → 94; opening galleries 17 → 22). Ch 21 intentionally has no opening figure (text hook).
- **CRIT-012 (P3, design)**: DONE. Vendored the three font families (Source Serif 4, Source Sans 3, JetBrains Mono — latin subset, 11 woff2 files, ~601 KiB) under `docs/assets/fonts/` and replaced the network `@import` in `extra.css` with local `@font-face` rules. The built site now makes **zero** external font requests (fonts.googleapis.com / fonts.gstatic.com refs = 0); non-latin glyphs fall back to the system stack. Fonts are OFL 1.1, so redistribution is license-clean.
- No P0/P1 accuracy or IP items remain open. Residual: a handful of chapters still carry moderately essayistic mid-body prose (not openers) that could be tightened in a future pass, but none delays the teaching point at the opening.

## 1.6 Boundaries honored

No invented trial results, NNTs, windows, or COR/LOE. No learning-objective sections reintroduced. No agent-marketing copy on the human UI (`llms.txt` is a quiet technical surface only). CC BY / educational disclaimer preserved. No PHI, no institution-specific pathway framing. All numbers changed = none; only an overclaimed qualifier ("optimal") removed and captions/prose tightened.
