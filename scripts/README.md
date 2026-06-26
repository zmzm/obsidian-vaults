# Scripts

Small helpers for maintaining the Obsidian vaults.

## TWIR ingest helpers

```bash
python3 scripts/twir_status.py
python3 scripts/create_twir_digest.py --issue 213
python3 scripts/twir_promotion_candidates.py --min-issues 4
python3 scripts/wiki_lint.py
```

Recommended TWIR ingest sequence:

```bash
python3 scripts/twir_status.py
# create/review missing digest pages
python3 scripts/create_twir_digest.py --issue <N>
# after wiki edits
python3 scripts/twir_status.py
python3 scripts/twir_promotion_candidates.py --min-issues 4 --limit 40
```

- `twir_status.py` compares `frontend/raw/twir/` with `frontend/wiki/sources/TWIR N.md` and reports missing digests, orphan digests, and index coverage.
- Pass `--check-raw-index` if you also want to require every raw issue to have a direct `frontend/index.md` raw-layer link.
- `create_twir_digest.py` creates a draft issue digest page from a raw TWIR issue file. It does not overwrite existing pages unless `--force` is passed.
- `twir_promotion_candidates.py` reports repeated raw tags/topics and normalized digest links across TWIR issues. It is read-only and meant to guide editorial promotion decisions.
- `wiki_lint.py` performs mechanical wiki checks: frontmatter type/status, unresolved wikilinks, duplicate page stems, and low-backlink pages.

These scripts automate bookkeeping only. Editorial promotion into concepts, patterns, syntheses, or case studies should still be done manually by the agent/editor.
