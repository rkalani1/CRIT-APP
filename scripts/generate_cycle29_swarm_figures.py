#!/usr/bin/env python3
"""CRIT-APP Cycle-29 densify: floor-14 → toward 15 (wave A, ch01–14).

14 original scientific Agg indigo plots. ARR/NNT; pred≠cause.
cycle29_swarm_* only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = (
    "#283593",
    "#00695C",
    "#F9A825",
    "#C62828",
    "#37474F",
    "#FFFFFF",
)
GREEN, BLUE, ORANGE, PURPLE, GRAY = (
    "#2E7D32",
    "#1565C0",
    "#EF6C00",
    "#6A1B9A",
    "#90A4AE",
)


def _save(fig, name: str):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    modes = ["Press\nRRR", "Abstract\nonly", "ARR+\nNNT", "ARR+NNT\n+harm"]
    overtx = [18, 12, 4, 2]
    undertx = [2, 3, 3, 2]
    x = np.arange(4)
    ax.bar(x, overtx, color=CORAL, edgecolor=INDIGO, label="Overtreatment /100")
    ax.bar(x, undertx, bottom=overtx, color=GOLD, edgecolor=INDIGO, label="Undertreatment /100")
    ax.set_xticks(x)
    ax.set_xticklabels(modes, fontsize=9)
    ax.set_ylabel("Absolute misallocation per 100 decisions")
    ax.set_title(
        "Why appraisal matters: absolute misallocation falls when ARR/NNT+harm are forced",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch01_misalloc.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    order = np.array([1, 2, 3, 4, 5])
    labels = ["Title", "Abstract", "Tables", "Methods\nbias", "Action"]
    # cumulative true-positive pathway decisions
    good = np.array([10, 25, 70, 88, 95])
    bad = np.array([40, 65, 70, 72, 74])  # title/abstract heavy
    ax.plot(order, good, "o-", color=TEAL, lw=2.4, label="Tables-first absolute path")
    ax.plot(order, bad, "s--", color=CORAL, lw=2.2, label="Title/abstract-first path")
    ax.set_xticks(order)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Cumulative absolute decision accuracy (%)")
    ax.set_title(
        "Time-pressure residual: tables/ARR first beats abstract-first accuracy",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch02_read_order.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 90, 100)
    # different index times shift absolute risk
    risk_symptom = 1 - np.exp(-0.01 * t)
    risk_admission = 1 - np.exp(-0.01 * np.maximum(t - 5, 0))
    risk_randomize = 1 - np.exp(-0.01 * np.maximum(t - 12, 0))
    ax.plot(t, risk_symptom * 100, color=CORAL, lw=2.2, label="Index: symptom onset")
    ax.plot(t, risk_admission * 100, color=GOLD, lw=2.2, label="Index: admission")
    ax.plot(t, risk_randomize * 100, color=TEAL, lw=2.4, label="Index: randomization")
    ax.set_xlabel("Days from calendar t0")
    ax.set_ylabel("Cumulative absolute risk %")
    ax.set_title(
        "Estimand residual: index-time choice moves absolute risk curves",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch03_index_time.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    domains = ["Selection", "Performance", "Detection", "Attrition", "Reporting"]
    risk_score = [3, 2, 2, 3, 1]
    arr_bias = [4.0, 2.5, 1.5, 3.0, 2.0]
    x = np.arange(5)
    ax.bar(x - 0.2, risk_score, width=0.4, color=GOLD, edgecolor=INDIGO, label="RoB domain score")
    ax.bar(x + 0.2, arr_bias, width=0.4, color=CORAL, edgecolor=INDIGO, label="Absolute ARR bias pp")
    ax.set_xticks(x)
    ax.set_xticklabels(domains, fontsize=9)
    ax.set_title(
        "Bias residual: domain risk scores should map to absolute effect distortion",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch04_rob_abs.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # simple DAG-inspired backdoor magnitude
    conf_prev = np.linspace(0.05, 0.5, 60)
    conf_effect_y = 0.25
    conf_effect_a = 0.40
    bias = conf_prev * conf_effect_y * conf_effect_a * 100  # rough teaching
    ax.plot(conf_prev * 100, bias, color=INDIGO, lw=2.5)
    ax.set_xlabel("Confounder prevalence (%)")
    ax.set_ylabel("Open-backdoor absolute bias (pp teaching)")
    ax.set_title(
        "DAG residual: confounder prevalence scales absolute open-backdoor bias",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch05_conf_prevalence.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # cumulative enrollment and interim ARR
    n = np.array([100, 200, 300, 400, 500, 600])
    arr = np.array([9.0, 7.2, 5.5, 4.8, 4.5, 4.3])
    ax.plot(n, arr, "o-", color=TEAL, lw=2.4, ms=8)
    ax.axhline(4.0, color=GOLD, ls="--", lw=1.3, label="Design alternative ARR")
    ax.fill_between(n, arr, 4.0, where=arr > 4.0, color=CORAL, alpha=0.12)
    ax.set_xlabel("Accumulated randomized n")
    ax.set_ylabel("Observed absolute ARR (pp)")
    ax.set_title(
        "RCT residual: early absolute ARR often exaggerates before regression to design effect",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch06_early_arr.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # immortal time: person-time misallocation invents ARR
    labs = ["Naive\nimmortal", "Exclude\nimmortal", "Time-varying\nexposure", "Landmark\nanalysis"]
    bias = [6.5, 2.0, 0.8, 0.5]
    ax.bar(range(4), bias, color=[CORAL, GOLD, TEAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute survival bias (pp teaching)")
    ax.set_title(
        "Observational residual: immortal time invents absolute benefit",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch07_immortal_time.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prev = np.linspace(0.01, 0.5, 100)
    se, sp = 0.90, 0.85
    ppv = (se * prev) / (se * prev + (1 - sp) * (1 - prev))
    npv = (sp * (1 - prev)) / (sp * (1 - prev) + (1 - se) * prev)
    ax.plot(prev * 100, ppv * 100, color=TEAL, lw=2.4, label="PPV %")
    ax.plot(prev * 100, npv * 100, color=INDIGO, lw=2.4, label="NPV %")
    ax.set_xlabel("Prevalence (%)")
    ax.set_ylabel("Absolute predictive value (%)")
    ax.set_title(
        "Diagnostic residual: Se/Sp fixed — absolute PPV/NPV swing with prevalence",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch08_ppv_npv.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # reclassification net benefit teaching
    cats = ["Up into\ntreat", "Down out\nof treat", "Net reclass.\n(events)", "Net reclass.\n(nonevents)"]
    vals = [8, 5, 3, -2]
    cols = [TEAL, GOLD, INDIGO, CORAL]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks(range(4))
    ax.set_xticklabels(cats, fontsize=8.5)
    ax.set_ylabel("Absolute reclassification count /100")
    ax.set_title(
        "Prognosis residual: reclassification must be event-aware absolute counts (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch09_nri_abs.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # funnel of study ARR
    rng = np.random.default_rng(3)
    n_studies = 24
    se = rng.uniform(0.5, 3.5, n_studies)
    arr = 3.0 + rng.normal(0, se * 0.6, n_studies)
    ax.scatter(arr, se, s=60, color=INDIGO, edgecolors=WHITE, alpha=0.85)
    ax.axvline(3.0, color=TEAL, ls="--", lw=1.5, label="Pooled ARR 3 pp")
    ax.invert_yaxis()
    ax.set_xlabel("Study absolute ARR (pp)")
    ax.set_ylabel("SE of ARR (pp)")
    ax.set_title(
        "Meta residual: funnel of absolute effects — asymmetry flags small-study bias",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch10_funnel_arr.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 365, 120)
    # KM ignores competing death
    km = 1 - np.exp(-0.0012 * t)
    cif = 1 - np.exp(-0.0012 * t) * np.exp(-0.0008 * t)  # rough competing
    # better: Fine-Gray style lower than 1-KM when competing
    cif = (1 - np.exp(-(0.0012 + 0.0008) * t)) * (0.0012 / (0.0012 + 0.0008))
    ax.plot(t, km * 100, color=CORAL, lw=2.3, label="1−KM (ignores competing)")
    ax.plot(t, cif * 100, color=TEAL, lw=2.4, label="Cause-specific CIF")
    ax.set_xlabel("Days")
    ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title(
        "Outcomes residual: 1−KM overstates absolute event risk under competing death",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch11_km_vs_cif.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cer = np.array([2, 5, 10, 15, 25, 40], dtype=float)
    rrr = 0.20
    arr = cer * rrr
    nnt = 100 / arr
    ax.plot(cer, arr, "o-", color=TEAL, lw=2.4, ms=8, label="ARR pp")
    ax2 = ax.twinx()
    ax2.plot(cer, nnt, "s--", color=CORAL, lw=2.2, ms=8, label="NNT")
    ax.set_xlabel("Control event rate (%)")
    ax.set_ylabel("ARR (pp)", color=TEAL)
    ax2.set_ylabel("NNT", color=CORAL)
    ax.tick_params(axis="y", labelcolor=TEAL)
    ax2.tick_params(axis="y", labelcolor=CORAL)
    ax.set_title(
        "Effect-size residual: same RRR → different absolute ARR/NNT across CER",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, fontsize=8, loc="center right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch12_cer_ladder.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # continuous HTE: absolute benefit vs baseline risk
    risk = np.linspace(1, 40, 80)
    arr = 0.25 * risk  # linear absolute HTE
    ax.plot(risk, arr, color=TEAL, lw=2.5, label="Absolute ARR(risk)")
    ax.axhline(np.mean(arr), color=GOLD, ls="--", lw=1.4, label="Average ARR (one-size)")
    ax.fill_between(risk, arr, np.mean(arr), alpha=0.12, color=INDIGO)
    ax.set_xlabel("Baseline risk (%)")
    ax.set_ylabel("Absolute treatment benefit (pp)")
    ax.set_title(
        "HTE residual: one average ARR hides continuous absolute benefit curve",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch13_continuous_hte.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # alert fatigue: alerts vs true absolute outcomes prevented
    alerts = np.array([10, 50, 100, 200, 400, 800])
    prevented = 2 * (1 - np.exp(-alerts / 120))  # saturates
    ppv_alert = prevented / (alerts / 100)  # messy teaching
    ax.plot(alerts, prevented, "o-", color=TEAL, lw=2.4, label="Absolute outcomes prevented /100 pts")
    ax2 = ax.twinx()
    ax2.plot(alerts, 100 * prevented / (alerts / 10), "s--", color=CORAL, lw=2.0, label="Yield per 10 alerts (scaled)")
    ax.set_xlabel("Alerts fired per 100 patients")
    ax.set_ylabel("Absolute outcomes prevented", color=TEAL)
    ax2.set_ylabel("Scaled yield", color=CORAL)
    ax.tick_params(axis="y", labelcolor=TEAL)
    ax2.tick_params(axis="y", labelcolor=CORAL)
    ax.set_title(
        "AI residual: more alerts ≠ proportional absolute outcome gain (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, fontsize=8, loc="lower right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle29_swarm_ch14_alert_fatigue.png")


def main():
    print("Cycle-29 →", OUT)
    for fn in [
        fig_ch01,
        fig_ch02,
        fig_ch03,
        fig_ch04,
        fig_ch05,
        fig_ch06,
        fig_ch07,
        fig_ch08,
        fig_ch09,
        fig_ch10,
        fig_ch11,
        fig_ch12,
        fig_ch13,
        fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
