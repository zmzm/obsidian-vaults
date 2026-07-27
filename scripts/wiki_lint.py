#!/usr/bin/env python3
"""Mechanical lint checks for the frontend LLM wiki."""

from __future__ import annotations

import argparse
import subprocess
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path

from vault_utils import (
    FRONTEND,
    INDEX,
    LOG,
    ROOT,
    WIKI,
    dump_json,
    parse_frontmatter,
    read_text,
    rel,
    section,
    title_from_target,
    wikilinks,
    write_text,
)


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
REQUIRED_SECTIONS = {
    "concept": ["Key Ideas", "Practical Significance", "Related Pages", "Sources", "Open Questions"],
    "tool": ["Key Ideas", "Practical Significance", "Related Pages", "Sources", "Open Questions"],
    "pattern": ["Key Ideas", "Practical Significance", "Related Pages", "Sources", "Open Questions"],
    "topic": ["Related Pages", "Sources", "Open Questions"],
    "case-study": ["Related Pages"],
    "source": ["Summary", "Why This Source Matters", "Related Pages"],
    "synthesis": ["Short Thesis", "Related Pages", "Sources", "Open Questions"],
}

SECTION_VARIANTS = {
    "case-study": [
        ["Context", "Summary"],
        ["Why It Matters", "Why This Case Matters"],
        ["Raw Source", "Raw Sources", "Sources"],
    ]
}


@dataclass(frozen=True)
class Link:
    source: Path
    raw_target: str
    resolved: Path | None
    is_raw: bool


def wiki_pages() -> list[Path]:
    return sorted(WIKI.rglob("*.md"))


def link_sources() -> list[Path]:
    return [INDEX, LOG, *wiki_pages()]


def page_by_stem() -> dict[str, list[Path]]:
    pages: dict[str, list[Path]] = defaultdict(list)
    for path in [FRONTEND / "AGENTS.md", INDEX, LOG, *wiki_pages()]:
        if path.exists():
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
        return resolve_path_like(source, target), is_raw
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
        for target, _label in wikilinks(read_text(source)):
            resolved, is_raw = resolve_link(source, target, stems)
            links.append(Link(source=source, raw_target=target, resolved=resolved, is_raw=is_raw))
    return links


def check_frontmatter() -> list[str]:
    errors: list[str] = []
    for path in wiki_pages():
        frontmatter = parse_frontmatter(read_text(path))
        if not frontmatter:
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


def check_required_sections() -> list[str]:
    errors: list[str] = []
    for path in wiki_pages():
        text = read_text(path)
        page_type = parse_frontmatter(text).get("type")
        for required in REQUIRED_SECTIONS.get(str(page_type), []):
            if not section(text, required):
                errors.append(f"{rel(path)}: missing required section: {required}")
        for alternatives in SECTION_VARIANTS.get(str(page_type), []):
            if not any(section(text, candidate) for candidate in alternatives):
                errors.append(f"{rel(path)}: missing one of required sections: {', '.join(alternatives)}")
    return errors


def check_links(links: list[Link]) -> list[str]:
    return [f"{rel(link.source)}: unresolved link [[{link.raw_target}]]" for link in links if link.resolved is None]


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


def index_coverage_warnings() -> list[str]:
    warnings: list[str] = []
    index = read_text(INDEX) if INDEX.exists() else ""
    for path in wiki_pages():
        page_type = parse_frontmatter(read_text(path)).get("type")
        if page_type == "synthesis" and path.stem not in index:
            warnings.append(f"{rel(path)}: synthesis missing from frontend/index.md")
    return warnings


def changed_markdown_files() -> set[Path]:
    result = subprocess.run(["git", "diff", "--name-only"], check=False, capture_output=True, text=True, cwd=ROOT)
    paths = set()
    for line in result.stdout.splitlines():
        path = ROOT / line
        if path.suffix == ".md" and path.exists():
            paths.add(path.resolve())
    return paths


def stale_updated_warnings() -> list[str]:
    warnings: list[str] = []
    for path in changed_markdown_files():
        try:
            path.relative_to(WIKI)
        except ValueError:
            continue
        frontmatter = parse_frontmatter(read_text(path))
        if not frontmatter.get("updated"):
            continue
        # This check is intentionally conservative: it warns only when changed wiki
        # files still carry dates older than the current repo-maintenance date.
        if str(frontmatter["updated"]) < "2026-07-27":
            warnings.append(f"{rel(path)}: changed file has stale updated date {frontmatter['updated']}")
    return warnings


def apply_safe_fixes() -> list[str]:
    fixed: list[str] = []
    # Normalize trailing whitespace in wiki/index/log markdown.
    for path in [INDEX, LOG, *wiki_pages()]:
        if not path.exists():
            continue
        text = read_text(path)
        normalized = "\n".join(line.rstrip() for line in text.splitlines()) + "\n"
        if normalized != text:
            write_text(path, normalized)
            fixed.append(f"{rel(path)}: stripped trailing whitespace")
    return fixed


def run_lint(args) -> tuple[list[str], list[str], list[str]]:
    fixed = apply_safe_fixes() if args.fix else []
    links = collect_links()
    errors = [*check_frontmatter(), *check_links(links)]
    if not args.no_required_sections:
        errors.extend(check_required_sections())
    warnings = duplicate_stems()
    warnings.extend(index_coverage_warnings())
    if not args.no_stale_updated:
        warnings.extend(stale_updated_warnings())
    if not args.no_orphans:
        warnings.extend(orphan_warnings(links, args.min_backlinks))
    return errors, warnings, fixed


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-backlinks", type=int, default=1, help="warn when a wiki page has fewer inbound wiki/index links")
    parser.add_argument("--no-orphans", action="store_true", help="skip orphan/backlink warnings")
    parser.add_argument("--no-required-sections", action="store_true", help="skip page-type section checks")
    parser.add_argument("--no-stale-updated", action="store_true", help="skip changed-file updated-date warnings")
    parser.add_argument("--fix", action="store_true", help="apply safe mechanical formatting fixes")
    parser.add_argument("--json", action="store_true", help="print machine-readable lint result")
    args = parser.parse_args()

    errors, warnings, fixed = run_lint(args)
    if args.json:
        dump_json({"errors": errors, "warnings": warnings, "fixed": fixed, "wiki_pages": len(wiki_pages()), "links": len(collect_links())})
        return 1 if errors else 0

    print("Frontend wiki lint")
    print("==================")
    print(f"wiki pages: {len(wiki_pages())}")
    print(f"links:      {len(collect_links())}")
    print(f"errors:     {len(errors)}")
    print(f"warnings:   {len(warnings)}")
    if fixed:
        print(f"fixed:      {len(fixed)}")
    print()

    if fixed:
        print("Fixed")
        for item in fixed:
            print(f"- {item}")
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
