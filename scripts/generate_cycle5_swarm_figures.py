#!/usr/bin/env python3
"""
CRIT-APP Cycle-5 densify swarm: original matplotlib scientific teaching figures.

Targets residual lowest-image chapters after cycles 1–4 (~6 imgs each):
  ch15 journal-club claim→decision gate + absolute-effect slot
  ch03 index-time misalignment / immortal-time counterexample
  ch02 15-minute triage: validity → absolute → transport
  ch07 confounding-by-indication residual + E-value on absolute scale
  ch14 calibration vs discrimination; prevalence→PPV for stroke AI
  ch09 predicted risk ≠ causal benefit; decision-curve net benefit
  ch01 RRR headline vs ARR/NNT bedside cost of misreading

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle5_swarm_* only). Does not redo cycle1–4 figures.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle, Polygon
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


def _box(ax, x, y, w, h, edge, title, body, title_fs=8.5, body_fs=7.8):
    ax.add_patch(
        FancyBboxPatch(
            (x, y),
            w,
            h,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor=WHITE,
            edgecolor=edge,
            lw=1.35,
        )
    )
    ax.text(x + 0.15, y + h - 0.35, title, fontsize=title_fs, fontweight="bold", color=edge, va="center")
    ax.text(x + 0.15, y + h * 0.38, body, fontsize=body_fs, color=SLATE, va="center")


def fig_ch15_jc_decision_gate() -> Path:
    """Journal-club claim→decision gate with mandatory absolute-effect slot."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    # Left: linear gate flow
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Claim → decision gate (must pass every slot)", fontsize=10, fontweight="bold", color=INDIGO)

    stages = [
        (8.4, TEAL, "1. Claim named", "Therapy / harm / diagnosis / prognosis?"),
        (6.6, BLUE, "2. Estimand board", "P · I · C · O · t0 · summary measure"),
        (4.8, GOLD, "3. Absolute-effect slot", "CER, EER, ARR, NNT/NNH + CIs  (MANDATORY)"),
        (3.0, CORAL, "4. Threat rank", "Top 3 validity threats + transport gaps"),
        (1.2, PURPLE, "5. Action menu", "Act · Adapt+audit · Wait · Design · Reject"),
    ]
    for y, edge, title, body in stages:
        ax.add_patch(
            FancyBboxPatch(
                (0.4, y - 0.55),
                9.2,
                1.55,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.5,
            )
        )
        ax.text(0.7, y + 0.35, title, fontsize=9, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y - 0.2, body, fontsize=8, color=SLATE, va="center")
        if y > 1.5:
            ax.annotate(
                "",
                xy=(5.0, y - 0.7),
                xytext=(5.0, y - 0.95),
                arrowprops=dict(arrowstyle="-|>", color=GRAY, lw=1.4),
            )

    # Right: time budget protecting absolute slot
    ax = axes[1]
    labels = ["Hook\n& stake", "PICO /\nestimand", "Methods\nmap", "Abs effects\nARR/NNT", "Red flags\n+ action"]
    mins = np.array([3, 5, 12, 12, 18])
    colors = [SLATE, BLUE, INDIGO, GOLD, TEAL]
    x = np.arange(len(labels))
    bars = ax.bar(x, mins, color=colors, edgecolor=INDIGO, width=0.68)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=8)
    ax.set_ylabel("Minutes in a 50-min journal club (synthetic)")
    ax.set_ylim(0, 22)
    ax.set_title("Protect the absolute-effect block (do not skip)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, v in zip(bars, mins):
        ax.text(b.get_x() + b.get_width() / 2, v + 0.4, f"{v}′", ha="center", fontsize=9, fontweight="bold", color=SLATE)
    ax.axhline(12, color=GOLD, ls="--", lw=1.1, alpha=0.8)
    ax.text(4.35, 12.5, "≥12′ for absolute ledger", fontsize=7.5, color=GOLD, ha="right", fontweight="bold")

    fig.suptitle(
        "Journal-club architecture: no bottom line without ARR/NNT (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch15_jc_decision_gate.png")


def fig_ch03_index_time() -> Path:
    """Index-time alignment vs immortal-time misclassification."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    # Left: aligned t0
    ax = axes[0]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Valid t0: eligibility · assignment · follow-up aligned", fontsize=10, fontweight="bold", color=INDIGO)

    ax.axvline(3.0, color=TEAL, lw=2.5)
    ax.text(3.0, 7.4, "t0", ha="center", fontsize=10, fontweight="bold", color=TEAL)
    for y, lab, col in [
        (5.8, "Eligibility met", BLUE),
        (4.2, "Treatment assigned", INDIGO),
        (2.6, "Outcome clock starts", GREEN),
    ]:
        ax.plot([3.0, 11.0], [y, y], color=col, lw=3.5, solid_capstyle="round")
        ax.plot(3.0, y, "o", color=col, ms=10, zorder=5)
        ax.text(3.3, y + 0.45, lab, fontsize=8.5, color=col, fontweight="bold")
    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.35),
            11.2,
            1.5,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#E8F5E9",
            edgecolor=GREEN,
            lw=1.3,
        )
    )
    ax.text(
        6.0,
        1.1,
        "RCT randomization enforces alignment. Observational designs must emulate it.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
    )

    # Right: immortal time
    ax = axes[1]
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Broken t0: immortal time favors ‘treated’", fontsize=10, fontweight="bold", color=INDIGO)

    # Discharge as false t0
    ax.axvline(2.0, color=CORAL, lw=2.0, ls="--")
    ax.text(2.0, 7.4, "discharge\n(false t0)", ha="center", fontsize=8, color=CORAL, fontweight="bold")
    # Rehab session day 45
    ax.axvline(7.0, color=TEAL, lw=2.0)
    ax.text(7.0, 7.4, "1st rehab\nsession", ha="center", fontsize=8, color=TEAL, fontweight="bold")

    # Unexposed: early death counted
    ax.plot([2.0, 4.5], [5.5, 5.5], color=CORAL, lw=4, solid_capstyle="round")
    ax.plot(4.5, 5.5, "X", color=CORAL, ms=12, mew=2)
    ax.text(3.2, 6.0, "Early death → forced ‘unexposed’", fontsize=8, color=CORAL, fontweight="bold")

    # Exposed: guaranteed survival window
    ax.plot([2.0, 7.0], [3.5, 3.5], color=GOLD, lw=6, solid_capstyle="round", alpha=0.85)
    ax.plot([7.0, 11.0], [3.5, 3.5], color=TEAL, lw=4, solid_capstyle="round")
    ax.plot(7.0, 3.5, "o", color=TEAL, ms=10)
    ax.text(4.5, 4.05, "Immortal window counted as exposed time", ha="center", fontsize=8, color=GOLD, fontweight="bold")
    ax.text(9.0, 4.05, "true exposure", ha="center", fontsize=7.5, color=TEAL)

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.35),
            11.2,
            1.7,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.3,
        )
    )
    ax.text(
        6.0,
        1.2,
        "Fix: landmark at day 90, time-varying exposure, or sequential target-trial emulation.\nNever invent NNTs from mis-timed observational associations.",
        ha="center",
        va="center",
        fontsize=8,
        color=SLATE,
    )

    fig.suptitle(
        "Estimands & index time: three clocks must agree at t0 (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch03_index_time.png")


def fig_ch02_triage_stack() -> Path:
    """15-minute paper triage card stack: validity → absolute → transport."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Card stack under time pressure (order is the method)", fontsize=10, fontweight="bold", color=INDIGO)

    cards = [
        (7.3, 0.35, INDIGO, "CARD 1 · Validity", "Design match? t0? ITT vs PP?\nTop bias threat named in one line"),
        (5.0, 0.55, GOLD, "CARD 2 · Absolute", "CER / EER → ARR → NNT\nARI → NNH · attach time horizon"),
        (2.7, 0.75, TEAL, "CARD 3 · Transport", "Who was excluded? Can we deliver?\nLocal CER → recalculated ARR"),
        (0.5, 0.95, PURPLE, "CARD 4 · Action", "Adopt · Adapt+audit · Wait · Reject\nOne sentence for the team board"),
    ]
    for y, xoff, edge, title, body in cards:
        ax.add_patch(
            FancyBboxPatch(
                (0.5 + xoff, y),
                8.2,
                2.0,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=WHITE,
                edgecolor=edge,
                lw=2.0,
            )
        )
        ax.text(0.85 + xoff, y + 1.45, title, fontsize=9.5, fontweight="bold", color=edge)
        ax.text(0.85 + xoff, y + 0.55, body, fontsize=8.2, color=SLATE)

    ax = axes[1]
    # Time budget pie-like horizontal
    phases = ["0–2′\nTriage", "2–7′\nTables", "7–11′\nMethods", "11–14′\nThreats", "14–15′\nAction"]
    mins = [2, 5, 4, 3, 1]
    colors = [SLATE, GOLD, INDIGO, CORAL, TEAL]
    left = 0.0
    ax.set_xlim(0, 15)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("15-minute compression (keep absolute block)", fontsize=10, fontweight="bold", color=INDIGO)
    for m, c, lab in zip(mins, colors, phases):
        ax.add_patch(Rectangle((left, 1.6), m, 1.4, facecolor=c, edgecolor=WHITE, lw=2, alpha=0.9))
        ax.text(left + m / 2, 2.3, lab, ha="center", va="center", fontsize=7.8, color=WHITE, fontweight="bold")
        left += m
    ax.text(7.5, 0.9, "Never drop Card 2 (absolute). Compress narrative, not arithmetic.", ha="center", fontsize=8.5, color=SLATE, style="italic")

    # Mini ARR example
    ax.add_patch(
        FancyBboxPatch(
            (0.5, 3.35),
            14.0,
            0.55,
            boxstyle="round,pad=0.02,rounding_size=0.05",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.1,
        )
    )
    ax.text(
        7.5,
        3.62,
        "Synthetic: CER 10% → EER 7% · ARR 3 pp · NNT ≈ 33 | ARI 1 pp · NNH = 100",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
        fontweight="bold",
    )

    fig.suptitle(
        "Time-pressure reading: validity → absolute → transport → action (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch02_triage_stack.png")


