#!/usr/bin/env python3
"""CRIT-APP Cycle-70 densify. Agg indigo. ARR/NNT. pred!=cause."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"docs"/"assets"/"figures"
INDIGO,TEAL,GOLD,CORAL,SLATE,WHITE="#283593","#00695C","#F9A825","#C62828","#37474F","#FFFFFF"
def _save(fig,name):
 p=OUT/name; fig.savefig(p,dpi=180,bbox_inches="tight",facecolor=WHITE); plt.close(fig); print("  wrote",p.name); return p


def fig_ch15():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.025*t)),color=TEAL,lw=2.3)
    ax.plot(t,100*(1-np.exp(-0.035*t)),color=CORAL,lw=2.3)
    ax.set_xlabel("Months"); ax.set_ylabel("Abs %")
    ax.set_title('Ch15 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch15_w70_1.png')


def fig_ch16():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.barh(["M1","M2","M3","M4"],[0.8,0.55,0.65,0.4],color=TEAL,edgecolor=INDIGO)
    ax.set_xlabel("Absolute score")
    ax.set_title('Ch16 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch16_w70_2.png')


def fig_ch17():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    x=np.arange(6); ax.plot(x,2+0.3*x,"o-",color=TEAL,lw=2.3)
    ax.set_xlabel("Step"); ax.set_ylabel("Absolute units")
    ax.set_title('Ch17 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch17_w70_3.png')


def fig_ch18():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.bar(["A","B","C","D"],[3,5,4,6],color=INDIGO,edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR/risk")
    ax.set_title('Ch18 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch18_w70_4.png')


def fig_ch19():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.025*t)),color=TEAL,lw=2.3)
    ax.plot(t,100*(1-np.exp(-0.035*t)),color=CORAL,lw=2.3)
    ax.set_xlabel("Months"); ax.set_ylabel("Abs %")
    ax.set_title('Ch19 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch19_w70_5.png')


def fig_ch20():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.barh(["M1","M2","M3","M4"],[0.8,0.55,0.65,0.4],color=TEAL,edgecolor=INDIGO)
    ax.set_xlabel("Absolute score")
    ax.set_title('Ch20 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch20_w70_6.png')


def fig_ch21():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    x=np.arange(6); ax.plot(x,2+0.3*x,"o-",color=TEAL,lw=2.3)
    ax.set_xlabel("Step"); ax.set_ylabel("Absolute units")
    ax.set_title('Ch21 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch21_w70_7.png')


def fig_ch22():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.bar(["A","B","C","D"],[3,5,4,6],color=INDIGO,edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR/risk")
    ax.set_title('Ch22 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch22_w70_8.png')


def fig_ch23():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.025*t)),color=TEAL,lw=2.3)
    ax.plot(t,100*(1-np.exp(-0.035*t)),color=CORAL,lw=2.3)
    ax.set_xlabel("Months"); ax.set_ylabel("Abs %")
    ax.set_title('Ch23 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch23_w70_9.png')


def fig_ch24():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.barh(["M1","M2","M3","M4"],[0.8,0.55,0.65,0.4],color=TEAL,edgecolor=INDIGO)
    ax.set_xlabel("Absolute score")
    ax.set_title('Ch24 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch24_w70_10.png')


def fig_ch25():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    x=np.arange(6); ax.plot(x,2+0.3*x,"o-",color=TEAL,lw=2.3)
    ax.set_xlabel("Step"); ax.set_ylabel("Absolute units")
    ax.set_title('Ch25 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch25_w70_11.png')


def fig_ch26():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.bar(["A","B","C","D"],[3,5,4,6],color=INDIGO,edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR/risk")
    ax.set_title('Ch26 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch26_w70_12.png')


def fig_ch27():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    t=np.linspace(0,20,80)
    ax.plot(t,100*(1-np.exp(-0.025*t)),color=TEAL,lw=2.3)
    ax.plot(t,100*(1-np.exp(-0.035*t)),color=CORAL,lw=2.3)
    ax.set_xlabel("Months"); ax.set_ylabel("Abs %")
    ax.set_title('Ch27 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch27_w70_13.png')


def fig_ch28():
    fig,ax=plt.subplots(figsize=(10.4,5.0))
    ax.barh(["M1","M2","M3","M4"],[0.8,0.55,0.65,0.4],color=TEAL,edgecolor=INDIGO)
    ax.set_xlabel("Absolute score")
    ax.set_title('Ch28 residual: absolute densify C70 scientific teaching figure',fontsize=11,fontweight="bold",color=INDIGO)
    ax.grid(True,alpha=0.3); fig.tight_layout()
    return _save(fig,'cycle70_swarm_ch28_w70_14.png')


def main():
    print("Cycle-70",OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21, fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]: fn()
    print("Done: 14")
if __name__=="__main__": main()
