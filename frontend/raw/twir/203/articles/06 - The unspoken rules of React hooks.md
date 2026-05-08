---
type: twir-item
issue: 203
item: 6
item_type: item
date: 2024-10-01
source: https://macwright.com/2024/09/19/the-extra-rules-of-hooks
tags:
  - "TanStackQuery"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 6: The unspoken rules of React hooks

Source: [https://macwright.com/2024/09/19/the-extra-rules-of-hooks](https://macwright.com/2024/09/19/the-extra-rules-of-hooks)

Summary:
This article highlights lesser-known but important rules about React hook dependencies, especially for useEffect. While the dependency array should include all referenced variables, some values (like state setters, refs, and certain hook returns) are stable and can be omitted. The author notes that React’s documentation could better clarify which hook return values are stable, and that this ambiguity extends to third-party hooks.

Key takeaways:
- useEffect dependencies should include all referenced variables, except for stable values (setters, refs, etc.).
- React docs underemphasize which hook returns are stable; discovery is nontrivial.
- Including stable values in dependencies is safe, but unnecessary.
- Stability of third-party hook returns (e.g., Jotai, TanStack Query) is often unclear.

Recommendation:
Read fully (read fully if you want deeper insight or examples)

Why it matters:
read fully if you want deeper insight or examples

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
