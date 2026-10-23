# Vaults Workspace

Personal knowledge vaults and a reusable coding instruction library, stored as Markdown and browsed in Obsidian.

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

### `coding/` — Coding Instruction Library

A curated library of reusable frontend, backend, and cross-cutting engineering skills. Start with [coding/index.md](coding/index.md); [coding/AGENTS.md](coding/AGENTS.md) defines its instruction-oriented structure and authoring rules. It does not use raw/source ingestion layers.

## Workspace-level Files

- `LLM-WIKI.md` — a detailed writeup of the LLM wiki pattern: the raw/wiki/schema architecture, ingest/query/lint workflows, and implementation notes.

## Conventions

- Markdown-first, Obsidian-compatible with `[[wikilinks]]`.
- Each vault is self-contained: its own `AGENTS.md`, `index.md`, `log.md`.
- Where a vault uses raw/wiki layers, raw layers store immutable sources and wiki layers hold agent-curated knowledge.
- The frontend wiki follows the ingest → normalize → synthesize → lint cycle described in `LLM-WIKI.md`; `coding/` follows its skill authoring and validation conventions.
- TWIR ingest helpers live in `scripts/`; agents should run `python3 scripts/twir_status.py` before and after TWIR ingest, then use `twir_promotion_candidates.py` to flag repeated themes for editorial review.
- For the frontend wiki, ask the agent for `ingest` or `lint`; the agent runs the scripts and performs the wiki updates/checks.
