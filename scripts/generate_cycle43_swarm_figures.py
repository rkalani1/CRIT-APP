#!/usr/bin/env python3
"""CRIT-APP Cycle-43 densify: ch01–14 toward uniform floor 22. Agg indigo. ARR/NNT. pred≠cause."""
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
    gens = np.arange(0, 6)
    cites = 1 * (2.2 ** gens)
    arr_vetted = 1 * (1.15 ** gens)
    ax.semilogy(gens, cites, "o-", color=CORAL, lw=2.3, label="Citation cascade (no ARR check)")
    ax.semilogy(gens, arr_vetted, "s-", color=TEAL, lw=2.3, label="ARR-vetted uptake")
    ax.set_xlabel("Citation generation"); ax.set_ylabel("Relative count (log)")
    ax.set_title("Ch01 residual: citation cascades amplify claims without absolute vetting", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, which="both", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch01_cascade.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    load = np.array([1, 2, 3, 4, 5])
    retention = np.array([0.9, 0.75, 0.55, 0.35, 0.22])
    arr_found = np.array([0.85, 0.70, 0.50, 0.30, 0.15])
    ax.plot(load, retention, "o-", color=GRAY, lw=2.2, label="Detail retention")
    ax.plot(load, arr_found, "s-", color=TEAL, lw=2.4, label="ARR extracted correctly")
    ax.set_xlabel("Simultaneous papers in cognitive load"); ax.set_ylabel("Absolute fraction")
    ax.set_title("Ch02 residual: cognitive load collapses absolute-risk extraction first", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch02_load.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strata = ["Always\ntakers", "Compliers", "Never\ntakers", "Defiers"]
    arr = [1.0, 6.5, 0.2, -1.0]
    colors = [GRAY, TEAL, GRAY, CORAL]
    ax.bar(strata, arr, color=colors, edgecolor=INDIGO)
    ax.axhline(0, color=SLATE)
    ax.set_ylabel("Principal-stratum absolute ARR (pp)")
    ax.set_title("Ch03 residual: principal strata redefine who owns the absolute effect", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch03_principal.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    attrition = np.linspace(0, 0.35, 40)
    true_arr = 4.0
    biased = true_arr + 12 * attrition  # differential attrition inflates
    ax.plot(attrition * 100, biased, color=CORAL, lw=2.5, label="Apparent ARR")
    ax.axhline(true_arr, color=TEAL, ls="--", label="True ARR=4pp")
    ax.set_xlabel("Differential attrition %"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch04 residual: attrition can manufacture absolute benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch04_attrition.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # IV LATE vs ATE absolute
    labels = ["ATE\n(all)", "LATE\n(compliers)", "ITT\n(absolute)"]
    vals = [3.0, 7.5, 2.4]
    ax.bar(labels, vals, color=[INDIGO, TEAL, GOLD], edgecolor=SLATE)
    ax.set_ylabel("Absolute effect (pp)")
    ax.set_title("Ch05 residual: IV LATE is not the absolute ATE for all patients", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch05_iv_late.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    designs = ["Double\nblind", "Single\nblind", "Open\nlabel"]
    perf_bias = [0.2, 1.5, 3.0]
    true = [4, 4, 4]
    ax.bar(designs, true, color=TEAL, edgecolor=INDIGO, label="True ARR")
    ax.bar(designs, perf_bias, bottom=true, color=CORAL, edgecolor=INDIGO, label="Performance/detection absolute bias")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch06 residual: open-label designs inflate absolute effects via performance bias", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch06_openlabel.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    # healthy-user: adherent look better absolutely
    event_adh = 0.015 * t
    event_non = 0.035 * t
    ax.plot(t, event_adh * 100, color=TEAL, lw=2.4, label="Adherent absolute cumulative risk")
    ax.plot(t, event_non * 100, color=CORAL, lw=2.4, label="Nonadherent absolute cumulative risk")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative risk %")
    ax.set_title("Ch07 residual: healthy-user bias appears as absolute risk separation", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch07_healthy_user.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    spectrum = ["Asymptomatic", "Primary\ncare", "ED", "ICU"]
    sens = [0.55, 0.70, 0.85, 0.95]
    ppv_at_10 = []
    for s in sens:
        # prior 10%, spec 0.9
        tp = s * 0.10
        fp = (1 - 0.9) * 0.90
        ppv_at_10.append(100 * tp / (tp + fp))
    x = np.arange(4)
    ax.bar(x - 0.2, [s * 100 for s in sens], width=0.4, color=GOLD, edgecolor=INDIGO, label="Sensitivity %")
    ax.bar(x + 0.2, ppv_at_10, width=0.4, color=TEAL, edgecolor=INDIGO, label="PPV at 10% prior %")
    ax.set_xticks(x); ax.set_xticklabels(spectrum, fontsize=8)
    ax.set_ylabel("Absolute %")
    ax.set_title("Ch08 residual: spectrum bias moves absolute PPV even at fixed prior", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch08_spectrum.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sites = ["Derive", "Int.\nvalid", "Ext.\nvalid", "Temporal"]
    auroc = [0.88, 0.84, 0.76, 0.71]
    cal = [0.5, 1.2, 4.5, 6.0]
    x = np.arange(4)
    ax.plot(x, auroc, "o-", color=GOLD, lw=2.2, label="AUROC")
    ax2 = ax.twinx()
    ax2.plot(x, cal, "s-", color=CORAL, lw=2.3, label="Abs cal error pp")
    ax.set_xticks(x); ax.set_xticklabels(sites)
    ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute calibration error")
    ax.set_title("Ch09 residual: pred≠cause — external validation fails on absolute calibration first", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch09_extval.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # network meta absolute ranking uncertainty
    tx = ["A", "B", "C", "D"]
    rank_p1 = [0.55, 0.25, 0.15, 0.05]
    arr = [5.0, 3.5, 2.0, 0.5]
    x = np.arange(4)
    ax.bar(x - 0.2, [p * 100 for p in rank_p1], width=0.4, color=GOLD, edgecolor=INDIGO, label="P(best rank) %")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, arr, width=0.4, color=TEAL, edgecolor=INDIGO, label="Absolute ARR pp")
    ax.set_xticks(x); ax.set_xticklabels(tx)
    ax.set_ylabel("P(best) %"); ax2.set_ylabel("Absolute ARR")
    ax.set_title("Ch10 residual: network rankings need absolute effects, not SUCRA alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper right", fontsize=8); ax2.legend(loc="center right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch10_nma_rank.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    metrics = ["Win\nratio", "Abs RD\nmRS≤2", "Abs RD\ndeath", "Mean\nutility"]
    # different scales — show that win ratio hides absolute
    vals = [1.35, 6.0, 1.5, 0.08]
    colors = [GOLD, TEAL, TEAL, INDIGO]
    ax.bar(metrics, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Metric value (heterogeneous units)")
    ax.set_title("Ch11 residual: win ratios need absolute RD companions for bedside use", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch11_winratio.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    harm = np.array([0.5, 1, 2, 4, 8])
    nnh = 100 / harm
    ax.plot(harm, nnh, "o-", color=CORAL, lw=2.5, ms=9)
    for h, n in zip(harm, nnh):
        ax.annotate(f"NNH={n:.0f}", (h, n), textcoords="offset points", xytext=(6, 4), fontsize=7, color=SLATE)
    ax.set_xlabel("Absolute risk increase (pp)"); ax.set_ylabel("NNH")
    ax.set_title("Ch12 residual: NNH is the absolute harm twin of NNT", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch12_nnh.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # spin: language positivity vs absolute null
    papers = np.arange(1, 9)
    spin_score = np.array([2, 3, 4, 3, 5, 4, 5, 6])
    arr = np.array([0.2, 0.5, 0.1, -0.3, 0.4, 0.0, 0.2, -0.1])
    ax.scatter(arr, spin_score, s=90, c=CORAL, edgecolors=INDIGO, zorder=3)
    ax.axvline(0, color=TEAL, ls="--", label="Null absolute ARR")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("Abstract spin score")
    ax.set_title("Ch13 residual: spin language can rise while absolute effects stay null", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch13_spin.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    groups = ["G1", "G2", "G3", "G4"]
    pred = [10, 10, 10, 10]
    obs = [9, 12, 6, 18]
    x = np.arange(4)
    ax.bar(x - 0.2, pred, width=0.4, color=GRAY, edgecolor=INDIGO, label="Predicted absolute risk")
    ax.bar(x + 0.2, obs, width=0.4, color=CORAL, edgecolor=INDIGO, label="Observed absolute risk")
    ax.set_xticks(x); ax.set_xticklabels(groups)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch14 residual: pred≠cause — fairness fails when absolute calibration differs by group", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle43_swarm_ch14_fair_cal.png")


def main():
    print("Cycle-43 →", OUT)
    for fn in [
        fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07,
        fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
