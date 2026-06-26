---
type: source
status: active
updated: 2026-06-26
tags:
  - react
  - server-components
  - tanstack-start
  - source
---

# RSC as Protocol

This source frames React Server Components as a protocol for serializing and streaming UI, not as one fixed server-owned application architecture.

## Summary

- RSC can support both server-owned trees with client islands and client-owned trees that fetch server-rendered fragments.
- TanStack Start's framing emphasizes composite components that let client code request and cache server-rendered output.
- The important distinction is ownership of the tree: framework defaults decide whether the server owns the app shell or whether the client can embed server fragments more freely.

## Why This Source Matters

- It sharpens the `Server Components Beyond Next.js` synthesis by separating protocol capability from framework architecture.
- It strengthens the `TanStack Start` branch with a concrete RSC composition model beyond ordinary SSR.
- It gives the vault a better vocabulary for comparing RSC implementations: tree ownership, caching surface, and composition direction.

## Caveats

- This is a TanStack-authored argument, so it is strongest as a framework-positioning source rather than a neutral survey.
- It should be read alongside bundler-boundary and server-function sources because protocol flexibility still depends on tooling and runtime integration.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[TanStack RSC as Data Streams]]
- [[RSC Bundle Boundaries]]

## Raw Sources

- [[../../raw/twir/280/articles/03 - Who Owns the Tree RSC as a Protocol, Not an Architecture|TWIR item note]]
- [[../../raw/twir/280/2026-05-06-TWIR-280|TWIR #280]]
