# Swarm 3h Cycle-2 — CRIT-APP

**When:** 2026-07-15  
**Repo:** `C:\Users\rkala\CRIT-APP` (`rkalani1/CRIT-APP`)  
**Product posture:** open-source ebook only (no meta nav pages)

## Goals addressed

1. **≥4 NEW original code-drawn matplotlib figures** — delivered **7** via `scripts/generate_cycle2_midlate_figures.py` under `docs/assets/figures/`.
2. **Scientific teaching diagrams** densifying mid/late chapters **17, 18, 19, 20, 22, 24, 27** (frequency / causation / inference / regression / screening / therapy / fragility).
3. **Embeds** — real on-disk PNGs only (`../assets/figures/cycle2_*.png`); 0 broken image paths.
4. **Math** — `scripts/verify_math_examples.py` ALL_PASS.
5. **Gates** — figure coverage, site tests, originality scan, `mkdocs build --strict` all green.
6. **Discipline** — no meta nav reintroduction; no DOCX image imports.

## Figures generated (7)

| File | Chapter | Teaching point |
|------|---------|----------------|
| `cycle2_ch17_rate_vs_risk.png` | 17 | Same incidence rate → different cumulative risks by window; rate≠risk |
| `cycle2_ch18_evalue_tipping.png` | 18 | E-value curve: residual confounding strength to nullify RR |
| `cycle2_ch19_ci_compatibility.png` | 19 | Four CIs vs null + MCID (estimation culture, not dichotomania) |
| `cycle2_ch20_ph_violation.png` | 20 | Crossing survival curves; single HR uninterpretable under PH violation |
| `cycle2_ch22_lead_time_bias.png` | 22 | Lead-time bias: longer Dx-to-death clock, same death date |
| `cycle2_ch24_benefit_harm_tradeoff.png` | 24 | Fixed RRR + fixed ARI → net tradeoff flips with baseline risk |
| `cycle2_ch27_fragility_ltfu.png` | 27 | Fragility index vs LTFU; LTFU≥FI ⇒ assumption-bound significance |

## Chapters touched

- `docs/curriculum/17-chapter-17-disease-frequency-association.md` (+1 embed)
- `docs/curriculum/18-causation-frameworks-bias-and-inference.md` (+1)
- `docs/curriculum/19-inference-estimation-and-the-architecture-of-uncertainty.md` (+1)
- `docs/curriculum/20-regression-and-survival-analysis-literacy-for-paper-readers.md` (+1)
- `docs/curriculum/22-screening-early-detection-and-overdiagnosis.md` (+1)
- `docs/curriculum/24-appraising-therapy-and-harm-questions.md` (+1)
- `docs/curriculum/27-missing-data-multiplicity-interim-analyses-and-fragility.md` (+1)

## Verification

| Check | Result |
|-------|--------|
| `verify_math_examples.py` | ALL_PASS |
| `check_figure_coverage.py` | OK 28 BAD 0 |
| `test_ebook_site.py` | 10/10 OK |
| `originality_scan.py` | OK |
| `mkdocs build --strict` | exit 0 |
| Broken image paths | 0 |

## Counts

- **Figures added this cycle:** 7 PNGs + generator script
- **Chapters densified:** 7 (17, 18, 19, 20, 22, 24, 27)
- **REQUIRED residuals:** empty

## Residual files

- `C:\Users\rkala\AppData\Local\Temp\grok-goal-e534d4870158\implementer\cycle2-crit-residuals.md`
- `C:\Users\rkala\CRIT-APP\_meta\swarm3h_cycle2_crit.md` (this file)
