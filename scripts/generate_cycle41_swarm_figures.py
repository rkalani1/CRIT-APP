#!/usr/bin/env python3
"""CRIT-APP Cycle-41 densify: ch01–14 toward uniform floor 21. Agg indigo. ARR/NNT. pred≠cause."""
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
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    weeks = np.arange(1, 13)
    inbound = 8 + 0.6 * weeks
    appraised = np.minimum(3 + 0.1 * weeks, inbound * 0.35)
    ax.bar(weeks - 0.15, inbound, width=0.3, color=GRAY, edgecolor=INDIGO, label="Inbound stroke papers")
    ax.bar(weeks + 0.15, appraised, width=0.3, color=TEAL, edgecolor=INDIGO, label="ARR-complete appraisals")
    ax.set_xlabel("Week"); ax.set_ylabel("Count")
    ax.set_title("Ch01 residual: inbound literature exceeds absolute-appraisal throughput", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch01_throughput.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mins = np.array([2, 5, 10, 15, 30])
    cards = np.array([0.2, 0.55, 0.85, 0.92, 0.95])
    ax.plot(mins, cards, "o-", color=INDIGO, lw=2.5, ms=9)
    ax.axvline(10, color=GOLD, ls="--", label="10-min absolute card")
    ax.set_xlabel("Minutes allocated"); ax.set_ylabel("Fraction with ARR/NNT captured")
    ax.set_title("Ch02 residual: a fixed absolute-risk card maximizes signal per minute", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch02_timecard.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Protocol\nestimand", "Analysis\nset used", "Gap\n(abs)"]
    arr = [4.5, 6.8, 2.3]
    colors = [TEAL, CORAL, GOLD]
    ax.bar(labels, arr, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch03 residual: estimand–analysis mismatch rewrites absolute effect", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch03_estimand_gap.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    steps = ["Source\npop", "Eligible", "Enrolled", "Analyzed"]
    risk = [12.0, 10.5, 7.0, 5.5]
    ax.plot(steps, risk, "s-", color=CORAL, lw=2.4, ms=10, label="Absolute outcome risk %")
    ax.fill_between(range(4), risk, color=CORAL, alpha=0.12)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch04 residual: selection cascade compresses absolute baseline risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch04_selection.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # collider conditioning vs confounder adjustment absolute bias
    scenarios = ["Crude", "Adjust\nconfounder", "Condition\ncollider"]
    bias = [3.0, 0.4, 4.5]
    colors = [GOLD, TEAL, CORAL]
    ax.bar(scenarios, bias, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("|Absolute ARR bias| (pp)")
    ax.set_title("Ch05 residual: collider conditioning inflates absolute bias vs confounder control", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch05_collider.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sets = ["ITT", "mITT", "Per-protocol", "As-treated"]
    arr = [3.2, 3.8, 5.5, 6.1]
    ax.bar(sets, arr, color=[TEAL, GREEN, GOLD, CORAL], edgecolor=INDIGO)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch06 residual: analysis-set choice moves absolute ARR more than chance", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch06_analysis_sets.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    covars = np.arange(0, 8)
    residual = 5.0 * np.exp(-0.35 * covars) + 0.8
    ax.plot(covars, residual, "o-", color=CORAL, lw=2.4, label="Residual absolute bias (pp)")
    ax.axhline(1.0, color=TEAL, ls="--", label="Acceptable residual 1pp")
    ax.set_xlabel("Measured covariates adjusted"); ax.set_ylabel("Residual |ARR bias| pp")
    ax.set_title("Ch07 residual: residual confounding can remain large in absolute units", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch07_residual_conf.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prev = np.linspace(0.02, 0.40, 40)
    sens, spec = 0.90, 0.85
    # absolute true-positive and false-positive rates among tested
    tp = sens * prev
    fp = (1 - spec) * (1 - prev)
    net = tp - 0.3 * fp  # weighted absolute utility sketch
    ax.plot(prev * 100, tp * 100, color=TEAL, lw=2.2, label="Absolute TP %")
    ax.plot(prev * 100, fp * 100, color=CORAL, lw=2.2, label="Absolute FP %")
    ax.plot(prev * 100, net * 100, color=INDIGO, lw=2.5, ls="--", label="Net absolute (weighted)")
    ax.set_xlabel("Prior absolute prevalence %"); ax.set_ylabel("Absolute % of tested")
    ax.set_title("Ch08 residual: sens/spec alone omit absolute TP/FP burden", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch08_tp_fp.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # calibration slope vs discrimination — pred≠cause
    models = ["A", "B", "C", "D"]
    auroc = [0.72, 0.81, 0.88, 0.91]
    cal_err = [1.0, 2.5, 5.0, 8.0]
    x = np.arange(4)
    ax.bar(x - 0.2, auroc, width=0.4, color=GOLD, edgecolor=INDIGO, label="AUROC")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, cal_err, width=0.4, color=CORAL, edgecolor=INDIGO, label="Abs cal error pp")
    ax.set_xticks(x); ax.set_xticklabels(models)
    ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute calibration error (pp)")
    ax.set_title("Ch09 residual: pred≠cause — high AUROC can hide absolute miscalibration", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch09_cal_vs_auc.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    certainty = ["High", "Mod", "Low", "V.low"]
    arr = [4.0, 3.5, 2.0, 1.0]
    ci_half = [0.8, 1.5, 3.0, 5.0]
    x = np.arange(4)
    ax.bar(x, arr, color=TEAL, edgecolor=INDIGO, label="Pooled absolute ARR")
    ax.errorbar(x, arr, yerr=ci_half, fmt="none", ecolor=CORAL, capsize=5, lw=2, label="Absolute CI half-width")
    ax.set_xticks(x); ax.set_xticklabels(certainty)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch10 residual: GRADE certainty should travel with absolute effect precision", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch10_grade_abs.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mrs = np.arange(0, 6)
    util = np.array([1.0, 0.91, 0.76, 0.65, 0.33, 0.0])
    shift_ctrl = np.array([0.12, 0.18, 0.22, 0.20, 0.15, 0.13])
    shift_tx = np.array([0.18, 0.22, 0.24, 0.16, 0.12, 0.08])
    ax.bar(mrs - 0.2, shift_ctrl, width=0.4, color=GRAY, edgecolor=INDIGO, label="Control proportion")
    ax.bar(mrs + 0.2, shift_tx, width=0.4, color=TEAL, edgecolor=INDIGO, label="Treatment proportion")
    ax2 = ax.twinx()
    ax2.plot(mrs, util, "o--", color=GOLD, lw=2, label="Utility weight")
    ax.set_xlabel("mRS"); ax.set_ylabel("Absolute probability"); ax2.set_ylabel("Utility")
    ax.set_title("Ch11 residual: ordinal shift needs absolute cell moves, not only common odds", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper right", fontsize=8); ax2.legend(loc="center right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch11_mrs_shift.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    baseline = np.array([2, 5, 10, 20, 40])
    rr = 0.75
    arr = baseline * (1 - rr)
    nnt = 100 / arr
    ax.plot(baseline, nnt, "o-", color=INDIGO, lw=2.5, ms=9, label="NNT = 1/ARR")
    for b, n, a in zip(baseline, nnt, arr):
        ax.annotate(f"ARR={a:.1f}pp", (b, n), textcoords="offset points", xytext=(6, 4), fontsize=7, color=SLATE)
    ax.set_xlabel("Baseline absolute risk %"); ax.set_ylabel("NNT")
    ax.set_title("Ch12 residual: same RR maps to a family of absolute NNT values", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch12_nnt_family.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    tests = np.arange(1, 21)
    # expected false absolute "significant" claims under null
    fpr = 1 - (1 - 0.05) ** tests
    ax.plot(tests, fpr * 100, color=CORAL, lw=2.5)
    ax.axhline(5, color=TEAL, ls="--", label="Single-test 5%")
    ax.set_xlabel("Unadjusted subgroup tests"); ax.set_ylabel("Absolute risk ≥1 false positive %")
    ax.set_title("Ch13 residual: multiplicity raises absolute false-positive claim risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch13_multiplicity.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    shifts = ["None", "Covariate", "Label", "Concept"]
    auroc = [0.86, 0.84, 0.82, 0.70]
    abs_nb = [0.10, 0.08, 0.02, -0.04]
    x = np.arange(4)
    ax.bar(x - 0.2, auroc, width=0.4, color=GOLD, edgecolor=INDIGO, label="AUROC")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, abs_nb, width=0.4, color=CORAL, edgecolor=INDIGO, label="Absolute net benefit")
    ax2.axhline(0, color=SLATE, ls=":")
    ax.set_xticks(x); ax.set_xticklabels(shifts)
    ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute net benefit")
    ax.set_title("Ch14 residual: pred≠cause — label/concept shift kills absolute net benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle41_swarm_ch14_shift_types.png")


def main():
    print("Cycle-41 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
