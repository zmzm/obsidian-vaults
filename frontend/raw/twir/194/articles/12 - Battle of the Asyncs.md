---
type: twir-item
issue: 194
item: 12
item_type: item
date: 2024-07-31
source: https://www.brenelz.com/posts/battle-of-the-asyncs/
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-07-31-TWIR-194|Index]]

# Item 12: Battle of the Asyncs

Source: [https://www.brenelz.com/posts/battle-of-the-asyncs/](https://www.brenelz.com/posts/battle-of-the-asyncs/)

Summary:
This post compares React's use and Solid's createAsync primitives for handling async data in components, highlighting differences in re-execution, component structure, and server/client boundaries. It also touches on how React Server Components (RSC) affect async patterns.

Key takeaways:
- React's use may re-execute async functions on state changes, while Solid's createAsync avoids this.
- Solid treats async values as signals, simplifying component logic.
- RSC changes the pattern by separating server and client concerns, preventing redundant fetches.
- The comparison illuminates subtle differences in async handling between frameworks.

Recommendation:
Summary sufficient (unless you are evaluating async data patterns across frameworks)

Why it matters:
unless you are evaluating async data patterns across frameworks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
