#!/usr/bin/env python3
"""Continuous densify wave runner for CRIT-APP.

Writes cycle generator scripts, generates Agg indigo scientific figures,
wires embeds, and reports counts. One half-book wave (14 chapters) per call.

Usage:
  python scripts/_densify_wave_runner.py <cycle> early|late
"""
from __future__ import annotations

import sys
import textwrap
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"
OUT = ROOT / "docs" / "assets" / "figures"

# Chapter teaching titles (ARR/NNT / pred≠cause literate)
TITLES = {
    1: "absolute risk framing beats relative-only claims",
    2: "under time pressure, extract ARR and NNT first",
    3: "PICO index time fixes the absolute estimand",
    4: "bias taxonomy mapped to absolute distortion",
    5: "DAG confounding shifts absolute event rates",
    6: "RCT arms: control vs treated absolute risks",
    7: "observational residual confounding vs ARR",
    8: "sensitivity/specificity feed absolute post-test risk",
    9: "prediction is not causation — calibrate absolute risk",
    10: "pooled absolute effects, not relative alone",
    11: "mRS shift as absolute outcome distribution",
    12: "ARR and NNT are the clinical importance core",
    13: "subgroup interaction needs absolute contrast",
    14: "AI model discrimination ≠ causal effect",
    15: "journal club absolute-risk board completeness",
    16: "autopsy flow ends in absolute action codes",
    17: "cumulative incidence is absolute risk over time",
    18: "causal contrast of potential outcome risks",
    19: "CI width on the absolute risk scale",
    20: "landmark survival ARR after index time",
    21: "effect modification on absolute risk difference",
    22: "overdiagnosis inflates apparent absolute benefit",
    23: "cognitive bias distorts absolute risk perception",
    24: "therapy harm: absolute risk increase and NNH",
    25: "diagnosis/prognosis absolute calibration check",
    26: "CPR absolute net benefit vs treat-all/none",
    27: "missingness and fragility of absolute estimates",
    28: "systems of care: absolute door-to-needle gains",
}

FIG_KINDS = [
    "line_arr",
    "bar_risks",
    "cuminc",
    "barh_scores",
    "forest_rd",
    "nnt_curve",
    "calib",
    "stacked_mrs",
]


