#!/usr/bin/env python3
"""
CRIT-APP Cycle-10 densify swarm: original matplotlib scientific teaching figures.

Residual floor-8 chapters after cycles 1–9:
  ch04 selection bias absolute sample distortion
  ch08 spectrum bias absolute Se/Sp shift
  ch12 net clinical benefit absolute ledger
  ch16 AI autopsy absolute recon
  ch21 additive vs multiplicative interaction absolute
  ch23 base-rate neglect absolute
  ch28 systems memo absolute action strip

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle10_swarm_* only).
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


def fig_ch04_selection() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    labels = ["Source\npopulation", "Eligible\nwith consent", "Analyzed\ncomplete cases"]
    n = np.array([1000, 420, 280])
    arr_claim = np.array([np.nan, 5.0, 9.0])
    x = np.arange(len(labels))
    ax.bar(x, n, color=[SLATE, BLUE, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Patients (synthetic)")
    ax.set_title("Selection funnel shrinks & selects healthier survivors", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(n):
        ax.text(i, v + 25, str(v), ha="center", fontsize=10, fontweight="bold", color=SLATE)

    ax = axes[1]
    labs = ["True target\nARR", "After selection\n(claimed)"]
    vals = [4.0, 9.0]
    ax.bar([0, 1], vals, color=[TEAL, CORAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("ARR (pp)")
    ax.set_title("Selection bias invents absolute benefit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(vals):
        ax.text(i, v + 0.3, f"{v:g} pp\nNNT {100/v:.0f}", ha="center", fontsize=9, fontweight="bold", color=SLATE)

    fig.suptitle("Bias taxonomy: selection distorts absolute effects (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch04_selection_funnel.png")


def fig_ch08_spectrum() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    cats = ["Healthy vs\nsevere stroke", "Consecutive\nsuspected", "Mild gray-zone\nonly"]
    se = np.array([0.98, 0.86, 0.62])
    sp = np.array([0.95, 0.82, 0.70])
    x = np.arange(len(cats))
    w = 0.35
    ax.bar(x - w / 2, se * 100, width=w, color=TEAL, edgecolor=INDIGO, label="Sensitivity %")
    ax.bar(x + w / 2, sp * 100, width=w, color=GOLD, edgecolor=INDIGO, label="Specificity %")
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=8.5)
    ax.set_ylabel("%")
    ax.set_ylim(0, 110)
    ax.set_title("Spectrum bias moves Se/Sp (absolute accuracy)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    # post-test at fixed prior 20% with different LR+
    priors = 0.20
    lr = se / (1 - sp)
    post = []
    for s_e, s_p in zip(se, sp):
        lrp = s_e / (1 - s_p)
        o = priors / (1 - priors)
        post.append((o * lrp) / (1 + o * lrp) * 100)
    ax.bar(x, post, color=[CORAL, INDIGO, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=8.5)
    ax.set_ylabel("Post-test % if + (prior 20%)")
    ax.set_title("Spectrum change rewrites absolute post-test risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, p in enumerate(post):
        ax.text(i, p + 1.5, f"{p:.0f}%", ha="center", fontsize=9, fontweight="bold", color=SLATE)

    fig.suptitle("Diagnostic accuracy: spectrum bias is an absolute problem (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch08_spectrum_bias.png")


def fig_ch12_net_benefit() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    labels = ["Ischemic\nARR", "sICH\nARI", "Net\nabsolute"]
    high = [6.0, 1.5, 4.5]
    low = [1.2, 1.5, -0.3]
    x = np.arange(len(labels))
    w = 0.35
    ax.bar(x - w / 2, high, width=w, color=TEAL, edgecolor=INDIGO, label="High baseline")
    ax.bar(x + w / 2, low, width=w, color=CORAL, edgecolor=INDIGO, label="Low baseline")
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Percentage points")
    ax.set_title("Net clinical benefit is absolute arithmetic", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Absolute effect translation checklist", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (7.5, INDIGO, "1 Extract CER & EER", "Same outcome · same horizon"),
        (5.5, GOLD, "2 ARR & CI", "Overlay MCID; note if CI includes 0"),
        (3.5, CORAL, "3 ARI & NNH", "Harms on same absolute scale"),
        (1.5, TEAL, "4 Net & NNT", "Net pp → treat count for one net win"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.7), 9.2, 1.7, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.7, y + 0.4, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.25, body, fontsize=8.3, color=SLATE)

    fig.suptitle("Effect sizes: net absolute benefit ledger (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch12_net_benefit.png")


def fig_ch16_ai_autopsy() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Autopsy recon · RapidLVO-like AI claim", fontsize=10, fontweight="bold", color=INDIGO)
    cells = [
        (8.0, INDIGO, "Claim", "AUROC 0.96 → autonomous triage"),
        (6.2, GOLD, "Estimand", "Detect LVO at ED CTA time zero"),
        (4.4, CORAL, "Threats", "Leakage · spectrum · site shift · Youden Pt"),
        (2.6, TEAL, "Absolute rebuild", "Local prev 8% → PPV ~40% even if Se/Sp high"),
        (0.8, PURPLE, "Action", "Human-in-loop pilot + calibration audit only"),
    ]
    for y, edge, title, body in cells:
        ax.add_patch(FancyBboxPatch((0.35, y - 0.55), 9.3, 1.5, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.3))
        ax.text(0.6, y + 0.35, title, fontsize=8.5, fontweight="bold", color=edge)
        ax.text(0.6, y - 0.2, body, fontsize=8.2, color=SLATE)

    ax = axes[1]
    labels = ["AUROC\n(hype)", "Local\nPPV", "Net benefit\n@Pt=15%", "Silent fail\nrate"]
    vals = [96, 40, 2, 8]
    colors = [GOLD, CORAL, TEAL, ORANGE]
    x = np.arange(len(labels))
    ax.bar(x, vals, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Value (mixed units teaching)")
    ax.set_title("Autopsy refuses AUROC-only verdicts", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)

    fig.suptitle("Paper autopsies: AI archetype absolute recon (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch16_ai_autopsy.png")


def fig_ch21_add_mult() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # two strata risks control/treat
    strata = ["Low risk", "High risk"]
    ctrl = np.array([4.0, 20.0])
    trt = np.array([3.0, 15.0])  # RR 0.75 both
    x = np.arange(len(strata))
    w = 0.35
    ax.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control")
    ax.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated")
    ax.set_xticks(x)
    ax.set_xticklabels(strata, fontsize=10)
    ax.set_ylabel("Event rate (%)")
    ax.set_title("Multiplicative homogeneous (RR=0.75)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    for i, (c, t) in enumerate(zip(ctrl, trt)):
        ax.text(i, max(c, t) + 0.8, f"ARR {c-t:.0f} pp\nRR {t/c:.2f}", ha="center", fontsize=8.5, fontweight="bold", color=SLATE)

    ax = axes[1]
    metrics = ["RR ratio\n(mult)", "ARR difference\n(add pp)"]
    vals = [1.0, 4.0]  # RR same → ratio 1; ARR 1 vs 5 → diff 4
    ax.bar([0, 1], vals, color=[GOLD, CORAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(metrics, fontsize=9)
    ax.set_ylabel("Interaction signal (synthetic units)")
    ax.set_title("No mult. interaction ≠ no additive HTE", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(0.5, 3.5, "Clinical decisions use additive absolute scale", ha="center", fontsize=8.5, color=PURPLE, style="italic")

    fig.suptitle("Interaction literacy: additive absolute HTE under constant RR (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch21_add_vs_mult.png")


def fig_ch23_base_rate() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # availability: rare dramatic case vs base rate
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Availability bias vs base-rate absolute", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5, 6.5), 9.0, 2.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(5, 8.3, "System-1: ‘Last week’s sICH after lytic’", ha="center", fontsize=10, fontweight="bold", color=CORAL)
    ax.text(5, 7.2, "Subjective harm probability → 20%", ha="center", fontsize=9, color=SLATE)
    ax.add_patch(FancyBboxPatch((0.5, 2.8), 9.0, 2.8, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(5, 4.6, "System-2 absolute: ARI ≈ 2% in eligible", ha="center", fontsize=10, fontweight="bold", color=TEAL)
    ax.text(5, 3.5, "Force natural frequencies before withholding", ha="center", fontsize=9, color=SLATE)
    ax.text(5, 1.2, "Debias: write ARI/NNH next to vivid case memory", ha="center", fontsize=8.5, color=PURPLE, style="italic")

    ax = axes[1]
    labels = ["Vivid\ncase prior", "Epidemiologic\nbase rate", "After forced\nabsolute card"]
    p = [20, 2, 2.5]
    ax.bar(np.arange(3), p, color=[CORAL, TEAL, GOLD], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(np.arange(3))
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Perceived sICH risk (%)")
    ax.set_title("Absolute card collapses availability inflation", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(p):
        ax.text(i, v + 0.4, f"{v:g}%", ha="center", fontsize=10, fontweight="bold", color=SLATE)

    fig.suptitle("Clinical reasoning: base-rate neglect is an absolute error (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch23_base_rate.png")


def fig_ch28_systems_memo() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("One-page systems memo strip", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (8.0, INDIGO, "Decision", "Adopt / Adapt+audit / De-implement / Wait"),
        (6.2, GOLD, "Absolute ledger", "ARR · ARI · NNT · NNH · horizon"),
        (4.4, TEAL, "Transport package", "Imaging · ICU · transfer · volume"),
        (2.6, CORAL, "Equity check", "ARR by access delay strata"),
        (0.8, PURPLE, "Audit metric", "What absolute outcome moves in 90 days?"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(FancyBboxPatch((0.35, y - 0.55), 9.3, 1.5, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.3))
        ax.text(0.6, y + 0.35, title, fontsize=8.5, fontweight="bold", color=edge)
        ax.text(0.6, y - 0.2, body, fontsize=8.2, color=SLATE)

    ax = axes[1]
    labels = ["Relative\nguideline\nlanguage only", "Memo with\nabsolute\n+ equity"]
    score = [30, 88]
    ax.bar([0, 1], score, color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Implementation readiness (synthetic)")
    ax.set_ylim(0, 100)
    ax.set_title("Policy without ARR is unfinished", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(score):
        ax.text(i, v + 2, f"{v}", ha="center", fontsize=11, fontweight="bold", color=SLATE)

    fig.suptitle("Systems of care: absolute action strip for policy memos (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle10_swarm_ch28_systems_memo.png")


def main() -> None:
    print("Cycle-10 swarm densify figures →", OUT)
    writers = [
        fig_ch04_selection,
        fig_ch08_spectrum,
        fig_ch12_net_benefit,
        fig_ch16_ai_autopsy,
        fig_ch21_add_mult,
        fig_ch23_base_rate,
        fig_ch28_systems_memo,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
