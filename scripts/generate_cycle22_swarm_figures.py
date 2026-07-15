#!/usr/bin/env python3
"""CRIT-APP Cycle-22 densify: floor-11 → 12 (wave B).
ch02,03,05,07,09,10,13 — Agg indigo. cycle22_swarm_* only.
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

def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    steps = ["Abstract", "Tables", "ARR", "Bias", "Action"]
    ok = [1, 1, 1, 0.6, 1]
    ax.bar(range(5), ok, color=[GRAY, TEAL, INDIGO, GOLD, CORAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(5)); ax.set_xticklabels(steps, fontsize=9)
    ax.set_ylabel("Triage weight"); ax.set_ylim(0, 1.2)
    ax.set_title("Speed protocol residual: never drop absolute ARR card", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch02_triage_weights.png")

def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Population", "Strategies", "Variable", "Intercurrent", "Summary ARR"]
    complete = [1, 1, 1, 0.4, 0.3]
    ax.barh(range(5)[::-1], complete, color=[TEAL if v>0.7 else CORAL for v in complete], edgecolor=INDIGO, height=0.6)
    ax.set_yticks(range(5)[::-1]); ax.set_yticklabels(labs, fontsize=9)
    ax.set_xlim(0, 1.15); ax.set_xlabel("Estimand completeness")
    ax.set_title("Estimand residual: incomplete intercurrent kills absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch03_estimand_complete.png")

def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    x = np.arange(2); w=0.35
    ax.bar(x-w/2, [10, 3], width=w, color=CORAL, edgecolor=INDIGO, label="Open backdoor ARR")
    ax.bar(x+w/2, [3.5, 3.2], width=w, color=TEAL, edgecolor=INDIGO, label="Closed residual ARR")
    ax.set_xticks(x); ax.set_xticklabels(["Crude", "After adjustment"], fontsize=9)
    ax.set_ylabel("ARR (pp)"); ax.set_title("DAG residual: close backdoors before absolute NNT", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch05_dag_close.png")

def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["User vs\nnon-user", "Active\ncomparator", "New-user\nACNU"]
    conf = [9, 5, 2.5]
    ax.bar(range(3), conf, color=[CORAL, GOLD, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Residual confounding ARR (pp teaching)")
    ax.set_title("Observational design residual: ACNU shrinks absolute bias", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch07_acnu_residual.png")

def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    deciles = np.arange(1, 11)
    pred = np.linspace(5, 55, 10)
    obs = pred + np.array([3, 2, -1, -4, -6, -5, -3, 0, 2, 4])
    ax.plot([0, 60], [0, 60], "--", color=GRAY)
    ax.plot(pred, obs, "o-", color=CORAL, lw=2.2, label="External calib.")
    ax.set_xlabel("Predicted %"); ax.set_ylabel("Observed %")
    ax.set_title("External calibration residual: absolute risk mispricing", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch09_ext_calib.png")

def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    labs = ["Pooled RR", "Local CER", "Local ARR", "Local NNT"]
    # display teaching
    vals = [0.75, 12, 3, 33]
    display = [7.5, 12, 3, 8]  # scaled NNT/4
    ax.bar(range(4), display, color=[GOLD, GRAY, TEAL, INDIGO], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(4)); ax.set_xticklabels([f"{l}\n({v})" for l,v in zip(labs,vals)], fontsize=8.5)
    ax.set_title("Guideline residual: convert pooled RR → local absolute NNT", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch10_local_nnt.png")

def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    strata = ["Low risk", "Mid", "High"]
    rr = [0.75, 0.75, 0.75]
    arr = [1.5, 4.0, 9.0]
    x = np.arange(3); w=0.35
    ax.bar(x-w/2, [r*10 for r in rr], width=w, color=GOLD, edgecolor=INDIGO, label="RR×10")
    ax.bar(x+w/2, arr, width=w, color=TEAL, edgecolor=INDIGO, label="ARR pp")
    ax.set_xticks(x); ax.set_xticklabels(strata, fontsize=9)
    ax.set_title("HTE residual: homogeneous RR, heterogeneous absolute ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle22_swarm_ch13_hte_abs.png")

def main():
    print("Cycle-22 →", OUT)
    for fn in [fig_ch02, fig_ch03, fig_ch05, fig_ch07, fig_ch09, fig_ch10, fig_ch13]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
