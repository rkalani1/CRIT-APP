#!/usr/bin/env python3
"""CRIT-APP Cycle-47 densify: ch01–14 toward uniform floor 24. Agg indigo. ARR/NNT. pred≠cause."""
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
    years = np.arange(2016, 2026)
    guidelines = 2 + 0.4 * (years - 2016)
    local_abs = 0.5 + 0.15 * (years - 2016)
    ax.plot(years, guidelines, "o-", color=GRAY, lw=2.2, label="Guideline updates citing stroke trials")
    ax.plot(years, local_abs, "s-", color=TEAL, lw=2.3, label="Local absolute-benefit rechecks")
    ax.set_xlabel("Year"); ax.set_ylabel("Count")
    ax.set_title("Ch01 residual: guideline churn outpaces local absolute reappraisal", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch01_guideline_churn.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    modes = ["Linear\nread", "Question\nfirst", "ARR\nfirst", "Bias\nfirst"]
    time_to_decision = [25, 18, 12, 15]
    quality = [0.5, 0.7, 0.85, 0.8]
    x = np.arange(4)
    ax.bar(x - 0.2, time_to_decision, width=0.4, color=GOLD, edgecolor=INDIGO, label="Minutes to decision")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, quality, width=0.4, color=TEAL, edgecolor=INDIGO, label="Decision quality")
    ax.set_xticks(x); ax.set_xticklabels(modes, fontsize=8)
    ax.set_ylabel("Minutes"); ax2.set_ylabel("Quality (0–1)")
    ax.set_title("Ch02 residual: ARR-first reading is fastest path to absolute decisions", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch02_arr_first.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pop = ["Trial P", "Local P′", "Elderly\nsubset", "Mild\nNIHSS"]
    pico_match = [1.0, 0.7, 0.4, 0.55]
    arr_applicable = [5.0, 3.5, 1.5, 2.0]
    x = np.arange(4)
    ax.bar(x - 0.2, [p * 100 for p in pico_match], width=0.4, color=GOLD, edgecolor=INDIGO, label="PICO match %")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, arr_applicable, width=0.4, color=TEAL, edgecolor=INDIGO, label="Applicable absolute ARR pp")
    ax.set_xticks(x); ax.set_xticklabels(pop, fontsize=8)
    ax.set_ylabel("PICO match %"); ax2.set_ylabel("Absolute ARR pp")
    ax.set_title("Ch03 residual: PICO mismatch shrinks applicable absolute benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper right", fontsize=8); ax2.legend(loc="center right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch03_pico_match.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # internal vs external validity absolute tradeoff sketch
    restrict = np.linspace(0, 1, 40)
    internal = 0.5 + 0.45 * restrict
    external = 0.95 - 0.7 * restrict
    ax.plot(restrict, internal, color=TEAL, lw=2.4, label="Internal validity (teaching)")
    ax.plot(restrict, external, color=CORAL, lw=2.4, label="External absolute transportability")
    ax.set_xlabel("Eligibility restriction intensity"); ax.set_ylabel("Score (0–1)")
    ax.set_title("Ch04 residual: tighter eligibility buys internal validity, costs absolute transport", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch04_int_ext.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # DAG: open backdoor absolute bias
    states = ["Open\nbackdoor", "Close\nvia M", "Close\nvia Z", "Overadjust\ncollider"]
    bias = [4.0, 0.5, 0.3, 3.5]
    ax.bar(states, bias, color=[CORAL, TEAL, TEAL, CORAL], edgecolor=INDIGO)
    ax.set_ylabel("|Absolute ARR bias| pp")
    ax.set_title("Ch05 residual: backdoor closure is judged by residual absolute bias", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch05_backdoor_close.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # crossover dilution absolute ITT
    cross = np.linspace(0, 0.4, 40)
    true_arr = 6.0
    itt = true_arr * (1 - cross)
    ax.plot(cross * 100, itt, color=INDIGO, lw=2.5, label="ITT absolute ARR")
    ax.axhline(true_arr, color=TEAL, ls="--", label="Per-protocol true ARR")
    ax.set_xlabel("Crossover %"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch06 residual: crossover dilutes absolute ITT effects predictably", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch06_crossover.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    designs = ["New-user", "Prevalent\nuser", "Active\ncomp", "Self-\ncontrol"]
    abs_bias = [1.0, 4.5, 1.5, 2.0]
    ax.bar(designs, abs_bias, color=[TEAL, CORAL, GOLD, GRAY], edgecolor=INDIGO)
    ax.set_ylabel("|Absolute residual bias| pp (teaching)")
    ax.set_title("Ch07 residual: design choice sets absolute confounding residual", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch07_designs.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # ROC vs absolute net
    fpr = np.linspace(0, 1, 50)
    tpr = fpr ** 0.4
    # net at prevalence 0.1
    prev = 0.1
    nb = tpr * prev - fpr * (1 - prev) * (0.2 / 0.8)
    ax.plot(fpr, tpr, color=GOLD, lw=2.2, label="ROC (TPR vs FPR)")
    ax2 = ax.twinx()
    ax2.plot(fpr, nb, color=TEAL, lw=2.4, label="Absolute net benefit sketch")
    ax.set_xlabel("FPR"); ax.set_ylabel("TPR"); ax2.set_ylabel("Absolute net benefit")
    ax.set_title("Ch08 residual: ROC curves omit absolute prevalence-weighted net benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="lower right", fontsize=8); ax2.legend(loc="center right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch08_roc_nb.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # optimism-corrected absolute performance
    metrics = ["Apparent\nAUROC", "Optimism\ncorr AUROC", "Apparent\ncal err", "Corr\ncal err"]
    vals = [0.88, 0.79, 1.0, 3.5]
    colors = [GOLD, TEAL, GOLD, CORAL]
    ax.bar(metrics, vals, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Metric value (mixed units)")
    ax.set_title("Ch09 residual: pred≠cause — optimism correction hits absolute calibration hard", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch09_optimism.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # GRADE domain downgrades absolute certainty
    domains = ["Risk of\nbias", "Inconsist.", "Indirect", "Imprecision", "Pub bias"]
    downgrade = [1, 1, 0, 2, 1]
    ax.bar(domains, downgrade, color=CORAL, edgecolor=INDIGO)
    ax.set_ylabel("Absolute GRADE levels lost")
    ax.set_title("Ch10 residual: imprecision is absolute CI width on the effect scale", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 3); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch10_grade_domains.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # utility-weighted mRS absolute gain
    mrs = np.arange(0, 6)
    d_prop = np.array([0.06, 0.04, 0.02, -0.04, -0.05, -0.03])
    util = np.array([1.0, 0.91, 0.76, 0.65, 0.33, 0.0])
    contrib = d_prop * util
    ax.bar(mrs, d_prop, color=TEAL, edgecolor=INDIGO, alpha=0.5, label="Δ absolute probability")
    ax.plot(mrs, contrib, "o-", color=INDIGO, lw=2.3, label="Utility-weighted absolute contrib")
    ax.axhline(0, color=SLATE)
    ax.set_xlabel("mRS"); ax.set_ylabel("Absolute change")
    ax.set_title("Ch11 residual: ordinal benefit is utility-weighted absolute probability shift", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch11_utility_shift.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # ARR vs RR presentation effect on uptake
    frame = ["RR 25%\nrelative", "ARR 2pp\nabsolute", "NNT 50", "Natural\nfreq 2/100"]
    uptake = [0.75, 0.45, 0.40, 0.42]
    ax.bar(frame, uptake, color=[CORAL, TEAL, TEAL, TEAL], edgecolor=INDIGO)
    ax.set_ylabel("Hypothetical absolute treatment uptake")
    ax.set_title("Ch12 residual: relative framing inflates uptake vs absolute/NNT frames", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch12_framing.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # pre-spec vs post-hoc absolute claim credibility
    claim_type = ["Pre-spec\nprimary", "Pre-spec\nsecondary", "Post-hoc\nsubgroup", "Data-\ndredged"]
    credibility = [0.9, 0.7, 0.35, 0.15]
    ax.bar(claim_type, credibility, color=[TEAL, GOLD, CORAL, CORAL], edgecolor=INDIGO)
    ax.set_ylabel("Credibility weight for absolute claim")
    ax.set_title("Ch13 residual: post-hoc absolute effects need severe credibility discounts", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.1); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch13_prespec.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # silent failure: accuracy stable, absolute harm rises
    months = np.arange(0, 10)
    acc = 0.90 - 0.005 * months
    harm = 0.02 + 0.008 * months
    ax.plot(months, acc, "o-", color=GOLD, lw=2.2, label="Accuracy")
    ax2 = ax.twinx()
    ax2.plot(months, harm, "s-", color=CORAL, lw=2.3, label="Absolute avoidable harm rate")
    ax.set_xlabel("Months post-deploy"); ax.set_ylabel("Accuracy"); ax2.set_ylabel("Absolute harm rate")
    ax.set_title("Ch14 residual: pred≠cause — accuracy can mask rising absolute harm", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle47_swarm_ch14_silent_fail.png")


def main():
    print("Cycle-47 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
