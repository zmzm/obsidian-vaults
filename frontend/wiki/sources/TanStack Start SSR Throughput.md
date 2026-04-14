---
type: source
status: active
updated: 2026-04-14
tags:
  - tanstack-start
  - ssr
  - performance
  - source
---

# TanStack Start SSR Throughput

This source documents a strong SSR optimization case study centered on profiling, hot-path reduction, and server-only fast paths in TanStack Start.

## Summary

- The reported SSR throughput improvement is substantial, alongside a large p99 latency reduction.
- The optimizations focus on removing unnecessary work in the SSR path, especially URL parsing and client-oriented reactivity.
- The source emphasizes profiling and benchmarking discipline rather than anecdotal tuning.

## Why This Source Matters

- It gives the vault a concrete SSR performance case study with transferable optimization ideas.
- It strengthens the distinction between client-reactivity concerns and server-rendering concerns.

## Caveats

- The performance claims come from a framework-specific case study and should not be generalized without care.

## Related Pages

- [[../topics/SSR Performance|SSR Performance]]
- [[../topics/React Rendering|React Rendering]]
- [[../concepts/Server Components|Server Components]]

## Raw Sources

- [[../../raw/twir/273/articles/07 - TanStack Start - 5x SSR Throughput after profiling SSR Hot Paths|TWIR item note]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
