#!/usr/bin/env python3
"""
CRIT-APP cycle-1 swarm: original matplotlib (Agg) teaching figures.

Generates code-drawn PNGs under docs/assets/figures/. Never imports commercial
art or DOCX content. Safe to re-run (overwrites only swarm_* outputs and
selected crit_fig_* regenerations).
"""
from __future__ import annotations

import os
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Circle, Rectangle
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


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    return path


def fig_reading_triage() -> Path:
    """Twenty-minute paper triage (ch02)."""
    fig, ax = plt.subplots(figsize=(10.5, 5.2))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title(
        "Twenty-Minute Paper Triage (Stroke/Neuro Service Reading)",
        fontsize=13,
        fontweight="bold",
        color=INDIGO,
        pad=12,
    )
    steps = [
        (0.4, 3.6, "0–2 min\nTitle + abstract\nspin screen", TEAL),
        (3.0, 3.6, "2–6 min\nFigures/tables\nfirst", TEAL),
        (5.6, 3.6, "6–10 min\nMethods: design,\nindex time, bias", TEAL),
        (2.0, 1.0, "10–14 min\nAbsolute effects\n+ CI", GOLD),
        (5.0, 1.0, "14–17 min\nApplicability to\nyour population", GOLD),
        (8.0, 1.0, "17–20 min\nDecision /\nredesign notes", CORAL),
    ]
    for x, y, text, color in steps:
        box = FancyBboxPatch(
            (x, y), 2.2, 1.7, boxstyle="round,pad=0.05,rounding_size=0.15",
            facecolor=color, edgecolor=INDIGO, linewidth=1.2, alpha=0.92,
        )
        ax.add_patch(box)
        ax.text(x + 1.1, y + 0.85, text, ha="center", va="center",
                fontsize=8.5, color=WHITE, fontweight="bold")
    # arrows top
    for x0, x1 in [(2.6, 3.0), (5.2, 5.6)]:
        ax.annotate("", xy=(x1, 4.45), xytext=(x0, 4.45),
                    arrowprops=dict(arrowstyle="->", color=INDIGO, lw=1.6))
    # down from step3
    ax.annotate("", xy=(6.7, 2.7), xytext=(6.7, 3.55),
                arrowprops=dict(arrowstyle="->", color=INDIGO, lw=1.6))
    # bottom chain
    ax.annotate("", xy=(5.0, 1.85), xytext=(4.2, 1.85),
                arrowprops=dict(arrowstyle="->", color=INDIGO, lw=1.6))
    ax.annotate("", xy=(8.0, 1.85), xytext=(7.2, 1.85),
                arrowprops=dict(arrowstyle="->", color=INDIGO, lw=1.6))
    # left return path
    ax.annotate("", xy=(3.1, 1.85), xytext=(6.7, 2.7),
                arrowprops=dict(arrowstyle="->", color=INDIGO, lw=1.2,
                                connectionstyle="arc3,rad=0.25"))
    ax.text(9.6, 4.9, "Optional early stop\nif design cannot\nanswer the decision",
            fontsize=7.5, color=CORAL,
            bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL))
    ax.text(6, 0.25,
            "Primary path: 0–2 → 2–6 → 6–10 → 10–14 → 14–17 → 17–20.  "
            "Never accept RR headlines without baseline risk + ARR/NNT.",
            ha="center", fontsize=7.5, color=SLATE,
            bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"))
    return _save(fig, "swarm_ch02_reading_triage.png")


def fig_bias_taxonomy() -> Path:
    """Three bias families + transport (ch04)."""
    fig, ax = plt.subplots(figsize=(9.5, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Bias Families vs Transportability", fontsize=13,
                 fontweight="bold", color=INDIGO, pad=10)
    families = [
        (0.4, 3.2, "Selection\nbias", "Who enters\nthe sample?"),
        (2.7, 3.2, "Confounding", "Shared causes\nof Rx & outcome"),
        (5.0, 3.2, "Information\nbias", "Misclassified\nexposure/outcome"),
        (7.3, 3.2, "Reporting\nbias", "What is shown\nvs suppressed?"),
    ]
    for x, y, title, sub in families:
        box = FancyBboxPatch((x, y), 2.0, 2.0, boxstyle="round,pad=0.08,rounding_size=0.12",
                             facecolor="#E8EAF6", edgecolor=INDIGO, linewidth=1.5)
        ax.add_patch(box)
        ax.text(x + 1.0, y + 1.35, title, ha="center", va="center",
                fontsize=9, fontweight="bold", color=INDIGO)
        ax.text(x + 1.0, y + 0.55, sub, ha="center", va="center", fontsize=7.5, color=SLATE)
    ax.add_patch(FancyBboxPatch((1.5, 0.5), 7.0, 1.6, boxstyle="round,pad=0.08,rounding_size=0.12",
                                facecolor="#FFF8E1", edgecolor=GOLD, linewidth=1.5))
    ax.text(5.0, 1.55, "External validity / transport", ha="center", fontsize=10,
            fontweight="bold", color="#F57F17")
    ax.text(5.0, 0.95, "Internally valid estimate may still fail for your catchment,\n"
            "case-mix, co-interventions, or care system.",
            ha="center", fontsize=8, color=SLATE)
    return _save(fig, "swarm_ch04_bias_taxonomy.png")


def fig_immortal_time() -> Path:
    """Immortal time schematic (ch07)."""
    fig, ax = plt.subplots(figsize=(9.5, 4.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("Immortal Time Bias (Registry / Claims Design Flaw)",
                 fontsize=12, fontweight="bold", color=INDIGO)
    # time axis
    ax.annotate("", xy=(9.2, 1.2), xytext=(0.8, 1.2),
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.5))
    ax.text(9.4, 1.2, "Time", va="center", fontsize=8, color=SLATE)
    ax.plot([1.5, 1.5], [1.0, 4.2], color=SLATE, lw=1.2, ls="--")
    ax.text(1.5, 4.4, "Admission\n(time zero?)", ha="center", fontsize=7.5, color=SLATE)
    # treated person
    ax.plot([1.5, 4.0], [3.4, 3.4], color="#90A4AE", lw=8, solid_capstyle="butt")
    ax.plot([4.0, 8.0], [3.4, 3.4], color=TEAL, lw=8, solid_capstyle="butt")
    ax.plot(4.0, 3.4, "o", color=GOLD, markersize=10)
    ax.text(0.3, 3.4, "Treated", va="center", fontsize=8, fontweight="bold")
    ax.text(2.7, 3.75, "immortal\n(must survive\nto start drug)", ha="center",
            fontsize=7, color=CORAL)
    ax.text(6.0, 3.75, "exposed follow-up", ha="center", fontsize=7.5, color=TEAL)
    # control
    ax.plot([1.5, 6.5], [2.0, 2.0], color=CORAL, lw=8, solid_capstyle="butt", alpha=0.7)
    ax.text(0.3, 2.0, "Control", va="center", fontsize=8, fontweight="bold")
    ax.text(4.0, 1.55, "events during early window count against control",
            ha="center", fontsize=7.5, color=CORAL)
    ax.text(5.0, 0.45,
            "Fix: align time zero (new-user / landmark / time-varying exposure).",
            ha="center", fontsize=8, color=SLATE,
            bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"))
    return _save(fig, "swarm_ch07_immortal_time.png")


def fig_calibration() -> Path:
    """Calibration plot (ch09)."""
    fig, ax = plt.subplots(figsize=(6.5, 5.5))
    rng = np.random.default_rng(7)
    pred = np.linspace(0.05, 0.9, 9)
    obs = pred + rng.normal(0, 0.04, size=pred.shape)
    obs = np.clip(obs + 0.06 * (pred - 0.5), 0.02, 0.95)  # mild overprediction mid
    ax.plot([0, 1], [0, 1], "--", color="#9E9E9E", lw=1.5, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2, markersize=8, label="Model (synthetic)")
    ax.fill_between(pred, obs - 0.05, obs + 0.05, color=INDIGO, alpha=0.12)
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_xlabel("Predicted risk", fontsize=10)
    ax.set_ylabel("Observed event rate", fontsize=10)
    ax.set_title("Calibration: predicted vs observed (teaching plot)",
                 fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.text(0.55, 0.18, "AUROC can look strong while\nabsolute risks are miscalibrated.",
            fontsize=8, color=SLATE,
            bbox=dict(boxstyle="round", facecolor="#FFF8E1", edgecolor=GOLD))
    return _save(fig, "swarm_ch09_calibration.png")


def fig_forest() -> Path:
    """Simple forest plot (ch10)."""
    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    studies = ["Study A", "Study B", "Study C", "Pooled"]
    rr = np.array([0.67, 0.75, 0.82, 0.72])
    lo = np.array([0.55, 0.58, 0.60, 0.62])
    hi = np.array([0.81, 0.97, 1.12, 0.84])
    y = np.arange(len(studies))[::-1]
    colors = [TEAL, TEAL, TEAL, CORAL]
    for i, (yi, r, l, h, c) in enumerate(zip(y, rr, lo, hi, colors)):
        ax.plot([l, h], [yi, yi], color=c, lw=2.2)
        marker = "D" if i == len(studies) - 1 else "o"
        ax.plot(r, yi, marker, color=c, markersize=9 if i == len(studies) - 1 else 8)
    ax.axvline(1.0, color=SLATE, ls="--", lw=1.2)
    ax.set_yticks(y)
    ax.set_yticklabels(studies)
    ax.set_xlabel("Risk ratio (log scale teaching sketch)")
    ax.set_xscale("log")
    ax.set_xlim(0.45, 1.35)
    ax.set_title("Forest plot intuition (synthetic teaching data)",
                 fontsize=11, fontweight="bold", color=INDIGO)
    ax.text(0.5, -0.9, "Convert pooled RR → ARR = CER × (1−RR) → NNT before acting.",
            transform=ax.transAxes, fontsize=8, color=SLATE)
    ax.grid(True, axis="x", alpha=0.25)
    return _save(fig, "swarm_ch10_forest.png")


def fig_mrs_shift() -> Path:
    """mRS stacked bars (ch11)."""
    fig, ax = plt.subplots(figsize=(8.0, 4.8))
    cats = ["mRS 0", "1", "2", "3", "4", "5", "6"]
    ctrl = np.array([8, 12, 15, 18, 17, 15, 15], dtype=float)
    tx = np.array([14, 18, 18, 16, 14, 10, 10], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum()
    tx = 100 * tx / tx.sum()
    colors = ["#1B5E20", "#43A047", "#9CCC65", "#FFF176", "#FFB74D", "#E57373", "#B71C1C"]
    x = np.array([0, 1.2])
    bottoms = np.zeros(2)
    for i, c in enumerate(colors):
        vals = [ctrl[i], tx[i]]
        ax.bar(x, vals, bottom=bottoms, width=0.7, color=c, edgecolor="white",
               label=cats[i])
        bottoms += vals
    ax.set_xticks(x)
    ax.set_xticklabels(["Control", "Treatment"])
    ax.set_ylabel("Percent of cohort")
    ax.set_title("mRS distribution shift (synthetic teaching figure)",
                 fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(ncol=7, fontsize=7, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100)
    ax.text(0.5, 1.02, "Never trust a common OR without inspecting where mass moved.",
            transform=ax.transAxes, ha="center", fontsize=8, color=SLATE)
    return _save(fig, "swarm_ch11_mrs_shift.png")


def fig_ai_leakage() -> Path:
    """Train/test leakage (ch14)."""
    fig, ax = plt.subplots(figsize=(9.0, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("AI Appraisal: Leakage vs Honest Split", fontsize=12,
                 fontweight="bold", color=INDIGO)
    # bad
    ax.add_patch(FancyBboxPatch((0.4, 2.6), 4.2, 2.0, boxstyle="round,pad=0.08,rounding_size=0.12",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(2.5, 4.2, "Leakage path (optimistic)", ha="center", fontsize=9,
            fontweight="bold", color=CORAL)
    ax.text(2.5, 3.4, "Normalize / feature select\non full cohort → then split\n"
            "→ inflated AUROC, fails outside",
            ha="center", fontsize=8, color=SLATE)
    # good
    ax.add_patch(FancyBboxPatch((5.4, 2.6), 4.2, 2.0, boxstyle="round,pad=0.08,rounding_size=0.12",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(7.5, 4.2, "Honest path", ha="center", fontsize=9,
            fontweight="bold", color=TEAL)
    ax.text(7.5, 3.4, "Split by patient/site first\n→ preprocess train only\n"
            "→ external site validation",
            ha="center", fontsize=8, color=SLATE)
    ax.add_patch(FancyBboxPatch((1.5, 0.4), 7.0, 1.5, boxstyle="round,pad=0.08,rounding_size=0.12",
                                facecolor=LIGHT, edgecolor=INDIGO, lw=1.2))
    ax.text(5.0, 1.15, "Also demand: calibration, prevalence-anchored PPV/NPV,\n"
            "and performance under site shift—not AUROC alone.",
            ha="center", va="center", fontsize=8.5, color=SLATE)
    return _save(fig, "swarm_ch14_ai_leakage.png")


def fig_jc_roles() -> Path:
    """Journal club roles (ch15)."""
    fig, ax = plt.subplots(figsize=(8.5, 5.0))
    ax.set_xlim(0, 8)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Journal Club Role Map (Decision-Focused)", fontsize=12,
                 fontweight="bold", color=INDIGO)
    roles = [
        (0.5, 4.0, "Chair", "Locks the decision\n& time box"),
        (3.0, 4.0, "Methods", "Design, bias,\nestimand"),
        (5.5, 4.0, "Numbers", "ARR / NNT /\nCI vs MID"),
        (1.75, 1.5, "Transport", "Our patients &\nsystem fidelity"),
        (4.25, 1.5, "Action scribe", "Act / Conditional /\nWatch / No change"),
    ]
    for x, y, title, sub in roles:
        ax.add_patch(FancyBboxPatch((x, y), 2.2, 1.6, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.4))
        ax.text(x + 1.1, y + 1.1, title, ha="center", fontsize=9, fontweight="bold", color=INDIGO)
        ax.text(x + 1.1, y + 0.5, sub, ha="center", fontsize=7.5, color=SLATE)
    return _save(fig, "swarm_ch15_jc_roles.png")


def fig_estimation_ci() -> Path:
    """CI as estimation not dichotomania (ch19)."""
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    estimates = [
        ("Imprecise\nbenefit-possible", 0.06, -0.01, 0.13, TEAL),
        ("Tiny but\n'significant'", 0.004, 0.001, 0.007, GOLD),
        ("Clear benefit\nvs MID", 0.10, 0.06, 0.14, "#2E7D32"),
    ]
    for i, (lab, pe, lo, hi, c) in enumerate(estimates):
        y = 2 - i
        ax.plot([lo, hi], [y, y], color=c, lw=3)
        ax.plot(pe, y, "o", color=c, markersize=10)
        ax.text(-0.045, y, lab, ha="right", va="center", fontsize=8, color=SLATE)
    ax.axvline(0, color=SLATE, ls="--", lw=1)
    ax.axvline(0.03, color=CORAL, ls=":", lw=1.5)
    ax.text(0.03, 2.45, "example MID", color=CORAL, fontsize=7.5, ha="center")
    ax.set_xlim(-0.05, 0.16)
    ax.set_ylim(-0.6, 2.8)
    ax.set_yticks([])
    ax.set_xlabel("Absolute risk reduction")
    ax.set_title("Estimation culture: read the interval against MID, not only p < 0.05",
                 fontsize=10, fontweight="bold", color=INDIGO)
    ax.spines["left"].set_visible(False)
    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)
    return _save(fig, "swarm_ch19_estimation_ci.png")


def fig_survival_censoring() -> Path:
    """Censoring vs event (ch20)."""
    fig, ax = plt.subplots(figsize=(8.5, 4.0))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("Time-to-Event Literacy: Events vs Censoring", fontsize=12,
                 fontweight="bold", color=INDIGO)
    rows = [
        (3.8, "Event at t", CORAL, 7.0, "X"),
        (2.6, "Censored at t", TEAL, 5.5, "|"),
        (1.4, "Still at risk", INDIGO, 10.5, "→"),
    ]
    ax.annotate("", xy=(11, 0.7), xytext=(1.5, 0.7),
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.3))
    ax.text(11.2, 0.7, "Time", va="center", fontsize=8)
    for y, lab, color, end, mark in rows:
        ax.text(0.2, y, lab, va="center", fontsize=8, fontweight="bold", color=color)
        ax.plot([1.5, end], [y, y], color=color, lw=3)
        ax.plot(end, y, marker=mark if mark != "→" else ">", color=color, markersize=10)
    ax.text(6, 4.5, "Censoring removes a person from the risk set without counting an event.\n"
            "Competing death is not neutral censoring for recurrent stroke risk.",
            ha="center", fontsize=8, color=SLATE,
            bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"))
    return _save(fig, "swarm_ch20_survival.png")


def fig_interaction_scales() -> Path:
    """Additive vs multiplicative interaction (ch21)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.2))
    # additive
    ax = axes[0]
    groups = ["A−B−", "A+B−", "A−B+", "A+B+"]
    risk = [0.05, 0.10, 0.12, 0.25]
    ax.bar(groups, risk, color=[TEAL, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.set_title("Risk (additive scale)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylabel("Event risk")
    ax.set_ylim(0, 0.35)
    ax.axhline(0.05 + (0.10 - 0.05) + (0.12 - 0.05), ls="--", color=SLATE, lw=1)
    ax.text(3, 0.28, "A+B+ exceeds\nadditive null", ha="center", fontsize=7.5, color=CORAL)
    # multi
    ax = axes[1]
    rr = [1.0, 2.0, 2.4, 5.0]
    ax.bar(groups, rr, color=[TEAL, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.set_title("Risk ratio (multiplicative)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylabel("RR vs A−B−")
    ax.set_ylim(0, 6)
    ax.axhline(2.0 * 2.4, ls="--", color=SLATE, lw=1)
    ax.text(3, 5.2, "same data,\ndifferent story", ha="center", fontsize=7.5, color=CORAL)
    fig.suptitle("Interaction depends on scale (synthetic teaching data)",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "swarm_ch21_interaction.png")


def fig_screening_biases() -> Path:
    """Lead-time / length / overdiagnosis (ch22)."""
    fig, ax = plt.subplots(figsize=(9.0, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("Screening Appraisal Traps (Original Sketch)", fontsize=12,
                 fontweight="bold", color=INDIGO)
    items = [
        (0.4, "Lead time", "Diagnosis earlier\nwithout longer life\n→ survival looks better"),
        (3.5, "Length bias", "Slow lesions\nover-represented\nin screen-detected set"),
        (6.6, "Overdiagnosis", "Detect lesions that\nwould never cause\nclinical harm"),
    ]
    colors = [TEAL, GOLD, CORAL]
    for (x, title, body), c in zip(items, colors):
        ax.add_patch(FancyBboxPatch((x, 1.2), 2.8, 3.0, boxstyle="round,pad=0.1,rounding_size=0.15",
                                    facecolor=WHITE, edgecolor=c, lw=2))
        ax.text(x + 1.4, 3.6, title, ha="center", fontsize=10, fontweight="bold", color=c)
        ax.text(x + 1.4, 2.4, body, ha="center", fontsize=8, color=SLATE)
    ax.text(5, 0.5, "Demand disease-specific mortality and absolute overdiagnosis estimates.",
            ha="center", fontsize=8.5, color=SLATE)
    return _save(fig, "swarm_ch22_screening.png")


def fig_dual_process() -> Path:
    """System 1/2 (ch23)."""
    fig, ax = plt.subplots(figsize=(8.5, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("Dual-Process Use of Evidence", fontsize=12, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5, 1.5), 3.8, 2.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#FFF3E0", edgecolor=GOLD, lw=1.8))
    ax.text(2.4, 3.8, "System 1", ha="center", fontsize=11, fontweight="bold", color="#E65100")
    ax.text(2.4, 2.7, "Fast pattern match\nAbstract spin, social proof,\nrelative-risk headlines",
            ha="center", fontsize=8.5, color=SLATE)
    ax.add_patch(FancyBboxPatch((5.7, 1.5), 3.8, 2.8, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.8))
    ax.text(7.6, 3.8, "System 2", ha="center", fontsize=11, fontweight="bold", color=INDIGO)
    ax.text(7.6, 2.7, "Forced structure\nPICO, bias taxonomy,\nARR/NNT, transport",
            ha="center", fontsize=8.5, color=SLATE)
    ax.annotate("", xy=(5.6, 2.9), xytext=(4.4, 2.9),
                arrowprops=dict(arrowstyle="->", color=SLATE, lw=2))
    ax.text(5.0, 0.7, "Appraisal checklists are System-2 scaffolds under time pressure.",
            ha="center", fontsize=8.5, color=SLATE)
    return _save(fig, "swarm_ch23_dual_process.png")


def fig_therapy_harm() -> Path:
    """Benefit-harm card (ch24)."""
    fig, ax = plt.subplots(figsize=(8.0, 4.2))
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 5)
    ax.set_title("Therapy vs Harm Absolute-Effect Card", fontsize=12,
                 fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5, 1.2), 4.0, 3.0, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#E8F5E9", edgecolor=TEAL, lw=1.8))
    ax.text(2.5, 3.7, "Benefit", ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(2.5, 2.5, "ARR = p_c − p_t\nNNT = 1 / ARR\n(time horizon required)",
            ha="center", fontsize=9, color=SLATE)
    ax.add_patch(FancyBboxPatch((5.5, 1.2), 4.0, 3.0, boxstyle="round,pad=0.1,rounding_size=0.15",
                                facecolor="#FFEBEE", edgecolor=CORAL, lw=1.8))
    ax.text(7.5, 3.7, "Harm", ha="center", fontsize=11, fontweight="bold", color=CORAL)
    ax.text(7.5, 2.5, "ARI = p_t(h) − p_c(h)\nNNH = 1 / ARI\n(weight outcome severity)",
            ha="center", fontsize=9, color=SLATE)
    ax.text(5, 0.55, "Same horizon; absolute scale; never RR alone for counseling.",
            ha="center", fontsize=8.5, color=SLATE)
    return _save(fig, "swarm_ch24_therapy_harm.png")


def fig_diagnostic_2x2() -> Path:
    """2x2 table (ch25)."""
    fig, ax = plt.subplots(figsize=(6.5, 5.0))
    ax.set_xlim(0, 6)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Diagnostic 2×2 Scaffold", fontsize=12, fontweight="bold", color=INDIGO)
    # headers
    ax.text(3.5, 5.4, "Reference standard", ha="center", fontsize=9, fontweight="bold")
    ax.text(2.5, 4.9, "D+", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.text(4.5, 4.9, "D−", ha="center", fontsize=9, fontweight="bold", color=TEAL)
    ax.text(0.7, 3.0, "Index\ntest", ha="center", va="center", fontsize=9, fontweight="bold", rotation=90)
    cells = [
        (1.5, 3.2, "T+", "TP", "#FFCDD2"),
        (3.5, 3.2, "", "FP", "#FFE0B2"),
        (1.5, 1.4, "T−", "FN", "#FFE0B2"),
        (3.5, 1.4, "", "TN", "#C8E6C9"),
    ]
    for x, y, lab, cell, color in cells:
        ax.add_patch(FancyBboxPatch((x, y), 1.8, 1.5, boxstyle="round,pad=0.05,rounding_size=0.08",
                                    facecolor=color, edgecolor=INDIGO, lw=1.2))
        ax.text(x + 0.9, y + 0.75, cell, ha="center", va="center", fontsize=14,
                fontweight="bold", color=INDIGO)
        if lab:
            ax.text(x - 0.35, y + 0.75, lab, ha="center", va="center",
                    fontsize=9, fontweight="bold")
    ax.text(3, 0.5, "Se=TP/(TP+FN)  Sp=TN/(TN+FP)  LR+=Se/(1−Sp)  PPV needs prevalence",
            ha="center", fontsize=7.5, color=SLATE)
    return _save(fig, "swarm_ch25_diagnostic_2x2.png")


def fig_cpr_lifecycle() -> Path:
    """CPR lifecycle (ch26)."""
    fig, ax = plt.subplots(figsize=(9.5, 3.8))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 4)
    ax.axis("off")
    ax.set_title("Clinical Prediction Rule Lifecycle", fontsize=12,
                 fontweight="bold", color=INDIGO)
    stages = ["Derive", "Internal\nvalidate", "External\nvalidate", "Impact /\nimplementation"]
    xs = [0.8, 3.6, 6.4, 9.2]
    for i, (x, s) in enumerate(zip(xs, stages)):
        ax.add_patch(FancyBboxPatch((x, 1.3), 2.2, 1.6, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.4))
        ax.text(x + 1.1, 2.1, s, ha="center", va="center", fontsize=9,
                fontweight="bold", color=INDIGO)
        if i < len(xs) - 1:
            ax.annotate("", xy=(xs[i + 1], 2.1), xytext=(x + 2.2, 2.1),
                        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.6))
    ax.text(6, 0.6, "Skipping external validation or impact evaluation is not 'early adoption'—it is deployment risk.",
            ha="center", fontsize=8, color=SLATE)
    return _save(fig, "swarm_ch26_cpr_lifecycle.png")


def fig_fragility_missing() -> Path:
    """Fragility + missingness (ch27)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.5, 4.0))
    ax = axes[0]
    ax.set_title("Fragility intuition", fontsize=10, fontweight="bold", color=INDIGO)
    ax.bar([0, 1], [40, 28], color=[CORAL, TEAL], edgecolor=INDIGO)
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Control\nevents", "Treatment\nevents"])
    ax.set_ylabel("Event counts (synthetic n=200/arm)")
    ax.text(0.5, 42, "Flip a few events\n→ significance vanishes",
            ha="center", fontsize=8, color=SLATE)
    ax = axes[1]
    ax.set_xlim(0, 5)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title("Missingness mechanisms", fontsize=10, fontweight="bold", color=INDIGO)
    for i, (lab, note) in enumerate([
        ("MCAR", "missingness ⊥ data"),
        ("MAR", "missingness ~ observed"),
        ("MNAR", "missingness ~ unobserved"),
    ]):
        y = 3.6 - i * 1.2
        ax.add_patch(FancyBboxPatch((0.3, y - 0.4), 4.2, 1.0,
                                    boxstyle="round,pad=0.05,rounding_size=0.1",
                                    facecolor=LIGHT, edgecolor=INDIGO, lw=1.1))
        ax.text(0.6, y, lab, fontsize=9, fontweight="bold", color=INDIGO, va="center")
        ax.text(2.0, y, note, fontsize=8, color=SLATE, va="center")
    fig.suptitle("Fragility, multiplicity, interim looks, and missing data",
                 fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "swarm_ch27_fragility_missing.png")


def fig_natural_frequencies() -> Path:
    """Natural frequencies communication (ch28)."""
    fig, ax = plt.subplots(figsize=(8.0, 4.5))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title("Natural Frequencies for Systems & Counseling", fontsize=12,
                 fontweight="bold", color=INDIGO)
    # 100 people icon row
    rng = np.random.default_rng(3)
    for i in range(10):
        for j in range(10):
            idx = i * 10 + j
            if idx < 8:
                c = CORAL  # events without
            elif idx < 10:
                c = TEAL  # prevented
            else:
                c = "#CFD8DC"
            ax.add_patch(Circle((0.8 + j * 0.35, 4.5 - i * 0.32), 0.12, color=c))
    ax.text(4.6, 3.5,
            "Of 100 similar patients over the horizon:\n"
            "• 8 events expected without strategy\n"
            "• 6 events expected with strategy\n"
            "• 2 events prevented (ARR 2%, NNT 50)\n\n"
            "Systems also ask: how many never reach care?",
            fontsize=9, color=SLATE, va="top",
            bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"))
    ax.text(2.4, 0.6, "Red = event without  |  Teal = prevented  |  Gray = no event",
            ha="center", fontsize=8, color=SLATE)
    return _save(fig, "swarm_ch28_natural_frequencies.png")


def fig_autopsy_flow() -> Path:
    """Paper autopsy sequence (ch16)."""
    fig, ax = plt.subplots(figsize=(9.5, 3.5))
    ax.set_xlim(0, 12)
    ax.set_ylim(0, 3.5)
    ax.axis("off")
    ax.set_title("Paper Autopsy Sequence", fontsize=12, fontweight="bold", color=INDIGO)
    steps = ["Claim", "Design", "Absolute\neffect", "Transport", "Decide"]
    xs = np.linspace(0.6, 9.5, len(steps))
    for i, (x, s) in enumerate(zip(xs, steps)):
        ax.add_patch(FancyBboxPatch((x, 1.1), 1.9, 1.4, boxstyle="round,pad=0.08,rounding_size=0.12",
                                    facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.4))
        ax.text(x + 0.95, 1.8, s, ha="center", va="center", fontsize=9,
                fontweight="bold", color=INDIGO)
        if i < len(steps) - 1:
            ax.annotate("", xy=(xs[i + 1], 1.8), xytext=(x + 1.9, 1.8),
                        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.5))
    ax.text(6, 0.45, "Act · Conditional · Watch · No change — never 'interesting' alone.",
            ha="center", fontsize=8.5, color=SLATE)
    return _save(fig, "swarm_ch16_autopsy_flow.png")


def fig_nnt_icon() -> Path:
    """Correct NNT icon array (ARR 10% → NNT 10)."""
    fig, ax = plt.subplots(figsize=(6.2, 6.5))
    ax.set_xlim(-0.05, 1.05)
    ax.set_ylim(-0.25, 1.08)
    ax.set_aspect("equal")
    ax.axis("off")
    # 100 people: baseline 20% → 10% with treatment ⇒ ARR 10%, NNT 10
    # 10 prevented (green), 10 events despite Rx (salmon), 80 no event (gray)
    k = 0
    for row in range(10):
        for col in range(10):
            if k < 10:
                color = "#43A047"  # prevented
            elif k < 20:
                color = "#E57373"  # still event
            else:
                color = "#B0BEC5"
            ax.add_patch(Circle((col * 0.1 + 0.05, 0.95 - row * 0.1), 0.035, color=color))
            k += 1
    ax.set_title("Icon array: ARR 10% → NNT 10 (synthetic)", fontsize=11,
                 fontweight="bold", color=INDIGO)
    ax.text(0.5, -0.08,
            "Green = events prevented (10)   Red = events despite treatment (10)\n"
            "Gray = no event (80)   Baseline risk 20% → treated risk 10%",
            ha="center", va="top", fontsize=8, color=SLATE)
    return _save(fig, "swarm_nnt_icon_array.png")


def fig_bayes_lr() -> Path:
    """Bayes with LR+ = 5 (matches ch08 caption)."""
    fig, ax = plt.subplots(figsize=(7.5, 4.5))
    priors = np.array([0.05, 0.10, 0.20, 0.40, 0.60])
    lr = 5.0
    posts = []
    for p in priors:
        odds = p / (1 - p)
        posts.append((odds * lr) / (1 + odds * lr))
    posts = np.array(posts)
    x = np.arange(len(priors))
    w = 0.35
    ax.bar(x - w / 2, priors, width=w, label="Pre-test", color="#90A4AE", edgecolor=INDIGO)
    ax.bar(x + w / 2, posts, width=w, label="Post-test (LR+ = 5)", color=TEAL, edgecolor=INDIGO)
    ax.set_xticks(x)
    ax.set_xticklabels([f"{int(p*100)}%" for p in priors])
    ax.set_xlabel("Pre-test probability")
    ax.set_ylabel("Probability")
    ax.set_ylim(0, 1)
    ax.set_title("Bayes update with LR+ = 5 (synthetic priors)", fontsize=11,
                 fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    return _save(fig, "crit_fig_bayes_lr.png")


def main() -> None:
    generators = [
        fig_reading_triage,
        fig_bias_taxonomy,
        fig_immortal_time,
        fig_calibration,
        fig_forest,
        fig_mrs_shift,
        fig_ai_leakage,
        fig_jc_roles,
        fig_estimation_ci,
        fig_survival_censoring,
        fig_interaction_scales,
        fig_screening_biases,
        fig_dual_process,
        fig_therapy_harm,
        fig_diagnostic_2x2,
        fig_cpr_lifecycle,
        fig_fragility_missing,
        fig_natural_frequencies,
        fig_autopsy_flow,
        fig_nnt_icon,
        fig_bayes_lr,
    ]
    paths = []
    for fn in generators:
        p = fn()
        paths.append(p)
        print("wrote", p.relative_to(ROOT))
    print(f"Generated {len(paths)} figures into {OUT}")


if __name__ == "__main__":
    main()
