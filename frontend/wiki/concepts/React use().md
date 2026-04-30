---
type: concept
status: active
updated: 2026-04-21
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

## Related Pages

- [[Server Components]]
- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../tools/Next.js|Next.js]]
- [[../sources/React cacheSignal|React cacheSignal]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/TWIR 274|TWIR 274]]

## Sources

- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/245/2025-07-30-TWIR-245|TWIR #245]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/React cacheSignal|React cacheSignal]]

## Open Questions

- Which `use()` patterns are genuinely durable versus still framework- or cache-model-dependent.
- Where `use()` should remain a low-level primitive versus becoming the default data access style.
