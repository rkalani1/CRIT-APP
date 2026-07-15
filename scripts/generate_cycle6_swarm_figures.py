#!/usr/bin/env python3
"""
CRIT-APP Cycle-6 densify swarm: original matplotlib scientific teaching figures.

Targets residual floor chapters after cycles 1–5 (~7 imgs each):
  ch06 noninferiority margin on absolute scale; ITT dilutes ARR
  ch08 natural frequencies Se/Sp → post-test at local prevalence
  ch04 information-bias absolute misclassification matrix
  ch21 standardization reweights stratum-specific ARRs
  ch23 cognitive de-anchor: hide RRR until ARR/NNT computed
  ch24 therapy/harm net absolute tradeoff under competing ARI
  ch25 diagnosis + prognosis dual three-gate scaffold

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle6_swarm_* only). Does not redo cycle1–5 figures.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch
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


def fig_ch06_ni_itt_arr() -> Path:
    """Noninferiority margin on absolute scale; ITT dilutes ARR vs PP."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: NI margin on absolute risk difference scale
    ax = axes[0]
    ax.set_xlim(-8, 6)
    ax.set_ylim(0, 6)
    ax.axvline(0, color=SLATE, lw=1.4, zorder=1)
    ax.axvspan(-8, -3.0, color="#FFEBEE", alpha=0.55, zorder=0)
    ax.axvspan(-3.0, 6, color="#E8F5E9", alpha=0.45, zorder=0)
    ax.axvline(-3.0, color=CORAL, lw=2.2, ls="--", zorder=2)
    ax.text(-3.0, 5.55, "δ = −3 pp\n(pre-specified NI margin)", ha="center", fontsize=8,
            color=CORAL, fontweight="bold")
    ax.text(0.15, 5.55, "favor new", fontsize=8, color=TEAL, fontweight="bold", ha="left")
    ax.text(-0.15, 5.55, "favor active control", fontsize=8, color=CORAL, fontweight="bold", ha="right")

    # Point estimate + 95% CI for RD (new − control) synthetic: RD −1.2, CI −2.6 to +0.2
    rd, lo, hi = -1.2, -2.6, 0.2
    ax.plot([lo, hi], [3.2, 3.2], color=INDIGO, lw=4, solid_capstyle="round", zorder=3)
    ax.plot(rd, 3.2, "o", color=GOLD, ms=12, zorder=4, markeredgecolor=INDIGO, markeredgewidth=1.5)
    ax.plot([lo, lo], [2.95, 3.45], color=INDIGO, lw=2.5)
    ax.plot([hi, hi], [2.95, 3.45], color=INDIGO, lw=2.5)
    ax.text(rd, 3.85, f"RD {rd:.1f} pp (95% CI {lo:.1f} to {hi:+.1f})", ha="center",
            fontsize=8.5, fontweight="bold", color=INDIGO)
    ax.text(-1.5, 2.35, "Upper CI bound < δ → noninferior on ABSOLUTE scale",
            ha="center", fontsize=8.2, color=GREEN, fontweight="bold")
    ax.text(-1.5, 1.55, "Never claim NI from a relative CI alone;\ntranslate δ into events / 100 treated.",
            ha="center", fontsize=8, color=SLATE)
    ax.set_xlabel("Risk difference (new − active control), percentage points", fontsize=9)
    ax.set_yticks([])
    ax.set_title("Noninferiority is an absolute claim", fontsize=10, fontweight="bold", color=INDIGO)
    for spine in ("top", "right", "left"):
        ax.spines[spine].set_visible(False)

    # Right: ITT dilutes ARR vs per-protocol
    ax = axes[1]
    cats = ["True on-treatment\nbiological ARR", "Per-protocol\n(compliers)", "ITT strategy\n(diluted)"]
    arr = np.array([8.0, 7.5, 4.0])  # crossover/nonadherence dilutes
    colors = [TEAL, BLUE, GOLD]
    x = np.arange(len(cats))
    bars = ax.bar(x, arr, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=8.5)
    ax.set_ylabel("Absolute risk reduction (pp, synthetic 90-day mRS 0–2)")
    ax.set_ylim(0, 11)
    ax.set_title("ITT preserves randomization; PP inflates purity", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    nnts = [100 / a for a in arr]
    for b, a, n in zip(bars, arr, nnts):
        ax.text(b.get_x() + b.get_width() / 2, a + 0.35, f"ARR {a:.1f} pp\nNNT ≈ {n:.0f}",
                ha="center", fontsize=8, fontweight="bold", color=SLATE)
    ax.annotate(
        "20% crossover → ITT ARR shrinks\n(pragmatic strategy effect)",
        xy=(2, 4.0),
        xytext=(0.55, 9.2),
        fontsize=7.8,
        color=ORANGE,
        fontweight="bold",
        arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.3),
    )
    ax.text(1.0, 0.45, "Report both estimands; do not shop for the prettier NNT.",
            ha="center", fontsize=7.8, color=PURPLE, style="italic")

    fig.suptitle(
        "RCT appraisal: absolute NI margin + ITT/PP ARR honesty (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch06_ni_itt_arr.png")


