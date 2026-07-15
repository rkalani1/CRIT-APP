#!/usr/bin/env python3
"""
CRIT-APP Cycle-7 densify swarm: original matplotlib scientific teaching figures.

Targets residual floor chapters after cycles 1–6 (~7 imgs each):
  ch26 SR credibility ladder + CPR external validation absolute
  ch05 clone-censor-weight target-trial strategy (absolute risks)
  ch28 equity: same relative protocol, ARR by access delay
  ch19 estimation: precision vs bias on absolute (ARR) scale
  ch16 autopsy absolute recon sheet (second archetype)
  ch22 lead-time absolute harm / screening survival illusion
  ch12 MCID vs CI on absolute scale (NNT when CI includes 0)

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle7_swarm_* only). Does not redo cycle1–6 figures.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INDIGO = "#283593"
TEAL = "#00695C"
GOLD = "#F9A825"
CORAL = "#C62828"
SLATE = "#37474F"
WHITE = "#FFFFFF"
GREEN = "#2E7D32"
BLUE = "#1565C0"
ORANGE = "#EF6C00"
PURPLE = "#6A1B9A"
GRAY = "#90A4AE"


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch26_sr_cpr_ladder() -> Path:
    """SR risk-of-bias → pooled ARR credibility; CPR validation calibration."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("SR → pooled ARR credibility ladder", fontsize=10, fontweight="bold", color=INDIGO)
    rungs = [
        (7.9, CORAL, "Rung 1 · Question & protocol", "Pre-registered PICO? Living protocol?"),
        (6.0, ORANGE, "Rung 2 · Study eligibility", "Design match? Stroke phenotype locked?"),
        (4.1, GOLD, "Rung 3 · Risk of bias map", "RoB2/ROBINS domain heat → exclude fatal"),
        (2.2, TEAL, "Rung 4 · Absolute synthesis", "Pooled CER/EER → ARR/NNT + prediction interval"),
        (0.35, PURPLE, "Rung 5 · Transport decision", "Local mix · capacity · de-implement if fragile"),
    ]
    for y, edge, title, body in rungs:
        ax.add_patch(
            FancyBboxPatch(
                (0.4, y - 0.55),
                9.2,
                1.55,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.45,
            )
        )
        ax.text(0.7, y + 0.4, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y - 0.15, body, fontsize=8, color=SLATE, va="center")

    ax = axes[1]
    # Calibration in derivation vs external validation
    pred = np.linspace(0.05, 0.55, 8)
    obs_der = pred * 0.95 + 0.01
    obs_ext = 0.08 + 0.55 * pred  # overconfident externally
    ax.plot([0, 0.6], [0, 0.6], "--", color=GRAY, lw=1.3, label="Perfect")
    ax.plot(pred, obs_der, "o-", color=TEAL, lw=2, ms=7, label="Derivation (optimistic)")
    ax.plot(pred, obs_ext, "s-", color=CORAL, lw=2, ms=7, label="External site (miscalibrated)")
    ax.set_xlim(0, 0.6)
    ax.set_ylim(0, 0.6)
    ax.set_xlabel("Predicted absolute risk")
    ax.set_ylabel("Observed absolute risk")
    ax.set_title("CPR: discrimination can travel; calibration often does not", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.text(0.32, 0.08, "Do not invent NNT from derivation\nrisk strata without external audit", fontsize=8, color=CORAL, fontweight="bold")

    fig.suptitle(
        "Systematic reviews & CPRs: absolute credibility before pathway rewrite (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch26_sr_cpr_ladder.png")


def fig_ch05_clone_censor() -> Path:
    """Clone-censor-weight target-trial strategy with absolute risks."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Target-trial clone–censor–weight (time-varying start)", fontsize=10, fontweight="bold", color=INDIGO)

    ax.axvline(2.0, color=TEAL, lw=2.2)
    ax.text(2.0, 7.4, "eligibility\nt0", ha="center", fontsize=8, fontweight="bold", color=TEAL)
    ax.axvline(6.0, color=GOLD, lw=2.0)
    ax.text(6.0, 7.4, "strategy\nstart window", ha="center", fontsize=8, fontweight="bold", color=GOLD)

    # Clone A: treat-if-starts-by-day
    ax.plot([2, 11], [5.5, 5.5], color=INDIGO, lw=3.5, solid_capstyle="round")
    ax.plot(6.0, 5.5, "o", color=TEAL, ms=10)
    ax.text(2.2, 6.05, "Clone: initiate rehab ≤14d", fontsize=8, color=INDIGO, fontweight="bold")
    ax.text(6.2, 5.9, "starts", fontsize=7.5, color=TEAL)

    # Clone B: no initiate in window → censored when starts late
    ax.plot([2, 8.5], [3.2, 3.2], color=CORAL, lw=3.5, solid_capstyle="round")
    ax.plot(8.5, 3.2, "x", color=CORAL, ms=12, mew=2)
    ax.text(2.2, 3.75, "Clone: do not initiate in window", fontsize=8, color=CORAL, fontweight="bold")
    ax.text(8.7, 3.55, "censor at deviation", fontsize=7.5, color=CORAL)

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.35),
            11.2,
            1.8,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#E3F2FD",
            edgecolor=BLUE,
            lw=1.3,
        )
    )
    ax.text(
        6.0,
        1.25,
        "IPCWweights restore the strategy contrast after artificial censoring.\n"
        "Never credit survival before treatment as ‘treated’ person-time.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
    )

    ax = axes[1]
    labels = ["Naive\nimmortal-time\nARR", "Aligned t0\nlandmark ARR", "Clone–censor\nweighted ARR"]
    arr = np.array([12.0, 4.0, 3.5])
    colors = [CORAL, GOLD, TEAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, arr, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Absolute risk reduction (pp, synthetic)")
    ax.set_ylim(0, 15)
    ax.set_title("Strategy effects shrink after time-zero honesty", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, a in zip(bars, arr):
        ax.text(
            b.get_x() + b.get_width() / 2,
            a + 0.4,
            f"ARR {a:.1f} pp\nNNT ≈ {100 / a:.0f}",
            ha="center",
            fontsize=8,
            fontweight="bold",
            color=SLATE,
        )
    ax.text(1.0, 13.5, "prediction ≠ causation; confounded start times invent NNT", fontsize=8, color=PURPLE, style="italic", ha="center")

    fig.suptitle(
        "Confounding & target trials: clone–censor restores absolute strategy effects (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch05_clone_censor.png")


def fig_ch28_equity_arr_delay() -> Path:
    """Systems: same relative protocol, ARR collapses with access delay."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    delay = np.array([0, 30, 60, 90, 120, 180])  # minutes from ideal door
    # efficacy decays; CER high early
    cer = 0.40 - 0.0005 * delay  # slight
    rrr = 0.35 * np.exp(-delay / 140)
    arr = cer * rrr * 100
    ax.plot(delay, arr, "o-", color=INDIGO, lw=2.5, ms=8)
    ax.fill_between(delay, arr, alpha=0.12, color=INDIGO)
    ax.set_xlabel("Access delay beyond ideal door-to-puncture (min)")
    ax.set_ylabel("Absolute benefit (pp independent outcome)")
    ax.set_title("Same protocol, unequal absolute benefit by access", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    ax.set_ylim(0, 16)
    for d, a in zip(delay[::2], arr[::2]):
        ax.text(d, a + 0.6, f"ARR {a:.1f}\nNNT {100 / a:.0f}", ha="center", fontsize=7.5, color=SLATE)

    ax = axes[1]
    sites = ["CSC\nurban", "PSC+\ntransfer", "Rural\nlong haul"]
    arr_s = np.array([12.0, 6.5, 2.8])
    ari = np.array([2.0, 2.0, 2.0])  # fixed procedural harm
    x = np.arange(len(sites))
    w = 0.35
    ax.bar(x - w / 2, arr_s, width=w, color=TEAL, edgecolor=INDIGO, label="ARR benefit")
    ax.bar(x + w / 2, ari, width=w, color=CORAL, edgecolor=INDIGO, label="ARI harm (fixed)")
    ax.set_xticks(x)
    ax.set_xticklabels(sites, fontsize=9)
    ax.set_ylabel("Absolute percentage points")
    ax.set_ylim(0, 16)
    ax.set_title("Equity ledger: net absolute by system stratum", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    for i, (a, h) in enumerate(zip(arr_s, ari)):
        net = a - h
        col = GREEN if net > 0 else CORAL
        ax.text(i, max(a, h) + 0.8, f"net {net:+.1f} pp", ha="center", fontsize=8.5, fontweight="bold", color=col)

    fig.suptitle(
        "Systems of care: relative pathway claims hide access-stratified ARR (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch28_equity_arr_delay.png")


def fig_ch19_precision_bias_arr() -> Path:
    """Inference: precision vs bias on absolute ARR scale."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    # Four estimators: unbiased imprecise, biased precise, etc.
    names = ["Large biased\nregistry", "Small honest\nRCT", "Biased +\nprecise", "Unbiased +\nprecise"]
    point = np.array([9.0, 3.0, 8.5, 3.2])
    lo = point - np.array([1.0, 4.5, 0.8, 1.2])
    hi = point + np.array([1.0, 4.5, 0.8, 1.2])
    truth = 3.0
    y = np.arange(len(names))
    ax.axvline(truth, color=TEAL, lw=2, ls="--", label=f"True ARR = {truth:.0f} pp")
    ax.axvline(0, color=GRAY, lw=1)
    for i, (p, l, h, name) in enumerate(zip(point, lo, hi, names)):
        col = CORAL if abs(p - truth) > 3 else INDIGO
        ax.plot([l, h], [i, i], color=col, lw=3.5, solid_capstyle="round")
        ax.plot(p, i, "o", color=GOLD if abs(p - truth) > 3 else TEAL, ms=10, markeredgecolor=INDIGO)
    ax.set_yticks(y)
    ax.set_yticklabels(names, fontsize=8.5)
    ax.set_xlabel("Absolute risk reduction (pp)")
    ax.set_xlim(-3, 12)
    ax.set_title("Narrow CI ≠ correct ARR", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, axis="x", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Estimation culture checklist (absolute)", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (7.6, INDIGO, "Point + interval", "Always report ARR CI, not p alone"),
        (5.6, GOLD, "Compatibility", "Does CI include 0 and MCID?"),
        (3.6, CORAL, "Bias budget", "Precise wrong > imprecise right for pathways"),
        (1.6, TEAL, "NNT discipline", "If CI includes 0 → NNT CI to ∞"),
        (0.15, PURPLE, "Decision", "Act only if lower CI still clinically useful"),
    ]
    for y0, edge, title, body in rows:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y0 - 0.45),
                9.3,
                1.65,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.6, y0 + 0.5, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.6, y0 - 0.1, body, fontsize=8.2, color=SLATE, va="center")

    fig.suptitle(
        "Inference architecture: precision and bias compete on the absolute scale (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch19_precision_bias_arr.png")


def fig_ch16_autopsy_recon() -> Path:
    """Paper autopsy absolute recon sheet for observational rehab archetype."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Autopsy recon sheet · REHAB-like observational", fontsize=10, fontweight="bold", color=INDIGO)
    cells = [
        (8.0, INDIGO, "Claim", "‘Early rehab reduces 90-day dependence 40%’"),
        (6.2, GOLD, "Estimand board", "Who · when t0 · strategy · outcome · summary"),
        (4.4, CORAL, "Threat rank", "1 Immortal time  2 Indication  3 Missing mRS"),
        (2.6, TEAL, "Absolute rebuild", "Crude ARR 12 pp → aligned ARR ~3–4 pp"),
        (0.8, PURPLE, "Action", "Adapt+audit only · do not rewrite staffing on crude"),
    ]
    for y, edge, title, body in cells:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y - 0.55),
                9.3,
                1.5,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.35,
            )
        )
        ax.text(0.6, y + 0.35, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.6, y - 0.2, body, fontsize=8.2, color=SLATE, va="center")

    ax = axes[1]
    labels = ["Press-release\nRRR frame", "Crude ARR\n(biased t0)", "Aligned\nlandmark ARR", "Harm ARI\nfalls/fatigue"]
    vals = [40, 12, 3.5, 1.5]
    colors = [CORAL, ORANGE, TEAL, GOLD]
    x = np.arange(len(labels))
    bars = ax.bar(x, vals, color=colors, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Reported number (mixed units — teaching)")
    ax.set_title("Autopsy forces unit honesty", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    notes = ["RRR %", "pp", "pp", "pp"]
    for b, v, n in zip(bars, vals, notes):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.2, f"{v:g} {n}", ha="center", fontsize=8, fontweight="bold", color=SLATE)
    ax.text(1.5, 36, "Never leave the autopsy in relative units only", fontsize=8, color=PURPLE, style="italic", ha="center")

    fig.suptitle(
        "Paper autopsies: absolute recon sheet before the verdict (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch16_autopsy_recon.png")


def fig_ch22_lead_time_harm() -> Path:
    """Screening: lead-time survival illusion + absolute overdiagnosis harm."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Lead time lengthens ‘survival’ without delaying death", fontsize=10, fontweight="bold", color=INDIGO)

    # Unscreened
    ax.plot([4, 10], [5.8, 5.8], color=CORAL, lw=4, solid_capstyle="round")
    ax.plot(4, 5.8, "o", color=CORAL, ms=9)
    ax.plot(10, 5.8, "x", color=CORAL, ms=11, mew=2)
    ax.text(4, 6.45, "clinical dx", fontsize=8, color=CORAL, ha="center", fontweight="bold")
    ax.text(10, 6.45, "death", fontsize=8, color=CORAL, ha="center")
    ax.text(7, 5.2, "survival from dx = 6 y", ha="center", fontsize=8, color=SLATE)

    # Screened
    ax.plot([2, 10], [3.0, 3.0], color=TEAL, lw=4, solid_capstyle="round")
    ax.plot(2, 3.0, "o", color=TEAL, ms=9)
    ax.plot(10, 3.0, "x", color=TEAL, ms=11, mew=2)
    ax.text(2, 3.65, "screen dx", fontsize=8, color=TEAL, ha="center", fontweight="bold")
    ax.text(10, 3.65, "same death", fontsize=8, color=TEAL, ha="center")
    ax.annotate(
        "",
        xy=(4, 3.0),
        xytext=(2, 3.0),
        arrowprops=dict(arrowstyle="<->", color=GOLD, lw=2),
    )
    ax.text(3, 2.35, "lead time\n(+2 y ‘survival’)", ha="center", fontsize=8, color=GOLD, fontweight="bold")
    ax.text(7, 2.35, "survival from dx = 8 y (illusion)", ha="center", fontsize=8, color=SLATE)

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.35),
            11.2,
            1.4,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.2,
        )
    )
    ax.text(
        6.0,
        1.05,
        "Appraise screening with mortality / disability rates from RCTs—not survival-from-diagnosis.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
    )

    ax = axes[1]
    cats = ["True early\ncures", "Overdiagnosed\n(harm net)", "False +\nworkups"]
    n = np.array([3, 18, 40])  # per 1000 screened synthetic
    colors = [TEAL, CORAL, ORANGE]
    x = np.arange(len(cats))
    bars = ax.bar(x, n, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylabel("Events per 1,000 screened (synthetic)")
    ax.set_title("Absolute harm ledger often dwarfs true benefit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, n):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.2, str(v), ha="center", fontsize=10, fontweight="bold", color=SLATE)
    ax.text(1.0, 45, "NNS and absolute overdiagnosis before pathway expansion", fontsize=8, color=PURPLE, style="italic", ha="center")

    fig.suptitle(
        "Screening appraisal: lead-time illusion + absolute overdiagnosis harm (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch22_lead_time_harm.png")


def fig_ch12_mcid_ci_nnt() -> Path:
    """Effect sizes: MCID vs ARR CI; NNT → ∞ when CI includes 0."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    ax = axes[0]
    ax.set_xlim(-4, 12)
    ax.set_ylim(0, 5)
    ax.axvline(0, color=GRAY, lw=1.3)
    ax.axvline(2.0, color=GOLD, lw=2, ls="--")
    ax.text(2.0, 4.55, "MCID = 2 pp", ha="center", fontsize=8.5, color=GOLD, fontweight="bold")
    # three study CIs
    studies = [
        (3.5, 1.5, 5.5, TEAL, "Study A: CI above MCID"),
        (2.2, -0.5, 4.8, ORANGE, "Study B: includes 0 & MCID"),
        (0.8, -1.5, 3.0, CORAL, "Study C: mostly below MCID"),
    ]
    for i, (pt, lo, hi, col, lab) in enumerate(studies):
        y = 3.4 - i * 1.1
        ax.plot([lo, hi], [y, y], color=col, lw=4, solid_capstyle="round")
        ax.plot(pt, y, "o", color=col, ms=10, markeredgecolor=INDIGO)
        ax.text(8.2, y, lab, fontsize=8, color=col, va="center", fontweight="bold")
    ax.set_xlabel("Absolute risk reduction (pp)")
    ax.set_yticks([])
    ax.set_title("Clinical importance ≠ statistical significance", fontsize=10, fontweight="bold", color=INDIGO)
    for sp in ("top", "right", "left"):
        ax.spines[sp].set_visible(False)

    ax = axes[1]
    # NNT point and when CI includes 0
    labels = ["ARR 4 pp\nCI 2 to 6", "ARR 2 pp\nCI 0.5 to 3.5", "ARR 1.5 pp\nCI −1 to 4"]
    nnt_pt = [25, 50, 67]
    # display upper NNT as large when crosses 0
    nnt_hi = [50, 200, np.nan]  # nan → infinity
    x = np.arange(len(labels))
    bars = ax.bar(x, nnt_pt, color=[TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Point NNT (1/ARR)")
    ax.set_ylim(0, 100)
    ax.set_title("If ARR CI includes 0 → NNT CI to ∞", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, (b, pt, hi) in enumerate(zip(bars, nnt_pt, nnt_hi)):
        if np.isnan(hi):
            txt = f"NNT {pt}\nCI → ∞"
        else:
            txt = f"NNT {pt}\nCI to {hi:.0f}"
        ax.text(b.get_x() + b.get_width() / 2, pt + 3, txt, ha="center", fontsize=8.5, fontweight="bold", color=SLATE)
    ax.text(1.0, 90, "Do not pathway-rewrite on an NNT whose CI explodes", fontsize=8, color=PURPLE, style="italic", ha="center")

    fig.suptitle(
        "Absolute benefit: MCID, ARR compatibility intervals, and honest NNT (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle7_swarm_ch12_mcid_ci_nnt.png")


def main() -> None:
    print("Cycle-7 swarm densify figures →", OUT)
    writers = [
        fig_ch26_sr_cpr_ladder,
        fig_ch05_clone_censor,
        fig_ch28_equity_arr_delay,
        fig_ch19_precision_bias_arr,
        fig_ch16_autopsy_recon,
        fig_ch22_lead_time_harm,
        fig_ch12_mcid_ci_nnt,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
