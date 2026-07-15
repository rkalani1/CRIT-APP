#!/usr/bin/env python3
"""CRIT-APP Cycle-39 densify: ch01–14 toward uniform floor 20. Agg indigo. ARR/NNT. pred≠cause."""
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
    months = np.arange(1, 13)
    pub = 10 + 0.8 * months
    local_adopt = np.minimum(pub * 0.4, 3 + 0.15 * months)
    ax.plot(months, pub, "o-", color=GRAY, lw=2, label="Papers claiming practice change")
    ax.plot(months, local_adopt, "s-", color=TEAL, lw=2.3, label="Local absolute ARR-vetted adopts")
    ax.fill_between(months, local_adopt, pub, color=CORAL, alpha=0.15, label="Uptake without absolute vetting")
    ax.set_xlabel("Month"); ax.set_ylabel("Count")
    ax.set_title("Ch01 residual: evidence velocity outruns absolute appraisal capacity", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch01_velocity.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    stages = ["Skim abstract", "Find ARR", "Bias screen", "Stop or deep"]
    p_continue = [1.0, 0.55, 0.30, 0.15]
    ax.plot(stages, p_continue, "o-", color=INDIGO, lw=2.5, ms=10)
    ax.fill_between(range(4), p_continue, color=TEAL, alpha=0.15)
    ax.set_ylabel("Fraction of papers still in hand")
    ax.set_title("Ch02 residual: absolute stop-rules prevent sunk-time on empty papers", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.15); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch02_stoprules.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    estimands = ["Treatment\npolicy", "While on\ntreatment", "Hypothetical\nno ICE", "Principal\nstratum"]
    arr = [3.0, 4.5, 5.2, 2.1]
    ax.bar(estimands, arr, color=[TEAL, GOLD, CORAL, INDIGO], edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR (pp) same trial")
    ax.set_title("Ch03 residual: intercurrent-event estimands rewrite absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch03_ice_estimand.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # transportability: trial ARR vs target absolute
    pops = ["Trial", "Target\nyoung", "Target\nold", "Target\nsevere"]
    arr = [5.0, 3.0, 7.5, 9.0]
    ax.bar(pops, arr, color=[INDIGO, TEAL, GOLD, CORAL], edgecolor=SLATE)
    ax.axhline(5.0, color=GRAY, ls="--", label="Trial ARR")
    ax.set_ylabel("Transported absolute ARR (pp)")
    ax.set_title("Ch04 residual: external validity is absolute transport, not vibes", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch04_transport.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # E-value style: how strong unmeasured confounder must be to explain ARR
    arr_obs = np.linspace(1, 8, 40)
    # simplified: RR_ud needed roughly scales
    strength = 1 + 12 / (arr_obs + 1)
    ax.plot(arr_obs, strength, color=CORAL, lw=2.5)
    ax.set_xlabel("Observed absolute ARR (pp)")
    ax.set_ylabel("Confounder strength needed to nullify (teaching units)")
    ax.set_title("Ch05 residual: small absolute ARR is fragile to unmeasured confounding", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch05_unmeasured.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    concealment = ["Adequate", "Unclear", "Inadequate"]
    inflated = [0, 1.5, 3.2]  # absolute ARR inflation
    true_arr = [4, 4, 4]
    ax.bar(concealment, true_arr, color=TEAL, edgecolor=INDIGO, label="True ARR")
    ax.bar(concealment, inflated, bottom=true_arr, color=CORAL, edgecolor=INDIGO, label="Bias inflation")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch06 residual: allocation concealment failure inflates absolute effects", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch06_conceal.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 12, 50)
    # immortal time: misclassified exposed person-time
    true_rate_exp = 2.0 * np.ones_like(t)
    biased_rate = 2.0 * np.ones_like(t)
    biased_rate[t < 3] = 0.3  # immortal window looks protected
    ax.plot(t, true_rate_exp, color=TEAL, lw=2.4, label="True absolute hazard (exposed)")
    ax.plot(t, biased_rate, color=CORAL, lw=2.4, ls="--", label="With immortal-time misclassification")
    ax.axvspan(0, 3, color=GOLD, alpha=0.15, label="Immortal window")
    ax.set_xlabel("Months from cohort entry"); ax.set_ylabel("Absolute event rate /100 py")
    ax.set_title("Ch07 residual: immortal time biases absolute rates downward", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch07_immortal.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # treat threshold after test
    post = np.linspace(0, 100, 50)
    treat = (post >= 30).astype(float) * 100
    ax.plot(post, treat, color=INDIGO, lw=2.5, label="Treat if post-test ≥30%")
    ax.axvline(30, color=GOLD, ls="--", label="Absolute action threshold")
    ax.set_xlabel("Post-test absolute probability %")
    ax.set_ylabel("Treat decision (0/100)")
    ax.set_title("Ch08 residual: tests inform only via absolute post-test thresholds", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch08_threshold.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # overfitting: AUROC train vs absolute calibration test
    complexity = np.arange(1, 11)
    auc_train = 0.70 + 0.03 * complexity
    auc_test = 0.70 + 0.03 * complexity - 0.008 * complexity ** 1.5
    cal_err = 0.02 * complexity ** 1.3
    ax.plot(complexity, auc_train, "o-", color=GRAY, label="Train AUROC")
    ax.plot(complexity, auc_test, "s-", color=TEAL, label="Test AUROC")
    ax2 = ax.twinx()
    ax2.plot(complexity, cal_err, "^-", color=CORAL, label="Absolute calibration error")
    ax.set_xlabel("Model complexity"); ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute cal error")
    ax.set_title("Ch09 residual: pred≠cause — overfit models lose absolute calibration first", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch09_overfit.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # funnel of absolute ARR
    np.random.seed(39)
    n = np.array([40, 60, 80, 100, 150, 200, 300, 400, 500, 600, 800, 1000])
    se = 15 / np.sqrt(n)
    arr = 4 + se * np.random.randn(len(n))
    ax.scatter(arr, n, c=TEAL, edgecolors=INDIGO, s=60, zorder=3)
    ax.axvline(4, color=GOLD, ls="--", label="True ARR=4pp")
    # missing small null studies (publication bias sketch)
    ax.scatter([1, 0, -1], [50, 70, 90], c=CORAL, marker="x", s=80, label="Possible missing nulls")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("Study n")
    ax.set_title("Ch10 residual: publication bias distorts pooled absolute effects", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch10_funnel.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    # CIF stroke vs death competing
    cif_stroke = 1 - np.exp(-0.04 * t)
    cif_death = 1 - np.exp(-0.025 * t)
    km_naive = 1 - np.exp(-0.04 * t) * 1.15  # inflated
    km_naive = np.clip(km_naive, 0, 0.95)
    ax.plot(t, cif_stroke * 100, color=TEAL, lw=2.4, label="CIF stroke (competing risk)")
    ax.plot(t, cif_death * 100, color=CORAL, lw=2.2, label="CIF death")
    ax.plot(t, km_naive * 100, color=GRAY, ls="--", lw=2, label="1−KM naive (overstates)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch11 residual: competing risks require absolute CIF, not naive 1−KM", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch11_cif.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mid = np.linspace(1, 10, 40)
    # patient-important absolute difference threshold
    ax.axhspan(0, 2, color=CORAL, alpha=0.15, label="Below MID — ignore statistically significant RR")
    ax.axhspan(2, 10, color=TEAL, alpha=0.12, label="Above MID — clinically discuss")
    ax.plot(mid, mid, color=INDIGO, lw=2)
    ax.axhline(2, color=GOLD, ls="--", lw=2, label="MID=2pp absolute")
    ax.set_xlabel("Observed absolute ARR (pp)"); ax.set_ylabel("Same scale")
    ax.set_title("Ch12 residual: MID is an absolute threshold, not a p-value", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left"); ax.set_xlim(0, 10); ax.set_ylim(0, 10)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch12_mid.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # interaction on absolute scale
    groups = ["A−", "A+"]
    arr_b0 = [3, 3.2]
    arr_b1 = [3.1, 7.5]
    x = np.arange(2); w = 0.35
    ax.bar(x - w/2, arr_b0, width=w, color=GRAY, edgecolor=INDIGO, label="Modifier− ARR")
    ax.bar(x + w/2, arr_b1, width=w, color=TEAL, edgecolor=INDIGO, label="Modifier+ ARR")
    ax.set_xticks(x); ax.set_xticklabels(groups)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch13 residual: claim HTE on absolute interaction, not cherry RR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch13_abs_interact.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # dataset shift absolute harm
    time = np.arange(0, 12)
    auroc = 0.85 - 0.01 * time
    net_benefit = 0.12 - 0.012 * time
    ax.plot(time, auroc, "o-", color=GOLD, lw=2.2, label="AUROC")
    ax2 = ax.twinx()
    ax2.plot(time, net_benefit, "s-", color=CORAL, lw=2.3, label="Absolute net benefit")
    ax2.axhline(0, color=INDIGO, ls="--")
    ax.set_xlabel("Months post-deployment"); ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute net benefit")
    ax.set_title("Ch14 residual: dataset shift can erase absolute net benefit first", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle39_swarm_ch14_shift.png")


def main():
    print("Cycle-39 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
