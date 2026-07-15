#!/usr/bin/env python3
"""CRIT-APP Cycle-51 densify: ch01-14 toward floor. Agg indigo. ARR/NNT. pred≠cause."""
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

    x = np.array([2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])
    ax.plot(x, [100, 120, 150, 180, 220, 260, 310, 360], 'o-', color=TEAL, lw=2.3, label='Papers')
    ax.plot(x, [20, 22, 24, 26, 28, 30, 32, 34], 's--', color=CORAL, lw=2.2, label='ARR-vetted')
    ax.set_xlabel('Year'); ax.set_ylabel('Count')

    ax.set_title('Ch01 residual: literature growth vs absolute-vetting capacity', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch01_lit_vs_vet.png')


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['No stop', 'ARR stop', 'Bias stop', 'Both']
    vals = [40, 22, 25, 15]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Hours sunk per 100 papers')

    ax.set_title('Ch02 residual: early absolute stop saves reader hours', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch02_stop_value.png')


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Policy', 'WoT', 'Hyp', 'Composite']
    vals = [3.2, 4.5, 5.8, 2.8]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch03 residual: ICE strategies rewrite absolute ARR', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch03_ice_arr.png')


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Trial', 'Target young', 'Target old', 'Target severe']
    vals = [5, 3, 8, 10]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute ARR pp')

    ax.set_title('Ch04 residual: absolute transport gap trial vs target', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch04_transport_gap.png')


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.linspace(1, 10, 80)
    y = 1+12/(x+1)
    ax.plot(x, y, color=INDIGO, lw=2.5)
    ax.fill_between(x, y, color=TEAL, alpha=0.15)
    ax.set_xlabel('Observed ARR pp'); ax.set_ylabel('Confounder strength units')

    ax.set_title('Ch05 residual: small absolute ARR needs strong confounding to null', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch05_evalue_abs.png')


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['Adequate', 'Unclear', 'Inadequate']
    vals = [0, 1.5, 3.0]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Absolute ARR inflation pp')

    ax.set_title('Ch06 residual: concealment failure absolute inflation', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch06_conceal_bias.png')


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    ax.plot(x, [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 'o-', color=TEAL, lw=2.3, label='True abs rate')
    ax.plot(x, [0.4, 0.4, 0.4, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2], 's--', color=CORAL, lw=2.2, label='Biased with immortal')
    ax.set_xlabel('Month'); ax.set_ylabel('Rate /100py')

    ax.set_title('Ch07 residual: immortal time absolute rate dip', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch07_immortal.png')


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100])
    ax.plot(x, [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 'o-', color=TEAL, lw=2.3, label='Treat decision')
    ax.plot(x, [0, 0, 0, 0, 0, 0, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100, 100], 's--', color=CORAL, lw=2.2, label='ref')
    ax.set_xlabel('Post-test abs %'); ax.set_ylabel('Treat 0/100')

    ax.set_title('Ch08 residual: absolute treat threshold as step function', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch08_treat_thresh.png')


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(10)
    ax.bar(x-0.2, [0.72, 0.75, 0.78, 0.81, 0.84, 0.86, 0.88, 0.9, 0.91, 0.92], width=0.4, color=TEAL, edgecolor=INDIGO, label='AUROC')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [0.5, 0.8, 1.2, 1.8, 2.5, 3.5, 4.8, 6.5, 8.5, 11], width=0.4, color=CORAL, edgecolor=INDIGO, label='Abs cal err pp')
    ax.set_xticks(x); ax.set_xticklabels(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'])
    ax.set_ylabel('AUROC'); ax2.set_ylabel('Cal err')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch09 residual: pred≠cause — complexity raises abs cal error', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch09_overfit_cal.png')


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    np.random.seed(5110)
    arr = np.linspace(-1, 8, 30)
    spin = 2 + 0.3*arr + np.random.randn(30)*0.8
    ax.scatter(arr, spin, c=CORAL, edgecolors=INDIGO, s=60)
    ax.axvline(0, color=TEAL, ls='--', label='Null ARR')
    ax.set_xlabel('Absolute ARR (pp)'); ax.set_ylabel('Claim intensity')

    ax.set_title('Ch10 residual: absolute funnel asymmetry suggests missing nulls', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch10_funnel_abs.png')


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24])
    ax.plot(x, [0.0, 7.688365361336425, 14.785621103378865, 21.337213893344654, 27.385096292630905, 32.967995396436066, 38.121660819385916, 42.879093615118514, 47.270757595695144, 51.324774404002824, 55.067103588277845, 58.52170883184187, 61.71071140248879], 'o-', color=TEAL, lw=2.3, label='CIF abs %')
    ax.plot(x, [0.0, 8.841620165536888, 17.003464268885693, 24.53779597734635, 31.49286073652554, 37.913194705901475, 43.8399099422938, 49.31095765738629, 54.36137123504941, 59.02349056460324, 63.327169126519514, 67.29996515661814, 70.9673181128621], 's--', color=CORAL, lw=2.2, label='Naive 1-KM %')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute %')

    ax.set_title('Ch11 residual: naive 1-KM overstates absolute CIF', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch11_cif_vs_km.png')


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    labels = ['<MID', '=MID', '>MID']
    vals = [0.2, 0.5, 0.9]
    colors = [TEAL if i%2==0 else INDIGO for i in range(len(vals))]
    ax.bar(labels, vals, color=colors, edgecolor=SLATE)
    ax.set_xlabel(''); ax.set_ylabel('Discuss probability')

    ax.set_title('Ch12 residual: MID is absolute threshold not p-value', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch12_mid_abs.png')


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.arange(2)
    ax.bar(x-0.2, [3.0, 3.1], width=0.4, color=TEAL, edgecolor=INDIGO, label='ARR B−')
    ax2 = ax.twinx()
    ax2.bar(x+0.2, [3.2, 7.5], width=0.4, color=CORAL, edgecolor=INDIGO, label='ARR B+')
    ax.set_xticks(x); ax.set_xticklabels(['Mod−', 'Mod+'])
    ax.set_ylabel('ARR'); ax2.set_ylabel('ARR')
    ax.legend(loc='upper left', fontsize=8); ax2.legend(loc='upper right', fontsize=8)

    ax.set_title('Ch13 residual: absolute interaction plot for HTE', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch13_abs_interact.png')


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))

    x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
    ax.plot(x, [0.12, 0.11, 0.09999999999999999, 0.09, 0.07999999999999999, 0.06999999999999999, 0.06, 0.04999999999999999, 0.039999999999999994, 0.03, 0.01999999999999999, 0.009999999999999995], 'o-', color=TEAL, lw=2.3, label='Abs net benefit')
    ax.plot(x, [0.85, 0.842, 0.834, 0.826, 0.818, 0.8099999999999999, 0.8019999999999999, 0.7939999999999999, 0.786, 0.778, 0.77, 0.762], 's--', color=CORAL, lw=2.2, label='AUROC')
    ax.set_xlabel('Month'); ax.set_ylabel('Value')

    ax.set_title('Ch14 residual: dataset shift erases absolute net benefit first', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    if ax.get_legend_handles_labels()[0]:
        ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle51_swarm_ch14_dataset_shift.png')


def main():
    print("Cycle-51 →", OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
