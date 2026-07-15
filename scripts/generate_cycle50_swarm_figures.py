#!/usr/bin/env python3
"""CRIT-APP Cycle-50 densify: ch15-28 raise floor. Agg indigo. ARR/NNT. pred≠cause."""
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

    labels = ['PICO', 'Bias', 'ARR', 'NNT', 'Action']
    vals = [0.9, 0.7, 0.4, 0.3, 0.5]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Completion fraction')

    ax.set_title('Ch15 residual: every JC needs a filled absolute-risk board', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch15_jc_abs_board.png')


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 2, 3, 4, 5])
    ax.plot(x, [1, 0.9, 0.75, 0.6, 0.55], 'o-', color=TEAL, lw=2.3, label='With abs board')
    ax.plot(x, [1, 0.7, 0.4, 0.2, 0.1], 's--', color=CORAL, lw=2.2, label='Without')
    ax.set_xlabel('Stage'); ax.set_ylabel('Fraction complete')

    ax.set_title('Ch16 residual: autopsy flow ends in absolute action code', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch16_autopsy_flow.png')


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.linspace(0, 24, 80)
    y = 100*(1-np.exp(-0.04*x))
    ax.plot(x, y, color=INDIGO, lw=2.5)
    ax.fill_between(x, y, color=TEAL, alpha=0.15)
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative incidence %')

    ax.set_title('Ch17 residual: cumulative incidence is absolute risk over time', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch17_cum_inc.png')


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Y1', 'Y0', 'ARR']
    vals = [18, 24, 6]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute risk % / pp')

    ax.set_title('Ch18 residual: causal absolute contrast of potential outcomes', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch18_cf_contrast.png')


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([50, 100, 200, 400, 800])
    ax.plot(x, [5.5, 3.9, 2.8, 2.0, 1.4], 'o-', color=TEAL, lw=2.3, label='CI half-width pp')
    ax.plot(x, [5.5, 3.9, 2.8, 2.0, 1.4], 's--', color=CORAL, lw=2.2, label='ref')
    ax.set_xlabel('n per arm'); ax.set_ylabel('pp')

    ax.set_title('Ch19 residual: absolute CI width is the honesty metric', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch19_ci_width.png')


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 3, 6, 9, 12, 18, 24])
    ax.plot(x, [0, 2, 4, 5, 5.5, 6, 6.2], 'o-', color=TEAL, lw=2.3, label='From t0 ARR cum')
    ax.plot(x, [0, 0, 0, 2, 3.5, 4.5, 5.0], 's--', color=CORAL, lw=2.2, label='Landmark@6 ARR')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute pp')

    ax.set_title('Ch20 residual: landmark absolute ARR after landmark time', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch20_landmark_arr.png')


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['S1', 'S2', 'S3', 'S4']
    vals = [0.4, 0.3, 0.2, 0.1]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute weight')

    ax.set_title('Ch21 residual: standardization weights define absolute target', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch21_std_weights.png')


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1.0])
    ax.plot(x, [0, 1, 3, 6, 10, 15], 'o-', color=TEAL, lw=2.3, label='Overdx abs %')
    ax.plot(x, [0, 0.5, 1.2, 2.0, 2.5, 2.8], 's--', color=CORAL, lw=2.2, label='Mortality benefit abs %')
    ax.set_xlabel('Screen intensity'); ax.set_ylabel('Absolute %')

    ax.set_title('Ch22 residual: absolute overdiagnosis rate vs intensity', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch22_overdx_rate.png')


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(4)
    ax.bar(x-0.2, [1, 5, 20, 50], width=0.4, color=TEAL, edgecolor=INDIGO, label='True prior %')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [20, 45, 70, 85], width=0.4, color=CORAL, edgecolor=INDIGO, label='Felt posterior %')
    ax.set_xticks(x); ax.set_xticklabels(['1%', '5%', '20%', '50%'])
    ax.set_ylabel('Prior'); ax2.set_ylabel('Felt')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch23 residual: base-rate neglect distorts absolute post-test', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch23_base_neglect.png')


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0.5, 1, 2, 3, 5])
    ax.plot(x, [0.5, 1.5, 3, 4, 4.5], 'o-', color=TEAL, lw=2.3, label='Benefit abs pp')
    ax.plot(x, [1.2, 1.5, 2, 2.5, 3.5], 's--', color=CORAL, lw=2.2, label='Harm abs pp')
    ax.set_xlabel('Years'); ax.set_ylabel('Absolute pp')

    ax.set_title('Ch24 residual: absolute net benefit by horizon', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch24_net_horizon.png')


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 10, 20, 30, 40, 50])
    ax.plot(x, [0, 10, 20, 30, 40, 50], 'o-', color=TEAL, lw=2.3, label='Ideal')
    ax.plot(x, [0, 8, 15, 22, 30, 42], 's--', color=CORAL, lw=2.2, label='Observed')
    ax.set_xlabel('Predicted abs %'); ax.set_ylabel('Observed abs %')

    ax.set_title('Ch25 residual: absolute calibration slope for prognosis', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch25_cal_slope.png')


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.linspace(0.05, 0.45, 80)
    y = 0.07-0.5*(x-0.15)**2
    ax.plot(x, y, color=INDIGO, lw=2.5)
    ax.fill_between(x, y, color=TEAL, alpha=0.15)
    ax.set_xlabel('Threshold'); ax.set_ylabel('Net benefit')

    ax.set_title('Ch26 residual: CPR absolute net benefit vs thresholds', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch26_cpr_nb.png')


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 5, 10, 20, 30, 40])
    ax.plot(x, [5, 5, 5, 5, 5, 5], 'o-', color=TEAL, lw=2.3, label='Point ARR')
    ax.plot(x, [5, 4.2, 3.5, 2.0, 0.5, -1.0], 's--', color=CORAL, lw=2.2, label='Lower abs bound')
    ax.set_xlabel('Missing %'); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch27 residual: missingness bounds absolute ARR', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch27_miss_arr.png')


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['A', 'B', 'C', 'D']
    vals = [45, 60, 85, 110]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Door-to-needle minutes')

    ax.set_title('Ch28 residual: absolute D2N equity gap by stratum', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle50_swarm_ch28_d2n_equity.png')


def main():
    print("Cycle-50 →", OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
