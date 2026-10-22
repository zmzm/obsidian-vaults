---
type: case-study
status: active
evidence: full-text
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [lovable, migration, tanstack-start, nextjs, rollout]
---

# Lovable Incremental Framework Migration

Lovable’s retrieved engineering account describes moving its own application from Next.js to TanStack Start while serving users through both frameworks.

## Context

- Dogfooding Lovable’s own hosting and sharing the stack with generated apps were the main goals. The author explicitly reports that the previous host had resolved earlier scaling issues.
- A proxy selected frameworks per route group and user. Migration groups followed common journeys to limit expensive full-document crossings, while deterministic flag overrides let tests cover both variants.
- Shared code used enforced import boundaries and small platform adapters. Framework-specific dependencies were reduced before broad code migration.
- Internal testing, gradual user rollout, rollback, and performance monitoring continued while agents moved code. Faster migration did not remove the need to observe production.

## Results and Tradeoffs

- The retrieved account reports better median TTFB but initially worse p90 and mostly unchanged client metrics. It also describes substantial custom build-plugin work.
- Cross-document view transitions reduced visual disruption at framework crossings; they did not eliminate the extra document-loading work.
- The article was fetched on 2026-10-22 and may have changed since TWIR 294. Scale figures and outcomes refer to that retrieved account.

## Why It Matters

A useful migration seam combines portable feature code, framework-specific adapters, deterministic routing decisions, and bounded rollout. The target framework alone does not explain the outcome.

## Related Pages

- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/Next.js|Next.js]]
- [[../tools/Vite|Vite]]
- [[Railway Off Next.js|Railway Off Next.js]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[../sources/TanStack Router Navigation Lifetimes|TanStack Router Navigation Lifetimes]]

## Sources

- [[../../raw/twir/294/recovered/10 - How Lovable.dev Migrated from Next.js to TanStack Start|10 - How Lovable.dev Migrated from Next.js to TanStack Start]]

## Open Questions

- What tail-latency and bundling costs persist after the final cutover?
- Which checks prevent new framework-specific feature code while both stacks keep evolving?
