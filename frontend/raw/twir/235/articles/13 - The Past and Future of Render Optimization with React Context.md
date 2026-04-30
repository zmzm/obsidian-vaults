---
type: twir-item
issue: 235
item: 15
item_type: item
date: 2025-05-21
source: https://newsletter.daishikato.com/p/the-past-and-future-of-render-optimization-with-react-context
tags:
  - "Compiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-05-21-TWIR-235|Index]]

# Item 15: The Past and Future of Render Optimization with React Context

Source: [https://newsletter.daishikato.com/p/the-past-and-future-of-render-optimization-with-react-context](https://newsletter.daishikato.com/p/the-past-and-future-of-render-optimization-with-react-context)

Summary:
Daishi Kato reviews the evolution of render optimization in React context, from useContextSelector to useSyncExternalStore, and discusses the upcoming use(store) API. The article explores selector-based patterns, external store syncing, and the trade-offs between different approaches, with speculation on how React Compiler may influence future best practices.

Key takeaways:
- Provider nesting and context updates can cause excessive rerenders ("Provider hell").
- useContextSelector and useSyncExternalStore offer different optimization strategies.
- React is moving toward a use(store) API for concurrent-compatible state subscriptions.
- Selector-based APIs may become less central if use(store) is widely adopted.

Recommendation:
Summary sufficient (read full post for historical context and code samples)

Why it matters:
read full post for historical context and code samples

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
