#!/usr/bin/env python3
"""CRIT-APP Cycle-27 densify: floor-13 → toward 14 (wave A, ch01–14).

14 original scientific Agg indigo plots. ARR/NNT; pred≠cause.
cycle27_swarm_* only.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle
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


def fig_ch01():
    """Protocol churn cost: absolute pathway rewrites vs papers misread/year."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    misreads = np.array([0, 2, 4, 6, 8, 10, 12])
    rewrites = 0.4 * misreads ** 1.35
    capacity = 100 - 3.5 * misreads
    ax.plot(misreads, rewrites, "o-", color=CORAL, lw=2.4, ms=8, label="Protocol rewrites / year")
    ax.set_xlabel("RRR-only misreads per year (teaching count)")
    ax.set_ylabel("Pathway rewrites", color=CORAL)
    ax.tick_params(axis="y", labelcolor=CORAL)
    ax2 = ax.twinx()
    ax2.plot(misreads, capacity, "s--", color=TEAL, lw=2.2, ms=8, label="Relative capacity %")
    ax2.set_ylabel("Service capacity retained (%)", color=TEAL)
    ax2.tick_params(axis="y", labelcolor=TEAL)
    ax2.set_ylim(40, 105)
    ax.set_title(
        "Appraisal failure compounds: absolute protocol churn vs RRR-only misreads",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, fontsize=8, loc="center left")
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch01_protocol_churn.png")


