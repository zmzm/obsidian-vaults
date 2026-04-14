---
type: source
status: active
updated: 2026-04-14
tags:
  - server-components
  - performance
  - source
---

# RSC Performance Tradeoffs

This source compares CSR, SSR, and React Server Components with a more practical and metrics-driven framing than most conceptual RSC discussions.

## Summary

- The article compares rendering strategies under real conditions rather than relying on generic claims.
- It highlights how RSC can reduce client JavaScript and shift data work to the server.
- It also makes clear that the performance story depends on what metric is being optimized and how the app is structured.

## Why This Source Matters

- It gives both `Server Components` and `SSR Performance` a more concrete performance baseline.
- It is especially useful for pushing back against simplistic “RSC is always faster” narratives.

## Caveats

- This is still a secondary analysis rather than framework-internal documentation.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../patterns/Caching in App Router|Caching in App Router]]

## Raw Sources

- [[../../raw/twir/255/articles/06 - React Server Components Do They Really Improve Performance|TWIR item note]]
- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
