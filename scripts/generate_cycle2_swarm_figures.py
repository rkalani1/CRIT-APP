#!/usr/bin/env python3
"""
CRIT-APP Cycle-2 densify swarm: original matplotlib scientific teaching figures.

Targets thinner mid/late chapters (17, 21, 24, 25, 27). Code-drawn only (Agg).
Writes PNGs under docs/assets/figures/. Safe to re-run (overwrites cycle2_swarm_* only).
Does not redo cycle-1 thin figures or cycle2_midlate_* outputs.
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


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch17_or_rr_divergence() -> Path:
    """OR vs RR as outcome frequency rises (same RR=2.0); ch17 association grammar."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.8))

    # Unexposed risk p0; RR fixed at 2.0 → p1 = min(2*p0, 0.99)
    p0 = np.array([0.02, 0.05, 0.10, 0.20, 0.30, 0.40])
    rr = 2.0
    p1 = np.minimum(rr * p0, 0.99)
    # RD
    rd = p1 - p0
    # OR = (p1/(1-p1)) / (p0/(1-p0))
    or_ = (p1 / (1 - p1)) / (p0 / (1 - p0))

    ax = axes[0]
    ax.plot(p0 * 100, np.full_like(p0, rr), "o-", color=TEAL, lw=2.2, ms=8, label="Risk ratio (fixed)")
    ax.plot(p0 * 100, or_, "s-", color=CORAL, lw=2.2, ms=8, label="Odds ratio")
    ax.axhline(1.0, color=SLATE, ls=":", lw=1.0)
    ax.set_xlabel("Unexposed risk p₀ (%)")
    ax.set_ylabel("Association measure")
    ax.set_ylim(0.5, 5.5)
    ax.set_title("Same RR = 2.0; OR inflates as events get common", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, alpha=0.3)
    # annotate last point
    ax.annotate(
        f"OR ≈ {or_[-1]:.2f}\nwhen p₀=40%",
        xy=(p0[-1] * 100, or_[-1]),
        xytext=(22, 4.6),
        fontsize=8,
        color=CORAL,
        arrowprops=dict(arrowstyle="->", color=CORAL),
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Teaching table (synthetic 90-day cohort)", fontsize=10, fontweight="bold", color=INDIGO)
    # mini 2x2 style panel from ch17 numbers
    rows = [
        (8.4, "Exposed risk", "10% (40/400)"),
        (6.9, "Unexposed risk", "5% (30/600)"),
        (5.4, "Risk difference", "5 pp"),
        (3.9, "Risk ratio", "2.00"),
        (2.4, "Odds ratio", "≈2.11"),
        (0.9, "Bedside needs", "RD first; RR/OR for math"),
    ]
    for y, lab, val in rows:
        ax.add_patch(
            FancyBboxPatch(
                (0.4, y - 0.45),
                9.2,
                1.2,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=LIGHT if "Bedside" in lab else WHITE,
                edgecolor=INDIGO,
                lw=1.0,
            )
        )
        ax.text(0.7, y + 0.15, lab, fontsize=8.5, fontweight="bold", color=INDIGO, va="center")
        ax.text(9.3, y + 0.15, val, fontsize=8.5, color=SLATE, ha="right", va="center")
    fig.suptitle(
        "Association grammar: RD, RR, and when OR ≠ RR (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch17_or_rr_divergence.png")


def fig_ch21_additive_net() -> Path:
    """Multiplicative homogeneity + additive interaction + net benefit (ch21 DAPT example)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # From chapter worked example: RR=0.67 both strata; ARR 4% vs 1%; ARI bleed 0.8%
    strata = ["High-risk\n(ABCD2 high)", "Low-risk\n(ABCD2 low)"]
    arr = np.array([4.0, 1.0])  # ischemic ARR %
    ari = np.array([0.8, 0.8])  # major hemorrhage ARI %
    rr = np.array([0.67, 0.67])

    ax = axes[0]
    x = np.arange(len(strata))
    w = 0.28
    b1 = ax.bar(x - w, arr, width=w, color=GREEN, edgecolor=INDIGO, label="Ischemic ARR (pp)")
    b2 = ax.bar(x, ari, width=w, color=CORAL, edgecolor=INDIGO, label="Bleed ARI (pp)")
    b3 = ax.bar(x + w, arr - ari, width=w, color=TEAL, edgecolor=INDIGO, label="Net absolute (pp)")
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xticks(x)
    ax.set_xticklabels(strata)
    ax.set_ylabel("Absolute percentage points (21-day)")
    ax.set_ylim(-0.5, 5.5)
    ax.set_title("Same RR, different net absolute benefit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    for rect, v in zip(b1, arr):
        ax.text(rect.get_x() + rect.get_width() / 2, v + 0.12, f"{v:.1f}", ha="center", fontsize=8)
    for rect, v in zip(b2, ari):
        ax.text(rect.get_x() + rect.get_width() / 2, v + 0.12, f"{v:.1f}", ha="center", fontsize=8)
    for rect, v in zip(b3, arr - ari):
        ax.text(rect.get_x() + rect.get_width() / 2, v + 0.12, f"{v:.1f}", ha="center", fontsize=8, color=TEAL)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Scale dependence (synthetic DAPT strata)", fontsize=10, fontweight="bold", color=INDIGO)
    boxes = [
        (7.2, TEAL, "#E0F2F1", "Multiplicative", "RR = 0.67 in both strata\nInteraction p > 0.05\n→ 'consistent relative effect'"),
        (4.0, ORANGE, "#FFF3E0", "Additive", "ARR 4.0 pp vs 1.0 pp\nNNT 25 vs 100\n→ clear additive interaction"),
        (0.7, CORAL, "#FFEBEE", "Clinical net", "High-risk: +3.2 pp net\nLow-risk: +0.2 pp net\nUniform policy is not justified"),
    ]
    for y, edge, face, title, body in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y),
                9.3,
                2.5,
                boxstyle="round,pad=0.06,rounding_size=0.1",
                facecolor=face,
                edgecolor=edge,
                lw=1.5,
            )
        )
        ax.text(0.7, y + 1.85, title, fontsize=9.5, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y + 0.85, body, fontsize=8.2, color=SLATE, va="center")
    fig.suptitle(
        "Effect modification: multiplicative homogeneity ≠ additive net benefit",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch21_additive_net.png")


def fig_ch24_composite_disagg() -> Path:
    """Composite primary driven by soft components; disaggregate absolute rates (ch24)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # Synthetic secondary-prevention composite: stroke/MI/CV death/revasc
    components = ["Disabling\nstroke", "Non-disabling\nstroke", "MI", "Urgent\nrevasc", "CV death"]
    # events per 1000 over 1 year, control vs treatment
    ctrl = np.array([28, 22, 18, 45, 12])
    tx = np.array([26, 20, 16, 22, 11])  # mostly revasc drives composite
    delta = ctrl - tx  # events avoided per 1000

    ax = axes[0]
    y = np.arange(len(components))
    ax.barh(y + 0.18, ctrl, height=0.32, color="#90A4AE", edgecolor=INDIGO, label="Control /1000")
    ax.barh(y - 0.18, tx, height=0.32, color=TEAL, edgecolor=INDIGO, label="Treatment /1000")
    ax.set_yticks(y)
    ax.set_yticklabels(components, fontsize=8.5)
    ax.set_xlabel("Events per 1000 patients · 1 year (synthetic)")
    ax.set_title("Disaggregated absolute component rates", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(True, axis="x", alpha=0.3)
    ax.invert_yaxis()

    ax = axes[1]
    colors = [GREEN if c in ("Disabling\nstroke", "CV death") else GOLD if c == "MI" else CORAL if "revasc" in c else SLATE for c in components]
    bars = ax.bar(np.arange(len(components)), delta, color=colors, edgecolor=INDIGO, width=0.65)
    ax.axhline(0, color=SLATE, lw=0.8)
    ax.set_xticks(np.arange(len(components)))
    ax.set_xticklabels(components, fontsize=7.5)
    ax.set_ylabel("Events avoided per 1000 (control − tx)")
    ax.set_title("What drives the 'significant composite'?", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, delta):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.6, f"{v:.0f}", ha="center", fontsize=8, fontweight="bold")
    # callout
    ax.text(
        0.5,
        0.97,
        f"Composite ARR ≈ {delta.sum()/10:.1f} pp — mostly urgent revasc ({delta[3]}/1000)",
        transform=ax.transAxes,
        ha="center",
        va="top",
        fontsize=8,
        color=CORAL,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    fig.suptitle(
        "Composite endpoint trap: significance without patient-important drivers (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch24_composite_disagg.png")


def fig_ch25_ppv_prevalence() -> Path:
    """PPV/NPV vs prevalence at fixed sens/spec; LVO triage worked example (ch25)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # From chapter: sens=0.85, spec=0.80
    sens, spec = 0.85, 0.80
    prev = np.linspace(0.02, 0.50, 120)
    # PPV = sens*p / (sens*p + (1-spec)*(1-p))
    ppv = (sens * prev) / (sens * prev + (1 - spec) * (1 - prev))
    npv = (spec * (1 - prev)) / (spec * (1 - prev) + (1 - sens) * prev)

    ax = axes[0]
    ax.plot(prev * 100, ppv * 100, color=TEAL, lw=2.4, label="PPV")
    ax.plot(prev * 100, npv * 100, color=INDIGO, lw=2.4, label="NPV")
    # mark EMS 15% and comprehensive 30%
    for p_mark, lab in [(0.05, "EMS ~5%"), (0.15, "EMS alerts\n15%"), (0.30, "CSC ~30%")]:
        ppv_m = (sens * p_mark) / (sens * p_mark + (1 - spec) * (1 - p_mark))
        ax.plot(p_mark * 100, ppv_m * 100, "o", color=CORAL, ms=8, zorder=5)
        ax.annotate(
            f"{lab}\nPPV≈{ppv_m*100:.0f}%",
            xy=(p_mark * 100, ppv_m * 100),
            xytext=(p_mark * 100 + (8 if p_mark < 0.2 else -12), ppv_m * 100 + 12),
            fontsize=7.2,
            color=CORAL,
            arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.0),
        )
    ax.set_xlabel("Local LVO prevalence among tested (%)")
    ax.set_ylabel("Predictive value (%)")
    ax.set_xlim(0, 52)
    ax.set_ylim(40, 102)
    ax.set_title(f"Fixed sens {sens*100:.0f}% · spec {spec*100:.0f}% — PPV travels with prevalence",
                 fontsize=9.5, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="center right")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Portable currency: likelihood ratios (synthetic)", fontsize=10, fontweight="bold", color=INDIGO)
    lr_pos = sens / (1 - spec)
    lr_neg = (1 - sens) / spec
    # Bayes at 15%
    pre = 0.15
    odds_pre = pre / (1 - pre)
    post_pos = (odds_pre * lr_pos) / (1 + odds_pre * lr_pos)
    post_neg = (odds_pre * lr_neg) / (1 + odds_pre * lr_neg)
    lines = [
        (8.3, f"LR+ = sens/(1−spec) = {lr_pos:.2f}"),
        (6.7, f"LR− = (1−sens)/spec = {lr_neg:.2f}"),
        (5.1, f"Pre-test 15% → post+ ≈ {post_pos*100:.0f}%"),
        (3.5, f"Pre-test 15% → post− ≈ {post_neg*100:.1f}%"),
        (1.5, "Action: if divert threshold = 25%,\npositives divert; negatives stay primary."),
    ]
    for y, text in lines:
        face = "#E8F5E9" if "Action" in text else WHITE
        edge = GREEN if "Action" in text else INDIGO
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y - 0.55),
                9.3,
                1.45 if "Action" in text else 1.25,
                boxstyle="round,pad=0.05,rounding_size=0.08",
                facecolor=face,
                edgecolor=edge,
                lw=1.2,
            )
        )
        ax.text(5.0, y + 0.05, text, ha="center", va="center", fontsize=8.5, color=SLATE)
    fig.suptitle(
        "Do not transport PPV: rebuild post-test probability from LRs + local prevalence",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch25_ppv_prevalence.png")


def fig_ch27_multiplicity_fwer() -> Path:
    """Family-wise error inflation with unadjusted secondary tests (ch27)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # FWER = 1 - (1-α)^k under independence, α=0.05
    k = np.arange(1, 21)
    alpha = 0.05
    fwer = 1.0 - (1.0 - alpha) ** k
    bonf = np.full_like(k, alpha, dtype=float)  # controlled at 0.05 with Bonferroni threshold α/k

    ax = axes[0]
    ax.plot(k, fwer * 100, "o-", color=CORAL, lw=2.3, ms=6, label="Unadjusted FWER\n(α=0.05 each test)")
    ax.axhline(5, color=TEAL, ls="--", lw=1.6, label="Nominal 5% family target")
    ax.axhline(40, color=GOLD, ls=":", lw=1.2, alpha=0.8)
    ax.text(14, 42, "≥40% chance of ≥1 false positive\nby k≈10 independent tests", fontsize=7.5, color=GOLD)
    ax.set_xlabel("Number of unadjusted secondary tests (k)")
    ax.set_ylabel("Family-wise type I error (%)")
    ax.set_xlim(1, 20)
    ax.set_ylim(0, 70)
    ax.set_title("Garden of forking paths: error compounds", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, alpha=0.3)
    # mark k=1 and k=20
    ax.annotate(f"k=1 → {fwer[0]*100:.0f}%", xy=(1, fwer[0] * 100), xytext=(3, 12),
                fontsize=8, color=SLATE, arrowprops=dict(arrowstyle="->", color=SLATE))
    ax.annotate(f"k=20 → {fwer[-1]*100:.0f}%", xy=(20, fwer[-1] * 100), xytext=(12, 62),
                fontsize=8, color=CORAL, arrowprops=dict(arrowstyle="->", color=CORAL))

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Appraisal defenses (stroke trial plumbing)", fontsize=10, fontweight="bold", color=INDIGO)
    items = [
        (7.6, GREEN, "Pre-specify & lock SAP", "Primary endpoint named before unblinding."),
        (5.4, TEAL, "Hierarchical testing", "Secondaries only if primary succeeds."),
        (3.2, INDIGO, "Alpha spending", "Bonferroni / Hochberg / gatekeeping."),
        (1.0, CORAL, "Reject abstract spin", "Null primary + shiny secondary = hypothesis-generating only."),
    ]
    for y, edge, title, body in items:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y),
                9.3,
                1.9,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.5,
            )
        )
        ax.text(0.7, y + 1.25, title, fontsize=9, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y + 0.5, body, fontsize=8.2, color=SLATE, va="center")
    fig.suptitle(
        "Multiplicity: unadjusted secondary sweeps inflate false positives (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch27_multiplicity_fwer.png")


