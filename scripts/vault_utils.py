#!/usr/bin/env python3
"""Shared helpers for frontend vault maintenance scripts."""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
FRONTEND = ROOT / "frontend"
RAW = FRONTEND / "raw"
RAW_TWIR = RAW / "twir"
RAW_ARTICLES = RAW / "articles"
WIKI = FRONTEND / "wiki"
WIKI_SOURCES = WIKI / "sources"
INDEX = FRONTEND / "index.md"
LOG = FRONTEND / "log.md"

SECTION_RE = re.compile(r"^## (?P<title>.+)$", re.MULTILINE)
WIKILINK_RE = re.compile(r"\[\[(?P<target>[^\]|#]+)(?:#[^\]|]+)?(?:\|(?P<label>[^\]]+))?\]\]")
DATE_TWIR_RE = re.compile(r"(?P<date>\d{4}-\d{2}-\d{2})-TWIR-(?P<issue>\d+)\.md$")


@dataclass(frozen=True)
class RawIssue:
    issue: int
    path: Path
    date: str


@dataclass(frozen=True)
class ArticleNote:
    path: Path
    frontmatter: dict[str, Any]
    title: str
    summary: str
    key_takeaways: list[str]
    recommendation: str
    related_notes: list[str]
    quality: str
    item: int | None


def rel(path: Path) -> str:
    return str(path.relative_to(ROOT))


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write_text(path: Path, text: str) -> None:
    path.write_text(text, encoding="utf-8")


def dump_json(data: Any) -> None:
    print(json.dumps(data, indent=2, ensure_ascii=False, sort_keys=True))


def extract_frontmatter_block(text: str) -> str:
    if not text.startswith("---\n"):
        return ""
    end = text.find("\n---", 4)
    return text[4:end] if end != -1 else ""


def parse_scalar(value: str) -> Any:
    value = value.strip()
    if not value:
        return ""
    if value.startswith("[") and value.endswith("]"):
        body = value[1:-1].strip()
        if not body:
            return []
        return [part.strip().strip('"').strip("'") for part in body.split(",") if part.strip()]
    if value.lower() in {"true", "false"}:
        return value.lower() == "true"
    if re.fullmatch(r"\d+", value):
        return int(value)
    return value.strip('"').strip("'")


def parse_frontmatter(text: str) -> dict[str, Any]:
    body = extract_frontmatter_block(text)
    if not body:
        return {}
    values: dict[str, Any] = {}
    lines = body.splitlines()
    index = 0
    while index < len(lines):
        line = lines[index]
        if ":" not in line or line.startswith("  "):
            index += 1
            continue
        key, value = line.split(":", 1)
        key = key.strip()
        value = value.strip()
        if value:
            values[key] = parse_scalar(value)
            index += 1
            continue
        items: list[str] = []
        index += 1
        while index < len(lines) and lines[index].startswith("  - "):
            items.append(lines[index].removeprefix("  - ").strip().strip('"').strip("'"))
            index += 1
        values[key] = items
    return values


def section(text: str, title: str) -> str:
    matches = list(SECTION_RE.finditer(text))
    for index, match in enumerate(matches):
        if match.group("title").strip() != title:
            continue
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        return text[start:end].strip()
    return ""


def bullets_from_section(section_text: str) -> list[str]:
    return [line.strip() for line in section_text.splitlines() if line.strip().startswith("- ")]


def wikilinks(text: str) -> list[tuple[str, str | None]]:
    return [(match.group("target").strip(), match.group("label")) for match in WIKILINK_RE.finditer(text)]


def date_from_issue_filename(path: Path) -> str:
    match = DATE_TWIR_RE.match(path.name)
    return match.group("date") if match else "unknown-date"


def raw_issue_file(issue_dir: Path) -> Path | None:
    matches = sorted(issue_dir.glob("*TWIR-*.md"))
    return matches[0] if matches else None


def raw_issues() -> dict[int, RawIssue]:
    issues: dict[int, RawIssue] = {}
    if not RAW_TWIR.exists():
        return issues
    for child in RAW_TWIR.iterdir():
        if not child.is_dir() or not child.name.isdigit():
            continue
        issue_file = raw_issue_file(child)
        if issue_file is None:
            continue
        issue = int(child.name)
        text = read_text(issue_file)
        frontmatter = parse_frontmatter(text)
        date = str(frontmatter.get("date") or date_from_issue_filename(issue_file))
        issues[issue] = RawIssue(issue=issue, path=issue_file, date=date)
    return dict(sorted(issues.items()))


def raw_issue_path(issue: int) -> Path:
    issue_dir = RAW_TWIR / str(issue)
    if not issue_dir.exists():
        raise SystemExit(f"raw issue directory not found: {rel(issue_dir)}")
    issue_file = raw_issue_file(issue_dir)
    if issue_file is None:
        raise SystemExit(f"raw issue markdown not found in {rel(issue_dir)}")
    return issue_file


def wiki_digest_paths() -> dict[int, Path]:
    digests: dict[int, Path] = {}
    if not WIKI_SOURCES.exists():
        return digests
    for path in WIKI_SOURCES.glob("TWIR *.md"):
        match = re.match(r"^TWIR (?P<issue>\d+)\.md$", path.name)
        if match:
            digests[int(match.group("issue"))] = path
    return dict(sorted(digests.items()))


def article_paths(issue: int) -> list[Path]:
    articles = RAW_TWIR / str(issue) / "articles"
    return sorted(articles.glob("*.md")) if articles.exists() else []


def heading_title(text: str, fallback: str) -> str:
    for line in text.splitlines():
        if line.startswith("# "):
            title = line.removeprefix("# ").strip()
            return re.sub(r"^Item\s+\d+:\s*", "", title)
    return fallback


def field_after_label(text: str, label: str) -> str:
    pattern = re.compile(rf"^{re.escape(label)}:\s*\n(?P<body>.*?)(?=\n[A-Z][A-Za-z ]+:\n|\n## |\n# |\Z)", re.MULTILINE | re.DOTALL)
    match = pattern.search(text)
    return match.group("body").strip() if match else ""


def parse_article_note(path: Path) -> ArticleNote:
    text = read_text(path)
    frontmatter = parse_frontmatter(text)
    summary = field_after_label(text, "Summary")
    recommendation = field_after_label(text, "Recommendation")
    key_takeaways = [line for line in field_after_label(text, "Key takeaways").splitlines() if line.strip().startswith("- ")]
    related = []
    related_match = re.search(r"Related notes:\s*(?P<body>.+)", text)
    if related_match:
        related = [target for target, _label in wikilinks(related_match.group("body"))]
    item = frontmatter.get("item")
    return ArticleNote(
        path=path,
        frontmatter=frontmatter,
        title=heading_title(text, path.stem),
        summary=summary,
        key_takeaways=key_takeaways,
        recommendation=recommendation,
        related_notes=related,
        quality=str(frontmatter.get("quality") or ""),
        item=item if isinstance(item, int) else None,
    )


def page_stems() -> dict[str, list[Path]]:
    pages: dict[str, list[Path]] = {}
    for path in [FRONTEND / "AGENTS.md", INDEX, LOG, *sorted(WIKI.rglob("*.md"))]:
        if not path.exists():
            continue
        pages.setdefault(path.stem, []).append(path)
    return pages


def canonical_key(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", value.lower())


def title_from_target(target: str) -> str:
    target = target.strip()
    if "/" in target:
        target = target.split("/")[-1]
    return Path(target).stem
