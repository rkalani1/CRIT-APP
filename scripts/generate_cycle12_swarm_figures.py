#!/usr/bin/env python3
"""CRIT-APP Cycle-12 densify: clear remaining floor-8 chapters to min 9.

ch02 F&T-first absolute extraction
ch03 intercurrent event absolute estimand
ch10 GRADE absolute certainty ladder
ch14 leakage absolute performance lie
ch19 multiplicity absolute false discovery
ch24 evidence memo absolute fields
ch26 CPR impact absolute outcomes

Agg indigo only. Overwrites cycle12_swarm_* only.
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
OUT.mkdir(parents=True, exist_ok=True)
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"
GREEN, BLUE, ORANGE, PURPLE, GRAY = "#2E7D32", "#1565C0", "#EF6C00", "#6A1B9A", "#90A4AE"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig); print("  wrote", p.name); return p

def fig_ch02():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.1))
    ax = axes[0]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("F&T-first absolute extraction order", fontsize=10, fontweight="bold", color=INDIGO)
    for y, edge, t, b in [(7.6,GOLD,"Table 1","Baseline risks / CER proxies"),(5.5,TEAL,"Table 2 outcomes","Event counts → ARR"),(3.4,CORAL,"Figure KM/forest","Horizon absolute gaps"),(1.3,PURPLE,"Abstract last","Only after absolute ledger")]:
        ax.add_patch(FancyBboxPatch((0.4,y-0.7),9.2,1.7,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor=WHITE,edgecolor=edge,lw=1.4))
        ax.text(0.7,y+0.35,t,fontsize=9,fontweight="bold",color=edge); ax.text(0.7,y-0.3,b,fontsize=8.2,color=SLATE)
    ax=axes[1]
    ax.bar([0,1],[25,90],color=[CORAL,TEAL],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(["Abstract-first","F&T absolute-first"],fontsize=9)
    ax.set_ylabel("% correct ARR computed (synthetic)"); ax.set_ylim(0,100)
    ax.set_title("Order changes arithmetic honesty", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    fig.suptitle("Time-pressure reading: figures & tables first for absolute effects (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch02_ft_absolute.png")

def fig_ch03():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]
    labs=["Treatment\npolicy ARR","Hypothetical\n(no rescue)","Composite\nwith death"]
    vals=[3.0,6.5,4.5]
    ax.bar(range(3),vals,color=[TEAL,GOLD,CORAL],edgecolor=INDIGO,width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs,fontsize=8.5)
    ax.set_ylabel("ARR (pp)"); ax.set_title("Intercurrent-event strategy changes absolute",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    ax=axes[1]; ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Estimand sentence must name strategy",fontsize=10,fontweight="bold",color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.5,2),9,6,boxstyle="round,pad=0.05,rounding_size=0.1",facecolor="#FFF8E1",edgecolor=GOLD,lw=1.4))
    ax.text(5,5.5,"Population · A vs C · Y@horizon\n· intercurrent strategy · ARR summary",ha="center",va="center",fontsize=10,color=SLATE,fontweight="bold")
    ax.text(5,3.2,"Mismatch abstract vs methods = spin",ha="center",fontsize=9,color=CORAL)
    fig.suptitle("Estimands: intercurrent events rewrite absolute contrasts (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch03_intercurrent_arr.png")

def fig_ch10():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]
    levels=["High","Moderate","Low","Very low"]
    # certainty down as bias/imprecision
    ax.barh(range(4),[4,3,2,1],color=[TEAL,GOLD,ORANGE,CORAL],edgecolor=INDIGO)
    ax.set_yticks(range(4)); ax.set_yticklabels(levels,fontsize=9)
    ax.set_xlabel("Certainty grade (schematic)"); ax.set_title("GRADE ladder (absolute outcomes)",fontsize=10,fontweight="bold",color=INDIGO)
    ax=axes[1]
    ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Absolute certainty language",fontsize=10,fontweight="bold",color=INDIGO)
    for y,edge,t,b in [(7.2,TEAL,"High","ARR 3–5 pp almost certain"),(5.0,GOLD,"Moderate","ARR likely; CI may include small"),(2.8,ORANGE,"Low","ARR uncertain; do not rewrite"),(0.6,CORAL,"Very low","Absolute effect unknown")]:
        ax.add_patch(FancyBboxPatch((0.4,y-0.7),9.2,1.65,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor=WHITE,edgecolor=edge,lw=1.3))
        ax.text(0.7,y+0.3,t,fontsize=9,fontweight="bold",color=edge); ax.text(0.7,y-0.3,b,fontsize=8.2,color=SLATE)
    fig.suptitle("Guidelines & synthesis: GRADE talks absolute outcomes (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch10_grade_abs.png")

def fig_ch14():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]
    labs=["Leaked\ntest AUROC","Clean\nholdout","External\nsite"]
    vals=[0.97,0.84,0.71]
    ax.bar(range(3),vals,color=[CORAL,GOLD,TEAL],edgecolor=INDIGO,width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs,fontsize=9)
    ax.set_ylabel("AUROC"); ax.set_ylim(0.5,1.05)
    ax.set_title("Leakage invents discrimination",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    ax=axes[1]
    labs2=["Claimed\nPPV","Local true\nPPV"]
    ax.bar([0,1],[0.85,0.32],color=[GOLD,CORAL],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(labs2,fontsize=9)
    ax.set_ylabel("PPV"); ax.set_title("Absolute PPV collapses after honesty",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    fig.suptitle("AI appraisal: leakage and transport break absolute PPV (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch14_leakage_ppv.png")

def fig_ch19():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]
    k=np.arange(1,21)
    # expected false positives at alpha 0.05 if all null
    ax.plot(k,k*0.05,"o-",color=CORAL,lw=2)
    ax.set_xlabel("Independent tests (all null)"); ax.set_ylabel("Expected false positives")
    ax.set_title("Multiplicity multiplies absolute false claims",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3)
    ax=axes[1]
    ax.bar([0,1,2],[1,5,12],color=[TEAL,GOLD,CORAL],edgecolor=INDIGO,width=0.6)
    ax.set_xticks([0,1,2]); ax.set_xticklabels(["Primary\nonly","+5 secondaries","+20 post-hoc"],fontsize=8.5)
    ax.set_ylabel("Claimed 'significant' findings (synthetic)")
    ax.set_title("Without correction, absolute noise rises",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    fig.suptitle("Inference: multiplicity creates absolute false discoveries (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch19_multiplicity.png")

def fig_ch24():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]; ax.set_xlim(0,10); ax.set_ylim(0,10); ax.axis("off")
    ax.set_title("Evidence memo absolute fields",fontsize=10,fontweight="bold",color=INDIGO)
    for y,edge,t,b in [(7.6,INDIGO,"PICO/t0","One sentence"),(5.6,GOLD,"ARR CI / ARI CI","Same horizon"),(3.6,TEAL,"NNT / NNH","Net absolute"),(1.6,PURPLE,"Action","Adopt/Adapt/Wait/Reject")]:
        ax.add_patch(FancyBboxPatch((0.4,y-0.7),9.2,1.65,boxstyle="round,pad=0.04,rounding_size=0.08",facecolor=WHITE,edgecolor=edge,lw=1.35))
        ax.text(0.7,y+0.3,t,fontsize=9,fontweight="bold",color=edge); ax.text(0.7,y-0.3,b,fontsize=8.2,color=SLATE)
    ax=axes[1]
    ax.bar([0,1],[35,92],color=[CORAL,TEAL],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(["Narrative\nmemo","Absolute\nfields filled"],fontsize=9)
    ax.set_ylabel("Committee decision quality (synthetic)"); ax.set_ylim(0,100)
    ax.set_title("Forms beat rhetoric",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    fig.suptitle("Therapy & harm: evidence memo absolute fields (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch24_evidence_memo.png")

def fig_ch26():
    fig, axes = plt.subplots(1,2,figsize=(10.8,5.1))
    ax=axes[0]
    labs=["Derivation\nonly","External\nvalid","Impact\ntrial"]
    # operational value
    vals=[20,55,90]
    ax.bar(range(3),vals,color=[CORAL,GOLD,TEAL],edgecolor=INDIGO,width=0.6)
    ax.set_xticks(range(3)); ax.set_xticklabels(labs,fontsize=9)
    ax.set_ylabel("Trust for pathway use (synthetic)"); ax.set_ylim(0,100)
    ax.set_title("CPR maturity ladder",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    ax=axes[1]
    labs2=["Process\nchange only","Patient-outcome\nARR"]
    ax.bar([0,1],[1,0],color=[GOLD,TEAL],edgecolor=INDIGO,width=0.55)
    ax.set_xticks([0,1]); ax.set_xticklabels(labs2,fontsize=9)
    ax.set_ylabel("Demonstrated absolute patient benefit")
    ax.set_title("Impact analysis must move outcomes",fontsize=10,fontweight="bold",color=INDIGO)
    ax.grid(True,axis="y",alpha=0.3)
    ax.text(0.5,0.85,"Many CPRs change ordering without ARR benefit",ha="center",fontsize=8,color=PURPLE,style="italic")
    fig.suptitle("SR & CPR: impact requires absolute patient outcomes (synthetic)",fontsize=11,fontweight="bold",color=INDIGO,y=1.01)
    fig.tight_layout(); return _save(fig,"cycle12_swarm_ch26_cpr_impact.png")

def main():
    print("Cycle-12 →", OUT)
    for fn in [fig_ch02, fig_ch03, fig_ch10, fig_ch14, fig_ch19, fig_ch24, fig_ch26]:
        fn()
    print("Done: 7")
if __name__ == "__main__":
    main()
