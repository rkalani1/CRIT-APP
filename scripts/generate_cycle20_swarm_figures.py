#!/usr/bin/env python3
"""CRIT-APP Cycle-20 densify: clear residual floor-10 → uniform floor ≥11.

ch22 lead-time absolute survival illusion residual
ch23 dual-process absolute threshold board
ch24 composite absolute component residual
ch25 LR absolute natural frequency residual
ch26 heterogeneity absolute prediction interval
ch27 fragility absolute FQ residual
ch28 shared decision absolute frequencies residual

Agg indigo. cycle20_swarm_* only.
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


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    # survival from diagnosis vs from randomization
    years = np.array([0, 1, 2, 3, 4, 5])
    surv_dx = np.array([100, 90, 80, 70, 60, 50])  # looks better
    surv_rand = np.array([100, 85, 70, 55, 45, 35])  # truth from t0
    ax.plot(years, surv_dx, "o-", color=GOLD, lw=2.2, label="Survival from diagnosis (lead-time)")
    ax.plot(years, surv_rand, "s-", color=TEAL, lw=2.2, label="Survival from randomization")
    ax.set_xlabel("Years")
    ax.set_ylabel("% alive")
    ax.set_title("Lead-time illusion: absolute survival clock must start at t0", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch22_leadtime_abs.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 4.9))
    # pre/post thresholds
    ax.axhline(10, color=GOLD, ls="--", lw=1.5)
    ax.axhline(60, color=TEAL, ls="--", lw=1.5)
    ax.text(0.2, 12, "test threshold", color=GOLD, fontsize=8)
    ax.text(0.2, 62, "treat threshold", color=TEAL, fontsize=8)
    xs = [1, 2, 3]
    probs = [5, 35, 75]
    labs = ["Pre-test", "After LR+", "After second test"]
    ax.plot(xs, probs, "o-", color=INDIGO, lw=2.5, ms=10)
    for x, p, l in zip(xs, probs, labs):
        ax.text(x, p + 4, f"{l}\n{p}%", ha="center", fontsize=8.5, fontweight="bold", color=INDIGO)
    ax.set_xlim(0.5, 3.5)
    ax.set_ylim(0, 100)
    ax.set_xticks([])
    ax.set_ylabel("Absolute probability (%)")
    ax.set_title("Dual-process thresholds: absolute post-test vs action lines", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch23_threshold_abs.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    comps = ["Composite\nheadline", "Death", "Disabling\nstroke", "Revasc\nurgency"]
    arr = [6.0, 0.5, 1.0, 4.5]
    cols = [INDIGO, CORAL, GOLD, TEAL]
    ax.bar(range(4), arr, color=cols, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(range(4))
    ax.set_xticklabels(comps, fontsize=9)
    ax.set_ylabel("ARR (pp)")
    ax.set_title("Composite absolute residual: soft components can drive the headline", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch24_composite_abs.png")


def fig_ch25():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # natural frequencies 1000, prev 10%, LR+ = 5 → post ≈ 36%
    ax.bar([0, 1], [10, 36], color=[GRAY, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Pre-test %", "Post-test %\n(LR+=5)"], fontsize=9)
    ax.set_ylabel("Absolute probability")
    ax.set_title("Diagnostic absolute update", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    # prognostic horizon risk
    ax.bar([0, 1, 2], [8, 18, 30], color=[TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["7 d", "30 d", "90 d"], fontsize=9)
    ax.set_ylabel("Absolute event risk %")
    ax.set_title("Prognostic absolute horizons", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Dx vs px papers: absolute post-test ≠ horizon risk (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch25_lr_horizon_abs.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    studies = np.array([2, 5, 3.5, 7, 1, 4])
    y = np.arange(len(studies))
    ax.hlines(y, studies - 2, studies + 2, color=INDIGO, lw=2.5)
    ax.plot(studies, y, "o", color=TEAL, ms=8)
    ax.axvline(3.8, color=GOLD, lw=2, label="Pooled mean")
    ax.axvspan(-1, 8.5, alpha=0.08, color=CORAL)
    ax.plot([-0.5, 8.2], [-0.8, -0.8], color=CORAL, lw=4, solid_capstyle="round")
    ax.text(3.8, -0.8, "  Prediction interval", va="center", fontsize=9, color=CORAL, fontweight="bold")
    ax.set_yticks(y)
    ax.set_yticklabels([f"Study {i+1}" for i in range(len(studies))], fontsize=8)
    ax.set_xlabel("ARR (pp)")
    ax.set_xlim(-2, 10)
    ax.set_ylim(-1.5, len(studies) - 0.3)
    ax.set_title("SR residual: prediction interval for absolute next-study ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch26_pi_abs.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    labs = ["Events\ncontrol", "Events\ntx", "Fragility\nindex", "FQ\n(%)"]
    # display mixed units carefully
    vals = [45, 32, 4, 9]
    cols = [GRAY, TEAL, CORAL, GOLD]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Count / % (teaching dual)")
    ax.set_title("Fragility: few event flips null the absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.text(2, 6, "FI=4", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch27_fragility_abs.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # natural frequencies for shared decision
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Shared decision: absolute frequencies per 100 patients", fontsize=11, fontweight="bold", color=INDIGO)
    boxes = [
        (0.4, 4.2, 4.4, 3.2, TEAL, "Without tx\n12 bad outcomes\n/ 100"),
        (5.2, 4.2, 4.4, 3.2, INDIGO, "With tx\n8 bad outcomes\n/ 100"),
        (0.4, 0.6, 9.2, 2.8, GOLD, "ARR 4 pp → NNT 25 · Harm 1.5 pp → NNH ≈ 67\nTalk numbers, not relative percentages alone"),
    ]
    for x, y, w, h, e, t in boxes:
        ax.add_patch(
            FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.04,rounding_size=0.08",
                           facecolor=WHITE, edgecolor=e, lw=1.6)
        )
        ax.text(x + w / 2, y + h / 2, t, ha="center", va="center", fontsize=10, fontweight="bold", color=e)
    fig.tight_layout()
    return _save(fig, "cycle20_swarm_ch28_sdm_abs.png")


def main():
    print("Cycle-20 →", OUT)
    for fn in [fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
