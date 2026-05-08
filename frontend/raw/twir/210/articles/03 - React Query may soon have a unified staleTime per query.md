---
type: twir-item
issue: 210
item: 3
item_type: item
date: 2024-11-20
source: https://github.com/TanStack/query/pull/8313
tags:
status: auto
quality: keep
---

[[2024-11-20-TWIR-210|Index]]

# Item 3: React Query may soon have a unified staleTime per query

Source: [https://github.com/TanStack/query/pull/8313](https://github.com/TanStack/query/pull/8313)

Summary:
A proposed change in React Query moves staleTime from the observer level to the query level, enforcing a single staleTime per query key. This reduces complexity and potential inconsistencies, as previously multiple observers could have different staleTimes, leading to performance issues and inconsistent UI states. The refactor also changes how staleTime: 0 is handled and ensures disabled observers reflect data staleness. Some breaking changes are expected, especially for apps relying on per-observer staleTime.

Key takeaways:
- staleTime will be unified per query, not per observer, simplifying state management.
- Reduces timer overhead and prevents inconsistent stale states across observers.
- staleTime: 0 now marks data as stale immediately, without timers.
- May break apps using different staleTimes for the same query in multiple places.

Recommendation:
Read fully (if using React Query and customizing staleTime or observer behavior)

Why it matters:
if using React Query and customizing staleTime or observer behavior

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
