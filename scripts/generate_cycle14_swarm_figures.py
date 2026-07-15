#!/usr/bin/env python3
"""CRIT-APP Cycle-14 densify: residual floor-9 chapters → 10.
ch01 pred≠cause absolute fork; ch06 CONSORT absolute sequence;
ch08 LR nomogram absolute; ch12 NNT CI infinity residual;
ch15 red-flag absolute checklist; ch17 rate vs risk absolute;
ch19 dichotomania absolute CI.
Agg indigo. cycle14_swarm_* only.
"""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig); print("  wrote", p.name); return p

def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.2, 4.8)); ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
    ax.set_title("Prediction vs causation absolute fork", fontsize=11, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((3.5,4.2),3,1.3,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor=WHITE,edgecolor=INDIGO,lw=1.5))
    ax.text(5,4.85,"High risk / strong association",ha="center",fontsize=9,fontweight="bold",color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.3,0.6),4.2,2.8,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor="#FFEBEE",edgecolor=CORAL,lw=1.5))
    ax.text(2.4,2.2,"Misread\n‘Treat because high risk’\nNeeds causal ARR",ha="center",fontsize=9,fontweight="bold",color=CORAL)
    ax.add_patch(FancyBboxPatch((5.5,0.6),4.2,2.8,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor="#E8F5E9",edgecolor=TEAL,lw=1.5))
    ax.text(7.6,2.2,"Correct\nCounsel absolute risk\nCausal claim needs TTE/RCT",ha="center",fontsize=9,fontweight="bold",color=TEAL)
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch01_pred_cause.png")

def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.2, 4.8)); ax.set_xlim(0,10); ax.set_ylim(0,8); ax.axis("off")
    ax.set_title("CONSORT-minded sequence ends on absolute quantitation", fontsize=11, fontweight="bold", color=INDIGO)
    steps = [(6.5,INDIGO,"1 Population"),(5.1,BLUE,"2 Assignment"),(3.7,GOLD,"3 Strategies"),(2.3,CORAL,"4 Blinding"),(0.9,TEAL,"5 Absolute RD/NNT")]
    for y,e,t in steps:
        ax.add_patch(FancyBboxPatch((0.5,y-0.5),9,1.2,boxstyle="round,pad=0.03,rounding_size=0.07",facecolor=WHITE,edgecolor=e,lw=1.4))
        ax.text(1,y+0.1,t,fontsize=10,fontweight="bold",color=e,va="center")
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch06_consort_abs.png")

def fig_ch08():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.0))
    ax=axes[0]
    prior=np.linspace(0.02,0.6,80); lr=5.0
    odds=prior/(1-prior); post=(odds*lr)/(1+odds*lr)
    ax.plot(prior*100, post*100, color=INDIGO, lw=2.5)
    ax.set_xlabel("Pre-test %"); ax.set_ylabel("Post-test % (LR+=5)")
    ax.set_title("Absolute Bayesian update", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    ax=axes[1]
    ax.bar([0,1,2],[20,56,5],color=[GRAY,CORAL,TEAL],edgecolor=INDIGO,width=0.6)
    ax.set_xticks([0,1,2]); ax.set_xticklabels(["Pre-test","Post if +","Post if −"],fontsize=9)
    ax.set_ylabel("%"); ax.set_title("Natural frequency endpoint (prior 20%, LR±)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Diagnostic LRs move absolute post-test probability (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch08_lr_post.png")

def fig_ch12():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    # NNT as function of ARR; explode near 0
    arr = np.linspace(0.5, 8, 50)
    nnt = 100/arr
    ax.plot(arr, nnt, color=INDIGO, lw=2.5)
    ax.axvline(0, color=CORAL, lw=1)
    ax.fill_between([0,0.5], 0, 250, color=CORAL, alpha=0.12)
    ax.text(0.6, 200, "ARR CI→0 ⇒ NNT→∞", color=CORAL, fontsize=10, fontweight="bold")
    ax.set_xlabel("ARR (pp)"); ax.set_ylabel("NNT"); ax.set_ylim(0,250); ax.set_xlim(0,8)
    ax.set_title("NNT explodes as absolute effect approaches null", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3)
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch12_nnt_explode.png")

def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.2, 5.0)); ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Red-flag super-checklist: absolute stops", fontsize=11, fontweight="bold", color=INDIGO)
    for i,(y,e,t) in enumerate([(8,CORAL,"No CER/EER disclosed"),(6.2,ORANGE,"Primary only relative"),(4.4,GOLD,"Harm ARI missing"),(2.6,PURPLE,"t0 / analysis set shopped"),(0.8,TEAL,"Action without NNT horizon")]):
        ax.add_patch(FancyBboxPatch((0.4,y-0.6),9.2,1.4,boxstyle="round,pad=0.03,rounding_size=0.07",facecolor=WHITE,edgecolor=e,lw=1.4))
        ax.text(0.8,y+0.1,f"STOP {i+1}: {t}",fontsize=10,fontweight="bold",color=e,va="center")
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch15_redflag_abs.png")

def fig_ch17():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.0))
    ax=axes[0]
    ax.bar([0,1],[10,5],color=[TEAL,CORAL],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(["Risk\n(cumulative %)", "Rate\n(/100 py)"],fontsize=9)
    ax.set_title("Risk ≠ rate (absolute units)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    ax=axes[1]; ax.set_xlim(0,10); ax.set_ylim(0,6); ax.axis("off")
    ax.add_patch(FancyBboxPatch((0.5,1),9,4,boxstyle="round,pad=0.05,rounding_size=0.1",facecolor="#FFF8E1",edgecolor=GOLD,lw=1.4))
    ax.text(5,3.5,"Risk: events / people over fixed horizon\nRate: events / person-time\nNNT needs risk (ARR), not crude rate alone",ha="center",va="center",fontsize=10,color=SLATE)
    fig.suptitle("Frequency literacy: absolute risk vs rate for decisions (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.01)
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch17_risk_rate.png")

def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.2, 4.8))
    # four CIs
    studies = [(3,1,5,"sig+important"),(2,-1,5,"nonsig imprecise"),(0.3,0.1,0.5,"sig tiny"),(1,-2,4,"harm possible")]
    for i,(pt,lo,hi,lab) in enumerate(studies):
        y=3.5-i*0.9
        col=[TEAL,GOLD,ORANGE,CORAL][i]
        ax.plot([lo,hi],[y,y],color=col,lw=4,solid_capstyle="round")
        ax.plot(pt,y,"o",color=col,ms=9)
        ax.text(5.5,y,lab,va="center",fontsize=9,color=col,fontweight="bold")
    ax.axvline(0,color=GRAY,lw=1.2); ax.axvline(2,color=GOLD,ls="--",lw=1.2)
    ax.text(2,4.2,"MCID",color=GOLD,fontsize=8)
    ax.set_xlim(-3,8); ax.set_ylim(0,4.5); ax.set_yticks([]); ax.set_xlabel("ARR (pp)")
    ax.set_title("Dichotomania fails: four absolute CI stories", fontsize=11, fontweight="bold", color=INDIGO)
    for s in ("top","right","left"): ax.spines[s].set_visible(False)
    fig.tight_layout(); return _save(fig, "cycle14_swarm_ch19_dichotomania.png")

def main():
    print("Cycle-14 →", OUT)
    for fn in [fig_ch01, fig_ch06, fig_ch08, fig_ch12, fig_ch15, fig_ch17, fig_ch19]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
