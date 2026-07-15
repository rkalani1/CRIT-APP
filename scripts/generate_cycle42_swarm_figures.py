#!/usr/bin/env python3
"""CRIT-APP Cycle-42 densify: ch15–28 raise uniform floor to 21. Agg indigo. ARR/NNT. pred≠cause."""
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
    roles = ["Chair", "Methods", "Stats", "Clinician", "Scribe"]
    arr_mentions = [1, 4, 5, 2, 3]
    ax.barh(roles, arr_mentions, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel("Absolute ARR/NNT mentions per JC")
    ax.set_title("Ch15 residual: role design determines absolute-risk board completeness", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch15_roles.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    domains = ["Question", "Bias", "Absolute\neffect", "Spin", "Action"]
    severity = [1, 3, 4, 2, 3]
    colors = [TEAL if s <= 1 else (GOLD if s <= 2 else CORAL) for s in severity]
    ax.bar(domains, severity, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Autopsy severity (0–4 absolute scale)")
    ax.set_title("Ch16 residual: autopsy severity scores privilege absolute-effect failures", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 4.5); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch16_severity.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    groups = ["Ref", "A", "B", "C"]
    rate = [2.0, 2.4, 3.5, 5.0]
    excess = [0, 0.4, 1.5, 3.0]
    x = np.arange(4)
    ax.bar(x, rate, color=GRAY, edgecolor=INDIGO, label="Absolute incidence /100py")
    ax.bar(x, excess, color=CORAL, edgecolor=INDIGO, alpha=0.7, label="Absolute excess vs ref")
    ax.set_xticks(x); ax.set_xticklabels(groups)
    ax.set_ylabel("Absolute rate")
    ax.set_title("Ch17 residual: SMR-style claims need absolute excess rates, not ratios alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch17_excess.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    paths = ["Total\neffect", "Natural\ndirect", "Natural\nindirect", "Controlled\ndirect"]
    arr = [5.0, 3.2, 1.8, 2.9]
    ax.bar(paths, arr, color=[INDIGO, TEAL, GOLD, PURPLE], edgecolor=SLATE)
    ax.set_ylabel("Absolute effect (pp)")
    ax.set_title("Ch18 residual: mediation decomposes absolute effects, not only log-odds", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch18_mediation.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    n_looks = np.arange(1, 11)
    # CI half-width inflation under optional stopping sketch
    half = 1.96 * 5 / np.sqrt(200) * (1 + 0.15 * (n_looks - 1))
    ax.plot(n_looks, half, "o-", color=CORAL, lw=2.4)
    ax.set_xlabel("Unplanned looks at absolute ARR"); ax.set_ylabel("CI half-width (pp, teaching)")
    ax.set_title("Ch19 residual: optional stopping widens honest absolute uncertainty", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch19_optional_stop.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 36, 100)
    # landmark at 6 months
    s_all = np.exp(-0.02 * t)
    s_land = np.where(t < 6, np.nan, np.exp(-0.02 * (t - 6)))
    ax.plot(t, (1 - s_all) * 100, color=GRAY, lw=2.2, label="From time-zero absolute risk")
    ax.plot(t, (1 - s_land) * 100, color=TEAL, lw=2.4, label="Landmark absolute risk (t≥6)")
    ax.axvline(6, color=GOLD, ls="--", label="Landmark")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative risk %")
    ax.set_title("Ch20 residual: landmarking restarts absolute risk clocks honestly", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch20_landmark.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # same data: relative interaction null, absolute interaction present
    g = ["Low risk\nB−", "Low risk\nB+", "High risk\nB−", "High risk\nB+"]
    risk = [4, 3, 20, 10]  # RR interaction constant-ish, ARR differs
    ax.bar(g, risk, color=[GRAY, TEAL, GRAY, TEAL], edgecolor=INDIGO)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch21 residual: scale dependence — absolute interaction can exist when RR is flat", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch21_scale.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # lead-time bias: diagnosis earlier without changing death time
    t = np.array([0, 2, 4, 6, 8, 10])
    death = 10
    dx_screen = 2
    dx_clin = 6
    ax.hlines(1, 0, death, color=GRAY, lw=8, label="Natural history")
    ax.plot([dx_screen], [1], "o", color=TEAL, ms=14, label=f"Screen dx (lead +{dx_clin-dx_screen}y)")
    ax.plot([dx_clin], [1], "s", color=CORAL, ms=12, label="Clinical dx")
    ax.plot([death], [1], "X", color=INDIGO, ms=14, label="Death (unchanged)")
    ax.set_yticks([]); ax.set_xlabel("Years")
    ax.set_xlim(-0.5, 11); ax.set_ylim(0.5, 1.5)
    ax.set_title("Ch22 residual: lead time inflates apparent absolute survival without changing death", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left"); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch22_leadtime.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    base = np.array([1, 5, 15, 40])
    remembered = np.array([12, 18, 25, 45])  # availability inflates rare
    x = np.arange(4)
    labels = ["1%", "5%", "15%", "40%"]
    ax.bar(x - 0.2, base, width=0.4, color=TEAL, edgecolor=INDIGO, label="True absolute base rate")
    ax.bar(x + 0.2, remembered, width=0.4, color=CORAL, edgecolor=INDIGO, label="Availability-distorted estimate")
    ax.set_xticks(x); ax.set_xticklabels(labels)
    ax.set_ylabel("Absolute probability %")
    ax.set_title("Ch23 residual: availability heuristic warps absolute base rates", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch23_availability.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    components = ["Death", "mRS>2", "sICH", "Composite"]
    ctrl = [8, 25, 2, 30]
    tx = [6, 18, 3, 22]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control absolute %")
    ax.bar(x + w/2, tx, width=w, color=TEAL, edgecolor=INDIGO, label="Treatment absolute %")
    ax.set_xticks(x); ax.set_xticklabels(components)
    ax.set_ylabel("Absolute event %")
    ax.set_title("Ch24 residual: composite ARR hides component absolute directions", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch24_composite.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    months = np.array([1, 3, 6, 12, 24])
    auroc = np.array([0.82, 0.80, 0.78, 0.74, 0.70])
    brier = np.array([0.12, 0.14, 0.16, 0.20, 0.24])
    ax.plot(months, auroc, "o-", color=GOLD, lw=2.2, label="Time-dependent AUROC")
    ax2 = ax.twinx()
    ax2.plot(months, brier, "s-", color=CORAL, lw=2.3, label="Absolute Brier score")
    ax.set_xlabel("Horizon (months)"); ax.set_ylabel("AUROC"); ax2.set_ylabel("Absolute Brier")
    ax.set_title("Ch25 residual: prognosis value is horizon-specific absolute calibration", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch25_horizon.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    outcomes = ["Death", "Depend.", "ICH", "mRS0–2"]
    abs_fx = [-1.5, -4.0, 0.8, 5.0]
    colors = [TEAL if v < 0 and o != "mRS0–2" else (TEAL if v > 0 and o == "mRS0–2" else CORAL)
              for o, v in zip(outcomes, abs_fx)]
    # fix colors simply: benefit teal for favorable, coral for harm
    colors = [TEAL, TEAL, CORAL, TEAL]
    ax.barh(outcomes, abs_fx, color=colors, edgecolor=INDIGO)
    ax.axvline(0, color=SLATE)
    ax.set_xlabel("Absolute risk difference (pp)")
    ax.set_title("Ch26 residual: SoF tables must show absolute effects with certainty", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch26_sof_abs.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    looks = ["L1", "L2", "L3", "Final"]
    alpha_spend = [0.001, 0.005, 0.01, 0.034]
    cum = np.cumsum(alpha_spend)
    ax.bar(looks, alpha_spend, color=GOLD, edgecolor=INDIGO, label="Alpha spent")
    ax.plot(looks, cum, "o-", color=CORAL, lw=2.3, label="Cumulative alpha")
    ax.axhline(0.05, color=TEAL, ls="--", label="Family-wise 0.05")
    ax.set_ylabel("Absolute alpha")
    ax.set_title("Ch27 residual: interim looks spend absolute alpha that final tests must respect", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch27_alpha_spend.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strata = ["A", "B", "C", "D"]
    d2n = [45, 62, 88, 120]
    good = [42, 36, 28, 20]
    x = np.arange(4)
    ax.bar(x - 0.2, d2n, width=0.4, color=CORAL, edgecolor=INDIGO, label="Door-to-needle (min)")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, good, width=0.4, color=TEAL, edgecolor=INDIGO, label="Absolute good outcome %")
    ax.set_xticks(x); ax.set_xticklabels(strata)
    ax.set_xlabel("Equity stratum"); ax.set_ylabel("Minutes"); ax2.set_ylabel("Absolute %")
    ax.set_title("Ch28 residual: equity gaps are absolute process and outcome differences", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle42_swarm_ch28_equity.png")


def main():
    print("Cycle-42 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
