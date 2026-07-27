#!/usr/bin/env python3
"""Create a draft wiki source digest from a raw TWIR issue."""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from vault_utils import (
    ROOT,
    WIKI_SOURCES,
    article_paths,
    bullets_from_section,
    dump_json,
    parse_article_note,
    parse_frontmatter,
    raw_issue_path,
    read_text,
    rel,
    section,
    wikilinks,
    write_text,
)


def slug_tag(tag: str) -> str:
    tag = tag.lower().replace(".", "")
    tag = re.sub(r"[^a-z0-9]+", "-", tag).strip("-")
    return tag


def selected_tags(raw_tags: list[str]) -> list[str]:
    normalized = []
    for tag in raw_tags[:8]:
        slug = slug_tag(tag)
        if slug and slug not in normalized:
            normalized.append(slug)
    return ["twir", "digest", *normalized[:5]]


def article_score(note) -> int:
    score = 0
    if note.quality == "keep":
        score += 2
    if note.frontmatter.get("item_type") == "featured":
        score += 3
    if "Read fully" in note.recommendation:
        score += 3
    if note.summary and "Content not available" not in note.summary:
        score += 2
    score += min(len(note.related_notes), 3)
    score += min(len(note.key_takeaways), 3)
    return score


def article_link(issue: int, path: Path) -> str:
    return f"[[../../raw/twir/{issue}/articles/{path.stem}|{path.stem.split(' - ', 1)[-1]}]]"


def compact_summary(summary: str, max_chars: int = 260) -> str:
    summary = " ".join(summary.split())
    if len(summary) <= max_chars:
        return summary
    return summary[: max_chars - 1].rsplit(" ", 1)[0] + "."


def related_pages(raw_text: str, article_notes) -> list[str]:
    candidates: list[str] = []
    frontmatter = parse_frontmatter(raw_text)
    for value in frontmatter.get("topics", []):
        if isinstance(value, str):
            candidates.append(value)
    for target, _label in wikilinks(section(raw_text, "Main Topics")):
        candidates.append(target)
    for note in article_notes:
        candidates.extend(note.related_notes)

    seen: set[str] = set()
    related: list[str] = []
    for candidate in candidates:
        title = candidate.split("/")[-1].strip()
        if not title or title in seen or title.startswith("This Week in React"):
            continue
        seen.add(title)
        related.append(title)
    return related[:8]


def draft_digest(issue: int, status: str) -> tuple[str, dict]:
    raw_path = raw_issue_path(issue)
    raw_text = read_text(raw_path)
    frontmatter = parse_frontmatter(raw_text)
    date = str(frontmatter.get("date") or raw_path.name[:10])
    raw_tags = [str(tag) for tag in frontmatter.get("tags", [])]
    tags = selected_tags(raw_tags)
    tldr = bullets_from_section(section(raw_text, "TL;DR"))
    action_items = bullets_from_section(section(raw_text, "Action Items"))

    notes = [parse_article_note(path) for path in article_paths(issue)]
    ranked = sorted(notes, key=lambda note: (-article_score(note), note.item or 999, note.title))
    notable = ranked[:8]
    full_read = [note for note in ranked if "Read fully" in note.recommendation][:6]
    related = related_pages(raw_text, notable)

    tag_block = "\n".join(f"  - {tag}" for tag in tags)
    summary = "\n".join(tldr[:5]) or "- Draft summary pending."
    notable_lines = []
    for note in notable:
        detail = compact_summary(note.summary) if note.summary else "Article note needs review."
        notable_lines.append(f"- {article_link(issue, note.path)} — {detail}")
    action_lines = [f"- {article_link(issue, note.path)}" for note in full_read]
    if not action_lines:
        action_lines = action_items[:4] or ["- No explicit high-priority article review items found."]
    related_lines = [f"- [[../{page}|{page}]]" if "/" in page else f"- [[{page}]]" for page in related]
    if not related_lines:
        related_lines = ["- [[../topics/React Rendering|React Rendering]]"]

    caveat = (
        "- This page is an active reviewed digest, but individual article summaries may still rely on raw extraction quality."
        if status == "active"
        else "- This page was generated mechanically from the raw issue MOC and article notes; review before treating it as fully ingested."
    )
    raw_target = raw_path.with_suffix("").name
    raw_link = f"[[../../raw/twir/{issue}/{raw_target}|{date}-TWIR-{issue}]]"
    text = f"""---
type: source
status: {status}
updated: {date}
tags:
{tag_block}
---

# TWIR {issue}

TWIR #{issue} is a digest generated from the raw issue and article notes.

## Summary

{summary}

## Notable Articles

{chr(10).join(notable_lines) if notable_lines else "- Draft article review pending."}

## Action Items From Raw

{chr(10).join(action_lines)}

## Why This Source Matters

- Review the notable articles above to decide whether this issue strengthens an existing concept, tool, pattern, case study, or synthesis branch.
- Promote only repeated or durable signals; keep thin announcements at the issue-digest layer.

## Caveats

{caveat}
- Do not promote individual articles until their summaries connect to durable wiki pages.

## Related Pages

{chr(10).join(related_lines)}

## Raw Source

- {raw_link}
"""
    metadata = {
        "issue": issue,
        "date": date,
        "output": rel(WIKI_SOURCES / f"TWIR {issue}.md"),
        "notable_articles": [rel(note.path) for note in notable],
        "read_fully": [rel(note.path) for note in full_read],
        "related_pages": related,
    }
    return text, metadata


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--issue", type=int, required=True, help="TWIR issue number, e.g. 213")
    parser.add_argument("--force", action="store_true", help="overwrite an existing wiki digest page")
    parser.add_argument("--print", action="store_true", dest="print_only", help="print the draft instead of writing it")
    parser.add_argument("--json", action="store_true", help="print metadata as JSON")
    parser.add_argument(
        "--status",
        choices=["review", "active"],
        default="review",
        help="frontmatter status for the generated digest",
    )
    args = parser.parse_args()

    output_path = WIKI_SOURCES / f"TWIR {args.issue}.md"
    draft, metadata = draft_digest(args.issue, args.status)

    if args.json:
        dump_json(metadata)
        return 0

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