def fig_ch07_confounding_evalue() -> Path:
    """Confounding-by-indication residual bias + E-value on absolute scale."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.2))

    # Left: crude vs stratified absolute risks (confounding by indication)
    ax = axes[0]
    # High severity: treated more often, worse prognosis
    groups = ["Mild\n(unadj.)", "Severe\n(unadj.)", "Mild\nstratum", "Severe\nstratum"]
    # Crude: mix — treated look better overall but...
    # Teaching: within-stratum ARR fixed at 5 pp; crude inflates
    # Show treated vs control bars for crude pool vs strata
    cats = ["Crude\npool", "Mild\nstratum", "Severe\nstratum"]
    ctrl = np.array([28.0, 12.0, 45.0])
    trt = np.array([15.0, 7.0, 40.0])  # crude ARR inflated; strata ARR = 5
    x = np.arange(len(cats))
    w = 0.35
    b1 = ax.bar(x - w / 2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control event rate %")
    b2 = ax.bar(x + w / 2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated event rate %")
    ax.set_xticks(x)
    ax.set_xticklabels(cats, fontsize=9)
    ax.set_ylabel("90-day death or dependence (%)")
    ax.set_ylim(0, 55)
    ax.set_title("Confounding by indication: crude ARR lies", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    arrs = ctrl - trt
    for i, a in enumerate(arrs):
        ax.text(i, max(ctrl[i], trt[i]) + 2.0, f"ARR {a:.0f} pp", ha="center", fontsize=8, fontweight="bold", color=CORAL if i == 0 else GREEN)

    ax.annotate(
        "Crude mixes severity\n(treated = sicker)",
        xy=(0, 28),
        xytext=(-0.35, 48),
        fontsize=7.5,
        color=CORAL,
        arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=1.2),
    )

    # Right: E-value + absolute residual
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("E-value on RR + absolute residual ledger", fontsize=10, fontweight="bold", color=INDIGO)

    # RR = 0.80 example from chapter
    rr = 0.80
    inv = 1 / rr
    e = inv + np.sqrt(inv * (inv - 1))

    boxes = [
        (7.6, INDIGO, "Observed adjusted RR", f"RR = {rr:.2f}  →  inv RR = {inv:.2f}"),
        (5.7, GOLD, "E-value (approx)", f"E = inv + √[inv(inv−1)] ≈ {e:.2f}"),
        (3.8, CORAL, "Clinical read", "Frailty/goals-of-care easily ≥1.8×\n→ signal fragile; do not rewrite pathway"),
        (1.7, TEAL, "Absolute residual (synthetic)", "If true ARR = 0 but crude ARR = 8 pp,\nresidual confounding invented NNT ≈ 12"),
        (0.15, PURPLE, "Discipline", "Never invert confounded HR into NNT;\nprediction ≠ causation for treatment choice"),
    ]
    for y, edge, title, body in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.5),
                9.4,
                1.7,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.55, y + 0.55, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.1, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Observational appraisal: indication confounding + E-value on absolute terms (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch07_confounding_evalue.png")


def fig_ch14_cal_disc_ppv() -> Path:
    """Calibration vs discrimination; prevalence collapse of PPV for stroke AI."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    # Left: calibration plot concept vs ROC-only fetish
    ax = axes[0]
    rng = np.random.default_rng(7)
    # Overconfident model: predicted extremes, observed pulled to mean
    pred = np.linspace(0.05, 0.95, 10)
    obs_over = 0.25 + 0.5 * pred  # slope < 1
    obs_good = pred.copy()
    ax.plot([0, 1], [0, 1], "--", color=GRAY, lw=1.3, label="Perfect calibration")
    ax.plot(pred, obs_good, "o-", color=TEAL, lw=2, ms=7, label="Well calibrated")
    ax.plot(pred, obs_over, "s-", color=CORAL, lw=2, ms=7, label="Overconfident (slope < 1)")
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Predicted probability")
    ax.set_ylabel("Observed event frequency")
    ax.set_title("Discrimination ranks; calibration prices risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, alpha=0.3)
    ax.text(0.55, 0.12, "AUROC can be identical\nwhile absolute risks lie", fontsize=8, color=CORAL, fontweight="bold")

    # Right: prevalence → PPV at fixed Se/Sp
    ax = axes[1]
    se, sp = 0.90, 0.90
    prev = np.linspace(0.01, 0.40, 80)
    # PPV = Se*p / (Se*p + (1-Sp)*(1-p))
    ppv = (se * prev) / (se * prev + (1 - sp) * (1 - prev))
    ax.plot(prev * 100, ppv * 100, color=INDIGO, lw=2.5)
    # Markers for stroke AI contexts
    mark_p = np.array([0.02, 0.08, 0.25])
    mark_ppv = (se * mark_p) / (se * mark_p + (1 - sp) * (1 - mark_p))
    labs = ["ED dizziness\n(~2%)", "Code stroke\n(~8%)", "LVO-enriched\n(~25%)"]
    ax.scatter(mark_p * 100, mark_ppv * 100, s=70, color=GOLD, zorder=5, edgecolor=INDIGO)
    for p, v, lab in zip(mark_p, mark_ppv, labs):
        ax.annotate(
            f"{lab}\nPPV≈{v*100:.0f}%",
            xy=(p * 100, v * 100),
            xytext=(p * 100 + 6, v * 100 - 12 if p < 0.15 else v * 100 - 8),
            fontsize=7.5,
            color=SLATE,
            arrowprops=dict(arrowstyle="-|>", color=GOLD, lw=1.1),
        )
    ax.set_xlabel("True prevalence of target finding (%)")
    ax.set_ylabel("PPV at Se=Sp=0.90 (%)")
    ax.set_xlim(0, 42)
    ax.set_ylim(0, 100)
    ax.set_title("Same model, different floor: prevalence owns PPV", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    ax.axhline(50, color=CORAL, ls=":", lw=1.1)
    ax.text(40, 52, "coin-flip PPV", fontsize=7.5, color=CORAL, ha="right")

    fig.suptitle(
        "AI/ML appraisal: calibration + prevalence-conditioned PPV (synthetic stroke AI)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch14_cal_disc_ppv.png")


def fig_ch09_pred_vs_causal_dca() -> Path:
    """Predicted risk is not causal benefit; decision-curve net benefit sketch."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    # Left: prediction vs causal fork
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("High predicted risk ≠ treatment benefit", fontsize=10, fontweight="bold", color=INDIGO)

    ax.add_patch(
        FancyBboxPatch(
            (2.5, 7.8),
            5.0,
            1.5,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor=WHITE,
            edgecolor=INDIGO,
            lw=1.6,
        )
    )
    ax.text(5.0, 8.55, "Risk score high\n(prognosis only)", ha="center", va="center", fontsize=9, fontweight="bold", color=INDIGO)

    # Two branches
    ax.annotate("", xy=(2.2, 5.8), xytext=(4.0, 7.7), arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=2))
    ax.annotate("", xy=(7.8, 5.8), xytext=(6.0, 7.7), arrowprops=dict(arrowstyle="-|>", color=TEAL, lw=2))

    ax.add_patch(
        FancyBboxPatch(
            (0.3, 3.6),
            4.0,
            2.4,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.5,
        )
    )
    ax.text(
        2.3,
        4.8,
        "Misread\n‘Treat because high risk’\n\nNeeds causal HTE /\nRCT interaction",
        ha="center",
        va="center",
        fontsize=8,
        color=CORAL,
        fontweight="bold",
    )

    ax.add_patch(
        FancyBboxPatch(
            (5.7, 3.6),
            4.0,
            2.4,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor="#E8F5E9",
            edgecolor=TEAL,
            lw=1.5,
        )
    )
    ax.text(
        7.7,
        4.8,
        "Correct use\nCounsel absolute risk\nCalibrate + validate\nDecide via utility",
        ha="center",
        va="center",
        fontsize=8,
        color=TEAL,
        fontweight="bold",
    )

    ax.add_patch(
        FancyBboxPatch(
            (0.5, 0.4),
            9.0,
            2.4,
            boxstyle="round,pad=0.04,rounding_size=0.08",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.3,
        )
    )
    ax.text(
        5.0,
        1.6,
        "Statin-at-admission OR 1.4 in a prognostic model is association\nproxy (access, frailty), not a license to start a drug at door time.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
    )

    # Right: decision curve sketch
    ax = axes[1]
    pt = np.linspace(0.01, 0.60, 120)
    prev = 0.20
    # Treat all net benefit = prev - (1-prev)*pt/(1-pt)
    nb_all = prev - (1 - prev) * (pt / (1 - pt))
    # Synthetic model better in mid range
    nb_model = 0.55 * prev - 0.35 * (1 - prev) * (pt / (1 - pt)) + 0.02
    nb_none = np.zeros_like(pt)
    ax.plot(pt * 100, nb_none, color=GRAY, lw=1.5, label="Treat none (NB=0)")
    ax.plot(pt * 100, nb_all, color=CORAL, lw=1.8, label="Treat all")
    ax.plot(pt * 100, nb_model, color=TEAL, lw=2.4, label="Model (synthetic)")
    ax.fill_between(
        pt * 100,
        nb_model,
        np.maximum(nb_all, 0),
        where=(nb_model > np.maximum(nb_all, 0)),
        color=TEAL,
        alpha=0.15,
        label="Useful threshold band",
    )
    ax.set_xlim(0, 60)
    ax.set_ylim(-0.05, 0.25)
    ax.set_xlabel("Threshold probability Pt (%)")
    ax.set_ylabel("Net benefit (per patient)")
    ax.set_title("Decision curve: utility beats AUROC alone", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.2, loc="upper right")
    ax.grid(True, alpha=0.3)
    ax.axvline(10, color=GOLD, ls="--", lw=1.1)
    ax.text(11, 0.22, "example Pt=10%", fontsize=7.5, color=GOLD)

    fig.suptitle(
        "Prognosis models: prediction ≠ causation; net benefit decides deployment (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch09_pred_vs_causal_dca.png")


def fig_ch01_rrr_vs_arr_cost() -> Path:
    """Why appraisal matters: RRR headline vs ARR/NNT bedside cost of misreading."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))

    # Left: same RRR 25% at two baselines
    ax = axes[0]
    labels = ["High-risk\nminor stroke\nCER 8%", "Low-risk\nclinic TIA\nCER 2%"]
    rrr = 0.25
    cer = np.array([0.08, 0.02])
    arr = cer * rrr * 100  # pp
    nnt = 100 / arr
    x = np.arange(len(labels))
    bars = ax.bar(x, arr, color=[TEAL, GOLD], edgecolor=INDIGO, width=0.55)
    ax.set_xticks(x)
    ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Absolute risk reduction (pp) at RRR=25%")
    ax.set_ylim(0, 3.2)
    ax.set_title("Same RRR headline; different bedside reality", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for b, a, n in zip(bars, arr, nnt):
        ax.text(
            b.get_x() + b.get_width() / 2,
            a + 0.12,
            f"ARR {a:.1f} pp\nNNT ≈ {n:.0f}",
            ha="center",
            fontsize=8.5,
            fontweight="bold",
            color=SLATE,
        )
    ax.text(0.5, 2.85, "Press release: ‘25% fewer strokes!’", ha="center", fontsize=8.5, color=CORAL, fontweight="bold", style="italic")

    # Right: cost of misreading ledger
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Cost of skipping absolute appraisal", fontsize=10, fontweight="bold", color=INDIGO)

    rows = [
        (7.8, CORAL, "Clinical", "Treat 200 low-risk patients to match\nbenefit of 50 high-risk patients (same RRR)"),
        (5.7, ORANGE, "Harm ledger", "Fixed ARI 0.5 pp · NNH 200 — net may invert\nwhen baseline ischemic risk collapses"),
        (3.6, GOLD, "Operational", "Pathway rewritten on relative spin →\ncapacity spent where ARR is tiny"),
        (1.5, TEAL, "DFR fix", "Decision named · estimand stated ·\nARR/NNT calculated · action logged"),
        (0.1, PURPLE, "Rule", "prediction ≠ causation; absolute first"),
    ]
    for y, edge, title, body in rows:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.45),
                9.4,
                1.75,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.55, y + 0.55, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.1, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Why appraisal matters: relative headlines hide absolute opportunity cost (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle5_swarm_ch01_rrr_vs_arr_cost.png")


def main() -> None:
    print("Cycle-5 swarm densify figures →", OUT)
    writers = [
        fig_ch15_jc_decision_gate,
        fig_ch03_index_time,
        fig_ch02_triage_stack,
        fig_ch07_confounding_evalue,
        fig_ch14_cal_disc_ppv,
        fig_ch09_pred_vs_causal_dca,
        fig_ch01_rrr_vs_arr_cost,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
