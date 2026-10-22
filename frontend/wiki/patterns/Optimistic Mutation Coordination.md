---
type: pattern
status: active
evidence: full-text
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [react, optimistic-ui, actions, mutation, concurrency]
---

# Optimistic Mutation Coordination

Optimistic mutation coordination separates immediate presentation from confirmed state, mutation ordering, and handling failures or conflicting writers.

## Key Ideas

- Compute a queued change against the previous confirmed result when the queue executes. Serial requests still lose updates if their full replacement payloads were computed from the same stale state.
- A useActionState dispatcher provides a local sequence and previous result. useOptimistic overlays temporary presentation while Actions are pending; their composition does not create a global transaction.
- In the reviewed Huddle example, an error preserves the last confirmed groups and the optimistic overlay resolves back to that base. This changes the UI without undoing an already committed server write.
- Coordination across components needs explicit scope and ownership. Coordination across users or devices needs a server conflict policy or synchronization model beyond one client queue.

## Practical Significance

- Test two rapid dependent edits, failure between edits, retry behavior, and confirmation arriving alongside refreshed data.
- Choose intent-like payloads where possible so later changes can apply to the latest confirmed base.
- The recovered tutorial is truncated; only its reviewed Huddle section is used here. Current React references support the queue and optimistic-state boundaries.

## Related Pages

- [[Client-First Data Sync|Client-First Data Sync]]
- [[Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[../sources/React useTransition|React useTransition]]

## Sources

- [[../../raw/twir/294/recovered/15 - Coordinating Optimistic Updates in Next.js|15 - Coordinating Optimistic Updates in Next.js]]
- [[../../raw/articles/React useActionState Reference - 2026-10-22|React useActionState Reference - 2026-10-22]]
- [[../../raw/articles/React useOptimistic Reference - 2026-10-22|React useOptimistic Reference - 2026-10-22]]
- [[../../raw/twir/292/recovered/09 - The Absolute State of Management|09 - The Absolute State of Management]] — opinionated terminology argument; not a universal definition of state management.

## Open Questions

- How should later queued edits be handled when an earlier mutation fails?
- Where are version checks, idempotency, conflict resolution, or compensation needed beyond presentation rollback?
