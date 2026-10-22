---
type: synthesis
status: active
evidence: full-text
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [react, async, actions, transitions, effects]
---

# Async React Patterns - use() vs useTransition vs useEffect

These React APIs operate at different boundaries: render-time reads, non-blocking updates and Actions, and synchronization with external systems.

## Short Thesis

Use use() to consume a render-time resource, transitions to coordinate non-blocking updates and Action pending state, and effects to synchronize external systems after commit. Mutation ordering and optimistic presentation require their own explicit contracts.

## Render-time Reads

use() consumes promises or context during render. Promise reads can participate in Suspense and error boundaries; resource ownership and stable promise identity still need a framework or data-layer contract.

## Transitions and Async Actions

Current React documentation includes async Actions in startTransition. A transition coordinates non-blocking updates and pending UI; it is not limited to synchronous render optimization. The Action callback starts immediately, so arbitrary synchronous computation inside it still blocks. State updates after await currently need another transition wrapper. Custom async work may finish out of order; transition priority does not establish request ordering.

## Effects and Lifecycle

Effects synchronize committed UI with external systems. The extracted Activity failure case shows why render-time allocation cannot depend on a later effect for cleanup: a hidden subtree may render without its effects mounting. This supplies stronger direct evidence than the older unextracted anti-effect essay.

## Mutation Coordination

useActionState queues calls through its dispatcher and supplies the previous result. useOptimistic shows temporary state during an Action. Apply changes to confirmed state when they execute; request order alone cannot repair payloads computed from a stale snapshot. A local queue is not a cross-user conflict protocol.

## Practical Significance

- First identify whether the problem concerns reading data, responsiveness, external synchronization, mutation order, or confirmation of optimistic state.
- Validate overlapping interactions and failures. UI returning to a confirmed base is not a server transaction rollback.
- Keep controlled text inputs urgent and separate expensive derived rendering where needed.

## Current Evidence Quality

The correction uses the three current first-party React API references, the extracted Activity case, and the recovered Huddle mutation example. The latter snapshot is truncated, so only its reviewed sidebar example supports this page; it is not evidence for the complete later Flow implementation.

## Related Pages

- [[../concepts/React use()|React use()]]
- [[../sources/React useTransition|React useTransition]]
- [[../concepts/React Activity|React Activity]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[../patterns/Optimistic Mutation Coordination|Optimistic Mutation Coordination]]
- [[../patterns/Client-First Data Sync|Client-First Data Sync]]
- [[../topics/React Rendering|React Rendering]]

## Sources

- [[../sources/React useTransition|React useTransition]]
- [[../../raw/twir/298/articles/06 - React Activity When A Render No Longer Guarantees an Effect|06 - React Activity When A Render No Longer Guarantees an Effect]]
- [[../../raw/twir/294/recovered/15 - Coordinating Optimistic Updates in Next.js|15 - Coordinating Optimistic Updates in Next.js]]
- [[../../raw/articles/React useActionState Reference - 2026-10-22|React useActionState Reference - 2026-10-22]]
- [[../../raw/articles/React useOptimistic Reference - 2026-10-22|React useOptimistic Reference - 2026-10-22]]

## Open Questions

- Which state should share one mutation queue and which writes can proceed independently?
- How do framework or data-library contracts add cancellation, freshness, and conflict handling beyond React’s local APIs?
