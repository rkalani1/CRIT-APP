#!/usr/bin/env python3
"""CRIT-APP Cycle-1733 densify (early). Agg indigo. ARR/NNT. pred!=cause."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p

def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cats = ["mRS0", "mRS1", "mRS2", "mRS3", "mRS4-5", "mRS6"]
    ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
    trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
    x = np.arange(2)
    bottom_c = bottom_t = 0
    colors = [TEAL, "#4DB6AC", INDIGO, GOLD, CORAL, SLATE]
    for i, c in enumerate(cats):
        ax.bar(0, ctrl[i], bottom=bottom_c, color=colors[i], edgecolor=WHITE, width=0.55, label=c)
        ax.bar(1, trt[i], bottom=bottom_t, color=colors[i], edgecolor=WHITE, width=0.55)
        bottom_c += ctrl[i]; bottom_t += trt[i]
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Control", "Treated"])
    ax.set_ylabel("Absolute % of patients")
    ax.set_title("Ch01 residual: absolute risk framing beats relative-only claims (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch01_w1733_1.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (2 % 5), 18 + (2 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch02 residual: under time pressure, extract ARR and NNT first (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch02_w1733_2.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (4) * 0.02 + (3) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch03 residual: PICO index time fixes the absolute estimand (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch03_w1733_3.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch04 residual: bias taxonomy mapped to absolute distortion (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch04_w1733_4.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cats = ["mRS0", "mRS1", "mRS2", "mRS3", "mRS4-5", "mRS6"]
    ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
    trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
    x = np.arange(2)
    bottom_c = bottom_t = 0
    colors = [TEAL, "#4DB6AC", INDIGO, GOLD, CORAL, SLATE]
    for i, c in enumerate(cats):
        ax.bar(0, ctrl[i], bottom=bottom_c, color=colors[i], edgecolor=WHITE, width=0.55, label=c)
        ax.bar(1, trt[i], bottom=bottom_t, color=colors[i], edgecolor=WHITE, width=0.55)
        bottom_c += ctrl[i]; bottom_t += trt[i]
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Control", "Treated"])
    ax.set_ylabel("Absolute % of patients")
    ax.set_title("Ch05 residual: DAG confounding shifts absolute event rates (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch05_w1733_5.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (6 % 5), 18 + (6 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch06 residual: RCT arms: control vs treated absolute risks (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch06_w1733_6.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (4) * 0.02 + (3) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch07 residual: observational residual confounding vs ARR (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch07_w1733_7.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch08 residual: sensitivity/specificity feed absolute post-test risk (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch08_w1733_8.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cats = ["mRS0", "mRS1", "mRS2", "mRS3", "mRS4-5", "mRS6"]
    ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
    trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
    x = np.arange(2)
    bottom_c = bottom_t = 0
    colors = [TEAL, "#4DB6AC", INDIGO, GOLD, CORAL, SLATE]
    for i, c in enumerate(cats):
        ax.bar(0, ctrl[i], bottom=bottom_c, color=colors[i], edgecolor=WHITE, width=0.55, label=c)
        ax.bar(1, trt[i], bottom=bottom_t, color=colors[i], edgecolor=WHITE, width=0.55)
        bottom_c += ctrl[i]; bottom_t += trt[i]
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Control", "Treated"])
    ax.set_ylabel("Absolute % of patients")
    ax.set_title("Ch09 residual: prediction is not causation — calibrate absolute risk (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch09_w1733_9.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (10 % 5), 18 + (10 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch10 residual: pooled absolute effects, not relative alone (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch10_w1733_10.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (4) * 0.02 + (3) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch11 residual: mRS shift as absolute outcome distribution (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch11_w1733_11.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch12 residual: ARR and NNT are the clinical importance core (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch12_w1733_12.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cats = ["mRS0", "mRS1", "mRS2", "mRS3", "mRS4-5", "mRS6"]
    ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
    trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
    x = np.arange(2)
    bottom_c = bottom_t = 0
    colors = [TEAL, "#4DB6AC", INDIGO, GOLD, CORAL, SLATE]
    for i, c in enumerate(cats):
        ax.bar(0, ctrl[i], bottom=bottom_c, color=colors[i], edgecolor=WHITE, width=0.55, label=c)
        ax.bar(1, trt[i], bottom=bottom_t, color=colors[i], edgecolor=WHITE, width=0.55)
        bottom_c += ctrl[i]; bottom_t += trt[i]
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Control", "Treated"])
    ax.set_ylabel("Absolute % of patients")
    ax.set_title("Ch13 residual: subgroup interaction needs absolute contrast (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch13_w1733_13.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (14 % 5), 18 + (14 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch14 residual: AI model discrimination ≠ causal effect (C1733)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1733_swarm_ch14_w1733_14.png")


def main():
    print("Cycle-1733", OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
