#!/usr/bin/env python3
"""
CRIT-APP Cycle-3 densify swarm: original matplotlib scientific teaching figures.

Targets high-value residual gaps after cycles 1–2:
  ch17 person-time / incidence density
  ch18 selection bias (collider / survivor)
  ch05 confounding by indication (crude vs stratified ARR/NNT)
  ch20 survival absolute risk from KM landmarks
  ch04 selection structure vs confounding fork

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle3_swarm_* only). Does not redo cycle1/2 figures.
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, FancyArrowPatch, FancyBboxPatch, Rectangle
import numpy as np

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
OUT.mkdir(parents=True, exist_ok=True)

INDIGO = "#283593"
TEAL = "#00695C"
GOLD = "#F9A825"
CORAL = "#C62828"
SLATE = "#37474F"
LIGHT = "#ECEFF1"
WHITE = "#FFFFFF"
GREEN = "#2E7D32"
BLUE = "#1565C0"
ORANGE = "#EF6C00"
PURPLE = "#6A1B9A"


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch17_person_time() -> Path:
    """Open-cohort person-time grid: incidence rate = events / person-time."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.0))

    # Left: 10 synthetic patients, 12 months; events and censoring
    ax = axes[0]
    # (start_month, end_month, event: 1=event, 0=censor/admin end)
    trajectories = [
        (0, 12, 0),
        (0, 4, 1),
        (0, 12, 0),
        (1, 9, 1),
        (0, 12, 0),
        (2, 6, 1),
        (0, 11, 0),
        (0, 3, 1),
        (3, 12, 0),
        (0, 8, 1),
    ]
    n_events = sum(e for _, _, e in trajectories)
    person_months = sum(end - start for start, end, _ in trajectories)
    person_years = person_months / 12.0
    rate = n_events / person_years

    for i, (start, end, event) in enumerate(trajectories):
        y = 9.5 - i * 0.9
        ax.plot([start, end], [y, y], color=TEAL if not event else CORAL, lw=3.2, solid_capstyle="round")
        ax.plot(start, y, "o", color=INDIGO, ms=6, zorder=3)
        if event:
            ax.plot(end, y, "X", color=CORAL, ms=9, mew=2, zorder=3)
        else:
            ax.plot(end, y, "s", color=SLATE, ms=6, zorder=3)
        ax.text(-0.7, y, f"P{i+1}", ha="right", va="center", fontsize=7.5, color=SLATE)

    ax.set_xlim(-1.2, 13.5)
    ax.set_ylim(-0.3, 10.5)
    ax.set_xlabel("Months since cohort entry (synthetic open cohort)")
    ax.set_yticks([])
    ax.set_title("Person-time accrues while each patient is at risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.axvline(0, color=LIGHT, lw=0.8)
    # legend proxies
    ax.plot([], [], color=TEAL, lw=3, label="Followed (no event)")
    ax.plot([], [], color=CORAL, lw=3, label="Followed until event")
    ax.plot([], [], "X", color=CORAL, ms=8, label="Incident event")
    ax.plot([], [], "s", color=SLATE, ms=6, label="Censored / admin end")
    ax.legend(fontsize=7.2, loc="lower right", framealpha=0.95)
    ax.grid(True, axis="x", alpha=0.25)

    # Right: teaching arithmetic panel
    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Incidence density (rate) arithmetic", fontsize=10, fontweight="bold", color=INDIGO)

    boxes = [
        (7.6, TEAL, "#E0F2F1", "Numerator", f"{n_events} new events in the window"),
        (5.4, INDIGO, "#E8EAF6", "Denominator", f"{person_months} person-months\n= {person_years:.2f} person-years"),
        (3.2, CORAL, "#FFEBEE", "Incidence rate", f"{n_events} / {person_years:.2f} = {rate:.2f} per person-year\n≈ {rate * 100:.1f} per 100 person-years"),
        (0.7, GOLD, "#FFF8E1", "Do not mix clocks", "A rate is not a 90-day risk.\nConvert before comparing trial risks\nto secondary-prevention rates."),
    ]
    for y, edge, face, title, body in boxes:
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y),
                9.3,
                1.95,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=face,
                edgecolor=edge,
                lw=1.4,
            )
        )
        ax.text(0.7, y + 1.35, title, fontsize=9, fontweight="bold", color=edge, va="center")
        ax.text(0.7, y + 0.55, body, fontsize=8.2, color=SLATE, va="center")

    fig.suptitle(
        "Person-time and incidence density: events ÷ time at risk (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle3_swarm_ch17_person_time.png")


