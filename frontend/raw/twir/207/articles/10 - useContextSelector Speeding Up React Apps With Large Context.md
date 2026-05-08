---
type: twir-item
issue: 207
item: 10
item_type: item
date: 2024-10-30
source: https://marmelab.com/blog/2024/10/16/usecontextselector-a-faster-usecontext-for-react.html
tags:
  - "useContextSelector"
status: auto
quality: keep
---

[[2024-10-30-TWIR-207|Index]]

# Item 10: useContextSelector: Speeding Up React Apps With Large Context

Source: [https://marmelab.com/blog/2024/10/16/usecontextselector-a-faster-usecontext-for-react.html](https://marmelab.com/blog/2024/10/16/usecontextselector-a-faster-usecontext-for-react.html)

Summary:
The article addresses performance issues with large React contexts, where any change causes all consumers to rerender. It reviews common workarounds (splitting components, multiple contexts) and introduces the use-context-selector library, which allows components to subscribe only to specific context slices. This targeted subscription reduces unnecessary rerenders and improves app performance.

Key takeaways:
- Large contexts cause widespread rerenders; splitting or memoizing components can help but is cumbersome.
- use-context-selector enables fine-grained subscriptions to context values.
- This approach is more scalable and maintainable for large apps.
- React 19 may address some of these issues, but use-context-selector is valuable now.

Recommendation:
Read fully (read fully if you manage large contexts or want performance gains)

Why it matters:
read fully if you manage large contexts or want performance gains

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
