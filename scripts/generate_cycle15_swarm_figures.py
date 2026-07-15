#!/usr/bin/env python3
"""CRIT-APP Cycle-15 densify: residual floor-9 chapters → 10 (wave A).

ch02 20-min absolute ledger order
ch03 estimand population absolute board
ch05 backdoor open/closed absolute residual
ch07 case-control OR ≠ absolute risk / NNT
ch09 calibration absolute risk bands (pred≠cause)
ch10 forest absolute RD vs relative RR
ch14 AUROC ≠ absolute net clinical benefit

Agg indigo. cycle15_swarm_* only.
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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


def fig_ch02():
    """20-minute protocol: absolute ledger order (ARR/NNT before RRR)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title(
        "20-minute absolute ledger order (synthetic teaching)",
        fontsize=11, fontweight="bold", color=INDIGO,
    )
    steps = [
        (6.6, TEAL, "1  Extract CER / EER at fixed horizon"),
        (5.1, INDIGO, "2  Compute ARR = CER − EER (pp)"),
        (3.6, GOLD, "3  NNT = 1/ARR · state horizon & analysis set"),
        (2.1, ORANGE, "4  Only then read RRR (optional marketing layer)"),
        (0.6, CORAL, "STOP if primary is RRR-only or denominator missing"),
    ]
    for y, e, t in steps:
        ax.add_patch(
            FancyBboxPatch(
                (0.4, y - 0.55), 9.2, 1.25,
                boxstyle="round,pad=0.03,rounding_size=0.07",
                facecolor=WHITE, edgecolor=e, lw=1.5,
            )
        )
        ax.text(0.75, y + 0.08, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch02_abs_ledger_order.png")


def fig_ch03():
    """Estimand board: population vs sample absolute ARR mismatch."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    labs = ["Target\npopulation", "Enrolled\nsample", "Analytic\nset"]
    arr = [4.5, 6.2, 7.8]
    cols = [TEAL, GOLD, CORAL]
    bars = ax.bar(range(3), arr, color=cols, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("ARR (pp) at 90 d")
    ax.set_title("Same intervention, three absolute estimands", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 10)
    for b, v in zip(bars, arr):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.25, f"{v:.1f}", ha="center", fontsize=9, color=SLATE)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Write the estimand before the NNT", fontsize=10, fontweight="bold", color=INDIGO)
    items = [
        (6.2, "Population: who is eligible at t0?"),
        (4.5, "Treatment strategies: policy vs hypothetical"),
        (2.8, "Endpoint + horizon: disablement @ 90 d"),
        (1.1, "Summary: ARR / RD — not OR alone"),
    ]
    for y, t in items:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.55), 9.4, 1.2,
                boxstyle="round,pad=0.03,rounding_size=0.07",
                facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.2,
            )
        )
        ax.text(0.6, y + 0.05, t, fontsize=9.5, color=INDIGO, va="center", fontweight="bold")
    fig.suptitle(
        "Estimand board: absolute ARR is not transportable without population clarity",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch03_estimand_abs_board.png")


def fig_ch05():
    """Open vs closed backdoor: absolute residual confounding."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # crude vs adjusted ARR
    labels = ["Crude\n(open backdoor)", "Adjusted\n(closed backdoor)"]
    vals = [12.0, 3.5]
    cols = [CORAL, TEAL]
    ax.bar(range(2), vals, color=cols, edgecolor=INDIGO, width=0.55)
    ax.set_xticks(range(2))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Apparent ARR (pp)")
    ax.set_title("Severity confounds indication", fontsize=10, fontweight="bold", color=INDIGO)
    ax.axhline(3.5, color=TEAL, ls="--", lw=1, alpha=0.6)
    ax.text(0.5, 12.4, "invented 8.5 pp", ha="center", color=CORAL, fontsize=9, fontweight="bold")
    ax.set_ylim(0, 15)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Structural residual ledger", fontsize=10, fontweight="bold", color=INDIGO)
    # mini DAG labels
    nodes = [(2, 6, "Severity"), (5, 3.5, "Treatment"), (8, 6, "Outcome")]
    for x, y, lab in nodes:
        ax.add_patch(
            FancyBboxPatch(
                (x - 1.1, y - 0.55), 2.2, 1.1,
                boxstyle="round,pad=0.03,rounding_size=0.08",
                facecolor=WHITE, edgecolor=INDIGO, lw=1.4,
            )
        )
        ax.text(x, y, lab, ha="center", va="center", fontsize=9, fontweight="bold", color=INDIGO)
    ax.annotate("", xy=(4.0, 3.9), xytext=(2.5, 5.5),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax.annotate("", xy=(7.0, 5.6), xytext=(2.9, 6.2),
                arrowprops=dict(arrowstyle="->", color=CORAL, lw=2))
    ax.annotate("", xy=(7.0, 3.9), xytext=(6.0, 3.5),
                arrowprops=dict(arrowstyle="->", color=TEAL, lw=2))
    ax.text(5, 1.2, "Close severity→treatment & severity→outcome\nbefore trusting absolute ARR / NNT",
            ha="center", fontsize=9.5, color=SLATE, fontweight="bold")
    fig.suptitle(
        "Open backdoor invents absolute benefit; closed path restores residual ARR (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch05_backdoor_residual.png")


def fig_ch07():
    """Case-control OR cannot mint NNT without external absolute risk."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # 2x2 teaching counts (case-control sampling)
    table = np.array([[80, 40], [120, 160]])  # exposed cases/controls; unexp cases/controls style
    # Better as odds visualization
    cats = ["Cases\nexposed", "Cases\nunexp", "Controls\nexposed", "Controls\nunexp"]
    counts = [80, 40, 120, 160]
    cols = [CORAL, GOLD, BLUE, GRAY]
    ax.bar(range(4), counts, color=cols, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(range(4))
    ax.set_xticklabels(cats, fontsize=8.5)
    ax.set_ylabel("Sample counts (design-sampled)")
    ax.set_title("Case-control sampling ≠ cohort risks", fontsize=10, fontweight="bold", color=INDIGO)
    ax.text(1.5, max(counts) * 0.92, "OR ≈ 2.67", ha="center", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Absolute path to NNT", fontsize=10, fontweight="bold", color=INDIGO)
    boxes = [
        (6.0, CORAL, "OR alone: direction / association"),
        (3.8, GOLD, "Need baseline risk (external CER)"),
        (1.6, TEAL, "Then ARR ≈ CER − CER·OR/(1−CER+CER·OR)\n→ NNT only after absolute conversion"),
    ]
    for y, e, t in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.85), 9.4, 1.7,
                boxstyle="round,pad=0.03,rounding_size=0.08",
                facecolor=WHITE, edgecolor=e, lw=1.5,
            )
        )
        ax.text(5, y, t, ha="center", va="center", fontsize=9.2, fontweight="bold", color=e)
    fig.suptitle(
        "Observational case-control: refuse pathway NNT without absolute baseline risk (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch07_or_not_nnt.png")


def fig_ch09():
    """Calibration bands: predicted risk vs observed — pred≠cause."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    pred = np.array([5, 15, 25, 40, 60])
    obs_good = np.array([6, 14, 26, 38, 58])
    obs_bad = np.array([12, 28, 45, 55, 62])
    ax.plot([0, 70], [0, 70], "--", color=GRAY, lw=1.5, label="Perfect calib.")
    ax.plot(pred, obs_good, "o-", color=TEAL, lw=2.2, ms=8, label="Well-calibrated")
    ax.plot(pred, obs_bad, "s-", color=CORAL, lw=2.2, ms=8, label="Miscalibrated")
    ax.set_xlabel("Predicted risk (%)")
    ax.set_ylabel("Observed event rate (%)")
    ax.set_title("Absolute calibration is the decision metric", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left")
    ax.set_xlim(0, 70)
    ax.set_ylim(0, 70)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Pred ≠ cause (absolute fork)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(
        FancyBboxPatch((0.4, 4.5), 9.2, 2.8, boxstyle="round,pad=0.04,rounding_size=0.08",
                       facecolor="#E8F5E9", edgecolor=TEAL, lw=1.4)
    )
    ax.text(5, 5.9, "OK: counsel absolute predicted risk\n(with calibration & horizon)",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=TEAL)
    ax.add_patch(
        FancyBboxPatch((0.4, 0.6), 9.2, 2.8, boxstyle="round,pad=0.04,rounding_size=0.08",
                       facecolor="#FFEBEE", edgecolor=CORAL, lw=1.4)
    )
    ax.text(5, 2.0, "NOT OK: treat because score high\nwithout causal ARR / TTE / RCT",
            ha="center", va="center", fontsize=9.5, fontweight="bold", color=CORAL)
    fig.suptitle(
        "Risk scores: absolute calibration for counseling; causation needs a separate design (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch09_calib_abs_bands.png")


def fig_ch10():
    """Forest: absolute RD can reverse ranking vs relative RR."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    studies = ["A high-risk", "B mid-risk", "C low-risk", "Pooled"]
    # relative RRs similar
    rr = np.array([0.75, 0.78, 0.72, 0.76])
    # absolute RDs differ by baseline
    rd = np.array([8.0, 4.0, 1.2, 3.5])  # pp benefit

    ax = axes[0]
    y = np.arange(len(studies))[::-1]
    ax.axvline(1.0, color=GRAY, lw=1.2)
    for i, (yi, r) in enumerate(zip(y, rr)):
        lo, hi = r - 0.12, r + 0.10
        col = TEAL if i < 3 else INDIGO
        ax.plot([lo, hi], [yi, yi], color=col, lw=3.5, solid_capstyle="round")
        ax.plot(r, yi, "o", color=col, ms=9)
    ax.set_yticks(y)
    ax.set_yticklabels(studies, fontsize=9)
    ax.set_xlabel("RR (relative)")
    ax.set_xlim(0.5, 1.3)
    ax.set_title("Relative forest: similar RRs", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3)

    ax = axes[1]
    y = np.arange(len(studies))[::-1]
    ax.axvline(0, color=GRAY, lw=1.2)
    for i, (yi, d) in enumerate(zip(y, rd)):
        lo, hi = d - 1.5, d + 1.5
        col = TEAL if i < 3 else INDIGO
        ax.plot([lo, hi], [yi, yi], color=col, lw=3.5, solid_capstyle="round")
        ax.plot(d, yi, "s", color=col, ms=9)
    ax.set_yticks(y)
    ax.set_yticklabels(studies, fontsize=9)
    ax.set_xlabel("ARR (pp absolute benefit)")
    ax.set_xlim(-2, 12)
    ax.set_title("Absolute forest: risk-dependent ARR", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3)
    fig.suptitle(
        "Meta-analysis: pool and report absolute RD/NNT, not RR alone (synthetic)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch10_forest_abs_rd.png")


def fig_ch14():
    """AUROC vs absolute net clinical benefit at operating point."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    fpr = np.linspace(0, 1, 100)
    tpr_a = fpr ** 0.35  # AUROC-ish high
    tpr_b = fpr ** 0.55
    ax.plot(fpr, tpr_a, color=INDIGO, lw=2.4, label="Model A AUROC≈0.88")
    ax.plot(fpr, tpr_b, color=GOLD, lw=2.4, label="Model B AUROC≈0.80")
    ax.plot([0, 1], [0, 1], "--", color=GRAY, lw=1)
    ax.set_xlabel("1 − Specificity")
    ax.set_ylabel("Sensitivity")
    ax.set_title("Discrimination ranking", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    # decision thresholds vs net benefit (synthetic)
    thresh = np.array([0.05, 0.10, 0.15, 0.20, 0.30, 0.40])
    nb_a = np.array([0.08, 0.11, 0.10, 0.07, 0.03, 0.01])
    nb_b = np.array([0.06, 0.12, 0.13, 0.11, 0.06, 0.02])  # B wins on absolute NB mid-range
    treat_all = np.maximum(0.18 - thresh * 0.9, 0)
    ax.plot(thresh * 100, nb_a, "o-", color=INDIGO, lw=2.2, label="A net benefit")
    ax.plot(thresh * 100, nb_b, "s-", color=GOLD, lw=2.2, label="B net benefit")
    ax.plot(thresh * 100, treat_all, "--", color=GRAY, lw=1.5, label="Treat-all")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlabel("Threshold probability (%)")
    ax.set_ylabel("Absolute net benefit")
    ax.set_title("Utility can reverse AUROC rank", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.suptitle(
        "AI/ML appraisal: AUROC ≠ absolute decision value (synthetic decision-curve spirit)",
        fontsize=11, fontweight="bold", color=INDIGO, y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle15_swarm_ch14_auroc_vs_nb.png")


def main():
    print("Cycle-15 →", OUT)
    for fn in [fig_ch02, fig_ch03, fig_ch05, fig_ch07, fig_ch09, fig_ch10, fig_ch14]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
