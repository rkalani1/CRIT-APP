# Swarm 3h Cycle-1 — CRIT-APP

**When:** 2026-07-15  
**Repo:** `C:\Users\rkala\CRIT-APP` (`rkalani1/CRIT-APP`)  
**Product posture:** open-source ebook only (no meta nav pages)

## Goals addressed

1. **≥5 NEW original code-drawn matplotlib figures** — delivered **7** via `scripts/generate_cycle1_dense_figures.py` under `docs/assets/figures/`.
2. **Scientific teaching diagrams** (not decorative cards) densifying thinner chapters **11, 13, 14, 15, 16**.
3. **Math** — `scripts/verify_math_examples.py` ALL_PASS (no FAIL to fix).
4. **Gates** — figure coverage, site tests, originality scan, `mkdocs build --strict` all green.
5. **Discipline** — no meta nav reintroduction; no DOCX image imports.

## Figures generated (7)

| File | Chapter | Teaching point |
|------|---------|----------------|
| `cycle1_ch11_dichotomy_loss.png` | 11 | Dichotomized mRS hides 4→3 ordinal shifts |
| `cycle1_ch11_km_vs_cif.png` | 11 | Naive KM overestimates vs competing-risk CIF |
| `cycle1_ch13_abs_vs_rel_hte.png` | 13 | Constant RR → baseline-driven absolute HTE |
| `cycle1_ch13_stratum_pvalue_fallacy.png` | 13 | Same RR, power-driven stratum p-values |
| `cycle1_ch14_prevalence_ppv.png` | 14 | Prevalence shift collapses PPV at fixed Se/Sp |
| `cycle1_ch15_jc_agenda.png` | 15 | 45–60 min timeboxed JC agenda |
| `cycle1_ch16_decision_matrix.png` | 16 | Act / Conditional / Watch / No change matrix |

## Chapters touched

- `docs/curriculum/11-stroke-outcomes-mrs-time-to-event-and-competing-risks.md` (+2 embeds)
- `docs/curriculum/13-subgroups-heterogeneity-of-treatment-effect-and-spin.md` (+2 embeds)
- `docs/curriculum/14-appraising-artificial-intelligence-and-machine-learning-papers.md` (+1)
- `docs/curriculum/15-journal-club-architecture-and-teaching-critical-appraisal.md` (+1)
- `docs/curriculum/16-paper-autopsies-integrated-worked-critiques.md` (+1)

## Verification

| Check | Result |
|-------|--------|
| `verify_math_examples.py` | ALL_PASS |
| `check_figure_coverage.py` | OK 28 BAD 0 |
| `test_ebook_site.py` | 10/10 OK |
| `originality_scan.py` | OK |
| `mkdocs build --strict` | exit 0 |

## Counts

- **Figures added this cycle:** 7 PNGs + generator script
- **Chapters densified:** 5 (11, 13, 14, 15, 16)
- **REQUIRED residuals:** empty (optional backlog in residuals file)

## Residual files

- `C:\Users\rkala\AppData\Local\Temp\grok-goal-e534d4870158\implementer\cycle1-crit-residuals.md`
- `C:\Users\rkala\CRIT-APP\_meta\swarm3h_cycle1_crit.md` (this file)
