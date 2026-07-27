#!/usr/bin/env python3
"""Triage and optionally scaffold missing TWIR digest pages."""

from __future__ import annotations

import argparse
import subprocess
import sys

from create_twir_digest import draft_digest
from vault_utils import WIKI_SOURCES, article_paths, dump_json, parse_article_note, raw_issues, rel, wiki_digest_paths, write_text


def run_check(command: list[str]) -> int:
    print(f"$ {' '.join(command)}")
    result = subprocess.run(command, check=False)
    print()
    return result.returncode


def high_signal_articles(issue: int, limit: int) -> list[dict[str, str | int | None]]:
    notes = [parse_article_note(path) for path in article_paths(issue)]

    def score(note) -> int:
        value = 0
        if note.frontmatter.get("item_type") == "featured":
            value += 3
        if note.quality == "keep":
            value += 2
        if "Read fully" in note.recommendation:
            value += 3
        if note.related_notes:
            value += 2
        if note.summary and "Content not available" not in note.summary:
            value += 1
        return value

    ranked = sorted(notes, key=lambda note: (-score(note), note.item or 999, note.title))
    return [
        {
            "item": note.item,
            "title": note.title,
            "path": rel(note.path),
            "recommendation": note.recommendation,
            "related_notes": ", ".join(note.related_notes),
            "score": score(note),
        }
        for note in ranked[:limit]
    ]


def missing_issues() -> list[int]:
    raw = set(raw_issues())
    digests = set(wiki_digest_paths())
    return sorted(raw - digests)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--create-drafts", action="store_true", help="write missing digest drafts")
    parser.add_argument("--force", action="store_true", help="overwrite existing digest pages when creating drafts")
    parser.add_argument("--status", choices=["review", "active"], default="review", help="status for generated drafts")
    parser.add_argument("--article-limit", type=int, default=6, help="high-signal article notes shown per missing issue")
    parser.add_argument("--json", action="store_true", help="print triage as JSON and skip final command output")
    parser.add_argument("--skip-final-checks", action="store_true", help="skip status/lint/candidate commands")
    args = parser.parse_args()

    missing = missing_issues()
    triage = [
        {
            "issue": issue,
            "digest": rel(WIKI_SOURCES / f"TWIR {issue}.md"),
            "high_signal_articles": high_signal_articles(issue, args.article_limit),
        }
        for issue in missing
    ]

    if args.json:
        dump_json({"missing_issues": missing, "triage": triage})
        return 0 if not missing else 1

    print("Missing TWIR ingest triage")
    print("==========================")
    print(f"missing issues: {len(missing)}")
    print()
    if not missing:
        print("none")
    for item in triage:
        print(f"TWIR {item['issue']} -> {item['digest']}")
        for article in item["high_signal_articles"]:
            related = f" [{article['related_notes']}]" if article["related_notes"] else ""
            print(f"  - {article['title']} ({article['score']}){related}")
        print()

    if args.create_drafts:
        for issue in missing:
            output = WIKI_SOURCES / f"TWIR {issue}.md"
            if output.exists() and not args.force:
                print(f"skip existing {rel(output)}")
                continue
            draft, _metadata = draft_digest(issue, args.status)
            write_text(output, draft)
            print(f"wrote {rel(output)}")
        print()

    if not args.skip_final_checks:
        exit_code = 0
        for command in [
            [sys.executable, "scripts/twir_status.py"],
            [sys.executable, "scripts/wiki_lint.py"],
            [sys.executable, "scripts/twir_promotion_candidates.py", "--min-issues", "4", "--limit", "40"],
        ]:
            exit_code = max(exit_code, run_check(command))
        return exit_code

    return 0 if not missing else 1


if __name__ == "__main__":
    raise SystemExit(main())
