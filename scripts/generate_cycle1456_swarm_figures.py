#!/usr/bin/env python3
"""CRIT-APP Cycle-1456 densify (late). Agg indigo. ARR/NNT. pred!=cause."""
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

def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(145615)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch15 residual: journal club absolute-risk board completeness (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch15_w1456_1.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.024) * t))
    tr = 100 * (1 - np.exp(-(0.017) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch16 residual: autopsy flow ends in absolute action codes (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch16_w1456_2.png")


def fig_ch17():
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
    ax.set_title("Ch17 residual: cumulative incidence is absolute risk over time (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch17_w1456_3.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 18) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch18 residual: causal contrast of potential outcome risks (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch18_w1456_4.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(145619)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch19 residual: CI width on the absolute risk scale (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch19_w1456_5.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.02) * t))
    tr = 100 * (1 - np.exp(-(0.014) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch20 residual: landmark survival ARR after index time (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch20_w1456_6.png")


def fig_ch21():
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
    ax.set_title("Ch21 residual: effect modification on absolute risk difference (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch21_w1456_7.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 22) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch22 residual: overdiagnosis inflates apparent absolute benefit (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch22_w1456_8.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(145623)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch23 residual: cognitive bias distorts absolute risk perception (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch23_w1456_9.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.036000000000000004) * t))
    tr = 100 * (1 - np.exp(-(0.026000000000000002) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch24 residual: therapy harm: absolute risk increase and NNH (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch24_w1456_10.png")


def fig_ch25():
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
    ax.set_title("Ch25 residual: diagnosis/prognosis absolute calibration check (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch25_w1456_11.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    pred = np.linspace(0.05, 0.55, 8)
    obs = pred + 0.04 * np.sin(pred * 12 + 26) - 0.02 * (1)
    ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
    ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
    ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
    ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
    ax.set_title("Ch26 residual: CPR absolute net benefit vs treat-all/none (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch26_w1456_12.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    rng = np.random.default_rng(145627)
    x = np.arange(0, 7)
    ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
    trt = ctrl - (3.5 + 0.35 * x)
    ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
    ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
    ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
    ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch27 residual: missingness and fragility of absolute estimates (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch27_w1456_13.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 100)
    c = 100 * (1 - np.exp(-(0.032) * t))
    tr = 100 * (1 - np.exp(-(0.023) * t))
    ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
    ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
    ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
    ax.set_title("Ch28 residual: systems of care: absolute door-to-needle gains (C1456)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1456_swarm_ch28_w1456_14.png")


def main():
    print("Cycle-1456", OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
