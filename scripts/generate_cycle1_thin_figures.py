#!/usr/bin/env python3
"""
CRIT-APP cycle-1 densify (thin late/mid chapters): original matplotlib figures.

Targets thinner chapters: ch23 dual-process, ch26 SR/CPRs, ch28 systems,
plus mid-book ch20 survival literacy. Code-drawn only (Agg).
Writes PNGs under docs/assets/figures/. Safe to re-run (overwrites cycle1_ch*
thin outputs only when names match).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INDIGO = "#283593"
TEAL = "#00695C"
GOLD = "#F9A825"
CORAL = "#C62828"
SLATE = "#37474F"
LIGHT = "#ECEFF1"
WHITE = "#FFFFFF"
GREEN = "#2E7D32"
BLUE = "#1565C0"
ORANGE = "#EF6C00"


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch23_urgency_uncertainty() -> Path:
    """Dual-process switch: urgency × uncertainty → System 1 vs System 2 (ch23)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # Left: 2×2 allocation grid
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(
        "When to force System 2 while reading evidence",
        fontsize=10,
        fontweight="bold",
        color=INDIGO,
    )

    cells = [
        # x, y, w, h, title, body, face, edge
        (0.5, 5.2, 4.3, 4.0, "High urgency\nLow uncertainty",
         "System 1 OK\nClassic LVO phenotype\n+ known pathway",
         "#E8F5E9", GREEN),
        (5.2, 5.2, 4.3, 4.0, "High urgency\nHigh uncertainty",
         "Micro-System 2\n60s timeout +\nabsolute risk gate",
         "#FFF3E0", ORANGE),
        (0.5, 0.6, 4.3, 4.0, "Low urgency\nLow uncertainty",
         "System 1 OK\nRoutine secondary\nprevention defaults",
         "#E0F2F1", TEAL),
        (5.2, 0.6, 4.3, 4.0, "Low urgency\nHigh uncertainty",
         "Full System 2\nARR/NNT, bias map,\npre-mortem",
         "#FFEBEE", CORAL),
    ]
    for x, y, w, h, title, body, face, edge in cells:
        ax.add_patch(
            FancyBboxPatch(
                (x, y), w, h,
                boxstyle="round,pad=0.06,rounding_size=0.12",
                facecolor=face, edgecolor=edge, lw=1.8,
            )
        )
        ax.text(x + w / 2, y + h - 0.85, title, ha="center", va="top",
                fontsize=8, fontweight="bold", color=edge)
        ax.text(x + w / 2, y + 1.35, body, ha="center", va="center",
                fontsize=7.5, color=SLATE)

    # Right: synthetic error rates when System 2 is skipped
    ax = axes[1]
    scenarios = [
        "Classic code\n(low unc.)",
        "Mimic-rich\n(high unc.)",
        "Abstract RRR\nspin skim",
        "Pathway change\nfrom 1 trial",
    ]
    # synthetic % of inappropriate decisions
    sys1_only = np.array([4, 28, 35, 42])
    with_s2 = np.array([5, 9, 11, 12])
    x = np.arange(len(scenarios))
    w = 0.36
    ax.bar(x - w / 2, sys1_only, width=w, color=CORAL, edgecolor=INDIGO,
           label="System 1 only")
    ax.bar(x + w / 2, with_s2, width=w, color=TEAL, edgecolor=INDIGO,
           label="Forced System 2 gate")
    ax.set_xticks(x)
    ax.set_xticklabels(scenarios, fontsize=7.5)
    ax.set_ylabel("Inappropriate decisions (%)")
    ax.set_ylim(0, 55)
    ax.set_title(
        "Synthetic teaching: cost of skipping System 2",
        fontsize=10, fontweight="bold", color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(
        0.5, 0.97,
        "Biggest gains where uncertainty is high — not in pure pattern-match codes.",
        transform=ax.transAxes, ha="center", va="top", fontsize=7.5, color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )

    fig.suptitle(
        "Dual-process allocation for evidence use (synthetic teaching)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch23_urgency_uncertainty.png")


def fig_ch23_rrr_anchor() -> Path:
    """RRR abstract anchor vs forced ARR/NNT translation (ch23 cognitive bias)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    # Left: same data, two frames
    ax = axes[0]
    frames = ["Abstract frame\n(relative)", "Forced translation\n(absolute)"]
    # perceived benefit 0-100 scale (synthetic subjective weight)
    perceived = [78, 22]
    colors = [CORAL, TEAL]
    bars = ax.bar(frames, perceived, color=colors, edgecolor=INDIGO, width=0.55)
    ax.set_ylim(0, 100)
    ax.set_ylabel("Subjective 'large benefit' rating (0–100)")
    ax.set_title("Framing effect on the same trial", fontsize=10,
                 fontweight="bold", color=INDIGO)
    for b, v, lab in zip(bars, perceived, ["RRR 45%", "ARR 1.2% · NNT 83"]):
        ax.text(b.get_x() + b.get_width() / 2, v + 3, lab,
                ha="center", fontsize=8, color=SLATE, fontweight="bold")
    ax.axhline(50, ls=":", color=SLATE, lw=1)
    ax.text(1.45, 52, "decision threshold\n(illustrative)", fontsize=7, color=SLATE, ha="right")

    # Right: natural frequency box
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Same numbers, anti-anchor format", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.add_patch(
        FancyBboxPatch(
            (0.5, 1.2), 9.0, 7.5,
            boxstyle="round,pad=0.1,rounding_size=0.15",
            facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.6,
        )
    )
    text = (
        "Control events:  27 / 1000  (2.7%)\n"
        "Treated events:  15 / 1000  (1.5%)\n"
        "─────────────────────────\n"
        "ARR = 1.2 percentage points\n"
        "RRR = 1.2 / 2.7 ≈ 45%\n"
        "NNT ≈ 83 over trial horizon\n\n"
        "Anchor on RRR → overtreatment risk\n"
        "Anchor on ARR/NNT → calibrated decision"
    )
    ax.text(5.0, 5.2, text, ha="center", va="center", fontsize=9,
            color=SLATE, family="monospace")
    fig.suptitle(
        "Anchoring bias: relative risk in abstracts vs absolute translation (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch23_rrr_anchor.png")


def fig_ch26_epv_overfit() -> Path:
    """Events-per-variable vs apparent vs external performance (ch26 CPR)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    epv = np.array([3, 5, 8, 10, 15, 25, 40])
    # optimistic derivation c-stat falls toward truth as EPV rises
    c_deriv = 0.92 - 0.12 * (1 - np.exp(-8 / epv))
    c_ext = 0.72 + 0.06 * (1 - np.exp(-epv / 12))
    # calibration slope (1 = perfect)
    cal_slope = 1.0 - 0.55 * np.exp(-epv / 8)

    ax = axes[0]
    ax.plot(epv, c_deriv, "o-", color=CORAL, lw=2.2, markersize=7,
            label="Derivation c-statistic (optimistic)")
    ax.plot(epv, c_ext, "s-", color=TEAL, lw=2.2, markersize=7,
            label="External c-statistic")
    ax.fill_between(epv, c_ext, c_deriv, color=CORAL, alpha=0.12,
                     label="Optimism gap")
    ax.axvline(10, ls="--", color=SLATE, lw=1.1)
    ax.text(10.3, 0.905, "rule-of-thumb\n≥10 EPV", fontsize=7.5, color=SLATE)
    ax.set_xlabel("Events per candidate predictor (EPV)")
    ax.set_ylabel("Discrimination (c-statistic)")
    ax.set_xlim(2, 42)
    ax.set_ylim(0.65, 0.95)
    ax.set_title("Overfitting shrinks as EPV rises", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="lower right")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(epv, cal_slope, "D-", color=BLUE, lw=2.2, markersize=7)
    ax.axhline(1.0, color=GREEN, ls=":", lw=1.4, label="Perfect calibration slope = 1")
    ax.fill_between(epv, cal_slope, 1.0, where=cal_slope < 1, color=GOLD, alpha=0.2)
    ax.set_xlabel("Events per candidate predictor (EPV)")
    ax.set_ylabel("External calibration slope")
    ax.set_xlim(2, 42)
    ax.set_ylim(0.3, 1.15)
    ax.set_title("Low EPV → predicted risks too extreme", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
    ax.text(
        22, 0.42,
        "ICH/expansion scores with EPV≪10\noften look great at home,\nfail abroad.",
        fontsize=8, color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    fig.suptitle(
        "CPR derivation: events-per-variable and transportability (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch26_epv_overfit.png")


def fig_ch26_i2_pooling() -> Path:
    """Heterogeneous trials: pooling can invent a meaningless average (ch26 SR)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.3, 4.8))

    # Forest of 6 synthetic trials with opposing directions
    trials = [
        ("A (early window)", 0.55, 0.40, 0.75),
        ("B (early window)", 0.62, 0.48, 0.80),
        ("C (late window)", 1.35, 1.05, 1.75),
        ("D (late window)", 1.28, 0.95, 1.72),
        ("E (mixed dosing)", 0.90, 0.55, 1.45),
        ("F (mixed dosing)", 1.10, 0.70, 1.70),
    ]
    ax = axes[0]
    y = np.arange(len(trials))[::-1]
    for yi, (lab, pe, lo, hi) in zip(y, trials):
        color = TEAL if pe < 1 else CORAL
        ax.plot([lo, hi], [yi, yi], color=color, lw=2.2)
        ax.plot(pe, yi, "o", color=color, markersize=9)
        ax.text(0.28, yi, lab, ha="right", va="center", fontsize=8, color=SLATE)
    # pooled random-effects near null
    ax.plot([0.88, 1.12], [-0.9, -0.9], color=INDIGO, lw=3.0)
    ax.plot(0.99, -0.9, "D", color=INDIGO, markersize=10)
    ax.text(0.28, -0.9, "Pooled RE (I²≈78%)", ha="right", va="center",
            fontsize=8, fontweight="bold", color=INDIGO)
    ax.axvline(1.0, color=SLATE, ls="--", lw=1.1)
    ax.set_xscale("log")
    ax.set_xlim(0.3, 2.2)
    ax.set_yticks([])
    ax.set_xlabel("Risk ratio (log scale, synthetic)")
    ax.set_title("Six uncombinable trials → null average", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.set_ylim(-1.5, 5.6)
    ax.grid(True, axis="x", alpha=0.25)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Appraisal decision rule", fontsize=10,
                 fontweight="bold", color=INDIGO)
    rows = [
        (8.2, "Signal", "Action", True),
        (6.6, "I² high + opposing directions", "Do not pool; explain", False),
        (5.0, "Clinical windows differ", "Stratify or leave narrative", False),
        (3.4, "Tight CI around garbage mean", "Precision ≠ validity", False),
        (1.8, "Only early trials beneficial", "Report stratum effects", False),
    ]
    for i, (y0, a, b, header) in enumerate(rows):
        fc = "#E8EAF6" if header else WHITE
        for text, x0, width in [(a, 0.3, 5.2), (b, 5.6, 4.0)]:
            ax.add_patch(
                FancyBboxPatch(
                    (x0, y0 - 0.55), width, 1.2,
                    boxstyle="round,pad=0.02,rounding_size=0.06",
                    facecolor=fc if header else ("#FFEBEE" if i == 1 else WHITE),
                    edgecolor=INDIGO, lw=0.9,
                )
            )
            ax.text(
                x0 + width / 2, y0 + 0.05, text,
                ha="center", va="center",
                fontsize=7.5 if not header else 8.5,
                fontweight="bold" if header or i == 0 else "normal",
                color=INDIGO if header else SLATE,
            )
    ax.text(
        5.0, 0.35,
        "Random-effects does not license pooling apples with oranges.",
        ha="center", fontsize=8, color=CORAL,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    fig.suptitle(
        "Meta-analysis heterogeneity: when not to pool (synthetic forest)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch26_i2_pooling.png")


def fig_ch28_goodhart_dtn() -> Path:
    """Goodhart: door-to-needle improves while mimic treatment rises (ch28)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.3, 4.8))

    quarters = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    qlab = [f"Q{q}" for q in quarters]
    dtn = np.array([58, 52, 48, 44, 40, 37, 35, 33])  # median minutes
    mimic_tx = np.array([4, 5, 6, 8, 10, 13, 16, 18])  # % of thrombolysis to mimics
    sich = np.array([2.1, 2.2, 2.3, 2.5, 2.8, 3.1, 3.4, 3.7])  # % sICH

    ax = axes[0]
    ax.plot(quarters, dtn, "o-", color=TEAL, lw=2.4, markersize=8, label="Median door-to-needle (min)")
    ax.set_xlabel("Quarter after metric hard-targets")
    ax.set_ylabel("Median DTN (minutes)", color=TEAL)
    ax.tick_params(axis="y", labelcolor=TEAL)
    ax.set_xticks(quarters)
    ax.set_xticklabels(qlab)
    ax.set_ylim(25, 65)
    ax.set_title("Process metric 'wins'", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)

    ax2 = ax.twinx()
    ax2.plot(quarters, mimic_tx, "s--", color=CORAL, lw=2.2, markersize=7,
             label="Mimic treatment rate (%)")
    ax2.set_ylabel("Thrombolysis given to mimics (%)", color=CORAL)
    ax2.tick_params(axis="y", labelcolor=CORAL)
    ax2.set_ylim(0, 25)
    # combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="center right", fontsize=7.5)

    ax = axes[1]
    ax.bar(qlab, sich, color="#90A4AE", edgecolor=INDIGO, width=0.7)
    ax.plot(qlab, sich, "o-", color=CORAL, lw=1.8, markersize=6)
    ax.set_ylabel("sICH among treated (%)")
    ax.set_xlabel("Quarter")
    ax.set_ylim(0, 5)
    ax.set_title("Safety signal rides along", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(
        0.5, 0.95,
        "Green DTN dashboard ≠ better care.\nPair speed with appropriateness + harm audits.",
        transform=ax.transAxes, ha="center", va="top", fontsize=8, color=SLATE,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    fig.suptitle(
        "Goodhart's Law on the stroke clock (synthetic systems teaching)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch28_goodhart_dtn.png")


def fig_ch20_informative_censoring() -> Path:
    """Informative censoring biases KM survival estimates (mid-book ch20)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    t = np.array([0, 30, 90, 180, 365, 540, 730])
    # true survival (latent)
    true_s = np.array([1.00, 0.92, 0.84, 0.76, 0.68, 0.62, 0.58])
    # non-informative censoring: KM tracks truth closely
    km_ni = np.array([1.00, 0.92, 0.83, 0.75, 0.67, 0.61, 0.57])
    # informative: sicker patients drop out → optimistic KM
    km_inf = np.array([1.00, 0.93, 0.88, 0.84, 0.80, 0.77, 0.75])

    ax = axes[0]
    ax.plot(t, true_s * 100, "-", color=SLATE, lw=2.5, label="True survival (latent)")
    ax.plot(t, km_ni * 100, "o--", color=TEAL, lw=2.0, markersize=6,
            label="KM: non-informative censoring")
    ax.plot(t, km_inf * 100, "s-", color=CORAL, lw=2.0, markersize=6,
            label="KM: informative dropout (sicker leave)")
    ax.fill_between(t, true_s * 100, km_inf * 100, color=CORAL, alpha=0.12,
                     label="Optimism bias")
    ax.set_xlabel("Days since index stroke")
    ax.set_ylabel("Survival free of bad outcome (%)")
    ax.set_xlim(0, 750)
    ax.set_ylim(50, 105)
    ax.set_title("Informative censoring invents survivors", fontsize=10,
                 fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.2, loc="lower left")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Reader checklist (ch20)", fontsize=10,
                 fontweight="bold", color=INDIGO)
    items = [
        (8.0, "Who is censored, and why?", GREEN),
        (6.2, "Are dropouts sicker / different sites?", ORANGE),
        (4.4, "Is censoring balanced by arm?", TEAL),
        (2.6, "Sensitivity: worst-case for LTFU?", CORAL),
        (0.8, "Competing events handled correctly?", INDIGO),
    ]
    for y, text, edge in items:
        ax.add_patch(
            FancyBboxPatch(
                (0.5, y - 0.55), 9.0, 1.35,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=WHITE, edgecolor=edge, lw=1.5,
            )
        )
        ax.text(5.0, y + 0.1, text, ha="center", va="center",
                fontsize=9, color=SLATE, fontweight="bold")
    fig.suptitle(
        "Survival literacy: informative censoring bias (synthetic teaching)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch20_informative_censoring.png")


def main() -> None:
    gens = [
        fig_ch23_urgency_uncertainty,
        fig_ch23_rrr_anchor,
        fig_ch26_epv_overfit,
        fig_ch26_i2_pooling,
        fig_ch28_goodhart_dtn,
        fig_ch20_informative_censoring,
    ]
    print(f"Generating {len(gens)} cycle-1 thin-chapter figures → {OUT}")
    for g in gens:
        g()
    print("DONE")


if __name__ == "__main__":
    main()
