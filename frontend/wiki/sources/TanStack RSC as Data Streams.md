---
type: source
status: active
updated: 2026-04-21
tags:
  - tanstack-start
  - server-components
  - tanstack-query
  - source
---

# TanStack RSC as Data Streams

This source reframes React Server Components as stream-shaped data that applications can fetch, cache, and compose explicitly instead of treating RSC as a framework-owned rendering model.

## Summary

- TanStack Start presents RSC payloads as ordinary Flight streams that can be fetched and decoded on demand.
- The model keeps the API surface intentionally small and pushes caching toward existing mechanisms such as Query caches, CDNs, and standard HTTP layers.
- The main architectural claim is that RSC should be usable incrementally and compositionally, without forcing the entire app into a server-owned tree model.

## Why This Source Matters

- It gives the `Server Components` page a much clearer alternative architecture than the vault had before.
- It strengthens the `TanStack Start` branch with concrete RSC positioning instead of only migration and middleware evidence.
- It improves the `Next.js vs TanStack Start` comparison by making the difference about control and composition, not just general framework vibe.

## Caveats

- This is still a perspective from the TanStack side, so it is most useful as an architectural framing source rather than a neutral survey.
- The source is stronger on mental model and composition than on broad production evidence.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[TWIR 277]]

## Raw Sources

- [[../../raw/twir/277/articles/01 - TanStack - React Server Components Your Way|TWIR item note]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
