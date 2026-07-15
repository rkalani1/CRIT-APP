#!/usr/bin/env python3
"""CRIT-APP Cycle-16 densify: clear residual floor-9 → uniform floor ≥10.

ch16 autopsy absolute residual checklist
ch21 additive vs multiplicative interaction (absolute)
ch22 overdiagnosis absolute excess prevalence
ch23 base-rate neglect absolute post-test
ch24 benefit NNT vs harm NNH absolute ledger
ch25 diagnosis vs prognosis absolute horizons
ch26 CPR impact absolute outcomes residual

Agg indigo. cycle16_swarm_* only.
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"


def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Paper autopsy: absolute residual checklist", fontsize=11, fontweight="bold", color=INDIGO)
    items = [
        (8.4, CORAL, "1  Question: prediction vs causal ARR?"),
        (6.7, ORANGE, "2  t0 / eligibility / analysis set aligned?"),
        (5.0, GOLD, "3  CER & EER disclosed at fixed horizon?"),
        (3.3, PURPLE, "4  Confounding residual that could invent ARR?"),
        (1.6, TEAL, "5  Action only if NNT/NNH + transport OK"),
    ]
    for y, e, t in items:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y - 0.6), 9.3, 1.35,
                boxstyle="round,pad=0.03,rounding_size=0.07",
                facecolor=WHITE, edgecolor=e, lw=1.5,
            )
        )
        ax.text(0.7, y + 0.08, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch16_autopsy_abs.png")


def fig_ch21():
    """Additive interaction on absolute risk difference scale."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # risks: noA noB, A, B, A+B
    labs = ["Neither", "Factor A", "Factor B", "A + B"]
    risk = [4, 8, 10, 22]  # super-additive absolute
    expected_add = 4 + (8 - 4) + (10 - 4)  # 14
    cols = [GRAY, BLUE, GOLD, CORAL]
    ax.bar(range(4), risk, color=cols, edgecolor=INDIGO, width=0.62)
    ax.axhline(expected_add, color=TEAL, ls="--", lw=1.6, label=f"Additive expect {expected_add}%")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute risk (%)")
    ax.set_title("Absolute risks under joint exposure", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.set_ylim(0, 28)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    measures = ["RERI\n(additive)", "Multiplicative\nRR ratio", "ARR in\nhigh-risk joint"]
    vals = [8, 1.1, 18]  # teaching scales
    # normalize display: show qualitative
    display = [8, 2, 18]
    ax.bar(range(3), display, color=[TEAL, GOLD, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(measures, fontsize=9)
    ax.set_ylabel("Teaching scale (absolute-first)")
    ax.set_title("Interaction: additive scale for decisions", fontsize=10, fontweight="bold", color=INDIGO)
    ax.text(0, 8.5, "+8 pp RERI", ha="center", fontsize=8, color=TEAL, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Effect modification: absolute additive interaction can exist when RRs look null (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch21_additive_interaction.png")


def fig_ch22():
    """Overdiagnosis: absolute excess prevalence from screening."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    years = np.array([0, 1, 2, 3, 4, 5])
    # screened invents early cases; mortality flat
    incidence_scr = np.array([2, 8, 7, 5, 4, 3.5])
    incidence_ctrl = np.array([2, 2.2, 2.4, 2.5, 2.6, 2.7])
    mort_scr = np.array([1.0, 1.0, 0.95, 0.95, 0.9, 0.9])
    mort_ctrl = np.array([1.0, 1.0, 1.0, 0.95, 0.95, 0.9])
    ax.plot(years, incidence_scr, "o-", color=CORAL, lw=2.2, label="Incidence screened")
    ax.plot(years, incidence_ctrl, "s-", color=GRAY, lw=2.2, label="Incidence control")
    ax.plot(years, mort_scr, "^-", color=TEAL, lw=2.0, label="Mortality screened")
    ax.plot(years, mort_ctrl, "v--", color=INDIGO, lw=1.8, label="Mortality control")
    ax.set_xlabel("Years from screen start")
    ax.set_ylabel("Events / 1000 py (teaching)")
    ax.set_title("Incidence spike without mortality win", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    cats = ["True\nbenefit", "Overdiag.\nexcess", "False\npositives"]
    vals = [1.5, 12.0, 40.0]
    ax.bar(range(3), vals, color=[TEAL, CORAL, GOLD], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylabel("Absolute counts / 1000 screened")
    ax.set_title("Absolute screening ledger", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Screening appraisal: demand absolute mortality benefit vs overdiagnosis excess (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch22_overdiag_abs.png")


def fig_ch23():
    """Base-rate neglect: absolute natural frequencies."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # 1000 people, prev 1%, Se 90%, Sp 90%
    # TP=9, FN=1, FP=99, TN=891
    sizes = [9, 99, 1, 891]
    labels = ["TP 9", "FP 99", "FN 1", "TN 891"]
    colors = [TEAL, CORAL, GOLD, GRAY]
    ax.pie(sizes, labels=labels, colors=colors, startangle=90,
           textprops={"fontsize": 9, "fontweight": "bold"})
    ax.set_title("Natural frequencies @ 1% prevalence", fontsize=10, fontweight="bold", color=INDIGO)

    ax = axes[1]
    ax.bar([0, 1], [90, 8.3], color=[GOLD, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Intuitive PPV\n(neglect base rate)", "True PPV\n=9/(9+99)"], fontsize=9)
    ax.set_ylabel("Perceived / true PPV (%)")
    ax.set_title("Base-rate neglect inflates absolute PPV", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 100)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Clinical reasoning: dual-process fails when absolute base rates vanish (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch23_baserate_abs.png")


def fig_ch24():
    """Benefit NNT vs harm NNH absolute ledger."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    labs = ["CER\n(event)", "EER\n(event)", "Control\nharm", "Tx\nharm"]
    vals = [12, 8, 1.0, 2.5]
    cols = [GRAY, TEAL, GRAY, CORAL]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute risk (%)")
    ax.set_title("Efficacy and harm absolute risks", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    # ARR=4pp NNT=25; ARI=1.5pp NNH≈67
    metrics = ["ARR\n(pp)", "NNT", "ARI\n(pp)", "NNH"]
    mvals = [4.0, 25, 1.5, 67]
    # scale for dual axis feel - two groups
    ax.bar([0, 2], [4.0, 1.5], color=[TEAL, CORAL], edgecolor=INDIGO, width=0.55, label="pp")
    ax2 = ax.twinx()
    ax2.bar([1, 3], [25, 67], color=[INDIGO, ORANGE], edgecolor=INDIGO, width=0.55, alpha=0.85)
    ax.set_xticks([0, 1, 2, 3])
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylabel("Absolute Δ (pp)", color=SLATE)
    ax2.set_ylabel("NNT / NNH", color=SLATE)
    ax.set_title("Paired absolute benefit–harm ledger", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 8)
    ax2.set_ylim(0, 90)
    fig.suptitle(
        "Therapy & harm: always pair NNT with NNH on the same absolute horizon (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch24_nnt_nnh_ledger.png")


def fig_ch25():
    """Diagnosis vs prognosis absolute horizons."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Two absolute questions", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(
        FancyBboxPatch((0.3, 4.2), 9.4, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                       facecolor="#E3F2FD", edgecolor=BLUE, lw=1.5)
    )
    ax.text(5, 5.7, "DIAGNOSIS\nDoes disease exist now?\nAbsolute: post-test probability / PPV",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=BLUE)
    ax.add_patch(
        FancyBboxPatch((0.3, 0.5), 9.4, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                       facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5)
    )
    ax.text(5, 2.0, "PROGNOSIS\nWhat happens over a horizon?\nAbsolute: risk @ t (calibrated)",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=TEAL)

    ax = axes[1]
    horizons = ["Now\n(dx)", "7 d", "30 d", "90 d", "1 y"]
    # different absolute risks for same patient label "high risk"
    risks = [35, 8, 15, 28, 40]  # dx PPV vs future event risks
    cols = [BLUE, TEAL, TEAL, TEAL, TEAL]
    ax.bar(range(5), risks, color=cols, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(range(5))
    ax.set_xticklabels(horizons, fontsize=9)
    ax.set_ylabel("Absolute probability (%)")
    ax.set_title("'High risk' is horizon-bound", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Diagnosis ≠ prognosis: never mix post-test disease probability with future ARR (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch25_dx_px_horizons.png")


def fig_ch26():
    """CPR impact: classification gain vs absolute outcome change."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    labs = ["Reclass.\nup", "Reclass.\ndown", "Net correct\nreclass."]
    vals = [18, 12, 6]
    ax.bar(range(3), vals, color=[GOLD, BLUE, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("% of cohort")
    ax.set_title("Discrimination / reclassification", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    labs2 = ["Events\nprevented", "Events\ncaused", "Net absolute\noutcome Δ"]
    vals2 = [2.0, 0.8, 1.2]
    ax.bar(range(3), vals2, color=[TEAL, CORAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs2, fontsize=9)
    ax.set_ylabel("Absolute events / 100 patients")
    ax.set_title("Impact study: hard absolute outcomes", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "CPR appraisal: reclassification ≠ impact—demand absolute outcome change (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle16_swarm_ch26_cpr_impact_abs.png")


def main():
    print("Cycle-16 →", OUT)
    for fn in [fig_ch16, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
