#!/usr/bin/env python3
"""CRIT-APP Cycle-55 densify: ch01-14 densify. Agg indigo. ARR/NNT. pred!=cause."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"
def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([2, 3, 4, 3.5, 5, 4])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch01 residual: absolute uptake lags published claims', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch01_uptake_gap.png')


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [4, 5, 3, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch02 residual: minutes to first absolute ARR extract', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch02_minute_arr.png')


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.03 * t)
    b = 1 - np.exp(-0.03 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch03 residual: index-time absolute risk zero point', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch03_index_risk.png')


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [4, 5, 3, 7]
    v2 = [2, 4, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch04 residual: external validity is absolute transport', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch04_ext_valid.png')


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    y = ['D1','D2','D3','D4','D5']
    v = [0.9, 0.6499999999999999, 0.5, 0.8, 0.4]
    ax.barh(y, v, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score / fraction')
    ax.set_title('Ch05 residual: IV LATE is a local absolute effect', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch05_iv_abs.png')


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([4, 4, 4, 3.5, 5, 5])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch06 residual: blinding protects absolute outcome assessment', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch06_blind_bias.png')


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [5, 5, 2, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch07 residual: healthy-user absolute risk separation', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch07_healthy_abs.png')


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.025 * t)
    b = 1 - np.exp(-0.034999999999999996 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch08 residual: spectrum bias moves absolute PPV', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch08_spec_bias.png')


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [6, 5, 3, 6]
    v2 = [2, 3, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch09 residual: pred!=cause — external absolute calibration gap', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch09_ext_cal.png')


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    y = ['D1','D2','D3','D4','D5']
    v = [0.9, 0.7, 0.5, 0.8, 0.45]
    ax.barh(y, v, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score / fraction')
    ax.set_title('Ch10 residual: SUCRA ranks need absolute ARR companions', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch10_sucra_arr.png')


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([3, 3, 4, 3.5, 5, 4])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch11 residual: win ratio needs absolute RD companion', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch11_win_rd.png')


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [6, 5, 4, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch12 residual: NNH absolute harm curve', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch12_nnh_curve.png')


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.02 * t)
    b = 1 - np.exp(-0.03 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch13 residual: subgroup absolute ARR forest', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch13_hte_forest.png')


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [5, 5, 3, 7]
    v2 = [2, 4, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch14 residual: pred!=cause — group absolute miscalibration', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle55_swarm_ch14_fair_abs.png')


def main():
    print('Cycle-55 ->', OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print('Done: 14')
if __name__ == '__main__':
    main()
