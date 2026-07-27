#!/usr/bin/env python3
"""Report TWIR raw/wiki ingest coverage for the frontend vault."""

from __future__ import annotations

import argparse

from vault_utils import INDEX, dump_json, raw_issues, read_text, rel, wiki_digest_paths


def format_issue_list(issues: list[int], raw: dict | None = None) -> str:
    if not issues:
        return "  none"
    lines: list[str] = []
    for issue in issues:
        if raw and issue in raw:
            lines.append(f"  {issue}: {raw[issue].date}  {rel(raw[issue].path)}")
        else:
            lines.append(f"  {issue}")
    return "\n".join(lines)


def issue_in_selected_range(issue: int, since: int | None, until: int | None) -> bool:
    if since is not None and issue < since:
        return False
    if until is not None and issue > until:
        return False
    return True


def status(args) -> dict[str, object]:
    raw = raw_issues()
    digests = wiki_digest_paths()
    index = read_text(INDEX) if INDEX.exists() else ""
    raw_set = set(raw)
    digest_set = set(digests)
    missing_digests = sorted(raw_set - digest_set)
    orphan_digests = sorted(digest_set - raw_set)
    selected_raw = [issue for issue in sorted(raw_set) if issue_in_selected_range(issue, args.since, args.until)]
    missing_index_raw = (
        [issue for issue in selected_raw if f"raw/twir/{issue}/" not in index]
        if args.check_raw_index
        else []
    )
    missing_index_digest = [
        issue
        for issue in sorted(digest_set)
        if issue_in_selected_range(issue, args.since, args.until)
        and f"wiki/sources/TWIR {issue}|TWIR {issue}" not in index
    ]
    return {
        "raw_count": len(raw_set),
        "digest_count": len(digest_set),
        "missing_digests": missing_digests,
        "orphan_digests": orphan_digests,
        "missing_index_raw": missing_index_raw,
        "missing_index_digest": missing_index_digest,
        "raw": raw,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-raw-index", action="store_true", help="also require raw issues to be linked directly")
    parser.add_argument("--since", type=int, help="only check index coverage for issues >= this number")
    parser.add_argument("--until", type=int, help="only check index coverage for issues <= this number")
    parser.add_argument("--json", action="store_true", help="print machine-readable status")
    args = parser.parse_args()

    result = status(args)
    raw = result.pop("raw")

    if args.json:
        dump_json(result)
        return 1 if any(result[key] for key in ["missing_digests", "orphan_digests", "missing_index_raw", "missing_index_digest"]) else 0

    print("TWIR ingest status")
    print("==================")
    print(f"raw issues:        {result['raw_count']}")
    print(f"wiki digests:      {result['digest_count']}")
    print(f"missing digests:   {len(result['missing_digests'])}")
    print(f"orphan digests:    {len(result['orphan_digests'])}")
    print()

    print("Missing wiki digest pages")
    print(format_issue_list(result["missing_digests"], raw))
    print()

    print("Wiki digests without raw issue")
    print(format_issue_list(result["orphan_digests"]))
    print()

    if args.check_raw_index:
        print("Raw issues missing from frontend/index.md")
        print(format_issue_list(result["missing_index_raw"], raw))
        print()

    print("Digest pages missing from frontend/index.md")
    print(format_issue_list(result["missing_index_digest"]))

    return 1 if any(result[key] for key in ["missing_digests", "orphan_digests", "missing_index_raw", "missing_index_digest"]) else 0


if __name__ == "__main__":
    raise SystemExit(main())
