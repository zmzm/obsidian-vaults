---
type: twir-item
issue: 191
item: 6
item_type: item
date: 2024-06-26
source: https://bobaekang.com/blog/component-colocation-composition/
tags:
  - "ReactQuery"
  - "Suspense"
status: auto
quality: keep
---

[[2024-06-26-TWIR-191|Index]]

# Item 6: Component, colocation, composition: A note on the state of React

Source: [https://bobaekang.com/blog/component-colocation-composition/](https://bobaekang.com/blog/component-colocation-composition/)

Summary:
This blog post reflects on recent debates in the React community around component colocation, state management, and data fetching patterns, especially in light of changes to Suspense behavior in React 19 RC. It discusses the tension between colocating state/data in components versus managing shared state outside the component tree, and how this impacts performance and developer experience.

Key takeaways:
- React's component model is successful, but colocating all state/data can lead to performance issues in large apps.
- Fetch-on-render patterns can cause network waterfalls; prefetching outside components is recommended.
- State often needs to be managed outside the component tree (e.g., via context, external stores) for scalability.
- React's direction and ecosystem solutions (Redux, React Query, etc.) reflect ongoing trade-offs between simplicity and performance.

Recommendation:
Read fully (for insights into React architecture, state, and data-fetching best practices)

Why it matters:
for insights into React architecture, state, and data-fetching best practices

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
