#!/usr/bin/env python3
"""CRIT-APP Cycle-45 densify: ch01–14 toward uniform floor 23. Agg indigo. ARR/NNT. pred≠cause."""
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
    stages = ["Headline", "Relative\nonly", "ARR\nfound", "NNT\nbedside", "Local\nadopt"]
    frac = [1.0, 0.70, 0.35, 0.22, 0.12]
    ax.plot(stages, frac, "o-", color=INDIGO, lw=2.5, ms=10)
    ax.fill_between(range(5), frac, color=TEAL, alpha=0.15)
    ax.set_ylabel("Fraction of practice-changing claims surviving filter")
    ax.set_title("Ch01 residual: absolute filters shrink the adopt-worthy claim set", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.15); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch01_filter.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sections = ["Abstract", "Methods", "Results\nARR", "Tables", "Spin\ncheck"]
    minutes = [1, 3, 2, 3, 1]
    value = [0.3, 0.5, 1.0, 0.8, 0.9]
    x = np.arange(5)
    ax.bar(x - 0.2, minutes, width=0.4, color=GRAY, edgecolor=INDIGO, label="Minutes")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, value, width=0.4, color=TEAL, edgecolor=INDIGO, label="Absolute-signal value")
    ax.set_xticks(x); ax.set_xticklabels(sections, fontsize=8)
    ax.set_ylabel("Minutes"); ax2.set_ylabel("Relative value (teaching)")
    ax.set_title("Ch02 residual: spend scarce minutes where absolute signal lives", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch02_minute_roi.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # index time shifts absolute risk zero
    t = np.linspace(-30, 180, 100)
    risk_dx = np.where(t < 0, 0, 1 - np.exp(-0.008 * t))
    risk_hosp = np.where(t < 14, 0, 1 - np.exp(-0.008 * (t - 14)))
    ax.plot(t, risk_dx * 100, color=TEAL, lw=2.3, label="Index = diagnosis day")
    ax.plot(t, risk_hosp * 100, color=CORAL, lw=2.3, label="Index = hospital day 14")
    ax.axvline(0, color=GOLD, ls="--", label="Diagnosis")
    ax.set_xlabel("Days from diagnosis"); ax.set_ylabel("Absolute cumulative risk %")
    ax.set_title("Ch03 residual: index-time choice rewrites absolute cumulative risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch03_index_time.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    biases = ["Selection", "Info", "Confound", "Attrition", "Reporting"]
    abs_bias = [2.5, 1.2, 3.0, 1.8, 0.9]
    ax.barh(biases, abs_bias, color=CORAL, edgecolor=INDIGO)
    ax.set_xlabel("|Absolute ARR distortion| (pp)")
    ax.set_title("Ch04 residual: bias taxonomy must be scored in absolute units", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch04_bias_abs.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # backdoor adjustment path absolute
    steps = ["Crude", "Age", "+Sex", "+NIHSS", "+LVO"]
    arr = [8.0, 6.2, 5.8, 4.1, 3.9]
    ax.plot(steps, arr, "o-", color=INDIGO, lw=2.5, ms=10)
    ax.axhline(3.9, color=TEAL, ls="--", label="Target-trial ARR sketch")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch05 residual: sequential backdoor control moves absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch05_backdoor.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    n = np.array([50, 100, 200, 400, 800])
    se = 12 / np.sqrt(n)
    arr = 4.0
    ax.fill_between(n, arr - 1.96 * se, arr + 1.96 * se, color=TEAL, alpha=0.25, label="95% CI absolute ARR")
    ax.plot(n, np.full_like(n, arr, dtype=float), color=INDIGO, lw=2.3, label="Point ARR=4pp")
    ax.set_xlabel("Sample size per arm"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch06 residual: power is precision of absolute effects, not only p-values", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch06_precision.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # confounding by indication absolute
    severity = np.array([1, 2, 3, 4, 5])
    treat_prob = np.array([0.1, 0.25, 0.45, 0.7, 0.9])
    outcome = 5 + 3 * severity  # worse if severe
    ax.plot(severity, treat_prob * 100, "o-", color=GOLD, lw=2.2, label="P(treat) %")
    ax2 = ax.twinx()
    ax2.plot(severity, outcome, "s-", color=CORAL, lw=2.3, label="Absolute outcome risk %")
    ax.set_xlabel("Severity stratum"); ax.set_ylabel("Treatment probability %"); ax2.set_ylabel("Absolute risk %")
    ax.set_title("Ch07 residual: confounding-by-indication couples treatment to absolute risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch07_cbi.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    thresh = np.linspace(0.05, 0.5, 40)
    # treat if post > thresh; net absolute benefit sketch
    nb = 0.08 - 0.2 * (thresh - 0.15) ** 2
    ax.plot(thresh, nb, color=TEAL, lw=2.5)
    ax.axhline(0, color=CORAL, ls="--")
    ax.set_xlabel("Absolute post-test treat threshold"); ax.set_ylabel("Net absolute benefit")
    ax.set_title("Ch08 residual: diagnostic value is threshold-specific absolute net benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch08_nb_thresh.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    deciles = np.arange(1, 11)
    pred = deciles * 4
    obs = pred + np.array([-1, 0, 1, -2, 2, 3, -1, 4, 5, 8])  # miscal high end
    ax.plot([0, 45], [0, 45], "--", color=GRAY, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=CORAL, lw=2.3, label="Observed absolute risk")
    ax.set_xlabel("Predicted absolute risk %"); ax.set_ylabel("Observed absolute risk %")
    ax.set_title("Ch09 residual: pred≠cause — calibration plots police absolute claims", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch09_calplot.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    studies = ["S1", "S2", "S3", "S4", "S5", "Pool"]
    arr = [2, 5, 3, 8, 1, 3.6]
    colors = [TEAL] * 5 + [INDIGO]
    ax.bar(studies, arr, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch10 residual: pooled absolute effects can mask study-level absolute spread", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch10_study_spread.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 12, 80)
    cif = 1 - np.exp(-0.05 * t)
    aci = 1 - np.exp(-0.03 * t)  # all-cause
    ax.plot(t, cif * 100, color=TEAL, lw=2.4, label="Stroke CIF absolute %")
    ax.plot(t, aci * 100, color=CORAL, lw=2.2, label="Death CIF absolute %")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch11 residual: report competing absolute CIFs side-by-side", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch11_dual_cif.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # NNT uncertainty band
    arr = np.linspace(0.5, 10, 50)
    nnt = 100 / arr
    nnt_lo = 100 / (arr + 1.5)
    nnt_hi = 100 / np.maximum(arr - 1.5, 0.2)
    ax.plot(arr, nnt, color=INDIGO, lw=2.5, label="NNT")
    ax.fill_between(arr, nnt_lo, nnt_hi, color=GOLD, alpha=0.25, label="Absolute ARR CI → NNT band")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("NNT")
    ax.set_title("Ch12 residual: NNT inherits absolute ARR uncertainty asymmetrically", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 80); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch12_nnt_band.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # forest of subgroup absolute ARRs
    labs = ["Age<70", "Age≥70", "Male", "Female", "LVO+", "LVO−"]
    arr = [4.0, 6.5, 4.5, 4.2, 8.0, 2.0]
    lo = [1, 3, 2, 1.5, 5, -0.5]
    hi = [7, 10, 7, 7, 11, 4.5]
    y = np.arange(len(labs))
    ax.hlines(y, lo, hi, color=TEAL, lw=2)
    ax.plot(arr, y, "o", color=INDIGO, ms=9)
    ax.axvline(0, color=CORAL, ls="--")
    ax.set_yticks(y); ax.set_yticklabels(labs)
    ax.set_xlabel("Absolute ARR (pp) with CI")
    ax.set_title("Ch13 residual: subgroup claims need absolute forests, not only RR stars", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch13_sub_forest.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    gates = ["Data\nlineage", "Leakage\ncheck", "Abs\ncal", "Decision\ncurve", "Monitor\nplan"]
    pass_rate = [0.9, 0.55, 0.35, 0.25, 0.15]
    ax.bar(gates, pass_rate, color=[TEAL if p > 0.5 else (GOLD if p > 0.3 else CORAL) for p in pass_rate], edgecolor=INDIGO)
    ax.set_ylabel("Fraction of ML papers passing gate")
    ax.set_title("Ch14 residual: pred≠cause — absolute calibration is the rarest ML pass", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.1); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle45_swarm_ch14_ml_gates.png")


def main():
    print("Cycle-45 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