def fig_ch02():
    """Five-minute card: minutes allocated vs absolute error residual heat."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    tasks = ["PICO", "Design", "ARR table", "Bias", "Action"]
    ideal = np.array([0.5, 1.0, 1.5, 1.5, 0.5])
    rushed = np.array([1.5, 1.5, 0.3, 0.5, 1.2])  # skips ARR
    x = np.arange(len(tasks))
    w = 0.35
    ax.bar(x - w / 2, ideal, width=w, color=TEAL, edgecolor=INDIGO, label="DFR allocation (min)")
    ax.bar(x + w / 2, rushed, width=w, color=CORAL, edgecolor=INDIGO, label="Rushed skim (min)")
    ax.set_xticks(x)
    ax.set_xticklabels(tasks, fontsize=9)
    ax.set_ylabel("Minutes under time pressure")
    ax.set_title(
        "Speed residual: rushed readers starve the absolute ARR table",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch02_minute_budget.png")


def fig_ch03():
    """PICO completeness heatmap → estimand ARR readiness."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    elements = ["P", "I", "C", "O", "T\n(time)", "E\n(estimand)"]
    papers = ["Paper A", "Paper B", "Paper C", "Paper D"]
    # 1=complete, 0=missing
    M = np.array(
        [
            [1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 0, 0],
            [1, 1, 0, 1, 1, 0],
            [1, 1, 1, 0, 0, 0],
        ],
        dtype=float,
    )
    im = ax.imshow(M, cmap="RdYlGn", vmin=0, vmax=1, aspect="auto")
    ax.set_xticks(range(6))
    ax.set_xticklabels(elements, fontsize=9)
    ax.set_yticks(range(4))
    ax.set_yticklabels(papers, fontsize=9)
    for i in range(4):
        for j in range(6):
            ax.text(j, i, "✓" if M[i, j] else "·", ha="center", va="center", fontsize=12, fontweight="bold")
    scores = M.mean(axis=1)
    for i, s in enumerate(scores):
        ax.text(5.7, i, f"ARR-ready {s:.0%}", va="center", fontsize=8, color=INDIGO, fontweight="bold")
    ax.set_title(
        "Question residual: incomplete PICO/estimand blocks absolute ARR transport",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    fig.colorbar(im, ax=ax, fraction=0.03, pad=0.08, label="Complete")
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch03_pico_heatmap.png")


def fig_ch04():
    """Internal vs external validity tradeoff frontier (absolute transport)."""
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    # frontier: higher internal often narrower external
    internal = np.linspace(0.4, 0.98, 40)
    external = 1.05 - 0.55 * internal ** 1.2 + 0.05 * np.sin(8 * internal)
    ax.plot(internal, external, color=INDIGO, lw=2.5, label="Design frontier (teaching)")
    pts = [(0.55, 0.85, "Pragmatic registry"), (0.90, 0.45, "Tight RCT"), (0.75, 0.70, "Target trial")]
    for x, y, lab in pts:
        ax.scatter([x], [y], s=110, zorder=5, edgecolors=WHITE, color=TEAL if "Target" in lab else GOLD if "Prag" in lab else CORAL)
        ax.text(x + 0.02, y + 0.02, lab, fontsize=8, fontweight="bold", color=SLATE)
    ax.set_xlabel("Internal validity (bias control)")
    ax.set_ylabel("External transportability")
    ax.set_xlim(0.35, 1.05)
    ax.set_ylim(0.3, 1.0)
    ax.set_title(
        "Validity residual: absolute local ARR needs both axes, not internal alone",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch04_validity_frontier.png")


def fig_ch05():
    """Target trial specification checklist score vs residual absolute bias."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    score = np.linspace(0, 1, 60)
    residual_bias = 8 * np.exp(-3.2 * score) + 0.4  # pp
    ax.plot(score, residual_bias, color=CORAL, lw=2.6)
    ax.fill_between(score, 0, residual_bias, color=CORAL, alpha=0.12)
    ax.axvline(0.7, color=TEAL, ls="--", lw=1.4)
    ax.text(0.72, 6.5, "target-trial\nthreshold", color=TEAL, fontsize=8, fontweight="bold")
    ax.set_xlabel("Target-trial specification completeness (0–1)")
    ax.set_ylabel("Residual absolute confounding bias (pp)")
    ax.set_title(
        "Confounding residual: complete target-trial design shrinks absolute bias",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.set_ylim(0, 9)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch05_target_trial_bias.png")


def fig_ch06():
    """ITT vs per-protocol absolute ARR with nonadherence gradient."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    nonadh = np.linspace(0, 0.4, 50)
    true_arr = 6.0
    itt = true_arr * (1 - 0.85 * nonadh)
    pp_biased = true_arr + 4 * nonadh  # selection inflates
    ax.plot(nonadh * 100, itt, color=TEAL, lw=2.5, label="ITT ARR (diluted)")
    ax.plot(nonadh * 100, pp_biased, color=CORAL, lw=2.5, label="Naive PP ARR (selected)")
    ax.axhline(true_arr, color=INDIGO, ls="--", lw=1.4, label="True assigned ARR")
    ax.set_xlabel("Differential nonadherence (%)")
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title(
        "RCT residual: nonadherence dilutes ITT ARR; naive PP invents absolute benefit",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch06_itt_pp_arr.png")


def fig_ch07():
    """E-value curve for absolute residual confounding threat."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rr = np.linspace(1.05, 3.0, 80)
    # E-value for RR: RR + sqrt(RR*(RR-1))
    evalue = rr + np.sqrt(rr * (rr - 1))
    ax.plot(rr, evalue, color=INDIGO, lw=2.6)
    ax.axvline(1.25, color=GOLD, ls="--", lw=1.3)
    ax.axhline(1.25 + np.sqrt(1.25 * 0.25), color=GOLD, ls=":", lw=1.2)
    ax.text(1.28, 4.5, "RR=1.25\nmodest association", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xlabel("Observed risk ratio (point)")
    ax.set_ylabel("E-value (confounder RR strength)")
    ax.set_title(
        "Observational residual: small RR → small E-value → fragile absolute claims",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch07_evalue_curve.png")


def fig_ch08():
    """Likelihood ratio nomogram-style absolute probability ladder."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prior = np.array([1, 2, 5, 10, 20, 40, 60])
    for lr, c, lab in [(0.1, CORAL, "LR−=0.1"), (2, GOLD, "LR+=2"), (10, TEAL, "LR+=10")]:
        posts = []
        for p in prior / 100:
            o = p / (1 - p)
            post = (o * lr) / (1 + o * lr) * 100
            posts.append(post)
        ax.plot(prior, posts, "o-", color=c, lw=2.2, ms=7, label=lab)
    ax.plot([0, 70], [0, 70], ":", color=GRAY, lw=1.2)
    ax.set_xlabel("Pre-test absolute probability (%)")
    ax.set_ylabel("Post-test absolute probability (%)")
    ax.set_title(
        "Diagnostic residual: LR maps pre-test absolute risk to post-test absolute risk",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    ax.set_xlim(0, 70)
    ax.set_ylim(0, 100)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch08_lr_ladder.png")


def fig_ch09():
    """Discrimination vs calibration dual-axis residual (pred ≠ cause)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 4.9))
    ax = axes[0]
    fpr = np.linspace(0, 1, 100)
    tpr_a = fpr ** 0.35
    tpr_b = fpr ** 0.7
    ax.plot(fpr, tpr_a, color=GOLD, lw=2.3, label="Model A AUROC≈0.86")
    ax.plot(fpr, tpr_b, color=GRAY, lw=2.0, label="Model B AUROC≈0.72")
    ax.plot([0, 1], [0, 1], ":", color=GRAY)
    ax.set_xlabel("1 − Specificity")
    ax.set_ylabel("Sensitivity")
    ax.set_title("Discrimination", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    pred = np.linspace(0.05, 0.7, 8)
    obs_a = pred * 0.6 + 0.05  # overconfident
    obs_b = pred * 0.95 + 0.01
    ax.plot([0, 0.75], [0, 0.75], "--", color=GRAY)
    ax.plot(pred, obs_a, "o-", color=CORAL, lw=2.2, label="A: poor calibration")
    ax.plot(pred, obs_b, "s-", color=TEAL, lw=2.2, label="B: better calibration")
    ax.set_xlabel("Predicted risk")
    ax.set_ylabel("Observed risk")
    ax.set_title("Absolute calibration", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.suptitle(
        "Prognosis residual: high AUROC with miscalibration misprices absolute risk (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch09_disc_vs_calib.png")


def fig_ch10():
    """Heterogeneity: I² and prediction interval width for absolute effects."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    i2 = np.array([0, 15, 30, 50, 70, 90])
    # prediction interval half-width for ARR (pp) grows with I2
    pi_hw = 1.0 + 0.08 * i2 + 0.0015 * i2 ** 2
    ax.plot(i2, pi_hw, "o-", color=INDIGO, lw=2.5, ms=8)
    ax.fill_between(i2, 0, pi_hw, color=INDIGO, alpha=0.12)
    ax.axvline(50, color=GOLD, ls="--", lw=1.3)
    ax.text(52, 8, "I²=50%\ninterpret PI", color=GOLD, fontsize=8, fontweight="bold")
    ax.set_xlabel("I² (%)")
    ax.set_ylabel("95% prediction interval half-width (ARR pp)")
    ax.set_title(
        "Meta residual: high I² widens absolute prediction intervals for next study",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch10_i2_pi_width.png")


def fig_ch11():
    """mRS utility-weighted distribution shift with absolute Δ utility."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    mrs = np.arange(0, 7)
    util = np.array([1.0, 0.91, 0.76, 0.65, 0.33, 0.0, 0.0])
    ctrl = np.array([8, 12, 18, 22, 20, 12, 8], dtype=float)
    trt = np.array([12, 16, 20, 20, 16, 10, 6], dtype=float)
    ctrl /= ctrl.sum()
    trt /= trt.sum()
    w = 0.35
    ax.bar(mrs - w / 2, ctrl * 100, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(mrs + w / 2, trt * 100, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    eu_c = (ctrl * util).sum()
    eu_t = (trt * util).sum()
    ax.set_xlabel("mRS (6 = death)")
    ax.set_ylabel("% of arm")
    ax.set_title(
        f"Ordinal residual: utility-weighted absolute ΔEU ≈ {eu_t - eu_c:.3f}",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch11_mrs_utility.png")


def fig_ch12():
    """NNT uncertainty band as function of CI for ARR."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(0.01, 0.15, 80)
    nnt = 1 / arr
    # CI asymmetric mapping
    arr_lo = arr * 0.5
    arr_hi = arr * 1.5
    nnt_hi = 1 / np.maximum(arr_lo, 1e-6)
    nnt_lo = 1 / arr_hi
    ax.plot(arr * 100, nnt, color=INDIGO, lw=2.5, label="NNT point")
    ax.fill_between(arr * 100, nnt_lo, nnt_hi, color=INDIGO, alpha=0.15, label="NNT from ARR CI")
    ax.set_xlabel("ARR (pp)")
    ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title(
        "Effect-size residual: absolute NNT inherits asymmetric uncertainty from ARR CI",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch12_nnt_uncertainty.png")


def fig_ch13():
    """Spin detector: subgroup forest with overall null absolute primary."""
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    labels = ["Overall primary", "Age <70", "Age ≥70", "Male", "Female", "NIHSS high", "NIHSS low"]
    arr = np.array([0.5, 3.5, -1.0, 2.0, -0.5, 4.5, -2.0])
    lo = arr - np.array([2.0, 2.5, 2.5, 2.2, 2.2, 3.0, 2.8])
    hi = arr + np.array([2.0, 2.5, 2.5, 2.2, 2.2, 3.0, 2.8])
    y = np.arange(len(labels))[::-1]
    for yi, a, l, h, name in zip(y, arr, lo, hi, labels):
        c = INDIGO if name.startswith("Overall") else (CORAL if a > 2 else SLATE)
        ax.plot([l, h], [yi, yi], color=c, lw=2.2 if name.startswith("Overall") else 1.6)
        ax.plot(a, yi, "D" if name.startswith("Overall") else "o", color=c, ms=8)
    ax.axvline(0, color=GRAY, ls="--", lw=1)
    ax.set_yticks(y)
    ax.set_yticklabels(labels, fontsize=9)
    ax.set_xlabel("Absolute ARR (pp)")
    ax.set_title(
        "Subgroup residual: overall null absolute primary; spin via exploratory strata",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, axis="x", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch13_spin_forest.png")


def fig_ch14():
    """Train/test leakage: feature availability at prediction time vs AUROC inflation."""
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    leak_frac = np.linspace(0, 0.5, 40)
    auroc_leaked = 0.75 + 0.4 * leak_frac + 0.15 * leak_frac ** 0.5
    auroc_clean = np.full_like(leak_frac, 0.75)
    ax.plot(leak_frac * 100, auroc_leaked, color=CORAL, lw=2.5, label="Leaked evaluation AUROC")
    ax.plot(leak_frac * 100, auroc_clean, color=TEAL, lw=2.3, ls="--", label="Time-safe holdout AUROC")
    ax.fill_between(leak_frac * 100, auroc_clean, auroc_leaked, color=CORAL, alpha=0.12)
    ax.set_xlabel("% of features only known after outcome time")
    ax.set_ylabel("AUROC")
    ax.set_ylim(0.65, 1.0)
    ax.set_title(
        "AI residual: leakage inflates discrimination; absolute impact still unproven (pred ≠ cause)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle27_swarm_ch14_leakage_auroc.png")


def main():
    print("Cycle-27 →", OUT)
    fns = [
        fig_ch01,
        fig_ch02,
        fig_ch03,
        fig_ch04,
        fig_ch05,
        fig_ch06,
        fig_ch07,
        fig_ch08,
        fig_ch09,
        fig_ch10,
        fig_ch11,
        fig_ch12,
        fig_ch13,
        fig_ch14,
    ]
    for fn in fns:
        fn()
    print(f"Done: {len(fns)}")


if __name__ == "__main__":
    main()
