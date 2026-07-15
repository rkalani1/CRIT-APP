#!/usr/bin/env python3
"""CRIT-APP Cycle-44 densify: ch15–28 raise uniform floor to 22. Agg indigo. ARR/NNT. pred≠cause."""
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
    method = ["Lecture\nonly", "Slide\nARR", "Teach-back\nARR board"]
    retention = [35, 55, 82]
    ax.bar(method, retention, color=[GRAY, GOLD, TEAL], edgecolor=INDIGO)
    ax.set_ylabel("Absolute % recalling NNT next week")
    ax.set_title("Ch15 residual: teach-back with absolute boards sticks better than slides", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 100); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch15_teachback.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    stages = ["Claim", "Abs\neffect", "Bias\nmap", "Counter\ncase", "Verdict"]
    redteam = [1.0, 0.85, 0.70, 0.55, 0.40]
    naive = [1.0, 0.40, 0.25, 0.10, 0.05]
    ax.plot(stages, redteam, "o-", color=TEAL, lw=2.4, label="Red-team autopsy completion")
    ax.plot(stages, naive, "s--", color=CORAL, lw=2.2, label="Naive reading completion")
    ax.set_ylabel("Fraction completing stage")
    ax.set_title("Ch16 residual: red-team autopsies force absolute-effect stress tests", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 1.15); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch16_redteam.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # attributable fraction vs absolute attributable risk
    pe = np.linspace(0.05, 0.80, 40)
    rr = 2.0
    af = pe * (rr - 1) / (1 + pe * (rr - 1))
    # absolute attributable among exposed at incidence 5%/y in unexp
    i0 = 5.0
    aar = pe * (rr - 1) * i0  # rough population attributable absolute rate units
    ax.plot(pe * 100, af * 100, color=GOLD, lw=2.3, label="Attributable fraction %")
    ax2 = ax.twinx()
    ax2.plot(pe * 100, aar, color=TEAL, lw=2.3, label="Pop. attributable absolute rate units")
    ax.set_xlabel("Exposure prevalence %"); ax.set_ylabel("AF %"); ax2.set_ylabel("Absolute attributable")
    ax.set_title("Ch17 residual: AF% without absolute rates misleads policy scale", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch17_af_abs.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    items = ["Hill\nlist", "DAG\nbackdoor", "Target\ntrial", "Abs\nARR"]
    weight = [0.4, 0.85, 0.9, 1.0]
    ax.barh(items, weight, color=[GOLD, TEAL, TEAL, INDIGO], edgecolor=SLATE)
    ax.set_xlabel("Teaching priority for causal absolute claims")
    ax.set_title("Ch18 residual: DAGs + target trials outrank checklist vibes for absolute causation", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_xlim(0, 1.15); ax.grid(True, axis="x", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch18_dag_vs_hill.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # sequential testing: absolute type I accumulation
    k = np.arange(1, 12)
    alpha_uncor = 1 - (1 - 0.05) ** k
    alpha_bonf = np.minimum(0.05 * k, 1)
    ax.plot(k, alpha_uncor * 100, color=CORAL, lw=2.4, label="Uncorrected absolute type-I risk %")
    ax.plot(k, alpha_bonf * 100, color=TEAL, lw=2.2, ls="--", label="Bonferroni absolute α spend %")
    ax.set_xlabel("Sequential absolute ARR tests"); ax.set_ylabel("Absolute type-I %")
    ax.set_title("Ch19 residual: sequential peeks accumulate absolute false-positive risk", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch19_sequential.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 60, 120)
    s_tx = np.exp(-0.015 * t)
    s_ct = np.exp(-0.022 * t)
    ax.plot(t, s_tx * 100, color=TEAL, lw=2.4, label="Treatment absolute survival %")
    ax.plot(t, s_ct * 100, color=CORAL, lw=2.4, label="Control absolute survival %")
    ax.fill_between(t, s_tx * 100, s_ct * 100, color=GOLD, alpha=0.2, label="Absolute survival difference")
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute survival %")
    ax.set_title("Ch20 residual: report absolute survival differences, not only HR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch20_surv_diff.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # additive vs multiplicative measures of interaction
    measures = ["RERI\n(abs)", "AP", "S", "Ratio of\nRRs"]
    vals = [2.5, 0.35, 1.8, 1.1]
    colors = [TEAL, GOLD, GOLD, GRAY]
    ax.bar(measures, vals, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Interaction measure (heterogeneous units)")
    ax.set_title("Ch21 residual: absolute RERI answers clinical HTE better than RR ratios alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch21_reri.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # length-time bias: slow tumors overrepresented
    types = ["Fast\nprogress", "Medium", "Slow\nindolent"]
    true_mix = [40, 35, 25]
    screen_mix = [15, 30, 55]
    x = np.arange(3); w = 0.35
    ax.bar(x - w/2, true_mix, width=w, color=GRAY, edgecolor=INDIGO, label="True population mix %")
    ax.bar(x + w/2, screen_mix, width=w, color=CORAL, edgecolor=INDIGO, label="Screen-detected mix %")
    ax.set_xticks(x); ax.set_xticklabels(types)
    ax.set_ylabel("Absolute mix %")
    ax.set_title("Ch22 residual: length-time bias enriches absolute indolent disease among screens", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch22_lengthtime.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    anchors = [1, 5, 15, 30, 50]
    estimates = [8, 12, 18, 28, 40]  # pulled toward anchor
    truth = 15
    ax.plot(anchors, estimates, "o-", color=CORAL, lw=2.4, label="Anchored absolute estimate")
    ax.axhline(truth, color=TEAL, ls="--", lw=2, label=f"True absolute risk={truth}%")
    ax.set_xlabel("Anchor absolute % shown first"); ax.set_ylabel("Clinician absolute estimate %")
    ax.set_title("Ch23 residual: anchoring distorts absolute risk judgments", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch23_anchor.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # surrogacy failure: surrogate moves, hard absolute endpoint does not
    arms = ["Control", "Drug"]
    surr = [40, 70]
    hard = [12, 11.5]
    x = np.arange(2); w = 0.35
    ax.bar(x - w/2, surr, width=w, color=GOLD, edgecolor=INDIGO, label="Surrogate absolute response %")
    ax.bar(x + w/2, hard, width=w, color=TEAL, edgecolor=INDIGO, label="Hard absolute endpoint %")
    ax.set_xticks(x); ax.set_xticklabels(arms)
    ax.set_ylabel("Absolute %")
    ax.set_title("Ch24 residual: surrogate gains can fail to deliver absolute hard-endpoint benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch24_surrogate.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # diagnosis timing absolute: earlier test shifts label time
    stages = ["Symptom", "ED test", "Admit", "Discharge"]
    cum_dx = [10, 55, 80, 95]
    ax.step(stages, cum_dx, where="mid", color=INDIGO, lw=2.5)
    ax.fill_between(range(4), cum_dx, step="mid", color=TEAL, alpha=0.15)
    ax.set_ylabel("Absolute cumulative diagnosis %")
    ax.set_title("Ch25 residual: diagnostic yield is path-dependent absolute capture over time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 105); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch25_dx_path.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    years = np.array([2018, 2019, 2020, 2021, 2022, 2023])
    living_arr = np.array([3.0, 3.2, 3.8, 4.0, 4.1, 4.2])
    static_arr = np.array([3.0, 3.0, 3.0, 3.0, 3.0, 3.0])
    ax.plot(years, living_arr, "o-", color=TEAL, lw=2.4, label="Living SR absolute ARR")
    ax.plot(years, static_arr, "s--", color=GRAY, lw=2.2, label="Static guideline ARR")
    ax.set_xlabel("Year"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch26 residual: living reviews update absolute effects; static docs lag", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch26_living.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # tipping point: how extreme missing outcomes must be to nullify ARR
    extreme = np.linspace(0, 100, 50)
    arr_tip = 5 - 0.08 * extreme
    ax.plot(extreme, arr_tip, color=INDIGO, lw=2.5)
    ax.axhline(0, color=CORAL, ls="--", label="Null ARR")
    ax.axvline(62.5, color=GOLD, ls=":", label="Tipping absolute missing severity")
    ax.set_xlabel("Assumed absolute event % in missing arm extremes")
    ax.set_ylabel("Imputed absolute ARR (pp)")
    ax.set_title("Ch27 residual: tipping-point analysis states absolute assumptions that kill ARR", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch27_tipping.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    policies = ["Status\nquo", "Bypass", "Mobile\nstroke", "24/7\nEVT"]
    good_pp = [0, 3, 5, 7]
    cost = [0, 2, 8, 12]
    x = np.arange(4)
    ax.bar(x - 0.2, good_pp, width=0.4, color=TEAL, edgecolor=INDIGO, label="Absolute good-outcome gain pp")
    ax2 = ax.twinx()
    ax2.bar(x + 0.2, cost, width=0.4, color=GOLD, edgecolor=INDIGO, label="Relative cost units")
    ax.set_xticks(x); ax.set_xticklabels(policies)
    ax.set_ylabel("Absolute outcome gain (pp)"); ax2.set_ylabel("Cost units")
    ax.set_title("Ch28 residual: policy choices trade absolute outcomes against resources", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle44_swarm_ch28_policy.png")


def main():
    print("Cycle-44 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
