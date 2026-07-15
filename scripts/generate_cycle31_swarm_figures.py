#!/usr/bin/env python3
"""CRIT-APP Cycle-31 densify: floor-15 → toward 16 (ch01–14). Agg indigo. cycle31_swarm_*."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig); print("  wrote", p.name); return p

def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    years = np.arange(2016, 2026)
    papers = 40 + 8 * (years - 2016) + np.array([0, 2, -1, 3, 1, 4, 2, 5, 3, 6])
    appraised = papers * np.linspace(0.2, 0.55, 10)
    ax.plot(years, papers, "o-", color=GRAY, lw=2, label="Stroke papers/week (teaching)")
    ax.plot(years, appraised, "s-", color=TEAL, lw=2.3, label="Truly ARR-appraised")
    ax.fill_between(years, appraised, papers, color=CORAL, alpha=0.12, label="Appraisal gap")
    ax.set_title("Density residual: absolute appraisal capacity lags literature volume", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylabel("Count (teaching)"); ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    fig.tight_layout(); return _save(fig, "cycle31_swarm_ch01_appraisal_gap.png")

def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cards = ["Q", "Design", "ARR", "Bias", "Action"]
    complete = [1, 1, 0, 1, 1]
    ax.bar(cards, complete, color=[TEAL if c else CORAL for c in complete], edgecolor=INDIGO)
    ax.set_ylim(0, 1.3); ax.set_ylabel("Card completed (0/1)")
    ax.set_title("Speed residual: missing absolute ARR card breaks the 5-card chain", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch02_five_card.png")

def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strategies = ["Drug A\n// usual", "Drug A\n// active", "Strategy\n// strategy"]
    arr = [5.5, 3.0, 2.2]
    ax.bar(strategies, arr, color=[CORAL, GOLD, TEAL], edgecolor=INDIGO)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Estimand residual: comparator choice rewrites absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch03_comparator_arr.png")

def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.linspace(0, 1, 50)
    internal = x
    external = 1 - 0.6 * x + 0.1 * np.sin(6 * x)
    ax.plot(internal, external, color=INDIGO, lw=2.5)
    ax.scatter([0.85], [0.42], s=100, color=CORAL, zorder=5)
    ax.text(0.7, 0.5, "tight RCT", color=CORAL, fontsize=8, fontweight="bold")
    ax.set_xlabel("Internal validity"); ax.set_ylabel("External transport")
    ax.set_title("Validity residual: absolute local use needs transport, not bias control alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch04_transport.png")

def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    steps = ["Eligibility", "Treatment\nstrategies", "Assignment", "Follow-up", "Outcome", "Analysis"]
    complete = [1, 0.8, 0.6, 0.9, 1, 0.5]
    ax.plot(range(6), complete, "o-", color=TEAL, lw=2.4, ms=9)
    ax.axhline(0.8, color=GOLD, ls="--")
    ax.set_xticks(range(6)); ax.set_xticklabels(steps, fontsize=8)
    ax.set_ylabel("Target-trial component completeness")
    ax.set_title("DAG/target-trial residual: weak analysis linkage leaks absolute bias", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.15); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch05_tte_components.png")

def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arms = np.array([0, 1])
    # cumulative incidence
    t = np.linspace(0, 90, 50)
    c = 1 - np.exp(-0.004 * t)
    tr = 1 - np.exp(-0.0028 * t)
    ax.plot(t, c * 100, color=GRAY, lw=2.3, label="Control")
    ax.plot(t, tr * 100, color=TEAL, lw=2.3, label="Treated")
    ax.fill_between(t, tr * 100, c * 100, color=INDIGO, alpha=0.15, label="Absolute ARR(t)")
    ax.set_xlabel("Days"); ax.set_ylabel("Cumulative incidence %")
    ax.set_title("RCT residual: absolute ARR as the vertical gap between incidence curves", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch06_arr_gap.png")

def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    methods = ["Crude", "Multivar", "PS match", "IPTW", "IV"]
    residual = [7, 4.5, 3.2, 2.8, 1.5]
    ax.plot(methods, residual, "o-", color=CORAL, lw=2.4, ms=9)
    ax.set_ylabel("Residual absolute confounding (pp)")
    ax.set_title("Observational residual: design ladder shrinks absolute residual confounding", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch07_design_ladder.png")

def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    thr = np.linspace(0, 1, 80)
    # ROC
    tpr = thr ** 0.4
    fpr = thr ** 1.2
    ax.plot(fpr, tpr, color=INDIGO, lw=2.5, label="ROC")
    ax.plot([0, 1], [0, 1], ":", color=GRAY)
    # mark utility point
    ax.scatter([0.22], [0.78], s=120, color=GOLD, zorder=5, label="Utility operating point")
    ax.set_xlabel("FPR"); ax.set_ylabel("TPR")
    ax.set_title("Diagnostic residual: pick absolute utility operating point on the ROC", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch08_roc_utility.png")

def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # DCA-like thresholds already done; show Brier components
    labs = ["Reliability", "Resolution", "Uncertainty", "Brier"]
    vals = [0.02, 0.08, 0.15, 0.09]
    ax.bar(labs, vals, color=[TEAL, GOLD, GRAY, INDIGO], edgecolor=INDIGO)
    ax.set_ylabel("Score component (teaching)")
    ax.set_title("Prognosis residual: Brier decomposes absolute probability accuracy (pred ≠ cause)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch09_brier.png")

def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # cumulative meta ARR
    k = np.arange(1, 11)
    arr = 6 - 0.3 * k + np.array([0.5, -0.2, 0.3, -0.1, 0, 0.2, -0.15, 0.1, 0, -0.05])
    ax.plot(k, arr, "o-", color=TEAL, lw=2.4)
    ax.axhline(3.5, color=GOLD, ls="--", label="Stable absolute ARR")
    ax.set_xlabel("Studies added (cumulative meta)")
    ax.set_ylabel("Pooled absolute ARR (pp)")
    ax.set_title("Meta residual: early cumulative absolute ARR often drifts before stability", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch10_cum_meta.png")

def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mrs = np.arange(0, 6)
    shift = np.array([4, 3, 2, -2, -3, -4])
    cols = [TEAL if s > 0 else CORAL for s in shift]
    ax.bar(mrs, shift, color=cols, edgecolor=INDIGO)
    ax.axhline(0, color=GRAY)
    ax.set_xlabel("mRS"); ax.set_ylabel("Absolute % point shift (treated − control)")
    ax.set_title("Outcomes residual: ordinal absolute shifts by mRS bin", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch11_mrs_shift.png")

def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(0.5, 10, 40)
    nnt = 100 / arr
    ax.plot(arr, nnt, color=INDIGO, lw=2.5)
    ax.set_xlabel("ARR (pp)"); ax.set_ylabel("NNT")
    ax.set_title("Effect-size residual: NNT is the reciprocal absolute transform of ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 80); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch12_nnt_reciprocal.png")

def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # interaction p vs absolute RERI
    p_int = np.array([0.8, 0.4, 0.2, 0.05, 0.01])
    reri = np.array([0.5, 1.5, 2.0, 2.2, 2.5])
    ax.scatter(p_int, reri, s=90, color=TEAL, edgecolors=INDIGO)
    ax.set_xscale("log"); ax.invert_xaxis()
    ax.set_xlabel("Multiplicative interaction p (log)")
    ax.set_ylabel("Absolute RERI (pp)")
    ax.set_title("Subgroup residual: significant p ≠ large absolute interaction", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, which="both"); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch13_p_vs_reri.png")

def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    stages = ["Offline\nAUROC", "Silent\ntrial", "RCT\nimpact", "Post-deploy\nARR"]
    vals = [0.91, 0.84, 0.6, 0.2]
    display = [9.1, 8.4, 6.0, 2.0]
    ax.bar(stages, display, color=[GOLD, GRAY, TEAL, INDIGO], edgecolor=INDIGO)
    ax.set_ylabel("Scaled metric (AUROC×10 or ARR pp×10)")
    ax.set_title("AI residual: absolute impact ARR is the last — not first — gate (pred ≠ cause)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle31_swarm_ch14_impact_gates.png")

def main():
    print("Cycle-31 →", OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
               fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
