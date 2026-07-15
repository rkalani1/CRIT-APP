#!/usr/bin/env python3
"""CRIT-APP Cycle-19 densify: residual floor-10 → 11 (wave C).

ch14 leakage absolute performance lie residual
ch16 multi-autopsy absolute verdict board
ch17 incidence vs prevalence absolute reservoir
ch18 Bradford Hill absolute residual
ch19 CI width absolute decision zones
ch20 hazard vs absolute risk residual
ch21 standardization absolute rates

Agg indigo. cycle19_swarm_* only.
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


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    labs = ["Leaked\ntest AUROC", "Clean\nholdout", "External\nsite"]
    vals = [0.96, 0.81, 0.72]
    cols = [CORAL, GOLD, TEAL]
    ax.bar(range(3), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("AUROC")
    ax.set_title("Leakage invents absolute performance; external reveals residual", fontsize=11, fontweight="bold", color=INDIGO)
    ax.axhline(0.75, color=GRAY, ls="--", lw=1)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch14_leakage_abs.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Multi-autopsy absolute verdict board", fontsize=11, fontweight="bold", color=INDIGO)
    verdicts = [
        (6.2, TEAL, "RCT: valid ARR → adopt/adapt"),
        (4.4, GOLD, "Obs: residual confounding → wait"),
        (2.6, CORAL, "AI: leakage / no impact → reject deploy"),
        (0.8, ORANGE, "NI / model: shopped estimand → reject"),
    ]
    for y, e, t in verdicts:
        ax.add_patch(
            FancyBboxPatch((0.4, y - 0.55), 9.2, 1.25,
                           boxstyle="round,pad=0.03,rounding_size=0.07",
                           facecolor=WHITE, edgecolor=e, lw=1.5)
        )
        ax.text(0.75, y + 0.05, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch16_verdict_board.png")


def fig_ch17():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # reservoir diagram as bars
    labs = ["Incidence\n(/100 py)", "Prevalence\n(%)", "Duration\n(years)"]
    # prevalence ≈ incidence × duration teaching
    vals = [2.0, 10.0, 5.0]
    ax.bar(range(3), vals, color=[TEAL, INDIGO, GOLD], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_title("P ≈ I × D (teaching units)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Absolute reservoir caution", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.4, 1.5), 9.2, 5, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#FFF8E1", edgecolor=GOLD, lw=1.5))
    ax.text(5, 4.2, "Prevalence is a stock\nIncidence is a flow\nNNT needs incidence/risk,\nnot crude prevalence alone",
            ha="center", va="center", fontsize=10, fontweight="bold", color=SLATE)
    fig.suptitle("Disease frequency: absolute incidence vs prevalence reservoir (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch17_reservoir_abs.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Bradford Hill residual: absolute evidence weight", fontsize=11, fontweight="bold", color=INDIGO)
    items = [
        (8.2, TEAL, "Strength: large absolute ARR more persuasive"),
        (6.4, INDIGO, "Temporality: t0 before outcome (non-negotiable)"),
        (4.6, GOLD, "Dose–response: absolute gradient preferred"),
        (2.8, ORANGE, "Experiment: RCT absolute still king"),
        (1.0, CORAL, "Analogy alone ≠ causal ARR license"),
    ]
    for y, e, t in items:
        ax.add_patch(
            FancyBboxPatch((0.35, y - 0.6), 9.3, 1.35,
                           boxstyle="round,pad=0.03,rounding_size=0.07",
                           facecolor=WHITE, edgecolor=e, lw=1.5)
        )
        ax.text(0.7, y + 0.05, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch18_hill_abs.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    # decision zones on ARR CI
    ax.axvspan(-5, 0, color=CORAL, alpha=0.12)
    ax.axvspan(0, 2, color=GOLD, alpha=0.15)
    ax.axvspan(2, 12, color=TEAL, alpha=0.12)
    ax.text(-2.5, 3.2, "Harm\npossible", ha="center", color=CORAL, fontsize=9, fontweight="bold")
    ax.text(1, 3.2, "Below\nMCID", ha="center", color=GOLD, fontsize=9, fontweight="bold")
    ax.text(7, 3.2, "Clinically\nimportant", ha="center", color=TEAL, fontsize=9, fontweight="bold")
    # three CIs
    for y, lo, hi, pt, col in [
        (2.2, 3, 9, 6, TEAL),
        (1.4, -1, 5, 2, GOLD),
        (0.6, -3, 1.5, -0.5, CORAL),
    ]:
        ax.plot([lo, hi], [y, y], color=col, lw=4, solid_capstyle="round")
        ax.plot(pt, y, "o", color=col, ms=9)
    ax.axvline(0, color=GRAY, lw=1.2)
    ax.axvline(2, color=GOLD, ls="--", lw=1.2)
    ax.set_xlim(-5, 12)
    ax.set_ylim(0, 3.8)
    ax.set_yticks([])
    ax.set_xlabel("ARR (pp)")
    ax.set_title("CI width absolute decision zones (MCID-aware)", fontsize=11, fontweight="bold", color=INDIGO)
    for s in ("top", "right", "left"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch19_ci_zones.png")


def fig_ch20():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    t = np.linspace(0, 36, 60)
    s0 = np.exp(-0.03 * t)
    s1 = np.exp(-0.02 * t)  # HR≈0.67-ish
    ax.plot(t, (1 - s0) * 100, color=GRAY, lw=2.2, label="Control CIF-like")
    ax.plot(t, (1 - s1) * 100, color=TEAL, lw=2.2, label="Treated")
    ax.set_xlabel("Months")
    ax.set_ylabel("Absolute cumulative risk (%)")
    ax.set_title("Same HR, rising absolute gap", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    labs = ["HR", "ARR @12m\n(pp)", "ARR @36m\n(pp)"]
    vals = [0.67, 3.5, 9.0]
    # dual scale display - normalize HR*10 for bar
    display = [6.7, 3.5, 9.0]
    cols = [GOLD, TEAL, INDIGO]
    ax.bar(range(3), display, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Teaching scale (HR×10 | ARR pp)")
    ax.set_title("Hazard ≠ absolute risk difference", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Regression/survival literacy: convert HR to absolute risk@t (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch20_hr_vs_arr.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    groups = ["Site A\ncrude", "Site B\ncrude", "A std", "B std"]
    rates = [12, 7, 9.5, 9.0]
    cols = [CORAL, GOLD, TEAL, INDIGO]
    ax.bar(range(4), rates, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4))
    ax.set_xticklabels(groups, fontsize=9)
    ax.set_ylabel("Event rate (/100 py)")
    ax.set_title("Standardization: crude absolute rates mislead; age-std converges", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle19_swarm_ch21_std_rates.png")


def main():
    print("Cycle-19 →", OUT)
    for fn in [fig_ch14, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
