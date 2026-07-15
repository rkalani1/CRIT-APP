#!/usr/bin/env python3
"""CRIT-APP Cycle-26 densify: clear residual floor-12 → uniform floor ≥13.

14 original scientific Agg indigo plots for ch15–ch28 (remaining half-book).
Prefer continuous scientific graphics over decorative bars.
ARR/NNT; pred≠cause. cycle26_swarm_* only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
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
    """Journal club: pre-spec scorecard radar-like multi-axis absolute board."""
    fig, ax = plt.subplots(figsize=(10.4, 5.2), subplot_kw=dict(polar=True))
    labels = [
        "Primary\nendpoint",
        "Absolute\nARR/NNT",
        "Bias\nrisk",
        "Transport",
        "Spin\nabsent",
        "Action\nsentence",
    ]
    N = len(labels)
    angles = np.linspace(0, 2 * np.pi, N, endpoint=False).tolist()
    good = [0.95, 0.90, 0.85, 0.80, 0.90, 0.85]
    spun = [0.70, 0.25, 0.40, 0.55, 0.20, 0.90]
    angles_c = angles + angles[:1]
    good_c = good + good[:1]
    spun_c = spun + spun[:1]
    ax.plot(angles_c, good_c, "o-", color=TEAL, lw=2.2, label="Disciplined JC")
    ax.fill(angles_c, good_c, color=TEAL, alpha=0.12)
    ax.plot(angles_c, spun_c, "s-", color=CORAL, lw=2.2, label="Spin-prone JC")
    ax.fill(angles_c, spun_c, color=CORAL, alpha=0.10)
    ax.set_xticks(angles)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylim(0, 1.0)
    ax.set_yticks([0.25, 0.5, 0.75])
    ax.set_title(
        "Journal club residual: absolute ARR/NNT axis separates disciplined from spin-prone sessions",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        pad=18,
    )
    ax.legend(loc="upper right", bbox_to_anchor=(1.25, 1.1), fontsize=8)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch15_jc_radar.png")


def fig_ch16():
    """Paper autopsy: multi-axis severity → absolute action mapping (scatter)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(11)
    # synthetic autopsy scores
    internal = rng.uniform(0.2, 0.95, 18)
    absolute = rng.uniform(0.1, 0.9, 18)
    # force clusters
    internal[:6] = rng.uniform(0.7, 0.95, 6)
    absolute[:6] = rng.uniform(0.65, 0.95, 6)
    internal[6:12] = rng.uniform(0.4, 0.7, 6)
    absolute[6:12] = rng.uniform(0.3, 0.6, 6)
    internal[12:] = rng.uniform(0.15, 0.45, 6)
    absolute[12:] = rng.uniform(0.1, 0.4, 6)
    cols = [TEAL] * 6 + [GOLD] * 6 + [CORAL] * 6
    labs_pts = ["adopt/adapt"] * 6 + ["wait/adapt"] * 6 + ["reject"] * 6
    for x, y, c in zip(internal, absolute, cols):
        ax.scatter(x, y, s=90, color=c, edgecolors=INDIGO, zorder=3)
    ax.axhline(0.5, color=GRAY, ls="--", lw=1)
    ax.axvline(0.5, color=GRAY, ls="--", lw=1)
    ax.text(0.78, 0.88, "Adopt/adapt", color=TEAL, fontsize=9, fontweight="bold")
    ax.text(0.55, 0.22, "Valid but tiny absolute", color=GOLD, fontsize=8, fontweight="bold")
    ax.text(0.18, 0.18, "Reject", color=CORAL, fontsize=9, fontweight="bold")
    ax.set_xlabel("Internal validity score (teaching 0–1)")
    ax.set_ylabel("Absolute effect credibility / magnitude (0–1)")
    ax.set_title(
        "Autopsy residual: validity × absolute magnitude jointly map to action",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch16_autopsy_map.png")


def fig_ch17():
    """Incidence, prevalence, duration surface: P ≈ I × D with absolute teaching grid."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    I = np.linspace(0.5, 8, 80)  # /100 py
    for D, c, ls in [(2, TEAL, "-"), (5, INDIGO, "--"), (10, CORAL, "-.")]:
        P = I * D  # crude teaching
        ax.plot(I, P, color=c, lw=2.3, ls=ls, label=f"Duration = {D} y → P≈I×D")
    ax.set_xlabel("Incidence I (events / 100 person-years)")
    ax.set_ylabel("Prevalence P (per 100, teaching)")
    ax.set_title(
        "Disease frequency residual: prevalence is a stock; NNT needs risk/incidence",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.annotate(
        "Do not compute NNT from crude prevalence alone",
        xy=(6, 50),
        xytext=(3.5, 70),
        fontsize=8.5,
        fontweight="bold",
        color=CORAL,
        arrowprops=dict(arrowstyle="->", color=CORAL),
    )
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch17_ixd_surface.png")


def fig_ch18():
    """Causal credibility vs association strength: absolute ARR confidence ladder curve."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    steps = np.array([1, 2, 3, 4, 5, 6])
    labels = [
        "Crude\nassoc",
        "Adjusted\nobs",
        "New-user\nACNU",
        "Target\ntrial",
        "RCT",
        "Multi-RCT\n+ local ARR",
    ]
    credibility = np.array([0.15, 0.30, 0.45, 0.60, 0.85, 0.95])
    abs_claim = np.array([8.0, 6.5, 4.5, 3.8, 3.5, 3.4])  # claimed ARR shrinks toward truth
    ax.plot(steps, credibility, "o-", color=TEAL, lw=2.4, ms=9, label="Causal credibility")
    ax.set_ylabel("Causal credibility (0–1)", color=TEAL)
    ax.tick_params(axis="y", labelcolor=TEAL)
    ax.set_xticks(steps)
    ax.set_xticklabels(labels, fontsize=8)
    ax2 = ax.twinx()
    ax2.plot(steps, abs_claim, "s--", color=CORAL, lw=2.2, ms=8, label="Claimed ARR (pp)")
    ax2.set_ylabel("Claimed absolute ARR (pp)", color=CORAL)
    ax2.tick_params(axis="y", labelcolor=CORAL)
    ax.set_title(
        "Causation residual: association strength ≠ absolute causal ARR credibility",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="center right")
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch18_causal_ladder.png")


def fig_ch19():
    """CI width and decision zones for absolute ARR across n."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    n = np.array([50, 100, 200, 400, 800, 1600, 3200])
    arr = 0.04  # true 4 pp
    # SE of risk difference ≈ sqrt(p1(1-p1)/n1 + p0(1-p0)/n0) with equal n/2
    p0, p1 = 0.20, 0.16
    se = np.sqrt(p1 * (1 - p1) / (n / 2) + p0 * (1 - p0) / (n / 2))
    lo = (arr - 1.96 * se) * 100
    hi = (arr + 1.96 * se) * 100
    ax.fill_between(n, lo, hi, color=INDIGO, alpha=0.18, label="95% CI for ARR")
    ax.plot(n, np.full_like(n, arr * 100, dtype=float), color=TEAL, lw=2.4, label="Point ARR 4 pp")
    ax.axhline(0, color=CORAL, ls="--", lw=1.3)
    ax.axhline(2, color=GOLD, ls=":", lw=1.3)
    ax.text(2200, 2.3, "clinical importance floor", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xscale("log")
    ax.set_xlabel("Total sample size n (log scale)")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title(
        "Inference residual: absolute precision and decision zones scale with n",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, alpha=0.3, which="both")
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch19_arr_ci_n.png")


def fig_ch20():
    """Hazard ratio vs absolute risk difference over time (survival literacy)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0.1, 36, 120)  # months
    # constant HR=0.75, baseline hazard
    h0 = 0.03
    s0 = np.exp(-h0 * t)
    s1 = np.exp(-h0 * 0.75 * t)
    arr_t = (s1 - s0) * 100  # survival gain as absolute %
    # also show risk of event
    risk0 = (1 - s0) * 100
    risk1 = (1 - s1) * 100
    ax.plot(t, risk0, color=GRAY, lw=2.0, label="Control event risk %")
    ax.plot(t, risk1, color=TEAL, lw=2.0, label="Treated event risk %")
    ax.plot(t, risk0 - risk1, color=INDIGO, lw=2.5, label="Absolute RD(t) = ARR(t)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xlabel("Months from index")
    ax.set_ylabel("Absolute risk / difference (pp)")
    ax.set_title(
        "Regression residual: constant HR ≠ constant absolute ARR over time",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(
        20,
        max(risk0) * 0.55,
        "HR=0.75 fixed\nARR grows then plateaus",
        fontsize=8.5,
        fontweight="bold",
        color=INDIGO,
        bbox=dict(boxstyle="round,pad=0.3", facecolor=WHITE, edgecolor=INDIGO),
    )
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch20_hr_vs_arr_t.png")


def fig_ch21():
    """Interaction: RERI / additive vs multiplicative absolute panel."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    # risks
    r00, r10, r01, r11 = 0.05, 0.10, 0.12, 0.30
    ax = axes[0]
    labs = ["Neither", "A only", "B only", "A+B"]
    risks = [r00, r10, r01, r11]
    expected_add = r00 + (r10 - r00) + (r01 - r00)
    ax.bar(range(4), [r * 100 for r in risks], color=[GRAY, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.axhline(expected_add * 100, color=INDIGO, ls="--", lw=1.5, label=f"Additive expect {expected_add*100:.0f}%")
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Absolute risks by exposure", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    reri = r11 - r10 - r01 + r00
    mult_rr = (r11 / r00) / ((r10 / r00) * (r01 / r00))
    ax.bar([0, 1], [reri * 100, (mult_rr - 1) * 10], color=[INDIGO, GOLD], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels([f"RERI\n{reri*100:.1f} pp", f"Multiplicative\nRR ratio {mult_rr:.2f}"], fontsize=9)
    ax.set_ylabel("Interaction metric (scaled teaching)")
    ax.set_title("Additive RERI vs multiplicative", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle(
        "Interaction residual: report absolute RERI, not multiplicative p alone",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch21_reri_abs.png")


def fig_ch22():
    """Lead-time / length-time absolute: stage shift without mortality ARR."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    ax = axes[0]
    stages = ["I", "II", "III", "IV"]
    no_scr = [15, 25, 35, 25]
    scr = [35, 30, 20, 15]
    x = np.arange(4)
    w = 0.35
    ax.bar(x - w / 2, no_scr, width=w, color=GRAY, edgecolor=INDIGO, label="No screen")
    ax.bar(x + w / 2, scr, width=w, color=TEAL, edgecolor=INDIGO, label="Screened")
    ax.set_xticks(x)
    ax.set_xticklabels(stages)
    ax.set_ylabel("% of detections")
    ax.set_title("Stage shift (not proof of benefit)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    years = np.array([0, 1, 2, 3, 4, 5])
    # disease-specific mortality identical
    mort = 100 - np.array([0, 4, 9, 14, 20, 26])
    ax.plot(years, mort, "o-", color=CORAL, lw=2.3, label="Disease mortality (both arms)")
    # survival from diagnosis looks better with lead time
    surv_dx = 100 - np.array([0, 2, 5, 9, 14, 18])
    ax.plot(years, surv_dx, "s--", color=GOLD, lw=2.1, label="Survival from diagnosis (lead-time)")
    ax.set_xlabel("Years")
    ax.set_ylabel("%")
    ax.set_title("Absolute mortality vs lead-time clock", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)
    fig.suptitle(
        "Screening residual: stage shift ≠ absolute mortality ARR",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch22_stage_vs_mort.png")


def fig_ch23():
    """Base-rate neglect: absolute post-test vs intuitive relative-only path."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    priors = np.array([1, 5, 10, 20, 40])  # %
    lr = 5.0
    posts = []
    for p in priors / 100:
        odds = p / (1 - p)
        post = (odds * lr) / (1 + odds * lr)
        posts.append(post * 100)
    posts = np.array(posts)
    # intuitive wrong: treat LR as additive percentage points
    wrong = np.clip(priors + 40, 0, 99)  # "feels like +40%"
    ax.plot(priors, posts, "o-", color=TEAL, lw=2.5, ms=9, label="Bayes absolute post-test (LR+=5)")
    ax.plot(priors, wrong, "s--", color=CORAL, lw=2.2, ms=8, label="Base-rate neglect (relative intuition)")
    ax.set_xlabel("Pre-test absolute probability (%)")
    ax.set_ylabel("Post-test absolute probability (%)")
    ax.set_title(
        "Reasoning residual: absolute Bayes update vs base-rate neglect",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 45)
    ax.set_ylim(0, 100)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch23_bayes_baserate.png")


def fig_ch24():
    """Therapy/harm: benefit-harm plane with NNT/NNH iso-lines."""
    fig, ax = plt.subplots(figsize=(10.2, 5.2))
    arr = np.linspace(0.5, 12, 80)
    for nnh, c in [(20, GRAY), (50, GOLD), (100, TEAL)]:
        ari = 100 / nnh
        ax.axhline(ari, color=c, ls="--", lw=1.2, alpha=0.8)
        ax.text(10.5, ari + 0.15, f"NNH={nnh}", color=c, fontsize=8, fontweight="bold")
    # net > 0 region
    ari_grid = np.linspace(0, 8, 80)
    ARR, ARI = np.meshgrid(arr, ari_grid)
    net = ARR - ARI
    ax.contourf(ARR, ARI, net, levels=[-20, 0, 20], colors=["#FFCDD2", "#E8F5E9"], alpha=0.45)
    # example therapies
    pts = [(5.0, 1.2, "Tx A"), (2.0, 2.5, "Tx B"), (8.0, 0.8, "Tx C")]
    for x, y, lab in pts:
        ax.scatter([x], [y], s=100, color=INDIGO, zorder=5, edgecolors=WHITE)
        ax.text(x + 0.2, y + 0.15, lab, fontsize=9, fontweight="bold", color=INDIGO)
    ax.set_xlabel("ARR benefit (pp)")
    ax.set_ylabel("ARI harm (pp)")
    ax.set_title(
        "Therapy residual: plot absolute benefit vs absolute harm on one plane",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.text(8, 6.5, "Net harm", color=CORAL, fontsize=9, fontweight="bold")
    ax.text(8, 1.0, "Net benefit", color=TEAL, fontsize=9, fontweight="bold")
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch24_benefit_harm_plane.png")


def fig_ch25():
    """Dx vs px papers: LR natural frequencies + prognostic horizon risks dual panel."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    ax = axes[0]
    # 1000 patients, prior 10%, Se 90% Sp 80% → LR+ = 4.5
    prior = 100
    disease = 100
    well = 900
    tp, fn = 90, 10
    fp, tn = 180, 720
    # post-test if test+
    post_pos = tp / (tp + fp) * 100
    ax.bar(
        [0, 1, 2],
        [10, post_pos, tn / (fn + tn) * 100],
        color=[GRAY, TEAL, INDIGO],
        edgecolor=INDIGO,
        width=0.55,
    )
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(["Pre-test %", "Post | test+", "Post | test−"], fontsize=8.5)
    ax.set_ylabel("Absolute probability %")
    ax.set_title("Dx: natural-frequency absolute update", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    horiz = ["7 d", "30 d", "90 d", "1 y"]
    risks = [4, 9, 16, 28]
    ax.plot(range(4), risks, "o-", color=CORAL, lw=2.4, ms=9)
    for i, r in enumerate(risks):
        ax.text(i, r + 1.2, f"{r}%", ha="center", fontsize=8, fontweight="bold", color=CORAL)
    ax.set_xticks(range(4))
    ax.set_xticklabels(horiz, fontsize=9)
    ax.set_ylabel("Absolute event risk %")
    ax.set_title("Px: horizon-specific absolute risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 35)
    ax.grid(True, alpha=0.3)
    fig.suptitle(
        "Dx/Px residual: absolute post-test probability ≠ prognostic horizon risk (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch25_dx_px_absolute.png")


def fig_ch26():
    """CPR maturity: derivation → validation → impact absolute ARR path."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    stages = np.array([1, 2, 3, 4, 5])
    labs = ["Derivation\nc-stat", "Internal\nvalid.", "External\nvalid.", "Impact\nRCT", "Local\nARR"]
    # performance metrics rescaled
    cstat = [0.86, 0.84, 0.74, 0.74, 0.74]
    impact = [0, 0, 0, 1.5, 0.8]  # absolute ARR pp when used
    ax.plot(stages, cstat, "o-", color=GOLD, lw=2.3, ms=9, label="c-statistic")
    ax.set_ylabel("c-statistic", color=GOLD)
    ax.tick_params(axis="y", labelcolor=GOLD)
    ax.set_xticks(stages)
    ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_ylim(0.5, 1.0)
    ax2 = ax.twinx()
    ax2.bar(stages, impact, color=TEAL, alpha=0.45, edgecolor=INDIGO, width=0.45, label="Impact ARR (pp)")
    ax2.set_ylabel("Absolute impact ARR (pp)", color=TEAL)
    ax2.tick_params(axis="y", labelcolor=TEAL)
    ax2.set_ylim(0, 3)
    ax.set_title(
        "CPR residual: derivation discrimination ≠ absolute clinical impact ARR",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="upper right")
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch26_cpr_impact_path.png")


def fig_ch27():
    """Fragility index surface: events flipped vs p and absolute ARR margin."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # synthetic: FI vs sample size for fixed thin ARR
    n = np.array([100, 200, 400, 800, 1600])
    # thinner absolute margins more fragile
    fi_thin = np.array([1, 2, 3, 4, 6])  # ARR 1.5pp
    fi_mod = np.array([3, 5, 9, 14, 22])  # ARR 4pp
    fi_rob = np.array([8, 14, 25, 40, 70])  # ARR 8pp
    ax.plot(n, fi_thin, "o-", color=CORAL, lw=2.3, label="Thin ARR ~1.5 pp")
    ax.plot(n, fi_mod, "s-", color=GOLD, lw=2.3, label="Moderate ARR ~4 pp")
    ax.plot(n, fi_rob, "^-", color=TEAL, lw=2.3, label="Robust ARR ~8 pp")
    ax.axhline(5, color=GRAY, ls="--", lw=1.2)
    ax.text(900, 6, "FI < 5: fragile absolute claim", color=GRAY, fontsize=8, fontweight="bold")
    ax.set_xlabel("Sample size n")
    ax.set_ylabel("Fragility index (events to tip significance)")
    ax.set_title(
        "Fragility residual: p<0.05 with thin absolute margins is still fragile",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch27_fragility_surface.png")


def fig_ch28():
    """Systems/policy: absolute frequencies communication vs relative-only consent."""
    fig, ax = plt.subplots(figsize=(10.6, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title(
        "Policy residual: absolute frequency communication for systems & consent",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    # two columns
    ax.add_patch(
        FancyBboxPatch(
            (0.3, 0.5),
            4.4,
            6.5,
            boxstyle="round,pad=0.04,rounding_size=0.1",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.6,
        )
    )
    ax.add_patch(
        FancyBboxPatch(
            (5.3, 0.5),
            4.4,
            6.5,
            boxstyle="round,pad=0.04,rounding_size=0.1",
            facecolor="#E8F5E9",
            edgecolor=TEAL,
            lw=1.6,
        )
    )
    ax.text(2.5, 6.5, "Relative-only (avoid)", ha="center", fontsize=11, fontweight="bold", color=CORAL)
    ax.text(7.5, 6.5, "Absolute frequencies", ha="center", fontsize=11, fontweight="bold", color=TEAL)
    left = [
        "\"50% relative reduction\"",
        "No baseline stated",
        "NNT hidden",
        "Harm as separate story",
        "Press-release framing",
    ]
    right = [
        "12/100 → 6/100 events",
        "ARR 6 pp · NNT ≈ 17",
        "ARI 1/100 · NNH ≈ 100",
        "Same horizon for both",
        "Out of 100 patients…",
    ]
    for i, (L, R) in enumerate(zip(left, right)):
        y = 5.4 - i * 0.95
        ax.text(2.5, y, L, ha="center", fontsize=9, color=SLATE)
        ax.text(7.5, y, R, ha="center", fontsize=9, fontweight="bold", color=INDIGO)
    fig.tight_layout()
    return _save(fig, "cycle26_swarm_ch28_abs_comm.png")


def main():
    print("Cycle-26 →", OUT)
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
