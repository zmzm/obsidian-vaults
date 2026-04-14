---
type: tool
status: seed
updated: 2026-04-14
tags:
  - tanstack
  - query
  - data-fetching
---

# TanStack Query

TanStack Query is the tool hub for client/server data synchronization, query abstractions, and the conventions that shape server-state work in React applications.

## Key Ideas

- The important part is not only the API surface but also the evolving conventions around query definitions and colocated configuration.
- TanStack Query is a useful lens for tracking changes in developer ergonomics and data-fetching best practices.
- The topic intersects with broader questions around reactivity, caching, and server-state management.

## Practical Significance

- This page should accumulate durable rules and mental-model changes, not just scattered release notes.
- It is especially useful to connect it with architectural pages rather than treat it as an isolated library log.

## Current Signals

- The current raw layer already points to stronger convention enforcement around colocated query definitions.
- That makes this page useful not only as a library overview but also as a place to track authoring discipline and tooling-driven patterns.
- Newer raw material also adds a more nuanced source on abstraction tradeoffs over the query API.

## Related Pages

- [[../concepts/Signals|Signals]]
- [[../topics/React Rendering|React Rendering]]
- [[TanStack Start]]
- [[../sources/TanStack Query prefer-query-options|TanStack Query prefer-query-options]]
- [[../sources/Creating Query Abstractions|Creating Query Abstractions]]
- [[../sources/TWIR 270|TWIR 270]]

## Sources

- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
- [[../../raw/twir/266/2026-01-28-TWIR-266|TWIR #266]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/Creating Query Abstractions|Creating Query Abstractions]]
- [[../sources/TanStack Start Single-Flight Mutations|TanStack Start Single-Flight Mutations]]
- [[../sources/TanStack Query prefer-query-options|TanStack Query prefer-query-options]]

## Open Questions

- Which conventions around query options and key organization genuinely reduce complexity at scale.
- Which aspects of TanStack Query deserve their own pattern pages.
