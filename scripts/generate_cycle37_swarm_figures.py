#!/usr/bin/env python3
"""CRIT-APP Cycle-37 densify: ch01–14 toward uniform floor 19. Agg indigo. ARR/NNT. pred≠cause."""
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
    protocol_err = np.cumsum(np.array([0.4, 0.3, 0.5, 0.2, 0.6, 0.3, 0.4, 0.5, 0.2, 0.3, 0.4, 0.5]))
    arr_miss = protocol_err * 0.35
    ax.plot(weeks, protocol_err, "o-", color=CORAL, lw=2.3, label="Cumulative protocol drift (pp absolute)")
    ax.plot(weeks, arr_miss, "s--", color=TEAL, lw=2.2, label="Estimated ARR mis-specification")
    ax.set_xlabel("Week after new stroke pathway live")
    ax.set_ylabel("Absolute percentage points")
    ax.set_title("Ch01 residual: protocol drift accumulates absolute decision error", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch01_protocol_drift.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    order = ["Question", "Design", "ARR/NNT", "Bias map", "Action"]
    minutes = [2, 3, 4, 5, 3]
    colors = [TEAL, TEAL, GOLD, TEAL, INDIGO]
    bars = ax.barh(order[::-1], minutes[::-1], color=colors[::-1], edgecolor=INDIGO)
    ax.axvline(12, color=CORAL, ls="--", lw=1.8, label="15-min budget minus buffer")
    ax.set_xlabel("Minutes allocated (teaching budget)")
    ax.set_title("Ch02 residual: absolute ARR card needs protected time under pressure", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch02_timebox.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    index = ["Symptom\nonset", "Door\ntime", "Randomize", "First\ndose", "Discharge"]
    arr = [4.8, 4.2, 3.5, 2.1, 1.0]
    ax.plot(range(5), arr, "o-", color=INDIGO, lw=2.5, ms=9)
    for i, (lab, a) in enumerate(zip(index, arr)):
        ax.annotate(f"{a:.1f}pp", (i, a), textcoords="offset points", xytext=(0, 8), ha="center", fontsize=8, color=SLATE)
    ax.set_xticks(range(5)); ax.set_xticklabels(index, fontsize=8)
    ax.set_ylabel("Absolute ARR (pp) under same data")
    ax.set_title("Ch03 residual: index-time choice rewrites absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 6); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch03_index_arr.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    biases = ["Selection", "Confounding", "Info\nmisclass", "Attrition", "Reporting"]
    direction = np.array([1, -1, 1, -1, 1])  # + favors treatment
    magnitude = np.array([2.0, 3.5, 1.2, 1.8, 0.8])
    colors = [CORAL if d > 0 else TEAL for d in direction]
    ax.barh(biases, direction * magnitude, color=colors, edgecolor=INDIGO)
    ax.axvline(0, color=SLATE, lw=1.2)
    ax.set_xlabel("Signed absolute bias on ARR (pp; + favors treatment)")
    ax.set_title("Ch04 residual: bias taxonomy needs direction AND absolute magnitude", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch04_bias_signed.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    steps = ["Crude", "Age", "+Sex", "+NIHSS", "+AF", "+Still open\nbackdoor?"]
    arr = [8.0, 5.5, 5.0, 3.8, 3.2, 3.2]
    ax.step(range(6), arr, where="mid", color=INDIGO, lw=2.5)
    ax.plot(range(6), arr, "o", color=TEAL, ms=9)
    ax.axhspan(2.5, 3.5, color=GOLD, alpha=0.15, label="Residual uncertainty band")
    ax.set_xticks(range(6)); ax.set_xticklabels(steps, fontsize=8)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch05 residual: conditioning shrinks ARR; open backdoors remain absolute risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch05_backdoor_arr.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sets = ["ITT", "mITT", "Per-protocol", "As-treated"]
    event_tx = [12, 11, 9, 8]
    event_ctl = [18, 17, 14, 16]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, event_tx, width=w, color=TEAL, edgecolor=INDIGO, label="Tx event %")
    ax.bar(x + w/2, event_ctl, width=w, color=GRAY, edgecolor=INDIGO, label="Ctl event %")
    for i, (a, b) in enumerate(zip(event_tx, event_ctl)):
        ax.text(i, max(a, b) + 0.6, f"ARR={b-a}pp", ha="center", fontsize=8, fontweight="bold", color=INDIGO)
    ax.set_xticks(x); ax.set_xticklabels(sets)
    ax.set_ylabel("Absolute event rate %")
    ax.set_title("Ch06 residual: analysis set changes absolute event rates and ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 24); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch06_analysis_sets.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    severity = np.linspace(0, 10, 40)
    treated = 5 + 1.2 * severity
    untreated = 8 + 0.9 * severity
    # confounding by indication: treated sicker
    ax.plot(severity, treated, color=TEAL, lw=2.4, label="Treated (sicker) absolute risk")
    ax.plot(severity, untreated, color=CORAL, lw=2.4, label="Untreated absolute risk")
    ax.fill_between(severity, treated, untreated, color=GOLD, alpha=0.2, label="Naïve absolute gap ≠ causal ARR")
    ax.set_xlabel("Indication severity score")
    ax.set_ylabel("Absolute outcome risk %")
    ax.set_title("Ch07 residual: confounding by indication distorts absolute contrasts", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch07_cbi.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prior = np.linspace(0.01, 0.40, 80)
    sens, spec = 0.90, 0.85
    lr_pos = sens / (1 - spec)
    odds = prior / (1 - prior) * lr_pos
    ppv = odds / (1 + odds)
    ax.plot(prior * 100, ppv * 100, color=INDIGO, lw=2.5)
    ax.axvline(10, color=GOLD, ls="--", label="Stroke code prior 10%")
    ax.axhline(ppv[np.argmin(np.abs(prior - 0.10))] * 100, color=TEAL, ls=":", label="PPV at that prior")
    ax.set_xlabel("Pre-test absolute probability %")
    ax.set_ylabel("Post-test absolute PPV %")
    ax.set_title("Ch08 residual: sensitivity alone ≠ absolute post-test probability", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch08_prior_ppv.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # discrimination high but calibration bad → absolute error
    pred = np.linspace(0.05, 0.60, 12)
    obs_good = pred
    obs_bad = 0.08 + 0.55 * pred  # overprediction at high end
    ax.plot([0, 0.65], [0, 0.65], "--", color=GRAY, label="Perfect absolute calibration")
    ax.plot(pred, obs_good, "o-", color=TEAL, lw=2.2, label="Well-calibrated (AUROC same)")
    ax.plot(pred, obs_bad, "s-", color=CORAL, lw=2.2, label="Miscalibrated (AUROC same)")
    ax.set_xlabel("Predicted absolute risk")
    ax.set_ylabel("Observed absolute risk")
    ax.set_title("Ch09 residual: pred≠cause — discrimination ≠ absolute calibration", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch09_cal_gap.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    studies = [f"S{i}" for i in range(1, 7)]
    rr = np.array([0.75, 0.80, 0.70, 0.85, 0.72, 0.78])
    baseline = np.array([20, 8, 15, 4, 25, 12])
    arr = baseline * (1 - rr)
    x = np.arange(6)
    ax.bar(x - 0.2, rr * 10, width=0.35, color=GRAY, edgecolor=INDIGO, label="RR×10 (relative scale)")
    ax.bar(x + 0.2, arr, width=0.35, color=TEAL, edgecolor=INDIGO, label="Absolute ARR (pp)")
    ax.set_xticks(x); ax.set_xticklabels(studies)
    ax.set_ylabel("Scaled metric")
    ax.set_title("Ch10 residual: similar RR can hide large absolute ARR heterogeneity", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch10_rr_vs_arr.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mrs = np.arange(0, 7)
    ctl = np.array([8, 12, 18, 22, 20, 12, 8])
    tx = np.array([12, 16, 20, 20, 16, 10, 6])
    # shift toward better
    ax.bar(mrs - 0.2, ctl, width=0.4, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(mrs + 0.2, tx, width=0.4, color=TEAL, edgecolor=INDIGO, label="Treatment %")
    # binary mRS 0-2 ARR
    bin_ctl = ctl[:3].sum(); bin_tx = tx[:3].sum()
    ax.axhline(0, color=SLATE, lw=0.5)
    ax.text(5.2, 20, f"Binary mRS0–2\nARR={bin_tx-bin_ctl}pp", fontsize=9, color=INDIGO, fontweight="bold",
            bbox=dict(boxstyle="round", facecolor=WHITE, edgecolor=GOLD))
    ax.set_xlabel("mRS category"); ax.set_ylabel("Absolute percent of cohort")
    ax.set_title("Ch11 residual: ordinal shift ≠ single binary ARR — report both", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch11_mrs_shift.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    baseline = np.linspace(2, 40, 80)
    rr = 0.75
    arr = baseline * (1 - rr)
    nnt = 100 / arr
    ax.plot(baseline, nnt, color=INDIGO, lw=2.5)
    ax.axhline(50, color=CORAL, ls="--", label="NNT=50 teaching threshold")
    ax.axvline(8, color=GOLD, ls=":", label="Low baseline risk 8%")
    ax.set_xlabel("Control absolute risk %")
    ax.set_ylabel("NNT (1/ARR)")
    ax.set_title("Ch12 residual: fixed RR → NNT explodes as baseline absolute risk falls", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 200); ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch12_nnt_baseline.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # flat RR, heterogeneous ARR
    strata = ["Age<65", "Age≥65", "NIHSS<10", "NIHSS≥10", "Women", "Men"]
    control_risk = np.array([6, 18, 8, 22, 12, 14])
    rr = 0.80
    arr = control_risk * (1 - rr)
    x = np.arange(len(strata))
    ax.bar(x, arr, color=TEAL, edgecolor=INDIGO, label="Absolute ARR (pp)")
    ax.axhline(control_risk.mean() * (1 - rr), color=GOLD, ls="--", label="Overall ARR")
    ax2 = ax.twinx()
    ax2.plot(x, [rr] * len(strata), "s-", color=CORAL, lw=2, label="RR (flat)")
    ax2.set_ylim(0, 1.5); ax2.set_ylabel("RR")
    ax.set_xticks(x); ax.set_xticklabels(strata, fontsize=8, rotation=15)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch13 residual: flat RR with heterogeneous absolute ARR is not HTE spin-free", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch13_flatrr_hetarr.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    gates = ["Label\nleakage", "External\nvalidation", "Calibration\nslope", "Decision\ncurve", "Causal\nclaim?"]
    scores = [0, 1, 0, 1, 0]  # fail/pass
    colors = [CORAL if s == 0 else TEAL for s in scores]
    ax.bar(gates, [1] * 5, color=colors, edgecolor=INDIGO)
    for i, s in enumerate(scores):
        ax.text(i, 0.5, "FAIL" if s == 0 else "PASS", ha="center", va="center", fontsize=10, fontweight="bold", color=WHITE)
    ax.set_ylim(0, 1.3); ax.set_yticks([])
    ax.set_title("Ch14 residual: ML paper gates — pred≠cause; absolute net benefit required", fontsize=11, fontweight="bold", color=INDIGO)
    fig.tight_layout()
    return _save(fig, "cycle37_swarm_ch14_ml_gates.png")


def main():
    print("Cycle-37 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
