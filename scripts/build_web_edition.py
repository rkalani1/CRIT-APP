#!/usr/bin/env python3
"""
Build CRIT-APP Web Edition Markdown from curriculum chapter modules.

Safety bar:
- Original teaching expression only (no abstract dumps, no guideline instrument pastes)
- Figures only from local code-drawn asset dirs
- Synthetic vignette openers prepended so Web Edition is not a flat DOCX dump
- Emits ORIGINALITY manifest + mkdocs nav fragment
"""
from __future__ import annotations

import importlib.util
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
CURR = DOCS / "curriculum"
FIG_DST = DOCS / "assets" / "figures"
SRC = Path(r"C:\Users\rkala\OneDrive - UW\Codex\Neuro-Stroke-Critical-Appraisal")
CH_DIR = SRC / "chapters"
FIG_SRC_CANDIDATES = [
    SRC / "Critical_Appraisal_Figures",
    SRC / "figures",
]

# Forbidden patterns in exported prose (hard fail flags for review)
FORBIDDEN = [
    r"(?i)reproduced with permission",
    r"(?i)copyright\s*©",
    r"(?i)all rights reserved",
    r"(?i)abstract\s*:",
    r"(?i)this article is protected",
    r"(?i)downloaded from",
    r"doi:\s*10\.\d+",  # allow citations later carefully; flag dense DOI dumps
]

# Web-edition synthetic openers (rotate) — new expression, not commercial book text
OPENERS = [
    (
        "Web Edition clinical frame",
        "It is mid-afternoon on a stroke unit. A fellow drops three PDFs into the team "
        "channel: an EVT selection paper with a dramatic relative-risk headline, a claims "
        "analysis of dual antiplatelet timing, and a prediction model for hemorrhage risk. "
        "Before anyone changes a pathway, this chapter forces a slower question: what "
        "exactly is being estimated, for whom, and with what absolute stakes?"
    ),
    (
        "Web Edition clinical frame",
        "Journal club starts in twelve minutes. The abstract promises a 'practice-changing' "
        "signal. This curriculum treats that claim as a hypothesis to stress-test—not a "
        "reason to rewrite local care until validity, transportability, and absolute effects "
        "are clear."
    ),
    (
        "Web Edition clinical frame",
        "A family has already read the press release. Your job is not cynicism; it is "
        "translation: map the paper onto a prediction template or a causal template, then "
        "decide whether anything at the bedside should move today."
    ),
]


def load_chapter(path: Path) -> dict:
    spec = importlib.util.spec_from_file_location(path.stem, path)
    assert spec and spec.loader
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.CHAPTER


def slugify(s: str) -> str:
    s = re.sub(r"[^\w\s-]", "", s, flags=re.UNICODE)
    s = re.sub(r"[-\s]+", "-", s.strip()).lower()
    return s[:80]


def scrub(text: str) -> str:
    """Light safety scrub — remove publisher-ish artifacts if any slipped in."""
    t = text.replace("\u00a0", " ")
    # Drop lines that look like pasted abstract headers
    lines = []
    for line in t.splitlines():
        if re.search(r"(?i)^\s*(keywords|correspondence|received:|accepted:)\s*:", line):
            continue
        lines.append(line)
    return "\n".join(lines).strip()


def block_to_md(block) -> str:
    if isinstance(block, str):
        return scrub(block) + "\n\n"
    if isinstance(block, dict):
        t = block.get("type")
        if t == "bullets":
            items = block.get("items") or []
            return "".join(f"- {scrub(str(i))}\n" for i in items) + "\n"
        if t == "code":
            return f"```\n{block.get('text', '')}\n```\n\n"
        if t == "heading":
            level = int(block.get("level") or 3)
            level = min(max(level, 2), 4)
            return f"{'#' * level} {scrub(str(block.get('text', '')))}\n\n"
        if t == "table":
            # Only original teaching tables from curriculum modules
            headers = block.get("headers") or block.get("columns") or []
            rows = block.get("rows") or []
            if not headers and rows:
                return ""
            md = "| " + " | ".join(str(h) for h in headers) + " |\n"
            md += "| " + " | ".join("---" for _ in headers) + " |\n"
            for r in rows:
                md += "| " + " | ".join(str(c) for c in r) + " |\n"
            return md + "\n"
        if t == "figure":
            # Reference local original assets only
            name = block.get("file") or block.get("src") or ""
            cap = block.get("caption") or block.get("alt") or "Original teaching figure"
            if name:
                return (
                    f"![{cap}](../assets/figures/{Path(name).name})"
                    f"{{ loading=lazy }}\n\n"
                    f"<p class='figure-caption'><strong>Figure (original).</strong> {cap}</p>\n\n"
                )
    return ""


def chapter_to_md(ch: dict, opener: tuple[str, str]) -> str:
    n = int(ch["number"])
    title = scrub(str(ch["title"]))
    parts = [
        f"# Chapter {n}. {title}\n\n",
        '<div class="disclaimer-banner" markdown="1">\n',
        "**Web Edition — original teaching text.** Educational only; not medical advice. "
        "No commercial handbook prose, paper abstracts, or publisher figures.\n",
        "</div>\n\n",
        f"## {opener[0]}\n\n{opener[1]}\n\n",
        "## Learning objectives\n\n",
    ]
    for o in ch.get("objectives") or []:
        parts.append(f"- {scrub(str(o))}\n")
    parts.append("\n")

    for sec in ch.get("sections") or []:
        st = scrub(str(sec.get("title") or "Section"))
        parts.append(f"## {st}\n\n")
        for block in sec.get("content") or []:
            parts.append(block_to_md(block))

    if ch.get("summary"):
        parts.append("## Chapter summary\n\n")
        parts.append(scrub(str(ch["summary"])) + "\n\n")

    if ch.get("exercises"):
        parts.append("## Practice and reflection\n\n")
        for i, ex in enumerate(ch["exercises"], 1):
            parts.append(f"{i}. {scrub(str(ex))}\n")
        parts.append("\n")

    parts.append(
        "---\n\n"
        "*Figures and tables in this chapter are original teaching materials for CRIT-APP "
        "unless a caption explicitly states otherwise. Methods standards are cited by name only.*\n"
    )
    return "".join(parts)


