---
type: log
status: active
updated: 2026-04-20
---

# Log

## [2026-04-16] structure | Root scaffold for coding vault

- Added `AGENTS.md` to define the coding vault as an instruction-oriented skill library rather than a source-ingest wiki.
- Added `index.md` as the root navigation map for `frontend`, `backend`, and `common`.
- Added `backend/INDEX.md` and `common/INDEX.md` so those branches have explicit entry points like `frontend/INDEX.md`.
- Next sensible step: normalize metadata and formatting across `SKILL.md` and `references/` files, then reduce duplicated cross-skill guidance.

## [2026-04-16] structure | QMD-ready normalization layer

- Added `RULES.md` to define cross-vault rule priority, wording discipline, and conflict handling.
- Added shared templates for `SKILL.md`, `references/*.md`, and `INDEX.md`.
- Updated root guidance so future edits can migrate the corpus gradually toward a consistent `QMD`-ready format.
- Next sensible step: apply the new templates incrementally to the highest-value skills first, starting with the most duplicated or most frequently used frontend files.

## [2026-04-16] normalize | Corpus-wide format alignment

- Normalized all current `SKILL.md` files into a shared routing-oriented structure with consistent section ordering.
- Added frontmatter to reference files that previously had none so the whole corpus is now easier to index and reason about mechanically.
- Manually rewrote the `common/` skill entry points after the broad pass because they were originally guide-style documents rather than sectioned skill files.
- Next sensible step: start a second pass focused on content quality rather than format, especially canonical references, duplicated rules, and overly absolute wording.

## [2026-04-16] cleanup | First content-reduction pass

- Removed fourteen low-value generic reference pages, mainly weak `core-principles`, `anti-patterns`, checklist, and decision-tree files.
- Folded testing anti-pattern guidance into `frontend/testing/references/core-principles.md`.
- Folded hook-level mutation return guidance into `frontend/react-query/references/custom-hooks.md` and removed the extra hook mutation page.
- Merged Serena best-practice guidance into `common/serena/references/tools.md` and removed the extra standalone page.
- Rewired affected `SKILL.md` and reference links so the remaining references point to stronger canonical pages.
- Next sensible step: second cleanup pass on medium-value overlaps such as React Query anti-patterns, hook core/anti-pattern split, and backend controller/service testing duplication.

## [2026-04-16] cleanup | Second consolidation pass

- Merged hook anti-pattern guidance into `frontend/hook/references/core-principles.md` and removed the extra anti-pattern page.
- Merged i18n anti-pattern guidance into `frontend/i18n/references/core-principles.md` and removed the extra anti-pattern page.
- Folded React Query anti-pattern guidance into `frontend/react-query/references/query-options.md` and removed the extra anti-pattern page.
- Replaced separate backend controller/service testing pages with one canonical `backend/testing/references/test-layer-patterns.md`.
- Split the oversized frontend file-structure page into `component-structure.md`, `hook-file-conventions.md`, and `test-placement.md`.
- Rewired affected skill maps to the new canonical references.
- Next sensible step: third pass on lower-level redundancy, especially whether some remaining `core-principles` pages in `accessibility`, `testing`, `ui`, and `i18n` should be renamed or further narrowed.

## [2026-04-20] docs | QMD rollout guide

- Added `qmd-setup.md` with commands for clean rebuild, collection creation, context setup, embeddings, and verification on another machine.
- Linked the new guide from `index.md` so the vault now contains its own `QMD` deployment instructions.
- Next sensible step: if the collection layout or context texts change later, update the setup guide and keep it aligned with the actual local `QMD` baseline.
