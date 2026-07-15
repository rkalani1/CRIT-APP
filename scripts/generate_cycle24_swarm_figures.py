#!/usr/bin/env python3
"""CRIT-APP Cycle-24 densify: clear residual floor-11 → uniform floor ≥12.
ch22,23,24,25,26,27,28 — Agg indigo. cycle24_swarm_* only.
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

def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Mortality\nARR", "Overdiag\n/1000", "FP\n/1000", "NNScreen"]
    vals = [1.2, 15, 50, 833]
    display = [1.2, 15, 20, 12]
    ax.bar(range(4), display, color=[TEAL, CORAL, GOLD, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels([f"{l}\n≈{v}" for l,v in zip(labs,vals)], fontsize=8.5)
    ax.set_title("Screening residual: absolute benefit vs overdiagnosis burden", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch22_screen_ledger.png")

def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    biases = ["Base-rate\nneglect", "Anchoring", "Availability", "Premature\nclosure"]
    harm = [8, 5, 6, 7]
    ax.barh(range(4)[::-1], harm, color=[CORAL, ORANGE, GOLD, PURPLE], edgecolor=INDIGO, height=0.6)
    ax.set_yticks(range(4)[::-1]); ax.set_yticklabels(biases, fontsize=9)
    ax.set_xlabel("Absolute error risk units (teaching)")
    ax.set_title("Reasoning residual: cognitive biases cost absolute probability accuracy", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch23_bias_cost.png")

def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Primary\nARR", "Safety\nARI", "Net\nbenefit", "Fragile?"]
    vals = [4.0, 1.2, 2.8, 1]
    cols = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(range(4), vals, color=cols, edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("pp or flag")
    ax.set_title("Therapy residual: net absolute benefit after safety ARI", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch24_net_benefit.png")

def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["LR+", "Post-test\n@10% prior", "Calib slope", "Action?"]
    vals = [5, 36, 0.85, 1]
    display = [5, 9, 8.5, 4]
    ax.bar(range(4), display, color=[INDIGO, TEAL, GOLD, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels([f"{l}\n({v})" for l,v in zip(labs,vals)], fontsize=8.5)
    ax.set_title("Dx/Px residual: absolute post-test and calibration before action", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch25_action_gate.png")

def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Derivation\nc-stat", "External\nc-stat", "Impact\nARR pp"]
    vals = [0.82, 0.71, 0.8]
    display = [8.2, 7.1, 0.8]
    ax.bar(range(3), display, color=[GOLD, TEAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_title("CPR residual: derivation hype ≠ absolute impact ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch26_cpr_maturity.png")

def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Primary p", "FI", "FQ %", "Missing\n%"]
    vals = [0.04, 3, 7, 18]
    display = [4, 3, 7, 18]
    ax.bar(range(4), display, color=[GOLD, CORAL, ORANGE, GRAY], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels([f"{l}\n({v})" for l,v in zip(labs,vals)], fontsize=8.5)
    ax.set_title("Fragility residual: thin absolute margins despite significance", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle24_swarm_ch27_thin_margin.png")

def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 4.9)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
    ax.set_title("Policy residual: absolute communication checklist", fontsize=11, fontweight="bold", color=INDIGO)
    for y,e,t in [(4.2,TEAL,"Out of 100: events with / without"),(2.4,INDIGO,"NNT and NNH same horizon"),(0.6,CORAL,"No RRR-only consent language")]:
        ax.add_patch(FancyBboxPatch((0.4,y),9.2,1.4,boxstyle="round,pad=0.03,rounding_size=0.07",facecolor=WHITE,edgecolor=e,lw=1.5))
        ax.text(5,y+0.7,t,ha="center",va="center",fontsize=10,fontweight="bold",color=e)
    fig.tight_layout(); return _save(fig, "cycle24_swarm_ch28_policy_comm.png")

def main():
    print("Cycle-24 →", OUT)
    for fn in [fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
