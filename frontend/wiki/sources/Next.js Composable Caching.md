---
type: source
status: active
updated: 2026-04-30
tags:
  - nextjs
  - caching
  - app-router
---

# Next.js Composable Caching

This source captures the early `use cache` direction in Next.js: cacheability is expressed through compiler-visible function and component boundaries rather than only ad hoc runtime cache calls.

## Summary

- `use cache` is framed as a directive that lets Next.js derive cache keys from serializable inputs and captured dependencies.
- The model attempts to reduce manual cache-key bugs while still supporting tagging and invalidation.
- Non-serializable values are handled differently from ordinary cache-key inputs, making boundary design important.
- The source helps explain why App Router caching is a component-architecture question, not just a performance switch.

## Why This Source Matters

- It gives `Caching in App Router` an early first-party anchor for explicit cache design.
- It supports `Next.js` by showing how framework compiler behavior and runtime data access are converging.
- It helps connect later Next.js 16 and Partial Prerendering material back to the earlier composable-caching direction.

## Caveats

- Next.js caching behavior has evolved since this source, so later release pages should take precedence for exact API details.
- Treat this as architectural direction rather than final reference documentation.

## Related Pages

- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[Next.js 16]]
- [[Partial Prerendering Architecture]]
- [[TWIR 216]]

## Raw Sources

- [[../../raw/twir/216/articles/01 - Composable Caching with Next.js|Composable Caching with Next.js]]
- [[../../raw/twir/216/2025-01-08-TWIR-216|TWIR #216]]
