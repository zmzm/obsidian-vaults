#!/usr/bin/env python3
"""Report repeated TWIR themes that may deserve wiki promotion."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
RAW_TWIR = FRONTEND / "raw" / "twir"
WIKI_SOURCES = FRONTEND / "wiki" / "sources"

WIKILINK_RE = re.compile(r"\[\[(?P<target>[^\]|#]+)(?:#[^\]|]+)?(?:\|[^\]]+)?\]\]")

STOP_TAGS = {
    "ai",
    "css",
    "docs",
    "expo",
    "forms",
    "node",
    "nodejs",
    "npm",
    "pnpm",
    "pr",
    "rsc",
    "rscs",
    "ts",
    "typescript",
}

ALIASES = {
    "compiler": "React Compiler",
    "reactcompiler": "React Compiler",
    "react-compiler": "React Compiler",
    "reactrouter": "React Router",
    "react-router": "React Router",
    "tanstack": "TanStack",
    "tanstackquery": "TanStack Query",
    "tanstack-query": "TanStack Query",
    "tanstackrouter": "TanStack Router",
    "tanstack-router": "TanStack Router",
    "tanstackstart": "TanStack Start",
    "tanstack-start": "TanStack Start",
    "nextjs": "Next.js",
    "next-js": "Next.js",
    "servercomponents": "Server Components",
    "server-components": "Server Components",
    "serverfunctions": "Server Functions",
    "server-functions": "Server Functions",
    "react19": "React 19",
    "react-19": "React 19",
    "storybook": "Storybook",
    "stylex": "StyleX",
    "security": "Security",
    "suspense": "Suspense",
    "performance": "Performance",
    "testing": "Testing",
    "accessibility": "Accessibility",
    "routing": "Routing",
}


@dataclass
class ThemeHit:
    issues: set[int] = field(default_factory=set)
    origins: set[str] = field(default_factory=set)


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def raw_issue_path(issue_dir: Path) -> Path | None:
    matches = sorted(issue_dir.glob("*TWIR-*.md"))
    return matches[0] if matches else None


def raw_issue_paths() -> dict[int, Path]:
    issues: dict[int, Path] = {}
    for child in RAW_TWIR.iterdir():
        if not child.is_dir() or not child.name.isdigit():
            continue
        issue_file = raw_issue_path(child)
        if issue_file:
            issues[int(child.name)] = issue_file
    return dict(sorted(issues.items()))


def extract_frontmatter(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def extract_list_field(frontmatter: str, key: str) -> list[str]:
    # YAML subset parser for the simple frontmatter used in this vault.
    block = re.search(rf"^{re.escape(key)}:\n(?P<body>(?:  - .+\n)+)", frontmatter, re.MULTILINE)
    if block:
        return [
            line.removeprefix("  - ").strip().strip('"')
            for line in block.group("body").splitlines()
            if line.strip()
        ]
    inline = re.search(rf"^{re.escape(key)}:\s*\[(?P<body>[^\]]*)\]", frontmatter, re.MULTILINE)
    if inline:
        return [part.strip().strip('"') for part in inline.group("body").split(",") if part.strip()]
    return []


def canonical_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def normalize_theme(value: str, *, preserve_label: bool = False) -> str | None:
    value = value.strip().strip('"')
    if not value:
        return None

    alias_key = re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")
    compact_key = canonical_key(value)
    if alias_key in ALIASES:
        return ALIASES[alias_key]
    if compact_key in ALIASES:
        return ALIASES[compact_key]
    if alias_key in STOP_TAGS or compact_key in STOP_TAGS:
        return None
    if len(value) <= 2:
        return None
    if preserve_label:
        return value.replace("_", " ").strip()
    return value.replace("_", " ").replace("-", " ").strip().title()


def wiki_digest_links(issue: int) -> set[str]:
    path = WIKI_SOURCES / f"TWIR {issue}.md"
    if not path.exists():
        return set()
    text = read_text(path)
    links: set[str] = set()
    for match in WIKILINK_RE.finditer(text):
        target = match.group("target").strip()
        if target.startswith("../"):
            target = target.split("/")[-1]
        if target.startswith("../../raw/"):
            continue
        if target.startswith("TWIR "):
            continue
        links.add(target)
    return links


def scan() -> dict[str, ThemeHit]:
    hits: dict[str, ThemeHit] = defaultdict(ThemeHit)
    for issue, path in raw_issue_paths().items():
        text = read_text(path)
        frontmatter = extract_frontmatter(text)
        raw_values = [
            *extract_list_field(frontmatter, "topics"),
            *extract_list_field(frontmatter, "tags"),
        ]
        for raw_value in raw_values:
            theme = normalize_theme(raw_value)
            if theme:
                hits[theme].issues.add(issue)
                hits[theme].origins.add("raw")
        for link in wiki_digest_links(issue):
            theme = normalize_theme(link, preserve_label=True)
            if theme:
                hits[theme].issues.add(issue)
                hits[theme].origins.add("wiki")
    return dict(hits)


def existing_wiki_pages() -> dict[str, str]:
    pages: dict[str, str] = {}
    for path in (FRONTEND / "wiki").rglob("*.md"):
        pages[canonical_key(path.stem)] = path.stem
    return pages


def format_issues(issues: set[int], limit: int) -> str:
    ordered = sorted(issues)
    shown = ordered[:limit]
    suffix = f" (+{len(ordered) - limit} more)" if len(ordered) > limit else ""
    return ", ".join(str(issue) for issue in shown) + suffix


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-issues", type=int, default=3, help="minimum distinct issues for a theme")
    parser.add_argument("--limit", type=int, default=40, help="maximum themes to print")
    parser.add_argument("--issue-limit", type=int, default=16, help="maximum issue numbers shown per theme")
    parser.add_argument(
        "--only-unpaged",
        action="store_true",
        help="show only themes without an exact matching wiki page title",
    )
    args = parser.parse_args()

    hits = scan()
    pages = existing_wiki_pages()
    candidates = [
        (theme, hit)
        for theme, hit in hits.items()
        if len(hit.issues) >= args.min_issues
        and (not args.only_unpaged or canonical_key(theme) not in pages)
    ]
    candidates.sort(key=lambda item: (-len(item[1].issues), item[0].lower()))

    print("TWIR promotion candidates")
    print("=========================")
    print(f"minimum issues: {args.min_issues}")
    print(f"themes shown:   {min(len(candidates), args.limit)} of {len(candidates)}")
    print()

    for theme, hit in candidates[: args.limit]:
        page_state = "existing page" if canonical_key(theme) in pages else "no exact page"
        origins = "/".join(sorted(hit.origins))
        print(f"- {theme} ({len(hit.issues)} issues, {origins}, {page_state})")
        print(f"  issues: {format_issues(hit.issues, args.issue_limit)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
