# Swarm Cycle-1 — CRIT-APP

**When:** 2026-07-14  
**Repo:** `C:\Users\rkala\CRIT-APP` (`rkalani1/CRIT-APP`)  
**Product posture:** open-source ebook only (no meta nav pages added)

## Goals addressed

1. **Visual coverage** — all 28 curriculum chapters have ≥1 original visual; each has a chapter-relevant figure after `## Opening`.
2. **Original figures** — code-drawn only via `scripts/generate_crit_swarm_figures.py` (matplotlib Agg).
3. **Broken paths** — zero missing image targets after embed.
4. **Math accuracy** — recomputed worked examples; fixed Ch12 OR 2.27→2.25.
5. **Ebook discipline** — no How-to-use / Originality / meta nav chrome in `mkdocs.yml`.

## Figures generated (21)

| File | Chapter use |
|------|-------------|
| `swarm_ch02_reading_triage.png` | 02 |
| `swarm_ch04_bias_taxonomy.png` | 04 |
| `swarm_ch07_immortal_time.png` | 07 |
| `swarm_ch09_calibration.png` | 09 |
| `swarm_ch10_forest.png` | 10 |
| `swarm_ch11_mrs_shift.png` | 11 |
| `swarm_ch14_ai_leakage.png` | 14 |
| `swarm_ch15_jc_roles.png` | 15 |
| `swarm_ch16_autopsy_flow.png` | 16 |
| `swarm_ch19_estimation_ci.png` | 19 |
| `swarm_ch20_survival.png` | 20 |
| `swarm_ch21_interaction.png` | 21 |
| `swarm_ch22_screening.png` | 22 |
| `swarm_ch23_dual_process.png` | 23 |
| `swarm_ch24_therapy_harm.png` | 24 |
| `swarm_ch25_diagnostic_2x2.png` | 25 |
| `swarm_ch26_cpr_lifecycle.png` | 26 |
| `swarm_ch27_fragility_missing.png` | 27 |
| `swarm_ch28_natural_frequencies.png` | 28 |
| `swarm_nnt_icon_array.png` | library (ARR 10% / NNT 10) |
| `crit_fig_bayes_lr.png` | regenerated (ch08) |

## Chapters fixed / enhanced (19 new opening embeds)

02, 04, 07, 09, 10, 11, 14, 15, 16, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28  

Already had chapter-specific openers (left in place): 01, 03, 05, 06, 08, 12, 13, 17, 18  

## Verification

| Check | Result |
|-------|--------|
| Figure coverage | OK 28 BAD 0 |
| `test_ebook_site.py` | 7/7 pass |
| `mkdocs build` | exit 0 |

## Counts

- **Figures added this cycle:** 21 PNGs generated (19 newly embedded as chapter openers; +2 library regenerations)
- **Chapters fixed:** 19 opening embeds + 1 math fix (ch12) + coverage verification on all 28
- **REQUIRED residuals:** empty

## Residual file

`C:\Users\rkala\AppData\Local\Temp\grok-goal-d7de3228caab\implementer\cycle1-crit-residuals.md`
