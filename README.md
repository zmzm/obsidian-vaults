# Vaults Workspace

Personal knowledge-base vaults maintained as LLM-driven wikis, stored as markdown and browsed in Obsidian.

## Vaults

### `frontend/` — Frontend Wiki

The primary vault. An LLM-maintained wiki built on top of *This Week in React* source material.

**Layers:**
- `raw/twir/` — TWIR issues with per-article notes as the intake layer
- `wiki/` — curated durable knowledge

**Wiki page types:** concepts, tools, patterns, topics, case-studies, sources, syntheses

**Navigation:** `index.md` (content map), `log.md` (append-only operation log), `AGENTS.md` (agent rules).

### `LLM/` — LLM Notes

Notes on transformer architecture, reasoning models, and how LLMs work internally.

### `coding/` — Coding Wiki

A second LLM-maintained wiki covering backend, frontend, and general coding practices.

## Workspace-level Files

- `LLM-WIKI.md` — a detailed writeup of the LLM wiki pattern: the raw/wiki/schema architecture, ingest/query/lint workflows, and implementation notes.

## Conventions

- Markdown-first, Obsidian-compatible with `[[wikilinks]]`.
- Each vault is self-contained: its own `AGENTS.md`, `index.md`, `log.md`.
- Raw layers store immutable sources; wiki layers hold agent-curated knowledge.
- All vaults follow the ingest → normalize → synthesize → lint cycle described in `LLM-WIKI.md`.
- TWIR ingest helpers live in `scripts/`; agents should run `python3 scripts/twir_status.py` before and after TWIR ingest, then use `twir_promotion_candidates.py` to flag repeated themes for editorial review.
- User-facing workflow is intentionally simple: ask the agent for `ingest` or `lint`; the agent runs the scripts and performs the wiki updates/checks.
