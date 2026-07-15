#!/usr/bin/env python3
"""
CRIT-APP 3h-swarm cycle-1 densification: original matplotlib teaching figures.

Code-drawn only (Agg). Writes PNGs under docs/assets/figures/.
Safe to re-run (overwrites cycle1_* outputs only).
"""
from __future__ import annotations

from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Circle, FancyArrowPatch
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


def _save(fig: plt.Figure, name: str) -> Path:
    path = OUT / name
    fig.savefig(path, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print(f"  wrote {path.name}")
    return path


def fig_ch11_dichotomy_loss() -> Path:
    """Dichotomized mRS loses mass that shift analysis can capture (ch11)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6))
    cats = np.arange(7)
    labels = ["0", "1", "2", "3", "4", "5", "6"]
    # synthetic: treatment shifts 4→3 mass (clinically huge) but not 3→≤2
    ctrl = np.array([6, 10, 14, 16, 22, 18, 14], dtype=float)
    tx = np.array([7, 11, 15, 28, 12, 15, 12], dtype=float)
    ctrl = 100 * ctrl / ctrl.sum()
    tx = 100 * tx / tx.sum()

    ax = axes[0]
    w = 0.38
    ax.bar(cats - w / 2, ctrl, width=w, color="#90A4AE", edgecolor=INDIGO, label="Control")
    ax.bar(cats + w / 2, tx, width=w, color=TEAL, edgecolor=INDIGO, label="Treatment")
    ax.set_xticks(cats)
    ax.set_xticklabels(labels)
    ax.set_xlabel("mRS category")
    ax.set_ylabel("Percent of cohort")
    ax.set_title("Full ordinal distribution", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.set_ylim(0, 35)
    ax.annotate(
        "Mass moves 4→3\n(walk / live at home\nwith help)",
        xy=(3.2, 28),
        xytext=(5.0, 30),
        fontsize=7.5,
        color=CORAL,
        arrowprops=dict(arrowstyle="->", color=CORAL, lw=1.2),
    )

    ax = axes[1]
    # dichotomy mRS 0-2 vs 3-6: almost no ARR despite real shift
    good_c = ctrl[:3].sum()
    good_t = tx[:3].sum()
    poor_c = 100 - good_c
    poor_t = 100 - good_t
    x = np.array([0, 1])
    ax.bar(x - w / 2, [good_c, poor_c], width=w, color="#90A4AE", edgecolor=INDIGO, label="Control")
    ax.bar(x + w / 2, [good_t, poor_t], width=w, color=TEAL, edgecolor=INDIGO, label="Treatment")
    ax.set_xticks(x)
    ax.set_xticklabels(["mRS 0–2\n('good')", "mRS 3–6\n('poor')"])
    ax.set_ylabel("Percent of cohort")
    ax.set_title("Same data, 0–2 dichotomy", fontsize=10, fontweight="bold", color=INDIGO)
    ax.set_ylim(0, 80)
    arr = good_t - good_c
    ax.text(
        0.5,
        72,
        f"ARR for mRS 0–2 ≈ {arr:.1f} pp\n"
        "(near-null primary while\n4→3 shift is large)",
        ha="center",
        fontsize=8,
        color=CORAL,
        bbox=dict(boxstyle="round", facecolor="#FFEBEE", edgecolor=CORAL),
    )
    fig.suptitle(
        "Dichotomized mRS can hide clinically meaningful shifts (synthetic teaching data)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch11_dichotomy_loss.png")


def fig_ch11_km_vs_cif() -> Path:
    """Kaplan–Meier treats death as censoring → overestimates cumulative risk (ch11)."""
    fig, ax = plt.subplots(figsize=(8.2, 4.8))
    t = np.array([0, 30, 90, 180, 365])
    # synthetic cumulative risks (%)
    km = np.array([0.0, 4.0, 5.8, 6.5, 6.7])  # naive KM treating death as censor
    cif = np.array([0.0, 4.0, 5.4, 6.0, 6.5])  # competing-risk CIF
    death = np.array([0.0, 6.0, 9.5, 12.0, 14.5])  # cumulative competing death

    ax.plot(t, km, "o-", color=CORAL, lw=2.2, markersize=7, label="Naive KM (death = censor)")
    ax.plot(t, cif, "s-", color=TEAL, lw=2.2, markersize=7, label="CIF (competing-risk aware)")
    ax.fill_between(t, cif, km, color=CORAL, alpha=0.15, label="Overestimation gap")
    ax2 = ax.twinx()
    ax2.plot(t, death, "--", color=SLATE, lw=1.5, alpha=0.8, label="Competing death CIF")
    ax2.set_ylabel("Cumulative competing death (%)", color=SLATE, fontsize=9)
    ax2.set_ylim(0, 25)
    ax2.tick_params(axis="y", labelcolor=SLATE)

    ax.set_xlabel("Days since discharge")
    ax.set_ylabel("Cumulative recurrent stroke risk (%)")
    ax.set_xlim(0, 370)
    ax.set_ylim(0, 10)
    ax.set_title(
        "Competing risks: KM overestimates nonfatal event risk (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.grid(True, alpha=0.3)
    # combined legend
    lines1, labels1 = ax.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax.legend(lines1 + lines2, labels1 + labels2, loc="upper left", fontsize=8)
    ax.text(
        200,
        1.2,
        "Censoring death invents an immortal universe\n"
        "where dead patients can still recur.\n"
        "Use CIF / Fine–Gray for absolute prognosis.",
        fontsize=8,
        color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    return _save(fig, "cycle1_ch11_km_vs_cif.png")


def fig_ch13_abs_vs_rel_hte() -> Path:
    """Constant RR → baseline-driven absolute HTE (ch13)."""
    fig, axes = plt.subplots(1, 2, figsize=(9.8, 4.5))
    groups = ["Severe\n(baseline 50%)", "Mild\n(baseline 5%)"]
    # constant RR 0.80
    ctrl = np.array([0.50, 0.05])
    tx = ctrl * 0.80
    arr = ctrl - tx

    ax = axes[0]
    x = np.arange(2)
    w = 0.35
    ax.bar(x - w / 2, ctrl * 100, width=w, color="#90A4AE", edgecolor=INDIGO, label="Control risk")
    ax.bar(x + w / 2, tx * 100, width=w, color=TEAL, edgecolor=INDIGO, label="Treated risk")
    ax.set_xticks(x)
    ax.set_xticklabels(groups)
    ax.set_ylabel("Event risk (%)")
    ax.set_ylim(0, 60)
    ax.set_title("Constant relative effect (RR = 0.80)", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    for i, (c, t) in enumerate(zip(ctrl, tx)):
        ax.text(i, t * 100 + 2.5, f"ARR {100 * (c - t):.0f} pp", ha="center", fontsize=8, color=CORAL)

    ax = axes[1]
    metrics = ["Relative\nrisk", "ARR", "NNT"]
    severe = [0.80, 0.10, 10]
    mild = [0.80, 0.01, 100]
    # normalize for dual display: show as table-like bars for ARR and NNT, note RR equal
    ax.axis("off")
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 6)
    ax.set_title("Same RR, different decisions", fontsize=10, fontweight="bold", color=INDIGO)
    rows = [
        (4.8, "Metric", "Severe", "Mild", True),
        (3.7, "RR", "0.80", "0.80", False),
        (2.6, "ARR", "10%", "1%", False),
        (1.5, "NNT", "10", "100", False),
        (0.4, "Clinical weight", "High absolute\nbenefit", "Tiny absolute\nbenefit", False),
    ]
    for y, a, b, c, header in rows:
        fc = "#E8EAF6" if header else WHITE
        for i, (text, x0) in enumerate([(a, 0.4), (b, 3.4), (c, 6.6)]):
            ax.add_patch(
                FancyBboxPatch(
                    (x0, y - 0.35),
                    2.8,
                    0.9,
                    boxstyle="round,pad=0.03,rounding_size=0.08",
                    facecolor=fc if i == 0 or header else ("#E8F5E9" if i == 1 else "#FFF8E1"),
                    edgecolor=INDIGO,
                    lw=1.0,
                )
            )
            ax.text(
                x0 + 1.4,
                y + 0.1,
                text,
                ha="center",
                va="center",
                fontsize=8 if not header else 9,
                fontweight="bold" if header or i == 0 else "normal",
                color=INDIGO if header or i == 0 else SLATE,
            )
    fig.suptitle(
        "Absolute HTE from constant RR × baseline risk (synthetic)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch13_abs_vs_rel_hte.png")


def fig_ch13_stratum_pvalue_fallacy() -> Path:
    """Identical RR; different n → different stratum p-values (ch13)."""
    fig, ax = plt.subplots(figsize=(8.5, 4.6))
    # forest-style: men n=750, women n=250, same RR 0.75
    rows = [
        ("Overall (n=1000)", 0.75, 0.62, 0.90, True),
        ("Men (n=750)", 0.75, 0.60, 0.93, True),
        ("Women (n=250)", 0.75, 0.48, 1.17, False),
    ]
    y = np.arange(len(rows))[::-1]
    for yi, (lab, pe, lo, hi, sig) in zip(y, rows):
        color = TEAL if sig else CORAL
        ax.plot([lo, hi], [yi, yi], color=color, lw=2.4)
        ax.plot(pe, yi, "o", color=color, markersize=10)
        ax.text(0.38, yi, lab, ha="right", va="center", fontsize=9, color=SLATE)
        tag = "p < 0.05" if sig else "p = 0.18 (CI crosses 1)"
        ax.text(1.28, yi, tag, ha="left", va="center", fontsize=8, color=color)
    ax.axvline(1.0, color=SLATE, ls="--", lw=1.2)
    ax.set_xscale("log")
    ax.set_xlim(0.4, 1.5)
    ax.set_yticks([])
    ax.set_xlabel("Risk ratio (log scale, synthetic)")
    ax.set_title(
        "Significance fallacy: same RR, power-driven stratum p-values",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
    )
    ax.text(
        0.75,
        -0.85,
        "Point estimates identical (RR 0.75). Interaction p ≈ 1.0.\n"
        "Do not declare 'works only in men' from unequal precision.",
        ha="center",
        fontsize=8.5,
        color=SLATE,
        transform=ax.get_xaxis_transform(),
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    ax.set_ylim(-0.6, 2.6)
    ax.grid(True, axis="x", alpha=0.25)
    return _save(fig, "cycle1_ch13_stratum_pvalue_fallacy.png")


def fig_ch14_prevalence_ppv() -> Path:
    """Prevalence shift destroys PPV for fixed Se/Sp (ch14)."""
    fig, axes = plt.subplots(1, 2, figsize=(10.0, 4.6))

    se, sp = 0.95, 0.90
    prevalences = np.array([0.50, 0.20, 0.10, 0.03])
    # PPV = Se*p / (Se*p + (1-Sp)*(1-p))
    ppv = (se * prevalences) / (se * prevalences + (1 - sp) * (1 - prevalences))

    ax = axes[0]
    colors = [TEAL, "#00897B", GOLD, CORAL]
    bars = ax.bar(
        [f"{int(p * 100)}%" for p in prevalences],
        ppv * 100,
        color=colors,
        edgecolor=INDIGO,
        width=0.65,
    )
    ax.set_ylabel("Positive predictive value (%)")
    ax.set_xlabel("True prevalence in deployment setting")
    ax.set_ylim(0, 100)
    ax.set_title("Fixed Se=95%, Sp=90% → PPV collapses", fontsize=10, fontweight="bold", color=INDIGO)
    for b, v in zip(bars, ppv):
        ax.text(b.get_x() + b.get_width() / 2, v * 100 + 2, f"{v * 100:.0f}%", ha="center", fontsize=8)
    ax.axhline(50, ls=":", color=SLATE, lw=1)
    ax.text(3.0, 52, "coin-flip territory", fontsize=7.5, color=SLATE, ha="right")

    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Community ED example (prev 3%, n=1000)", fontsize=10, fontweight="bold", color=INDIGO)
    # natural frequencies box
    text = (
        "True LVO: 30\n"
        "Non-LVO: 970\n\n"
        f"TP = 0.95 × 30 = 28.5 ≈ 28\n"
        f"FP = 0.10 × 970 = 97\n\n"
        "PPV = 28 / (28 + 97) ≈ 22%\n"
        "→ ~4 of 5 alerts are false"
    )
    ax.add_patch(
        FancyBboxPatch(
            (0.8, 1.0),
            8.4,
            6.2,
            boxstyle="round,pad=0.12,rounding_size=0.15",
            facecolor="#FFEBEE",
            edgecolor=CORAL,
            lw=1.6,
        )
    )
    ax.text(5.0, 4.2, text, ha="center", va="center", fontsize=10, color=SLATE, family="monospace")
    fig.suptitle(
        "AI transportability: prevalence shift (synthetic Bayes teaching figure)",
        fontsize=11,
        fontweight="bold",
        color=INDIGO,
        y=1.02,
    )
    fig.tight_layout()
    return _save(fig, "cycle1_ch14_prevalence_ppv.png")


def fig_ch15_jc_agenda() -> Path:
    """45–60 minute decision-focused journal club agenda (ch15)."""
    fig, ax = plt.subplots(figsize=(10.5, 4.2))
    ax.set_xlim(0, 60)
    ax.set_ylim(0, 5)
    ax.axis("off")
    ax.set_title(
        "Decision-Focused Journal Club Agenda (45–60 min)",
        fontsize=12,
        fontweight="bold",
        color=INDIGO,
        pad=10,
    )
    segments = [
        (0, 3, "Hook &\nstake", TEAL),
        (3, 5, "PICO /\nestimand", TEAL),
        (8, 10, "Methods\nmap", INDIGO),
        (18, 10, "Absolute\nresults", GREEN),
        (28, 10, "Red-flag\nchecklist", GOLD),
        (38, 10, "Applicability\n& equity", "#EF6C00"),
        (48, 7, "Decide +\ndissent", CORAL),
        (55, 5, "Pearl", SLATE),
    ]
    for start, dur, lab, color in segments:
        ax.add_patch(
            FancyBboxPatch(
                (start + 0.15, 1.6),
                dur - 0.3,
                2.2,
                boxstyle="round,pad=0.02,rounding_size=0.08",
                facecolor=color,
                edgecolor=WHITE,
                lw=1.0,
                alpha=0.92,
            )
        )
        ax.text(
            start + dur / 2,
            2.7,
            lab,
            ha="center",
            va="center",
            fontsize=7.5 if dur < 6 else 8,
            color=WHITE,
            fontweight="bold",
        )
        ax.text(start + dur / 2, 1.25, f"{start}", ha="center", fontsize=7, color=SLATE)
    ax.annotate(
        "",
        xy=(60, 1.0),
        xytext=(0, 1.0),
        arrowprops=dict(arrowstyle="->", color=SLATE, lw=1.4),
    )
    ax.text(30, 0.55, "Minutes (timebox protects methods + absolute effects)", ha="center", fontsize=8.5, color=SLATE)
    ax.text(
        30,
        4.55,
        "Never let pathophysiology fill the hour. Force ARR/NNT and a bottom-line decision.",
        ha="center",
        fontsize=8.5,
        color=SLATE,
        bbox=dict(boxstyle="round", facecolor=LIGHT, edgecolor="#B0BEC5"),
    )
    return _save(fig, "cycle1_ch15_jc_agenda.png")


def fig_ch16_decision_matrix() -> Path:
    """Autopsy bottom-line decision matrix (ch16)."""
    fig, ax = plt.subplots(figsize=(9.5, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title(
        "Paper Autopsy Bottom Line: Four Decision Buckets",
        fontsize=12,
        fontweight="bold",
        color=INDIGO,
        pad=8,
    )
    cells = [
        (0.4, 4.2, "ACT", "Internally valid;\nimportant absolute\neffect; transportable\nto our system", GREEN, "#E8F5E9"),
        (5.1, 4.2, "CONDITIONAL", "Valid core claim,\nbut needs local\nops/equity gate\nor limited subgroup", TEAL, "#E0F2F1"),
        (0.4, 0.5, "WATCH", "Promising signal;\nreplication, calibration,\nor external site data\nrequired first", GOLD, "#FFF8E1"),
        (5.1, 0.5, "NO CHANGE", "Design cannot support\nthe claim; spin or\nirreparable bias;\npathway stays put", CORAL, "#FFEBEE"),
    ]
    for x, y, title, body, edge, face in cells:
        ax.add_patch(
            FancyBboxPatch(
                (x, y),
                4.4,
                3.2,
                boxstyle="round,pad=0.1,rounding_size=0.15",
                facecolor=face,
                edgecolor=edge,
                lw=2.0,
            )
        )
        ax.text(x + 2.2, y + 2.5, title, ha="center", fontsize=12, fontweight="bold", color=edge)
        ax.text(x + 2.2, y + 1.2, body, ha="center", va="center", fontsize=9, color=SLATE)
    ax.text(
        5.0,
        7.55,
        "Map claim → design capacity → absolute effect → transport → one of four actions.",
        ha="center",
        fontsize=8.5,
        color=SLATE,
    )
    return _save(fig, "cycle1_ch16_decision_matrix.png")


def main() -> None:
    gens = [
        fig_ch11_dichotomy_loss,
        fig_ch11_km_vs_cif,
        fig_ch13_abs_vs_rel_hte,
        fig_ch13_stratum_pvalue_fallacy,
        fig_ch14_prevalence_ppv,
        fig_ch15_jc_agenda,
        fig_ch16_decision_matrix,
    ]
    print(f"Generating {len(gens)} cycle-1 densification figures → {OUT}")
    for g in gens:
        g()
    print("DONE")


if __name__ == "__main__":
    main()
