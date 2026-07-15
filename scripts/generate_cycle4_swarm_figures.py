#!/usr/bin/env python3
"""
CRIT-APP Cycle-4 densify swarm: original matplotlib scientific teaching figures.

Targets residual lowest-image chapters after cycles 1–3 (~6 imgs each):
  ch28 systems of care / transportability / absolute counseling
  ch22 screening length-time bias and overdiagnosis
  ch19 inference: ARR CI that crosses null → NNT through infinity
  ch16 paper autopsy absolute-effect reconstruction (CLEAR-PATH synthetic)
  ch10 fixed-effect vs random-effects weight paradox
  ch12 net absolute benefit flips with baseline risk (ARR − ARI)

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle4_swarm_* only). Does not redo cycle1/2/3 figures.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Ellipse
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INDIGO = "#283593"
TEAL = "#00695C"
GOLD = "#F9A825"
CORAL = "#C62828"
SLATE = "#37474F"
LIGHT = "#ECEFF1"
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


def fig_ch28_transport_arr() -> Path:
    """Trial ARR attenuates as co-intervention package is lost from hub → spoke."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.05))

    # Left: stacked co-intervention package that carries the effect
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("What carried the trial ARR? (co-intervention package)", fontsize=10, fontweight="bold", color=INDIGO)

    layers = [
        (7.4, TEAL, "Operator volume & 24/7 EVT team"),
        (5.7, BLUE, "CTA + advanced imaging within minutes"),
        (4.0, PURPLE, "1:1 ICU / arterial-line titration"),
        (2.3, ORANGE, "Door-to-puncture system discipline"),
        (0.6, GOLD, "Transfer network & exclusion discipline"),
    ]
    for y, edge, lab in layers:
        ax.add_patch(
            FancyBboxPatch(
                (0.5, y),
                9.0,
                1.45,
                boxstyle="round,pad=0.04,rounding_size=0.1",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.6,
            )
        )
        ax.text(5.0, y + 0.72, lab, ha="center", va="center", fontsize=9, color=edge, fontweight="bold")

    ax.text(
        5.0,
        9.35,
        "Efficacy is not a free-floating RR — it rides on infrastructure",
        ha="center",
        fontsize=8.2,
        color=SLATE,
        style="italic",
    )

    # Right: expected ARR attenuation
    ax = axes[1]
    settings = ["Trial\n(ideal package)", "Hub CSC\n(near match)", "PSC spoke\n(partial)", "Resource-\nlimited"]
    # Synthetic teaching ARR % for independence at 90 d
    arr = np.array([10.3, 8.0, 4.5, 1.5])
    colors = [TEAL, GREEN, GOLD, CORAL]
    x = np.arange(len(settings))
    bars = ax.bar(x, arr, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(settings, fontsize=8.5)
    ax.set_ylabel("Expected ARR for mRS 0–2 (pp, synthetic)")
    ax.set_ylim(0, 13.5)
    ax.set_title("Transportability: ARR shrinks when the package breaks", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    nnts = [round(100 / a) for a in arr]
    for b, v, n in zip(bars, arr, nnts):
        ax.text(
            b.get_x() + b.get_width() / 2,
            v + 0.35,
            f"{v:.1f} pp\nNNT≈{n}",
            ha="center",
            fontsize=8,
            fontweight="bold",
            color=SLATE,
        )
    ax.axhline(10.3, color=TEAL, ls="--", lw=1.1, alpha=0.7)
    ax.text(3.05, 10.5, "trial ARR", fontsize=7.5, color=TEAL, ha="right")

    fig.suptitle(
        "Systems of care: trial ARR is not portable without co-interventions (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch28_transport_arr.png")


def fig_ch22_length_overdiagnosis() -> Path:
    """Length-time preferential capture of indolent lesions + overdiagnosis harm."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.05))

    # Left: length-time — aggressive vs indolent sojourn windows
    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Length-time bias: screening favors slow biology", fontsize=10, fontweight="bold", color=INDIGO)

    # Aggressive: short sojourn
    ax.plot([1.0, 3.0], [6.2, 6.2], color=CORAL, lw=8, solid_capstyle="round")
    ax.plot([1.0, 3.0], [6.2, 6.2], color=CORAL, lw=2, marker="|", ms=14, mew=2)
    ax.text(2.0, 6.85, "Aggressive lesion\n(short sojourn)", ha="center", fontsize=8.2, color=CORAL, fontweight="bold")
    ax.text(2.0, 5.45, "Often presents clinically\nbefore screen visit", ha="center", fontsize=7.5, color=SLATE)

    # Indolent: long sojourn
    ax.plot([1.0, 10.5], [3.4, 3.4], color=TEAL, lw=8, solid_capstyle="round")
    ax.plot([1.0, 10.5], [3.4, 3.4], color=TEAL, lw=2, marker="|", ms=14, mew=2)
    ax.text(5.75, 4.15, "Indolent lesion (long sojourn)", ha="center", fontsize=8.2, color=TEAL, fontweight="bold")
    ax.text(5.75, 2.65, "Much more likely to be screen-detected", ha="center", fontsize=7.5, color=SLATE)

    # Screen visit line
    ax.axvline(6.0, color=GOLD, ls="--", lw=1.6)
    ax.text(6.0, 7.55, "Screen day", ha="center", fontsize=8, color=GOLD, fontweight="bold")
    ax.annotate(
        "",
        xy=(6.0, 3.55),
        xytext=(6.0, 5.0),
        arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.5),
    )
    ax.text(6.5, 4.7, "captured", fontsize=8, color=GOLD, fontweight="bold")

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.25),
            11.2,
            1.7,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.2,
        )
    )
    ax.text(
        6.0,
        1.1,
        "Screen-detected cohorts are enriched for indolent biology.\nComparing them to clinically detected cases credits screening for natural history.",
        ha="center",
        va="center",
        fontsize=8,
        color=SLATE,
    )

    # Right: overdiagnosis natural frequencies
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Overdiagnosis ≠ false positive (synthetic N=100)", fontsize=10, fontweight="bold", color=INDIGO)

    rows = [
        (8.0, TEAL, "True lesions found", "25 small aneurysms on screening MRA"),
        (6.0, GOLD, "Would never rupture in life", "≈18 overdiagnosed (die with, not of)"),
        (4.0, CORAL, "If all 25 treated today", "3–5 procedural strokes (pure harm on overdiagnosed)"),
        (2.0, INDIGO, "Appraisal demand", "Outcome benefit from invitation RCT — not detection yield"),
        (0.35, PURPLE, "Communication", "Per 100 like yours: <1 rupture/year vs 3–5 procedure strokes"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.55),
                9.4,
                1.7,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.35,
            )
        )
        ax.text(0.55, y + 0.45, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.2, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Screening traps: length-time enrichment and overdiagnosis (synthetic neurovascular)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch22_length_overdiagnosis.png")


def fig_ch19_nnt_infinity() -> Path:
    """ARR CI crossing null → NNT CI discontinuous through infinity."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.05))

    # Left: ARR on number line with CI
    ax = axes[0]
    arr_pt = 0.02  # 2 pp
    arr_lo, arr_hi = -0.01, 0.05  # crosses 0
    ax.axhline(0, color=LIGHT, lw=0.5)
    ax.axvline(0, color=SLATE, lw=1.4, label="Null ARR = 0")
    ax.axvline(0.03, color=GOLD, ls="--", lw=1.3, label="MCID ≈ 3 pp (example)")
    # CI bar
    ax.plot([arr_lo * 100, arr_hi * 100], [1.0, 1.0], color=INDIGO, lw=4, solid_capstyle="round")
    ax.plot(arr_pt * 100, 1.0, "o", color=TEAL, ms=12, zorder=5)
    ax.plot([arr_lo * 100, arr_hi * 100], [1.0, 1.0], "|", color=INDIGO, ms=16, mew=2)
    ax.text(arr_pt * 100, 1.35, f"ARR {arr_pt*100:.0f} pp", ha="center", fontsize=9, color=TEAL, fontweight="bold")
    ax.text(arr_lo * 100, 0.55, f"{arr_lo*100:.0f}", ha="center", fontsize=8, color=CORAL)
    ax.text(arr_hi * 100, 0.55, f"{arr_hi*100:.0f}", ha="center", fontsize=8, color=GREEN)
    ax.set_xlim(-3.5, 7.5)
    ax.set_ylim(0, 2.2)
    ax.set_xlabel("Absolute risk reduction (percentage points)")
    ax.set_yticks([])
    ax.set_title("Estimation: point ARR with 95% CI crossing null", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, axis="x", alpha=0.3)
    ax.text(
        2.0,
        1.85,
        "Compatible with harm (−1), null, and benefit (+5)",
        ha="center",
        fontsize=8,
        color=SLATE,
        style="italic",
    )

    # Right: reciprocal map → NNT/NNH split
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Reciprocal of ARR CI is not a simple interval", fontsize=10, fontweight="bold", color=INDIGO)

    # Benefit limb
    ax.add_patch(
        FancyBboxPatch(
            (0.4, 6.6),
            9.2,
            2.5,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor="#E8F5E9",
            edgecolor=GREEN,
            lw=1.5,
        )
    )
    ax.text(5.0, 8.45, "Benefit limb (ARR > 0)", ha="center", fontsize=9, fontweight="bold", color=GREEN)
    ax.text(
        5.0,
        7.4,
        "ARR +5% → NNT = 20\nAs ARR → 0⁺ → NNT → +∞",
        ha="center",
        fontsize=8.5,
        color=SLATE,
    )

    # Infinity break
    ax.annotate(
        "",
        xy=(5.0, 5.5),
        xytext=(5.0, 6.4),
        arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=2),
    )
    ax.text(5.5, 5.9, "CI crosses 0 → interval\nfractures through ∞", fontsize=8, color=GOLD, fontweight="bold")

    # Harm limb
    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.5),
            9.2,
            2.5,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.5,
        )
    )
    ax.text(5.0, 2.35, "Harm limb (ARR < 0)", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.text(
        5.0,
        1.3,
        "ARR −1% → NNH = 100\nDo not report a single NNT point estimate",
        ha="center",
        fontsize=8.5,
        color=SLATE,
    )

    ax.text(
        5.0,
        4.6,
        "Prefer: “between 1 more and 5 fewer events per 100”",
        ha="center",
        fontsize=8.3,
        color=INDIGO,
        fontweight="bold",
    )

    fig.suptitle(
        "Inference hygiene: when ARR CI includes 0, NNT CI runs through infinity (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch19_nnt_ci_infinity.png")


def fig_ch16_autopsy_abs() -> Path:
    """CLEAR-PATH synthetic autopsy: absolute benefit, harm, net framing."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))

    # Left: primary outcome absolute risks
    ax = axes[0]
    arms = ["Control\n(best medical)", "EVT + medical"]
    indep = [33.1, 43.4]  # mRS 0-2 %
    x = np.arange(len(arms))
    bars = ax.bar(x, indep, color=[GRAY, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(arms, fontsize=9)
    ax.set_ylabel("90-day functional independence mRS 0–2 (%)")
    ax.set_ylim(0, 55)
    ax.set_title("CLEAR-PATH synthetic primary endpoint", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, indep):
        ax.text(b.get_x() + b.get_width() / 2, v + 1.2, f"{v:.1f}%", ha="center", fontsize=9, fontweight="bold")
    # ARR annotation
    ax.annotate(
        "",
        xy=(1, 43.4),
        xytext=(1, 33.1),
        arrowprops=dict(arrowstyle="<->", color=CORAL, lw=2),
    )
    ax.text(
        1.35,
        38.2,
        "ARR 10.3 pp\n(95% CI 1.9–18.7)\nNNT ≈ 10",
        fontsize=8.2,
        color=CORAL,
        fontweight="bold",
        va="center",
    )

    # Right: harm + decision bucket
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Autopsy absolute ledger → decision bucket", fontsize=10, fontweight="bold", color=INDIGO)

    blocks = [
        (7.6, TEAL, "Benefit", "Independence ARR 10.3 pp · NNT ≈ 10 at 90 d"),
        (5.5, CORAL, "Harm", "sICH ARI 2.7 pp (6.2% vs 3.5%) · NNH ≈ 37\nCI crosses null — not proof of safety"),
        (3.4, GOLD, "Quarantine", "Tandem-lesion subgroup p=0.04 without p_int"),
        (1.2, GREEN, "Bottom line", "Conditional Act if local ASPECTS selection holds\nPrediction models ≠ causal license for pathway"),
    ]
    for y, edge, title, body in blocks:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.7),
                9.4,
                1.85,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.4,
            )
        )
        ax.text(0.55, y + 0.55, title, fontsize=9, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.2, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Paper autopsy: reconstruct absolute effects before pathway rewrite (CLEAR-PATH synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch16_autopsy_abs.png")


def fig_ch10_fe_re_weights() -> Path:
    """Fixed-effect vs random-effects weights: small-trial inflation paradox."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))

    # Synthetic log-RR studies: mega-trial precise, small noisy
    studies = ["Mega-trial\nn=5000", "Mid\nn=800", "Small A\nn=120", "Small B\nn=80"]
    # SE on log-RR scale (teaching)
    se = np.array([0.04, 0.10, 0.28, 0.35])
    # tau from DL-like teaching value
    tau2 = 0.08
    w_fe = 1.0 / (se**2)
    w_re = 1.0 / (se**2 + tau2)
    # normalize to percent
    w_fe_p = 100 * w_fe / w_fe.sum()
    w_re_p = 100 * w_re / w_re.sum()

    ax = axes[0]
    x = np.arange(len(studies))
    w = 0.36
    ax.bar(x - w / 2, w_fe_p, width=w, color=INDIGO, edgecolor=INDIGO, label="Fixed-effect weight %")
    ax.bar(x + w / 2, w_re_p, width=w, color=CORAL, edgecolor=INDIGO, label="Random-effects weight %")
    ax.set_xticks(x)
    ax.set_xticklabels(studies, fontsize=8)
    ax.set_ylabel("Relative weight in the pooled estimate (%)")
    ax.set_ylim(0, 100)
    ax.set_title("Weights shift as τ² enters the denominator", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.8, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    for i, (a, b) in enumerate(zip(w_fe_p, w_re_p)):
        ax.text(i - w / 2, a + 1.5, f"{a:.0f}", ha="center", fontsize=7.2, color=INDIGO)
        ax.text(i + w / 2, b + 1.5, f"{b:.0f}", ha="center", fontsize=7.2, color=CORAL)

    # Right: teaching panel
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Random-effects paradox (appraisal)", fontsize=10, fontweight="bold", color=INDIGO)

    lines = [
        (8.0, TEAL, "Fixed-effect", "w_i = 1 / SE_i² — mega-trials dominate the pool"),
        (6.0, CORAL, "Random-effects", "w_i* = 1 / (SE_i² + τ²) — large τ² equalizes weights"),
        (4.0, GOLD, "Clinical risk", "Small, biased single-center trials gain influence"),
        (2.0, INDIGO, "Absolute still required", "Pooled RR must become ARR/NNT at local CER"),
        (0.35, PURPLE, "Prediction ≠ causation", "Meta-regression subgroups are observational patterns"),
    ]
    for y, edge, title, body in lines:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.55),
                9.4,
                1.65,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.55, y + 0.4, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.2, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Meta-analysis literacy: fixed-effect vs random-effects weighting (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch10_fe_re_weights.png")


def fig_ch12_net_benefit() -> Path:
    """Same RR=0.50; baseline risk flips net benefit after fixed procedural ARI."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))

    # CEA-style teaching numbers from ch12
    labels = ["Symptomatic\n70–99% stenosis", "Asymptomatic\n70–99% stenosis"]
    pc = np.array([0.26, 0.02])  # 2-year ipsilateral stroke medical
    rr = 0.50
    arr = pc * (1 - rr) * 100  # 13, 1
    ari = np.array([3.0, 3.0])  # perioperative %
    net = arr - ari  # +10, -2

    ax = axes[0]
    x = np.arange(len(labels))
    w = 0.28
    b1 = ax.bar(x - w, arr, width=w, color=TEAL, edgecolor=INDIGO, label="ARR (stroke prevented, pp)")
    b2 = ax.bar(x, ari, width=w, color=CORAL, edgecolor=INDIGO, label="ARI (peri-op stroke/death, pp)")
    b3 = ax.bar(x + w, net, width=w, color=GOLD, edgecolor=INDIGO, label="Net absolute benefit (pp)")
    ax.axhline(0, color=SLATE, lw=1.0)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Percentage points over 2-year horizon (synthetic)")
    ax.set_ylim(-5, 16)
    ax.set_title("Same RR = 0.50; baseline risk flips the decision", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    for bars in (b1, b2, b3):
        for rect in bars:
            h = rect.get_height()
            ax.text(
                rect.get_x() + rect.get_width() / 2,
                h + (0.4 if h >= 0 else -1.1),
                f"{h:.0f}",
                ha="center",
                fontsize=8,
                fontweight="bold",
                color=SLATE,
            )

    # Right: algebra + NNT
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("ARR = p_c × (1 − RR); then subtract harm", fontsize=10, fontweight="bold", color=INDIGO)

    boxes = [
        (7.5, INDIGO, "Portable relative", "RR = 0.50 (RRR 50%) looks identical in both labels"),
        (5.5, TEAL, "Absolute benefit", "Symptomatic: ARR = 26%×0.5 = 13 pp · NNT ≈ 8\nAsymptomatic: ARR = 2%×0.5 = 1 pp · NNT ≈ 100"),
        (3.5, CORAL, "Fixed harm", "Peri-op ARI ≈ 3 pp both groups · NNH ≈ 33"),
        (1.5, GOLD, "Net decision", "Symptomatic net +10 pp → operate\nAsymptomatic net −2 pp → medical therapy"),
        (0.15, PURPLE, "Rule", "Never invert observational associations into NNTs;\nprediction ≠ causation for surgical indication"),
    ]
    for y, edge, title, body in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.55),
                9.4,
                1.75,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.55, y + 0.5, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.15, body, fontsize=7.8, color=SLATE, va="center")

    fig.suptitle(
        "Effect sizes: absolute net benefit tracks baseline risk, not disease labels (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle4_swarm_ch12_net_benefit.png")


def main() -> None:
    print("Cycle-4 swarm densify figures →", OUT)
    writers = [
        fig_ch28_transport_arr,
        fig_ch22_length_overdiagnosis,
        fig_ch19_nnt_infinity,
        fig_ch16_autopsy_abs,
        fig_ch10_fe_re_weights,
        fig_ch12_net_benefit,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
