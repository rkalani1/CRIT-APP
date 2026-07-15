#!/usr/bin/env python3
"""CRIT-APP Cycle-23 densify: floor-11 → 12 (wave C).
ch14,16,17,18,19,20,21 — Agg indigo. cycle23_swarm_* only.
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
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig); print("  wrote", p.name); return p

def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Stand-alone\nAUROC", "Human+AI\nAUROC", "Door-to-needle\nΔ min", "mRS ARR\npp"]
    vals = [0.91, 0.93, 4, 0.5]
    display = [9.1, 9.3, 4, 0.5]
    ax.bar(range(4), display, color=[GOLD, INDIGO, TEAL, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_title("AI residual: accuracy without absolute outcome impact is incomplete", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch14_impact_gap.png")

def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 4.9)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
    ax.set_title("Autopsy residual: fatal flaw → absolute action map", fontsize=11, fontweight="bold", color=INDIGO)
    for i,(y,e,t) in enumerate([(4.5,CORAL,"Fatal: invalid causal ARR → REJECT"),(2.5,GOLD,"Major: transport fail → ADAPT/AUDIT"),(0.5,TEAL,"Minor: imprecise CI → WAIT")]):
        ax.add_patch(FancyBboxPatch((0.4,y),9.2,1.3,boxstyle="round,pad=0.03,rounding_size=0.07",facecolor=WHITE,edgecolor=e,lw=1.5))
        ax.text(5,y+0.65,t,ha="center",va="center",fontsize=10,fontweight="bold",color=e)
    fig.tight_layout(); return _save(fig, "cycle23_swarm_ch16_flaw_action.png")

def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    ax.bar([0,1,2],[8,12,5],color=[TEAL,INDIGO,GOLD],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1,2]); ax.set_xticklabels(["Cumulative\nincidence %","Prevalence\n%","Rate\n/100 py"],fontsize=9)
    ax.set_title("Frequency residual: three absolute units, three different claims", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch17_three_units.png")

def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Association", "Adjustment", "TTE/RCT", "Causal ARR"]
    vals = [1, 0.6, 0.9, 0.85]
    ax.plot(range(4), vals, "o-", color=INDIGO, lw=2.4, ms=10)
    ax.fill_between(range(4), vals, alpha=0.1, color=INDIGO)
    ax.set_xticks(range(4)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylim(0, 1.15); ax.set_ylabel("Causal credibility (teaching)")
    ax.set_title("Causation residual: association ≠ absolute causal ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch18_assoc_to_arr.png")

def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    n = np.array([50, 100, 200, 500, 1000])
    se = 20 / np.sqrt(n)  # teaching
    ax.plot(n, se, "o-", color=TEAL, lw=2.3)
    ax.set_xlabel("N"); ax.set_ylabel("SE of ARR (pp teaching)")
    ax.set_title("Inference residual: absolute precision scales with √N", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch19_precision_n.png")

def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Crude OR", "Adjusted OR", "Table-2\nfallacy OR", "Causal\ncontrast"]
    vals = [0.55, 0.70, 0.40, 0.75]
    ax.bar(range(4), vals, color=[GRAY, TEAL, CORAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.axhline(1, color=GRAY, lw=1); ax.set_xticks(range(4)); ax.set_xticklabels(labs, fontsize=8.5)
    ax.set_ylabel("OR"); ax.set_title("Regression residual: table-2 fallacy distorts absolute pathway claims", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch20_table2.png")

def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Multiplicative\ninteraction p", "Additive\nRERI", "Stratum ARR\nhigh-risk"]
    vals = [0.4, 6.0, 12.0]
    display = [4, 6, 12]
    ax.bar(range(3), display, color=[GOLD, TEAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_title("Interaction residual: report additive absolute RERI, not p alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle23_swarm_ch21_reri.png")

def main():
    print("Cycle-23 →", OUT)
    for fn in [fig_ch14, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
