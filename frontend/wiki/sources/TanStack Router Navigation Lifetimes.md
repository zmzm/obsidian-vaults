---
type: source
status: active
evidence: full-text
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [tanstack-router, navigation, concurrency, source]
---

# TanStack Router Navigation Lifetimes

The recovered TanStack navigation article separates ownership of loader work from permission to publish, route outcome selection, and acknowledgment that UI committed.

## Summary

- A loader flight has shared ownership through leases; losing one navigation consumer does not require aborting work still used by a preload or cache.
- The current transaction owns publication authority. A superseded lane may no longer update the UI even if its loader keeps running for another consumer.
- The lane reduces outcomes for the route attempt. One error finishing first does not necessarily decide the result while already-started work may redirect.
- A render receipt describes whether one publication committed. Commitment is distinct from browser paint; loader completion, publication, and visible output are different events.

## Why This Source Matters

Provides a concrete model for overlapping navigation rather than equating cancellation with supersession or successful fetching with rendered UI.

## Related Pages

- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../patterns/Typed Routing and URL State|Typed Routing and URL State]]
- [[../topics/React Rendering|React Rendering]]
- [[../case-studies/Lovable Incremental Framework Migration|Lovable Incremental Framework Migration]]

## Sources

- [[../../raw/twir/294/recovered/13 - Inside a TanStack Router Navigation|13 - Inside a TanStack Router Navigation]]

## Open Questions

- Which lifetime should a production metric observe: fetch completion, commit, or paint?
- How do request cleanup and streaming ownership extend the client-side model?
