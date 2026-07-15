#!/usr/bin/env python3
"""
CRIT-APP Cycle-9 densify swarm: original matplotlib scientific teaching figures.

Raise floor from 8 toward 9 with scientific novelty on mid/late chapters:
  ch11 competing risks: CIF vs naive KM absolute
  ch13 spin: relative subgroup signal vs absolute HTE
  ch17 RD vs RR absolute teaching board
  ch18 causation frameworks: association strength ≠ absolute action
  ch20 RMST absolute years gained
  ch27 fragility of absolute events vs MCID
  ch06 mITT dilution residual (analysis set absolute)

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle9_swarm_* only).
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


def fig_ch11_cif_km() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    t = np.linspace(0, 90, 50)
    # naive KM overstates cumulative stroke risk when death competes
    cif_stroke = 1 - np.exp(-0.004 * t)
    cif_death = 1 - np.exp(-0.006 * t)
    km_naive = 1 - np.exp(-0.004 * t / (1 - 0.5 * cif_death))  # exaggerated
    km_naive = np.minimum(1 - (1 - cif_stroke) * (1 - 0.35 * cif_death), 0.55)
    ax.plot(t, cif_stroke * 100, color=TEAL, lw=2.5, label="CIF stroke (competing-risk)")
    ax.plot(t, km_naive * 100, color=CORAL, lw=2.2, ls="--", label="Naive 1−KM (overstates)")
    ax.plot(t, cif_death * 100, color=GRAY, lw=1.8, label="CIF death (competitor)")
    ax.set_xlabel("Days from index stroke")
    ax.set_ylabel("Cumulative incidence (%)")
    ax.set_title("Competing risk: death steals stroke events", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 90)

    ax = axes[1]
    labels = ["Naive KM\n90d stroke", "CIF\n90d stroke", "ARR if treat\n(naive)", "ARR if treat\n(CIF)"]
    vals = [22, 14, 6, 3.5]
    colors = [CORAL, TEAL, ORANGE, GOLD]
    x = np.arange(len(labels))
    bars = ax.bar(x, vals, color=colors, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8.5)
    ax.set_ylabel("Absolute %")
    ax.set_title("Absolute effects shrink under proper CIF", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.5, f"{v:g}", ha="center", fontsize=9, fontweight="bold", color=SLATE)

    fig.suptitle("Stroke outcomes: CIF vs naive KM on the absolute scale (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch11_cif_vs_km.png")


def fig_ch13_spin_hte() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    groups = ["Age <70", "Age ≥70", "Men", "Women", "NIHSS\nlow", "NIHSS\nhigh"]
    # relative RRR looks heterogeneous
    rrr = np.array([0.35, 0.18, 0.30, 0.28, 0.40, 0.15])
    x = np.arange(len(groups))
    ax.bar(x, rrr * 100, color=GOLD, edgecolor=INDIGO, width=0.65)
    ax.axhline(25, color=TEAL, ls="--", lw=1.3)
    ax.text(5.2, 26, "overall RRR 25%", fontsize=8, color=TEAL, ha="right")
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=8)
    ax.set_ylabel("Relative risk reduction (%)")
    ax.set_title("Spin bait: noisy relative subgroups", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.set_ylim(0, 50)

    ax = axes[1]
    # absolute ARR more honest - baseline differs
    cer = np.array([8, 20, 12, 11, 6, 28])
    arr = cer * 0.25  # homogeneous RRR → different ARR
    ax.bar(x, arr, color=TEAL, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(x)
    ax.set_xticklabels(groups, fontsize=8)
    ax.set_ylabel("Absolute risk reduction (pp) at RRR=25%")
    ax.set_title("Absolute HTE (baseline-driven) without interaction test", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(2.5, max(arr) + 0.8, "Demand interaction p + absolute strata; no cherry RRR",
            ha="center", fontsize=8, color=CORAL, fontweight="bold")

    fig.suptitle("Subgroups & spin: relative noise vs absolute stratum benefit (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch13_spin_hte.png")


def fig_ch17_rd_rr() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # 2x2 natural frequencies
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Association table → RD and RR", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((1.5, 5.5), 3.2, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(3.1, 7.5, "Exposed\nEvents 40 / 400", ha="center", va="center", fontsize=10, fontweight="bold", color=TEAL)
    ax.text(3.1, 6.2, "r1 = 10%", ha="center", fontsize=9, color=SLATE)
    ax.add_patch(FancyBboxPatch((5.3, 5.5), 3.2, 3.0, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(6.9, 7.5, "Unexposed\nEvents 30 / 600", ha="center", va="center", fontsize=10, fontweight="bold", color=CORAL)
    ax.text(6.9, 6.2, "r0 = 5%", ha="center", fontsize=9, color=SLATE)
    ax.add_patch(FancyBboxPatch((1.5, 1.2), 7.0, 3.5, boxstyle="round,pad=0.04,rounding_size=0.08",
                                facecolor="#FFF8E1", edgecolor=GOLD, lw=1.4))
    ax.text(5.0, 3.5, "RD = r1 − r0 = 5 pp\nRR = r1 / r0 = 2.0\nOR ≈ 2.11 (from odds)",
            ha="center", va="center", fontsize=11, fontweight="bold", color=SLATE)
    ax.text(5.0, 1.7, "Action lives on RD; RR alone hides baseline", ha="center", fontsize=8.5, color=PURPLE, style="italic")

    ax = axes[1]
    bases = np.array([2, 5, 10, 20])
    rr = 2.0
    rd = bases  # pp when RR=2 and r0=bases%
    ax.plot(bases, rd, "o-", color=INDIGO, lw=2.4, ms=9, label="RD (pp) at RR=2")
    ax.set_xlabel("Baseline risk r0 (%)")
    ax.set_ylabel("Risk difference (pp)")
    ax.set_title("Same RR=2 → different absolute RD", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    for b, d in zip(bases, rd):
        ax.text(b, d + 0.6, f"RD {d:g}", ha="center", fontsize=8, fontweight="bold", color=SLATE)
    ax.legend(fontsize=8)

    fig.suptitle("Disease frequency & association: RD carries absolute action (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch17_rd_vs_rr.png")


def fig_ch18_causation_abs() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Causation checklist ≠ absolute license", fontsize=10, fontweight="bold", color=INDIGO)
    items = [
        (8.0, INDIGO, "Temporality", "Exposure before outcome at aligned t0"),
        (6.2, BLUE, "Strength / dose", "Large adjusted association — still not ARR"),
        (4.4, GOLD, "Specificity / bio", "Mechanism plausible — not decision-ready"),
        (2.6, TEAL, "Experiment / TTE", "Target trial or RCT for causal treat claim"),
        (0.8, CORAL, "Absolute action", "Only then compute ARR/NNT for pathway"),
    ]
    for y, edge, title, body in items:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.55), 9.2, 1.45, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.7, y + 0.3, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.2, body, fontsize=8.2, color=SLATE)

    ax = axes[1]
    labels = ["Strong\nassociation\n(RR 3)", "After\nconfound\nfix", "Causal ARR\nif valid", "If residual\nbias remains"]
    vals = [15, 6, 4, 0]
    colors = [GOLD, ORANGE, TEAL, CORAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, vals, color=colors, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Claimed absolute effect (pp, synthetic)")
    ax.set_title("Association strength shrinks toward action-grade ARR", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, vals):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v:g}", ha="center", fontsize=9, fontweight="bold", color=SLATE)

    fig.suptitle("Causation frameworks: from association rhetoric to absolute action (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch18_causation_abs.png")


def fig_ch20_rmst() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    t = np.linspace(0, 365, 200)
    s0 = np.exp(-0.0025 * t)
    s1 = np.exp(-0.0016 * t)
    ax.plot(t, s0, color=CORAL, lw=2.3, label="Control survival")
    ax.plot(t, s1, color=TEAL, lw=2.3, label="Treated survival")
    ax.fill_between(t, s0, s1, color=GOLD, alpha=0.35, label="RMST difference area")
    ax.set_xlabel("Days")
    ax.set_ylabel("Survival probability")
    ax.set_title("RMST: absolute time gained under the curves", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="lower left")
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 365)
    ax.set_ylim(0, 1.02)

    ax = axes[1]
    labels = ["HR only\n(0.70)", "1-year\nmortality ARR", "RMST Δ\nto 1 year"]
    # teaching: HR abstract vs absolute
    # show as categorical cards
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Report absolute time, not HR alone", fontsize=10, fontweight="bold", color=INDIGO)
    cards = [
        (7.2, CORAL, "Hazard ratio 0.70", "Relative instantaneous rate — hard to counsel"),
        (4.4, GOLD, "ARR death 6 pp @ 1y", "NNT ≈ 17 to prevent one death in 1 year"),
        (1.6, TEAL, "RMST +18 days", "Average absolute days of life gained to horizon"),
    ]
    for y, edge, title, body in cards:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.9), 9.2, 2.2, boxstyle="round,pad=0.05,rounding_size=0.1",
                                    facecolor=WHITE, edgecolor=edge, lw=1.5))
        ax.text(5.0, y + 0.55, title, ha="center", fontsize=10, fontweight="bold", color=edge)
        ax.text(5.0, y - 0.35, body, ha="center", fontsize=8.5, color=SLATE)

    fig.suptitle("Survival literacy: RMST as absolute time benefit (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch20_rmst.png")


def fig_ch27_fragility() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # 2x2 counts
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Fragility: events to flip significance", fontsize=10, fontweight="bold", color=INDIGO)
    ax.text(5, 9.0, "Treated 40/500 vs Control 60/500  → ARR 4 pp, p≈0.03",
            ha="center", fontsize=9, fontweight="bold", color=SLATE)
    ax.add_patch(FancyBboxPatch((0.8, 5.0), 8.4, 3.2, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(5, 7.2, "Flip only 3 treated non-events → events", ha="center", fontsize=11, fontweight="bold", color=CORAL)
    ax.text(5, 6.1, "Fragility index ≈ 3  (tiny for pathway rewrite)", ha="center", fontsize=9.5, color=SLATE)
    ax.add_patch(FancyBboxPatch((0.8, 1.2), 8.4, 3.0, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(5, 3.2, "MCID = 5 pp ARR  → result below clinical importance", ha="center", fontsize=10, fontweight="bold", color=TEAL)
    ax.text(5, 2.1, "Statistically fragile AND clinically modest", ha="center", fontsize=9, color=SLATE)

    ax = axes[1]
    labels = ["Fragility\nindex", "Events for\nMCID miss", "Missing\noutcomes", "Honest\nposture"]
    vals = [3, 5, 12, 0]
    colors = [CORAL, GOLD, ORANGE, TEAL]
    x = np.arange(3)
    ax.bar(x, vals[:3], color=colors[:3], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(x)
    ax.set_xticklabels(labels[:3], fontsize=9)
    ax.set_ylabel("Event counts (synthetic)")
    ax.set_title("Absolute fragility vs missingness budget", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(1.0, 13, "If missing ≫ fragility, do not claim robust ARR",
            ha="center", fontsize=8.5, color=PURPLE, style="italic")

    fig.suptitle("Missing data & fragility: absolute events that unmake significance (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch27_fragility.png")


def fig_ch06_mitt_dilution() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    sets = ["As randomized\nITT", "mITT\n(received ≥1 dose)", "Per-protocol\ncompliers"]
    n = np.array([1000, 860, 720])
    arr = np.array([3.5, 4.8, 7.0])
    x = np.arange(len(sets))
    ax.bar(x, arr, color=[TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.62)
    ax.set_xticks(x)
    ax.set_xticklabels(sets, fontsize=8.5)
    ax.set_ylabel("ARR (pp)")
    ax.set_title("Analysis set shopping inflates absolute effect", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, (a, ni) in enumerate(zip(arr, n)):
        ax.text(i, a + 0.25, f"ARR {a}\nn={ni}", ha="center", fontsize=8.5, fontweight="bold", color=SLATE)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Appraisal rule for analysis sets", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (7.4, TEAL, "Primary ITT ARR", "Policy estimand; may dilute biology"),
        (5.2, GOLD, "mITT definition", "Was exclusion post-randomization?"),
        (3.0, CORAL, "PP as causal claim", "Reintroduced confounding — observational"),
        (0.8, PURPLE, "Report both", "Never replace ITT with prettier PP NNT alone"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(FancyBboxPatch((0.35, y - 0.75), 9.3, 1.85, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.4))
        ax.text(0.65, y + 0.4, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.65, y - 0.3, body, fontsize=8.3, color=SLATE)

    fig.suptitle("RCT appraisal residual: mITT/PP absolute inflation vs ITT (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle9_swarm_ch06_mitt_dilution.png")


def main() -> None:
    print("Cycle-9 swarm densify figures →", OUT)
    writers = [
        fig_ch11_cif_km,
        fig_ch13_spin_hte,
        fig_ch17_rd_rr,
        fig_ch18_causation_abs,
        fig_ch20_rmst,
        fig_ch27_fragility,
        fig_ch06_mitt_dilution,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
