---
type: topic
status: active
updated: 2026-06-26
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
- It now also includes lower-level stream-pipeline work inside Next.js, React-level out-of-order streaming mechanics, and another framework-migration story where build and iteration speed were decisive.
- TWIR #287 adds a counterbalancing App Router case where server-first data fetching, React cache deduplication, and streaming configuration reduced slow responses on a high-traffic page.
- TWIR #194, #198, #202, #204, #206, #212, and #213 add older SSR/PPR evidence around Partial Prerendering, SSR performance comparisons, Cloudflare Workers PPR, serverless concurrency, Next.js 15 caching, Deno deployment, and SSR cost framing.
- Astro contributes the static-generation and islands side of the branch, especially where server work is shifted toward build-time, content pipelines, route caching, or selective hydration.

## Related Pages

- [[React Rendering]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/Astro|Astro]]
- [[../tools/Next.js|Next.js]]
- [[../tools/TanStack Start|TanStack Start]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[../sources/TWIR 255|TWIR 255]]
- [[../sources/TWIR 276|TWIR 276]]
- [[../sources/TWIR 194|TWIR 194]]
- [[../sources/TWIR 198|TWIR 198]]
- [[../sources/TWIR 202|TWIR 202]]
- [[../sources/TWIR 204|TWIR 204]]
- [[../sources/TWIR 206|TWIR 206]]
- [[../sources/TWIR 212|TWIR 212]]
- [[../sources/TWIR 213|TWIR 213]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../sources/TWIR 273|TWIR 273]]
- [[../case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]]
- [[../case-studies/Next.js App Router Slow Responses|Next.js App Router Slow Responses]]
- [[../case-studies/Railway Off Next.js|Railway Off Next.js]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
- [[../../raw/twir/194/2024-07-31-TWIR-194|TWIR #194]]
- [[../../raw/twir/198/2024-08-28-TWIR-198|TWIR #198]]
- [[../../raw/twir/202/2024-09-25-TWIR-202|TWIR #202]]
- [[../../raw/twir/204/2024-10-09-TWIR-204|TWIR #204]]
- [[../../raw/twir/206/2024-10-23-TWIR-206|TWIR #206]]
- [[../../raw/twir/212/2024-12-04-TWIR-212|TWIR #212]]
- [[../../raw/twir/213/2024-12-11-TWIR-213|TWIR #213]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]]
- [[../case-studies/Next.js App Router Slow Responses|Next.js App Router Slow Responses]]

## Open Questions

- Which SSR optimization patterns are broadly transferable across frameworks.
- Where the biggest performance gains come from architecture choices versus low-level hot-path work.
