---
type: source
status: active
updated: 2026-04-21
tags:
  - nextjs
  - caching
  - app-router
  - source
---

# The Precompute Pattern

This source describes a practical Next.js pattern for preserving cacheable rendering by resolving request-specific data before the page tree and encoding it into the URL.

## Summary

- Request-aware context such as auth, locale, or feature flags can be resolved in middleware and rewritten into a hidden URL segment.
- Pages then read from params instead of dynamic APIs like `cookies()` or `headers()`, which keeps them statically renderable.
- The pattern matters less after newer cache-oriented Next.js features, but it still helps in high-cardinality or variant-heavy applications.

## Why This Source Matters

- It sharpens the `Caching in App Router` page with a concrete workaround pattern instead of only high-level cache semantics.
- It is useful as a design technique for teams trying to separate request context from cacheable render paths.
- It also clarifies that some App Router patterns are really about controlling where dynamic inputs enter the tree.

## Caveats

- This is partly a historical workaround and should not be mistaken for the default recommendation in every new Next.js app.
- The approach adds routing and prop-shape complexity, so it is most useful where variant cardinality or static-generation value is unusually high.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[TWIR 276]]

## Raw Sources

- [[../../raw/twir/276/articles/02 - The Precompute Pattern Encoding Dynamic Data into URLs in Next.js|TWIR item note]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
