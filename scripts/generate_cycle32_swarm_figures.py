#!/usr/bin/env python3
"""CRIT-APP Cycle-32 densify: clear residual floor-15 → uniform floor ≥16 (ch15–28)."""
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

def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    weeks = np.arange(1, 9)
    spin = np.array([5, 4, 4, 3, 2, 2, 1, 1])
    abs_ok = np.array([1, 2, 3, 4, 5, 6, 7, 8])
    ax.plot(weeks, spin, "s--", color=CORAL, lw=2.2, label="Spin incidents")
    ax.plot(weeks, abs_ok, "o-", color=TEAL, lw=2.3, label="Absolute ARR cards completed")
    ax.set_xlabel("JC week"); ax.set_ylabel("Count")
    ax.set_title("JC residual: absolute drills reduce spin incidents over a term", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch15_spin_trend.png")

def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    x = np.array([0.2, 0.4, 0.6, 0.8, 0.9])
    y = np.array([0.9, 0.7, 0.5, 0.35, 0.2])
    ax.plot(x, y, "o-", color=INDIGO, lw=2.4)
    for xi, yi, lab in zip(x, y, ["Reject", "Wait", "Adapt", "Pilot", "Adopt"]):
        ax.text(xi, yi + 0.04, lab, ha="center", fontsize=8, fontweight="bold", color=SLATE)
    ax.set_xlabel("Fatal flaw burden"); ax.set_ylabel("Absolute action confidence")
    ax.set_title("Autopsy residual: absolute action confidence falls with fatal flaw burden", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch16_flaw_action_curve.png")

def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    exposed = np.array([40, 360]); unexp = np.array([30, 570])
    # 2x2 visual
    ax.imshow([[40, 360], [30, 570]], cmap="Blues", aspect="auto")
    for i in range(2):
        for j in range(2):
            ax.text(j, i, [[40, 360], [30, 570]][i][j], ha="center", va="center", fontsize=14, fontweight="bold", color=INDIGO)
    ax.set_xticks([0, 1]); ax.set_xticklabels(["Event+", "Event−"])
    ax.set_yticks([0, 1]); ax.set_yticklabels(["Exposed", "Unexposed"])
    ax.set_title("Association residual: RD=5pp RR=2 OR≈2.11 from absolute cell counts", fontsize=11, fontweight="bold", color=INDIGO)
    fig.tight_layout(); return _save(fig, "cycle32_swarm_ch17_twobytwo.png")

def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    path = ["Association", "Confounding\naddressed", "Temporality", "Dose-\nresponse", "Experiment", "Absolute\nARR"]
    score = [0.3, 0.45, 0.55, 0.6, 0.85, 0.95]
    ax.plot(range(6), score, "o-", color=TEAL, lw=2.5, ms=9)
    ax.set_xticks(range(6)); ax.set_xticklabels(path, fontsize=8)
    ax.set_ylabel("Causal absolute credibility")
    ax.set_title("Causation residual: absolute ARR is the endpoint of causal credibility", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 1.1); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch18_cred_path.png")

def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # compatibility interval visualization
    arr_grid = np.linspace(-2, 10, 100)
    # likelihood ratio vs null ARR=0
    est, se = 4.0, 1.5
    ll = -0.5 * ((arr_grid - est) / se) ** 2
    ll0 = -0.5 * ((0 - est) / se) ** 2
    # relative
    rel = np.exp(ll - ll.max())
    ax.plot(arr_grid, rel, color=INDIGO, lw=2.5)
    ax.axvline(0, color=CORAL, ls="--", label="Null ARR=0")
    ax.axvline(est, color=TEAL, ls="--", label="Point ARR")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("Relative likelihood")
    ax.set_title("Inference residual: likelihood over absolute ARR values", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch19_likelihood_arr.png")

def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # coefficients vs absolute risk difference for binary outcome
    beta = np.linspace(-1, 1, 80)
    # at baseline risk 0.2
    p0 = 0.2
    p1 = 1 / (1 + np.exp(-(np.log(p0 / (1 - p0)) + beta)))
    rd = (p1 - p0) * 100
    ax.plot(beta, rd, color=TEAL, lw=2.5)
    ax.axhline(0, color=GRAY)
    ax.set_xlabel("Log-odds coefficient β"); ax.set_ylabel("Absolute risk difference (pp)")
    ax.set_title("Regression residual: β is not absolute ARR without baseline risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch20_beta_to_rd.png")

def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # additive vs multiplicative scales side plot already; show stratum ARR table as bars
    strata = ["A−B−", "A+B−", "A−B+", "A+B+"]
    risk = [5, 10, 12, 28]
    ax.bar(strata, risk, color=[GRAY, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Interaction residual: joint absolute risks for additive interaction", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch21_joint_risks.png")

def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # disease reservoir: detected vs overdiagnosed
    intensity = np.linspace(0, 1, 40)
    true_prog = 8 + 2 * intensity
    over = 3 + 25 * intensity ** 1.3
    ax.stackplot(intensity, true_prog, over, colors=[TEAL, CORAL], labels=["Progressive disease", "Overdiagnosed stock"], alpha=0.7)
    ax.set_xlabel("Screening intensity"); ax.set_ylabel("Absolute detections /1000")
    ax.set_title("Screening residual: rising detections can be overdiagnosis stock", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left"); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch22_reservoir.png")

def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    biases = ["Anchoring", "Availability", "Representativeness", "Premature\nclosure"]
    pre = [12, 10, 9, 11]
    post = [4, 5, 4, 3]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, pre, width=w, color=CORAL, edgecolor=INDIGO, label="Pre-debias absolute error")
    ax.bar(x + w/2, post, width=w, color=TEAL, edgecolor=INDIGO, label="Post absolute checklists")
    ax.set_xticks(x); ax.set_xticklabels(biases, fontsize=8)
    ax.set_ylabel("Absolute probability error (pp)")
    ax.set_title("Reasoning residual: absolute checklists cut cognitive error", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch23_debias.png")

def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # time horizon matters for ARR
    years = np.array([0.5, 1, 2, 3, 5])
    arr = np.array([1.0, 2.0, 3.5, 4.5, 5.5])
    ari = np.array([0.8, 1.0, 1.2, 1.5, 2.0])
    ax.plot(years, arr, "o-", color=TEAL, lw=2.4, label="ARR benefit")
    ax.plot(years, ari, "s-", color=CORAL, lw=2.2, label="ARI harm")
    ax.plot(years, arr - ari, "^-", color=INDIGO, lw=2.4, label="Net absolute")
    ax.set_xlabel("Horizon (years)"); ax.set_ylabel("Absolute pp")
    ax.set_title("Therapy residual: absolute benefit/harm depend on shared horizon", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch24_horizon.png")

def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # time-dependent AUC vs calibration slope
    months = np.array([1, 3, 6, 12, 24])
    auc = np.array([0.82, 0.80, 0.77, 0.74, 0.70])
    slope = np.array([0.95, 0.90, 0.85, 0.78, 0.70])
    ax.plot(months, auc, "o-", color=GOLD, lw=2.3, label="Time-dependent AUC")
    ax.plot(months, slope, "s-", color=TEAL, lw=2.3, label="Calibration slope")
    ax.set_xlabel("Horizon (months)"); ax.set_ylabel("Metric")
    ax.set_title("Dx/Px residual: absolute calibration and discrimination decay with horizon", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch25_horizon_decay.png")

def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # leave-one-out influence on absolute ARR
    study = np.arange(1, 9)
    arr = 3.5 + np.array([0.2, -0.1, 0.4, -0.5, 0.1, 0.0, -0.2, 0.3])
    ax.axhline(3.5, color=GOLD, ls="--", label="Full pooled ARR")
    ax.plot(study, arr, "o-", color=INDIGO, lw=2.2)
    ax.set_xlabel("Study left out"); ax.set_ylabel("Pooled absolute ARR (pp)")
    ax.set_title("Synthesis residual: influence analysis on absolute pooled ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch26_influence.png")

def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # interim looks inflate absolute ARR
    looks = np.array([1, 2, 3, 4, 5])
    arr_interim = np.array([9, 7, 5.5, 4.8, 4.4])
    ax.plot(looks, arr_interim, "o-", color=CORAL, lw=2.4, label="Unadjusted interim ARR")
    ax.axhline(4.2, color=TEAL, ls="--", label="Final ARR")
    ax.set_xlabel("Interim look number"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Interim residual: early stopping can lock inflated absolute effects", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch27_interim_arr.png")

def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    metrics = ["D2N\nmin", "Good\noutcome %", "sICH %", "Equity\ngap pp"]
    before = [55, 32, 4.5, 8]
    after = [35, 38, 3.8, 3]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, before, width=w, color=GRAY, edgecolor=INDIGO, label="Before system change")
    ax.bar(x + w/2, after, width=w, color=TEAL, edgecolor=INDIGO, label="After")
    ax.set_xticks(x); ax.set_xticklabels(metrics, fontsize=9)
    ax.set_title("Systems residual: policy changes must show absolute outcome & equity metrics", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle32_swarm_ch28_system_metrics.png")

def main():
    print("Cycle-32 →", OUT)
    for fn in [fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
               fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28]:
        fn()
    print("Done: 14")

if __name__ == "__main__":
    main()
