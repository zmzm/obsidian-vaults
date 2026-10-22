---
type: pattern
evidence: mixed
evidence_reviewed: 2026-10-22
status: active
updated: 2026-10-22
tags:
  - data
  - sync
  - local-first
  - react
---

# Client-First Data Sync

Client-First Data Sync is the pattern page for treating client data as an actively synchronized working set rather than as a thin cache glued to server roundtrips.

## Key Ideas

- The core shift is moving user-facing responsiveness off the critical path of network reads and invalidation loops.
- Query caches help with fetch orchestration, but data-heavy applications often need normalized local data, live queries, and optimistic writes that remain coherent across multiple views.
- The hardest part is not storing data locally; it is deciding when a richer client data model genuinely reduces complexity instead of merely relocating it.

- Keep update propagation, optimistic presentation, and durable ordering/conflict resolution distinct. A fast local update does not establish a multi-user synchronization protocol.

## Practical Significance

- This pattern gives the vault a dedicated place for sync-engine thinking, TanStack DB's client-database model, and the tradeoff against plain query-cache architectures.
- It is especially relevant for collaborative products, dashboards, offline-capable apps, and UIs with frequent local writes or large data subsets.

## Current Signals

- The archive now contains both general sync-engine arguments and several increasingly specific TanStack DB signals.
- Those signals line up around the same idea: loading spinners, invalidation choreography, and manual optimistic update logic are often symptoms of a thin client-data model.
- That is enough to justify a dedicated pattern page instead of leaving the subject split between TanStack Query, TanStack DB, and isolated local-first articles.

- Recovered TWIR 292 and 294 articles now distinguish propagation, local mutation queues, optimistic presentation, and cross-user ordering. The state-management essay is an author’s terminology argument; a local Action queue is not a complete synchronization protocol.

## Related Pages

- [[../tools/TanStack|TanStack]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../tools/TanStack DB|TanStack DB]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/Creating Query Abstractions|Creating Query Abstractions]]
- [[../sources/TanStack DB Query-Driven Sync|TanStack DB Query-Driven Sync]]
- [[../sources/TWIR 219|TWIR 219]]
- [[../sources/TWIR 234|TWIR 234]]
- [[../sources/TWIR 245|TWIR 245]]
- [[../sources/TWIR 249|TWIR 249]]
- [[../sources/TWIR 258|TWIR 258]]

- [[Optimistic Mutation Coordination|Optimistic Mutation Coordination]]

## Sources

- [[../../raw/twir/219/articles/02 - DexieJs Reactive local state in React|DexieJs Reactive local state in React]]
- [[../../raw/twir/219/articles/04 - UX++ and DX++ with Sync Engines|UX++ and DX++ with Sync Engines]]
- [[../../raw/twir/234/articles/01 - TanStack DB|TanStack DB]]
- [[../../raw/twir/245/articles/01 - Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query|Stop Re-Rendering — TanStack DB, the Embedded Client Database for TanStack Query]]
- [[../../raw/twir/249/articles/01 - An Interactive Guide to TanStack DB|An Interactive Guide to TanStack DB]]
- [[../../raw/twir/258/articles/01 - TanStack DB 0.5 — Query-Driven Sync|TanStack DB 0.5 — Query-Driven Sync]]
- [[../sources/TanStack DB Query-Driven Sync|TanStack DB Query-Driven Sync]]

- [[../../raw/twir/292/articles/09 - The Absolute State of Management|09 - The Absolute State of Management]] — summary-only.
- [[../../raw/twir/293/articles/04 - Next.js 16 useOptimistic Fixing Rapid-Click Race Conditions & Auto-Rollbacks|04 - Next.js 16 useOptimistic Fixing Rapid-Click Race Conditions & Auto-Rollbacks]] — summary-only.
- [[../../raw/twir/294/articles/15 - Coordinating Optimistic Updates in Next.js|15 - Coordinating Optimistic Updates in Next.js]] — summary-only.

- [[../../raw/twir/292/recovered/09 - The Absolute State of Management|09 - The Absolute State of Management]]
- [[../../raw/twir/294/recovered/15 - Coordinating Optimistic Updates in Next.js|15 - Coordinating Optimistic Updates in Next.js]]

## Open Questions

- Where client-first sync meaningfully outperforms disciplined query-cache patterns in real production systems.
- How much local-first ambition teams can adopt incrementally before backend contracts need to change as well.
