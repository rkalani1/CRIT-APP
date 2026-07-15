#!/usr/bin/env python3
"""CRIT-APP Cycle-52 densify: ch15-28 raise floor. Agg indigo. ARR/NNT. pred≠cause."""
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

    labels = ['Chair', 'Methods', 'Stats', 'Clin', 'Scribe']
    vals = [1, 5, 4, 2, 3]
    ax.barh(labels, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('ARR mentions / JC')

    ax.set_title('Ch15 residual: methods role drives absolute ARR mentions', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch15_role_arr.png')


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Q', 'Bias', 'Abs effect', 'Spin', 'Action']
    vals = [1, 2, 4, 2, 3]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Severity 0-4')

    ax.set_title('Ch16 residual: absolute-effect domain highest autopsy severity', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch16_severity_abs.png')


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Ref', 'A', 'B', 'C']
    vals = [0, 0.5, 1.8, 3.2]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute excess /100py')

    ax.set_title('Ch17 residual: absolute excess incidence vs reference', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch17_excess_abs.png')


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Total', 'NDE', 'NIE', 'CDE']
    vals = [5, 3.2, 1.8, 2.9]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute effect pp')

    ax.set_title('Ch18 residual: absolute mediation decomposition', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch18_mediate_abs.png')


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    ax.plot(x, [1.4, 1.568, 1.736, 1.9039999999999997, 2.072, 2.2399999999999998, 2.408, 2.5759999999999996, 2.7439999999999998, 2.912], 'o-', color=TEAL, lw=2.3, label='CI half pp')
    ax.plot(x, [1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4, 1.4], 's--', color=CORAL, lw=2.2, label='Fixed design')
    ax.set_xlabel('Looks'); ax.set_ylabel('pp')

    ax.set_title('Ch19 residual: optional stopping widens absolute CI', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch19_opt_stop.png')


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24])
    ax.plot(x, [0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7, 0.7], 'o-', color=TEAL, lw=2.3, label='HR')
    ax.plot(x, [2.1950000000000003, 2.38, 2.555, 2.7199999999999998, 2.875, 3.02, 3.1550000000000002, 3.2800000000000002, 3.395, 3.5, 3.595, 3.6800000000000006, 3.755, 3.8200000000000007, 3.875, 3.92, 3.955, 3.9799999999999995, 3.995000000000001, 4.0, 3.995, 3.9800000000000004, 3.9550000000000005, 3.920000000000001], 's--', color=CORAL, lw=2.2, label='Abs RD pp')
    ax.set_xlabel('Month'); ax.set_ylabel('Value')

    ax.set_title('Ch20 residual: PH HR flat while absolute RD evolves', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch20_ph_vs_rd.png')


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Low B−', 'Low B+', 'High B−', 'High B+']
    vals = [4, 3, 20, 10]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute risk %')

    ax.set_title('Ch21 residual: absolute interaction with flat RR', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch21_scale_int.png')


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Screen dx age', 'Clin dx age', 'Death age']
    vals = [68, 72, 78]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Age years')

    ax.set_title('Ch22 residual: lead time adds absolute survival time artifact', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch22_lead_abs.png')


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(4)
    ax.bar(x-0.2, [1, 5, 15, 40], width=0.4, color=TEAL, edgecolor=INDIGO, label='True base %')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [12, 18, 25, 45], width=0.4, color=CORAL, edgecolor=INDIGO, label='Remembered %')
    ax.set_xticks(x); ax.set_xticklabels(['1%', '5%', '15%', '40%'])
    ax.set_ylabel('True'); ax2.set_ylabel('Remembered')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch23 residual: availability inflates rare absolute risks', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch23_avail_bias.png')


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(4)
    ax.bar(x-0.2, [8, 25, 2, 30], width=0.4, color=TEAL, edgecolor=INDIGO, label='Control %')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [6, 18, 3, 22], width=0.4, color=CORAL, edgecolor=INDIGO, label='Tx %')
    ax.set_xticks(x); ax.set_xticklabels(['Death', 'mRS>2', 'sICH', 'Comp'])
    ax.set_ylabel('Ctrl'); ax2.set_ylabel('Tx')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch24 residual: composite ARR vs component absolute moves', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch24_comp_parts.png')


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([1, 3, 6, 12, 24])
    ax.plot(x, [0.12, 0.14, 0.16, 0.2, 0.24], 'o-', color=TEAL, lw=2.3, label='Abs Brier')
    ax.plot(x, [0.82, 0.8, 0.78, 0.74, 0.7], 's--', color=CORAL, lw=2.2, label='AUROC')
    ax.set_xlabel('Months'); ax.set_ylabel('Value')

    ax.set_title('Ch25 residual: prognosis absolute Brier worsens with horizon', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch25_horizon_prog.png')


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Death', 'Depend', 'ICH', 'mRS0-2']
    vals = [-1.5, -4.0, 0.8, 5.0]
    ax.barh(labels, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute RD pp')

    ax.set_title('Ch26 residual: SoF absolute risk differences by outcome', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch26_sof_abs.png')


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['L1', 'L2', 'L3', 'Final']
    vals = [0.001, 0.005, 0.01, 0.034]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute alpha')

    ax.set_title('Ch27 residual: absolute alpha spent across looks', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch27_alpha_abs.png')


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(4)
    ax.bar(x-0.2, [22, 30, 38, 42], width=0.4, color=TEAL, edgecolor=INDIGO, label='Good outcome %')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [1, 4, 3, 5], width=0.4, color=CORAL, edgecolor=INDIGO, label='sICH %')
    ax.set_xticks(x); ax.set_xticklabels(['No lytics', 'IV', 'EVT', 'Both'])
    ax.set_ylabel('Good'); ax2.set_ylabel('sICH')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch28 residual: SDM absolute benefit-harm board', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle52_swarm_ch28_sdm_abs.png')


def main():
    print("Cycle-52 →", OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
