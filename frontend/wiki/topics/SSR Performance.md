---
type: topic
status: active
updated: 2026-04-21
tags:
  - ssr
  - performance
  - rendering
---

# SSR Performance

SSR Performance is the topic hub for server-side rendering throughput, latency, and the framework-level design choices that affect rendering work on the server.

## Scope

- Throughput and latency tradeoffs in SSR pipelines.
- Server-only fast paths and SSR-specific optimizations.
- Framework constraints that increase or reduce server rendering cost.
- The relationship between rendering architecture and operational performance.

## Practical Significance

- This topic is useful for connecting framework architecture discussions to measurable production behavior.
- It provides a place to compare optimization patterns across frameworks instead of treating each performance story in isolation.

## Current Signals

- The raw layer already includes strong material on custom RSC frameworks and TanStack Start SSR optimization.
- Even with limited coverage, there is enough here to justify a durable topic page rather than leaving these ideas scattered.
- The newer raw layer also adds a more direct RSC performance comparison and stronger platform-level caching signals from Next.js itself.
- It now also includes lower-level stream-pipeline work inside Next.js and another framework-migration story where build and iteration speed were decisive.

## Related Pages

- [[React Rendering]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[../sources/TWIR 255|TWIR 255]]
- [[../sources/TWIR 276|TWIR 276]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../sources/TWIR 273|TWIR 273]]
- [[../case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]]
- [[../case-studies/Railway Off Next.js|Railway Off Next.js]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]]

## Open Questions

- Which SSR optimization patterns are broadly transferable across frameworks.
- Where the biggest performance gains come from architecture choices versus low-level hot-path work.
