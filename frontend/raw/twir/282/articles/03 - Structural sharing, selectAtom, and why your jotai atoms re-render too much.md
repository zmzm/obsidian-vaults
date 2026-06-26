---
type: twir-item
issue: 282
item: 3
item_type: item
date: 2026-05-20
source: https://www.peterp.me/articles/jotai-structural-sharing-vs-selectatom/
tags:
  - "Jotai"
  - "TanStack"
status: auto
quality: keep
---

[[2026-05-20-TWIR-282|Index]]

# Item 3: Structural sharing, selectAtom, and why your jotai atoms re-render too much

Source: [https://www.peterp.me/articles/jotai-structural-sharing-vs-selectatom/](https://www.peterp.me/articles/jotai-structural-sharing-vs-selectatom/)

Summary:
The post analyzes excessive re-renders in jotai state management, particularly when using jotai-tanstack-query, and explains how jotai’s reliance on Object.is for atom value comparison can cause unnecessary updates. It discusses when to use selectAtom for deduplication, but advocates for decomposing state into primitive atoms whenever possible. For complex cases, structural sharing (as in React Query) is recommended to preserve references and minimize re-renders.

Key takeaways:
- Jotai triggers re-renders when derived atoms return new object references, even if values are unchanged.
- selectAtom can deduplicate updates but is often overused; splitting state into primitives is usually better.
- Structural sharing (replaceEqualDeep) upstream is the preferred solution for complex state shapes.
- Practical code examples and guidelines help determine when to use selectAtom or structural sharing.

Recommendation:
Summary sufficient (read full article for deep dives or if you maintain jotai-heavy codebases)

Why it matters:
read full article for deep dives or if you maintain jotai-heavy codebases

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
