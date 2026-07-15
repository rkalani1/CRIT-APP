#!/usr/bin/env python3
"""
CRIT-APP Cycle-8 densify swarm: original matplotlib scientific teaching figures.

Clears residual floor-7 chapters after cycles 1–7:
  ch01 DFR absolute board ritual
  ch02 red-flag absolute stop under time pressure
  ch03 composite vs component absolute estimand
  ch07 residual confounding ARR tipping sensitivity
  ch09 horizon-specific absolute risk curves
  ch10 prediction interval on absolute ARR scale
  ch14 threshold utility absolute for stroke AI
  ch15 role-card absolute ownership in journal club

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle8_swarm_* only).
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


def fig_ch01_dfr_board() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("DFR board ritual (cannot skip absolute)", fontsize=10, fontweight="bold", color=INDIGO)
    items = [
        (8.0, INDIGO, "Decision named", "What changes Monday if true?"),
        (6.2, BLUE, "Estimand stated", "PICO · t0 · summary measure"),
        (4.4, GOLD, "ARR/NNT calculated", "CER/EER → ARR → NNT + horizon"),
        (2.6, CORAL, "Threats ranked", "Top 3 validity / transport risks"),
        (0.8, TEAL, "Action logged", "Act · Adapt+audit · Wait · Reject"),
    ]
    for y, edge, title, body in items:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.55), 9.2, 1.5, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.4))
        ax.text(0.7, y + 0.35, title, fontsize=9, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y - 0.2, body, fontsize=8.2, color=SLATE, va="center")

    ax = axes[1]
    labels = ["Relative\nonly read", "DFR absolute\nboard"]
    # synthetic quality of Monday decision
    score = [28, 86]
    colors = [CORAL, TEAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, score, color=colors, edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Decision readiness score (synthetic teaching)")
    ax.set_ylim(0, 100)
    ax.set_title("Culture metric: absolute first", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, score):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v}", ha="center", fontsize=11, fontweight="bold", color=SLATE)
    ax.text(0.5, 8, "prediction ≠ causation · ARR before pathway rewrite", ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle("Why appraisal matters: Decision-Focused Reading absolute board (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch01_dfr_board.png")


def fig_ch02_redflag_stop() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Time-pressure red flags → absolute stop", fontsize=10, fontweight="bold", color=INDIGO)
    flags = [
        (7.6, CORAL, "STOP A", "No denominator for absolute risks in abstract/tables"),
        (5.5, ORANGE, "STOP B", "Primary result only as RRR / HR without CER"),
        (3.4, GOLD, "STOP C", "t0 / analysis set ambiguous (ITT vs PP shopped)"),
        (1.3, PURPLE, "STOP D", "Action claimed without NNT horizon or harm ARI"),
    ]
    for y, edge, title, body in flags:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.7), 9.2, 1.8, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.5))
        ax.text(0.7, y + 0.45, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.2, body, fontsize=8.5, color=SLATE)

    ax = axes[1]
    steps = ["Scan\nabs", "Open\ntables", "Build\n2×2", "ARR\nNNT", "One-line\naction"]
    mins = [2, 4, 4, 3, 2]
    colors = [SLATE, INDIGO, BLUE, GOLD, TEAL]
    left = 0
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("15′ budget protects absolute arithmetic", fontsize=10, fontweight="bold", color=INDIGO)
    for m, c, s in zip(mins, colors, steps):
        ax.add_patch(plt.Rectangle((left, 1.5), m, 1.5, facecolor=c, edgecolor=WHITE, lw=2))
        ax.text(left + m / 2, 2.25, s, ha="center", va="center", fontsize=8, color=WHITE, fontweight="bold")
        left += m
    ax.add_patch(FancyBboxPatch((0.4, 0.35), 14.2, 0.9, boxstyle="round,pad=0.03,rounding_size=0.06",
                                facecolor="#FFF8E1", edgecolor=GOLD, lw=1.2))
    ax.text(7.5, 0.8, "If STOP A–D fire: refuse pathway language until absolute ledger exists",
            ha="center", va="center", fontsize=8.2, color=SLATE, fontweight="bold")

    fig.suptitle("Time-pressure reading: red-flag stops before relative spin (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch02_redflag_stop.png")


def fig_ch03_composite_component() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    comps = ["Disabling\nstroke", "Urgent\nrevasc", "CV death", "Composite\nheadline"]
    ctrl = np.array([4.0, 8.0, 1.5, 12.0])
    trt = np.array([3.6, 4.0, 1.4, 8.5])
    x = np.arange(len(comps))
    w = 0.35
    ax.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    ax.set_xticks(x)
    ax.set_xticklabels(comps, fontsize=8.5)
    ax.set_ylabel("Absolute event rate (%)")
    ax.set_title("Estimand honesty: composite vs components", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    for i, (c, t) in enumerate(zip(ctrl, trt)):
        ax.text(i, max(c, t) + 0.4, f"ARR {c-t:.1f}", ha="center", fontsize=7.8, fontweight="bold",
                color=CORAL if i == 3 else SLATE)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Index-time + outcome definition board", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (7.5, INDIGO, "Population", "Who is eligible at a single t0?"),
        (5.5, GOLD, "Intervention/comparator", "Actionable strategies, not labels"),
        (3.5, TEAL, "Outcome hierarchy", "Patient-important first; surrogates last"),
        (1.5, CORAL, "Summary measure", "Prefer ARR; attach horizon; disaggregate composites"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.7), 9.2, 1.7, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.7, y + 0.4, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.25, body, fontsize=8.3, color=SLATE)

    fig.suptitle("Questions & estimands: absolute components beat composite spin (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch03_composite_component.png")


def fig_ch07_tipping_arr() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # residual confounding prevalence vs bias in ARR
    prev = np.linspace(0.05, 0.6, 80)
    # simplified tipping: bias ≈ prev * RR_conf * risk_diff_conf
    bias = prev * 12  # pp of spurious ARR
    ax.plot(prev * 100, bias, color=CORAL, lw=2.5)
    ax.axhline(5, color=TEAL, ls="--", lw=1.5)
    ax.text(55, 5.4, "Observed ARR 5 pp", fontsize=8, color=TEAL, fontweight="bold")
    ax.fill_between(prev * 100, bias, 5, where=(bias >= 5), color=CORAL, alpha=0.12)
    ax.set_xlabel("Unmeasured confounder prevalence imbalance (%)")
    ax.set_ylabel("Spurious ARR inventable (pp)")
    ax.set_title("Tipping: how much residual confounding nulls ARR", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(5, 60)
    ax.set_ylim(0, 10)

    ax = axes[1]
    labels = ["Crude ARR", "Adjusted ARR", "After tipping\nnull", "Honest\naction"]
    vals = [10, 5, 0, 0]
    colors = [CORAL, GOLD, GRAY, TEAL]
    # last bar as categorical action - use text
    x = np.arange(3)
    ax.bar(x, vals[:3], color=colors[:3], edgecolor=INDIGO, width=0.6)
    ax.set_xticks([0, 1, 2])
    ax.set_xticklabels(labels[:3], fontsize=9)
    ax.set_ylabel("ARR (pp)")
    ax.set_ylim(0, 12)
    ax.set_title("Observational absolute ledger under QBA", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(vals[:3]):
        ax.text(i, v + 0.35, f"{v:g} pp", ha="center", fontsize=9, fontweight="bold", color=SLATE)
    ax.text(1.0, 10.5, "If plausible confounder can invent the ARR → do not pathway NNT",
            ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle("Observational appraisal: residual confounding tips absolute benefit to null (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch07_tipping_arr.png")


def fig_ch09_horizon_risk() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    t = np.array([7, 30, 90, 365])
    # cumulative incidence absolute risks high vs low risk strata
    hi = np.array([4, 9, 15, 28])
    lo = np.array([1, 2.5, 4, 8])
    ax.plot(t, hi, "o-", color=CORAL, lw=2.3, ms=8, label="High-risk stratum")
    ax.plot(t, lo, "s-", color=TEAL, lw=2.3, ms=8, label="Low-risk stratum")
    ax.set_xlabel("Horizon (days)")
    ax.set_ylabel("Cumulative absolute risk (%)")
    ax.set_title("Prognosis is horizon-specific absolute risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xticks(t)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Score deployment gates", fontsize=10, fontweight="bold", color=INDIGO)
    gates = [
        (7.4, INDIGO, "1 Discrimination", "Ranks patients (c-stat) — necessary, not sufficient"),
        (5.2, GOLD, "2 Calibration @ horizon", "Predicted % ≈ observed % at YOUR mix"),
        (3.0, TEAL, "3 Utility / action", "Does a risk stratum change monitoring or therapy?"),
        (0.8, CORAL, "4 Not causal", "High risk ≠ treat benefit without HTE evidence"),
    ]
    for y, edge, title, body in gates:
        ax.add_patch(FancyBboxPatch((0.35, y - 0.75), 9.3, 1.85, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.4))
        ax.text(0.65, y + 0.45, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.65, y - 0.25, body, fontsize=8.2, color=SLATE)

    fig.suptitle("Prognosis models: absolute risks by horizon; prediction ≠ causation (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch09_horizon_risk.png")


def fig_ch10_pred_interval_arr() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # forest-like ARR for 5 studies + pooled mean + prediction interval
    studies = ["S1", "S2", "S3", "S4", "S5", "Pooled\nmean", "Pred.\ninterval"]
    pts = [5.0, 2.0, 6.5, 3.5, 4.0, 4.0, 4.0]
    lo = [2.0, -1.0, 3.0, 0.5, 1.0, 2.5, -1.5]
    hi = [8.0, 5.0, 10.0, 6.5, 7.0, 5.5, 9.5]
    y = np.arange(len(studies))[::-1]
    for i, (p, l, h, name) in enumerate(zip(pts, lo, hi, studies)):
        yi = y[i]
        col = PURPLE if "Pred" in name else (INDIGO if "Pooled" in name else TEAL)
        lw = 4 if "Pooled" in name or "Pred" in name else 2.5
        ax.plot([l, h], [yi, yi], color=col, lw=lw, solid_capstyle="round")
        ax.plot(p, yi, "D" if "Pooled" in name else "o", color=GOLD if "Pred" in name else col, ms=8)
    ax.axvline(0, color=GRAY, lw=1.2)
    ax.set_yticks(y)
    ax.set_yticklabels(studies, fontsize=8.5)
    ax.set_xlabel("Absolute risk reduction (pp)")
    ax.set_title("Mean CI ≠ next-study prediction interval", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Synthesis decision rules", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (7.6, TEAL, "Fixed-effect mean", "Assumes one true ARR — often false in stroke"),
        (5.5, GOLD, "Random-effect mean", "Average of distribution; still not transport alone"),
        (3.4, CORAL, "Prediction interval", "Where a *new* study’s ARR may land"),
        (1.3, PURPLE, "Guideline action", "If PI includes 0 or harm → conditional recommendation"),
    ]
    for y0, edge, title, body in rows:
        ax.add_patch(FancyBboxPatch((0.35, y0 - 0.7), 9.3, 1.75, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.65, y0 + 0.4, title, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.65, y0 - 0.25, body, fontsize=8.2, color=SLATE)

    fig.suptitle("Meta-analysis: absolute ARR mean vs prediction interval (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch10_pred_interval_arr.png")


def fig_ch14_threshold_utility() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    thr = np.linspace(0.05, 0.6, 100)
    # synthetic net benefit curves
    prev = 0.12
    nb_all = prev - (1 - prev) * (thr / (1 - thr))
    nb_model = 0.08 - 0.25 * (thr / (1 - thr)) + 0.03
    nb_none = np.zeros_like(thr)
    ax.plot(thr * 100, nb_none, color=GRAY, lw=1.5, label="Alert none")
    ax.plot(thr * 100, nb_all, color=CORAL, lw=1.8, label="Alert all")
    ax.plot(thr * 100, nb_model, color=TEAL, lw=2.4, label="Model (synthetic)")
    ax.axvline(15, color=GOLD, ls="--", lw=1.3)
    ax.text(16, 0.1, "operating\nPt=15%", fontsize=8, color=GOLD, fontweight="bold")
    ax.set_xlabel("Alert threshold probability (%)")
    ax.set_ylabel("Net benefit")
    ax.set_xlim(5, 60)
    ax.set_ylim(-0.05, 0.15)
    ax.set_title("AI operating point is a utility choice", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    metrics = ["AUROC", "Sens\n@Pt", "Spec\n@Pt", "PPV\n@local", "Net\nbenefit"]
    vals = [0.92, 0.85, 0.70, 0.28, 0.04]
    # normalize display for bars of different meanings - show as teaching board
    colors = [INDIGO, BLUE, TEAL, GOLD, CORAL]
    x = np.arange(len(metrics))
    ax.bar(x, [v * 100 if v < 1 else v for v in vals], color=colors, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(x)
    ax.set_xticklabels(metrics, fontsize=8.5)
    ax.set_ylabel("Value (AUROC/Sens/Spec/PPV ×100; NB×100)")
    ax.set_title("Pretty AUROC can hide low absolute PPV", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(2, 95, "Deploy only if NB>0 in local Pt band\n& monitoring plan exists",
            ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle("AI/ML appraisal: threshold utility and local absolute PPV (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch14_threshold_utility.png")


def fig_ch15_role_cards() -> Path:
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("JC role cards with absolute ownership", fontsize=10, fontweight="bold", color=INDIGO)
    roles = [
        (7.5, INDIGO, "Facilitator", "Protects agenda; blocks early bottom line"),
        (5.5, GOLD, "Absolute officer", "Owns CER/EER/ARR/NNT/NNH on the board"),
        (3.5, CORAL, "Threat officer", "Names top 3 bias/transport threats"),
        (1.5, TEAL, "Action scribe", "Writes Act/Adapt/Wait/Reject sentence"),
    ]
    for y, edge, title, body in roles:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.7), 9.2, 1.7, boxstyle="round,pad=0.04,rounding_size=0.08",
                                    facecolor=WHITE, edgecolor=edge, lw=1.5))
        ax.text(0.7, y + 0.4, title, fontsize=9.5, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.25, body, fontsize=8.3, color=SLATE)

    ax = axes[1]
    labels = ["No absolute\nofficer", "With absolute\nofficer"]
    done = [35, 92]
    x = np.arange(len(labels))
    bars = ax.bar(x, done, color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("% sessions with complete ARR ledger (synthetic)")
    ax.set_ylim(0, 100)
    ax.set_title("Role design beats good intentions", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, done):
        ax.text(b.get_x() + b.get_width() / 2, v + 2, f"{v}%", ha="center", fontsize=11, fontweight="bold", color=SLATE)
    ax.text(0.5, 8, "No bottom line without the absolute officer’s sign-off", ha="center", fontsize=8, color=PURPLE, style="italic")

    fig.suptitle("Journal club architecture: assign absolute ownership (synthetic)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout()
    return _save(fig, "cycle8_swarm_ch15_role_cards.png")


def main() -> None:
    print("Cycle-8 swarm densify figures →", OUT)
    writers = [
        fig_ch01_dfr_board,
        fig_ch02_redflag_stop,
        fig_ch03_composite_component,
        fig_ch07_tipping_arr,
        fig_ch09_horizon_risk,
        fig_ch10_pred_interval_arr,
        fig_ch14_threshold_utility,
        fig_ch15_role_cards,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