def fig_ch18_selection_collider() -> Path:
    """Survivor / selection bias: conditioning on collider invents association."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.95))

    # Left: DAG-style panel (drawn boxes/arrows — original teaching, not copied)
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Structural selection: condition on survival (collider)", fontsize=10, fontweight="bold", color=INDIGO)

    nodes = {
        "Tx": (2.0, 7.2, "Aggressive\ntherapy (Tx)"),
        "Res": (8.0, 7.2, "Unmeasured\nresilience (U)"),
        "S": (5.0, 3.6, "Survive to\nday 30 (S)"),
        "Y": (5.0, 0.9, "Analyzed\noutcomes (Y)"),
    }
    for key, (x, y, lab) in nodes.items():
        face = "#FFEBEE" if key == "S" else WHITE
        edge = CORAL if key == "S" else INDIGO
        ax.add_patch(
            FancyBboxPatch(
                (x - 1.35, y - 0.7),
                2.7,
                1.5,
                boxstyle="round,pad=0.04,rounding_size=0.1",
                facecolor=face,
                edgecolor=edge,
                lw=1.6,
            )
        )
        ax.text(x, y, lab, ha="center", va="center", fontsize=8, color=edge, fontweight="bold")

    def arrow(a, b, color=INDIGO, style="-|>"):
        ax.annotate(
            "",
            xy=b,
            xytext=a,
            arrowprops=dict(arrowstyle=style, color=color, lw=1.8, mutation_scale=14),
        )

    arrow((2.5, 6.5), (4.2, 4.4))  # Tx -> S
    arrow((7.5, 6.5), (5.8, 4.4))  # U -> S
    arrow((5.0, 2.9), (5.0, 1.65), color=TEAL)  # S -> analysis restriction

    ax.text(
        5.0,
        9.3,
        "Both Tx and U cause survival → S is a collider.\nAnalyzing only S=1 opens a non-causal Tx–U path.",
        ha="center",
        va="center",
        fontsize=8,
        color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor=SLATE, alpha=0.9),
    )
    ax.text(5.0, 5.35, "condition on S=1", ha="center", fontsize=8, color=CORAL, fontweight="bold")

    # Right: numeric intuition
    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("Synthetic survivor table (teaching)", fontsize=10, fontweight="bold", color=INDIGO)

    # Fake 2x2 among survivors only: Tx appears associated with high resilience
    rows = [
        (8.0, "Full cohort truth", "Tx ⊥ resilience (no association)"),
        (6.2, "Restrict to day-30 survivors", "Conditioning on collider S"),
        (4.4, "Among survivors", "Tx appears linked to high resilience"),
        (2.6, "Downstream illusion", "Therapy looks protective via healthier survivors"),
        (0.8, "Appraisal move", "Map selection node; ask who is missing and why"),
    ]
    colors = [TEAL, CORAL, CORAL, GOLD, GREEN]
    for (y, title, body), edge in zip(rows, colors):
        ax.add_patch(
            FancyBboxPatch(
                (0.3, y - 0.55),
                9.4,
                1.5,
                boxstyle="round,pad=0.04,rounding_size=0.08",
                facecolor=WHITE,
                edgecolor=edge,
                lw=1.3,
            )
        )
        ax.text(0.55, y + 0.35, title, fontsize=8.5, fontweight="bold", color=edge, va="center")
        ax.text(0.55, y - 0.2, body, fontsize=8, color=SLATE, va="center")

    fig.suptitle(
        "Selection bias ≠ confounding: conditioning on a collider invents associations (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle3_swarm_ch18_selection_collider.png")


def fig_ch05_crude_vs_stratified() -> Path:
    """Ch05 DOAC timing example: crude ARR inflated vs stratified ARR 5 pp."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 5.0))

    # From chapter worked example:
    # Large: Early 20% (n=1000), Delayed 25% (n=3000) → ARR 5%
    # Small: Early 5% (n=5000), Delayed 10% (n=1000) → ARR 5%
    # Crude: Early 7.5% (450/6000), Delayed 21.25% (850/4000) → ARR 13.75%
    strata = ["Large\ninfarct", "Small\ninfarct", "Crude\n(pooled)"]
    early = np.array([20.0, 5.0, 7.5])
    delayed = np.array([25.0, 10.0, 21.25])
    arr = delayed - early  # 5, 5, 13.75

    ax = axes[0]
    x = np.arange(len(strata))
    w = 0.32
    b1 = ax.bar(x - w / 2, delayed, width=w, color="#90A4AE", edgecolor=INDIGO, label="Delayed DOAC risk %")
    b2 = ax.bar(x + w / 2, early, width=w, color=TEAL, edgecolor=INDIGO, label="Early DOAC risk %")
    ax.set_xticks(x)
    ax.set_xticklabels(strata)
    ax.set_ylabel("90-day composite event risk (%)")
    ax.set_ylim(0, 30)
    ax.set_title("Stratified risks vs confounded crude pool", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=7.5, loc="upper right")
    ax.grid(True, axis="y", alpha=0.3)
    for rect, v in zip(list(b1) + list(b2), list(delayed) + list(early)):
        ax.text(rect.get_x() + rect.get_width() / 2, v + 0.5, f"{v:g}", ha="center", fontsize=7.5)

    ax = axes[1]
    colors = [GREEN, GREEN, CORAL]
    bars = ax.bar(x, arr, color=colors, edgecolor=INDIGO, width=0.55)
    ax.axhline(5.0, color=TEAL, ls="--", lw=1.5, label="True stratum ARR = 5 pp")
    ax.set_xticks(x)
    ax.set_xticklabels(strata)
    ax.set_ylabel("Absolute risk reduction (pp)")
    ax.set_ylim(0, 16)
    ax.set_title("Crude ARR invents a miracle NNT", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="upper left")
    ax.grid(True, axis="y", alpha=0.3)
    nnts = [20, 20, round(1 / 0.1375)]
    for b, v, nnt in zip(bars, arr, nnts):
        ax.text(
            b.get_x() + b.get_width() / 2,
            v + 0.35,
            f"ARR {v:.2g} pp\nNNT ≈ {nnt}",
            ha="center",
            fontsize=8,
            fontweight="bold",
            color=SLATE,
        )
    ax.text(
        0.5,
        0.02,
        "Confounding by indication: small infarcts flood the Early arm → crude overstates benefit",
        transform=ax.transAxes,
        ha="center",
        va="bottom",
        fontsize=7.8,
        color=CORAL,
    )

    fig.suptitle(
        "Confounding by indication: crude ARR 13.75 pp vs stratified ARR 5 pp (synthetic ch05)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle3_swarm_ch05_crude_vs_stratified.png")


