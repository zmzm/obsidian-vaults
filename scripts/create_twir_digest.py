#!/usr/bin/env python3
"""Create a draft wiki source digest from a raw TWIR issue."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
RAW_TWIR = FRONTEND / "raw" / "twir"
WIKI_SOURCES = FRONTEND / "wiki" / "sources"


SECTION_RE = re.compile(r"^## (?P<title>.+)$", re.MULTILINE)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def raw_issue_path(issue: int) -> Path:
    issue_dir = RAW_TWIR / str(issue)
    if not issue_dir.exists():
        raise SystemExit(f"raw issue directory not found: {issue_dir.relative_to(ROOT)}")
    matches = sorted(issue_dir.glob("*TWIR-*.md"))
    if not matches:
        raise SystemExit(f"raw issue markdown not found in {issue_dir.relative_to(ROOT)}")
    return matches[0]


def extract_frontmatter_value(text: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.+)$", text, re.MULTILINE)
    return match.group(1).strip().strip('"') if match else None


def extract_frontmatter_tags(text: str) -> list[str]:
    match = re.search(r"^tags:\n(?P<body>(?:  - .+\n)+)", text, re.MULTILINE)
    if not match:
        return []
    tags: list[str] = []
    for line in match.group("body").splitlines():
        item = line.removeprefix("  - ").strip().strip('"')
        if item:
            tags.append(item)
    return tags


def section(text: str, title: str) -> str:
    matches = list(SECTION_RE.finditer(text))
    for index, match in enumerate(matches):
        if match.group("title").strip() != title:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        return text[start:end].strip()
    return ""


def bullets_from_section(section_text: str) -> list[str]:
    return [line.strip() for line in section_text.splitlines() if line.strip().startswith("- ")]


def article_titles(section_text: str) -> list[str]:
    titles: list[str] = []
    for line in section_text.splitlines():
        match = re.search(r"\|(?P<title>[^\]]+)\]\]", line)
        if match:
            titles.append(match.group("title").strip())
    return titles


def slug_tag(tag: str) -> str:
    tag = tag.lower().replace(".", "")
    tag = re.sub(r"[^a-z0-9]+", "-", tag).strip("-")
    return tag


def selected_tags(raw_tags: list[str]) -> list[str]:
    normalized = []
    for tag in raw_tags[:6]:
        slug = slug_tag(tag)
        if slug and slug not in normalized:
            normalized.append(slug)
    return ["twir", "digest", *normalized[:4]]


def date_from_filename(path: Path) -> str:
    match = re.match(r"(?P<date>\d{4}-\d{2}-\d{2})-TWIR-\d+\.md$", path.name)
    return match.group("date") if match else "unknown-date"


def draft_digest(issue: int, raw_path: Path) -> str:
    text = read_text(raw_path)
    date = extract_frontmatter_value(text, "date") or date_from_filename(raw_path)
    raw_tags = extract_frontmatter_tags(text)
    tags = selected_tags(raw_tags)
    tldr = bullets_from_section(section(text, "TL;DR"))
    articles = article_titles(section(text, "Articles"))
    action_items = bullets_from_section(section(text, "Action Items"))

    tag_block = "\n".join(f"  - {tag}" for tag in tags)
    summary_lines = tldr[:5] or ["- Draft summary pending."]
    action_summary = action_items[:4]
    article_summary = articles[:8]

    summary = "\n".join(summary_lines)
    article_notes = "\n".join(f"- {title}" for title in article_summary) or "- Draft article review pending."
    action_notes = "\n".join(action_summary) or "- No explicit action items in the raw issue."
    raw_target = raw_path.with_suffix("").name
    raw_link = f"[[../../raw/twir/{issue}/{raw_target}|{date}-TWIR-{issue}]]"

    return f"""---
type: source
status: review
updated: {date}
tags:
{tag_block}
---

# TWIR {issue}

TWIR #{issue} is a draft digest generated from the raw issue. Review and tighten this page before treating it as fully ingested.

## Summary

{summary}

## Notable Articles

{article_notes}

## Action Items From Raw

{action_notes}

## Why This Source Matters

- Draft editorial judgment pending. Identify whether this issue strengthens an existing concept, tool, pattern, case study, or synthesis branch.

## Caveats

- This page was generated mechanically from the raw issue MOC and needs human/agent review.
- Do not promote individual articles until their summaries connect to durable wiki pages.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/Server Components|Server Components]]

## Raw Source

- {raw_link}
"""


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue", type=int, required=True, help="TWIR issue number, e.g. 213")
    parser.add_argument("--force", action="store_true", help="overwrite an existing wiki digest page")
    parser.add_argument("--print", action="store_true", dest="print_only", help="print the draft instead of writing it")
    args = parser.parse_args()

    raw_path = raw_issue_path(args.issue)
    output_path = WIKI_SOURCES / f"TWIR {args.issue}.md"
    draft = draft_digest(args.issue, raw_path)

    if args.print_only:
        print(draft)
        return 0

    if output_path.exists() and not args.force:
        raise SystemExit(f"refusing to overwrite existing page: {output_path.relative_to(ROOT)}")

    write_text(output_path, draft)
    print(f"wrote {output_path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