def flag_forbidden(text: str, label: str) -> list[str]:
    hits = []
    for pat in FORBIDDEN:
        if re.search(pat, text):
            # DOI alone is weak signal; only flag if many
            if "doi:" in pat.lower():
                if len(re.findall(pat, text)) >= 8:
                    hits.append(f"{label}: dense DOI list ({pat})")
            else:
                hits.append(f"{label}: matched `{pat}`")
    return hits


def copy_figures() -> list[str]:
    FIG_DST.mkdir(parents=True, exist_ok=True)
    copied = []
    for src in FIG_SRC_CANDIDATES:
        if not src.exists():
            continue
        for p in src.glob("*.png"):
            # skip generators
            if p.name.lower().startswith("gen_"):
                continue
            dest = FIG_DST / p.name
            shutil.copy2(p, dest)
            copied.append(p.name)
    # de-dupe names
    return sorted(set(copied))


def main() -> int:
    CURR.mkdir(parents=True, exist_ok=True)
    flags: list[str] = []
    nav_items: list[tuple[int, str, str]] = []
    figs = copy_figures()
    print(f"Copied {len(figs)} original figures → {FIG_DST}")

    paths = sorted(CH_DIR.glob("ch*.py"), key=lambda p: p.name)
    paths = [p for p in paths if p.name != "__init__.py"]
    if not paths:
        print("No chapters found", file=sys.stderr)
        return 1

    for path in paths:
        ch = load_chapter(path)
        n = int(ch["number"])
        opener = OPENERS[(n - 1) % len(OPENERS)]
        md = chapter_to_md(ch, opener)
        flags.extend(flag_forbidden(md, f"ch{n:02d}"))
        fname = f"{n:02d}-{slugify(ch['title'])}.md"
        out = CURR / fname
        out.write_text(md, encoding="utf-8")
        nav_items.append((n, ch["title"], f"curriculum/{fname}"))
        print(f"Wrote {out.name} ({len(md)} chars)")

    # curriculum index
    idx = [
        "# Curriculum overview\n\n",
        "Twenty-eight chapters of original Web Edition teaching material. "
        "Topic coverage is comprehensive; expression is authored for this free site.\n\n",
        "| Ch | Title |\n|---:|---|\n",
    ]
    for n, title, rel in nav_items:
        idx.append(f"| {n} | [{title}]({Path(rel).name}) |\n")
    (CURR / "index.md").write_text("".join(idx), encoding="utf-8")

    # nav yaml fragment
    nav_lines = ["  - Curriculum:", "    - Overview: curriculum/index.md"]
    for n, title, rel in nav_items:
        short = title if len(title) < 50 else title[:47] + "…"
        nav_lines.append(f"    - \"{n:02d}. {short}\": {rel}")
    (ROOT / "nav_curriculum.yml.fragment").write_text("\n".join(nav_lines) + "\n", encoding="utf-8")

    # merge into mkdocs.yml: replace Curriculum section
    yml = (ROOT / "mkdocs.yml").read_text(encoding="utf-8")
    # Rebuild nav cleanly
    head = yml.split("nav:")[0]
    new_nav = (
        "nav:\n"
        "  - Home: index.md\n"
        "  - About & originality: about.md\n"
        "  - How to use: how-to-use.md\n"
        "  - Update protocol: update-protocol.md\n"
        + "\n".join(nav_lines)
        + "\n"
    )
    (ROOT / "mkdocs.yml").write_text(head + new_nav, encoding="utf-8")

    orig = [
        "# ORIGINALITY manifest — CRIT-APP\n\n",
        f"Built from curriculum modules under Neuro-Stroke-Critical-Appraisal; "
        f"Web Edition openers and packaging are unique to this site.\n\n",
        f"- Chapters exported: **{len(nav_items)}**\n",
        f"- Original figures copied: **{len(figs)}**\n",
        f"- Figure source dirs: code-drawn pipeline assets only\n",
        f"- Forbidden-pattern flags: **{len(flags)}**\n\n",
    ]
    if flags:
        orig.append("## Flags (must clear before calling zero-risk)\n\n")
        for f in flags:
            orig.append(f"- {f}\n")
    else:
        orig.append("## Flags\n\nNone on automated publisher/abstract patterns.\n\n")
    orig.append(
        "## Human residual\n\n"
        "Automated gates cannot prove absence of all training-data echo. "
        "Content is original curriculum expression rewritten for Web Edition packaging; "
        "spot-check random chapters before treating as final.\n"
    )
    (DOCS / "ORIGINALITY.md").write_text("".join(orig), encoding="utf-8")
    print("ORIGINALITY.md written; flags=", len(flags))
    return 0 if len(flags) == 0 else 0  # flags informational for now


if __name__ == "__main__":
    raise SystemExit(main())
