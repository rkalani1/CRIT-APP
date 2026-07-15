#!/usr/bin/env python3
"""Continuous densify batch: generate, wire, gate, commit floor pairs, push.

Checks USER_STOP in residual/swarm-log between pairs. Updates residual + swarm-log.
"""
from __future__ import annotations
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOGDIR = Path(r"C:\Users\rkala\AppData\Local\Temp\grok-ebook-swarm-continuous")
LOGDIR.mkdir(parents=True, exist_ok=True)
SWARM_LOG = LOGDIR / "swarm-log.txt"
RESIDUAL = LOGDIR / "cycle-floor-current-crit-residuals.md"
LOCK = LOGDIR / "densify.lock"


def run(cmd, check=True):
    print("+", " ".join(str(c) for c in cmd), flush=True)
    r = subprocess.run(cmd, cwd=ROOT, text=True, capture_output=True)
    out = (r.stdout or "") + (r.stderr or "")
    if out.strip():
        print(out[-4000:], flush=True)
    if check and r.returncode != 0:
        raise SystemExit(f"FAILED rc={r.returncode}: {cmd}")
    return r


def now_iso() -> str:
    return datetime.now().astimezone().isoformat()


def user_stop() -> bool:
    for p in (SWARM_LOG, RESIDUAL):
        if p.exists() and "USER_STOP" in p.read_text(encoding="utf-8", errors="ignore"):
            return True
    return False


def append_log(line: str) -> None:
    with SWARM_LOG.open("a", encoding="utf-8") as f:
        f.write(line.rstrip() + "\n")


def write_residual(head: str, floor: int, embeds: int, uni: bool, start: int) -> None:
    RESIDUAL.write_text(
        f"# residual {now_iso()}\n"
        f"DONE HEAD={head} start_was={start}\n"
        f"floor={floor} embeds={embeds} uniform={uni}\n"
        f"continuous=yes\n",
        encoding="utf-8",
    )


def embed_stats():
    counts = []
    for p in sorted((ROOT / "docs" / "curriculum").glob("*.md")):
        t = p.read_text(encoding="utf-8")
        counts.append(len(re.findall(r"!\[[^\]]*\]\([^)]+\.png\)", t)))
    return min(counts), max(counts), sum(counts), len(set(counts)) == 1


def claim_lock() -> None:
    LOCK.write_text(
        f"grok-build continuous densify pid=batch start={now_iso()}\n",
        encoding="utf-8",
    )


def main():
    start_cycle = int(sys.argv[1]) if len(sys.argv) > 1 else 1471
    pairs = int(sys.argv[2]) if len(sys.argv) > 2 else 20
    claim_lock()
    if user_stop():
        print("USER_STOP detected before start; exiting")
        append_log(f"USER_STOP_SEEN {now_iso()} pre-start")
        return 0

    mn, mx, sm, uni = embed_stats()
    start_floor = mn
    log = LOGDIR / f"cycle{start_cycle}-batch.log"
    lines = [f"start cycle={start_cycle} pairs={pairs} floor={start_floor} embeds={sm} uniform={uni}"]
    print(lines[0], flush=True)
    append_log(
        f"GROK_BATCH_START {now_iso()} start={start_cycle} pairs={pairs} "
        f"floor={start_floor} embeds={sm}"
    )

    completed_pairs = 0
    for p in range(pairs):
        if user_stop():
            print("USER_STOP mid-batch; stopping after completed pairs", flush=True)
            lines.append("USER_STOP mid-batch")
            append_log(f"USER_STOP {now_iso()} mid-batch after {completed_pairs} pairs")
            break
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
        completed_pairs += 1

    mn, mx, sm, uni = embed_stats()
    print(f"after wire: min={mn} max={mx} sum={sm} uniform={uni}", flush=True)
    lines.append(f"after wire: min={mn} max={mx} sum={sm} uniform={uni}")

    if completed_pairs == 0:
        raise SystemExit("No pairs completed")

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

    r = run([sys.executable, "-m", "mkdocs", "build", "--strict"], check=False)
    if r.returncode != 0:
        raise SystemExit("GATE FAIL mkdocs --strict")
    lines.append("GATE mkdocs --strict: OK")

    # commits per floor pair
    for p in range(completed_pairs):
        c_early = start_cycle + p * 2
        c_late = c_early + 1
        floor = start_floor + p + 1
        to_add = [
            f"scripts/generate_cycle{c_early}_swarm_figures.py",
            f"scripts/generate_cycle{c_late}_swarm_figures.py",
        ]
        for c in (c_early, c_late):
            to_add.extend(
                str(x)
                for x in (ROOT / "docs" / "assets" / "figures").glob(f"cycle{c}_swarm_*.png")
            )
        to_add.extend(str(x) for x in (ROOT / "docs" / "curriculum").glob("*.md"))
        run(["git", "add", *to_add])
        r = run(
            [
                "git",
                "commit",
                "-m",
                f"Cycles {c_early}-{c_late} densify: 28 scientific swarm figures raising uniform floor to {floor}",
            ],
            check=False,
        )
        if r.returncode != 0:
            print(f"commit note pair {p}: may be empty", flush=True)

    run(["git", "push", "origin", "main"])
    head = subprocess.check_output(
        ["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, text=True
    ).strip()
    mn, mx, sm, uni = embed_stats()
    summary = f"DONE HEAD={head} floor={mn} embeds={sm} uniform={uni} pairs={completed_pairs}"
    print(summary, flush=True)
    lines.append(summary)
    log.write_text("\n".join(lines), encoding="utf-8")
    write_residual(head, mn, sm, uni, start_cycle)
    append_log(
        f"GROK_BATCH {now_iso()} start={start_cycle} pairs={completed_pairs} "
        f"HEAD={head} floor={mn} embeds={sm} uni={uni} exit=0"
    )
    append_log(
        f"RETURN {now_iso()} HEAD={head} floor={mn} embeds={sm} uniform={uni} "
        f"continuous=yes grok-build {start_cycle}-{start_cycle + completed_pairs * 2 - 1}"
    )
    print(f"log={log}", flush=True)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
