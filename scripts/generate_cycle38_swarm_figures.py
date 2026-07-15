#!/usr/bin/env python3
"""CRIT-APP Cycle-38 densify: ch15–28 raise uniform floor to 19. Agg indigo. ARR/NNT. pred≠cause."""
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
    roles = ["Skeptic", "Methodist", "Clinician", "Patient\nvoice", "Chair"]
    minutes = [4, 5, 4, 2, 3]
    arr_focus = [0, 1, 1, 1, 1]
    colors = [TEAL if a else CORAL for a in arr_focus]
    ax.bar(roles, minutes, color=colors, edgecolor=INDIGO)
    ax.set_ylabel("Minutes")
    ax.set_title("Ch15 residual: JC roles must protect absolute ARR discussion time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch15_roles.png")


def fig_ch16():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    flaws = ["Wrong\nestimand", "Open\nconfounding", "No absolute\nrisks", "Spin in\nabstract", "Unregistered\noutcome"]
    severity = [5, 4, 5, 3, 4]
    action = [1, 1, 1, 2, 1]  # 1=reject/adapt 2=teach
    ax.scatter(severity, action, s=180, c=[CORAL, CORAL, TEAL, GOLD, CORAL], edgecolors=INDIGO, zorder=3)
    for f, s, a in zip(flaws, severity, action):
        ax.annotate(f, (s, a), textcoords="offset points", xytext=(6, 4), fontsize=7, color=SLATE)
    ax.set_xlabel("Fatal-flaw severity (1–5)"); ax.set_ylabel("Action code (1=block adopt, 2=teach)")
    ax.set_title("Ch16 residual: autopsy maps absolute flaw severity to action", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_xlim(2, 6); ax.set_ylim(0.5, 2.5); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch16_autopsy_map.png")


def fig_ch17():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # incidence density
    person_years = np.array([1000, 800, 1200, 900])
    events = np.array([40, 20, 60, 18])
    rate = events / person_years * 1000
    labels = ["Exp A", "Unexp A", "Exp B", "Unexp B"]
    ax.bar(labels, rate, color=[TEAL, GRAY, CORAL, GRAY], edgecolor=INDIGO)
    ax.set_ylabel("Incidence density /1000 person-years")
    ax.set_title("Ch17 residual: absolute rates need person-time, not crude counts alone", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch17_incidence.png")


def fig_ch18():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    worlds = ["Y^{a=0}", "Y^{a=1}", "Observed\nmix"]
    risk = [18, 12, 15]
    ax.bar(worlds, risk, color=[GRAY, TEAL, GOLD], edgecolor=INDIGO)
    ax.annotate("Causal ARR=6pp", xy=(0.5, 15), xytext=(1.2, 20),
                arrowprops=dict(arrowstyle="->", color=INDIGO), fontsize=9, color=INDIGO, fontweight="bold")
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch18 residual: causal ARR is counterfactual contrast, not association", fontsize=11, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 25); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch18_counterfactual.png")


def fig_ch19():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    n = np.array([50, 100, 200, 400, 800, 1600])
    se = 8 / np.sqrt(n / 100)
    lo, hi = 4 - 1.96 * se, 4 + 1.96 * se
    ax.fill_between(n, lo, hi, color=TEAL, alpha=0.25, label="95% CI for ARR")
    ax.plot(n, [4] * len(n), color=INDIGO, lw=2.3, label="Point ARR=4pp")
    ax.axhline(0, color=CORAL, ls="--", label="Null")
    ax.set_xlabel("Sample size n"); ax.set_ylabel("Absolute ARR (pp)")
    ax.set_title("Ch19 residual: precision of absolute ARR scales with √n", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch19_arr_precision.png")


def fig_ch20():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    t = np.linspace(0, 36, 100)
    # PH holds on hazard but absolute RD grows then shrinks with competing risk feel
    s0 = np.exp(-0.03 * t)
    s1 = np.exp(-0.02 * t)
    rd = (s1 - s0) * 100  # survival difference
    ax.plot(t, rd, color=TEAL, lw=2.5, label="Absolute survival difference (pp)")
    ax.axhline(0, color=GRAY)
    ax.set_xlabel("Months"); ax.set_ylabel("Absolute difference (pp)")
    ax.set_title("Ch20 residual: constant HR ≠ constant absolute risk difference over time", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch20_hr_vs_rd.png")


def fig_ch21():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # RERI visual from absolute risks
    labs = ["A−B−", "A+B−", "A−B+", "A+B+"]
    r = np.array([5, 10, 12, 22])
    expected_add = 5 + (10 - 5) + (12 - 5)
    ax.bar(labs, r, color=[GRAY, TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.axhline(expected_add, color=INDIGO, ls="--", lw=2, label=f"Additive expectation={expected_add}%")
    ax.text(3, r[3] + 0.5, f"RERI≈{r[3]-expected_add:.0f}pp", ha="center", fontsize=9, fontweight="bold", color=CORAL)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch21 residual: additive interaction is absolute-risk arithmetic", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch21_reri.png")


def fig_ch22():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    cohorts = ["No screen", "Screen"]
    progressive = [20, 22]
    overdx = [0, 15]
    ax.bar(cohorts, progressive, color=TEAL, edgecolor=INDIGO, label="Progressive disease")
    ax.bar(cohorts, overdx, bottom=progressive, color=CORAL, edgecolor=INDIGO, label="Overdiagnosed stock")
    ax.set_ylabel("Absolute detections /1000")
    ax.set_title("Ch22 residual: screening gains can be absolute overdiagnosis, not benefit", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch22_overdx_stack.png")


def fig_ch23():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # base rate neglect
    scenarios = ["Intuitive\npost-test", "Base-rate\ncorrected"]
    post = [70, 18]
    ax.bar(scenarios, post, color=[CORAL, TEAL], edgecolor=INDIGO)
    ax.axhline(10, color=GOLD, ls="--", label="True prior 10%")
    ax.set_ylabel("Absolute post-test probability %")
    ax.set_title("Ch23 residual: base-rate neglect inflates absolute probability estimates", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 90); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch23_baserate.png")


def fig_ch24():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    arr = np.linspace(0.5, 8, 40)
    ari = 1.5
    nnt = 100 / arr
    nnh = 100 / ari
    ax.plot(arr, nnt, color=TEAL, lw=2.4, label="NNT")
    ax.axhline(nnh, color=CORAL, ls="--", lw=2, label=f"NNH={nnh:.0f} (ARI={ari}pp)")
    ax.set_xlabel("Absolute ARR (pp)"); ax.set_ylabel("NNT or NNH")
    ax.set_title("Ch24 residual: therapy appraisal needs absolute NNT and NNH on one plane", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 120); ax.grid(True, alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch24_nnt_nnh.png")


def fig_ch25():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    strata = ["Low", "Intermed", "High"]
    risk = [3, 12, 28]
    treat_thresh = 10
    ax.bar(strata, risk, color=[TEAL, GOLD, CORAL], edgecolor=INDIGO)
    ax.axhline(treat_thresh, color=INDIGO, ls="--", lw=2, label="Absolute treat threshold 10%")
    ax.set_ylabel("Predicted absolute risk %")
    ax.set_title("Ch25 residual: prognosis gates treatment only via absolute risk thresholds", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch25_risk_strata.png")


def fig_ch26():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    outcomes = ["Death", "mRS0–2", "sICH", "Recurrent\nstroke"]
    ctl = [12, 30, 2, 8]
    tx = [9, 38, 3, 5]
    x = np.arange(4); w = 0.35
    ax.bar(x - w/2, ctl, width=w, color=GRAY, edgecolor=INDIGO, label="Control %")
    ax.bar(x + w/2, tx, width=w, color=TEAL, edgecolor=INDIGO, label="Tx %")
    for i, (c, t) in enumerate(zip(ctl, tx)):
        ax.text(i, max(c, t) + 1, f"{t-c:+d}pp", ha="center", fontsize=8, fontweight="bold", color=INDIGO)
    ax.set_xticks(x); ax.set_xticklabels(outcomes)
    ax.set_ylabel("Absolute risk %")
    ax.set_title("Ch26 residual: SoF-style absolute risks beat relative-only synthesis", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.set_ylim(0, 50); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch26_sof_abs.png")


def fig_ch27():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    # fragility: events to reverse significance on absolute scale
    trials = ["T1", "T2", "T3", "T4", "T5"]
    fi = [2, 8, 1, 12, 4]
    colors = [CORAL if f <= 3 else TEAL for f in fi]
    ax.bar(trials, fi, color=colors, edgecolor=INDIGO)
    ax.axhline(3, color=GOLD, ls="--", label="Fragile if FI≤3")
    ax.set_ylabel("Fragility index (absolute events)")
    ax.set_title("Ch27 residual: fragility is an absolute event count, not a p-value vibe", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8); ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch27_fragility.png")


def fig_ch28():
    fig, ax = plt.subplots(figsize=(10.4, 5.0))
    sites = ["Hub", "Spoke A", "Spoke B", "Rural"]
    d2n = [32, 48, 55, 72]
    good = [42, 36, 33, 28]
    x = np.arange(4)
    ax.bar(x - 0.2, d2n, width=0.4, color=GOLD, edgecolor=INDIGO, label="Door-to-needle (min)")
    ax2 = ax.twinx()
    ax2.plot(x, good, "o-", color=TEAL, lw=2.4, ms=9, label="Good outcome %")
    ax.set_xticks(x); ax.set_xticklabels(sites)
    ax.set_ylabel("D2N minutes"); ax2.set_ylabel("Absolute good outcome %")
    ax.set_title("Ch28 residual: systems equity is absolute process AND outcome gaps", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(loc="upper left", fontsize=8); ax2.legend(loc="upper right", fontsize=8)
    ax.grid(True, axis="y", alpha=0.3); fig.tight_layout()
    return _save(fig, "cycle38_swarm_ch28_equity.png")


def main():
    print("Cycle-38 →", OUT)
    for fn in [
        fig_ch15, fig_ch16, fig_ch17, fig_ch18, fig_ch19, fig_ch20, fig_ch21,
        fig_ch22, fig_ch23, fig_ch24, fig_ch25, fig_ch26, fig_ch27, fig_ch28,
    ]:
        fn()
    print("Done: 14")


if __name__ == "__main__":
    main()
