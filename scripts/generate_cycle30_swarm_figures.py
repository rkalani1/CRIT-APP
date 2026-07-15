#!/usr/bin/env python3
"""CRIT-APP Cycle-30 densify: clear residual floor-14 → uniform floor ≥15.

14 original scientific Agg indigo plots for ch15–ch28.
ARR/NNT; pred≠cause. cycle30_swarm_* only.
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
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = (
    "#283593",
    "#00695C",
    "#F9A825",
    "#C62828",
    "#37474F",
    "#FFFFFF",
)
GREEN, BLUE, ORANGE, PURPLE, GRAY = (
    "#2E7D32",
    "#1565C0",
    "#EF6C00",
    "#6A1B9A",
    "#90A4AE",
)


def _save(fig, name: str):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    roles = ["Presenter", "Method\nskeptic", "Absolute\ncalc", "Clinician\nuser", "Chair"]
    weights = [0.15, 0.20, 0.25, 0.25, 0.15]
    ax.pie(
        weights,
        labels=roles,
        colors=[GRAY, GOLD, TEAL, INDIGO, CORAL],
        autopct="%1.0f%%",
        startangle=90,
        textprops={"fontsize": 8},
    )
    ax.set_title(
        "JC architecture residual: dedicate ≥25% time to absolute ARR/NNT calculation",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch15_role_time.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    papers = np.arange(1, 9)
    validity = np.array([0.9, 0.8, 0.7, 0.55, 0.4, 0.35, 0.25, 0.2])
    abs_mag = np.array([0.8, 0.3, 0.7, 0.6, 0.5, 0.2, 0.4, 0.15])
    action = validity * abs_mag
    ax.plot(papers, validity, "o-", color=TEAL, lw=2.2, label="Validity")
    ax.plot(papers, abs_mag, "s-", color=GOLD, lw=2.2, label="Absolute magnitude")
    ax.plot(papers, action, "^-", color=INDIGO, lw=2.4, label="Action score = V×A")
    ax.axhline(0.35, color=CORAL, ls="--", lw=1.2)
    ax.set_xlabel("Autopsy paper index")
    ax.set_ylabel("Score (0–1)")
    ax.set_title(
        "Autopsy residual: action requires both validity and absolute magnitude",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch16_action_score.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # person-time diagram as rates
    years = np.array([1, 2, 3, 4, 5])
    events = np.array([20, 18, 15, 12, 10])
    py = np.array([1000, 950, 900, 820, 700])
    rate = events / py * 100
    ax.bar(years, rate, color=TEAL, edgecolor=INDIGO, width=0.6)
    ax.plot(years, rate, "o-", color=INDIGO, lw=1.5)
    ax.set_xlabel("Follow-up year")
    ax.set_ylabel("Incidence rate (/100 py)")
    ax.set_title(
        "Frequency residual: incidence rate uses person-time — not crude counts alone",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch17_person_time.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # Hill viewpoints as weights vs absolute causal claim strength
    hills = ["Strength", "Consistency", "Specificity", "Temporality", "Gradient", "Plausibility", "Experiment"]
    weights = [0.7, 0.6, 0.3, 1.0, 0.5, 0.4, 0.9]
    abs_support = [0.5, 0.55, 0.2, 0.9, 0.45, 0.25, 0.95]
    x = np.arange(len(hills))
    ax.bar(x - 0.2, weights, width=0.4, color=GOLD, edgecolor=INDIGO, label="Viewpoint weight")
    ax.bar(x + 0.2, abs_support, width=0.4, color=TEAL, edgecolor=INDIGO, label="Absolute causal support")
    ax.set_xticks(x)
    ax.set_xticklabels(hills, fontsize=8, rotation=15)
    ax.set_ylim(0, 1.15)
    ax.set_title(
        "Causation residual: viewpoints are not a checklist substitute for absolute design strength",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch18_hill_weights.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # power curve for detecting ARR=3pp
    n = np.linspace(50, 2500, 80)
    # approximate power for RD
    from math import erf

    arr, p0 = 0.03, 0.15
    p1 = p0 - arr
    se = np.sqrt(p0 * (1 - p0) / (n / 2) + p1 * (1 - p1) / (n / 2))
    z = arr / se
    # power ≈ 1 - Φ(1.96 - z) two-sided approx (vectorized)
    power = 1 - 0.5 * (1 + np.vectorize(erf)((1.96 - z) / np.sqrt(2)))
    power = np.clip(power, 0, 1)
    ax.plot(n, power * 100, color=INDIGO, lw=2.5)
    ax.axhline(80, color=GOLD, ls="--", lw=1.3)
    ax.set_xlabel("Total sample size n")
    ax.set_ylabel("Power (%) to detect ARR=3 pp")
    ax.set_title(
        "Inference residual: power is about absolute ARR, not relative headlines",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch19_power_arr.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # PH violation: HR time-varying vs absolute RMST difference stable teaching
    t = np.linspace(1, 36, 60)
    hr_t = 0.9 - 0.25 * np.sin(t / 8)  # varies
    rmst_diff = 1.2 + 0.02 * t  # months gained absolute-ish teaching units
    ax.plot(t, hr_t, color=CORAL, lw=2.3, label="Time-varying HR")
    ax.axhline(0.75, color=GOLD, ls=":", lw=1.2, label="Assumed constant HR")
    ax2 = ax.twinx()
    ax2.plot(t, rmst_diff, color=TEAL, lw=2.4, label="ΔRMST (absolute months)")
    ax.set_xlabel("Months")
    ax.set_ylabel("Hazard ratio", color=CORAL)
    ax2.set_ylabel("Absolute ΔRMST", color=TEAL)
    ax.tick_params(axis="y", labelcolor=CORAL)
    ax2.tick_params(axis="y", labelcolor=TEAL)
    ax.set_title(
        "Survival residual: when PH fails, prefer absolute RMST differences",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    lines, labels = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines + lines2, labels + labels2, fontsize=8, loc="center right")
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch20_rmst.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # effect modification continuous: ARR by biomarker
    x = np.linspace(0, 10, 80)
    arr = 1 + 0.8 * x + 0.05 * x ** 2 / 2
    ax.plot(x, arr, color=TEAL, lw=2.5)
    ax.axhline(arr.mean(), color=GOLD, ls="--", lw=1.3, label="Marginal mean ARR")
    ax.set_xlabel("Biomarker level (teaching units)")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title(
        "Interaction residual: effect modification is an absolute ARR curve, not only a p-value",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch21_emod_curve.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # length-time: slow tumors over-represented
    growth = np.array([1, 2, 3, 4, 5, 6])  # slow to fast
    detect = np.array([35, 25, 18, 12, 7, 3])
    lethal = np.array([5, 10, 18, 28, 40, 55])
    ax.bar(growth - 0.15, detect, width=0.3, color=GOLD, edgecolor=INDIGO, label="% of screen detections")
    ax.bar(growth + 0.15, lethal / 2, width=0.3, color=CORAL, edgecolor=INDIGO, label="Relative lethality (scaled)")
    ax.set_xlabel("Tumor growth rate bin (slow → fast)")
    ax.set_ylabel("Teaching units")
    ax.set_title(
        "Screening residual: length-time bias over-samples slow indolent disease",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch22_length_time.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # anchoring: first number vs absolute posterior
    anchors = np.array([5, 15, 30, 50, 70])
    true_post = np.full_like(anchors, 22, dtype=float)
    anchored = 0.55 * anchors + 0.45 * 22
    ax.plot(anchors, anchored, "o-", color=CORAL, lw=2.4, label="Anchored absolute estimate")
    ax.axhline(22, color=TEAL, ls="--", lw=2, label="True absolute posterior 22%")
    ax.set_xlabel("Irrelevant anchor (%)")
    ax.set_ylabel("Stated absolute probability (%)")
    ax.set_title(
        "Reasoning residual: anchoring drags absolute probability estimates",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch23_anchoring.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # number needed to treat continuum with CI
    arr = np.array([8, 5, 3, 2, 1.2])
    lo = arr * 0.55
    hi = arr * 1.6
    nnt = 100 / arr
    nnt_lo = 100 / hi
    nnt_hi = 100 / lo
    y = np.arange(len(arr))
    ax.hlines(y, nnt_lo, nnt_hi, color=INDIGO, lw=2.5)
    ax.plot(nnt, y, "o", color=TEAL, ms=10)
    ax.set_yticks(y)
    ax.set_yticklabels([f"ARR {a} pp" for a in arr], fontsize=9)
    ax.set_xlabel("NNT (with CI mapped from ARR CI)")
    ax.set_title(
        "Therapy residual: communicate absolute NNT with uncertainty, not a lonely integer",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch24_nnt_ci.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # spectrum bias: Se/Sp shift absolute
    settings = ["Screening", "Primary\ncare", "Stroke\nunit", "ICU"]
    se = [0.70, 0.78, 0.88, 0.92]
    sp = [0.95, 0.90, 0.82, 0.70]
    x = np.arange(4)
    ax.plot(x, se, "o-", color=INDIGO, lw=2.3, label="Sensitivity")
    ax.plot(x, sp, "s-", color=TEAL, lw=2.3, label="Specificity")
    ax.set_xticks(x)
    ax.set_xticklabels(settings, fontsize=9)
    ax.set_ylim(0.6, 1.0)
    ax.set_ylabel("Se / Sp")
    ax.set_title(
        "Dx residual: spectrum shifts absolute accuracy — transport Se/Sp carefully",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch25_spectrum.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # GRADE certainty vs absolute effect size teaching
    certainty = ["High", "Moderate", "Low", "Very low"]
    arr = [4.0, 3.5, 3.0, 2.5]
    # widen CI as certainty falls
    err = [0.5, 1.2, 2.5, 4.0]
    x = np.arange(4)
    ax.errorbar(x, arr, yerr=err, fmt="o", color=INDIGO, lw=2.2, ms=10, capsize=5)
    ax.set_xticks(x)
    ax.set_xticklabels(certainty, fontsize=9)
    ax.set_ylabel("Absolute ARR (pp) with CI half-width")
    ax.set_title(
        "Evidence synthesis residual: lower certainty widens absolute effect intervals",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch26_grade_abs.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # multiplicity: FWER vs absolute false discoveries of ARR claims
    tests = np.array([1, 5, 10, 20, 50])
    fwer = 1 - (1 - 0.05) ** tests
    ax.plot(tests, fwer * 100, "o-", color=CORAL, lw=2.5, ms=8)
    ax.axhline(5, color=TEAL, ls="--", lw=1.3, label="Nominal 5%")
    ax.set_xlabel("Number of absolute ARR subgroup tests")
    ax.set_ylabel("Family-wise error rate (%)")
    ax.set_title(
        "Multiplicity residual: more absolute claims without control inflates false ARR wins",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch27_fwer.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.6, 5.0))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.axis("off")
    ax.set_title(
        "Policy residual: absolute risk communication ladder for patients & systems",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    steps = [
        (4.6, TEAL, "1. Baseline risk in natural frequencies"),
        (3.3, INDIGO, "2. Risk with intervention (same denominator)"),
        (2.0, GOLD, "3. ARR and NNT/NNH same horizon"),
        (0.7, CORAL, "4. Uncertainty + values; no RRR-only consent"),
    ]
    for y, c, t in steps:
        ax.add_patch(
            FancyBboxPatch(
                (0.5, y - 0.45),
                9.0,
                1.1,
                boxstyle="round,pad=0.03,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=c,
                lw=1.6,
            )
        )
        ax.text(5, y + 0.1, t, ha="center", va="center", fontsize=10, fontweight="bold", color=c)
    fig.tight_layout()
    return _save(fig, "cycle30_swarm_ch28_comm_ladder.png")


def main():
    print("Cycle-30 →", OUT)
    for fn in [
        fig_ch15,
        fig_ch16,
        fig_ch17,
        fig_ch18,
        fig_ch19,
        fig_ch20,
        fig_ch21,
        fig_ch22,
        fig_ch23,
        fig_ch24,
        fig_ch25,
        fig_ch26,
        fig_ch27,
        fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
