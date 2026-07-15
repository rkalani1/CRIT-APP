#!/usr/bin/env python3
"""
CRIT-APP Cycle-11 densify: original matplotlib Agg indigo teaching figures.

Targets residual floor-8 chapters:
  ch01 cost of misreading absolute board
  ch05 DAG backdoor residual absolute
  ch07 ACNU absolute confounding control
  ch09 overfitting optimism absolute calibration gap
  ch15 epistemic board absolute columns
  ch22 NNS absolute overdiagnosis
  ch25 dual-pathway absolute decision thresholds

Safe to re-run (overwrites cycle11_swarm_* only).
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

INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p

def fig_ch01():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    labels = ["Misread\nrelative", "Correct\nabsolute"]
    waste = [180, 40]  # bed-days or patients overtreated synthetic
    ax.bar([0, 1], waste, color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labels, fontsize=9)
    ax.set_ylabel("Patients treated without net benefit / year (synthetic)")
    ax.set_title("Cost of skipping absolute appraisal", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(waste):
        ax.text(i, v + 4, str(v), ha="center", fontsize=11, fontweight="bold", color=SLATE)
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Misreading cost categories", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [
        (7.5, CORAL, "Clinical", "Overtreat low-ARR strata; undertreat high-ARR"),
        (5.2, ORANGE, "Operational", "Pathway capacity spent on relative spin"),
        (2.9, GOLD, "Scientific", "Confounded associations become 'evidence'"),
        (0.6, TEAL, "Fix", "DFR absolute board before any rewrite"),
    ]:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.7), 9.2, 1.7, boxstyle="round,pad=0.04,rounding_size=0.08", facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.7, y + 0.35, t, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y - 0.3, b, fontsize=8.3, color=SLATE)
    fig.suptitle("Why appraisal matters: absolute cost of relative misreading (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch01_misread_cost.png")

def fig_ch05():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Backdoor path invents absolute association", fontsize=10, fontweight="bold", color=INDIGO)
    # simple nodes
    for (x, y, lab, col) in [(2, 7.5, "Severity U", CORAL), (5, 5, "Treatment A", INDIGO), (8, 7.5, "Outcome Y", TEAL)]:
        ax.add_patch(FancyBboxPatch((x - 1.2, y - 0.7), 2.4, 1.4, boxstyle="round,pad=0.04,rounding_size=0.08", facecolor=WHITE, edgecolor=col, lw=1.5))
        ax.text(x, y, lab, ha="center", va="center", fontsize=9, fontweight="bold", color=col)
    ax.annotate("", xy=(4, 5.5), xytext=(2.5, 7), arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=2))
    ax.annotate("", xy=(7.5, 7), xytext=(6, 5.5), arrowprops=dict(arrowstyle="-|>", color=INDIGO, lw=2))
    ax.annotate("", xy=(7.2, 7.5), xytext=(3.2, 7.5), arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=2, ls="--"))
    ax.text(5, 8.5, "open backdoor U→A and U→Y", ha="center", fontsize=8.5, color=CORAL, fontweight="bold")
    ax.text(5, 2.5, "Adjust/close backdoor before any ARR claim", ha="center", fontsize=9, color=PURPLE, style="italic")
    ax = axes[1]
    labs = ["Crude ARR", "After closing\nbackdoor", "If residual\npath open"]
    vals = [10, 3, 10]
    ax.bar(range(3), vals, color=[CORAL, TEAL, GOLD], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("ARR (pp)"); ax.set_title("DAG discipline changes absolute effect", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Confounding & DAGs: backdoors move absolute effects (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch05_backdoor_arr.png")

def fig_ch07():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    labs = ["Prevalent\nuser bias", "New-user\nactive comp"]
    arr = [8.5, 2.5]
    ax.bar([0, 1], arr, color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Apparent ARR (pp)"); ax.set_title("ACNU design shrinks confounded absolute", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    for i, v in enumerate(arr):
        ax.text(i, v + 0.25, f"{v} pp", ha="center", fontsize=10, fontweight="bold", color=SLATE)
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Observational absolute checklist", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [
        (7.4, INDIGO, "New-user", "Start follow-up at initiation t0"),
        (5.2, GOLD, "Active comparator", "Similar indication, different drug"),
        (3.0, TEAL, "Absolute rebuild", "Event rates both arms → ARR CI"),
        (0.8, CORAL, "Refuse NNT", "If design residual can invent ARR"),
    ]:
        ax.add_patch(FancyBboxPatch((0.35, y - 0.75), 9.3, 1.85, boxstyle="round,pad=0.04,rounding_size=0.08", facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.65, y + 0.4, t, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.65, y - 0.3, b, fontsize=8.3, color=SLATE)
    fig.suptitle("Observational appraisal: ACNU absolute honesty (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch07_acnu_arr.png")

def fig_ch09():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    stages = ["Apparent\nAUROC", "Optimism\ncorrected", "External\nAUROC"]
    vals = [0.92, 0.81, 0.74]
    ax.bar(range(3), vals, color=[GOLD, ORANGE, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(stages, fontsize=9)
    ax.set_ylabel("Discrimination"); ax.set_ylim(0.5, 1.0)
    ax.set_title("Overfitting optimism gap", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax = axes[1]
    pred = np.linspace(0.1, 0.7, 7)
    ax.plot([0, 0.8], [0, 0.8], "--", color=GRAY, lw=1.2)
    ax.plot(pred, pred * 0.6 + 0.05, "s-", color=CORAL, lw=2, label="Overfit derivation")
    ax.plot(pred, pred * 0.95, "o-", color=TEAL, lw=2, label="External (better)")
    ax.set_xlabel("Predicted risk"); ax.set_ylabel("Observed risk")
    ax.set_title("Absolute calibration fails first", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3)
    fig.suptitle("Prognosis models: optimism vs absolute calibration (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch09_optimism_cal.png")

def fig_ch15():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Epistemic board columns (absolute first)", fontsize=10, fontweight="bold", color=INDIGO)
    cols = [("Question", INDIGO), ("Estimand", BLUE), ("ARR/NNT", GOLD), ("Threats", CORAL), ("Action", TEAL)]
    for i, (lab, col) in enumerate(cols):
        x = 0.4 + i * 1.9
        ax.add_patch(FancyBboxPatch((x, 3), 1.75, 5.5, boxstyle="round,pad=0.03,rounding_size=0.08", facecolor=WHITE, edgecolor=col, lw=1.6))
        ax.text(x + 0.88, 7.8, lab, ha="center", fontsize=8.5, fontweight="bold", color=col, rotation=0)
        ax.text(x + 0.88, 5.5, "•", ha="center", fontsize=14, color=col)
    ax = axes[1]
    labs = ["Board without\nARR column", "Board with\nARR column"]
    done = [40, 95]
    ax.bar([0, 1], done, color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0, 1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("% complete absolute ledger (synthetic)"); ax.set_ylim(0, 100)
    ax.set_title("Visible columns enforce method", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Journal club: epistemic board absolute columns (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch15_epistemic_board.png")

def fig_ch22():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    labs = ["True lives\nextended", "Overdiagnosed\ntreated", "False +\nworkups"]
    n = [2, 25, 60]
    ax.bar(range(3), n, color=[TEAL, CORAL, ORANGE], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Per 1,000 screened (synthetic)")
    ax.set_title("Absolute screening ledger (NNS context)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax = axes[1]
    ax.set_xlim(0, 10); ax.set_ylim(0, 10); ax.axis("off")
    ax.set_title("Appraisal rule for screens", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [
        (7.2, TEAL, "Invitation RCT", "Mortality/disability from randomize-to-screen"),
        (4.6, GOLD, "Natural frequencies", "Benefit vs overdiagnosis per 1000"),
        (2.0, CORAL, "Refuse survival-from-dx", "Lead time is not life years"),
    ]:
        ax.add_patch(FancyBboxPatch((0.4, y - 0.9), 9.2, 2.2, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor=WHITE, edgecolor=edge, lw=1.5))
        ax.text(5, y + 0.5, t, ha="center", fontsize=10, fontweight="bold", color=edge)
        ax.text(5, y - 0.4, b, ha="center", fontsize=8.5, color=SLATE)
    fig.suptitle("Screening: absolute NNS/overdiagnosis before expansion (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch22_nns_overdx.png")

def fig_ch25():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.15))
    ax = axes[0]
    # diagnosis thresholds
    p = np.linspace(0, 100, 50)
    ax.axhline(10, color=TEAL, ls="--", lw=1.5); ax.text(80, 12, "test thr", color=TEAL, fontsize=8)
    ax.axhline(50, color=CORAL, ls="--", lw=1.5); ax.text(80, 52, "treat thr", color=CORAL, fontsize=8)
    ax.plot([0, 100], [5, 5], color=GRAY, lw=2, label="pre-test 5%")
    ax.plot([0, 40, 100], [5, 55, 55], color=INDIGO, lw=2.5, label="after LR+ path")
    ax.set_xlabel("Evidence accumulation (schematic)"); ax.set_ylabel("Probability (%)")
    ax.set_title("Diagnosis: absolute thresholds for action", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 100); ax.grid(True, alpha=0.3)
    ax = axes[1]
    labs = ["Risk 5%\n@90d", "Risk 15%\n@90d", "Both same\npathway?"]
    # if same pathway, score useless operationally
    change = [0, 0, 0]
    ax.bar(range(2), [5, 15], color=[TEAL, GOLD], edgecolor=INDIGO, width=0.55)
    ax.set_xticks(range(2)); ax.set_xticklabels(labs[:2], fontsize=9)
    ax.set_ylabel("Absolute risk %"); ax.set_title("Prognosis: strata must change actions", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(0.5, 16.5, "If both → same ICU pathway, score is counseling-only", ha="center", fontsize=8, color=PURPLE, style="italic")
    fig.suptitle("Diagnosis & prognosis: absolute thresholds and actionable strata (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle11_swarm_ch25_action_thresholds.png")

def main():
    print("Cycle-11 →", OUT)
    for fn in [fig_ch01, fig_ch05, fig_ch07, fig_ch09, fig_ch15, fig_ch22, fig_ch25]:
        fn()
    print("Done: 7")

if __name__ == "__main__":
    main()
