---
type: audit
status: active
updated: 2026-04-16
---

# Backend Cleanup Audit

This audit reviews the current backend skill corpus after the earlier frontend-heavy cleanup passes.

## Overall Judgment

The backend branch is meaningfully healthier than the frontend branch was.

Why:

- more pages are tied to real backend layer boundaries;
- there is less generic “best practices” repetition;
- more files encode framework- or stack-specific retrieval value;
- fewer near-duplicate page families exist.

That said, the backend branch still has a few weak areas:

- `versioning/` is the weakest cluster;
- parts of `debug/` are still generic;
- parts of `security/` are broad enough that they risk restating common model knowledge;
- a few `api/` and `coding/` references overlap more than necessary.

## Strong Keep Candidates

These files are strong enough to keep as real retrieval targets.

### API

- `backend/api/references/restful-conventions.md`
- `backend/api/references/response-structure.md`
- `backend/api/references/query-parameters.md`
- `backend/api/references/error-responses.md`

Reason:

- these encode concrete transport-layer decisions;
- they are specific enough to NestJS REST work;
- they are closer to policy than to generic web wisdom.

### Coding

- `backend/coding/references/controllers.md`
- `backend/coding/references/services.md`
- `backend/coding/references/dtos.md`
- `backend/coding/references/error-handling.md`

Reason:

- they map to real NestJS layers and responsibilities;
- they give the agent meaningful retrieval anchors when changing backend code.

### Database

- `backend/database/references/queries.md`
- `backend/database/references/transactions.md`
- `backend/database/references/indexing.md`
- `backend/database/references/migrations.md`

Reason:

- these are stack-specific and high-value;
- they are much less likely to be fully covered by generic model prior knowledge.

### Testing

- `backend/testing/references/test-layer-patterns.md`
- `backend/testing/references/mocking-patterns.md`

Reason:

- the layer split and Prisma mocking patterns are useful and sufficiently concrete.

## Merge Candidates

These are the best places to reduce redundancy without harming coverage.

### DTO Overlap

- `backend/api/references/dto-design.md`
- `backend/coding/references/dtos.md`

Reason:

- the split is understandable, but still slightly redundant;
- one page handles DTO design and another handles DTO basics and Prisma alignment.

Preferred action:

- keep `backend/coding/references/dtos.md` for simple DTO discipline;
- keep `backend/api/references/dto-design.md` only if it stays clearly focused on query DTOs, transforms, and nested validation;
- otherwise merge into one canonical DTO page.

### Debug Cluster

- `backend/debug/references/common-issues.md`
- `backend/debug/references/debugging-tools.md`

Reason:

- the cluster is already small, but `common-issues.md` is drifting toward generic debugging lore;
- `debugging-tools.md` may already be enough as the more actionable page.

Preferred action:

- either keep both but narrow `common-issues.md` to truly recurring local failure modes;
- or merge the recurring failure modes into `debugging-tools.md` and remove the generic remainder.

### API Nested/Pagination Boundary

- `backend/api/references/query-parameters.md`
- `backend/database/references/pagination.md`

Reason:

- some pagination concerns belong at the API boundary and some at the query layer;
- the overlap is not severe, but the distinction should be sharpened.

Preferred action:

- keep API pagination input and DTO concerns in `query-parameters.md`;
- keep DB pagination execution tradeoffs in `database/pagination.md`;
- remove duplicated examples if they say the same thing twice.

## Delete or Rewrite Candidates

These files are the weakest parts of the backend branch.

### Versioning Cluster

- `backend/versioning/references/strategies.md`
- `backend/versioning/references/module-structure.md`
- `backend/versioning/references/deprecation.md`
- `backend/versioning/references/breaking-changes.md`

Reason:

- this cluster is broad, policy-like, and partly speculative;
- many teams do not need active API versioning guidance often enough to justify four separate pages;
- several sections read like textbook guidance rather than local operating rules.

Preferred action:

- reduce this cluster to at most two pages:
  - `versioning-policy.md`
  - `deprecation-and-migration.md`
- or delete the entire cluster if API versioning is not a frequent real workflow in your projects.

Strongest delete candidate inside this cluster:

- `backend/versioning/references/module-structure.md`

Reason:

- highly specific example structure with relatively low retrieval value;
- likely not worth a standalone page unless this exact versioning layout is a hard project convention.

### Broad Security Survey Page

- `backend/security/references/owasp-protection.md`

Reason:

- most likely the most generic backend page in the whole corpus;
- “OWASP Top 10 protection” is useful as a concept, but too broad for a high-value retrieval page unless it is rewritten into local policy.

Preferred action:

- either delete it;
- or rewrite it into a small project-specific security baseline page with only the protections that are actually expected in your codebase.

### Refactor Anti-Patterns

- `backend/refactor/references/anti-patterns.md`

Reason:

- likely broad and checklist-like;
- refactor guidance is usually better framed as allowed/safe transformations than as a long anti-pattern list.

Preferred action:

- merge the strongest points into `safe-refactorings.md` and `permission-required.md`;
- then delete this page.

## Narrow-but-Useful Pages That Should Stay Small

These pages are worth keeping, but only if they remain sharply scoped:

- `backend/security/references/input-validation.md`
- `backend/security/references/rate-limiting.md`
- `backend/security/references/http-headers.md`
- `backend/database/references/transactions.md`
- `backend/testing/references/mocking-patterns.md`

If these pages grow into generic security essays, they will lose value quickly.

## Biggest Backend Risk

The main backend risk is not duplication at the same scale as frontend.

The main backend risk is **policy inflation**:

- versioning rules that may not matter often;
- security pages that drift into generic OWASP summaries;
- debug pages that repeat common engineering instincts.

## Recommended Cleanup Order

1. decide whether `backend/versioning/` should stay as a real branch at all;
2. delete or rewrite `backend/security/references/owasp-protection.md`;
3. merge or delete `backend/refactor/references/anti-patterns.md`;
4. sharpen the boundary between `api/dto-design.md` and `coding/dtos.md`;
5. optionally collapse the `debug/` branch into one stronger page if it remains generic.

## Summary

Backend is in better shape than frontend.

It has fewer redundant page families, stronger stack specificity, and clearer layer ownership.

The cleanup priority for backend is therefore not broad reduction.
It is targeted trimming of:

- versioning sprawl;
- generic security survey material;
- refactor/debug pages that drift away from concrete local practice.