def fig_ch27_early_stop_bias() -> Path:
    """Early stopping for benefit: exaggerated interim estimate then regression (ch27)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.4, 4.9))

    # Synthetic: true ARR = 6 pp; interim stop at random high 14 pp; later trials regress
    stages = ["Interim stop\n(early)", "Full trial\n(if continued)", "Replication\ntrial 1", "Replication\ntrial 2", "Meta-\nestimate"]
    arr_pp = np.array([14.0, 7.5, 5.5, 6.5, 6.2])
    colors = [CORAL, GOLD, TEAL, TEAL, INDIGO]

    ax = axes[0]
    x = np.arange(len(stages))
    bars = ax.bar(x, arr_pp, color=colors, edgecolor=INDIGO, width=0.62)
    ax.axhline(6.0, color=SLATE, ls="--", lw=1.5, label="True ARR = 6 pp (synthetic truth)")
    ax.set_xticks(x)
    ax.set_xticklabels(stages, fontsize=8)
    ax.set_ylabel("Absolute risk reduction (pp)")
    ax.set_ylim(0, 18)
    ax.set_title("Early stop catches a random high", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, arr_pp):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v:.1f}", ha="center", fontsize=8, fontweight="bold")

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("How to read early-stopped stroke trials", fontsize=10, fontweight="bold", color=INDIGO)
    bullets = [
        (7.8, "Bias direction", "Stopping for benefit on a boundary often inflates the point estimate."),
        (5.5, "Boundary matters", "O'Brien–Fleming (strict early) is less liberal than Pocock."),
        (3.2, "Appraisal move", "Down-weight magnitude; demand absolute risks + CIs, not victory rhetoric."),
        (0.9, "Futility stop", "≠ equivalence. Only says pre-specified difference is unlikely."),
    ]
    for y, title, body in bullets:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y),
                9.3,
                1.95,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=LIGHT if title.startswith("A") else WHITE,
                edgecolor=INDIGO,
                lw=1.1,
            )
        )
        ax.text(0.7, y + 1.3, title, fontsize=9, fontweight="bold", color=INDIGO, va="center")
        ax.text(0.7, y + 0.55, body, fontsize=8.2, color=SLATE, va="center")
    fig.suptitle(
        "Interim early stopping for benefit and regression to the truth (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_swarm_ch27_early_stop_bias.png")


def main() -> None:
    print("Cycle-2 swarm densify figures →", OUT)
    writers = [
        fig_ch17_or_rr_divergence,
        fig_ch21_additive_net,
        fig_ch24_composite_disagg,
        fig_ch25_ppv_prevalence,
        fig_ch27_multiplicity_fwer,
        fig_ch27_early_stop_bias,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
