---
type: twir-item
issue: 247
item: 2
item_type: item
date: 2025-08-27
source: https://github.com/reactjs/rfcs/pull/119#issuecomment-3214859601
tags:
  - "RFC"
  - "ConcurrentReact"
status: auto
quality: keep
---

[[2025-08-27-TWIR-247|Index]]

# Item 2: React Context Selectors RFC update

Source: [https://github.com/reactjs/rfcs/pull/119#issuecomment-3214859601](https://github.com/reactjs/rfcs/pull/119#issuecomment-3214859601)

Summary:
The Context Selectors RFC proposes a new hook, useContextSelector, allowing components to subscribe to specific slices of context, reducing unnecessary re-renders and improving performance. The discussion includes alternative APIs (like context.slice), userland implementations, and challenges with dynamic selectors and context propagation. The RFC aims to simplify external state subscriptions and make context usage more ergonomic and performant.

Key takeaways:
- useContextSelector would enable components to only re-render when the selected context value changes.
- Reduces complexity and code size in libraries, and improves compatibility with Concurrent React.
- Alternative APIs (context.slice) and userland implementations exist, but have limitations.
- The RFC focuses on hooks, but similar ideas could be extended to Consumer/contextType.

Recommendation:
Summary sufficient (read the RFC for implementation details or if building advanced context abstractions)

Why it matters:
read the RFC for implementation details or if building advanced context abstractions

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