def fig_ch08_natural_freq_post() -> Path:
    """Natural frequencies Se/Sp → post-test probability at local prevalence."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: natural frequency tree at prevalence 10%, Se 90%, Sp 85%
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Natural frequencies (n=1000; Se 90%, Sp 85%)", fontsize=10, fontweight="bold", color=INDIGO)

    # Root
    ax.add_patch(FancyBboxPatch((3.0, 8.3), 4.0, 1.2, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor=WHITE, edgecolor=INDIGO, lw=1.5))
    ax.text(5.0, 8.9, "1000 patients\nprevalence 10%", ha="center", va="center", fontsize=8.5,
            fontweight="bold", color=INDIGO)

    # Disease / no disease
    ax.add_patch(FancyBboxPatch((0.4, 5.8), 3.6, 1.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.4))
    ax.text(2.2, 6.5, "Disease\nn = 100", ha="center", va="center", fontsize=9,
            fontweight="bold", color=CORAL)
    ax.add_patch(FancyBboxPatch((6.0, 5.8), 3.6, 1.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.4))
    ax.text(7.8, 6.5, "No disease\nn = 900", ha="center", va="center", fontsize=9,
            fontweight="bold", color=TEAL)
    ax.annotate("", xy=(2.2, 7.25), xytext=(4.2, 8.3), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))
    ax.annotate("", xy=(7.8, 7.25), xytext=(5.8, 8.3), arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.2))

    # Test results
    leaves = [
        (0.3, 2.6, 2.0, CORAL, "TP 90", "Se×100"),
        (2.5, 2.6, 2.0, ORANGE, "FN 10", "miss"),
        (5.5, 2.6, 2.0, GOLD, "FP 135", "(1−Sp)×900"),
        (7.7, 2.6, 2.0, TEAL, "TN 765", "true neg"),
    ]
    for x, y, w, edge, title, sub in leaves:
        ax.add_patch(FancyBboxPatch((x, y), w, 1.8, boxstyle="round,pad=0.03,rounding_size=0.07",
                                    facecolor=WHITE, edgecolor=edge, lw=1.4))
        ax.text(x + w / 2, y + 1.15, title, ha="center", fontsize=9, fontweight="bold", color=edge)
        ax.text(x + w / 2, y + 0.45, sub, ha="center", fontsize=7.5, color=SLATE)

    ax.annotate("", xy=(1.3, 4.45), xytext=(1.8, 5.8), arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=1.1))
    ax.annotate("", xy=(3.5, 4.45), xytext=(2.6, 5.8), arrowprops=dict(arrowstyle="-|>", color=ORANGE, lw=1.1))
    ax.annotate("", xy=(6.5, 4.45), xytext=(7.0, 5.8), arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.1))
    ax.annotate("", xy=(8.7, 4.45), xytext=(8.6, 5.8), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=1.1))

    # PPV / NPV strip
    ax.add_patch(FancyBboxPatch((0.4, 0.35), 9.2, 1.6, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFF8E1", edgecolor=GOLD, lw=1.3))
    ax.text(5.0, 1.35, "PPV = 90 / (90+135) ≈ 40%   ·   NPV = 765 / (765+10) ≈ 99%",
            ha="center", va="center", fontsize=8.8, fontweight="bold", color=SLATE)
    ax.text(5.0, 0.7, "Same Se/Sp → different PPV if local prevalence ≠ 10%",
            ha="center", va="center", fontsize=7.8, color=CORAL)

    # Right: post-test vs prevalence curves
    ax = axes[1]
    se, sp = 0.90, 0.85
    lr_pos = se / (1 - sp)
    lr_neg = (1 - se) / sp
    prev = np.linspace(0.02, 0.50, 120)
    odds = prev / (1 - prev)
    post_pos = (odds * lr_pos) / (1 + odds * lr_pos)
    post_neg = (odds * lr_neg) / (1 + odds * lr_neg)
    ax.plot(prev * 100, post_pos * 100, color=CORAL, lw=2.4, label=f"Post-test if +  (LR+≈{lr_pos:.1f})")
    ax.plot(prev * 100, post_neg * 100, color=TEAL, lw=2.4, label=f"Post-test if −  (LR−≈{lr_neg:.2f})")
    ax.plot(prev * 100, prev * 100, "--", color=GRAY, lw=1.2, label="No information (post=pre)")
    # markers
    for p, lab in [(0.05, "TIA clinic\n5%"), (0.10, "ED rule-out\n10%"), (0.30, "Code stroke\n30%")]:
        o = p / (1 - p)
        pp = (o * lr_pos) / (1 + o * lr_pos)
        ax.scatter([p * 100], [pp * 100], s=55, color=GOLD, zorder=5, edgecolor=INDIGO)
        ax.annotate(lab, xy=(p * 100, pp * 100), xytext=(p * 100 + 4, pp * 100 - 12),
                    fontsize=7.2, color=SLATE, arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.0))
    ax.axhline(50, color=PURPLE, ls=":", lw=1.1, alpha=0.8)
    ax.text(48, 52, "treat threshold example 50%", fontsize=7.2, color=PURPLE, ha="right")
    ax.set_xlabel("Local pre-test probability (%)")
    ax.set_ylabel("Post-test probability (%)")
    ax.set_xlim(0, 52)
    ax.set_ylim(0, 100)
    ax.set_title("Transport LRs, not published PPV/NPV", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="center right")
    ax.grid(True, alpha=0.3)

    fig.suptitle(
        "Diagnostic accuracy: natural frequencies → local post-test absolute risk (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch08_natural_freq_post.png")


def fig_ch04_info_bias_matrix() -> Path:
    """Information bias: absolute misclassification matrix and biased ARR."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: 2x2 true vs observed with differential outcome misclassification
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Differential outcome misclassification (synthetic)", fontsize=10, fontweight="bold", color=INDIGO)

    # True rates
    ax.text(5.0, 9.3, "Truth: control 20% events · treated 12% events · true ARR 8 pp",
            ha="center", fontsize=8.5, fontweight="bold", color=SLATE)

    # Matrix headers
    headers = [("True event", 2.2), ("True nonevent", 6.5)]
    for lab, x in headers:
        ax.text(x, 8.3, lab, ha="center", fontsize=8, fontweight="bold", color=INDIGO)
    ax.text(0.3, 6.8, "Treated\narm", ha="left", fontsize=8, fontweight="bold", color=TEAL, va="center")
    ax.text(0.3, 4.5, "Control\narm", ha="left", fontsize=8, fontweight="bold", color=CORAL, va="center")

    # Cells: treated — some events reclassified as nonevents (optimistic adjudication)
    cells = [
        (1.3, 6.0, 2.6, 1.6, TEAL, "Se_T 70%\nmiss 30% of events"),
        (4.8, 6.0, 3.6, 1.6, TEAL, "Sp_T 98%\nfew false events"),
        (1.3, 3.7, 2.6, 1.6, CORAL, "Se_C 95%\nalmost all events seen"),
        (4.8, 3.7, 3.6, 1.6, CORAL, "Sp_C 90%\nmore false events"),
    ]
    for x, y, w, h, edge, body in cells:
        ax.add_patch(FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.03,rounding_size=0.07",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(x + w / 2, y + h / 2, body, ha="center", va="center", fontsize=8, color=SLATE)

    ax.add_patch(FancyBboxPatch((0.5, 0.4), 9.0, 2.4, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.3))
    ax.text(5.0, 1.9, "Observed event rates (approx): treated 8.6% · control 26%\n"
            "Observed ARR ≈ 17 pp  (true ARR was 8 pp)",
            ha="center", va="center", fontsize=8.5, fontweight="bold", color=CORAL)
    ax.text(5.0, 0.85, "Blinded adjudication + equal surveillance equalize Se/Sp across arms.",
            ha="center", va="center", fontsize=7.8, color=SLATE)

    # Right: bar true vs observed ARR + NNT
    ax = axes[1]
    labels = ["True ARR", "Biased\nobserved ARR"]
    vals = [8.0, 17.4]
    colors = [TEAL, CORAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, vals, color=colors, edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Absolute risk reduction (pp)")
    ax.set_ylim(0, 22)
    ax.set_title("Information bias invents absolute benefit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, vals):
        nnt = 100 / v
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.1f} pp\nNNT ≈ {nnt:.0f}",
                ha="center", fontsize=9, fontweight="bold", color=SLATE)
    ax.annotate(
        "NNT halved by misclassification\n→ pathway rewrite on noise",
        xy=(1, 17.4),
        xytext=(0.05, 19.5),
        fontsize=8,
        color=CORAL,
        fontweight="bold",
        arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=1.2),
    )
    ax.text(0.5, 1.2, "Taxonomy fix: name the information-bias mechanism\nbefore trusting any ARR/NNT.",
            ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle(
        "Bias taxonomy: information bias moves absolute effects, not just p-values (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch04_info_bias_matrix.png")


def fig_ch21_standardize_arr() -> Path:
    """Standardization reweights stratum-specific ARRs to a target mix."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: stratum-specific absolute risks
    ax = axes[0]
    strata = ["Age <70\n(mild mix)", "Age ≥70\n(severe mix)"]
    # control vs treated event %
    ctrl = np.array([12.0, 40.0])
    trt = np.array([8.0, 32.0])  # ARR 4 pp both strata (homogeneous additive)
    x = np.arange(len(strata))
    w = 0.35
    ax.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    ax.set_xticks(x)
    ax.set_xticklabels(strata, fontsize=9)
    ax.set_ylabel("90-day death/dependence (%)")
    ax.set_ylim(0, 52)
    ax.set_title("Stratum ARRs equal (4 pp) — additive EM absent", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, axis="y", alpha=0.3)
    for i, (c, t) in enumerate(zip(ctrl, trt)):
        ax.text(i, max(c, t) + 2, f"ARR {c - t:.0f} pp", ha="center", fontsize=8.5,
                fontweight="bold", color=GREEN)

    # Right: crude vs standardized to two target mixes
    ax = axes[1]
    # Trial mix: 70% young, 30% old → crude ARR = 0.7*4 + 0.3*4 = 4
    # But if rates shown as weighted event rates differ when RR homogeneous...
    # Teach standardization of ARR to target: w1*ARR1 + w2*ARR2
    # And crude comparison when baseline mix differs between sites
    # Site A: 80% young; Site B: 20% young
    # Crude control rates differ → relative spin differs even if ARR fixed
    labels = ["Trial crude\nARR", "Standardized\nto young site\n(80% <70)", "Standardized\nto older site\n(20% <70)"]
    # Homogeneous ARR 4 → standardized ARR always 4; contrast with crude RD when wrong pooling
    # Better teaching: multiplicative RR same → ARR differs by stratum
    # Redo conceptually: RR=0.75 both; young CER 12 → EER 9 ARR 3; old CER 40 → EER 30 ARR 10
    arr_std = np.array([
        0.70 * 3 + 0.30 * 10,  # trial mix 70/30
        0.80 * 3 + 0.20 * 10,  # young site
        0.20 * 3 + 0.80 * 10,  # older site
    ])
    colors = [INDIGO, GOLD, CORAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, arr_std, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Population ARR (pp) under RR=0.75 both strata")
    ax.set_ylim(0, 12)
    ax.set_title("Standardization: reweight stratum ARRs to target mix", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, a in zip(bars, arr_std):
        ax.text(b.get_x() + b.get_width() / 2, a + 0.3, f"ARR {a:.1f} pp\nNNT ≈ {100/a:.0f}",
                ha="center", fontsize=8, fontweight="bold", color=SLATE)
    ax.text(1.0, 0.5, "Effect modification on additive scale appears when RR is constant.\n"
            "Standardize to YOUR age/severity mix before pathway NNT.",
            ha="center", fontsize=7.8, color=PURPLE, style="italic")

    # Note: left panel used homogeneous ARR for contrast; add caption fix via suptitle detail
    # Update left to match RR-constant story for internal consistency
    # Actually inconsistency: left says ARR 4 both, right uses 3 and 10. Fix left panel.
    # I'll re-draw left values by clearing - better rewrite left before save.
    # Since we're mid-function, re-plot left with correct stratum ARRs.

    ax0 = axes[0]
    ax0.clear()
    strata = ["Age <70\nCER 12%", "Age ≥70\nCER 40%"]
    ctrl = np.array([12.0, 40.0])
    trt = np.array([9.0, 30.0])  # RR 0.75 both → ARR 3 vs 10
    x = np.arange(len(strata))
    w = 0.35
    ax0.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax0.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    ax0.set_xticks(x)
    ax0.set_xticklabels(strata, fontsize=9)
    ax0.set_ylabel("90-day death/dependence (%)")
    ax0.set_ylim(0, 52)
    ax0.set_title("Constant RR=0.75 → different stratum ARRs", fontsize=10, fontweight="bold", color=INDIGO)
    ax0.legend(fontsize=8, loc="upper left")
    ax0.grid(True, axis="y", alpha=0.3)
    for i, (c, t) in enumerate(zip(ctrl, trt)):
        ax0.text(i, max(c, t) + 2, f"ARR {c - t:.0f} pp", ha="center", fontsize=8.5,
                 fontweight="bold", color=GREEN)
    ax0.text(0.5, 48, "Additive effect modification present", ha="center", fontsize=8,
             color=ORANGE, fontweight="bold")

    fig.suptitle(
        "Interaction & standardization: transport ARR by reweighting strata (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch21_standardize_arr.png")


def fig_ch23_deanchor_rrr() -> Path:
    """Cognitive de-anchor: hide RRR until ARR/NNT computed."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: biased path vs debiased path
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("System-1 RRR anchor vs forced absolute card", fontsize=10, fontweight="bold", color=INDIGO)

    # Bad path
    ax.add_patch(FancyBboxPatch((0.3, 7.2), 4.3, 2.2, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(2.45, 8.7, "Biased path (anchor)", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.text(2.45, 7.85, "Headline RRR 40%\n→ ‘practice changing’\n→ skip absolute math",
            ha="center", fontsize=8, color=SLATE)

    # Good path
    ax.add_patch(FancyBboxPatch((5.4, 7.2), 4.3, 2.2, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(7.55, 8.7, "Debiased path", ha="center", fontsize=9, fontweight="bold", color=TEAL)
    ax.text(7.55, 7.85, "Cover relative claim\n→ CER/EER first\n→ ARR → NNT → then RRR",
            ha="center", fontsize=8, color=SLATE)

    steps = [
        (5.5, INDIGO, "1", "Read 2×2 / rates only (hide abstract RRR)"),
        (3.9, GOLD, "2", "Compute ARR & NNT (and ARI/NNH) with horizon"),
        (2.3, TEAL, "3", "Uncover RRR; check consistency with ARR/CER"),
        (0.7, PURPLE, "4", "Action sentence: adopt / adapt / wait / reject"),
    ]
    for y, edge, num, body in steps:
        ax.add_patch(FancyBboxPatch((0.5, y - 0.45), 9.0, 1.35, boxstyle="round,pad=0.03,rounding_size=0.07",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.add_patch(plt.Circle((1.15, y + 0.2), 0.32, color=edge))
        ax.text(1.15, y + 0.2, num, ha="center", va="center", fontsize=9, fontweight="bold", color=WHITE)
        ax.text(1.7, y + 0.2, body, ha="left", va="center", fontsize=8.5, color=SLATE)

    # Right: same RRR, two ARR cards as cognitive contrast
    ax = axes[1]
    labels = ["After RRR\nanchor only", "After forced\nARR card"]
    # Willingness to adopt pathway (synthetic survey teaching) — high when anchored
    adopt = np.array([78, 32])
    colors = [CORAL, TEAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, adopt, color=colors, edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("% saying ‘adopt pathway now’ (synthetic teaching)")
    ax.set_ylim(0, 100)
    ax.set_title("Debiasing changes decisions, not just feelings", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, adopt):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v}%", ha="center", fontsize=10,
                fontweight="bold", color=SLATE)
    ax.text(
        0.5,
        0.08,
        "Synthetic vignette: CER 5% · RRR 40% → ARR 2 pp · NNT 50\n"
        "Relative spin alone over-recruits ‘adopters’.",
        transform=ax.transAxes,
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
        bbox=dict(boxstyle="round,pad=0.4", facecolor="#FFF8E1", edgecolor=GOLD, lw=1.2),
    )

    fig.suptitle(
        "Dual-process appraisal: de-anchor from RRR until ARR/NNT is on the board (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch23_deanchor_rrr.png")


def fig_ch24_net_ari_tradeoff() -> Path:
    """Therapy/harm: net absolute tradeoff under competing ARI."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: benefit ARR vs harm ARI across baseline ischemic risk
    ax = axes[0]
    cer = np.linspace(0.02, 0.25, 80)
    rrr = 0.30
    arr = cer * rrr * 100  # pp
    ari_sICH = np.full_like(arr, 1.5)  # fixed absolute harm 1.5 pp
    net = arr - ari_sICH
    ax.plot(cer * 100, arr, color=TEAL, lw=2.4, label="ARR ischemic events (RRR 30%)")
    ax.plot(cer * 100, ari_sICH, color=CORAL, lw=2.2, ls="--", label="ARI sICH (fixed 1.5 pp)")
    ax.plot(cer * 100, net, color=INDIGO, lw=2.6, label="Net absolute (ARR − ARI)")
    ax.axhline(0, color=GRAY, lw=1.2)
    ax.fill_between(cer * 100, net, 0, where=(net >= 0), color=TEAL, alpha=0.12)
    ax.fill_between(cer * 100, net, 0, where=(net < 0), color=CORAL, alpha=0.12)
    # break-even
    be = 1.5 / (rrr * 100) * 100  # CER% where ARR=1.5
    ax.axvline(be, color=GOLD, ls=":", lw=1.4)
    ax.text(be + 0.4, 6.5, f"break-even\nCER≈{be:.1f}%", fontsize=8, color=GOLD, fontweight="bold")
    ax.set_xlabel("Baseline ischemic event risk CER (%)")
    ax.set_ylabel("Absolute percentage points")
    ax.set_xlim(2, 25)
    ax.set_ylim(-2, 9)
    ax.set_title("Competing ARI can invert net benefit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, alpha=0.3)

    # Right: ledger cards high vs low risk
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Side-by-side absolute ledger (same RRR)", fontsize=10, fontweight="bold", color=INDIGO)

    cards = [
        (5.5, TEAL, "High-risk TIA · CER 15%",
         "ARR 4.5 pp · NNT ≈ 22\nARI 1.5 pp · NNH ≈ 67\nNet +3.0 pp · ~33 treat for 1 net win"),
        (1.8, CORAL, "Low-risk clinic · CER 3%",
         "ARR 0.9 pp · NNT ≈ 111\nARI 1.5 pp · NNH ≈ 67\nNet −0.6 pp · harm dominates"),
    ]
    for y, edge, title, body in cards:
        ax.add_patch(FancyBboxPatch((0.4, y), 9.2, 3.0, boxstyle="round,pad=0.05,rounding_size=0.1",
                                    facecolor=WHITE, edgecolor=edge, lw=1.8))
        ax.text(5.0, y + 2.35, title, ha="center", fontsize=9.5, fontweight="bold", color=edge)
        ax.text(5.0, y + 1.1, body, ha="center", fontsize=8.5, color=SLATE)

    ax.text(5.0, 0.55, "Force benefit and harm onto one absolute time window before pathway rewrite.",
            ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle(
        "Therapy & harm: net absolute tradeoff under competing ARI (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle6_swarm_ch24_net_ari_tradeoff.png")


def fig_ch25_dual_gate_scaffold() -> Path:
    """Diagnosis + prognosis dual three-gate appraisal scaffold."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.25))

    for ax, title, edge, gates in [
        (
            axes[0],
            "Diagnosis · three gates",
            BLUE,
            [
                ("1 Trustworthiness", "Spectrum · verification\nincorporation · blinding"),
                ("2 Effect extraction", "Se/Sp → LR+ / LR−\nNOT raw PPV alone"),
                ("3 Local actionability", "Pre-test × LR → post-test\nCross action threshold?"),
            ],
        ),
        (
            axes[1],
            "Prognosis · three gates",
            PURPLE,
            [
                ("1 Trustworthiness", "Inception t0 · follow-up\nobjective outcomes"),
                ("2 Effect extraction", "Absolute risks @ horizon\ncalibration + discrimination"),
                ("3 Local actionability", "Strata change therapy?\nCounseling vs pathway tool"),
            ],
        ),
    ]:
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 10)
        ax.axis("off")
        ax.set_title(title, fontsize=10, fontweight="bold", color=edge)
        ys = [7.2, 4.35, 1.5]
        colors = [edge, GOLD, TEAL]
        for (g_title, body), y, c in zip(gates, ys, colors):
            ax.add_patch(FancyBboxPatch((0.5, y - 0.85), 9.0, 2.3,
                                        boxstyle="round,pad=0.05,rounding_size=0.1",
                                        facecolor=WHITE, edgecolor=c, lw=1.7))
            ax.text(1.0, y + 0.75, g_title, fontsize=9.5, fontweight="bold", color=c, va="center")
            ax.text(1.0, y - 0.15, body, fontsize=8.5, color=SLATE, va="center")
            if y > 2:
                ax.annotate("", xy=(5.0, y - 1.0), xytext=(5.0, y - 1.25),
                            arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4))

    fig.suptitle(
        "Diagnosis & prognosis papers: dual three-gate scaffold (synthetic teaching)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.text(
        0.5,
        0.01,
        "Shared rule: prediction ≠ causation · transport absolute quantities (LR, horizon risk), not press-release relatives.",
        ha="center",
        fontsize=8.2,
        color=SLATE,
        style="italic",
    )
    fig.tight_layout(rect=(0, 0.04, 1, 1))
    return _save(fig, "cycle6_swarm_ch25_dual_gate_scaffold.png")


def main() -> None:
    print("Cycle-6 swarm densify figures →", OUT)
    writers = [
        fig_ch06_ni_itt_arr,
        fig_ch08_natural_freq_post,
        fig_ch04_info_bias_matrix,
        fig_ch21_standardize_arr,
        fig_ch23_deanchor_rrr,
        fig_ch24_net_ari_tradeoff,
        fig_ch25_dual_gate_scaffold,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
