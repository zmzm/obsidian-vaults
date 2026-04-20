---
type: audit
status: active
updated: 2026-04-16
---

# Coding Vault Cleanup Audit

This file captures the first content-quality pass over the coding vault after structural normalization.

The main conclusion is:

- the vault is not too large overall;
- the main problem is repeated generic guidance;
- the highest-noise cluster is `frontend/*/references/core-principles.md` and `frontend/*/references/anti-patterns.md`;
- several pages are better treated as canonical references, while others should be merged or deleted.

## Highest-Value Cleanup Rule

Delete or merge pages when they are mostly:

- generic best practices a coding-focused AI agent already knows;
- repeated in several neighboring references;
- not project-specific;
- not the obvious canonical landing page for a topic.

Keep pages when they contain:

- product-specific conventions;
- library-specific APIs or wrappers;
- project-specific boundaries;
- examples that encode local decisions rather than general web advice.

## Delete Candidates

These are the strongest candidates for removal after their useful rules are folded elsewhere.

### Frontend Generic Principle Pages

- `frontend/auth/references/core-principles.md`
- `frontend/error-handling/references/core-principles.md`
- `frontend/performance/references/core-principles.md`
- `frontend/react-query/references/core-principles.md`
- `frontend/routing/references/core-principles.md`

Reason:

- these are mostly generic framework advice;
- they duplicate more concrete pages in the same skill;
- they are weak as standalone retrieval targets.

Preferred action:

- move any genuinely local rules into the owning `SKILL.md` or the more specific reference pages;
- then delete these files.

### Frontend Generic Anti-Pattern Pages

- `frontend/auth/references/anti-patterns.md`
- `frontend/error-handling/references/anti-patterns.md`
- `frontend/routing/references/anti-patterns.md`

Reason:

- these are mostly just the inverse of the concrete guidance already documented elsewhere;
- they add another retrieval surface without adding much unique structure.

Preferred action:

- fold the few local anti-pattern bullets into the concrete files they belong to;
- then delete these files.

### Generic Checklists That Likely Add Little Unique Value

- `frontend/performance/references/checklist.md`
- `frontend/accessibility/references/wcag-checklist.md`
- `backend/debug/references/decision-tree.md`

Reason:

- these are highly generic operational checklists;
- a coding agent already knows most of this by default;
- the value is low unless they encode local constraints, which these currently do not strongly do.

Preferred action:

- either delete outright;
- or keep only if rewritten to reflect project-specific policy and not general industry advice.

## Merge Candidates

These files likely should not survive as separate pages.

### Frontend Core/Anti-Pattern Consolidation

For each skill below, prefer one stronger canonical page rather than separate `core-principles` and `anti-patterns` pages:

- `frontend/testing/references/core-principles.md`
- `frontend/testing/references/anti-patterns.md`
- `frontend/react-query/references/core-principles.md`
- `frontend/react-query/references/anti-patterns.md`
- `frontend/hook/references/core-principles.md`
- `frontend/hook/references/anti-patterns.md`
- `frontend/i18n/references/core-principles.md`
- `frontend/i18n/references/anti-patterns.md`

Preferred action:

- merge each pair into one canonical page such as `principles.md` or keep the stronger one and absorb the weaker one into it.

Notes:

- `testing/core-principles` and `testing/anti-patterns` are especially close.
- `react-query/core-principles` and `react-query/anti-patterns` are especially close.

### Hook / React Query Mutation Overlap

- `frontend/hook/references/mutations.md`
- `frontend/react-query/references/mutations.md`
- `frontend/react-query/references/custom-hooks.md`

Reason:

- these are conceptually one cluster;
- current separation is too fine-grained;
- hook-level mutation guidance is probably better as a subsection of React Query custom-hook guidance.

Preferred action:

- keep `frontend/react-query/references/mutations.md` as the canonical mutation page;
- merge `frontend/hook/references/mutations.md` into `frontend/react-query/references/custom-hooks.md` or into the canonical mutations page.

### Testing Layer Overlap

- `backend/testing/references/controller-tests.md`
- `backend/testing/references/service-tests.md`

Reason:

- these are the closest backend duplicates by lexical overlap;
- they likely want one shared testing structure page plus short controller/service-specific subsections.

Preferred action:

- merge into one page such as `backend/testing/references/test-layer-patterns.md`;
- or keep one shared canonical testing-shape page and shorten the layer-specific pages heavily.

### Serena Overlap

- `common/serena/references/best-practices.md`
- `common/serena/references/tools.md`
- `common/serena/references/workflows.md`

Reason:

- tool choice, best practices, and workflows strongly overlap;
- the current split is probably too granular.

Preferred action:

- keep `tools.md` and `workflows.md`;
- merge `best-practices.md` into one of them and delete it.

## Keep as Canonical

These are good examples of pages that should remain because they own a real boundary.

### Frontend

- `frontend/ui/references/forms.md`
- `frontend/accessibility/references/forms.md`
- `frontend/accessibility/references/testing.md`
- `frontend/react-query/references/query-options.md`
- `frontend/react-query/references/cache-invalidation.md`
- `frontend/error-handling/references/api-errors.md`
- `frontend/error-handling/references/error-boundaries.md`
- `frontend/routing/references/route-guards.md`
- `frontend/ui/references/components.md`
- `frontend/chakra-ui/references/chakra-theme-tokens.md`

Reason:

- these pages encode either a specific library boundary or a real implementation decision space.

### Backend

- `backend/api/references/restful-conventions.md`
- `backend/api/references/response-structure.md`
- `backend/database/references/queries.md`
- `backend/database/references/transactions.md`
- `backend/security/references/input-validation.md`
- `backend/security/references/rate-limiting.md`

Reason:

- these are concrete enough to justify retrieval;
- they represent actual design decisions rather than generic coding platitudes.

### Common

- `common/serena/references/editing.md`
- `common/serena/references/tools.md`

Reason:

- Serena-specific operational knowledge is not generic model knowledge and is worth keeping.

## Files to Split, Not Delete

- `frontend/coding/references/file-structure.md`

Reason:

- this file is too large and likely mixes several concerns:
  - file naming;
  - folder layout;
  - component colocation;
  - hook naming;
  - test placement.

Preferred action:

- split into several narrower references instead of keeping one large catch-all page.

## Cleanup Order

If doing the cleanup incrementally, use this order:

1. remove or merge `core-principles` pages that add little unique value;
2. remove or merge weak `anti-patterns` pages;
3. consolidate mutation and testing overlap clusters;
4. merge `common/serena/references/best-practices.md` into a stronger page;
5. split oversized files such as `frontend/coding/references/file-structure.md`.

## Summary Judgment

The vault does contain a meaningful amount of content that a strong coding agent already knows.

The biggest win is not deleting advanced library-specific guidance.
The biggest win is deleting or merging:

- generic principle pages;
- generic anti-pattern pages;
- checklist-style pages that do not encode local policy;
- near-duplicate pages that differ more by folder than by substance.
