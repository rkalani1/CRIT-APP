#!/usr/bin/env python3
"""Continuous densify batch: generate, wire, gate, commit floor pairs, push."""
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGDIR = Path(r"C:\Users\rkala\AppData\Local\Temp\grok-ebook-swarm-continuous")
LOGDIR.mkdir(parents=True, exist_ok=True)

def run(cmd, check=True):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    r = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    out = (r.stdout or "") + (r.stderr or "")
    if out.strip():
        print(out[-4000:], flush=True)
    if check and r.returncode != 0:
        raise SystemExit(f"FAILED rc={r.returncode}: {cmd}")
    return r

def embed_stats():
    counts = []
    for p in sorted((ROOT / "docs" / "curriculum").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        counts.append(len(re.findall(r"!\[[^\]]*\]\([^)]+\.png\)", t)))
    return min(counts), max(counts), sum(counts), len(set(counts)) == 1

def main():
    start_cycle = int(sys.argv[1]) if len(sys.argv) > 1 else 369
    pairs = int(sys.argv[2]) if len(sys.argv) > 2 else 8
    mn, mx, sm, uni = embed_stats()
    start_floor = mn
    log = LOGDIR / f"cycle{start_cycle}-batch.log"
    lines = [f"start cycle={start_cycle} pairs={pairs} floor={start_floor} embeds={sm} uniform={uni}"]
    print(lines[0], flush=True)

    for p in range(pairs):
        c_early = start_cycle + p * 2
        c_late = c_early + 1
        floor = start_floor + p + 1
        msg = f"pair {p}: cycles {c_early}-{c_late} -> floor {floor}"
        print(msg, flush=True)
        lines.append(msg)
        run([sys.executable, "scripts/_densify_wave_runner.py", str(c_early), "early"])
        run([sys.executable, "scripts/_densify_wave_runner.py", str(c_late), "late"])
        run([sys.executable, "scripts/wire_cycle_swarm_figures.py", str(c_early), "early"])
        run([sys.executable, "scripts/wire_cycle_swarm_figures.py", str(c_late), "late"])

    mn, mx, sm, uni = embed_stats()
    print(f"after wire: min={mn} max={mx} sum={sm} uniform={uni}", flush=True)
    lines.append(f"after wire: min={mn} max={mx} sum={sm} uniform={uni}")

    # gates
    for script in [
        "scripts/verify_math_examples.py",
        "scripts/originality_scan.py",
        "scripts/check_figure_coverage.py",
        "scripts/test_ebook_site.py",
    ]:
        r = run([sys.executable, script], check=False)
        if r.returncode != 0:
            raise SystemExit(f"GATE FAIL {script}")
        tail = ((r.stdout or "") + (r.stderr or ""))[-500:]
        lines.append(f"GATE {script}: OK\n{tail}")

    # commits per floor pair
    for p in range(pairs):
        c_early = start_cycle + p * 2
        c_late = c_early + 1
        floor = start_floor + p + 1
        to_add = [
            f"scripts/generate_cycle{c_early}_swarm_figures.py",
            f"scripts/generate_cycle{c_late}_swarm_figures.py",
        ]
        for c in (c_early, c_late):
            to_add.extend(str(x) for x in (ROOT / "docs" / "assets" / "figures").glob(f"cycle{c}_swarm_*.png"))
        to_add.extend(str(x) for x in (ROOT / "docs" / "curriculum").glob("*.md"))
        run(["git", "add", *to_add])
        r = run([
            "git", "commit",
            "-m", f"Cycles {c_early}-{c_late} densify: 28 scientific swarm figures raising uniform floor to {floor}",
        ], check=False)
        if r.returncode != 0:
            print(f"commit note pair {p}: may be empty", flush=True)

    run(["git", "push", "origin", "main"])
    head = subprocess.check_output(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True).strip()
    mn, mx, sm, uni = embed_stats()
    summary = f"DONE HEAD={head} floor={mn} embeds={sm} uniform={uni}"
    print(summary, flush=True)
    lines.append(summary)
    log.write_text("\n".join(lines), encoding="utf-8")
    print(f"log={log}", flush=True)

if __name__ == "__main__":
    main()
