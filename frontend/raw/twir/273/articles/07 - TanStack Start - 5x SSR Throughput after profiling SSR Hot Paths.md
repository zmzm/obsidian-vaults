---
type: twir-item
issue: 273
item: 7
item_type: item
date: 2026-03-18
source: https://tanstack.com/blog/tanstack-start-5x-ssr-throughput
tags:
  - "TanStack"
  - "SSR"
  - "5x"
  - "Ease"
status: auto
---

[[2026-03-18-TWIR-273|Index]]

# Item 7: TanStack Start - 5x SSR Throughput after profiling SSR Hot Paths

Source: [https://tanstack.com/blog/tanstack-start-5x-ssr-throughput](https://tanstack.com/blog/tanstack-start-5x-ssr-throughput)

Summary:
TanStack Start achieved a 5.5x increase in SSR throughput by systematically profiling and optimizing server hot paths. Improvements included avoiding unnecessary URL parsing, skipping reactivity during SSR, and introducing server-only fast paths. The article details methodology, code changes, and transferable optimization patterns, validated by robust benchmarking.

Key takeaways:
- SSR throughput improved from 427 req/s to 2357 req/s; p99 latency dropped 7x.
- Key optimizations: minimize URL parsing, bypass client reactivity on server, use build-time flags for server-only code.
- Profiling and benchmarking under real load were critical to identifying bottlenecks.
- Patterns and techniques are transferable to other SSR frameworks.

Recommendation: Read fully (for SSR performance tuning and framework maintainers)
