#!/usr/bin/env python3
"""Report article-text availability separately from wiki maturity and editorial review."""

from __future__ import annotations

import argparse
from collections import Counter
import json

from recover_twir_sources import candidates
from vault_utils import FRONTEND, WIKI, dump_json, parse_frontmatter, read_text, rel


def status(since: int, until: int) -> dict:
    registry = FRONTEND / "system" / "source-review.json"
    reviews = json.loads(read_text(registry)).get("reviews", {}) if registry.exists() else {}
    missing = candidates(list(range(since, until + 1)), set())
    for row in missing:
        review = reviews.get(row["snapshot"], {})
        row["review"] = review.get("status", "pending") if row["recovered"] else "unavailable"
        if review.get("note"):
            row["review_note"] = review["note"]
    pages = []
    for path in sorted(WIKI.rglob("*.md")):
        fm = parse_frontmatter(read_text(path))
        pages.append({"path": rel(path), "status": fm.get("status"),
                      "evidence": fm.get("evidence", "unassessed")})
    return {
        "scope": {"since": since, "until": until},
        "missing_original_bodies": len(missing),
        "available_recovery_snapshots": sum(row["recovered"] for row in missing),
        "recovery_reviews": dict(Counter(row["review"] for row in missing)),
        "wiki_evidence": dict(Counter(row["evidence"] for row in pages)),
        "articles": missing, "pages": pages,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", type=int, default=292)
    parser.add_argument("--until", type=int, default=302)
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if args.since > args.until:
        parser.error("--since must not exceed --until")
    data = status(args.since, args.until)
    if args.json:
        dump_json(data)
    else:
        print(f"Article evidence: TWIR {args.since}–{args.until}")
        print(f"Missing original bodies: {data['missing_original_bodies']}")
        print(f"Recovery snapshots:     {data['available_recovery_snapshots']}")
        print(f"Snapshot review:        {data['recovery_reviews']}")
        print(f"Wiki evidence:          {data['wiki_evidence']}")
        for row in data["articles"]:
            if row["review"] in {"unavailable", "insufficient"}:
                print(f"  {row['issue']}:{row['item']} {row['review']}: {row['title']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
