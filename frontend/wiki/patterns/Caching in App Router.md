---
type: pattern
status: active
updated: 2026-04-21
tags:
  - nextjs
  - caching
  - app-router
  - server-components
---

# Caching in App Router

Caching in App Router is the pattern page for how cacheability, request-time APIs, rendering boundaries, and framework conventions interact in Next.js App Router applications.

## Key Ideas

- App Router caching is not just a performance detail; it shapes component boundaries and data access patterns.
- `use cache` works best when render paths avoid request-time dependencies.
- Features such as i18n, error handling, and dynamic request context can create friction with cacheable rendering paths.

## Practical Significance

- This pattern helps explain why some App Router designs compose cleanly while others fight the framework.
- It is a useful bridge between abstract Server Components discussion and concrete Next.js implementation tradeoffs.

## Current Signals

- The current source set already shows one clear cache-related friction point through `next-intl`.
- It also ties naturally into App Router ergonomics and framework-aware APIs.
- The newer raw layer adds a more operational view of caching and SSR tradeoffs in larger Next.js deployments.
- It now also includes a strong release anchor for explicit cache design and a stronger source on Partial Prerendering mechanics.
- Newer issue coverage also adds a concrete precompute workaround for separating request context from cacheable render paths.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[../concepts/React use()|React use()]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../sources/TWIR 255|TWIR 255]]
- [[../sources/TWIR 257|TWIR 257]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Partial Prerendering Architecture|Partial Prerendering Architecture]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../sources/The Precompute Pattern|The Precompute Pattern]]
- [[../sources/Next.js at Enterprise Level|Next.js at Enterprise Level]]
- [[../sources/Next.js 16.2|Next.js 16.2]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../sources/TWIR 276|TWIR 276]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/257/2025-11-05-TWIR-257|TWIR #257]]
- [[../../raw/twir/268/2026-02-11-TWIR-268|TWIR #268]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Partial Prerendering Architecture|Partial Prerendering Architecture]]
- [[../sources/Next.js at Enterprise Level|Next.js at Enterprise Level]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../sources/The Precompute Pattern|The Precompute Pattern]]
- [[../sources/Next.js 16.2|Next.js 16.2]]

## Open Questions

- Which cache-related constraints are fundamental to the model and which are likely to soften as the framework evolves.
- How best to model the boundary between request-aware logic and cacheable rendering units.