def gen_fig_body(ch: int, cycle: int, kind: str, idx: int) -> str:
    """Return Python source for one figure function body (indented)."""
    title = TITLES[ch]
    fname = f"cycle{cycle}_swarm_ch{ch:02d}_w{cycle}_{idx}.png"
    seed = cycle * 100 + ch

    if kind == "line_arr":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            rng = np.random.default_rng({seed})
            x = np.arange(0, 7)
            ctrl = 22 + 0.4 * x + rng.normal(0, 0.15, size=len(x))
            trt = ctrl - (3.5 + 0.35 * x)
            ax.plot(x, ctrl, "o-", color=CORAL, lw=2.3, label="Control abs risk %")
            ax.plot(x, trt, "s-", color=TEAL, lw=2.3, label="Treated abs risk %")
            ax.fill_between(x, trt, ctrl, color=INDIGO, alpha=0.12, label="ARR band")
            ax.set_xlabel("Horizon step"); ax.set_ylabel("Absolute risk %")
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "bar_risks":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            labels = ["Y1", "Y0", "ARR", "NNT"]
            y1, y0 = 12 + ({ch} % 5), 18 + ({ch} % 4)
            arr = y0 - y1
            nnt = round(100 / arr, 1) if arr else 0
            vals = [y1, y0, arr, nnt]
            colors = [TEAL, CORAL, INDIGO, GOLD]
            ax.bar(labels, vals, color=colors, edgecolor=SLATE)
            ax.set_ylabel("Abs risk % / pp / patients")
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3, axis="y"); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "cuminc":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            t = np.linspace(0, 24, 100)
            c = 100 * (1 - np.exp(-({0.02 + (ch % 5) * 0.004}) * t))
            tr = 100 * (1 - np.exp(-({0.014 + (ch % 5) * 0.003}) * t))
            ax.plot(t, c, color=CORAL, lw=2.3, label="Control cum inc %")
            ax.plot(t, tr, color=TEAL, lw=2.3, label="Treated cum inc %")
            ax.fill_between(t, tr, c, color=INDIGO, alpha=0.12, label="ARR(t)")
            ax.set_xlabel("Months"); ax.set_ylabel("Absolute cumulative incidence %")
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "barh_scores":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            labels = ["Internal val", "External val", "Abs report", "Actionable"]
            base = np.array([0.55, 0.45, 0.35, 0.40]) + ({cycle % 7}) * 0.02 + ({ch % 4}) * 0.03
            base = np.clip(base, 0.1, 0.95)
            ax.barh(labels, base, color=[TEAL, INDIGO, GOLD, CORAL], edgecolor=SLATE)
            ax.set_xlabel("Absolute appraisal score (0-1)")
            ax.set_xlim(0, 1)
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "forest_rd":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            studies = [f"S{{i}}" for i in range(1, 6)]
            rd = np.array([-2.0, -3.5, -1.2, -4.0, -2.8]) + ({ch % 3}) * 0.3
            lo, hi = rd - 1.8, rd + 1.8
            y = np.arange(len(studies))
            ax.hlines(y, lo, hi, color=SLATE, lw=2)
            ax.plot(rd, y, "o", color=INDIGO, ms=8)
            ax.axvline(0, color=CORAL, ls="--", lw=1.2)
            ax.set_yticks(y); ax.set_yticklabels(studies)
            ax.set_xlabel("Risk difference (pp, absolute)")
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3, axis="x"); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "nnt_curve":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            arr = np.linspace(1.0, 12.0, 40)
            nnt = 100.0 / arr
            ax.plot(arr, nnt, color=TEAL, lw=2.5)
            ax.axhline(50, color=GOLD, ls=":", lw=1.3, label="NNT=50 ref")
            ax.axvline(2.0, color=CORAL, ls="--", lw=1.2, label="ARR=2pp")
            ax.set_xlabel("ARR (percentage points)"); ax.set_ylabel("NNT")
            ax.set_ylim(0, 120)
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    if kind == "calib":
        return textwrap.dedent(
            f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            pred = np.linspace(0.05, 0.55, 8)
            obs = pred + 0.04 * np.sin(pred * 12 + {ch}) - 0.02 * ({cycle % 5})
            ax.plot([0, 0.6], [0, 0.6], "--", color=SLATE, label="Perfect calibration")
            ax.plot(pred, obs, "o-", color=INDIGO, lw=2.2, label="Observed abs risk")
            ax.set_xlabel("Predicted absolute risk"); ax.set_ylabel("Observed absolute risk")
            ax.set_xlim(0, 0.6); ax.set_ylim(0, 0.6)
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.grid(True, alpha=0.3); ax.legend(fontsize=8); fig.tight_layout()
            return _save(fig, "{fname}")
        """
        )
    # stacked_mrs
    return textwrap.dedent(
        f"""\
        def fig_ch{ch:02d}():
            fig, ax = plt.subplots(figsize=(10.4, 5.0))
            cats = ["mRS0", "mRS1", "mRS2", "mRS3", "mRS4-5", "mRS6"]
            ctrl = np.array([8, 12, 18, 22, 25, 15], dtype=float)
            trt = np.array([12, 16, 20, 20, 20, 12], dtype=float)
            ctrl = 100 * ctrl / ctrl.sum(); trt = 100 * trt / trt.sum()
            x = np.arange(2)
            bottom_c = bottom_t = 0
            colors = [TEAL, "#4DB6AC", INDIGO, GOLD, CORAL, SLATE]
            for i, c in enumerate(cats):
                ax.bar(0, ctrl[i], bottom=bottom_c, color=colors[i], edgecolor=WHITE, width=0.55, label=c)
                ax.bar(1, trt[i], bottom=bottom_t, color=colors[i], edgecolor=WHITE, width=0.55)
                bottom_c += ctrl[i]; bottom_t += trt[i]
            ax.set_xticks([0, 1]); ax.set_xticklabels(["Control", "Treated"])
            ax.set_ylabel("Absolute % of patients")
            ax.set_title("Ch{ch:02d} residual: {title} (C{cycle})", fontsize=11, fontweight="bold", color=INDIGO)
            ax.legend(fontsize=7, ncol=3, loc="upper center", bbox_to_anchor=(0.5, -0.08))
            ax.set_ylim(0, 100); fig.tight_layout()
            return _save(fig, "{fname}")
        """
    )


def write_generator(cycle: int, chapters: list[int], half: str) -> Path:
    fns = []
    bodies = []
    for i, ch in enumerate(chapters, start=1):
        kind = FIG_KINDS[(cycle + ch + i) % len(FIG_KINDS)]
        bodies.append(gen_fig_body(ch, cycle, kind, i))
        fns.append(f"fig_ch{ch:02d}")

    src = f'''#!/usr/bin/env python3
"""CRIT-APP Cycle-{cycle} densify ({half}). Agg indigo. ARR/NNT. pred!=cause."""
from __future__ import annotations
from pathlib import Path
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "docs" / "assets" / "figures"
INDIGO, TEAL, GOLD, CORAL, SLATE, WHITE = "#283593", "#00695C", "#F9A825", "#C62828", "#37474F", "#FFFFFF"

def _save(fig, name):
    p = OUT / name
    fig.savefig(p, dpi=180, bbox_inches="tight", facecolor=WHITE)
    plt.close(fig)
    print("  wrote", p.name)
    return p

'''
    src += "\n\n".join(bodies)
    src += f'''

def main():
    print("Cycle-{cycle}", OUT)
    for fn in [{", ".join(fns)}]:
        fn()
    print("Done: {len(chapters)}")

if __name__ == "__main__":
    main()
'''
    path = SCRIPTS / f"generate_cycle{cycle}_swarm_figures.py"
    path.write_text(src, encoding="utf-8")
    print(f"wrote {path.name}")
    return path


def main(argv: list[str]) -> int:
    if len(argv) < 3:
        print("Usage: _densify_wave_runner.py <cycle> early|late")
        return 2
    cycle = int(argv[1])
    half = argv[2]
    if half == "early":
        chapters = list(range(1, 15))
    elif half == "late":
        chapters = list(range(15, 29))
    else:
        print("half must be early|late")
        return 2
    OUT.mkdir(parents=True, exist_ok=True)
    write_generator(cycle, chapters, half)
    # Execute generator
    import importlib.util
    gen_path = SCRIPTS / f"generate_cycle{cycle}_swarm_figures.py"
    spec = importlib.util.spec_from_file_location(f"gen_c{cycle}", gen_path)
    mod = importlib.util.module_from_spec(spec)
    assert spec.loader is not None
    spec.loader.exec_module(mod)
    mod.main()
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
