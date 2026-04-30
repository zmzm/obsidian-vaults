---
type: guide
status: active
updated: 2026-04-20
---

# QMD Setup Guide

This file explains how to rebuild the `QMD` index for this coding vault on another computer.

It covers:

- creating collections;
- adding useful contexts;
- rebuilding embeddings;
- verifying the final setup.

## Assumptions

- `qmd` is installed and available in the shell.
- the vault lives at a path equivalent to `/home/pentagon-admin/Documents/apps/obsidian-vaults/coding`.
- Ollama is available if you want vector embeddings and `qmd query` / `qmd vsearch` to work well.

## Recommended Collection Layout

Use four collections:

- `coding-root`
- `coding-frontend`
- `coding-backend`
- `coding-common`

This keeps retrieval simple:

- `coding-root` for root maps, audits, setup docs, and shared rules;
- `coding-frontend` for frontend skills and references;
- `coding-backend` for backend skills and references;
- `coding-common` for cross-cutting workflow and Serena material.

## Clean Rebuild

If you want to destroy the old `QMD` index and rebuild from scratch:

```bash
rm -f ~/.cache/qmd/index.sqlite ~/.cache/qmd/index.sqlite-shm ~/.cache/qmd/index.sqlite-wal
```

Then recreate the collections:

```bash
qmd collection add /ABSOLUTE/PATH/TO/coding --name coding-root --mask '*.md'
qmd collection add /ABSOLUTE/PATH/TO/coding/frontend --name coding-frontend --mask '**/*.md'
qmd collection add /ABSOLUTE/PATH/TO/coding/backend --name coding-backend --mask '**/*.md'
qmd collection add /ABSOLUTE/PATH/TO/coding/common --name coding-common --mask '**/*.md'
```

Example for this machine:

```bash
qmd collection add /home/pentagon-admin/Documents/apps/obsidian-vaults/coding --name coding-root --mask '*.md'
qmd collection add /home/pentagon-admin/Documents/apps/obsidian-vaults/coding/frontend --name coding-frontend --mask '**/*.md'
qmd collection add /home/pentagon-admin/Documents/apps/obsidian-vaults/coding/backend --name coding-backend --mask '**/*.md'
qmd collection add /home/pentagon-admin/Documents/apps/obsidian-vaults/coding/common --name coding-common --mask '**/*.md'
```

## Update Existing Collections

If collections already exist and you only want to refresh the index:

```bash
qmd update
```

## Recommended Contexts

`qmd context add` is useful for short operational hints that should be attached to a path prefix.

Recommended contexts for this vault:

### Root context

Attach a short routing note to the vault root:

```bash
qmd context add /ABSOLUTE/PATH/TO/coding "Instruction-oriented coding vault. Start with index.md, then choose frontend, backend, or common. Prefer the narrowest relevant skill and use references only when more detail is needed."
```

### Frontend context

```bash
qmd context add /ABSOLUTE/PATH/TO/coding/frontend "Frontend implementation guidance. Prefer library-specific or boundary-specific references over generic React advice. Reach for UI, routing, react-query, testing, accessibility, and hook references based on task ownership."
```

### Backend context

```bash
qmd context add /ABSOLUTE/PATH/TO/coding/backend "Backend implementation guidance for NestJS and Prisma. Prefer layer-specific retrieval: api for transport contracts, coding for controllers/services/dtos, database for queries and transactions, security for hardening, testing for test structure."
```

### Common context

```bash
qmd context add /ABSOLUTE/PATH/TO/coding/common "Cross-cutting workflow guidance. Use task-workflow for skill-loading decisions, serena for semantic navigation and symbol-level editing, and skill-creator for creating or restructuring skills."
```

## Useful Context Commands

List contexts:

```bash
qmd context list
```

Remove a context:

```bash
qmd context rm /ABSOLUTE/PATH/TO/coding/backend
```

## Build Embeddings

After creating or updating collections, build embeddings:

```bash
qmd embed
```

Force a full rebuild of embeddings:

```bash
qmd embed -f
```

## Verification

Check status:

```bash
qmd status
```

List collections:

```bash
qmd collection list
```

List files in a collection:

```bash
qmd ls coding-backend
qmd ls coding-frontend
```

Test a text search:

```bash
qmd search "query parameters pagination response structure" -c coding-backend --md
```

Test vector search:

```bash
qmd vsearch "progress tracking API weighted average analytics" -c coding-backend --md
```

Test combined query search:

```bash
qmd query "Create progress tracking API with progress endpoints and analytics" -c coding-backend --md
```

## Suggested Rollout Procedure On Another Computer

1. Clone or copy the vault to the target machine.
2. Confirm `qmd` works: `qmd --help`.
3. Remove any stale local `QMD` index if you want a clean rebuild.
4. Add the four collections.
5. Add the four recommended contexts.
6. Run `qmd embed`.
7. Verify with `qmd status`, `qmd ls`, and one `search` plus one `query`.

## Notes On Stability

If `qmd` behaves inconsistently:

- retry `qmd status` first to confirm the index is readable;
- avoid running several heavy `qmd` commands in parallel;
- if SQLite appears stuck, remove the local index files and rebuild;
- if embeddings were interrupted, rerun `qmd embed`.

## Current Intended Baseline

For this vault, the intended baseline setup is:

- 4 collections;
- root plus domain contexts;
- embeddings fully built after indexing;
- root docs like `index.md`, `AGENTS.md`, `RULES.md`, audits, and setup notes indexed through `coding-root`.
