#!/usr/bin/env python3
"""CRIT-APP Cycle-25 densify: raise uniform floor 12 → toward 13 (wave A, half-book).

14 original scientific Agg indigo plots for ch01–ch14.
Prefer continuous scientific graphics (curves, forests, CIFs, calibration)
over decorative bars. ARR/NNT emphasis; pred≠cause.
cycle25_swarm_* only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
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
    """RRR fixed → ARR and NNT vs control event rate (absolute conversion surface)."""
    fig, ax1 = plt.subplots(figsize=(10.4, 5.0))
    cer = np.linspace(0.02, 0.40, 120)
    rrr = 0.25
    arr = rrr * cer * 100  # pp
    nnt = 1.0 / (rrr * cer)
    ax1.plot(cer * 100, arr, color=TEAL, lw=2.5, label="ARR (pp) = RRR × CER")
    ax1.set_xlabel("Control event rate CER (%)")
    ax1.set_ylabel("ARR (percentage points)", color=TEAL)
    ax1.tick_params(axis="y", labelcolor=TEAL)
    ax1.set_ylim(0, 12)
    ax1.grid(True, alpha=0.3)
    ax2 = ax1.twinx()
    ax2.plot(cer * 100, nnt, color=CORAL, lw=2.5, ls="--", label="NNT = 1/ARR")
    ax2.set_ylabel("NNT (same horizon)", color=CORAL)
    ax2.tick_params(axis="y", labelcolor=CORAL)
    ax2.set_ylim(0, 200)
    # annotate bedside vs trial CER
    ax1.axvline(8, color=GOLD, ls=":", lw=1.4)
    ax1.axvline(20, color=INDIGO, ls=":", lw=1.4)
    ax1.text(8.3, 10.5, "low-risk\nbedside", color=GOLD, fontsize=8, fontweight="bold")
    ax1.text(20.3, 10.5, "trial CER", color=INDIGO, fontsize=8, fontweight="bold")
    ax1.set_title(
        "Fixed RRR=25%: absolute ARR and NNT swing with baseline risk",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="center right")
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch01_rrr_arr_nnt_surface.png")


def fig_ch02():
    """Information gain under time pressure: cumulative absolute insight vs minutes."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    minutes = np.array([0, 1, 2, 3, 5, 8, 12, 18, 25])
    # diminishing returns if you skip tables
    full = np.array([0, 25, 48, 62, 78, 88, 94, 97, 99], dtype=float)
    abstract_only = np.array([0, 30, 40, 45, 48, 50, 51, 52, 52], dtype=float)
    tables_first = np.array([0, 15, 40, 58, 75, 90, 96, 98, 99], dtype=float)
    ax.plot(minutes, full, "o-", color=INDIGO, lw=2.3, ms=7, label="Structured DFR (abstract→tables→ARR)")
    ax.plot(minutes, tables_first, "s-", color=TEAL, lw=2.2, ms=7, label="Tables/ARR first")
    ax.plot(minutes, abstract_only, "^-", color=CORAL, lw=2.2, ms=7, label="Abstract-only skim")
    ax.axhline(70, color=GOLD, ls="--", lw=1.2)
    ax.text(18, 72, "actionable threshold", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xlabel("Reading minutes under sign-out pressure")
    ax.set_ylabel("Cumulative absolute decision insight (teaching %)")
    ax.set_title(
        "Time-pressure residual: abstract skim never reaches absolute action threshold",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="lower right")
    ax.set_ylim(0, 105)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch02_time_insight_curve.png")


def fig_ch03():
    """Estimand clock: index time, intercurrent events, outcome window with ARR at risk."""
    fig, ax = plt.subplots(figsize=(10.6, 4.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title(
        "Estimand residual: absolute ARR requires index time + intercurrent policy",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    # timeline
    ax.annotate(
        "",
        xy=(11.5, 3),
        xytext=(0.5, 3),
        arrowprops=dict(arrowstyle="->", color=SLATE, lw=2),
    )
    # markers
    marks = [
        (1.2, "Eligibility\n& index t0", TEAL),
        (4.0, "Intercurrent\n(crossover/rescue)", CORAL),
        (7.2, "Outcome\nwindow", INDIGO),
        (10.0, "Summary\nARR/NNT", GOLD),
    ]
    for x, lab, c in marks:
        ax.plot(x, 3, "o", color=c, ms=14, zorder=5)
        ax.plot([x, x], [3, 4.2], color=c, lw=1.5)
        ax.text(x, 4.6, lab, ha="center", va="bottom", fontsize=8.5, fontweight="bold", color=c)
    # incomplete box
    ax.add_patch(
        FancyBboxPatch(
            (3.2, 0.5),
            5.6,
            1.6,
            boxstyle="round,pad=0.03,rounding_size=0.08",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.4,
        )
    )
    ax.text(
        6.0,
        1.3,
        "If intercurrent policy unspecified → ARR is not transportable",
        ha="center",
        va="center",
        fontsize=9,
        fontweight="bold",
        color=CORAL,
    )
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch03_estimand_clock.png")


def fig_ch04():
    """Bias taxonomy: absolute distortion vectors (direction + magnitude)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    biases = [
        "Selection",
        "Confounding",
        "Information",
        "Attrition",
        "Reporting",
    ]
    # signed absolute pp distortion (positive = overestimate benefit)
    delta = np.array([3.5, 5.0, 1.5, 2.5, 4.0])
    y = np.arange(len(biases))
    colors = [CORAL if d > 0 else TEAL for d in delta]
    ax.barh(y, delta, color=colors, edgecolor=INDIGO, height=0.55)
    ax.axvline(0, color=SLATE, lw=1.2)
    ax.set_yticks(y)
    ax.set_yticklabels(biases, fontsize=10)
    ax.set_xlabel("Apparent ARR − true ARR (pp, teaching signs)")
    ax.set_title(
        "Bias taxonomy residual: each domain moves absolute effect on a signed scale",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="x", alpha=0.3)
    for yi, d in zip(y, delta):
        ax.text(d + 0.15, yi, f"+{d:.1f} pp", va="center", fontsize=8.5, color=SLATE)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch04_bias_vectors.png")


def fig_ch05():
    """Backdoor residual: confounding strength vs adjusted ARR (target-trial thinking)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    u = np.linspace(0, 1, 80)  # unmeasured confounding strength
    crude = 8.0 + 6.0 * u  # invents absolute benefit
    partially = 8.0 + 3.0 * u
    closed = np.full_like(u, 3.2)  # stable after closing backdoors
    ax.plot(u, crude, color=CORAL, lw=2.4, label="Crude ARR (open backdoors)")
    ax.plot(u, partially, color=GOLD, lw=2.2, label="Partial adjustment")
    ax.plot(u, closed, color=TEAL, lw=2.5, label="Target-trial / closed backdoors")
    ax.fill_between(u, closed, crude, color=CORAL, alpha=0.10)
    ax.set_xlabel("Unmeasured confounding strength (0–1 teaching scale)")
    ax.set_ylabel("Estimated ARR (pp)")
    ax.set_title(
        "DAG residual: absolute ARR only stabilizes when backdoors are closed",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, 16)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch05_backdoor_arr_curve.png")


def fig_ch06():
    """RCT attrition funnel with absolute event counts by arm."""
    fig, ax = plt.subplots(figsize=(10.4, 5.4))
    stages = ["Screened", "Randomized", "Received\nassigned", "Primary\noutcome"]
    ctrl = np.array([2400, 500, 480, 450], dtype=float)
    trt = np.array([2400, 500, 470, 440], dtype=float)
    x = np.arange(len(stages))
    w = 0.35
    ax.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control n")
    ax.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated n")
    # annotate absolute events at primary
    ax.annotate(
        "Events: C 90/450 (20%)\nT 68/440 (15.5%)\nARR≈4.5 pp",
        xy=(3, 440),
        xytext=(2.0, 1800),
        fontsize=9,
        fontweight="bold",
        color=INDIGO,
        arrowprops=dict(arrowstyle="->", color=INDIGO),
        bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE, edgecolor=INDIGO),
    )
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=9)
    ax.set_ylabel("Participants (n)")
    ax.set_title(
        "RCT residual: absolute ARR lives in the outcome denominator, not the screen",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch06_attrition_arr.png")


def fig_ch07():
    """Positivity / PS overlap: density overlap vs residual absolute bias."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    rng = np.random.default_rng(7)
    # good overlap
    ps_t = rng.beta(2.2, 2.0, 800)
    ps_c = rng.beta(2.0, 2.2, 800)
    ax = axes[0]
    ax.hist(ps_c, bins=25, density=True, alpha=0.55, color=GRAY, label="Control")
    ax.hist(ps_t, bins=25, density=True, alpha=0.55, color=TEAL, label="Treated")
    ax.set_xlabel("Propensity score")
    ax.set_ylabel("Density")
    ax.set_title("Good positivity (overlap)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.25)
    # poor overlap
    ps_t2 = rng.beta(5.0, 1.5, 800)
    ps_c2 = rng.beta(1.5, 5.0, 800)
    ax = axes[1]
    ax.hist(ps_c2, bins=25, density=True, alpha=0.55, color=GRAY, label="Control")
    ax.hist(ps_t2, bins=25, density=True, alpha=0.55, color=CORAL, label="Treated")
    ax.set_xlabel("Propensity score")
    ax.set_title("Poor positivity → residual ARR bias", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.25)
    fig.suptitle(
        "Observational residual: absolute estimates need common support, not just a PS model",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch07_positivity_overlap.png")


def fig_ch08():
    """Decision curve: net benefit absolute vs treat-all/none across threshold probability."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pt = np.linspace(0.01, 0.60, 120)
    prevalence = 0.18
    # synthetic sens/spec at fixed threshold (simplified constant performance)
    se, sp = 0.85, 0.75
    # net benefit of model: (TP/N) - (FP/N)*(pt/(1-pt))
    tp = se * prevalence
    fp = (1 - sp) * (1 - prevalence)
    nb_model = tp - fp * (pt / (1 - pt))
    nb_all = prevalence - (1 - prevalence) * (pt / (1 - pt))
    nb_none = np.zeros_like(pt)
    ax.plot(pt * 100, nb_model, color=INDIGO, lw=2.5, label="Test strategy NB")
    ax.plot(pt * 100, nb_all, color=GOLD, lw=2.0, ls="--", label="Treat-all")
    ax.plot(pt * 100, nb_none, color=GRAY, lw=1.8, ls=":", label="Treat-none")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlabel("Threshold probability pt (%)")
    ax.set_ylabel("Net benefit (absolute, per patient)")
    ax.set_title(
        "Diagnostic residual: absolute net benefit, not AUC alone, guides thresholds",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.set_ylim(-0.05, 0.22)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch08_decision_curve.png")


def fig_ch09():
    """Calibration plot with confidence band + action thresholds (pred ≠ cause)."""
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    pred = np.linspace(0.05, 0.70, 10)
    # miscalibrated external
    obs = pred * 0.75 + 0.04
    se = 0.03 + 0.02 * pred
    ax.plot([0, 0.75], [0, 0.75], "--", color=GRAY, lw=1.5, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=CORAL, lw=2.3, ms=8, label="External observed risk")
    ax.fill_between(pred, obs - 1.96 * se, obs + 1.96 * se, color=CORAL, alpha=0.15, label="95% band")
    ax.axhline(0.10, color=GOLD, ls=":", lw=1.3)
    ax.axhline(0.30, color=TEAL, ls=":", lw=1.3)
    ax.text(0.55, 0.11, "watch", color=GOLD, fontsize=8)
    ax.text(0.55, 0.31, "treat/discuss", color=TEAL, fontsize=8)
    ax.set_xlabel("Predicted absolute risk")
    ax.set_ylabel("Observed absolute risk")
    ax.set_title(
        "Prognosis residual: absolute miscalibration moves action thresholds (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.set_xlim(0, 0.75)
    ax.set_ylim(0, 0.75)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch09_calib_thresholds.png")


def fig_ch10():
    """Forest with prediction interval + local ARR translation panel."""
    fig, axes = plt.subplots(1, 2, figsize=(11.0, 5.0), gridspec_kw={"width_ratios": [1.35, 1]})
    ax = axes[0]
    studies = ["S1", "S2", "S3", "S4", "S5", "Pooled"]
    rr = np.array([0.70, 0.85, 0.62, 0.78, 0.90, 0.76])
    lo = np.array([0.52, 0.65, 0.45, 0.60, 0.72, 0.64])
    hi = np.array([0.94, 1.10, 0.85, 1.01, 1.12, 0.90])
    y = np.arange(len(studies))[::-1]
    for yi, r, l, h, name in zip(y, rr, lo, hi, studies):
        c = INDIGO if name == "Pooled" else SLATE
        lw = 2.6 if name == "Pooled" else 1.8
        ax.plot([l, h], [yi, yi], color=c, lw=lw)
        ax.plot(r, yi, "s" if name == "Pooled" else "o", color=c, ms=8 if name == "Pooled" else 6)
    # prediction interval
    ax.plot([0.48, 1.15], [-0.7, -0.7], color=CORAL, lw=3.0)
    ax.text(0.48, -1.15, "95% prediction interval", color=CORAL, fontsize=8, fontweight="bold")
    ax.axvline(1.0, color=GRAY, ls="--", lw=1)
    ax.set_yticks(list(y) + [-0.7])
    ax.set_yticklabels(studies + ["PI"], fontsize=9)
    ax.set_xlabel("Risk ratio")
    ax.set_xlim(0.35, 1.25)
    ax.set_title("Relative synthesis", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3)

    ax = axes[1]
    # local translation
    local_cer = np.array([6, 12, 20])  # %
    local_arr = (1 - 0.76) * local_cer
    local_nnt = 100 / local_arr
    x = np.arange(3)
    ax.bar(x, local_arr, color=TEAL, edgecolor=INDIGO, width=0.55)
    for i, (a, n) in enumerate(zip(local_arr, local_nnt)):
        ax.text(i, a + 0.25, f"NNT≈{n:.0f}", ha="center", fontsize=8, fontweight="bold", color=INDIGO)
    ax.set_xticks(x)
    ax.set_xticklabels([f"CER {c}%" for c in local_cer], fontsize=9)
    ax.set_ylabel("Local ARR (pp)")
    ax.set_title("Absolute local transport", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Meta residual: pooled RR is incomplete without local absolute ARR/NNT",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch10_forest_local_arr.png")


def fig_ch11():
    """Competing risks: cause-specific hazard vs cumulative incidence absolute."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 90, 100)
    # stroke recurrence CIF
    cif_stroke_c = 1 - np.exp(-0.004 * t)
    cif_stroke_t = 1 - np.exp(-0.0025 * t)
    # death competing
    cif_death = 1 - np.exp(-0.003 * t)
    ax.plot(t, cif_stroke_c * 100, color=CORAL, lw=2.4, label="Stroke CIF control")
    ax.plot(t, cif_stroke_t * 100, color=TEAL, lw=2.4, label="Stroke CIF treated")
    ax.plot(t, cif_death * 100, color=GRAY, lw=2.0, ls="--", label="Death competing CIF")
    # absolute difference at 90d
    d90 = (cif_stroke_c[-1] - cif_stroke_t[-1]) * 100
    ax.annotate(
        f"90-day absolute ΔCIF ≈ {d90:.1f} pp\n(not a hazard ratio)",
        xy=(90, cif_stroke_t[-1] * 100),
        xytext=(45, 22),
        fontsize=9,
        fontweight="bold",
        color=INDIGO,
        arrowprops=dict(arrowstyle="->", color=INDIGO),
        bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE, edgecolor=INDIGO),
    )
    ax.set_xlabel("Days from index stroke")
    ax.set_ylabel("Cumulative incidence (%)")
    ax.set_title(
        "Outcomes residual: absolute CIF differences under competing risks",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper left")
    ax.set_ylim(0, 35)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch11_competing_cif.png")


def fig_ch12():
    """ARR and NNT continuum vs baseline risk with harm ARI band."""
    fig, ax1 = plt.subplots(figsize=(10.4, 5.0))
    cer = np.linspace(0.02, 0.35, 100)
    rrr = 0.30
    arr = rrr * cer * 100
    ari = np.full_like(cer, 1.2)  # fixed absolute harm
    net = arr - ari
    nnt = 100 / arr
    ax1.plot(cer * 100, arr, color=TEAL, lw=2.4, label="ARR benefit")
    ax1.plot(cer * 100, ari, color=CORAL, lw=2.0, ls="--", label="ARI harm (fixed)")
    ax1.plot(cer * 100, net, color=INDIGO, lw=2.5, label="Net absolute (ARR−ARI)")
    ax1.axhline(0, color=GRAY, lw=0.9)
    ax1.fill_between(cer * 100, 0, net, where=net > 0, color=TEAL, alpha=0.10)
    ax1.fill_between(cer * 100, 0, net, where=net < 0, color=CORAL, alpha=0.12)
    ax1.set_xlabel("Baseline control risk (%)")
    ax1.set_ylabel("Absolute pp @ same horizon")
    ax1.set_title(
        "Effect-size residual: absolute benefit, harm, and net share one horizon",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax1.legend(fontsize=8, loc="upper left")
    ax1.grid(True, alpha=0.3)
    ax2 = ax1.twinx()
    ax2.plot(cer * 100, nnt, color=PURPLE, lw=1.6, alpha=0.7, label="NNT")
    ax2.set_ylabel("NNT (benefit)", color=PURPLE)
    ax2.tick_params(axis="y", labelcolor=PURPLE)
    ax2.set_ylim(0, 180)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch12_net_horizon.png")


def fig_ch13():
    """HTE: multiplicative RR flat vs additive ARR rising with risk."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    risk = np.array([5, 10, 15, 25, 35], dtype=float)  # control %
    rr = np.full_like(risk, 0.80)
    arr = risk * (1 - rr / 100 * 0 + 0)  # wrong
    arr = risk * (1 - 0.80)  # ARR = CER*(1-RR)
    ax = axes[0]
    ax.plot(risk, rr, "o-", color=GOLD, lw=2.4, ms=8)
    ax.set_ylim(0.5, 1.1)
    ax.axhline(1.0, color=GRAY, ls="--", lw=1)
    ax.set_xlabel("Baseline risk stratum (%)")
    ax.set_ylabel("Relative risk")
    ax.set_title("Multiplicative scale (flat RR)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.plot(risk, arr, "s-", color=TEAL, lw=2.4, ms=8)
    for x, a in zip(risk, arr):
        ax.text(x, a + 0.4, f"NNT={100/a:.0f}", ha="center", fontsize=7.5, color=INDIGO)
    ax.set_xlabel("Baseline risk stratum (%)")
    ax.set_ylabel("ARR (pp)")
    ax.set_title("Additive scale (rising ARR)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    fig.suptitle(
        "Subgroup residual: homogeneous RR ≠ homogeneous absolute benefit",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch13_hte_scales.png")


def fig_ch14():
    """AI deploy: AUROC held high while absolute impact ARR lags / decays."""
    fig, ax1 = plt.subplots(figsize=(10.4, 5.0))
    months = np.arange(0, 13)
    auroc = 0.88 - 0.01 * np.maximum(0, months - 6) * 0.5  # mild decay
    auroc = np.clip(auroc, 0.82, 0.88)
    # clinical impact ARR from alert-driven action (often near zero without workflow)
    impact = np.array([0.0, 0.2, 0.4, 0.5, 0.45, 0.35, 0.25, 0.2, 0.15, 0.12, 0.1, 0.08, 0.05])
    ax1.plot(months, auroc, "o-", color=GOLD, lw=2.3, ms=7, label="AUROC (discrimination)")
    ax1.set_ylabel("AUROC", color=GOLD)
    ax1.tick_params(axis="y", labelcolor=GOLD)
    ax1.set_ylim(0.70, 1.0)
    ax1.set_xlabel("Months post-deployment")
    ax2 = ax1.twinx()
    ax2.plot(months, impact, "s-", color=TEAL, lw=2.4, ms=7, label="Absolute outcome ARR (pp)")
    ax2.set_ylabel("Impact ARR (pp)", color=TEAL)
    ax2.tick_params(axis="y", labelcolor=TEAL)
    ax2.set_ylim(0, 1.2)
    ax1.axhline(0.85, color=GRAY, ls=":", lw=1)
    ax1.set_title(
        "AI residual: discrimination without absolute outcome impact is incomplete (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="center right")
    ax1.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle25_swarm_ch14_auroc_vs_impact.png")


def main():
    print("Cycle-25 →", OUT)
    fns = [
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
    ]
    for fn in fns:
        fn()
    print(f"Done: {len(fns)}")


if __name__ == "__main__":
    main()
