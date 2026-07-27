#!/usr/bin/env python3
"""Report repeated TWIR themes that may deserve wiki promotion."""

from __future__ import annotations

import argparse
import re
from collections import defaultdict
from dataclasses import dataclass, field
from pathlib import Path

from vault_utils import (
    FRONTEND,
    WIKI,
    WIKI_SOURCES,
    canonical_key,
    dump_json,
    parse_frontmatter,
    raw_issues,
    read_text,
    title_from_target,
    wiki_digest_paths,
    wikilinks,
)


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

NOISE_THEMES = {
    "Apollo",
    "Aria",
    "Audio",
    "Babel",
    "Bottomsheet",
    "Bottomtabs",
    "Docusaurus",
    "Eas",
    "Edge To Edge",
    "Enriched",
    "Executorch",
    "Flashlist",
    "Flow",
    "Fumadocs",
    "Gesturehandler",
    "Hermes",
    "Keyboardcontroller",
    "Legendlist",
    "Lynx",
    "Maestro",
    "Metro",
    "Newarch",
    "Radon",
    "Reanimated",
    "Remotion",
    "Screens",
    "Skia",
    "Temporal",
    "Voltra",
    "Webgpu",
    "Windows",
    "Worklets",
}

ALIASES = {
    "activity": "React Activity",
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
    "next": "Next.js",
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
    "viewtransition": "React View Transitions",
    "view-transition": "React View Transitions",
    "baseui": "Base UI",
    "reactaria": "React Aria",
    "react-aria": "React Aria",
    "shadcn": "shadcn",
    "shadcnui": "shadcn",
    "nuqs": "nuqs",
}

COVERED_BY = {
    "Security": "Frontend Security Boundaries in Server-First React",
    "Nuqs": "Typed Routing and URL State",
    "nuqs": "Typed Routing and URL State",
    "Viewtransition": "React View Transitions",
    "View Transition": "React View Transitions",
    "Activity": "React Activity",
    "Eslint": "Custom ESLint Rules",
    "Oxlint": "React Compiler Toolchain Adoption",
    "Rolldown": "React Compiler Toolchain Adoption",
    "Rspack": "React Compiler Toolchain Adoption",
    "Bun": "React Compiler Toolchain Adoption",
    "StyleX": "Linear StyleX Migration",
    "Vitest": "Vitest Browser Mode",
    "Navigation": "Next.js 16.3",
    "React Aria": "Resilient React Components",
    "shadcn": "Resilient React Components",
    "Base UI": "Resilient React Components",
}

RELEVANCE_KEYWORDS = {
    "React",
    "Next.js",
    "TanStack",
    "Router",
    "Compiler",
    "Server",
    "Testing",
    "Security",
    "Caching",
    "SSR",
    "Hydration",
    "Accessibility",
    "Storybook",
    "Astro",
    "Vite",
    "Bun",
    "Rspack",
    "Rolldown",
    "StyleX",
    "Base UI",
    "shadcn",
    "nuqs",
}


@dataclass
class ThemeHit:
    issues: set[int] = field(default_factory=set)
    origins: set[str] = field(default_factory=set)


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
    links: set[str] = set()
    for target, _label in wikilinks(read_text(path)):
        target = target.strip()
        if target.startswith("../"):
            target = title_from_target(target)
        if target.startswith("../../raw/"):
            continue
        if target.startswith("TWIR "):
            continue
        links.add(target)
    return links


def scan() -> dict[str, ThemeHit]:
    hits: dict[str, ThemeHit] = defaultdict(ThemeHit)
    for issue, raw_issue in raw_issues().items():
        frontmatter = parse_frontmatter(read_text(raw_issue.path))
        raw_values = []
        for key in ["topics", "tags"]:
            value = frontmatter.get(key, [])
            if isinstance(value, list):
                raw_values.extend(str(item) for item in value)
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
    for path in WIKI.rglob("*.md"):
        pages[canonical_key(path.stem)] = path.stem
    return pages


