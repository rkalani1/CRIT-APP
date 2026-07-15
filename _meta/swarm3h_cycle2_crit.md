# Swarm Cycle-2 densify — CRIT-APP (open-source ebook)

**When:** 2026-07-15  
**Repo:** `C:\Users\rkala\CRIT-APP` (`rkalani1/CRIT-APP`)  
**Product posture:** open-source ebook only (no meta nav pages)

## Goals addressed

1. **≥5 NEW original code-drawn matplotlib figures** — delivered **6** via `scripts/generate_cycle2_swarm_figures.py`.
2. **Scientific teaching diagrams** densifying thinner mid/late chapters **17, 21, 24, 25, 27** (frequency/association, interaction, therapy/harm, diagnosis/prognosis, multiplicity/fragility plumbing).
3. **Embeds** — real on-disk PNGs only (`../assets/figures/cycle2_swarm_*.png`); 0 broken image paths.
4. **Math** — `scripts/verify_math_examples.py` ALL_PASS.
5. **Gates** — figure coverage, site tests, originality scan, `mkdocs build --strict` all green.
6. **Discipline** — no meta nav reintroduction; no DOCX image imports; indigo brand retained; did not redo cycle-1 figures.

## Figures generated (6)

| File | Chapter | Teaching point |
|------|---------|----------------|
| `cycle2_swarm_ch17_or_rr_divergence.png` | 17 | Fixed RR=2.0 → OR inflates as events become common; RD/RR/OR grammar |
| `cycle2_swarm_ch21_additive_net.png` | 21 | Multiplicative homogeneity (RR 0.67) vs additive ARR/net benefit across risk strata |
| `cycle2_swarm_ch24_composite_disagg.png` | 24 | Composite “significance” driven by soft components (revasc), not disabling stroke |
| `cycle2_swarm_ch25_ppv_prevalence.png` | 25 | PPV travels with prevalence; rebuild post-test from LRs + local pre-test |
| `cycle2_swarm_ch27_multiplicity_fwer.png` | 27 | Family-wise error vs unadjusted secondary tests; SAP/hierarchy defenses |
| `cycle2_swarm_ch27_early_stop_bias.png` | 27 | Early stop for benefit inflates ARR; replications regress to truth |

## Chapters touched

- `docs/curriculum/17-chapter-17-disease-frequency-association.md` (+1 embed)
- `docs/curriculum/21-interaction-effect-modification-and-standardization.md` (+1)
- `docs/curriculum/24-appraising-therapy-and-harm-questions.md` (+1)
- `docs/curriculum/25-appraising-diagnosis-and-prognosis-papers.md` (+1)
- `docs/curriculum/27-missing-data-multiplicity-interim-analyses-and-fragility.md` (+2)

## Verification

| Check | Result |
|-------|--------|
| `verify_math_examples.py` | ALL_PASS |
| `check_figure_coverage.py` | OK 28 BAD 0 |
| `test_ebook_site.py` | 10/10 OK |
| `originality_scan.py` | OK |
| `mkdocs build --strict` | exit 0 |
| Broken image paths | 0 / 184 |

## Counts

- **Figures added this cycle:** 6 PNGs + generator script
- **Chapters densified:** 5 (17, 21, 24, 25, 27)
- **REQUIRED residuals:** empty

## Residual files

- `C:\Users\rkala\AppData\Local\Temp\grok-goal-fa96971be2ac\implementer\cycle2-crit-residuals.md`
- `C:\Users\rkala\CRIT-APP\_meta\swarm3h_cycle2_crit.md` (this file)
