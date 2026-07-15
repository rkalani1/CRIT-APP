#!/usr/bin/env python3
"""
CRIT-APP 3h-swarm cycle-2: original matplotlib scientific teaching figures.

Targets mid/late chapters (17–22, 24–28) that still need denser mid-chapter
scientific plots. Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle2_* outputs only).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch, Rectangle
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


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch17_rate_vs_risk() -> Path:
    """Same incidence rate → different cumulative risks by follow-up window (ch17)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    # Constant incidence rate λ = 0.20 / year → cum risk = 1 - exp(-λ t)
    lam = 0.20
    t_days = np.array([30, 90, 180, 365, 730])
    t_years = t_days / 365.25
    cum_risk = 1.0 - np.exp(-lam * t_years)
    # Naive "annualized" misuse: rate × time as if linear risk
    naive = np.minimum(lam * t_years, 0.99)

    ax = axes[0]
    x = np.arange(len(t_days))
    w = 0.36
    ax.bar(x - w / 2, cum_risk * 100, width=w, color=TEAL, edgecolor=INDIGO, label="True cum. risk\n1−e^(−λt)")
    ax.bar(x + w / 2, naive * 100, width=w, color="#90A4AE", edgecolor=INDIGO, label="Naive λ×t\n(rate misused as risk)")
    ax.set_xticks(x)
    ax.set_xticklabels([f"{d}d" for d in t_days])
    ax.set_ylabel("Cumulative incidence (%)")
    ax.set_xlabel("Follow-up window")
    ax.set_ylim(0, 55)
    ax.set_title("Fixed rate λ = 0.20 / person-year", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper left")
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Appraisal rule (synthetic teaching)", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (8.2, "Metric", "Clock", "Units"),
        (6.6, "Risk / cum. incidence", "Fixed window", "% by day 90"),
        (5.0, "Incidence rate", "Person-time", "events / 100 py"),
        (3.4, "Trial primary often", "90-day risk", "mRS, sICH, death"),
        (1.8, "Prevention often", "Person-time rate", "recurrent stroke / py"),
    ]
    for i, (y, a, b, c) in enumerate(rows):
        fc = "#E8EAF6" if i == 0 else WHITE
        for text, x0, width in [(a, 0.3, 3.4), (b, 3.8, 2.8), (c, 6.7, 3.0)]:
            ax.add_patch(
                FancyBboxPatch(
                    (x0, y - 0.55),
                    width,
                    1.15,
                    boxstyle="round,pad=0.02,rounding_size=0.06",
                    facecolor=fc,
                    edgecolor=INDIGO,
                    lw=0.9,
                )
            )
            ax.text(
                x0 + width / 2,
                y + 0.05,
                text,
                ha="center",
                va="center",
                fontsize=7.5 if i else 8.5,
                fontweight="bold" if i == 0 else "normal",
                color=INDIGO if i == 0 else SLATE,
            )
    ax.text(
        5.0,
        0.35,
        "Never put an annualized rate next to a 90-day risk without conversion.",
        ha="center",
        fontsize=8,
        color=CORAL,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    fig.suptitle(
        "Rate versus risk: same incidence rate, different clocks (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_ch17_rate_vs_risk.png")


def fig_ch18_evalue_tipping() -> Path:
    """How strong residual confounding must be to explain away an RR (ch18)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    # Observed RR grid; E-value for RR>1: RR + sqrt(RR*(RR-1))
    rr = np.linspace(1.05, 4.0, 80)
    evalue = rr + np.sqrt(rr * (rr - 1.0))

    ax = axes[0]
    ax.plot(rr, evalue, color=TEAL, lw=2.4)
    ax.fill_between(rr, 1.0, evalue, color=TEAL, alpha=0.12)
    # annotate example RR=2.0
    rr_ex = 2.0
    ev_ex = rr_ex + np.sqrt(rr_ex * (rr_ex - 1.0))
    ax.plot([rr_ex], [ev_ex], "o", color=CORAL, markersize=9)
    ax.annotate(
        f"Observed RR = {rr_ex:.1f}\nE-value ≈ {ev_ex:.2f}",
        xy=(rr_ex, ev_ex),
        xytext=(2.6, 2.2),
        fontsize=8,
        color=CORAL,
        arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2),
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    ax.axhline(2.0, ls=":", color=SLATE, lw=1.0)
    ax.text(1.1, 2.08, "confounder RR≈2 on both arms", fontsize=7, color=SLATE)
    ax.set_xlabel("Observed risk ratio (RR)")
    ax.set_ylabel("E-value (min. confounder RR to nullify)")
    ax.set_xlim(1.0, 4.0)
    ax.set_ylim(1.0, 7.5)
    ax.set_title("E-value curve for nullifying RR→1", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("What the E-value does / does not do", fontsize=10, fontweight="bold", color=INDIGO)
    boxes = [
        (0.4, 6.6, GREEN, "#E8F5E9", "Does", "Quantifies how strong an\nunmeasured confounder must\nbe (on the risk-ratio scale)\nto fully explain away the\nobserved association."),
        (0.4, 1.0, CORAL, "#FFEBEE", "Does not", "Prove causation, fix selection\nbias, or replace a target-trial\nDAG. Weak RRs need only weak\nconfounding to evaporate."),
    ]
    for x, y, edge, face, title, body in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                9.2,
                3.6,
                boxstyle="round,pad=0.08,rounding_size=0.12",
                facecolor=face,
                edgecolor=edge,
                lw=1.6,
            )
        )
        ax.text(5.0, y + 2.9, title, ha="center", fontsize=11, fontweight="bold", color=edge)
        ax.text(5.0, y + 1.4, body, ha="center", va="center", fontsize=8.5, color=SLATE)
    fig.suptitle(
        "Residual confounding sensitivity: E-value intuition (synthetic teaching)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_ch18_evalue_tipping.png")


def fig_ch19_ci_compatibility() -> Path:
    """Four synthetic CIs classified against null and MCID (ch19)."""
    fig, ax = plt.subplots(figsize=(9.8, 5.2))

    # ARR % scale; null=0, MCID = +3 pp benefit
    trials = [
        ("A: Precise benefit", 6.0, 4.0, 8.0, GREEN),
        ("B: Imprecise but hopeful", 5.0, -1.0, 11.0, GOLD),
        ("C: Precise trivial", 0.4, 0.1, 0.7, SLATE),
        ("D: Compatible with harm", -1.5, -4.0, 1.0, CORAL),
    ]
    y = np.arange(len(trials))[::-1]
    mcid = 3.0

    for yi, (lab, pe, lo, hi, color) in zip(y, trials):
        ax.plot([lo, hi], [yi, yi], color=color, lw=3.0, solid_capstyle="round")
        ax.plot(pe, yi, "o", color=color, markersize=11, zorder=5)
        ax.text(-6.2, yi, lab, ha="right", va="center", fontsize=9, color=SLATE, fontweight="bold")
        # label classification
        if lo > mcid:
            tag = "CI entirely > MCID"
        elif lo > 0 and hi < mcid:
            tag = "sig but < MCID"
        elif lo < 0 < hi and hi > mcid:
            tag = "crosses null & MCID"
        elif hi < 0:
            tag = "favoring harm"
        elif lo < 0 < hi:
            tag = "crosses null"
        else:
            tag = "mixed"
        # refine tags per design
        tags = {
            "A: Precise benefit": "rules out null & MCID miss",
            "B: Imprecise but hopeful": "compatible with harm & big benefit",
            "C: Precise trivial": "sig, clinically tiny",
            "D: Compatible with harm": "compatible with harm & small benefit",
        }
        ax.text(12.2, yi, tags[lab], ha="left", va="center", fontsize=8, color=color)

    ax.axvline(0, color=SLATE, ls="--", lw=1.4, label="Null (ARR = 0)")
    ax.axvline(mcid, color=INDIGO, ls=":", lw=1.6, label=f"MCID = +{mcid:.0f} pp")
    ax.axvspan(mcid, 14, color=GREEN, alpha=0.06)
    ax.axvspan(-6, 0, color=CORAL, alpha=0.05)
    ax.set_xlim(-6.5, 14)
    ax.set_ylim(-0.6, 3.6)
    ax.set_yticks([])
    ax.set_xlabel("Absolute risk reduction (percentage points, synthetic)")
    ax.set_title(
        "Estimation culture: read the CI against null AND MCID",
        fontsize=12,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(loc="lower right", fontsize=8)
    ax.grid(True, axis="x", alpha=0.25)
    ax.text(
        4.0,
        -0.45,
        "p < 0.05 is neither necessary nor sufficient for a practice-changing claim.",
        ha="center",
        fontsize=8.5,
        color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    return _save(fig, "cycle2_ch19_ci_compatibility.png")


def fig_ch20_ph_violation() -> Path:
    """Crossing hazards: single HR is meaningless (ch20)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.7))

    t = np.linspace(0, 365, 200)
    # Synthetic survival: treatment has early peri-procedural hazard, late benefit
    # S_ctrl(t) = exp(-0.0012 t)
    # S_tx early worse then better
    s_ctrl = np.exp(-0.00115 * t)
    # piecewise hazard for treatment
    h_tx = np.where(t < 30, 0.0045, 0.00055)
    # integrate hazard numerically
    dt = t[1] - t[0]
    H = np.cumsum(h_tx) * dt
    s_tx = np.exp(-H)
    # renormalize start
    s_tx = s_tx / s_tx[0]

    ax = axes[0]
    ax.plot(t, s_ctrl * 100, color="#90A4AE", lw=2.3, label="Control")
    ax.plot(t, s_tx * 100, color=TEAL, lw=2.3, label="Treatment (early harm → late benefit)")
    ax.axvline(30, color=CORAL, ls="--", lw=1.2, alpha=0.8)
    ax.text(32, 92, "peri-procedural\nwindow", fontsize=7.5, color=CORAL)
    # mark crossing
    cross_idx = np.argmin(np.abs(s_tx - s_ctrl))
    ax.plot(t[cross_idx], s_tx[cross_idx] * 100, "o", color=GOLD, markersize=8, zorder=5)
    ax.annotate(
        "curves cross\n→ PH violated",
        xy=(t[cross_idx], s_tx[cross_idx] * 100),
        xytext=(180, 78),
        fontsize=8,
        color=CORAL,
        arrowprops=dict(arrowstyle="->", color=CORAL),
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    ax.set_xlabel("Days since index procedure")
    ax.set_ylabel("Event-free survival (%)")
    ax.set_xlim(0, 365)
    ax.set_ylim(55, 101)
    ax.set_title("Kaplan–Meier style curves (synthetic)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="lower left")
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("What a single HR hides", fontsize=10, fontweight="bold", color=INDIGO)
    items = [
        (8.0, "Time-averaged HR", "Blends early excess harm with late benefit into one uninterpretable number."),
        (5.5, "Appraisal demand", "Schoenfeld / log-log checks; split early vs late HRs; consider RMST."),
        (3.0, "Clinical parallel", "CEA/CAS and some device trials: peri-op stroke risk, then lower late stroke."),
        (0.5, "Reporting fix", "Plot absolute risks at day 30 and day 365; never quote one HR alone."),
    ]
    for y, title, body in items:
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y),
                9.4,
                2.1,
                boxstyle="round,pad=0.06,rounding_size=0.1",
                facecolor=LIGHT if title.startswith("A") or title.startswith("R") else WHITE,
                edgecolor=INDIGO,
                lw=1.0,
            )
        )
        ax.text(0.6, y + 1.4, title, fontsize=9, fontweight="bold", color=INDIGO, va="center")
        ax.text(0.6, y + 0.55, body, fontsize=8, color=SLATE, va="center")
    fig.suptitle(
        "Proportional-hazards violation: crossing survival curves (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_ch20_ph_violation.png")


