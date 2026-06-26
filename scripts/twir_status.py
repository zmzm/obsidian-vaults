#!/usr/bin/env python3
"""Report TWIR raw/wiki ingest coverage for the frontend vault."""

from __future__ import annotations

import argparse
import re
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
RAW_TWIR = FRONTEND / "raw" / "twir"
WIKI_SOURCES = FRONTEND / "wiki" / "sources"
INDEX = FRONTEND / "index.md"

TWIR_SOURCE_RE = re.compile(r"^TWIR (?P<issue>\d+)\.md$")


@dataclass(frozen=True)
class RawIssue:
    issue: int
    path: Path
    date: str


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def raw_issue_file(issue_dir: Path) -> Path | None:
    matches = sorted(issue_dir.glob("*TWIR-*.md"))
    return matches[0] if matches else None


def extract_date(path: Path) -> str:
    match = re.match(r"(?P<date>\d{4}-\d{2}-\d{2})-TWIR-\d+\.md$", path.name)
    return match.group("date") if match else "unknown-date"


def raw_issues() -> dict[int, RawIssue]:
    issues: dict[int, RawIssue] = {}
    for child in RAW_TWIR.iterdir():
        if not child.is_dir() or not child.name.isdigit():
            continue
        issue = int(child.name)
        issue_file = raw_issue_file(child)
        if issue_file is None:
            continue
        issues[issue] = RawIssue(issue=issue, path=issue_file, date=extract_date(issue_file))
    return dict(sorted(issues.items()))


def wiki_digests() -> dict[int, Path]:
    digests: dict[int, Path] = {}
    for path in WIKI_SOURCES.glob("TWIR *.md"):
        match = TWIR_SOURCE_RE.match(path.name)
        if match:
            digests[int(match.group("issue"))] = path
    return dict(sorted(digests.items()))


def index_text() -> str:
    return read_text(INDEX) if INDEX.exists() else ""


def format_issue_list(issues: list[int], raw: dict[int, RawIssue] | None = None) -> str:
    if not issues:
        return "  none"
    lines: list[str] = []
    for issue in issues:
        if raw and issue in raw:
            lines.append(f"  {issue}: {raw[issue].date}  {raw[issue].path.relative_to(ROOT)}")
        else:
            lines.append(f"  {issue}")
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="workspace root; defaults to this script's parent")
    parser.add_argument(
        "--check-raw-index",
        action="store_true",
        help="also require every raw issue to be linked directly from frontend/index.md",
    )
    args = parser.parse_args()

    if args.root.resolve() != ROOT:
        raise SystemExit("--root is reserved for future use; run from this workspace for now")

    raw = raw_issues()
    digests = wiki_digests()
    index = index_text()

    raw_set = set(raw)
    digest_set = set(digests)
    missing_digests = sorted(raw_set - digest_set)
    orphan_digests = sorted(digest_set - raw_set)
    missing_index_raw = (
        [issue for issue in sorted(raw_set) if f"raw/twir/{issue}/" not in index]
        if args.check_raw_index
        else []
    )
    missing_index_digest = [
        issue for issue in sorted(digest_set) if f"wiki/sources/TWIR {issue}|TWIR {issue}" not in index
    ]

    print("TWIR ingest status")
    print("==================")
    print(f"raw issues:        {len(raw_set)}")
    print(f"wiki digests:      {len(digest_set)}")
    print(f"missing digests:   {len(missing_digests)}")
    print(f"orphan digests:    {len(orphan_digests)}")
    print()

    print("Missing wiki digest pages")
    print(format_issue_list(missing_digests, raw))
    print()

    print("Wiki digests without raw issue")
    print(format_issue_list(orphan_digests))
    print()

    if args.check_raw_index:
        print("Raw issues missing from frontend/index.md")
        print(format_issue_list(missing_index_raw, raw))
        print()

    print("Digest pages missing from frontend/index.md")
    print(format_issue_list(missing_index_digest))

    return 1 if missing_digests or orphan_digests or missing_index_raw or missing_index_digest else 0


if __name__ == "__main__":
    raise SystemExit(main())
