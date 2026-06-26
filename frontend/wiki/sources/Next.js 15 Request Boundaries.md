---
type: source
status: active
updated: 2026-06-26
tags:
  - nextjs
  - app-router
  - request-apis
  - source
---

# Next.js 15 Request Boundaries

This source page normalizes the 2024 archive thread around Next.js 15 async request APIs, cache behavior, server functions, and deployment/request-boundary changes.

## Summary

- Next.js 15 moved request-bound APIs such as `cookies`, `headers`, `draftMode`, `params`, and `searchParams` toward async access so rendering could distinguish static and dynamic work more explicitly.
- The same archive period introduced or discussed `connection()`, segment cache work, cache invalidation naming, server-action/function security, and request-interceptor experiments.
- These changes make App Router architecture depend more visibly on request boundaries, cacheability, and runtime placement.

## Why This Source Matters

- It gives the `Next.js` hub an older release-era anchor for the platform shift later pages assume.
- It supports `Caching in App Router`, `Next.js Portability Boundaries`, and SSR-performance pages by tying cache behavior to request API shape.
- It helps explain why framework conventions became more important as React server features moved into production frameworks.

## Caveats

- API names and defaults evolved after the canary/RC period. Use newer Next.js docs for implementation.
- This page is best used as architecture history and source routing, not direct upgrade guidance.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[TWIR 202]]
- [[TWIR 203]]
- [[TWIR 204]]
- [[TWIR 205]]
- [[TWIR 206]]

## Raw Sources

- [[../../raw/twir/202/articles/03 - Next.js PR - Update Dynamic APIs to be async|Next.js dynamic APIs become async]]
- [[../../raw/twir/203/articles/02 - Next.js PR - Update Dynamic APIs to be async|Next.js dynamic APIs follow-up]]
- [[../../raw/twir/203/articles/03 - Next.js PR - Add connection() as a new dynamic API|Next.js connection API]]
- [[../../raw/twir/204/articles/04 - Next.js Guide - Fixing breaking changes after v15.0.0-canary.171|Next.js 15 canary breaking changes]]
- [[../../raw/twir/205/articles/01 - Next.js 15 RC 2|Next.js 15 RC 2]]
- [[../../raw/twir/206/articles/01 - Next.js 15|Next.js 15]]
