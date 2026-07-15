#!/usr/bin/env python3
"""CRIT-APP Cycle-1466 densify (early). Agg indigo. ARR/NNT. pred!=cause."""
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
    studies = [f"S{i}" for i in range(1, 6)]
    rd = np.array([-2.0, -3.5, -1.2, -4.0, -2.8]) + (1) * 0.3
    lo, hi = rd - 1.8, rd + 1.8
    y = np.arange(len(studies))
    ax.hlines(y, lo, hi, color=SLATE, lw=2)
    ax.plot(rd, y, "o", color=INDIGO, ms=8)
    ax.axvline(0, color=CORAL, ls="--", lw=1.2)
    ax.set_yticks(y); ax.set_yticklabels(studies)
    ax.set_xlabel("Risk difference (pp, absolute)")
    ax.set_title("Ch01 residual: absolute risk framing beats relative-only claims (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch01_w1466_1.png")


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 2) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch02 residual: under time pressure, extract ARR and NNT first (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch02_w1466_2.png")


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(146603)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch03 residual: PICO index time fixes the absolute estimand (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch03_w1466_3.png")


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.036000000000000004) * t))
    tr = 100 * (1 - np.exp(-(0.026000000000000002) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch04 residual: bias taxonomy mapped to absolute distortion (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch04_w1466_4.png")


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    studies = [f"S{i}" for i in range(1, 6)]
    rd = np.array([-2.0, -3.5, -1.2, -4.0, -2.8]) + (2) * 0.3
    lo, hi = rd - 1.8, rd + 1.8
    y = np.arange(len(studies))
    ax.hlines(y, lo, hi, color=SLATE, lw=2)
    ax.plot(rd, y, "o", color=INDIGO, ms=8)
    ax.axvline(0, color=CORAL, ls="--", lw=1.2)
    ax.set_yticks(y); ax.set_yticklabels(studies)
    ax.set_xlabel("Risk difference (pp, absolute)")
    ax.set_title("Ch05 residual: DAG confounding shifts absolute event rates (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch05_w1466_5.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 6) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch06 residual: RCT arms: control vs treated absolute risks (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch06_w1466_6.png")


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(146607)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch07 residual: observational residual confounding vs ARR (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch07_w1466_7.png")


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.032) * t))
    tr = 100 * (1 - np.exp(-(0.023) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch08 residual: sensitivity/specificity feed absolute post-test risk (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch08_w1466_8.png")


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    studies = [f"S{i}" for i in range(1, 6)]
    rd = np.array([-2.0, -3.5, -1.2, -4.0, -2.8]) + (0) * 0.3
    lo, hi = rd - 1.8, rd + 1.8
    y = np.arange(len(studies))
    ax.hlines(y, lo, hi, color=SLATE, lw=2)
    ax.plot(rd, y, "o", color=INDIGO, ms=8)
    ax.axvline(0, color=CORAL, ls="--", lw=1.2)
    ax.set_yticks(y); ax.set_yticklabels(studies)
    ax.set_xlabel("Risk difference (pp, absolute)")
    ax.set_title("Ch09 residual: prediction is not causation — calibrate absolute risk (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch09_w1466_9.png")


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 10) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch10 residual: pooled absolute effects, not relative alone (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch10_w1466_10.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(146611)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch11 residual: mRS shift as absolute outcome distribution (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch11_w1466_11.png")


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.028) * t))
    tr = 100 * (1 - np.exp(-(0.02) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch12 residual: ARR and NNT are the clinical importance core (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch12_w1466_12.png")


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    studies = [f"S{i}" for i in range(1, 6)]
    rd = np.array([-2.0, -3.5, -1.2, -4.0, -2.8]) + (1) * 0.3
    lo, hi = rd - 1.8, rd + 1.8
    y = np.arange(len(studies))
    ax.hlines(y, lo, hi, color=SLATE, lw=2)
    ax.plot(rd, y, "o", color=INDIGO, ms=8)
    ax.axvline(0, color=CORAL, ls="--", lw=1.2)
    ax.set_yticks(y); ax.set_yticklabels(studies)
    ax.set_xlabel("Risk difference (pp, absolute)")
    ax.set_title("Ch13 residual: subgroup interaction needs absolute contrast (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch13_w1466_13.png")


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 14) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch14 residual: AI model discrimination ≠ causal effect (C1466)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1466_swarm_ch14_w1466_14.png")


def main():
    print("Cycle-1466", OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
