---
type: case-study
status: active
updated: 2026-10-22
tags: [remix, react-router, migration, ai, validation]
---

# Remix v2 to React Router Route Parity

Kent C. Dodds’s migration account shows how comparing generated route structures gave an agent a concrete correction target while upgrading Remix v2 to React Router v7.

## Context

- The application had existing tests, documentation, framework patches, and a file-route convention. Dependency upgrades were grouped by difficulty and larger changes were handled separately.
- The author chose to change route-convention tooling during the upgrade. The first attempt did not preserve the intended route structure.
- Comparing the original remix routes output with the migrated react-router routes output exposed the mismatch; the author then specified structural equivalence despite changed filenames and ordering.
- Further type updates, automated review, and human interaction checks followed before merging. Route-tree parity was one validation step, not a complete behavior proof.

## Why It Matters

- Generated structural output can make a migration requirement reviewable and give an agent fast evidence for correcting a wrong transformation.
- This is a Remix v2 continuation into React Router, not evidence for a Remix v2-to-Remix 3 upgrade path.
- Changing route conventions adds migration work. The account documents a choice made in one application rather than recommending combined migrations by default.

## Related Pages

- [[../tools/Remix|Remix]]
- [[../tools/React Router|React Router]]
- [[../patterns/Typed Routing and URL State|Typed Routing and URL State]]
- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Sources

- [[../../raw/twir/270/articles/06 - Kent C. Dodds - Migrating Remix v2 to React Router v7 with Cursor|06 - Kent C. Dodds - Migrating Remix v2 to React Router v7 with Cursor]]

## Open Questions

- Which route behaviors require browser or integration checks beyond structural parity?
- How should redirects, route precedence, loader/action contracts, and error boundaries be compared during a convention change?
