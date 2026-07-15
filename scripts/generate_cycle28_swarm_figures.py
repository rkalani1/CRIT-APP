#!/usr/bin/env python3
"""CRIT-APP Cycle-28 densify: clear residual floor-13 → uniform floor ≥14.

14 original scientific Agg indigo plots for ch15–ch28.
ARR/NNT; pred≠cause. cycle28_swarm_* only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
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


def fig_ch15():
    """JC run chart: absolute decision quality over successive sessions."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sessions = np.arange(1, 13)
    quality = np.array([45, 48, 52, 50, 58, 62, 70, 72, 75, 78, 82, 85], dtype=float)
    nostruct = np.array([45, 46, 44, 48, 47, 50, 49, 51, 50, 52, 51, 53], dtype=float)
    ax.plot(sessions, quality, "o-", color=TEAL, lw=2.4, ms=8, label="Structured absolute JC")
    ax.plot(sessions, nostruct, "s--", color=CORAL, lw=2.1, ms=7, label="Unstructured opinion JC")
    ax.axhline(70, color=GOLD, ls=":", lw=1.3)
    ax.text(1.2, 72, "action-ready floor", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xlabel("Journal club session number")
    ax.set_ylabel("Absolute decision-quality score (teaching)")
    ax.set_title(
        "Teaching residual: structured absolute ARR drills lift JC quality over time",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.set_ylim(30, 100)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch15_jc_runchart.png")


def fig_ch16():
    """Autopsy severity stacked: fatal/major/minor absolute counts by paper type."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    types = ["RCT", "Obs", "Dx", "Px/AI", "Meta"]
    fatal = np.array([1, 3, 2, 4, 2])
    major = np.array([2, 4, 3, 3, 3])
    minor = np.array([5, 3, 4, 2, 4])
    x = np.arange(len(types))
    ax.bar(x, fatal, color=CORAL, edgecolor=INDIGO, label="Fatal")
    ax.bar(x, major, bottom=fatal, color=GOLD, edgecolor=INDIGO, label="Major")
    ax.bar(x, minor, bottom=fatal + major, color=TEAL, edgecolor=INDIGO, label="Minor")
    ax.set_xticks(x)
    ax.set_xticklabels(types, fontsize=9)
    ax.set_ylabel("Flaw counts (teaching autopsy set)")
    ax.set_title(
        "Autopsy residual: fatal absolute flaws dominate reject decisions",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch16_flaw_stack.png")


def fig_ch17():
    """OR vs RR vs RD divergence as outcome becomes common."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    p0 = np.linspace(0.02, 0.45, 80)
    rr = 0.70
    p1 = rr * p0
    rd = (p0 - p1) * 100  # ARR if protective
    # OR = (p1/(1-p1))/(p0/(1-p0))
    OR = (p1 / (1 - p1)) / (p0 / (1 - p0))
    ax.plot(p0 * 100, np.full_like(p0, rr), color=GOLD, lw=2.2, label="RR (fixed 0.70)")
    ax.plot(p0 * 100, OR, color=CORAL, lw=2.2, label="OR")
    ax2 = ax.twinx()
    ax2.plot(p0 * 100, rd, color=TEAL, lw=2.4, label="RD/ARR (pp)")
    ax.set_xlabel("Control risk p0 (%)")
    ax.set_ylabel("Ratio measures", color=SLATE)
    ax2.set_ylabel("Absolute RD (pp)", color=TEAL)
    ax2.tick_params(axis="y", labelcolor=TEAL)
    ax.set_title(
        "Association residual: OR ≠ RR when outcomes are common; RD is the absolute story",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    # combined legend
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, fontsize=8, loc="center right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch17_or_rr_rd.png")


def fig_ch18():
    """Counterfactual contrast: observed vs potential outcomes absolute."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ["Y¹ observed\n(treated)", "Y⁰ counterfactual\n(if untreated)", "Y⁰ observed\n(control)", "Y¹ counterfactual\n(if treated)"]
    # two people teaching
    vals = [12, 20, 18, 11]  # absolute risk %
    cols = [TEAL, CORAL, GRAY, GOLD]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.annotate(
        "",
        xy=(1, 20),
        xytext=(0, 12),
        arrowprops=dict(arrowstyle="<->", color=INDIGO, lw=1.8),
    )
    ax.text(0.5, 22, "Individual causal contrast\n(unobservable pair)", ha="center", fontsize=8, color=INDIGO, fontweight="bold")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=8)
    ax.set_ylabel("Absolute event risk %")
    ax.set_title(
        "Causation residual: average causal ARR needs design, not observed association alone",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch18_counterfactual.png")


def fig_ch19():
    """p-value function for absolute ARR (compatibility curve)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(-0.05, 0.15, 200)
    # observed ARR 0.04, SE 0.02
    se = 0.02
    est = 0.04
    z = (arr - est) / se
    # two-sided p from normal
    from math import erfc

    p = np.array([erfc(abs(zi) / np.sqrt(2)) for zi in z])
    ax.plot(arr * 100, p, color=INDIGO, lw=2.5)
    ax.axhline(0.05, color=CORAL, ls="--", lw=1.2)
    ax.axvline(0, color=GRAY, ls=":", lw=1.2)
    ax.axvline(est * 100, color=TEAL, ls="--", lw=1.3)
    ax.text(est * 100 + 0.3, 0.8, "point ARR", color=TEAL, fontsize=8, fontweight="bold")
    ax.set_xlabel("Absolute ARR (pp)")
    ax.set_ylabel("Two-sided p (compatibility)")
    ax.set_title(
        "Inference residual: p-value function over absolute ARR, not a single star",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.set_ylim(0, 1.05)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch19_pvalue_function.png")


def fig_ch20():
    """Table-2 fallacy: total vs direct effect absolute decomposition."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ["Total effect\nARR", "Via mediator\n(indirect)", "Direct residual\n(after adjusting M)", "Naive Table-2\ncoefficient"]
    vals = [5.0, 2.0, 3.0, 1.2]
    cols = [INDIGO, TEAL, GOLD, CORAL]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_ylabel("Absolute effect (pp teaching)")
    ax.set_title(
        "Regression residual: Table-2 adjustment can erase pathway absolute effects",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch20_table2_decomp.png")


def fig_ch21():
    """Standardization: crude vs standardized absolute rates."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strata = ["Young", "Mid", "Old"]
    rate_a = np.array([2, 5, 12])
    rate_b = np.array([3, 6, 10])
    weights = np.array([0.5, 0.3, 0.2])  # standard pop
    x = np.arange(3)
    w = 0.35
    ax.bar(x - w / 2, rate_a, width=w, color=TEAL, edgecolor=INDIGO, label="Pop A stratum rates")
    ax.bar(x + w / 2, rate_b, width=w, color=GOLD, edgecolor=INDIGO, label="Pop B stratum rates")
    std_a = (rate_a * weights).sum()
    std_b = (rate_b * weights).sum()
    ax.axhline(std_a, color=TEAL, ls="--", lw=1.4)
    ax.axhline(std_b, color=GOLD, ls="--", lw=1.4)
    ax.text(2.15, std_a + 0.3, f"std A={std_a:.1f}", color=TEAL, fontsize=8, fontweight="bold")
    ax.text(2.15, std_b - 0.8, f"std B={std_b:.1f}", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xticks(x)
    ax.set_xticklabels(strata, fontsize=9)
    ax.set_ylabel("Absolute event rate (/100 py)")
    ax.set_title(
        "Standardization residual: crude rates mislead; standardized absolute rates compare",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch21_standardization.png")


def fig_ch22():
    """Overdiagnosis absolute count vs mortality ARR over screening intensity."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    intensity = np.linspace(0, 1, 50)
    overdx = 5 + 40 * intensity ** 1.2  # /1000
    mort_arr = 2.5 * (1 - np.exp(-2.5 * intensity))  # /1000 saturates
    ax.plot(intensity, overdx, color=CORAL, lw=2.5, label="Overdiagnosis /1000")
    ax.plot(intensity, mort_arr, color=TEAL, lw=2.5, label="Mortality ARR /1000")
    ax.fill_between(intensity, mort_arr, overdx, where=overdx >= mort_arr, color=CORAL, alpha=0.10)
    ax.set_xlabel("Screening intensity (0–1 teaching)")
    ax.set_ylabel("Absolute events per 1000")
    ax.set_title(
        "Screening residual: overdiagnosis can dwarf absolute mortality ARR",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch22_overdx_vs_arr.png")


def fig_ch23():
    """Dual-process: System-1 vs System-2 absolute error under prevalence shift."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prev = np.linspace(1, 40, 40)
    # S1 anchors on 50% → large absolute error at extremes
    s1 = np.abs(50 - prev)
    # S2 uses base rate → smaller error
    s2 = 3 + 0.08 * prev
    ax.plot(prev, s1, color=CORAL, lw=2.4, label="System-1 absolute error (pp)")
    ax.plot(prev, s2, color=TEAL, lw=2.4, label="System-2 absolute error (pp)")
    ax.set_xlabel("True prevalence / pre-test (%)")
    ax.set_ylabel("Absolute probability error (pp)")
    ax.set_title(
        "Reasoning residual: dual-process absolute error widens when base rates shift",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch23_dual_process_error.png")


def fig_ch24():
    """NNH and NNT joint: isobars of net absolute benefit."""
    fig, ax = plt.subplots(figsize=(10.2, 5.2))
    arr = np.linspace(0.5, 15, 100)
    ari = np.linspace(0.2, 8, 100)
    ARR, ARI = np.meshgrid(arr, ari)
    net = ARR - ARI
    cs = ax.contourf(ARR, ARI, net, levels=np.linspace(-8, 15, 12), cmap="RdYlGn", alpha=0.85)
    fig.colorbar(cs, ax=ax, label="Net absolute (ARR−ARI) pp")
    ax.contour(ARR, ARI, net, levels=[0], colors=["#283593"], linewidths=2)
    ax.scatter([6], [1.5], s=100, color=INDIGO, edgecolors=WHITE, zorder=5)
    ax.text(6.3, 1.7, "example Tx", fontsize=8, fontweight="bold", color=INDIGO)
    ax.set_xlabel("ARR (pp)")
    ax.set_ylabel("ARI (pp)")
    ax.set_title(
        "Therapy residual: net absolute benefit isosurfaces (ARR vs ARI)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch24_net_isobars.png")


def fig_ch25():
    """Prognostic model transport: calibration slope across sites."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sites = ["Derive", "Site B", "Site C", "Site D", "Site E"]
    slopes = [1.00, 0.88, 0.72, 0.65, 0.55]
    intercepts = [0.0, 0.02, 0.05, 0.08, 0.12]
    x = np.arange(len(sites))
    ax.bar(x, slopes, color=[TEAL if s > 0.8 else GOLD if s > 0.7 else CORAL for s in slopes], edgecolor=INDIGO)
    ax.axhline(1.0, color=GRAY, ls="--", lw=1.2)
    for i, (s, b) in enumerate(zip(slopes, intercepts)):
        ax.text(i, s + 0.03, f"int={b:.2f}", ha="center", fontsize=7.5, color=SLATE)
    ax.set_xticks(x)
    ax.set_xticklabels(sites, fontsize=9)
    ax.set_ylabel("Calibration slope")
    ax.set_ylim(0, 1.2)
    ax.set_title(
        "Dx/Px residual: external sites degrade absolute calibration slope (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch25_calib_transport.png")


def fig_ch26():
    """Prediction interval vs confidence interval for next absolute effect."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    y = [2, 1]
    # CI for mean ARR
    ax.errorbar([4], [2], xerr=[[1.0], [1.0]], fmt="o", color=INDIGO, lw=2.5, ms=10, label="95% CI (mean ARR)")
    # PI for new study
    ax.errorbar([4], [1], xerr=[[3.5], [3.5]], fmt="s", color=CORAL, lw=2.5, ms=10, label="95% PI (new study ARR)")
    ax.axvline(0, color=GRAY, ls="--", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels(["Mean effect CI", "Next-study PI"], fontsize=10)
    ax.set_xlabel("Absolute ARR (pp)")
    ax.set_xlim(-2, 10)
    ax.set_title(
        "Synthesis residual: prediction intervals bound next absolute effect, not only the mean",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch26_ci_vs_pi.png")


def fig_ch27():
    """Missingness mechanisms: absolute bias under MCAR/MAR/MNAR."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    miss = np.linspace(0, 0.4, 50)
    mcar = np.full_like(miss, 0.3)  # small noise
    mar = 0.3 + 2.5 * miss
    mnar = 0.3 + 6.0 * miss + 8 * miss ** 2
    ax.plot(miss * 100, mcar, color=TEAL, lw=2.3, label="MCAR residual bias")
    ax.plot(miss * 100, mar, color=GOLD, lw=2.3, label="MAR (if unadjusted)")
    ax.plot(miss * 100, mnar, color=CORAL, lw=2.5, label="MNAR absolute bias")
    ax.set_xlabel("Missing outcome fraction (%)")
    ax.set_ylabel("Absolute ARR bias (pp teaching)")
    ax.set_title(
        "Missing-data residual: MNAR can dominate absolute effect estimates",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch27_missingness_bias.png")


def fig_ch28():
    """Systems absolute: door-to-needle minutes vs population ARR-equivalent."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    minutes = np.array([20, 30, 45, 60, 75, 90])
    # each 15 min delay costs absolute good outcomes
    good = 40 - 0.22 * (minutes - 20)
    ax.plot(minutes, good, "o-", color=TEAL, lw=2.5, ms=9)
    ax.fill_between(minutes, good, 25, color=TEAL, alpha=0.12)
    for m, g in zip(minutes, good):
        ax.text(m, g + 0.6, f"{g:.1f}%", ha="center", fontsize=8, fontweight="bold", color=INDIGO)
    ax.set_xlabel("Door-to-needle / door-to-puncture (minutes)")
    ax.set_ylabel("Absolute good outcome % (teaching)")
    ax.set_title(
        "Systems residual: process minutes translate into absolute outcome percentages",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    ax.set_ylim(20, 45)
    fig.tight_layout()
    return _save(fig, "cycle28_swarm_ch28_d2n_absolute.png")


def main():
    print("Cycle-28 →", OUT)
    fns = [
        fig_ch15,
        fig_ch16,
        fig_ch17,
        fig_ch18,
        fig_ch19,
        fig_ch20,
        fig_ch21,
        fig_ch22,
        fig_ch23,
        fig_ch24,
        fig_ch25,
        fig_ch26,
        fig_ch27,
        fig_ch28,
    ]
    for fn in fns:
        fn()
    print(f"Done: {len(fns)}")


if __name__ == "__main__":
    main()
