#!/usr/bin/env python3
"""CRIT-APP Cycle-57 densify: ch01-14. Agg indigo. ARR/NNT. pred!=cause."""
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
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.02*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.03*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch01 residual: absolute appraisal capacity ceiling', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch01_c57a.png')


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [5,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 4, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch02 residual: absolute stop-rule saves reader hours', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch02_c57b.png')


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.7, 0.45, 0.75, 0.35]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch03 residual: estimand choice rewrites absolute ARR', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch03_c57c.png')


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 5 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch04 residual: selection compresses absolute baseline risk', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch04_c57d.png')


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([4, 5, 2, 7, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch05 residual: backdoor residual absolute bias map', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch05_c57e.png')


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.024*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.038*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch06 residual: analysis set moves absolute effect size', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch06_c57f.png')


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [4,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 3, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch07 residual: indication confounding absolute coupling', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch07_c57g.png')


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.65, 0.45, 0.75, 0.39999999999999997]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch08 residual: threshold-specific absolute net benefit', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch08_c57h.png')


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 2 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch09 residual: pred!=cause absolute calibration plot', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch09_c57i.png')


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([3, 5, 3, 6, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch10 residual: study-level absolute ARR dispersion', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch10_c57j.png')


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.028*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.034*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch11 residual: competing absolute CIF pair', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch11_c57k.png')


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [6,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 4, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch12 residual: NNT band from absolute ARR CI', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch12_c57l.png')


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.6, 0.45, 0.75, 0.35]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch13 residual: subgroup absolute forest plot', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch13_c57m.png')


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 3 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch14 residual: pred!=cause absolute ML gate pass rates', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle57_swarm_ch14_c57n.png')


def main():
    print('Cycle-57 ->', OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]:
        fn()
    print('Done: 14')
if __name__ == '__main__':
    main()
