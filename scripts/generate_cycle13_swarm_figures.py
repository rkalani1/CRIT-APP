#!/usr/bin/env python3
"""CRIT-APP Cycle-13 densify: raise floor from 9 toward 10.

ch11 ordinal mRS absolute shift residual
ch13 industry spin absolute
ch18 counterfactual absolute
ch20 table-2 fallacy absolute
ch27 interim early-stop absolute bias
ch04 collider absolute distortion
ch28 shared decision absolute frequencies

Agg indigo. Overwrites cycle13_swarm_* only.
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
    plt.close(fig); print("  wrote", p.name); return p

def fig_ch11():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    mrs = np.arange(0, 6)
    ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
    trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
    w = 0.35
    ax.bar(mrs - w/2, ctrl, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(mrs + w/2, trt, width=w, color=TEAL, edgecolor=INDIGO, label="Treated %")
    ax.set_xlabel("mRS"); ax.set_ylabel("% of arm"); ax.set_title("Ordinal shift: mass moves left", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3)
    ax = axes[1]
    labs = ["Dichotomized\nmRS0–2 ARR", "Utility-weighted\nmean gain", "Worst strata\n(mRS5–6) Δ"]
    vals = [5.0, 0.04, -1.5]
    ax.bar(range(3), [5, 4, 1.5], color=[TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_ylabel("Absolute metrics (scaled teaching)"); ax.set_title("Do not hide ordinal harm in a binary win", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Stroke outcomes: ordinal absolute shift vs dichotomized ARR (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch11_ordinal_shift.png")

def fig_ch13():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Industry-adjacent spin patterns", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [
        (7.5, CORAL, "Relative headline", "RRR in abstract; ARR buried"),
        (5.3, ORANGE, "Subgroup rescue", "Null primary → favorable stratum"),
        (3.1, GOLD, "Composite inflate", "Soft components drive significance"),
        (0.9, TEAL, "Defense", "Force absolute primary + interaction test"),
    ]:
        ax.add_patch(FancyBboxPatch((0.4, y-0.7), 9.2, 1.7, boxstyle="round,pad=0.04,rounding_size=0.08", facecolor=WHITE, edgecolor=edge, lw=1.35))
        ax.text(0.7, y+0.35, t, fontsize=9, fontweight="bold", color=edge)
        ax.text(0.7, y-0.3, b, fontsize=8.2, color=SLATE)
    ax = axes[1]
    ax.bar([0,1], [70, 18], color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(["Press-release\nenthusiasm", "After absolute\n+ HTE audit"], fontsize=9)
    ax.set_ylabel("% 'practice-changing' votes (synthetic)"); ax.set_ylim(0,100)
    ax.set_title("Spin collapses under absolute audit", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Subgroups & spin: absolute audit defeats relative theater (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch13_spin_audit.png")

def fig_ch18():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Counterfactual pair → absolute contrast", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5, 6), 4, 2.8, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor=WHITE, edgecolor=TEAL, lw=1.5))
    ax.text(2.5, 7.4, "Y(1)\nif treated", ha="center", fontsize=10, fontweight="bold", color=TEAL)
    ax.add_patch(FancyBboxPatch((5.5, 6), 4, 2.8, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor=WHITE, edgecolor=CORAL, lw=1.5))
    ax.text(7.5, 7.4, "Y(0)\nif control", ha="center", fontsize=10, fontweight="bold", color=CORAL)
    ax.add_patch(FancyBboxPatch((1.5, 1.5), 7, 3.2, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor="#FFF8E1", edgecolor=GOLD, lw=1.4))
    ax.text(5, 3.1, "ATE = E[Y(1)−Y(0)]\n≈ ARR when Y is binary event", ha="center", fontsize=11, fontweight="bold", color=SLATE)
    ax = axes[1]
    labs = ["Association\nRD", "Causal ARR\nif identified", "If backdoor\nopen"]
    ax.bar(range(3), [8, 3, np.nan], color=[GOLD, TEAL, GRAY], edgecolor=INDIGO, width=0.6)
    # plot only first two properly
    ax.cla()
    ax.bar([0,1,2], [8, 3, 0], color=[GOLD, TEAL, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks([0,1,2]); ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_ylabel("pp"); ax.set_title("Identification before absolute causal claim", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax.text(2, 0.4, "refuse", ha="center", fontsize=8, color=WHITE, fontweight="bold")
    fig.suptitle("Causation: counterfactuals justify absolute treat effects (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch18_counterfactual.png")

def fig_ch20():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    labs = ["Treatment\n(primary)", "Infarct\nvolume", "sICH\n(mediator)", "Age"]
    # table 2 fallacy - all shown as causal
    vals = [0.70, 1.40, 2.10, 1.05]
    ax.barh(range(4), vals, color=[TEAL, GOLD, CORAL, GRAY], edgecolor=INDIGO)
    ax.axvline(1, color=SLATE, lw=1.2)
    ax.set_yticks(range(4)); ax.set_yticklabels(labs, fontsize=9)
    ax.set_xlabel("Adjusted OR (Table 2 dump)")
    ax.set_title("Table 2 fallacy: every row looks causal", fontsize=10, fontweight="bold", color=INDIGO)
    ax = axes[1]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Absolute reading discipline", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [
        (7.2, TEAL, "One exposure", "Model built for one total effect"),
        (4.6, GOLD, "Absolute for primary", "ARR/NNT only for target exposure"),
        (2.0, CORAL, "Mediators ≠ co-causes", "Do not invent NNT for sICH coefficient"),
    ]:
        ax.add_patch(FancyBboxPatch((0.4, y-0.9), 9.2, 2.2, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor=WHITE, edgecolor=edge, lw=1.5))
        ax.text(5, y+0.5, t, ha="center", fontsize=10, fontweight="bold", color=edge)
        ax.text(5, y-0.4, b, ha="center", fontsize=8.5, color=SLATE)
    fig.suptitle("Regression literacy: Table 2 fallacy blocks absolute NNT shopping (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch20_table2.png")

def fig_ch27():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    looks = ["Look1", "Look2", "Look3", "Final"]
    arr = [8.0, 5.5, 4.0, 3.2]
    ax.plot(range(4), arr, "o-", color=INDIGO, lw=2.4, ms=9)
    ax.axhline(2.0, color=GOLD, ls="--", lw=1.3)
    ax.text(3.1, 2.2, "MCID", color=GOLD, fontsize=8)
    ax.set_xticks(range(4)); ax.set_xticklabels(looks, fontsize=9)
    ax.set_ylabel("Interim ARR (pp)"); ax.set_title("Early stop freezes inflated absolute", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    ax = axes[1]
    labs = ["Stopped early\nARR", "Completed\nARR", "Bias\n(overestimate)"]
    ax.bar(range(3), [6.5, 3.5, 3.0], color=[CORAL, TEAL, GOLD], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("pp"); ax.set_title("Absolute inflation from information-time stop", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Interim analyses: early stopping biases absolute effects (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch27_early_stop.png")

def fig_ch04():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Collider conditioning invents association", fontsize=10, fontweight="bold", color=INDIGO)
    for (x,y,lab,col) in [(2,7.5,"Tx A",INDIGO),(8,7.5,"Severity U",CORAL),(5,3.5,"ICU admit\n(collider)",GOLD)]:
        ax.add_patch(FancyBboxPatch((x-1.3,y-0.8),2.6,1.6,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor=WHITE,edgecolor=col,lw=1.5))
        ax.text(x,y,lab,ha="center",va="center",fontsize=9,fontweight="bold",color=col)
    ax.annotate("", xy=(4.2,4.5), xytext=(2.5,6.8), arrowprops=dict(arrowstyle="-|>", color=INDIGO, lw=1.8))
    ax.annotate("", xy=(5.8,4.5), xytext=(7.5,6.8), arrowprops=dict(arrowstyle="-|>", color=CORAL, lw=1.8))
    ax.text(5,1.5,"Condition on ICU → spurious A–U link → biased ARR", ha="center", fontsize=8.5, color=PURPLE, style="italic")
    ax = axes[1]
    labs = ["True ARR", "After collider\nstratification"]
    ax.bar([0,1],[4, -2], color=[TEAL, CORAL], edgecolor=INDIGO, width=0.55)
    ax.axhline(0, color=GRAY, lw=1)
    ax.set_xticks([0,1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("ARR (pp)"); ax.set_title("Collider bias can invert absolute effect", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Bias taxonomy: collider stratification moves absolute effects (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch04_collider.png")

def fig_ch28():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Shared decision natural frequencies", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5, 5.5), 9, 3.5, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor="#E8F5E9", edgecolor=TEAL, lw=1.5))
    ax.text(5, 7.8, "Out of 100 patients like you…", ha="center", fontsize=11, fontweight="bold", color=TEAL)
    ax.text(5, 6.5, "+5 walk independently (ARR)\n+2 severe bleed (ARI)", ha="center", fontsize=10, color=SLATE)
    ax.add_patch(FancyBboxPatch((0.5, 1.2), 9, 3.5, boxstyle="round,pad=0.05,rounding_size=0.1", facecolor="#FFEBEE", edgecolor=CORAL, lw=1.5))
    ax.text(5, 3.5, "Avoid: '40% fewer strokes'\nwithout denominator", ha="center", fontsize=10, fontweight="bold", color=CORAL)
    ax = axes[1]
    labs = ["Relative\nonly SDM", "Natural\nfrequency SDM"]
    ax.bar([0,1], [40, 85], color=[CORAL, TEAL], edgecolor=INDIGO, width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Patient understanding score (synthetic)"); ax.set_ylim(0,100)
    ax.set_title("Absolute frequencies improve consent quality", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Systems & communication: natural-frequency absolute SDM (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle13_swarm_ch28_sdm_freq.png")

def main():
    print("Cycle-13 →", OUT)
    for fn in [fig_ch11, fig_ch13, fig_ch18, fig_ch20, fig_ch27, fig_ch04, fig_ch28]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
