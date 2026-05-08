---
type: twir-item
issue: 193
item: 3
item_type: item
date: 2024-07-24
source: https://thisweekinreact.com/articles/useSyncExternalStore-the-underrated-react-api
tags:
  - "ES"
  - "useSyncExternalStore"
status: auto
quality: keep
---

[[2024-07-24-TWIR-193|Index]]

# Item 3: my favorite underrated hook useSyncExternalStore

Source: [https://thisweekinreact.com/articles/useSyncExternalStore-the-underrated-react-api](https://thisweekinreact.com/articles/useSyncExternalStore-the-underrated-react-api)

Summary:
This article explains how useSyncExternalStore, introduced in React 18, can be used to efficiently subscribe to external data sources and avoid unnecessary re-renders. It highlights common pitfalls with over-returning data in hooks (e.g., React-Router’s useLocation) and demonstrates how custom selector hooks built on useSyncExternalStore can optimize component updates. Practical examples include tracking browser history and scroll position, showing how to implement fine-grained subscriptions for better performance.

Key takeaways:
- useSyncExternalStore enables efficient subscriptions to external stores, supporting concurrent rendering.
- Over-returning data in hooks can cause excessive re-renders; selectors can mitigate this.
- Custom hooks using useSyncExternalStore can target specific data changes, improving performance.
- Examples provided for React-Router and scroll position tracking.

Recommendation:
Read fully (for performance-focused developers and those building custom hooks)

Why it matters:
for performance-focused developers and those building custom hooks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
