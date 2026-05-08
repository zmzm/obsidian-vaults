---
type: twir-item
issue: 191
item: 9
item_type: item
date: 2024-06-26
source: https://dev.to/alexandereardon/wait-for-pending-a-not-great-alternative-suspense-algorithm-1gdl
tags:
  - "Suspense"
status: auto
quality: keep
---

[[2024-06-26-TWIR-191|Index]]

# Item 9: Wait for pending: A (not great) alternative Suspense algorithm

Source: [https://dev.to/alexandereardon/wait-for-pending-a-not-great-alternative-suspense-algorithm-1gdl](https://dev.to/alexandereardon/wait-for-pending-a-not-great-alternative-suspense-algorithm-1gdl)

Summary:
This post explores an alternative algorithm for React's <Suspense> component, called "wait for pending," which waits for all pending promises in a boundary before re-rendering. It compares this approach to the algorithms in React 18 and 19, highlighting trade-offs in parallelization, re-render minimization, and async tree depth.

Key takeaways:
- "Wait for pending" reduces redundant renders but can delay nested async component rendering.
- React 18's approach favors parallelization but causes more re-renders; React 19's is more sequential.
- The proposed algorithm is more efficient for flat async trees, but less so for deeply nested async components.
- Useful for understanding Suspense internals and trade-offs in async rendering.

Recommendation:
Read fully (read fully if you are working on advanced Suspense patterns)

Why it matters:
read fully if you are working on advanced Suspense patterns

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