def fig_ch20_km_absolute_arr() -> Path:
    """Read ARR/NNT from survival curves at a fixed clinical horizon; HR ≠ ARR."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.95))

    # Synthetic exponential-ish KM via step interpolation of cumulative incidence
    t = np.array([0, 30, 90, 180, 365, 730])
    # Control cumulative incidence of event (higher)
    ci_c = np.array([0.00, 0.04, 0.10, 0.16, 0.24, 0.32])
    # Treatment cumulative incidence
    ci_t = np.array([0.00, 0.03, 0.07, 0.11, 0.16, 0.22])
    # Survival = 1 - CI
    s_c = 1 - ci_c
    s_t = 1 - ci_t

    ax = axes[0]
    ax.step(t, s_c * 100, where="post", color="#90A4AE", lw=2.4, label="Control survival")
    ax.step(t, s_t * 100, where="post", color=TEAL, lw=2.4, label="Treatment survival")
    # landmark day 365
    day = 365
    sc365 = 1 - 0.24
    st365 = 1 - 0.16
    ax.axvline(day, color=GOLD, ls="--", lw=1.3)
    ax.plot([day, day], [sc365 * 100, st365 * 100], color=CORAL, lw=2.5)
    ax.plot(day, sc365 * 100, "o", color="#546E7A", ms=8)
    ax.plot(day, st365 * 100, "o", color=TEAL, ms=8)
    ax.annotate(
        "ARR at day 365\n= 8 pp\nNNT ≈ 13",
        xy=(day, (sc365 + st365) / 2 * 100),
        xytext=(430, 78),
        fontsize=8.5,
        color=CORAL,
        fontweight="bold",
        arrowprops=dict(arrowstyle="->", color=CORAL),
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    ax.set_xlabel("Days since index (synthetic secondary prevention)")
    ax.set_ylabel("Event-free survival (%)")
    ax.set_xlim(0, 760)
    ax.set_ylim(60, 102)
    ax.set_title("Absolute benefit is a vertical gap at a named horizon", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8, loc="lower left")
    ax.grid(True, alpha=0.3)
    ax.text(day, 61.5, "day 365", ha="center", fontsize=7.5, color=GOLD)

    ax = axes[1]
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.set_title("HR is relative; counseling needs ARR/NNT", fontsize=10, fontweight="bold", color=INDIGO)

    # Cumulative incidence at landmarks
    landmarks = [
        (8.0, "Day 90", ci_c[2], ci_t[2]),
        (5.6, "Day 365", ci_c[4], ci_t[4]),
        (3.2, "Day 730", ci_c[5], ci_t[5]),
    ]
    for y, lab, pc, pt in landmarks:
        arr = (pc - pt) * 100
        nnt = 1 / (pc - pt)
        ax.add_patch(
            FancyBboxPatch(
                (0.35, y - 0.9),
                9.3,
                2.0,
                boxstyle="round,pad=0.05,rounding_size=0.1",
                facecolor=WHITE,
                edgecolor=INDIGO,
                lw=1.2,
            )
        )
        ax.text(0.65, y + 0.45, lab, fontsize=9, fontweight="bold", color=INDIGO, va="center")
        ax.text(
            0.65,
            y - 0.25,
            f"Control risk {pc*100:.0f}% · Tx risk {pt*100:.0f}% · ARR {arr:.0f} pp · NNT ≈ {nnt:.0f}",
            fontsize=8.2,
            color=SLATE,
            va="center",
        )

    ax.add_patch(
        FancyBboxPatch(
            (0.35, 0.35),
            9.3,
            1.7,
            boxstyle="round,pad=0.05,rounding_size=0.1",
            facecolor="#FFF8E1",
            edgecolor=GOLD,
            lw=1.4,
        )
    )
    ax.text(
        5.0,
        1.2,
        "A single HR (e.g., 0.70) does not equal a 30% absolute reduction.\n"
        "Prediction models forecast risk; they do not by themselves prove cause.",
        ha="center",
        va="center",
        fontsize=8.2,
        color=SLATE,
    )

    fig.suptitle(
        "Survival literacy: read absolute risk difference from the curves (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle3_swarm_ch20_km_absolute_arr.png")


def fig_ch04_selection_vs_confounding() -> Path:
    """Side-by-side: confounding fork vs selection/collider structure."""
    fig, axes = plt.subplots(1, 2, figsize=(10.6, 4.8))

    def draw_node(ax, x, y, text, edge=INDIGO, face=WHITE):
        ax.add_patch(
            FancyBboxPatch(
                (x - 1.15, y - 0.55),
                2.3,
                1.15,
                boxstyle="round,pad=0.03,rounding_size=0.08",
                facecolor=face,
                edgecolor=edge,
                lw=1.5,
            )
        )
        ax.text(x, y, text, ha="center", va="center", fontsize=8.2, color=edge, fontweight="bold")

    def arr(ax, a, b, color=INDIGO):
        ax.annotate(
            "",
            xy=b,
            xytext=a,
            arrowprops=dict(arrowstyle="-|>", color=color, lw=1.7, mutation_scale=13),
        )

    # Left: confounding fork
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Confounding: open backdoor (common cause)", fontsize=10, fontweight="bold", color=INDIGO)
    draw_node(ax, 5.0, 8.0, "Severity (C)", edge=ORANGE, face="#FFF3E0")
    draw_node(ax, 2.2, 3.5, "Treatment (A)")
    draw_node(ax, 7.8, 3.5, "Outcome (Y)")
    arr(ax, (4.3, 7.4), (2.7, 4.2), ORANGE)
    arr(ax, (5.7, 7.4), (7.3, 4.2), ORANGE)
    arr(ax, (3.4, 3.5), (6.6, 3.5), TEAL)  # possible causal A->Y
    ax.text(5.0, 2.2, "A ← C → Y  (backdoor)\nAdjust for C (pre-exposure) to block.", ha="center", fontsize=8.3, color=SLATE)
    ax.text(5.0, 0.7, "Classic: NIHSS drives both EVT and mRS", ha="center", fontsize=8, color=ORANGE, style="italic")

    # Right: selection collider
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Selection: condition on common effect", fontsize=10, fontweight="bold", color=INDIGO)
    draw_node(ax, 2.2, 7.5, "Exposure (A)")
    draw_node(ax, 7.8, 7.5, "Outcome\ncauses (U)")
    draw_node(ax, 5.0, 3.8, "In study (S=1)", edge=CORAL, face="#FFEBEE")
    arr(ax, (2.8, 6.9), (4.3, 4.5), CORAL)
    arr(ax, (7.2, 6.9), (5.7, 4.5), CORAL)
    ax.text(
        5.0,
        1.8,
        "A → S ← U  (collider)\nRestricting to S=1 invents A–U association.",
        ha="center",
        fontsize=8.3,
        color=SLATE,
    )
    ax.text(5.0, 0.55, "Classic: complete MRI follow-up only", ha="center", fontsize=8, color=CORAL, style="italic")

    fig.suptitle(
        "Bias taxonomy structures: confounding fork vs selection collider (teaching DAGs)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.01,
    )
    fig.tight_layout()
    return _save(fig, "cycle3_swarm_ch04_selection_vs_confounding.png")


def main() -> None:
    print("Cycle-3 swarm densify figures →", OUT)
    writers = [
        fig_ch17_person_time,
        fig_ch18_selection_collider,
        fig_ch05_crude_vs_stratified,
        fig_ch20_km_absolute_arr,
        fig_ch04_selection_vs_confounding,
    ]
    paths = [fn() for fn in writers]
    print(f"Done: {len(paths)} figures")


if __name__ == "__main__":
    main()
