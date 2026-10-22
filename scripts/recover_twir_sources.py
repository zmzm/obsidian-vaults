#!/usr/bin/env python3
"""Inventory missing article bodies and optionally create immutable recovery snapshots."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
import json
from pathlib import Path
import subprocess

from vault_utils import RAW_TWIR, article_paths, parse_article_note, read_text, rel


def missing_body(text: str) -> bool:
    body = text.partition("\nContent:\n")[2].strip()
    return not body or body.startswith(("Content not available.", "Content unavailable."))


def failure_kind(text: str) -> str:
    if "lxml_html_clean" in text or "Missing Python deps" in text:
        return "dependency"
    if "403" in text:
        return "access-denied"
    return "unavailable"


def candidates(issues: list[int], articles: set[tuple[int, int]]) -> list[dict]:
    rows = []
    for issue in issues:
        for path in article_paths(issue):
            note = parse_article_note(path)
            text = read_text(path)
            if articles and (issue, note.item) not in articles:
                continue
            if not missing_body(text):
                continue
            snapshot = path.parent.parent / "recovered" / path.name
            rows.append({
                "issue": issue, "item": note.item, "path": rel(path),
                "title": note.title, "url": note.frontmatter.get("source", ""),
                "failure": failure_kind(text), "snapshot": rel(snapshot),
                "recovered": snapshot.exists(),
            })
    return rows


def recover(row: dict, clipper: Path, python: str, output_root: Path) -> dict:
    target = output_root / str(row["issue"]) / "recovered" / Path(row["path"]).name
    if target.exists():
        return {**row, "recovered": True, "result": "exists"}
    if not str(row["url"]).startswith(("https://", "http://")):
        return {**row, "result": "failed", "error": "Missing HTTP source URL"}
    try:
        proc = subprocess.run(
            [python, str(clipper), row["url"]], capture_output=True,
            text=True, timeout=70, check=False,
        )
        data = json.loads(proc.stdout)
        markdown = data.get("markdown", "").strip()
        if proc.returncode or not data.get("ok") or len(markdown) < 200:
            return {**row, "result": "failed", "error": data.get("error") or "Empty extraction"}
    except (subprocess.TimeoutExpired, OSError, ValueError) as exc:
        return {**row, "result": "failed", "error": str(exc)}
    # A successful extractor response is a snapshot candidate, not editorial verification.
    fetched = datetime.now(timezone.utc).isoformat(timespec="seconds")
    metadata = {
        "type": "twir-recovery", "issue": row["issue"], "item": row["item"],
        "source": row["url"], "final_url": data.get("finalUrl", row["url"]),
        "retrieved": fetched, "original_note": row["path"],
        "editorial_review": "pending", "truncated": "... (content truncated)" in markdown,
    }
    frontmatter = "---\n" + "\n".join(f"{k}: {json.dumps(v)}" for k, v in metadata.items()) + "\n---\n\n"
    original = "../articles/" + Path(row["path"]).stem
    text = frontmatter + f"Original intake note: [[{original}|{row['title']}]]\n\n" + markdown + "\n"
    target.parent.mkdir(parents=True, exist_ok=True)
    # Exclusive creation protects both the original raw note and earlier snapshots.
    with target.open("x", encoding="utf-8") as handle:
        handle.write(text)
    return {**row, "recovered": True, "result": "saved", "characters": len(markdown)}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--since", type=int, default=292)
    parser.add_argument("--until", type=int, default=302)
    parser.add_argument("--article", action="append", default=[], metavar="ISSUE:ITEM")
    parser.add_argument("--write", action="store_true", help="fetch and save new snapshots; default inventories only")
    parser.add_argument("--clipper", type=Path, help="path to the react-news-bot Python clipper")
    parser.add_argument("--python", default="python3", help="interpreter with the clipper requirements installed")
    parser.add_argument("--output-root", type=Path, default=RAW_TWIR)
    parser.add_argument("--workers", type=int, default=4, help="concurrent fetches (1–8)")
    parser.add_argument("--report", type=Path)
    args = parser.parse_args()
    if args.since > args.until:
        parser.error("--since must not exceed --until")
    if not 1 <= args.workers <= 8:
        parser.error("--workers must be between 1 and 8")
    try:
        selected = {tuple(map(int, value.split(":"))) for value in args.article}
        if any(len(value) != 2 for value in selected):
            raise ValueError()
    except ValueError:
        parser.error("--article must have the form ISSUE:ITEM")
    issues = sorted({n for n, _ in selected}) if selected else list(range(args.since, args.until + 1))
    rows = candidates(issues, selected)
    if args.write:
        if not args.clipper or not args.clipper.is_file():
            parser.error("--write requires an existing --clipper script")
        with ThreadPoolExecutor(max_workers=args.workers) as executor:
            rows = list(executor.map(
                lambda row: recover(row, args.clipper, args.python, args.output_root), rows,
            ))
    report = {"missing_original_bodies": len(rows), "articles": rows}
    encoded = json.dumps(report, indent=2, ensure_ascii=False) + "\n"
    if args.report:
        args.report.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    return 1 if any(row.get("result") == "failed" for row in rows) else 0


if __name__ == "__main__":
    raise SystemExit(main())
