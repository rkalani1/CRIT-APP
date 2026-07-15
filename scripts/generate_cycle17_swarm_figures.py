#!/usr/bin/env python3
"""CRIT-APP Cycle-17 densify: raise uniform floor 10 → toward 11 (wave A).

ch01 absolute opportunity cost of spin
ch04 internal vs external validity absolute transport
ch06 ITT vs per-protocol absolute residual
ch08 spectrum bias absolute Se/Sp distortion
ch11 competing risk absolute CIF vs 1-KM
ch12 RRR marketing vs ARR decision
ch15 journal club absolute roles board

Agg indigo. cycle17_swarm_* only.
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
    plt.close(fig)
    print("  wrote", p.name)
    return p


def fig_ch01():
    fig, ax = plt.subplots(figsize=(10.4, 4.9))
    labs = ["RRR-only\nheadline adopt", "ARR+NNT\nhonest adopt", "Reject\n(invalid)", "Wait\n(imprecise)"]
    # "cost" as wasted pathway-hours / 100 reads (teaching)
    cost = [40, 8, 5, 12]
    cols = [CORAL, TEAL, INDIGO, GOLD]
    ax.bar(range(4), cost, color=cols, edgecolor=INDIGO, width=0.62)
    ax.set_xticks(range(4))
    ax.set_xticklabels(labs, fontsize=9)
    ax.set_ylabel("Pathway-regret units (teaching)")
    ax.set_title("Absolute opportunity cost of appraisal failure modes", fontsize=11, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch01_spin_cost.png")


def fig_ch04():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("Internal validity", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.4, 1), 9.2, 5.5, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#E8EAF6", edgecolor=INDIGO, lw=1.5))
    ax.text(5, 4.5, "For this study sample:\nIs ARR causal?\nRandomization, blinding,\nanalysis set, missingness",
            ha="center", va="center", fontsize=10, fontweight="bold", color=INDIGO)
    ax = axes[1]
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 8)
    ax.axis("off")
    ax.set_title("External / transport", fontsize=10, fontweight="bold", color=INDIGO)
    ax.add_patch(FancyBboxPatch((0.4, 1), 9.2, 5.5, boxstyle="round,pad=0.05,rounding_size=0.1",
                                facecolor="#E0F2F1", edgecolor=TEAL, lw=1.5))
    ax.text(5, 4.5, "For my patients:\nSame absolute baseline?\nSame delivery / lag?\nLocal NNT still honest?",
            ha="center", va="center", fontsize=10, fontweight="bold", color=TEAL)
    fig.suptitle("Bias taxonomy ends on absolute transport of ARR/NNT (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch04_int_ext_abs.png")


def fig_ch06():
    fig, ax = plt.subplots(figsize=(10.2, 4.9))
    x = np.arange(3)
    itt = [4.0, 3.5, 2.0]  # ARR pp
    pp = [7.5, 6.0, 4.5]
    w = 0.35
    ax.bar(x - w / 2, itt, width=w, color=TEAL, edgecolor=INDIGO, label="ITT ARR")
    ax.bar(x + w / 2, pp, width=w, color=CORAL, edgecolor=INDIGO, label="Per-protocol ARR")
    ax.set_xticks(x)
    ax.set_xticklabels(["High\nadherence", "Moderate\ncrossover", "High\ncrossover"], fontsize=9)
    ax.set_ylabel("ARR (pp)")
    ax.set_title("ITT vs per-protocol: absolute residual widens with crossover", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=9)
    ax.grid(True, axis="y", alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch06_itt_pp_arr.png")


def fig_ch08():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    settings = ["Quaternary\nLVO floor", "ED\nmixed", "Clinic\nlow prev"]
    se = [0.94, 0.82, 0.70]
    sp = [0.70, 0.85, 0.92]
    x = np.arange(3)
    w = 0.35
    ax.bar(x - w / 2, se, width=w, color=INDIGO, edgecolor=INDIGO, label="Sensitivity")
    ax.bar(x + w / 2, sp, width=w, color=TEAL, edgecolor=INDIGO, label="Specificity")
    ax.set_xticks(x)
    ax.set_xticklabels(settings, fontsize=9)
    ax.set_ylim(0, 1.05)
    ax.set_ylabel("Operating characteristic")
    ax.set_title("Spectrum shifts Se/Sp", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, axis="y", alpha=0.3)

    ax = axes[1]
    # PPV at fixed Se/Sp with prevalence
    prev = np.array([0.40, 0.10, 0.02])
    se_f, sp_f = 0.90, 0.90
    ppv = (se_f * prev) / (se_f * prev + (1 - sp_f) * (1 - prev))
    ax.bar(range(3), ppv * 100, color=[CORAL, GOLD, TEAL], edgecolor=INDIGO, width=0.6)
    ax.set_xticks(range(3))
    ax.set_xticklabels(["Prev 40%", "Prev 10%", "Prev 2%"], fontsize=9)
    ax.set_ylabel("Absolute PPV (%)")
    ax.set_title("Same Se/Sp → different absolute PPV", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Diagnostic spectrum bias rewrites absolute post-test risk (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch08_spectrum_abs.png")


def fig_ch11():
    fig, ax = plt.subplots(figsize=(10.2, 5.0))
    t = np.linspace(0, 90, 50)
    # crude 1-KM overstates stroke risk when death competes
    cif_stroke = 1 - np.exp(-0.004 * t)
    cif_death = 1 - np.exp(-0.006 * t)
    one_km_naive = 1 - np.exp(-0.004 * t) * 1.35  # inflated teaching
    one_km_naive = np.clip(one_km_naive, 0, 0.55)
    ax.plot(t, cif_stroke * 100, color=TEAL, lw=2.4, label="CIF stroke (competing risk)")
    ax.plot(t, one_km_naive * 100, "--", color=CORAL, lw=2.2, label="Naive 1−KM (ignores death)")
    ax.plot(t, cif_death * 100, ":", color=GRAY, lw=2.0, label="CIF death")
    ax.set_xlabel("Days from t0")
    ax.set_ylabel("Absolute cumulative incidence (%)")
    ax.set_title("Competing risks: absolute CIF vs overstated 1−KM", fontsize=11, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch11_cif_vs_km.png")


def fig_ch12():
    fig, axes = plt.subplots(1, 2, figsize=(10.8, 5.0))
    ax = axes[0]
    baserisk = np.array([2, 5, 10, 20, 40])
    rrr = 0.30
    arr = baserisk * rrr
    ax.plot(baserisk, np.full_like(baserisk, rrr * 100), "o-", color=GOLD, lw=2.2, label="RRR 30% (flat)")
    ax.plot(baserisk, arr, "s-", color=TEAL, lw=2.2, label="ARR (pp)")
    ax.set_xlabel("Baseline risk CER (%)")
    ax.set_ylabel("%")
    ax.set_title("RRR constant; ARR scales with risk", fontsize=10, fontweight="bold", color=INDIGO)
    ax.legend(fontsize=8)
    ax.grid(True, alpha=0.3)

    ax = axes[1]
    nnt = 100 / arr
    ax.bar(range(len(baserisk)), nnt, color=INDIGO, edgecolor=INDIGO, width=0.65)
    ax.set_xticks(range(len(baserisk)))
    ax.set_xticklabels([f"CER {b}%" for b in baserisk], fontsize=8.5, rotation=15)
    ax.set_ylabel("NNT")
    ax.set_title("Same RRR → different absolute NNT", fontsize=10, fontweight="bold", color=INDIGO)
    ax.grid(True, axis="y", alpha=0.3)
    fig.suptitle("Effect sizes: refuse RRR-only marketing; decide on ARR/NNT (synthetic)", fontsize=11, fontweight="bold", color=INDIGO, y=1.02)
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch12_rrr_vs_arr.png")


def fig_ch15():
    fig, ax = plt.subplots(figsize=(10.4, 5.2))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 10)
    ax.axis("off")
    ax.set_title("Journal club absolute roles board", fontsize=11, fontweight="bold", color=INDIGO)
    roles = [
        (8.2, BLUE, "Moderator: lock clinical question + horizon"),
        (6.4, INDIGO, "Methods: bias / t0 / analysis set"),
        (4.6, TEAL, "Quant: CER, EER, ARR, NNT, NNH"),
        (2.8, GOLD, "Transport: local baseline & delivery"),
        (1.0, CORAL, "Action owner: adopt / adapt / wait / reject"),
    ]
    for y, e, t in roles:
        ax.add_patch(
            FancyBboxPatch((0.35, y - 0.6), 9.3, 1.35,
                           boxstyle="round,pad=0.03,rounding_size=0.07",
                           facecolor=WHITE, edgecolor=e, lw=1.5)
        )
        ax.text(0.7, y + 0.05, t, fontsize=10, fontweight="bold", color=e, va="center")
    fig.tight_layout()
    return _save(fig, "cycle17_swarm_ch15_jc_roles_abs.png")


def main():
    print("Cycle-17 →", OUT)
    for fn in [fig_ch01, fig_ch04, fig_ch06, fig_ch08, fig_ch11, fig_ch12, fig_ch15]:
        fn()
    print("Done: 7")


if __name__ == "__main__":
    main()
