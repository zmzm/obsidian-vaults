---
type: case-study
status: active
updated: 2026-06-26
tags:
  - nextjs
  - app-router
  - performance
  - server-components
---

# Next.js App Router Slow Responses

This case study preserves Subito's App Router migration as a counterweight to migration-away-from-Next.js stories: App Router can be a performance win when the workload fits server-first rendering and streaming.

## Context

- The target was a high-traffic ad detail page with slow-response problems under the Pages Router.
- The team migrated incrementally, reusing client components while introducing Server Components for data fetching and streaming.
- The migration had to preserve SEO semantics such as HTTP 410 responses for expired ads.

## What Helped

- Incremental migration avoided a freeze on product work and reduced duplicated implementation.
- React `cache()` and Server Components improved data-fetching deduplication.
- Streaming required operational changes: Nginx and Akamai buffering had to be configured so Suspense skeletons could reach users.
- Express middleware handled status-code behavior that did not map cleanly to the App Router path.

## Why It Matters

- It makes the Next.js branch more balanced: some teams leave App Router, but some server-heavy pages benefit from it.
- It supports the SSR performance branch with production evidence around streaming, cache deduplication, and CDN behavior.
- It reinforces that App Router performance work is partly application architecture and partly host/runtime configuration.

## Main Lesson

- App Router works best when teams can align data fetching, streaming, cache behavior, and edge/proxy configuration around a server-first page.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]
- [[../topics/SSR Performance|SSR Performance]]
- [[Next.js App Router Exit]]
- [[Next.js Host Runtime Friction]]
- [[../sources/TWIR 287|TWIR 287]]

## Raw Source

- [[../../raw/twir/287/articles/06 - How We Cut Slow Responses by 80% Migrating to Next.js App Router|TWIR item note]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
