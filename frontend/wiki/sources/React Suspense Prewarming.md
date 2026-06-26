---
type: source
status: active
updated: 2026-06-26
tags:
  - react
  - suspense
  - rendering
  - source
---

# React Suspense Prewarming

This source page normalizes the repeated 2024 archive thread around React 19 Suspense sibling prerendering, non-blocking prerender work, and prewarming.

## Summary

- Early React 19 RC behavior could stop prerendering siblings after one child suspended, risking waterfalls in colocated data-fetching or lazy-loading patterns.
- Follow-up React core work explored and re-landed non-blocking prerendering so suspended work would not block independent siblings.
- Later sibling prewarming material reframed the fix as a way to preserve parallel discovery of async work while still respecting Suspense boundaries.

## Why This Source Matters

- It explains why Suspense behavior is part of performance architecture, not only loading-state UI.
- It supports the `React Rendering` hub with a concrete example of scheduler semantics changing application-level data waterfalls.
- It gives historical context for newer async React APIs and why teams should design Suspense boundaries deliberately.

## Caveats

- This is a historical normalization page. Current React behavior should be checked against current release notes before implementation.
- The source base here is mainly RC-era discussion and PR notes, not a single stable API document.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React use()|React use()]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[TWIR 190]]
- [[TWIR 196]]
- [[TWIR 205]]
- [[TWIR 209]]
- [[TWIR 210]]

## Raw Sources

- [[../../raw/twir/190/articles/01 - React 19 and Suspense - A Drama in 3 Acts|React 19 and Suspense - A Drama in 3 Acts]]
- [[../../raw/twir/190/articles/02 - How React 19 (Almost) Made the Internet Slower|How React 19 Almost Made the Internet Slower]]
- [[../../raw/twir/196/articles/02 - React 19 - Disabling prerendering siblings of suspended components breaking common pattern|React 19 sibling prerendering issue]]
- [[../../raw/twir/205/articles/02 - React Core PR - Re-land non-blocking prerendering|React core non-blocking prerendering]]
- [[../../raw/twir/209/articles/02 - React PR - Make prerendering always non-blocking|React prerendering always non-blocking]]
- [[../../raw/twir/210/articles/01 - React 19 RC1 - Siblings pre-warming|React 19 RC1 siblings pre-warming]]
