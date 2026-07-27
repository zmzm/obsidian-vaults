# Scripts

Small helpers for maintaining the Obsidian vaults.

## TWIR ingest helpers

```bash
python3 scripts/twir_status.py
python3 scripts/ingest_missing_twir.py
python3 scripts/create_twir_digest.py --issue 213
python3 scripts/twir_promotion_candidates.py --min-issues 4
python3 scripts/raw_source_status.py
python3 scripts/wiki_lint.py
```

Recommended TWIR ingest sequence:

```bash
python3 scripts/twir_status.py
python3 scripts/raw_source_status.py
# create/review missing digest pages
python3 scripts/create_twir_digest.py --issue <N>
# after wiki edits
python3 scripts/twir_status.py
python3 scripts/twir_promotion_candidates.py --min-issues 4 --limit 40
python3 scripts/wiki_lint.py
```

- `twir_status.py` compares `frontend/raw/twir/` with `frontend/wiki/sources/TWIR N.md` and reports missing digests, orphan digests, and index coverage.
- Pass `--check-raw-index` if you also want to require raw issues to have direct `frontend/index.md` raw-layer links. Use `--since <N>` or `--until <N>` to avoid old-archive noise. Use `--json` for automation.
- `raw_source_status.py` reports standalone `frontend/raw/articles/` files that are not referenced by the wiki/index.
- `ingest_missing_twir.py` reports missing TWIR digests, ranks high-signal article notes, optionally writes draft pages with `--create-drafts`, then can run the final checks.
- `create_twir_digest.py` creates a draft issue digest page from a raw TWIR issue file and article notes. It uses article summaries, recommendations, related notes, and raw links. It does not overwrite existing pages unless `--force` is passed. Use `--status active` only after review.
- `twir_promotion_candidates.py` reports repeated raw tags/topics and normalized digest links across TWIR issues. It scores by relevance, recognizes broader coverage aliases, can hide covered/noisy themes, and supports `--json`.
- `wiki_lint.py` performs mechanical wiki checks: frontmatter type/status, unresolved wikilinks, duplicate page stems, required sections, synthesis index coverage, stale `updated` dates on changed files, and low-backlink pages. Use `--fix` only for safe mechanical formatting fixes.

These scripts automate bookkeeping only. Editorial promotion into concepts, patterns, syntheses, or case studies should still be done manually by the agent/editor.
