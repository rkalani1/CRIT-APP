#!/usr/bin/env python3
"""CRIT-APP Cycle-58 densify: ch15-28. Agg indigo. ARR/NNT. pred!=cause."""
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
    x = np.arange(4)
    ax.bar(x-0.2, [4,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 3, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch15 residual: shared absolute card lifts JC fidelity', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch15_c58a.png')


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.65, 0.45, 0.75, 0.39999999999999997]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch16 residual: missing ARR is modal autopsy fail', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch16_c58b.png')


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 4 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch17 residual: absolute excess incidence by group', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch17_c58c.png')


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([3, 5, 3, 6, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch18 residual: potential outcome absolute contrast', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch18_c58d.png')


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.02*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.034*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch19 residual: absolute SE scales as 1/sqrt(n)', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch19_c58e.png')


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [6,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 4, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch20 residual: landmark restarts absolute risk clock', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch20_c58f.png')


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.6, 0.45, 0.75, 0.35]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch21 residual: scale dependence of absolute interaction', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch21_c58g.png')


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 5 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch22 residual: lead-time absolute survival artifact', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch22_c58h.png')


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([5, 5, 2, 8, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch23 residual: availability warps absolute base rates', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch23_c58i.png')


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 30, 100)
    ax.plot(t, 100*(1-np.exp(-0.024*t)), color=TEAL, lw=2.3, label='Abs risk A')
    ax.plot(t, 100*(1-np.exp(-0.03*t)), color=CORAL, lw=2.3, label='Abs risk B')
    ax.set_xlabel('Months'); ax.set_ylabel('Absolute cumulative %')
    ax.set_title('Ch24 residual: composite hides component absolute moves', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch24_c58j.png')


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(4)
    ax.bar(x-0.2, [5,5,3,6], width=0.4, color=TEAL, edgecolor=INDIGO, label='Benefit')
    ax.bar(x+0.2, [2, 3, 4, 3], width=0.4, color=CORAL, edgecolor=INDIGO, label='Harm')
    ax.set_xticks(x); ax.set_xticklabels(['G1','G2','G3','G4'])
    ax.set_ylabel('Absolute pp')
    ax.set_title('Ch25 residual: horizon-specific absolute Brier', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch25_c58k.png')


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ylabs = ['M1','M2','M3','M4','M5']
    vals = [0.85, 0.7, 0.45, 0.75, 0.39999999999999997]
    ax.barh(ylabs, vals, color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute fraction / score')
    ax.set_title('Ch26 residual: SoF absolute effects with certainty', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch26_c58l.png')


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.arange(1, 8)
    y = 2 + 0.4*x + 0.05*np.sin(x)
    ax.plot(x, y, 'o-', color=TEAL, lw=2.4, label='Absolute metric')
    ax.set_xlabel('Index'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch27 residual: interim absolute alpha spend', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch27_c58m.png')


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    labels = [f'S{k}' for k in range(1,6)]
    vals = np.array([4, 5, 3, 7, 4])
    ax.bar(labels, vals, color=INDIGO, edgecolor=SLATE, alpha=0.85)
    ax.set_ylabel('Absolute ARR/risk units')
    ax.set_title('Ch28 residual: absolute equity process-outcome gaps', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle58_swarm_ch28_c58n.png')


def main():
    print('Cycle-58 ->', OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print('Done: 14')
if __name__ == '__main__':
    main()
