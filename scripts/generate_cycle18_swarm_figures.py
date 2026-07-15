#!/usr/bin/env python3
"""CRIT-APP Cycle-18 densify: floor-10 chapters → 11 (wave B).

ch02 time-box absolute stopwatch residual
ch03 PECO absolute exposure contrast
ch05 target-trial absolute eligibility
ch07 immortal-time absolute inflation
ch09 discrimination vs absolute decision
ch10 publication bias absolute funnel residual
ch13 subgroup absolute spin ladder

Agg indigo. cycle18_swarm_* only.
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


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 4.8))
    mins = ["0–2", "2–8", "8–13", "13–17", "17–20"]
    focus = [2, 6, 5, 4, 3]
    labels_short = ["Triage", "F&T abs", "Methods", "Threats", "Action"]
    cols = [GRAY, TEAL, INDIGO, GOLD, CORAL]
    ax.barh(range(5)[::-1], focus, color=cols, edgecolor=INDIGO, height=0.65)
    ax.set_yticks(range(5)[::-1])
    ax.set_yticklabels([f"{m}  {l}" for m, l in zip(mins, labels_short)], fontsize=9)
    ax.set_xlabel("Minutes allocated (teaching)")
    ax.set_title("Time-box residual: protect absolute F&T and action minutes", fontsize=11, fontweight="bold", color=INDIGO)
    ax.axvline(0, color=SLATE, lw=0.5)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch02_timebox_abs.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("PECO absolute exposure contrast board", fontsize=11, fontweight="bold", color=INDIGO)
    boxes = [
        (0.3, 5.5, "P population @ t0", INDIGO),
        (5.2, 5.5, "E exposure strategy", TEAL),
        (0.3, 2.5, "C comparator strategy", GOLD),
        (5.2, 2.5, "O outcome @ horizon\n→ ARR", CORAL),
    ]
    for x, y, t, e in boxes:
        ax.add_patch(
            FancyBboxPatch((x, y), 4.5, 2.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                           facecolor=WHITE, edgecolor=e, lw=1.6)
        )
        ax.text(x + 2.25, y + 1.0, t, ha="center", va="center", fontsize=10, fontweight="bold", color=e)
    ax.annotate("", xy=(5.0, 3.5), xytext=(5.0, 5.5),
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.5))
    ax.text(5, 0.8, "Write PECO before any relative effect claim", ha="center", fontsize=10, color=SLATE, fontweight="bold")
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch03_peco_abs.png")


def fig_ch05():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    steps = ["Eligibility", "Treatment\nstrategies", "Assignment", "Follow-up", "Outcomes", "Analysis"]
    ok = [1, 1, 0.3, 0.8, 1, 0.5]  # fidelity scores teaching
    cols = [TEAL if v > 0.7 else (GOLD if v > 0.4 else CORAL) for v in ok]
    ax.barh(range(len(steps))[::-1], ok, color=cols, edgecolor=INDIGO, height=0.65)
    ax.set_yticks(range(len(steps))[::-1])
    ax.set_yticklabels(steps, fontsize=9)
    ax.set_xlim(0, 1.15)
    ax.set_xlabel("Target-trial fidelity (teaching)")
    ax.set_title("Emulation scorecard", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3)

    ax = axes[1]
    ax.bar([0, 1], [11, 3.5], color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Naive ARR\n(broken t0)", "Emulated ARR\n(aligned)"], fontsize=9)
    ax.set_ylabel("ARR (pp)")
    ax.set_title("Absolute residual after alignment", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Target-trial thinking: eligibility & t0 failures invent absolute benefit (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch05_tte_abs.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    # timeline schematic as bars
    labs = ["Truth\n(landmark)", "Immortal-time\nmisclassified"]
    # person-time composition
    exposed_immortal = [30, 0]  # % of follow-up wrongly called exposed-event-free
    true_risk = [8, 8]
    apparent = [8, 3]  # immortal time deflates exposed risk
    x = np.arange(2)
    w = 0.35
    ax.bar(x - w / 2, true_risk, width=w, color=TEAL, edgecolor=INDIGO, label="True risk %")
    ax.bar(x + w / 2, apparent, width=w, color=CORAL, edgecolor=INDIGO, label="Apparent risk %")
    ax.set_xticks(x)
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Event risk (%)")
    ax.set_title("Immortal time invents absolute benefit for 'exposed'", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=9)
    ax.text(1, 7.2, "deflated EER → fake ARR", ha="center", color=CORAL, fontsize=9, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch07_immortal_abs.png")


def fig_ch09():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # ROC-ish
    fpr = np.linspace(0, 1, 80)
    tpr = fpr ** 0.4
    ax.plot(fpr, tpr, color=INDIGO, lw=2.4)
    ax.plot([0, 1], [0, 1], "--", color=GRAY)
    ax.set_xlabel("1 − Spec")
    ax.set_ylabel("Sensitivity")
    ax.set_title("Discrimination (ranking only)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.text(0.55, 0.25, "AUROC high\n≠ action", color=CORAL, fontsize=9, fontweight="bold")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    thresh = np.array([5, 10, 15, 20, 30])
    treat_rate = np.array([60, 40, 25, 15, 8])
    event_prev = np.array([18, 18, 18, 18, 18])
    ax.plot(thresh, treat_rate, "o-", color=GOLD, lw=2.2, label="% treated if threshold")
    ax.plot(thresh, event_prev, "s--", color=TEAL, lw=2.0, label="Event rate (flat)")
    ax.set_xlabel("Risk threshold (%)")
    ax.set_ylabel("% of cohort")
    ax.set_title("Absolute decisions need thresholds", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.suptitle("Prognosis models: discrimination ≠ absolute treat policy (pred≠cause) (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch09_disc_vs_decision.png")


def fig_ch10():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    # funnel-like scatter
    rng = np.random.default_rng(7)
    se = rng.uniform(0.05, 0.35, 24)
    # bias: smaller studies more positive RR reduction
    logrr = -0.15 + rng.normal(0, se) - 0.4 * (se - 0.05)
    ax.scatter(logrr, se, c=INDIGO, s=40, alpha=0.85, edgecolors=WHITE, linewidths=0.5)
    ax.axvline(-0.15, color=TEAL, ls="--", lw=1.5, label="Pooled")
    ax.invert_yaxis()
    ax.set_xlabel("log RR")
    ax.set_ylabel("SE (precision ↓)")
    ax.set_title("Funnel asymmetry (teaching)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    labs = ["Published\nARR", "Trim-fill\ncorrected", "Large-trial\nonly"]
    vals = [5.5, 3.0, 2.8]
    ax.bar(range(3), vals, color=[CORAL, GOLD, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Publication bias inflates absolute effect", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Evidence synthesis: small-study bias rewrites absolute RD/NNT (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch10_funnel_abs.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Subgroup spin ladder → absolute residual", fontsize=11, fontweight="bold", color=INDIGO)
    steps = [
        (8.2, CORAL, "1  Fish subgroup p without interaction test"),
        (6.4, ORANGE, "2  Report only favorable stratum RR"),
        (4.6, GOLD, "3  Hide absolute risks / NNT by stratum"),
        (2.8, PURPLE, "4  Market 'works only in X' without pre-spec"),
        (1.0, TEAL, "STOP: demand interaction + stratum ARR/NNT"),
    ]
    for y, e, t in steps:
        ax.add_patch(
            FancyBboxPatch((0.35, y - 0.6), 9.3, 1.35,
                           boxstyle="round,pad=0.03,rounding_size=0.07",
                           facecolor=WHITE, edgecolor=e, lw=1.5)
        )
        ax.text(0.7, y + 0.05, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle18_swarm_ch13_subgroup_spin.png")


def main():
    print("Cycle-18 →", OUT)
    for fn in [fig_ch02, fig_ch03, fig_ch05, fig_ch07, fig_ch09, fig_ch10, fig_ch13]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