def coverage_for(theme: str, pages: dict[str, str]) -> str | None:
    if canonical_key(theme) in pages:
        return pages[canonical_key(theme)]
    mapped = COVERED_BY.get(theme)
    if mapped and canonical_key(mapped) in pages:
        return pages[canonical_key(mapped)]
    return mapped


def relevance_score(theme: str, hit: ThemeHit, pages: dict[str, str]) -> int:
    score = len(hit.issues) * 2
    if "wiki" in hit.origins:
        score += 8
    if coverage_for(theme, pages):
        score -= 12
    if theme in NOISE_THEMES:
        score -= 20
    if any(keyword.lower() in theme.lower() for keyword in RELEVANCE_KEYWORDS):
        score += 8
    return score


def format_issues(issues: set[int], limit: int) -> str:
    ordered = sorted(issues)
    shown = ordered[:limit]
    suffix = f" (+{len(ordered) - limit} more)" if len(ordered) > limit else ""
    return ", ".join(str(issue) for issue in shown) + suffix


def candidate_rows(args) -> list[dict[str, object]]:
    hits = scan()
    pages = existing_wiki_pages()
    rows = []
    for theme, hit in hits.items():
        if len(hit.issues) < args.min_issues:
            continue
        covered_by = coverage_for(theme, pages)
        exact_page = pages.get(canonical_key(theme))
        if args.only_unpaged and exact_page:
            continue
        if args.hide_covered and covered_by:
            continue
        if args.hide_noise and theme in NOISE_THEMES:
            continue
        score = relevance_score(theme, hit, pages)
        if score < args.min_score:
            continue
        rows.append(
            {
                "theme": theme,
                "issues": sorted(hit.issues),
                "issue_count": len(hit.issues),
                "origins": sorted(hit.origins),
                "exact_page": exact_page,
                "covered_by": covered_by,
                "noise": theme in NOISE_THEMES,
                "score": score,
            }
        )
    rows.sort(key=lambda row: (-int(row["score"]), -int(row["issue_count"]), str(row["theme"]).lower()))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--min-issues", type=int, default=3, help="minimum distinct issues for a theme")
    parser.add_argument("--limit", type=int, default=40, help="maximum themes to print")
    parser.add_argument("--issue-limit", type=int, default=16, help="maximum issue numbers shown per theme")
    parser.add_argument("--only-unpaged", action="store_true", help="show only themes without an exact matching wiki page title")
    parser.add_argument("--hide-covered", action="store_true", help="hide themes covered by broader pages")
    parser.add_argument("--hide-noise", action="store_true", help="hide low-relevance recurring raw themes")
    parser.add_argument("--min-score", type=int, default=-999, help="minimum relevance score")
    parser.add_argument("--json", action="store_true", help="print candidates as JSON")
    args = parser.parse_args()

    rows = candidate_rows(args)
    if args.json:
        dump_json({"candidates": rows[: args.limit], "total": len(rows)})
        return 0

    print("TWIR promotion candidates")
    print("=========================")
    print(f"minimum issues: {args.min_issues}")
    print(f"themes shown:   {min(len(rows), args.limit)} of {len(rows)}")
    print()

    for row in rows[: args.limit]:
        exact = row["exact_page"]
        covered = row["covered_by"]
        if exact:
            page_state = f"existing page: {exact}"
        elif covered:
            page_state = f"covered by: {covered}"
        else:
            page_state = "no page"
        flags = []
        if row["noise"]:
            flags.append("noise")
        flag_text = f", {', '.join(flags)}" if flags else ""
        print(
            f"- {row['theme']} ({row['issue_count']} issues, {'/'.join(row['origins'])}, "
            f"score {row['score']}, {page_state}{flag_text})"
        )
        print(f"  issues: {format_issues(set(row['issues']), args.issue_limit)}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
