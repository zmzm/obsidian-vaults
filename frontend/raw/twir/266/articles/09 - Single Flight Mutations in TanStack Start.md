---
type: twir-item
issue: 266
item: 9
item_type: item
date: 2026-01-28
source: https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/
tags:
  - "TanStack"
  - "TanStackQuery"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 9: Single Flight Mutations in TanStack Start

Source: [https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/](https://frontendmasters.com/blog/single-flight-mutations-in-tanstack-start-part-1/)

Summary:
This blog post introduces the concept of "single flight mutations"—performing a data mutation and updating the UI with a single network round trip—using TanStack Query, Router, and Start. The author explains the motivation (reducing network latency and redundant fetches), shows how to structure queries and server functions, and demonstrates a simple implementation that refetches and returns updated data in one server response. Part 2 promises deeper middleware integration and advanced patterns.

Key takeaways:
- "Single flight mutation" means updating data and UI with one network request/response.
- TanStack Query and Start can structure queries and server functions for efficient updates.
- Example shows editing data, refetching relevant queries on the server, and returning all updated data at once.
- Reduces redundant network requests and improves perceived performance.

Recommendation: Read fully (read fully if you use TanStack Start or want to optimize mutation flows)

Related notes: [[TanStack Query]]