def fig_ch22_lead_time_bias() -> Path:
    """Lead-time bias: earlier diagnosis lengthens 'survival' without delaying death (ch22)."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title(
        "Lead-time bias: longer survival-from-diagnosis without a later death date",
        fontsize=12,
        fontweight="bold",
        color=INDIGO,
        pad=10,
    )

    # Clinical detection pathway (top)
    y1 = 7.2
    ax.text(0.3, y1 + 1.4, "Usual care (clinical detection)", fontsize=10, fontweight="bold", color=SLATE)
    ax.annotate("", xy=(18.5, y1), xytext=(1.0, y1), arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.6))
    ax.text(9.5, y1 - 0.55, "calendar time →", ha="center", fontsize=8, color=SLATE)
    # clinical diagnosis at t=10, death at t=15 → survival 5y
    ax.plot(10, y1, "s", color=CORAL, markersize=12)
    ax.plot(15, y1, "X", color=CORAL, markersize=12, markeredgewidth=2)
    ax.plot([10, 15], [y1, y1], color=CORAL, lw=4, solid_capstyle="round")
    ax.text(10, y1 + 0.55, "Clinical Dx", ha="center", fontsize=8, color=CORAL)
    ax.text(15, y1 + 0.55, "Death", ha="center", fontsize=8, color=CORAL)
    ax.text(12.5, y1 - 0.9, "Survival from Dx = 5 years", ha="center", fontsize=9, color=CORAL, fontweight="bold")

    # Screening pathway (bottom)
    y2 = 3.0
    ax.text(0.3, y2 + 1.4, "Screened (earlier label only)", fontsize=10, fontweight="bold", color=SLATE)
    ax.annotate("", xy=(18.5, y2), xytext=(1.0, y2), arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.6))
    ax.plot(5, y2, "s", color=TEAL, markersize=12)
    ax.plot(15, y2, "X", color=CORAL, markersize=12, markeredgewidth=2)
    ax.plot([5, 15], [y2, y2], color=TEAL, lw=4, solid_capstyle="round")
    ax.text(5, y2 + 0.55, "Screen Dx", ha="center", fontsize=8, color=TEAL)
    ax.text(15, y2 + 0.55, "Death (same date)", ha="center", fontsize=8, color=CORAL)
    ax.text(10, y2 - 0.9, "Survival from Dx = 10 years  ← lead time = 5 years", ha="center", fontsize=9, color=TEAL, fontweight="bold")

    # lead time brace
    ax.annotate(
        "",
        xy=(10, 5.4),
        xytext=(5, 5.4),
        arrowprops=dict(arrowstyle="<->", color=GOLD, lw=2.0),
    )
    ax.text(7.5, 5.7, "Lead time\n(no life years gained)", ha="center", fontsize=8.5, color=GOLD, fontweight="bold")

    ax.add_patch(
        FancyBboxPatch(
            (0.4, 0.25),
            19.2,
            1.35,
            boxstyle="round,pad=0.06,rounding_size=0.1",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.4,
        )
    )
    ax.text(
        10.0,
        0.9,
        "Valid screen evaluation clocks outcomes from randomization — not from diagnosis date.\n"
        "If death dates do not move later, 'improved 5-year survival' is an artifact of earlier labeling.",
        ha="center",
        va="center",
        fontsize=8.5,
        color=SLATE,
    )
    return _save(fig, "cycle2_ch22_lead_time_bias.png")


def fig_ch24_benefit_harm_tradeoff() -> Path:
    """Absolute benefit vs absolute harm on same scale (ch24)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.8))

    # Two populations, same RR benefit and same absolute harm
    # Benefit RR 0.70; baseline 20% vs 2%; harm ARI fixed 1.5%
    labels = ["High-risk TIA\n(base 20%)", "Low-risk syndrome\n(base 2%)"]
    base = np.array([0.20, 0.02])
    arr = base * 0.30  # 30% RRR
    ari = np.array([0.015, 0.015])

    ax = axes[0]
    x = np.arange(2)
    w = 0.35
    b1 = ax.bar(x - w / 2, arr * 100, width=w, color=GREEN, edgecolor=INDIGO, label="ARR (ischemic events avoided)")
    b2 = ax.bar(x + w / 2, ari * 100, width=w, color=CORAL, edgecolor=INDIGO, label="ARI (major hemorrhage)")
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.set_ylabel("Absolute percentage points (90-day)")
    ax.set_ylim(0, 10)
    ax.set_title("Same relative benefit, same absolute harm", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    for rect, v in zip(b1, arr):
        ax.text(rect.get_x() + rect.get_width() / 2, v * 100 + 0.25, f"{v*100:.1f}", ha="center", fontsize=8)
    for rect, v in zip(b2, ari):
        ax.text(rect.get_x() + rect.get_width() / 2, v * 100 + 0.25, f"{v*100:.1f}", ha="center", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Net absolute tradeoff (synthetic)", fontsize=10, fontweight="bold", color=INDIGO)
    # table
    header = ["Population", "NNT", "NNH", "Net per 1000"]
    rows = [
        header,
        ["High-risk", f"{1/arr[0]:.0f}", f"{1/ari[0]:.0f}", f"+{(arr[0]-ari[0])*1000:.0f} events"],
        ["Low-risk", f"{1/arr[1]:.0f}", f"{1/ari[1]:.0f}", f"{(arr[1]-ari[1])*1000:+.0f} events"],
    ]
    ys = [8.0, 5.8, 3.6]
    for i, (y, row) in enumerate(zip(ys, rows)):
        for j, (text, x0) in enumerate(zip(row, [0.3, 2.8, 5.0, 7.0])):
            width = 2.3 if j else 2.4
            if j == 3:
                width = 2.7
            fc = "#E8EAF6" if i == 0 else ("#E8F5E9" if i == 1 else "#FFEBEE")
            ax.add_patch(
                FancyBboxPatch(
                    (x0, y - 0.7),
                    width,
                    1.5,
                    boxstyle="round,pad=0.03,rounding_size=0.08",
                    facecolor=fc,
                    edgecolor=INDIGO,
                    lw=0.9,
                )
            )
            ax.text(
                x0 + width / 2,
                y + 0.05,
                text,
                ha="center",
                va="center",
                fontsize=8 if i else 8.5,
                fontweight="bold" if i == 0 or j == 0 else "normal",
                color=INDIGO if i == 0 else SLATE,
            )
    ax.text(
        5.0,
        1.2,
        "Transporting DAPT/EVT effects to lower baseline risk\n"
        "can invert the benefit–harm ledger while the RR looks unchanged.",
        ha="center",
        fontsize=8.5,
        color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    fig.suptitle(
        "Therapy vs harm: absolute tradeoffs by baseline risk (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_ch24_benefit_harm_tradeoff.png")


def fig_ch27_fragility_ltfu() -> Path:
    """Fragility index vs lost-to-follow-up: when conclusions rest on missingness (ch27)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.8))

    trials = ["Trial P\n(robust)", "Trial Q\n(fragile)", "Trial R\n(brittle)"]
    fi = np.array([18, 4, 2])
    ltfu = np.array([6, 12, 15])

    ax = axes[0]
    x = np.arange(len(trials))
    w = 0.36
    ax.bar(x - w / 2, fi, width=w, color=TEAL, edgecolor=INDIGO, label="Fragility index")
    ax.bar(x + w / 2, ltfu, width=w, color=CORAL, edgecolor=INDIGO, label="Lost to follow-up (n)")
    ax.set_xticks(x)
    ax.set_xticklabels(trials)
    ax.set_ylabel("Patient count")
    ax.set_ylim(0, 24)
    ax.set_title("FI versus LTFU (synthetic dichotomous trials)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    for i, (f, l) in enumerate(zip(fi, ltfu)):
        if l > f:
            ax.text(i, max(f, l) + 0.8, "LTFU > FI", ha="center", fontsize=8, color=CORAL, fontweight="bold")
        else:
            ax.text(i, max(f, l) + 0.8, "FI > LTFU", ha="center", fontsize=8, color=GREEN, fontweight="bold")
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Fragility appraisal checklist", fontsize=10, fontweight="bold", color=INDIGO)
    checks = [
        "1. Compute FI for the primary dichotomous result.",
        "2. Count missing primary outcomes (not just deaths).",
        "3. If LTFU ≥ FI, the p-value is assumption-bound.",
        "4. Demand tipping-point / worst-case sensitivity.",
        "5. Do not rewrite pathways on FI ≤ 3 without replication.",
    ]
    for i, text in enumerate(checks):
        y = 8.2 - i * 1.55
        ax.add_patch(
            FancyBboxPatch(
                (0.4, y - 0.45),
                9.2,
                1.3,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor="#E0F2F1" if i % 2 == 0 else WHITE,
                edgecolor=TEAL,
                lw=1.0,
            )
        )
        ax.text(5.0, y + 0.2, text, ha="center", va="center", fontsize=8.5, color=SLATE)
    fig.suptitle(
        "Fragility index vs missing outcomes (synthetic teaching figure)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle2_ch27_fragility_ltfu.png")


def main() -> None:
    gens = [
        fig_ch17_rate_vs_risk,
        fig_ch18_evalue_tipping,
        fig_ch19_ci_compatibility,
        fig_ch20_ph_violation,
        fig_ch22_lead_time_bias,
        fig_ch24_benefit_harm_tradeoff,
        fig_ch27_fragility_ltfu,
    ]
    print(f"Generating {len(gens)} cycle-2 mid/late scientific figures → {OUT}")
    for g in gens:
        g()
    print("DONE")


if __name__ == "__main__":
    main()
