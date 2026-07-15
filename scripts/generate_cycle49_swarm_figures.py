#!/usr/bin/env python3
"""CRIT-APP Cycle-49 densify: ch01-14 toward floor. Agg indigo. ARR/NNT. pred≠cause."""
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

    x = np.array([1, 2, 3, 4, 5, 6])
    ax.plot(x, [0.4, 0.45, 0.5, 0.48, 0.52, 0.55], 'o-', color=TEAL, lw=2.3, label='ARR-vetted signal')
    ax.plot(x, [0.9, 0.95, 1.0, 1.1, 1.2, 1.3], 's--', color=CORAL, lw=2.2, label='All claims')
    ax.set_xlabel('Month'); ax.set_ylabel('Relative count')

    ax.set_title('Ch01 residual: absolute signal fraction among claims', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch01_signal_noise.png')


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Skim', 'ARR?', 'Bias', 'Deep', 'Stop']
    vals = [100, 55, 30, 15, 45]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute % of papers')

    ax.set_title('Ch02 residual: absolute triage ladder cuts reading load', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch02_triage_ladder.png')


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Policy', 'WoT', 'Hypoth', 'PrinStrat']
    vals = [3.5, 4.8, 5.5, 2.0]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch03 residual: estimand map changes absolute target', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch03_estimand_map.png')


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Sel', 'Info', 'Conf', 'Attr', 'Rep']
    vals = [2.5, 1.2, 3.1, 1.8, 0.9]
    ax.barh(labels, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('|ARR bias| pp')

    ax.set_title('Ch04 residual: multi-bias absolute distortion map', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch04_bias_radar.png')


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 2, 3, 4, 5])
    ax.plot(x, [8, 6.5, 5.2, 4.3, 4.0], 'o-', color=TEAL, lw=2.3, label='Sequential adj ARR')
    ax.plot(x, [8, 8, 8, 8, 8], 's--', color=CORAL, lw=2.2, label='Crude ARR')
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch05 residual: target-trial steps recover absolute ARR', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch05_target_trial.png')


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Good', 'Unclear', 'Poor']
    vals = [4.0, 5.2, 6.8]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Apparent absolute ARR pp')

    ax.set_title('Ch06 residual: randomization quality protects absolute effects', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch06_rand_quality.png')


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(3)
    ax.bar(x-0.2, [4.5, 1.2, 1.5], width=0.4, color=TEAL, edgecolor=INDIGO, label='|Abs bias| pp')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [12, 8, 9], width=0.4, color=CORAL, edgecolor=INDIGO, label='Events/100py')
    ax.set_xticks(x); ax.set_xticklabels(['Prevalent', 'New-user', 'Active-comp'])
    ax.set_ylabel('Bias'); ax2.set_ylabel('Rate')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch07 residual: new-user design cuts absolute healthy-user gap', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch07_new_user.png')


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.linspace(0, 100, 80)
    y = 1/(1+np.exp(-(x-30)/8))*100
    ax.plot(x, y, color=INDIGO, lw=2.5)
    ax.fill_between(x, y, color=TEAL, alpha=0.15)
    ax.set_xlabel('Prior/score'); ax.set_ylabel('Post-test absolute %')

    ax.set_title('Ch08 residual: post-test absolute probability drives action', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch08_posttest.png')


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.plot(x, [5, 10, 15, 20, 25, 30, 35, 40, 45, 50], 'o-', color=TEAL, lw=2.3, label='Predicted abs %')
    ax.plot(x, [6, 11, 14, 18, 22, 28, 40, 48, 55, 62], 's--', color=CORAL, lw=2.2, label='Observed abs %')
    ax.set_xlabel('Decile center'); ax.set_ylabel('Absolute risk %')

    ax.set_title('Ch09 residual: pred≠cause — recalibration fixes absolute risk', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch09_recal.png')


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Low I2', 'Mod', 'High', 'V.high']
    vals = [1.0, 1.8, 3.2, 5.0]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute CI half-width pp')

    ax.set_title('Ch10 residual: heterogeneity widens absolute pooled uncertainty', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch10_het_i2.png')


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['mRS0', '1', '2', '3', '4', '5']
    vals = [0.06, 0.04, 0.02, -0.03, -0.05, -0.04]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Δ absolute probability')

    ax.set_title('Ch11 residual: absolute utility gain from mRS shift', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch11_mrs_utility.png')


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(4)
    ax.bar(x-0.2, [3, 5, 2, 6], width=0.4, color=TEAL, edgecolor=INDIGO, label='ARR pp')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [1.2, 1.5, 2.0, 1.0], width=0.4, color=CORAL, edgecolor=INDIGO, label='CI half pp')
    ax.set_xticks(x); ax.set_xticklabels(['StudyA', 'B', 'C', 'D'])
    ax.set_ylabel('ARR'); ax2.set_ylabel('CI half')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch12 residual: report absolute ARR with CI not RR alone', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch12_arr_ci.png')


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['A−', 'A+']
    vals = [3.0, 7.0]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch13 residual: HTE claims require absolute interaction', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch13_hte_abs.png')


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 1, 2, 3, 4, 5, 6])
    ax.plot(x, [0.1, 0.09, 0.08, 0.06, 0.04, 0.02, 0.0], 'o-', color=TEAL, lw=2.3, label='Abs net benefit')
    ax.plot(x, [0.86, 0.85, 0.84, 0.83, 0.82, 0.81, 0.8], 's--', color=CORAL, lw=2.2, label='AUROC')
    ax.set_xlabel('Month'); ax.set_ylabel('Value')

    ax.set_title('Ch14 residual: pred≠cause — monitor absolute net benefit live', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle49_swarm_ch14_monitor.png')


def main():
    print("Cycle-49 →", OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
