---
type: concept
status: active
updated: 2026-04-30
tags:
  - react
  - use-hook
  - suspense
  - async-rendering
---

# React use()

`use()` is a React concept centered on reading promises and context during render, making async coordination a first-class part of the rendering model rather than something orchestrated primarily through effects.

## Key Ideas

- `use()` allows render-time reads of async values and integrates directly with Suspense and Error Boundaries.
- It shifts many loading and data-fetching patterns away from effect-driven orchestration.
- The feature matters not only as a new hook, but as a signal of how React wants async work to compose with rendering.

## Practical Significance

- This concept helps explain why some traditional `useEffect` data-fetching patterns now feel like legacy workarounds.
- It belongs between high-level rendering discussions and framework-specific Server Components patterns.

## Current Signals

- The current source set already contains a clear developer-facing explanation of `use()`.
- It also connects naturally to `React Rendering`, `Server Components`, and caching concerns.
- The older archive now also adds `cacheSignal()`, which makes the cache-side lifecycle around async reads more explicit instead of treating cancellation as an afterthought.
- TWIR #215 adds a simple bridge from legacy thrown promises to `use()`, while the forms material shows the same React 19 direction toward render/action-aware async primitives.

## Related Pages

- [[Server Components]]
- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../tools/Next.js|Next.js]]
- [[../sources/React cacheSignal|React cacheSignal]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/Progressive React Forms|Progressive React Forms]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../sources/TWIR 215|TWIR 215]]

## Sources

- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/215/articles/05 - Replacing Legacy throw in React 19 with Suspense and use|Replacing Legacy throw in React 19 with Suspense and use]]
- [[../../raw/twir/245/2025-07-30-TWIR-245|TWIR #245]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/Progressive React Forms|Progressive React Forms]]
- [[../sources/React cacheSignal|React cacheSignal]]

## Open Questions

- Which `use()` patterns are genuinely durable versus still framework- or cache-model-dependent.
- Where `use()` should remain a low-level primitive versus becoming the default data access style.
