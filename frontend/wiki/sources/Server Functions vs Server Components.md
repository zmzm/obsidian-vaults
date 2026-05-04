---
type: source
status: active
updated: 2026-04-30
tags:
  - server-components
  - server-functions
  - tanstack-start
---

# Server Functions vs Server Components

This source compares two modern React data-access models: client-driven server functions and server-centric React Server Components.

## Summary

- Server functions behave more like transparent RPC from client-capable code, giving applications granular calls and invalidation points.
- Server Components move more composition and data fetching into the server-rendered tree.
- RSCs do not remove data-fetching architecture problems; teams still need to hoist data to avoid waterfalls and coordinate cache boundaries.
- The choice is partly about preferred ownership of data flow: client-driven calls versus server-driven composition.

## Why This Source Matters

- It strengthens `Server Components Beyond Next.js` with a comparison against server functions, not only against other RSC frameworks.
- It supports `TanStack Start` because server functions are one of the framework's explicit primitives.
- It gives the RSC branch a useful counterweight to overclaiming that RSC automatically solves data fetching.

## Caveats

- The source is architectural commentary and should be balanced against later framework docs and production reports.
- The exact tradeoffs vary by framework implementation and cache model.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[TanStack Start Content Apps]]
- [[TWIR 218]]

## Raw Sources

- [[../../raw/twir/218/articles/04 - Why Server Functions Matter In A Server Component World|Why Server Functions Matter In A Server Component World]]
- [[../../raw/twir/218/2025-01-22-TWIR-218|TWIR #218]]
