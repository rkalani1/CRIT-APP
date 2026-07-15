#!/usr/bin/env python3
"""CRIT-APP Cycle-60 densify: ch15-28. Agg indigo. ARR/NNT. pred!=cause."""
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
    x = np.arange(1, 8)
    y = 2 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch15 residual: teach-back absolute NNT retention', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch15_c60a.png')


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([4, 5, 3, 7, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch16 residual: red-team absolute stress stages', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch16_c60b.png')


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.028*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.038*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch17 residual: AF% needs absolute rate scale', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch17_c60c.png')


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [4,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 4, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch18 residual: DAG target-trial absolute priority', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch18_c60d.png')


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.65, 0.45, 0.75, 0.35]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch19 residual: sequential absolute type-I growth', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch19_c60e.png')


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 3 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch20 residual: absolute survival difference panel', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch20_c60f.png')


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([3, 5, 2, 6, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch21 residual: absolute RERI beyond additivity', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch21_c60g.png')


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.032*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.034*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch22 residual: length-time absolute indolent mix', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch22_c60h.png')


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [6,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 3, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch23 residual: anchoring absolute estimate pull', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch23_c60i.png')


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.6, 0.45, 0.75, 0.39999999999999997]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch24 residual: surrogate absolute hard-endpoint fail', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch24_c60j.png')


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 4 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch25 residual: diagnostic absolute path yield', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch25_c60k.png')


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([5, 5, 3, 8, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch26 residual: living review absolute ARR updates', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch26_c60l.png')


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.02*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.03*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch27 residual: tipping absolute missing extremes', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch27_c60m.png')


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [5,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 4, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch28 residual: policy absolute outcome-cost board', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle60_swarm_ch28_c60n.png')


def main():
    print('Cycle-60 ->', OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print('Done: 14')
if __name__ == '__main__':
    main()
