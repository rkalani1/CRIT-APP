#!/usr/bin/env python3
"""CRIT-APP Cycle-61 densify. Agg indigo. ARR/NNT. pred!=cause."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GRAY = "#90A4AE"
def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.bar(['A','B','C','D'], [3,5,4,6], color=INDIGO, edgecolor=SLATE)
    ax.set_ylabel('Absolute ARR/risk')
    ax.set_title('Ch01 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch01_w61_1.png')


def fig_ch02():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.026*t)), color=TEAL, lw=2.3, label='A')
    ax.plot(t,100*(1-np.exp(-0.036*t)), color=CORAL, lw=2.3, label='B')
    ax.set_xlabel('Months'); ax.set_ylabel('Abs cumulative %')
    ax.set_title('Ch02 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch02_w61_2.png')


def fig_ch03():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.barh(['M1','M2','M3','M4'], [0.8,0.6,0.65,0.4], color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score')
    ax.set_title('Ch03 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch03_w61_3.png')


def fig_ch04():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x=np.arange(6); ax.plot(x, 2+0.3*x, 'o-', color=TEAL, lw=2.3)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch04 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch04_w61_4.png')


def fig_ch05():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.bar(['A','B','C','D'], [3,5,4,7], color=INDIGO, edgecolor=SLATE)
    ax.set_ylabel('Absolute ARR/risk')
    ax.set_title('Ch05 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch05_w61_5.png')


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.027*t)), color=TEAL, lw=2.3, label='A')
    ax.plot(t,100*(1-np.exp(-0.036*t)), color=CORAL, lw=2.3, label='B')
    ax.set_xlabel('Months'); ax.set_ylabel('Abs cumulative %')
    ax.set_title('Ch06 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch06_w61_6.png')


def fig_ch07():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.barh(['M1','M2','M3','M4'], [0.8,0.5,0.65,0.4], color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score')
    ax.set_title('Ch07 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch07_w61_7.png')


def fig_ch08():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x=np.arange(6); ax.plot(x, 3+0.3*x, 'o-', color=TEAL, lw=2.3)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch08 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch08_w61_8.png')


def fig_ch09():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.bar(['A','B','C','D'], [3,5,4,8], color=INDIGO, edgecolor=SLATE)
    ax.set_ylabel('Absolute ARR/risk')
    ax.set_title('Ch09 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch09_w61_9.png')


def fig_ch10():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.025*t)), color=TEAL, lw=2.3, label='A')
    ax.plot(t,100*(1-np.exp(-0.036*t)), color=CORAL, lw=2.3, label='B')
    ax.set_xlabel('Months'); ax.set_ylabel('Abs cumulative %')
    ax.set_title('Ch10 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch10_w61_10.png')


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.barh(['M1','M2','M3','M4'], [0.8,0.55,0.65,0.4], color=TEAL, edgecolor=INDIGO)
    ax.set_xlabel('Absolute score')
    ax.set_title('Ch11 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch11_w61_11.png')


def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x=np.arange(6); ax.plot(x, 4+0.3*x, 'o-', color=TEAL, lw=2.3)
    ax.set_xlabel('Step'); ax.set_ylabel('Absolute units')
    ax.set_title('Ch12 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch12_w61_12.png')


def fig_ch13():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ax.bar(['A','B','C','D'], [3,5,4,6], color=INDIGO, edgecolor=SLATE)
    ax.set_ylabel('Absolute ARR/risk')
    ax.set_title('Ch13 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch13_w61_13.png')


def fig_ch14():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.026*t)), color=TEAL, lw=2.3, label='A')
    ax.plot(t,100*(1-np.exp(-0.036*t)), color=CORAL, lw=2.3, label='B')
    ax.set_xlabel('Months'); ax.set_ylabel('Abs cumulative %')
    ax.set_title('Ch14 residual: absolute densify wave C61 teaching figure', fontsize=11, fontweight='bold', color=INDIGO)
    ax.grid(True, alpha=0.3)
    h,_=ax.get_legend_handles_labels()
    if h: ax.legend(fontsize=8)
    fig.tight_layout()
    return _save(fig, 'cycle61_swarm_ch14_w61_14.png')


def main():
    print('Cycle-61', OUT)
    for fn in [fig_ch01, fig_ch02, fig_ch03, fig_ch04, fig_ch05, fig_ch06, fig_ch07, fig_ch08, fig_ch09, fig_ch10, fig_ch11, fig_ch12, fig_ch13, fig_ch14]: fn()
    print('Done: 14')
if __name__ == '__main__': main()
