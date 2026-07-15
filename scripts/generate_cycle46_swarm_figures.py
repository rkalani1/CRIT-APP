#!/usr/bin/env python3
"""CRIT-APP Cycle-46 densify: ch15–28 raise uniform floor to 23. Agg indigo. ARR/NNT. pred≠cause."""
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
    weeks = np.arange(1, 9)
    without = np.array([40, 42, 38, 41, 39, 40, 38, 42])
    with_card = np.array([55, 62, 68, 72, 75, 78, 80, 82])
    ax.plot(weeks, without, "s--", color=GRAY, lw=2.2, label="JC without absolute card")
    ax.plot(weeks, with_card, "o-", color=TEAL, lw=2.4, label="JC with shared ARR/NNT card")
    ax.set_xlabel("Week"); ax.set_ylabel("Absolute % trainees stating NNT correctly")
    ax.set_title("Ch15 residual: shared absolute cards raise JC teaching fidelity", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch15_jc_card.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    fails = ["Wrong\nPICO", "No ARR", "Bias\nblind", "Spin\naccept", "No action"]
    counts = [3, 8, 5, 6, 4]
    ax.bar(fails, counts, color=CORAL, edgecolor=INDIGO)
    ax.set_ylabel("Absolute autopsy fail counts (teaching set)")
    ax.set_title("Ch16 residual: missing absolute effect is the modal autopsy failure", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch16_fail_mode.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    ages = np.array([40, 50, 60, 70, 80])
    inc = np.array([0.5, 1.2, 2.5, 5.0, 9.0])
    prev = np.array([0.8, 2.0, 5.0, 12.0, 22.0])
    ax.plot(ages, inc, "o-", color=TEAL, lw=2.3, label="Incidence %/y")
    ax.plot(ages, prev, "s-", color=GOLD, lw=2.3, label="Point prevalence %")
    ax.set_xlabel("Age"); ax.set_ylabel("Absolute frequency")
    ax.set_title("Ch17 residual: prevalence stacks survivors; incidence is absolute new events", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch17_age_freq.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    worlds = ["Factual\ntreat", "Counterfactual\nno treat", "ARR"]
    risk = [18, 24, 6]
    colors = [TEAL, CORAL, INDIGO]
    ax.bar(worlds, risk, color=colors, edgecolor=SLATE)
    ax.set_ylabel("Absolute risk % / difference pp")
    ax.set_title("Ch18 residual: causation is a contrast of absolute potential outcomes", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch18_counterfact.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # estimate precision vs n
    n = np.logspace(1.5, 3.5, 40)
    se = 10 / np.sqrt(n)
    ax.plot(n, se, color=INDIGO, lw=2.5)
    ax.set_xscale("log")
    ax.set_xlabel("n (log)"); ax.set_ylabel("SE of absolute ARR (pp)")
    ax.set_title("Ch19 residual: absolute precision scales as 1/√n, not wishful thinking", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, which="both", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch19_se_n.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # PH violation: HR constant but absolute RD grows then shrinks
    t = np.linspace(0.5, 36, 80)
    s0 = np.exp(-0.03 * t)
    s1 = np.exp(-0.02 * t)
    hr = np.full_like(t, 0.02 / 0.03)
    rd = (s1 - s0) * 100  # survival difference as absolute
    ax.plot(t, hr, color=GRAY, lw=2.2, label="HR (constant under PH)")
    ax2 = ax.twinx()
    ax2.plot(t, rd, color=TEAL, lw=2.4, label="Absolute survival difference pp")
    ax.set_xlabel("Months"); ax.set_ylabel("HR"); ax2.set_ylabel("Absolute difference pp")
    ax.set_title("Ch20 residual: constant HR ≠ constant absolute risk difference", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch20_hr_vs_rd.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # standardization: crude vs std absolute
    labels = ["Crude ARR", "Std to\nyoung", "Std to\nold", "Std to\ntarget"]
    vals = [5.0, 3.0, 7.5, 5.8]
    ax.bar(labels, vals, color=[GRAY, TEAL, CORAL, INDIGO], edgecolor=SLATE)
    ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch21 residual: standardization answers which absolute population effect", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch21_std_pop.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # overdiagnosis absolute stack
    cats = ["True\nbenefit", "Overdx\nharm", "False\n+ workup", "Net"]
    vals = [2.0, -3.5, -1.0, -2.5]
    colors = [TEAL, CORAL, GOLD, INDIGO]
    ax.bar(cats, vals, color=colors, edgecolor=SLATE)
    ax.axhline(0, color=SLATE)
    ax.set_ylabel("Absolute pp (teaching scale)")
    ax.set_title("Ch22 residual: net screening absolute can be negative despite true benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch22_overdx_stack.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    prior = np.linspace(1, 40, 40)
    lr = 5
    odds = (prior / 100) / (1 - prior / 100)
    post = 100 * (odds * lr) / (1 + odds * lr)
    ax.plot(prior, post, color=INDIGO, lw=2.5, label="Post-test absolute % (LR+=5)")
    ax.plot(prior, prior, "--", color=GRAY, label="No information")
    ax.set_xlabel("Prior absolute %"); ax.set_ylabel("Post-test absolute %")
    ax.set_title("Ch23 residual: base-rate neglect ignores absolute priors under LR updates", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch23_base_rate.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    horizon = np.array([0.5, 1, 2, 3, 5])
    nnt = np.array([50, 35, 25, 22, 20])
    nnh = np.array([80, 60, 40, 30, 22])
    ax.plot(horizon, nnt, "o-", color=TEAL, lw=2.4, label="NNT benefit")
    ax.plot(horizon, nnh, "s-", color=CORAL, lw=2.4, label="NNH harm")
    ax.set_xlabel("Horizon (years)"); ax.set_ylabel("NNT / NNH")
    ax.set_title("Ch24 residual: absolute benefit and harm NNTs can cross over time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch24_nnt_nnh.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strata = ["Low", "Intermed", "High", "V.high"]
    pred = [5, 12, 25, 45]
    obs = [6, 11, 22, 38]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, pred, width=w, color=GRAY, edgecolor=INDIGO, label="Predicted absolute %")
    ax.bar(x + w/2, obs, width=w, color=TEAL, edgecolor=INDIGO, label="Observed absolute %")
    ax.set_xticks(x); ax.set_xticklabels(strata)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch25 residual: prognosis tools live or die on absolute risk strata", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch25_risk_strata.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # CPR net benefit vs treat all/none
    thr = np.linspace(0.05, 0.4, 50)
    nb_cpr = 0.06 - 0.4 * (thr - 0.12) ** 2
    nb_all = 0.10 - thr
    ax.plot(thr, nb_cpr, color=TEAL, lw=2.5, label="CPR absolute net benefit")
    ax.plot(thr, nb_all, color=GOLD, lw=2.2, label="Treat all")
    ax.axhline(0, color=GRAY, label="Treat none")
    ax.set_xlabel("Absolute risk threshold"); ax.set_ylabel("Net benefit")
    ax.set_title("Ch26 residual: CPR usefulness is absolute decision-curve territory", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch26_cpr_dca.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # fragility: events to tip significance
    n_events_tip = np.array([1, 2, 3, 5, 8, 12])
    fragility_index = n_events_tip
    arr = 100 / (50 + 5 * n_events_tip)  # sketch
    ax.plot(fragility_index, arr, "o-", color=CORAL, lw=2.4)
    ax.set_xlabel("Fragility index (events to tip)"); ax.set_ylabel("Absolute ARR context (pp sketch)")
    ax.set_title("Ch27 residual: fragility is absolute event counts, not only p-values", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch27_fragility.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    opts = ["Med\nRx", "Endo\nRx", "Surgery", "Palliate"]
    benefit = [8, 15, 20, 3]
    harm = [2, 5, 12, 1]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, benefit, width=w, color=TEAL, edgecolor=INDIGO, label="Absolute benefit %")
    ax.bar(x + w/2, harm, width=w, color=CORAL, edgecolor=INDIGO, label="Absolute harm %")
    ax.set_xticks(x); ax.set_xticklabels(opts)
    ax.set_ylabel("Absolute %")
    ax.set_title("Ch28 residual: patient communication needs absolute benefit and harm boards", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle46_swarm_ch28_comm_board.png")


def main():
    print("Cycle-46 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
