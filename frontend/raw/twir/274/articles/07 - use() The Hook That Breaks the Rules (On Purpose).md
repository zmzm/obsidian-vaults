---
type: twir-item
issue: 274
item: 7
item_type: item
date: 2026-03-25
source: https://saschb2b.com/blog/use-hook-react
tags:
  - "useEffect"
status: auto
---

[[2026-03-25-TWIR-274|Index]]

# Item 7: use(): The Hook That Breaks the Rules (On Purpose)

Source: [https://saschb2b.com/blog/use-hook-react](https://saschb2b.com/blog/use-hook-react)

Summary:
React 19’s `use()` hook enables reading promises and context at render time, integrating directly with Suspense and eliminating common useEffect anti-patterns for data fetching. It simplifies components by removing boilerplate state and effect logic, but requires careful boundary placement and understanding of caching behavior.

Key takeaways:
- `use()` can be called inside conditionals/loops and works with both promises and context.
- Suspense boundaries are required to handle loading states; Error Boundaries handle errors.
- Components using `use()` are cleaner and focus on the "happy path" UI.
- Caching and separation of concerns are important to avoid unnecessary re-fetches or stale data.

Recommendation: Read fully
