#!/usr/bin/env python3
"""CRIT-APP Cycle-48 densify: ch15–28 raise uniform floor to 24. Agg indigo. ARR/NNT. pred≠cause."""
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
    agenda = ["Paper\npick", "PICO", "Bias", "ARR\nboard", "Action"]
    minutes = [5, 8, 12, 15, 10]
    ax.bar(agenda, minutes, color=[GRAY, GOLD, GOLD, TEAL, INDIGO], edgecolor=SLATE)
    ax.axhline(15, color=CORAL, ls="--", label="Protect ARR board time")
    ax.set_ylabel("Minutes")
    ax.set_title("Ch15 residual: JC agendas must protect absolute-effect board time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch15_agenda.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # autopsy time vs quality of absolute critique
    hours = np.array([0.5, 1, 2, 3, 4])
    quality = 1 - np.exp(-0.9 * hours)
    ax.plot(hours, quality, "o-", color=INDIGO, lw=2.5)
    ax.set_xlabel("Autopsy hours"); ax.set_ylabel("Absolute critique completeness")
    ax.set_title("Ch16 residual: deep autopsies buy absolute-effect completeness with diminishing returns", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch16_time_quality.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # person-time absolute density
    months = np.array([1, 3, 6, 12, 24])
    events = np.array([5, 12, 20, 30, 42])
    py = months / 12 * 1000  # 1000 persons
    density = events / py * 100  # per 100 py
    ax.plot(months, density, "o-", color=TEAL, lw=2.4)
    ax.set_xlabel("Follow-up months"); ax.set_ylabel("Absolute incidence density /100 py")
    ax.set_title("Ch17 residual: incidence density needs absolute events over person-time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch17_density.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    criteria = ["Temporality", "Dose-\nresponse", "Specificity", "Experiment", "Abs\nstrength"]
    weight = [0.9, 0.6, 0.3, 0.95, 0.85]
    ax.barh(criteria, weight, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel("Causal teaching weight")
    ax.set_title("Ch18 residual: absolute strength + experiment dominate weak checklist items", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_xlim(0, 1.1); ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch18_causal_weight.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # compatibility intervals absolute
    estimates = ["A", "B", "C", "D"]
    mid = [2, 4, 1, 5]
    half = [1.5, 0.8, 2.5, 1.0]
    x = np.arange(4)
    ax.errorbar(x, mid, yerr=half, fmt="o", color=INDIGO, ecolor=TEAL, capsize=6, ms=10, lw=2)
    ax.axhline(0, color=CORAL, ls="--", label="Null absolute ARR")
    ax.set_xticks(x); ax.set_xticklabels(estimates)
    ax.set_ylabel("Absolute ARR (pp) with compatibility interval")
    ax.set_title("Ch19 residual: compatibility intervals communicate absolute uncertainty", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch19_compat_int.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # time-varying HR absolute RD panel
    t = np.linspace(1, 24, 24)
    hr = 0.7 + 0.01 * t
    rd = 3 + 0.15 * t - 0.004 * t ** 2
    ax.plot(t, hr, color=GRAY, lw=2.2, label="HR(t)")
    ax2 = ax.twinx()
    ax2.plot(t, rd, color=TEAL, lw=2.4, label="Absolute RD(t) pp")
    ax.set_xlabel("Months"); ax.set_ylabel("HR"); ax2.set_ylabel("Absolute RD pp")
    ax.set_title("Ch20 residual: time-varying effects need absolute RD(t), not only HR(t)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch20_tv_rd.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # interaction absolute RERI visual
    cells = ["A−B−", "A+B−", "A−B+", "A+B+"]
    risk = [5, 8, 9, 18]
    expected_add = 5 + (8 - 5) + (9 - 5)
    ax.bar(cells, risk, color=[GRAY, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.axhline(expected_add, color=INDIGO, ls="--", lw=2, label=f"Additive expected={expected_add}")
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch21 residual: RERI is excess absolute risk beyond additivity", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch21_reri_cells.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # stage shift absolute without mortality change
    stages = ["I", "II", "III", "IV"]
    pre = [20, 30, 30, 20]
    post = [40, 30, 20, 10]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, pre, width=w, color=GRAY, edgecolor=INDIGO, label="Pre-screen stage mix %")
    ax.bar(x + w/2, post, width=w, color=TEAL, edgecolor=INDIGO, label="Post-screen stage mix %")
    ax.set_xticks(x); ax.set_xticklabels(stages)
    ax.set_ylabel("Absolute stage mix %")
    ax.set_title("Ch22 residual: stage shift is absolute reclassification, not proof of benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch22_stage_shift.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # dual-process absolute checklist interrupts
    steps = ["S1\ngut", "Check\nprior", "Check\nARR", "S2\nverify"]
    error = [20, 12, 6, 3]
    ax.plot(steps, error, "o-", color=CORAL, lw=2.5, ms=10)
    ax.set_ylabel("Absolute decision error %")
    ax.set_title("Ch23 residual: absolute checklists interrupt System-1 error cascades", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch23_interrupt.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # harm surveillance absolute rates
    months = np.arange(1, 13)
    sich = 3.5 + 0.1 * np.sin(months)
    ax.plot(months, sich, "o-", color=CORAL, lw=2.3, label="sICH absolute %")
    ax.axhline(4.0, color=GOLD, ls="--", label="Safety absolute threshold")
    ax.set_xlabel("Month"); ax.set_ylabel("Absolute harm %")
    ax.set_title("Ch24 residual: harm appraisal tracks absolute safety thresholds over time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch24_harm_track.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # likelihood ratio → absolute post-test board
    priors = [5, 10, 20, 40]
    lr = 8
    posts = []
    for p in priors:
        o = (p / 100) / (1 - p / 100)
        posts.append(100 * (o * lr) / (1 + o * lr))
    x = np.arange(4)
    ax.bar(x - 0.2, priors, width=0.4, color=GRAY, edgecolor=INDIGO, label="Prior absolute %")
    ax.bar(x + 0.2, posts, width=0.4, color=TEAL, edgecolor=INDIGO, label="Post-test absolute %")
    ax.set_xticks(x); ax.set_xticklabels([f"{p}%" for p in priors])
    ax.set_ylabel("Absolute probability %")
    ax.set_title("Ch25 residual: LR boards must land on absolute post-test probabilities", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch25_lr_board.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # living SR update absolute effect trajectory
    update = np.arange(0, 6)
    arr = np.array([2.0, 2.5, 3.2, 3.5, 3.6, 3.7])
    ci = np.array([1.5, 1.2, 1.0, 0.9, 0.85, 0.8])
    ax.fill_between(update, arr - ci, arr + ci, color=TEAL, alpha=0.2)
    ax.plot(update, arr, "o-", color=INDIGO, lw=2.4)
    ax.set_xlabel("Living SR update #"); ax.set_ylabel("Absolute ARR (pp) ± CI half")
    ax.set_title("Ch26 residual: living reviews tighten absolute effect estimates over updates", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch26_living_arr.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # multiplicity absolute family-wise error
    m = np.arange(1, 30)
    fwer = 1 - (1 - 0.05) ** m
    ax.plot(m, fwer * 100, color=CORAL, lw=2.5)
    ax.axhline(5, color=TEAL, ls="--", label="Single-test 5%")
    ax.set_xlabel("Absolute number of tests"); ax.set_ylabel("Family-wise type-I %")
    ax.set_title("Ch27 residual: multiplicity inflates absolute family-wise error", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch27_fwer.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # policy absolute equity gap closure
    years = np.array([0, 1, 2, 3, 4, 5])
    gap = 15 * np.exp(-0.25 * years)
    ax.plot(years, gap, "o-", color=CORAL, lw=2.4, label="Absolute outcome gap pp")
    ax.fill_between(years, 0, gap, color=CORAL, alpha=0.15)
    ax.set_xlabel("Years of equity intervention"); ax.set_ylabel("Absolute gap (pp)")
    ax.set_title("Ch28 residual: equity progress is measured in absolute outcome gap closure", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle48_swarm_ch28_gap_close.png")


def main():
    print("Cycle-48 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
