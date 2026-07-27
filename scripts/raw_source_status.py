#!/usr/bin/env python3
"""Report standalone raw frontend sources that are not referenced by the wiki."""

from __future__ import annotations

import argparse
from pathlib import Path

from vault_utils import FRONTEND, RAW_ARTICLES, WIKI, dump_json, read_text, rel


def markdown_files(path: Path) -> list[Path]:
    return sorted(path.rglob("*.md")) if path.exists() else []


def referenced_raw_targets() -> set[str]:
    text = "\n".join(read_text(path) for path in [FRONTEND / "index.md", *sorted(WIKI.rglob("*.md"))] if path.exists())
    return {path.stem for path in markdown_files(RAW_ARTICLES) if path.stem in text}


def status() -> dict[str, object]:
    articles = markdown_files(RAW_ARTICLES)
    referenced = referenced_raw_targets()
    unprocessed = [path for path in articles if path.stem not in referenced]
    return {
        "standalone_raw_articles": len(articles),
        "referenced": len(articles) - len(unprocessed),
        "unprocessed": [rel(path) for path in unprocessed],
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--json", action="store_true", help="print machine-readable status")
    args = parser.parse_args()
    result = status()
    if args.json:
        dump_json(result)
    else:
        print("Standalone raw source status")
        print("============================")
        print(f"standalone raw articles: {result['standalone_raw_articles']}")
        print(f"referenced:              {result['referenced']}")
        print(f"unprocessed:             {len(result['unprocessed'])}")
        print()
        if result["unprocessed"]:
            for item in result["unprocessed"]:
                print(f"- {item}")
        else:
            print("none")
    return 1 if result["unprocessed"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
