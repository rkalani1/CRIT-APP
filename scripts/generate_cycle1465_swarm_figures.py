#!/usr/bin/env python3
"""CRIT-APP Cycle-1465 densify (late). Agg indigo. ARR/NNT. pred!=cause."""
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
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (15 % 5), 18 + (15 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch15 residual: journal club absolute-risk board completeness (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch15_w1465_1.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (2) * 0.02 + (0) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch16 residual: autopsy flow ends in absolute action codes (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch16_w1465_2.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch17 residual: cumulative incidence is absolute risk over time (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch17_w1465_3.png")


def fig_ch18():
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
    ax.set_title("Ch18 residual: causal contrast of potential outcome risks (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch18_w1465_4.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (19 % 5), 18 + (19 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch19 residual: CI width on the absolute risk scale (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch19_w1465_5.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (2) * 0.02 + (0) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch20 residual: landmark survival ARR after index time (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch20_w1465_6.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch21 residual: effect modification on absolute risk difference (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch21_w1465_7.png")


def fig_ch22():
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
    ax.set_title("Ch22 residual: overdiagnosis inflates apparent absolute benefit (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch22_w1465_8.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (23 % 5), 18 + (23 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch23 residual: cognitive bias distorts absolute risk perception (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch23_w1465_9.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (2) * 0.02 + (0) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch24 residual: therapy harm: absolute risk increase and NNH (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch24_w1465_10.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(1.0, 12.0, 40)
    nnt = 100.0 / arr
    ax.plot(arr, nnt, color=TEAL, lw=2.5)
    ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
    ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
    ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
    ax.set_ylim(0, 120)
    ax.set_title("Ch25 residual: diagnosis/prognosis absolute calibration check (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch25_w1465_11.png")


def fig_ch26():
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
    ax.set_title("Ch26 residual: CPR absolute net benefit vs treat-all/none (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
    ax.set_ylim(0, 100); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch26_w1465_12.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Y1", "Y0", "ARR", "NNT"]
    y1, y0 = 12 + (27 % 5), 18 + (27 % 4)
    arr = y0 - y1
    nnt = round(100 / arr, 1) if arr else 0
    vals = [y1, y0, arr, nnt]
    colors = [TEAL, CORAL, INDIGO, GOLD]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Abs risk % / pp / patients")
    ax.set_title("Ch27 residual: missingness and fragility of absolute estimates (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch27_w1465_13.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ["Internal val", "External val", "Abs report", "Actionable"]
    base = np.array([0.55, 0.45, 0.35, 0.40]) + (2) * 0.02 + (0) * 0.03
    base = np.clip(base, 0.1, 0.95)
    ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
    ax.set_xlabel("Absolute appraisal score (0-1)")
    ax.set_xlim(0, 1)
    ax.set_title("Ch28 residual: systems of care: absolute door-to-needle gains (C1465)", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
    return _save(fig, "cycle1465_swarm_ch28_w1465_14.png")


def main():
    print("Cycle-1465", OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
