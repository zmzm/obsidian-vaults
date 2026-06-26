#!/usr/bin/env python3
"""Mechanical lint checks for the frontend LLM wiki."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
WIKI = FRONTEND / "wiki"
INDEX = FRONTEND / "index.md"
LOG = FRONTEND / "log.md"

ALLOWED_TYPES = {
    "concept",
    "tool",
    "pattern",
    "topic",
    "case-study",
    "source",
    "synthesis",
}
ALLOWED_STATUSES = {"seed", "active", "review"}
LINK_RE = re.compile(r"\[\[(?P<target>[^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")


@dataclass(frozen=True)
class Link:
    source: Path
    raw_target: str
    resolved: Path | None
    is_raw: bool


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def wiki_pages() -> list[Path]:
    return sorted(WIKI.rglob("*.md"))


def link_sources() -> list[Path]:
    return [INDEX, LOG, *wiki_pages()]


def extract_frontmatter(text: str) -> dict[str, str] | None:
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    body = text[4:end]
    values: dict[str, str] = {}
    for line in body.splitlines():
        if ":" not in line or line.startswith("  "):
            continue
        key, value = line.split(":", 1)
        values[key.strip()] = value.strip().strip('"')
    return values


def page_by_stem() -> dict[str, list[Path]]:
    pages: dict[str, list[Path]] = defaultdict(list)
    for path in [FRONTEND / "AGENTS.md", INDEX, LOG, *wiki_pages()]:
        if not path.exists():
            continue
        pages[path.stem].append(path)
    return dict(pages)


def resolve_path_like(source: Path, target: str) -> Path | None:
    candidate = (source.parent / target).resolve()
    candidates = [candidate]
    if candidate.suffix != ".md":
        candidates.append(Path(f"{candidate}.md"))
    for path in candidates:
        try:
            path.relative_to(ROOT)
        except ValueError:
            continue
        if path.exists():
            return path
    return None


def resolve_link(source: Path, target: str, stems: dict[str, list[Path]]) -> tuple[Path | None, bool]:
    target = target.strip()
    is_raw = target.startswith("raw/") or target.startswith("../raw/") or target.startswith("../../raw/")

    if "/" in target:
        resolved = resolve_path_like(source, target)
        return resolved, is_raw

    matches = stems.get(target, stems.get(Path(target).stem, []))
    if len(matches) == 1:
        return matches[0], False
    return None, False


def collect_links() -> list[Link]:
    stems = page_by_stem()
    links: list[Link] = []
    for source in link_sources():
        if not source.exists():
            continue
        for match in LINK_RE.finditer(read_text(source)):
            raw_target = match.group("target").strip()
            resolved, is_raw = resolve_link(source, raw_target, stems)
            links.append(Link(source=source, raw_target=raw_target, resolved=resolved, is_raw=is_raw))
    return links


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def check_frontmatter() -> list[str]:
    errors: list[str] = []
    for path in wiki_pages():
        frontmatter = extract_frontmatter(read_text(path))
        if frontmatter is None:
            errors.append(f"{rel(path)}: missing YAML frontmatter")
            continue
        page_type = frontmatter.get("type")
        status = frontmatter.get("status")
        updated = frontmatter.get("updated")
        if page_type not in ALLOWED_TYPES:
            errors.append(f"{rel(path)}: invalid or missing type: {page_type!r}")
        if status not in ALLOWED_STATUSES:
            errors.append(f"{rel(path)}: invalid or missing status: {status!r}")
        if not updated:
            errors.append(f"{rel(path)}: missing updated")
    return errors


def check_links(links: list[Link]) -> list[str]:
    errors: list[str] = []
    for link in links:
        if link.resolved is None:
            errors.append(f"{rel(link.source)}: unresolved link [[{link.raw_target}]]")
    return errors


def inbound_counts(links: list[Link]) -> dict[Path, int]:
    counts = {path: 0 for path in wiki_pages()}
    for link in links:
        if link.resolved in counts and link.resolved != link.source:
            counts[link.resolved] += 1
    return counts


def orphan_warnings(links: list[Link], min_backlinks: int) -> list[str]:
    warnings: list[str] = []
    counts = inbound_counts(links)
    for path, count in sorted(counts.items(), key=lambda item: (item[1], rel(item[0]))):
        if count < min_backlinks:
            warnings.append(f"{rel(path)}: {count} inbound wiki/index links")
    return warnings


def duplicate_stems() -> list[str]:
    warnings: list[str] = []
    for stem, paths in sorted(page_by_stem().items()):
        if len(paths) > 1:
            joined = ", ".join(rel(path) for path in paths)
            warnings.append(f"{stem}: duplicate page stem across {joined}")
    return warnings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--min-backlinks",
        type=int,
        default=1,
        help="warn when a wiki page has fewer inbound wiki/index links",
    )
    parser.add_argument("--no-orphans", action="store_true", help="skip orphan/backlink warnings")
    args = parser.parse_args()

    links = collect_links()
    errors = [*check_frontmatter(), *check_links(links)]
    warnings = duplicate_stems()
    if not args.no_orphans:
        warnings.extend(orphan_warnings(links, args.min_backlinks))

    print("Frontend wiki lint")
    print("==================")
    print(f"wiki pages: {len(wiki_pages())}")
    print(f"links:      {len(links)}")
    print(f"errors:     {len(errors)}")
    print(f"warnings:   {len(warnings)}")
    print()

    if errors:
        print("Errors")
        for item in errors:
            print(f"- {item}")
        print()

    if warnings:
        print("Warnings")
        for item in warnings:
            print(f"- {item}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
