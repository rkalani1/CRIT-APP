#!/usr/bin/env python3
"""CRIT-APP Cycle-21 densify: raise uniform floor 11 → toward 12 (wave A).

ch01 misread cascade absolute cost residual
ch04 selection bias absolute distortion
ch06 co-intervention absolute contamination
ch08 threshold absolute tradeoff Se/Sp
ch11 mRS shift absolute utility residual
ch12 harm ARI absolute paired with ARR
ch15 spin detector absolute board

Agg indigo. cycle21_swarm_* only.
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


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 4.9))
    stages = ["Abstract\nRRR hype", "Pathway\nrewrite", "Low-risk\nover-tx", "Capacity\nlost"]
    cum = [10, 28, 45, 60]
    ax.plot(range(4), cum, "o-", color=CORAL, lw=2.5, ms=10)
    ax.fill_between(range(4), cum, color=CORAL, alpha=0.12)
    ax.set_xticks(range(4))
    ax.set_xticklabels(stages, fontsize=9)
    ax.set_ylabel("Cumulative absolute harm units")
    ax.set_title("Misread cascade: relative hype compounds absolute system cost", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch01_cascade_cost.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    labs = ["Target\npop risk", "Selected\nsample", "Analyzed\ncompleters"]
    arr_app = [4.0, 7.5, 11.0]
    ax.bar(range(3), arr_app, color=[TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Apparent ARR (pp)")
    ax.set_title("Selection bias inflates absolute effect along the pipeline", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch04_selection_abs.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    x = np.arange(3)
    pure = [5.0, 5.0, 5.0]
    contaminated = [5.0, 7.5, 9.0]
    w = 0.35
    ax.bar(x - w / 2, pure, width=w, color=TEAL, edgecolor=INDIGO, label="Protocol co-int equal")
    ax.bar(x + w / 2, contaminated, width=w, color=CORAL, edgecolor=INDIGO, label="Unblinded co-int favor tx")
    ax.set_xticks(x)
    ax.set_xticklabels(["Low intensity", "Moderate", "High differential"], fontsize=9)
    ax.set_ylabel("Observed ARR (pp)")
    ax.set_title("Co-intervention contamination invents absolute benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch06_coint_abs.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    thr = np.linspace(0.1, 0.9, 40)
    se = 1 - thr ** 1.2
    sp = thr ** 0.9
    ax.plot(thr, se, color=INDIGO, lw=2.3, label="Sensitivity")
    ax.plot(thr, sp, color=TEAL, lw=2.3, label="Specificity")
    ax.axvline(0.45, color=GOLD, ls="--", lw=1.5)
    ax.text(0.47, 0.2, "operating\npoint", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xlabel("Threshold (normalized)")
    ax.set_ylabel("Se / Sp")
    ax.set_title("Threshold absolute tradeoff: pick utility, not Youden alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch08_threshold_tradeoff.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    mrs = np.arange(0, 6)
    util = np.array([1.0, 0.91, 0.76, 0.65, 0.33, 0.0])
    ctrl = np.array([10, 15, 20, 25, 18, 12], dtype=float)
    trt = np.array([14, 18, 22, 22, 14, 10], dtype=float)
    ctrl /= ctrl.sum()
    trt /= trt.sum()
    eu_c = (ctrl * util).sum()
    eu_t = (trt * util).sum()
    w = 0.35
    ax.bar(mrs - w / 2, ctrl * 100, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(mrs + w / 2, trt * 100, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    ax.set_xlabel("mRS")
    ax.set_ylabel("% of arm")
    ax.set_title(f"Ordinal shift: ΔEU ≈ {eu_t - eu_c:.3f} absolute utility units", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch11_utility_shift.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    labs = ["ARR\nbenefit", "ARI\nharm", "Net\n(ARR−ARI)"]
    vals = [5.0, 1.5, 3.5]
    cols = [TEAL, CORAL, INDIGO]
    ax.bar(range(3), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute pp @ same horizon")
    ax.set_title("Effect sizes residual: always pair absolute benefit with absolute harm", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch12_arr_ari_pair.png")


def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("JC spin detector: absolute stops", fontsize=11, fontweight="bold", color=INDIGO)
    items = [
        (8.2, CORAL, "Primary endpoint switched vs registry"),
        (6.4, ORANGE, "Relative only in abstract conclusion"),
        (4.6, GOLD, "Subgroup rescue after null primary"),
        (2.8, PURPLE, "Composite driven by soft component"),
        (1.0, TEAL, "Action sentence forced despite stops"),
    ]
    for y, e, t in items:
        ax.add_patch(
            FancyBboxPatch((0.35, y - 0.6), 9.3, 1.35,
                           boxstyle="round,pad=0.03,rounding_size=0.07",
                           facecolor=WHITE, edgecolor=e, lw=1.5)
        )
        ax.text(0.7, y + 0.05, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle21_swarm_ch15_spin_detector.png")


def main():
    print("Cycle-21 →", OUT)
    for fn in [fig_ch01, fig_ch04, fig_ch06, fig_ch08, fig_ch11, fig_ch12, fig_ch15]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
