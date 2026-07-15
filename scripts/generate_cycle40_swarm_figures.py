#!/usr/bin/env python3
"""CRIT-APP Cycle-40 densify: ch15–28 raise uniform floor to 20. Agg indigo. ARR/NNT. pred≠cause."""
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


def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sessions = np.arange(1, 9)
    without = np.array([2, 2, 3, 2, 3, 2, 2, 3])
    with_board = np.array([1, 2, 3, 4, 5, 6, 6, 7])
    ax.plot(sessions, without, "s--", color=CORAL, lw=2.2, label="ARR cards completed (no board)")
    ax.plot(sessions, with_board, "o-", color=TEAL, lw=2.3, label="ARR cards completed (flip-board)")
    ax.set_xlabel("JC session"); ax.set_ylabel("Count")
    ax.set_title("Ch15 residual: visible absolute-risk board raises appraisal completion", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch15_flipboard.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    items = ["PICO\nclear?", "ARR\nshown?", "Bias\nmapped?", "Spin\nabsent?", "Action\ncoded?"]
    pre = [0.4, 0.2, 0.3, 0.3, 0.2]
    post = [0.9, 0.85, 0.8, 0.75, 0.8]
    x = np.arange(5); w = 0.35
    ax.bar(x - w/2, pre, width=w, color=CORAL, edgecolor=INDIGO, label="Pre-mortem checklist pass rate")
    ax.bar(x + w/2, post, width=w, color=TEAL, edgecolor=INDIGO, label="After autopsy training")
    ax.set_xticks(x); ax.set_xticklabels(items, fontsize=8)
    ax.set_ylabel("Absolute pass fraction")
    ax.set_title("Ch16 residual: pre-mortem absolute checklist lifts autopsy quality", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 1.15); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch16_premortem.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # prevalence vs incidence absolute
    labels = ["Point\nprevalence", "Period\nprevalence", "Incidence\nproportion", "Incidence\ndensity"]
    vals = [8.0, 12.0, 3.5, 4.2]
    units = ["%", "%", "%/y", "/100py"]
    ax.bar(labels, vals, color=[GRAY, GOLD, TEAL, INDIGO], edgecolor=SLATE)
    for i, (v, u) in enumerate(zip(vals, units)):
        ax.text(i, v + 0.3, u, ha="center", fontsize=8, color=SLATE)
    ax.set_ylabel("Absolute frequency measure")
    ax.set_title("Ch17 residual: prevalence ≠ incidence — absolute units must match the claim", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch17_prev_inc.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    hills = ["Strength\n(ARR)", "Consistency", "Temporality", "Dose-\nresponse", "Experiment", "Analogy"]
    score = [0.9, 0.6, 0.85, 0.5, 0.95, 0.3]
    colors = [TEAL if s >= 0.7 else (GOLD if s >= 0.5 else CORAL) for s in score]
    ax.barh(hills, score, color=colors, edgecolor=INDIGO)
    ax.axvline(0.7, color=SLATE, ls="--", lw=1.2)
    ax.set_xlabel("Teaching weight (absolute-first causal checklist)")
    ax.set_title("Ch18 residual: causal checklists privilege absolute strength + experiment", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_xlim(0, 1.1); ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch18_hill_abs.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(-2, 10, 200)
    # compatibility curve peaking at 4
    compat = np.exp(-0.5 * ((arr - 4) / 1.8) ** 2)
    ax.plot(arr, compat, color=INDIGO, lw=2.5)
    ax.fill_between(arr, compat, where=(arr > 0), color=TEAL, alpha=0.2, label="ARR>0 region")
    ax.axvline(0, color=CORAL, ls="--", label="Null ARR")
    ax.axvline(4, color=GOLD, ls=":", label="Point estimate")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("Compatibility density (teaching)")
    ax.set_title("Ch19 residual: reason with absolute compatibility, not binary p", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch19_compat.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    # time-varying treatment absolute risk
    risk_static = 1 - np.exp(-0.03 * t)
    risk_tv = 1 - np.exp(-0.02 * t - 0.01 * np.maximum(t - 6, 0))
    ax.plot(t, risk_static * 100, color=GRAY, lw=2.2, label="Static exposure model")
    ax.plot(t, risk_tv * 100, color=TEAL, lw=2.4, label="Time-varying absolute risk")
    ax.axvline(6, color=GOLD, ls="--", label="Treatment start")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative risk %")
    ax.set_title("Ch20 residual: time-varying exposure needs absolute risk curves", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch20_timevar.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # standardization weights
    strata = ["S1", "S2", "S3", "S4"]
    crude = [6, 6, 6, 6]
    std = [3, 5, 8, 12]
    weights = [0.4, 0.3, 0.2, 0.1]
    std_overall = sum(s * w for s, w in zip(std, weights))
    crude_overall = 6
    x = np.arange(4)
    ax.bar(x - 0.2, crude, width=0.4, color=GRAY, edgecolor=INDIGO, label="Crude stratum ARR")
    ax.bar(x + 0.2, std, width=0.4, color=TEAL, edgecolor=INDIGO, label="Stratum-specific ARR")
    ax.axhline(std_overall, color=GOLD, ls="--", lw=2, label=f"Standardized ARR={std_overall:.1f}pp")
    ax.axhline(crude_overall, color=CORAL, ls=":", label=f"Crude={crude_overall}pp")
    ax.set_xticks(x); ax.set_xticklabels(strata)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch21 residual: standardization is weighted absolute risk arithmetic", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch21_std.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    intensity = np.linspace(0, 1, 50)
    benefit = 2 * intensity / (1 + intensity)
    harm_overdx = 0.5 * intensity ** 2 * 20
    net = benefit - harm_overdx * 0.05
    ax.plot(intensity, benefit, color=TEAL, lw=2.3, label="Absolute mortality benefit (pp)")
    ax.plot(intensity, harm_overdx * 0.05, color=CORAL, lw=2.3, label="Absolute overdx harm (scaled)")
    ax.plot(intensity, net, color=INDIGO, lw=2.5, ls="--", label="Net absolute")
    ax.set_xlabel("Screening intensity"); ax.set_ylabel("Absolute pp (teaching scale)")
    ax.set_title("Ch22 residual: overdiagnosis can dominate absolute net screening benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch22_net_screen.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # dual process override
    modes = ["System-1\nalone", "S1+absolute\nchecklist", "S2 full\nworkup"]
    err = [18, 7, 4]
    time = [1, 3, 12]
    x = np.arange(3)
    ax.bar(x - 0.2, err, width=0.4, color=CORAL, edgecolor=INDIGO, label="Absolute probability error (pp)")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, time, width=0.4, color=TEAL, edgecolor=INDIGO, alpha=0.7, label="Minutes")
    ax.set_xticks(x); ax.set_xticklabels(modes, fontsize=8)
    ax.set_ylabel("Error pp"); ax2.set_ylabel("Minutes")
    ax.set_title("Ch23 residual: absolute checklists cheaply cut dual-process error", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch23_dualprocess.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    years = np.array([0.25, 0.5, 1, 2, 3, 5])
    benefit = np.array([0.5, 1.2, 2.5, 4.0, 5.0, 6.0])
    harm = np.array([1.5, 1.8, 2.0, 2.2, 2.5, 3.0])
    ax.plot(years, benefit, "o-", color=TEAL, lw=2.4, label="Absolute benefit")
    ax.plot(years, harm, "s-", color=CORAL, lw=2.2, label="Absolute harm")
    ax.plot(years, benefit - harm, "^-", color=INDIGO, lw=2.4, label="Net absolute")
    ax.axhline(0, color=GRAY)
    ax.set_xlabel("Horizon (years)"); ax.set_ylabel("Absolute pp")
    ax.set_title("Ch24 residual: benefit−harm absolute curves can cross over time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch24_benefit_harm.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # NRI-style absolute reclassification
    cats = ["Up among\nevents", "Down among\nevents", "Up among\nnonevents", "Down among\nnonevents"]
    n = [40, 10, 25, 50]
    colors = [TEAL, CORAL, CORAL, TEAL]
    ax.bar(cats, n, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Absolute count reclassified")
    ax.set_title("Ch25 residual: reclassification is absolute counts, not only NRI index", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch25_reclass.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    threshold = np.linspace(0.05, 0.50, 40)
    # decision curve net benefit
    nb_model = 0.08 - 0.15 * (threshold - 0.1) ** 2
    nb_all = 0.12 - threshold
    nb_none = np.zeros_like(threshold)
    ax.plot(threshold, nb_model, color=TEAL, lw=2.5, label="CPR absolute net benefit")
    ax.plot(threshold, nb_all, color=GOLD, lw=2.2, label="Treat all")
    ax.plot(threshold, nb_none, color=GRAY, lw=2, label="Treat none")
    ax.axhline(0, color=SLATE, ls=":")
    ax.set_xlabel("Absolute risk threshold"); ax.set_ylabel("Net benefit")
    ax.set_title("Ch26 residual: CPR value is absolute decision-curve net benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch26_dca.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # missingness absolute bias bound
    miss = np.linspace(0, 0.40, 40)
    arr_point = 5 * np.ones_like(miss)
    bound = 5 + 20 * miss  # worst-case absolute bias growth
    lo = 5 - 20 * miss
    ax.plot(miss * 100, arr_point, color=INDIGO, lw=2.3, label="Complete-case ARR")
    ax.fill_between(miss * 100, lo, bound, color=CORAL, alpha=0.2, label="Absolute bias bound")
    ax.set_xlabel("Missing outcome %"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch27 residual: missing data widens absolute ARR uncertainty bounds", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch27_missing_bound.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # SDM board: absolute risks for options
    options = ["No\nlytics", "IV\nlytics", "EVT", "Lytics+\nEVT"]
    good = [22, 30, 38, 42]
    sich = [1, 4, 3, 5]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, good, width=w, color=TEAL, edgecolor=INDIGO, label="Good outcome %")
    ax.bar(x + w/2, sich, width=w, color=CORAL, edgecolor=INDIGO, label="sICH %")
    ax.set_xticks(x); ax.set_xticklabels(options)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch28 residual: shared decisions need absolute benefit and harm side-by-side", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle40_swarm_ch28_sdm.png")


def main():
    print("Cycle-40 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
