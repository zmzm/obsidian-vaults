---
type: twir-item
issue: 245
item: 6
item_type: item
date: 2025-07-30
source: https://tkdodo.eu/blog/the-useless-use-callback
tags:
  - "memo"
  - "Perf"
status: auto
quality: keep
---

[[2025-07-30-TWIR-245|Index]]

# Item 6: The Useless useCallback

Source: [https://tkdodo.eu/blog/the-useless-use-callback](https://tkdodo.eu/blog/the-useless-use-callback)

Summary:
This article critiques the overuse of useCallback and useMemo in React, especially when referential stability is unnecessary. It explains that memoizing functions or values is only beneficial when passed to memoized components or as dependencies in effects, and often does not yield performance gains otherwise. The author provides examples where useCallback is pointless and discusses common pitfalls, such as using props as dependencies or enforcing unnecessary memoization policies.

Key takeaways:
- Memoization (useCallback/useMemo) is only useful for referential stability when required by React.memo or effect dependencies.
- Memoizing props for non-memoized components or DOM elements provides no performance benefit.
- Passing non-primitive props as dependencies can lead to unnecessary re-renders or effects.
- Over-memoization adds complexity without real-world gains; use it judiciously.

Recommendation:
Read fully (especially for teams standardizing on memoization patterns or reviewing performance practices)

Why it matters:
especially for teams standardizing on memoization patterns or reviewing performance practices

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
