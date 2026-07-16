#!/usr/bin/env python3
"""Regenerate the small set of accuracy-critical CRIT-APP teaching figures.

The figures are intentionally dependency-free and deterministic.  Numeric
claims are asserted here so that a visual cannot silently drift away from the
chapter text.
"""
from __future__ import annotations

import argparse
import math
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIGURE_DIR = ROOT / "docs" / "assets" / "figures"

INK = "#1e1b4b"
MUTED = "#475569"
PRIMARY = "#4f46e5"
DEEP = "#3730a3"
TEAL = "#0f766e"
RED = "#b91c1c"
GOLD = "#a16207"
GRID = "#cbd5e1"
SURFACE = "#f8fafc"
WHITE = "#ffffff"


def svg_shell(title: str, description: str, body: str, height: int = 720) -> str:
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1200 {height}" role="img" aria-labelledby="title desc">
  <title id="title">{title}</title>
  <desc id="desc">{description}</desc>
  <rect width="1200" height="{height}" rx="28" fill="{SURFACE}"/>
  <style>
    text {{ font-family: "Source Sans 3", "Segoe UI", Arial, sans-serif; fill: {INK}; }}
    .title {{ font-size: 34px; font-weight: 700; }}
    .subtitle {{ font-size: 21px; fill: {MUTED}; }}
    .label {{ font-size: 20px; font-weight: 650; }}
    .small {{ font-size: 17px; fill: {MUTED}; }}
    .value {{ font-size: 24px; font-weight: 700; }}
  </style>
{body}
</svg>
'''


def roc_figure() -> str:
    target_auc = 0.83
    exponent = 1.0 / target_auc - 1.0
    calculated_auc = 1.0 / (exponent + 1.0)
    assert math.isclose(calculated_auc, target_auc, rel_tol=0, abs_tol=1e-12)

    left, top, width, height = 130.0, 135.0, 930.0, 455.0

    def point(fpr: float) -> tuple[float, float, float]:
        tpr = fpr**exponent if fpr else 0.0
        return left + fpr * width, top + (1.0 - tpr) * height, tpr

    curve = " ".join(
        ("M" if i == 0 else "L") + f" {x:.2f} {y:.2f}"
        for i in range(101)
        for x, y, _ in [point(i / 100)]
    )
    x1, y1, tpr1 = point(0.10)
    x2, y2, tpr2 = point(0.40)
    assert math.isclose(tpr1, 0.624, abs_tol=0.001)
    assert math.isclose(tpr2, 0.829, abs_tol=0.001)

    grid_lines = []
    tick_labels = []
    for i in range(6):
        value = i / 5
        x = left + value * width
        y = top + (1 - value) * height
        grid_lines.append(f'  <path d="M {x:.1f} {top:.1f} V {top + height:.1f}" stroke="{GRID}" stroke-width="1"/>')
        grid_lines.append(f'  <path d="M {left:.1f} {y:.1f} H {left + width:.1f}" stroke="{GRID}" stroke-width="1"/>')
        tick_labels.append(f'  <text x="{x:.1f}" y="{top + height + 31:.1f}" text-anchor="middle" class="small">{value:.1f}</text>')
        tick_labels.append(f'  <text x="{left - 22:.1f}" y="{y + 6:.1f}" text-anchor="end" class="small">{value:.1f}</text>')

    body = f'''  <text x="70" y="58" class="title">ROC performance and operating thresholds</text>
  <text x="70" y="91" class="subtitle">Synthetic ROC curve with AUROC = {target_auc:.2f}; each threshold chooses a different error trade-off.</text>
{chr(10).join(grid_lines)}
  <path d="M {left:.1f} {top + height:.1f} L {left + width:.1f} {top:.1f}" stroke="{MUTED}" stroke-width="3" stroke-dasharray="10 10"/>
  <path d="{curve}" fill="none" stroke="{PRIMARY}" stroke-width="8" stroke-linecap="round" stroke-linejoin="round"/>
  <circle cx="{x1:.1f}" cy="{y1:.1f}" r="10" fill="{WHITE}" stroke="{DEEP}" stroke-width="6"/>
  <path d="M {x1 + 10:.1f} {y1 + 8:.1f} L 360 365" fill="none" stroke="{DEEP}" stroke-width="2"/>
  <rect x="348" y="350" width="330" height="70" rx="12" fill="{WHITE}" stroke="{GRID}"/>
  <text x="368" y="378" class="label">More specific threshold</text>
  <text x="368" y="404" class="small">FPR 0.10 · sensitivity {tpr1:.2f}</text>
  <circle cx="{x2:.1f}" cy="{y2:.1f}" r="10" fill="{WHITE}" stroke="{GOLD}" stroke-width="6"/>
  <path d="M {x2 + 10:.1f} {y2 - 6:.1f} L 665 165" fill="none" stroke="{GOLD}" stroke-width="2"/>
  <rect x="653" y="130" width="350" height="70" rx="12" fill="{WHITE}" stroke="{GRID}"/>
  <text x="673" y="158" class="label">More sensitive threshold</text>
  <text x="673" y="184" class="small">FPR 0.40 · sensitivity {tpr2:.2f}</text>
{chr(10).join(tick_labels)}
  <text x="{left + width / 2:.1f}" y="665" text-anchor="middle" class="label">False-positive rate (1 − specificity)</text>
  <text x="39" y="{top + height / 2:.1f}" text-anchor="middle" class="label" transform="rotate(-90 39 {top + height / 2:.1f})">True-positive rate (sensitivity)</text>
  <text x="1040" y="560" text-anchor="end" class="small">Chance line</text>'''
    return svg_shell(
        "ROC performance and operating thresholds",
        "A synthetic receiver operating characteristic curve with area 0.83. A false-positive rate of 0.10 has sensitivity 0.62, while a false-positive rate of 0.40 has sensitivity 0.83.",
        body,
    )


def fisher_two_sided(a: int, b: int, c: int, d: int) -> float:
    """Two-sided Fisher exact p-value using the probability-ordering definition."""
    row1 = a + b
    row2 = c + d
    col1 = a + c
    total = row1 + row2
    low = max(0, col1 - row2)
    high = min(row1, col1)

    def probability(x: int) -> float:
        return math.comb(row1, x) * math.comb(row2, col1 - x) / math.comb(total, col1)

    observed = probability(a)
    return sum(probability(x) for x in range(low, high + 1) if probability(x) <= observed + 1e-15)


def fragility_figure() -> str:
    control_events = 40
    treatment_events = 22
    per_arm = 200
    initial_p = fisher_two_sided(control_events, per_arm - control_events, treatment_events, per_arm - treatment_events)
    assert math.isclose(initial_p, 0.018316, rel_tol=0, abs_tol=0.000001)

    fragility_index = 0
    changed_p = initial_p
    while changed_p < 0.05:
        fragility_index += 1
        changed_p = fisher_two_sided(
            control_events,
            per_arm - control_events,
            treatment_events + fragility_index,
            per_arm - treatment_events - fragility_index,
        )
    assert fragility_index == 3
    assert math.isclose(changed_p, 0.057172, rel_tol=0, abs_tol=0.000001)

    def bar(x: int, y: int, label: str, events: int, color: str) -> str:
        track_width = 250
        fill_width = events / per_arm * track_width
        return f'''  <text x="{x}" y="{y - 11}" class="label">{label}</text>
  <rect x="{x}" y="{y}" width="{track_width}" height="34" rx="9" fill="#e2e8f0"/>
  <rect x="{x}" y="{y}" width="{fill_width:.1f}" height="34" rx="9" fill="{color}"/>
  <text x="{x + track_width + 18}" y="{y + 25}" class="value">{events}/{per_arm}</text>'''

    body = f'''  <text x="70" y="58" class="title">Fragility is test- and direction-specific</text>
  <text x="70" y="91" class="subtitle">Specified example: unfavorable events, equal groups, two-sided Fisher exact test, α = 0.05.</text>
  <rect x="70" y="130" width="480" height="370" rx="22" fill="{WHITE}" stroke="{GRID}" stroke-width="2"/>
  <text x="105" y="180" class="title">Reported result</text>
  <text x="105" y="215" class="subtitle">40 vs 22 unfavorable events</text>
{bar(105, 270, "Control", control_events, RED)}
{bar(105, 365, "Treatment", treatment_events, TEAL)}
  <text x="105" y="470" class="value">Fisher p = {initial_p:.4f}</text>
  <path d="M 575 310 H 625" stroke="{DEEP}" stroke-width="5" stroke-linecap="round"/>
  <path d="M 614 296 L 630 310 L 614 324" fill="none" stroke="{DEEP}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="600" y="350" text-anchor="middle" class="small">3 outcomes</text>
  <text x="600" y="374" text-anchor="middle" class="small">reclassified</text>
  <rect x="650" y="130" width="480" height="370" rx="22" fill="{WHITE}" stroke="{GRID}" stroke-width="2"/>
  <text x="685" y="180" class="title">Tipping point</text>
  <text x="685" y="215" class="subtitle">40 vs 25 unfavorable events</text>
{bar(685, 270, "Control", control_events, RED)}
{bar(685, 365, "Treatment", treatment_events + fragility_index, GOLD)}
  <text x="685" y="470" class="value">Fisher p = {changed_p:.4f}</text>
  <rect x="150" y="550" width="900" height="105" rx="20" fill="#eef2ff" stroke="#c7d2fe" stroke-width="2"/>
  <text x="600" y="592" text-anchor="middle" class="title">Fragility index = {fragility_index}</text>
  <text x="600" y="628" text-anchor="middle" class="subtitle">Three treatment non-events changed to events move p from below to above 0.05.</text>'''
    return svg_shell(
        "Fragility index worked example",
        "With 40 unfavorable events among 200 control participants and 22 among 200 treatment participants, the two-sided Fisher exact p-value is 0.0183. Reclassifying three treatment non-events as events gives 25 of 200 and p 0.0572, so the fragility index is 3 for this specified test and direction.",
        body,
    )


def natural_frequency_figure() -> str:
    persistent_events = 6
    prevented_events = 2
    no_events = 92
    assert persistent_events + prevented_events + no_events == 100
    without_strategy = persistent_events + prevented_events
    with_strategy = persistent_events
    assert (without_strategy, with_strategy, prevented_events) == (8, 6, 2)

    circles = []
    for index in range(100):
        row, column = divmod(index, 10)
        x = 94 + column * 45
        y = 175 + row * 43
        if index < persistent_events:
            fill, stroke = RED, RED
            label = "event with either strategy"
        elif index < persistent_events + prevented_events:
            fill, stroke = "#ccfbf1", TEAL
            label = "event prevented by the strategy"
        else:
            fill, stroke = "#e2e8f0", "#94a3b8"
            label = "no event"
        circles.append(
            f'  <circle cx="{x}" cy="{y}" r="14" fill="{fill}" stroke="{stroke}" stroke-width="{4 if index < 8 else 2}"><title>Person {index + 1}: {label}</title></circle>'
        )

    body = f'''  <text x="70" y="58" class="title">Natural frequencies: 2 fewer events per 100 people</text>
  <text x="70" y="91" class="subtitle">Illustrative absolute effects over the stated time horizon.</text>
{chr(10).join(circles)}
  <rect x="610" y="150" width="510" height="420" rx="24" fill="{WHITE}" stroke="{GRID}" stroke-width="2"/>
  <text x="655" y="210" class="title">Read the 100-person grid</text>
  <circle cx="675" cy="266" r="15" fill="{RED}"/>
  <text x="710" y="274" class="label">6 experience the outcome</text>
  <text x="710" y="301" class="small">with or without the strategy</text>
  <circle cx="675" cy="355" r="15" fill="#ccfbf1" stroke="{TEAL}" stroke-width="4"/>
  <text x="710" y="363" class="label">2 additional outcomes without it</text>
  <text x="710" y="390" class="small">shown as outcomes prevented by the strategy</text>
  <circle cx="675" cy="444" r="15" fill="#e2e8f0" stroke="#94a3b8" stroke-width="2"/>
  <text x="710" y="452" class="label">92 do not experience the outcome</text>
  <text x="710" y="479" class="small">under either strategy in this illustration</text>
  <path d="M 655 518 H 1075" stroke="{GRID}" stroke-width="2"/>
  <text x="655" y="551" class="value">8 without strategy → 6 with strategy</text>
  <text x="70" y="660" class="subtitle">This is a group-level contrast: it does not identify which two people would benefit.</text>'''
    return svg_shell(
        "Natural-frequency icon array",
        "A 100-person array shows six red people who experience the outcome with either strategy, two outlined teal people whose outcomes are prevented by the strategy, and 92 gray people with no outcome. This represents eight events without the strategy and six with it, or two fewer per 100.",
        body,
    )


def figures() -> dict[str, str]:
    return {
        "fig73_roc_operating.svg": roc_figure(),
        "swarm_ch27_fragility_missing.svg": fragility_figure(),
        "swarm_ch28_natural_frequencies.svg": natural_frequency_figure(),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="Fail if tracked figures differ from deterministic output.")
    args = parser.parse_args()
    expected = figures()

    if args.check:
        stale = [name for name, content in expected.items() if not (FIGURE_DIR / name).is_file() or (FIGURE_DIR / name).read_text(encoding="utf-8") != content]
        if stale:
            print("ACCURACY_FIGURES_STALE " + ", ".join(stale))
            return 1
        print(f"ACCURACY_FIGURES_OK {len(expected)}")
        return 0

    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    for name, content in expected.items():
        (FIGURE_DIR / name).write_text(content, encoding="utf-8", newline="\n")
        print(f"WROTE {FIGURE_DIR / name}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
