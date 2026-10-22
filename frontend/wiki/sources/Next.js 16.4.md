---
type: source
status: active
updated: 2026-10-22
tags: [nextjs, caching, navigation, source]
---

# Next.js 16.4

The captured Next.js 16.4 release article frames Cache Components and Partial Prefetching as the recommended cache model and gives explicit controls for static guarantees.

## Summary

- Cache boundaries combine reusable UI with request-time rendering rather than requiring an entire page to share one rendering mode.
- The captured model uses cacheComponents and partialPrefetching together; configuration and defaults are release-specific.
- ensureStatic distinguishes shell, prefetch, and full-navigation guarantees. Static guarantees concern when work may happen, not only where data is stored.
- The related parameter-matching API is an unstable PR, and new Link prefetch stage options are another PR; neither should be presented as stable merely because the release is stable.

## Why This Source Matters

- Connects the existing App Router cache pattern to concrete release and testable navigation evidence.
- Provides a stronger extracted anchor than earlier summary-only 16.3 notes while retaining their historical context.

## Related Pages

- [[Next.js 16.3|Next.js 16.3]]
- [[../tools/Next.js|Next.js]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../case-studies/v0 Partial Prefetching|v0 Partial Prefetching]]

## Sources

- [[../../raw/twir/300/articles/01 - Next.js 16.4|01 - Next.js 16.4]]
- [[../../raw/twir/300/articles/04 - Next.js PR - unstable_paramMatching API|04 - Next.js PR - unstable_paramMatching API]] — unstable proposal.
- [[../../raw/twir/302/articles/04 - Next.js PR - Link prefetch= navigation|04 - Next.js PR - Link prefetch= navigation]] — PR-level proposal.
- [[../../raw/twir/302/articles/06 - Improving navigation experience in v0 with Next.js 16.4|06 - Improving navigation experience in v0 with Next.js 16.4]]

## Open Questions

- Which data must remain request-time even when the shell is static?
- How do cache invalidation and personalization affect useful prefetch coverage?
