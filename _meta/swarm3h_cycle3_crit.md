# Swarm Cycle-3 FINAL densify — CRIT-APP (open-source ebook)

**When:** 2026-07-15  
**Repo:** `C:\Users\rkala\CRIT-APP` (`rkalani1/CRIT-APP`)  
**Product posture:** open-source ebook only (no meta nav pages)

## Goals addressed

1. **≥4 NEW original code-drawn matplotlib figures** — delivered **5** via `scripts/generate_cycle3_swarm_figures.py`.
2. **High-value residual gaps** after C1/C2: epidemiology person-time (ch17), selection bias / collider (ch18), confounding-by-indication ARR/NNT (ch05), survival absolute risk landmarks (ch20), bias taxonomy structures (ch04).
3. **Captions** emphasize ARR/NNT and prediction ≠ causation where relevant.
4. **Optional fix** — ch08 practice list double-numbering `1. 1.` → `1.` (surgical).
5. **Gates** — math, figure coverage, site tests, originality, `mkdocs build --strict` all green.
6. **Discipline** — no meta nav; no DOCX imports; indigo brand; no redo of cycle1/2 figure filenames.

## Figures generated (5)

| File | Chapter | Teaching point |
|------|---------|----------------|
| `cycle3_swarm_ch17_person_time.png` | 17 | Open-cohort person-time; incidence density arithmetic |
| `cycle3_swarm_ch18_selection_collider.png` | 18 | Day-30 survivor selection as collider conditioning |
| `cycle3_swarm_ch05_crude_vs_stratified.png` | 05 | Stratified ARR 5 pp (NNT 20) vs crude ARR 13.75 pp (NNT ≈7) |
| `cycle3_swarm_ch20_km_absolute_arr.png` | 20 | Vertical ARR gap on KM at day 365; HR is not absolute |
| `cycle3_swarm_ch04_selection_vs_confounding.png` | 04 | Confounding fork vs selection collider side-by-side |

## Chapters touched

- `docs/curriculum/17-chapter-17-disease-frequency-association.md` (+1 embed)
- `docs/curriculum/18-causation-frameworks-bias-and-inference.md` (+1)
- `docs/curriculum/05-confounding-dags-and-target-trial-thinking.md` (+1)
- `docs/curriculum/20-regression-and-survival-analysis-literacy-for-paper-readers.md` (+1)
- `docs/curriculum/04-internal-validity-external-validity-and-bias-taxonomy.md` (+1)
- `docs/curriculum/08-diagnostic-accuracy-studies-from-sensitivity-to-decisions.md` (exercise numbering only)

## Verification

| Check | Result |
|-------|--------|
| `verify_math_examples.py` | ALL_PASS |
| `check_figure_coverage.py` | OK 28 BAD 0 |
| `test_ebook_site.py` | 10/10 OK |
| `originality_scan.py` | OK |
| `mkdocs build --strict` | exit 0 |
| Broken image paths | 0 / 189 |

## Counts

- **Figures added this cycle:** 5 PNGs + generator script
- **Chapters densified:** 5 (17, 18, 05, 20, 04)
- **REQUIRED residuals:** empty

## Residual files

- `C:\Users\rkala\AppData\Local\Temp\grok-goal-fa96971be2ac\implementer\cycle3-crit-residuals.md`
- `C:\Users\rkala\CRIT-APP\_meta\swarm3h_cycle3_crit.md` (this file)

## Optional only (non-blocking)

- Boilerplate “Advanced Application” tails on several mid/late chapters
- ch17 still thinner on original prose words than early book
- Same exercise double-numbering pattern still present in ch06/07/10 (not requested this cycle)
