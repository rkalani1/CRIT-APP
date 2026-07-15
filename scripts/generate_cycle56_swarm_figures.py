#!/usr/bin/env python3
"""CRIT-APP Cycle-56 densify: ch15-28 densify. Agg indigo. ARR/NNT. pred!=cause."""
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


def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([2, 3, 4, 3.5, 5, 4])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch15 residual: teach-back absolute ARR retention', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch15_teach_arr.png')


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [4, 5, 3, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch16 residual: red-team absolute stress-test completion', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch16_redteam.png')


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.03 * t)
    b = 1 - np.exp(-0.03 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch17 residual: attributable fraction needs absolute rates', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch17_af_abs.png')


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [4, 5, 3, 7]
    v2 = [2, 4, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch18 residual: DAG+trial beat weak absolute checklists', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch18_dag_hill.png')


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    y = ['D1','D2','D3','D4','D5']
    v = [0.9, 0.6499999999999999, 0.5, 0.8, 0.4]
    ax.barh(y, v, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score / fraction')
    ax.set_title('Ch19 residual: sequential absolute false-positive growth', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch19_seq_fpr.png')


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([4, 4, 4, 3.5, 5, 5])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch20 residual: absolute survival difference curves', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch20_surv_diff.png')


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [5, 5, 2, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch21 residual: RERI is absolute interaction excess', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch21_reri_abs.png')


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.025 * t)
    b = 1 - np.exp(-0.034999999999999996 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch22 residual: length-time absolute indolent enrichment', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch22_length_abs.png')


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [6, 5, 3, 6]
    v2 = [2, 3, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch23 residual: anchoring distorts absolute estimates', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch23_anchor_abs.png')


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    y = ['D1','D2','D3','D4','D5']
    v = [0.9, 0.7, 0.5, 0.8, 0.45]
    ax.barh(y, v, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score / fraction')
    ax.set_title('Ch24 residual: surrogate absolute gains without hard benefit', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch24_surr_fail.png')


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 7)
    y = np.array([3, 3, 4, 3.5, 5, 4])
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute teaching metric')
    ax.set_title('Ch25 residual: diagnostic absolute yield over care path', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch25_dx_path.png')


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = ['A','B','C','D','E']
    vals = [6, 5, 4, 6, 4]
    ax.bar(labels, vals, color=[TEAL, INDIGO, GOLD, CORAL, GRAY], edgecolor=SLATE)
    ax.set_ylabel('Absolute units (pp or %)')
    ax.set_title('Ch26 residual: living SR absolute ARR trajectory', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch26_living_arr.png')


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 24, 80)
    a = 1 - np.exp(-0.02 * t)
    b = 1 - np.exp(-0.03 * t)
    ax.plot(t, a*100, color=TEAL, lw=2.3, label='Arm A abs %')
    ax.plot(t, b*100, color=CORAL, lw=2.3, label='Arm B abs %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch27 residual: tipping-point absolute missing assumptions', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch27_tip_abs.png')


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labs = ['Q1','Q2','Q3','Q4']
    v1 = [5, 5, 3, 7]
    v2 = [2, 4, 4, 3]
    x = np.arange(4)
    ax.bar(x-0.2, v1, width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit abs')
    ax.bar(x+0.2, v2, width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm abs')
    ax.set_xticks(x); ax.set_xticklabels(labs)
    ax.set_ylabel('Absolute pp / %')
    ax.set_title('Ch28 residual: policy absolute outcome vs cost trade', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    handles, labels = ax.get_legend_handles_labels()
    if handles:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle56_swarm_ch28_policy_abs.png')


def main():
    print('Cycle-56 ->', OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print('Done: 14')
if __name__ == '__main__':
    main()
