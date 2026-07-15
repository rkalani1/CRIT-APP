#!/usr/bin/env python3
"""Wire cycleXX_swarm_chNN_*.png embeds into curriculum chapters after last densify block."""
from __future__ import annotations
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURR = ROOT / "docs" / "curriculum"
FIG = ROOT / "docs" / "assets" / "figures"


def chapter_file(n: int) -> Path:
    matches = sorted(CURR.glob(f"{n:02d}-*.md"))
    if not matches:
        raise FileNotFoundError(f"No chapter for {n:02d}")
    return matches[0]


def find_png(cycle: int, ch: int) -> Path:
    hits = sorted(FIG.glob(f"cycle{cycle}_swarm_ch{ch:02d}_*.png"))
    if not hits:
        raise FileNotFoundError(f"No PNG for cycle{cycle} ch{ch:02d}")
    return hits[0]


def wire(cycle: int, chapters: range, label: str) -> int:
    n_wired = 0
    for ch in chapters:
        png = find_png(cycle, ch)
        rel = f"../assets/figures/{png.name}"
        path = chapter_file(ch)
        text = path.read_text(encoding="utf-8")
        if png.name in text:
            print(f"  skip ch{ch:02d} already wired {png.name}")
            continue
        block = (
            f"![Cycle densify scientific residual for chapter {ch:02d} "
            f"(original scientific teaching figure).]({rel})\n\n"
            f"*Teaching figure (synthetic).* {label}\n\n"
        )
        # Insert after last densify teaching-figure italic line, else after first teaching figure block
        pattern = re.compile(
            r"(\*Teaching figure \(synthetic\)\.\*[^\n]*\n)",
            re.M,
        )
        matches = list(pattern.finditer(text))
        if matches:
            m = matches[0]  # near top densify cluster
            # Prefer the most recent densify residual caption near the top (first 80 lines zone)
            top = [x for x in matches if x.start() < 4000]
            m = top[-1] if top else matches[0]
            insert_at = m.end()
            # ensure blank line separation
            text = text[:insert_at] + "\n" + block + text[insert_at:]
        else:
            # fallback: after first heading block
            lines = text.splitlines(keepends=True)
            insert_line = min(40, len(lines))
            text = "".join(lines[:insert_line]) + "\n" + block + "".join(lines[insert_line:])
        path.write_text(text, encoding="utf-8")
        print(f"  wired ch{ch:02d} <- {png.name}")
        n_wired += 1
    return n_wired


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: wire_cycle_swarm_figures.py <cycle> [early|late|all]")
        return 2
    cycle = int(argv[1])
    half = argv[2] if len(argv) > 2 else "all"
    if half == "early":
        chapters = range(1, 15)
        label = f"Cycle-{cycle} densify scientific residual (ch01–14)."
    elif half == "late":
        chapters = range(15, 29)
        label = f"Cycle-{cycle} densify scientific residual (ch15–28)."
    else:
        chapters = range(1, 29)
        label = f"Cycle-{cycle} densify scientific residual."
    print(f"Wire cycle {cycle} half={half}")
    n = wire(cycle, chapters, label)
    print(f"Wired {n} chapters")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
