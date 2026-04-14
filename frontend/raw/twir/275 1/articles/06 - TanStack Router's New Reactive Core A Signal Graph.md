---
type: twir-item
issue: 275
item: 6
item_type: item
date: 2026-04-01
source: https://tanstack.com/blog/tanstack-router-signal-graph
tags:
  - "TanStack"
  - "TanStackRouter"
  - "Signals"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 6: TanStack Router's New Reactive Core: A Signal Graph

Source: [https://tanstack.com/blog/tanstack-router-signal-graph](https://tanstack.com/blog/tanstack-router-signal-graph)

Summary:
TanStack Router has refactored its internal state management to use a graph of smaller reactive stores instead of a single broad state object. This change enables more granular updates, fewer unnecessary rerenders, and faster client-side navigation. The new architecture is adapter-driven, letting each platform (React, Solid, Vue) implement its own store model, while maintaining a consistent API.

Key takeaways:
- Router state is now composed of focused stores (location, matches, etc.), improving update efficiency.
- router.state is now derived from these stores, not the source of truth.
- Enables more targeted subscriptions and reduces work during navigation.
- Adapter pattern allows platform-specific optimizations (e.g., Solid uses native signals).

Recommendation: Summary sufficient
