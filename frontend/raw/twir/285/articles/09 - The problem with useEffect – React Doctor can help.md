---
type: twir-item
issue: 285
item: 9
item_type: item
date: 2026-06-10
source: https://www.react.doctor/blog/the-problem-with-useeffect
tags:
status: auto
quality: keep
---

[[2026-06-10-TWIR-285|Index]]

# Item 9: The problem with useEffect – React Doctor can help

Source: [https://www.react.doctor/blog/the-problem-with-useeffect](https://www.react.doctor/blog/the-problem-with-useeffect)

Summary:
The article explains common pitfalls with useEffect, especially infinite loops caused by unstable dependencies or missing dependency arrays. It illustrates how React compares dependencies by reference, leading to subtle bugs with objects, arrays, or functions. Solutions include stabilizing dependencies with useMemo/useCallback and using ESLint rules or tools like React Doctor to catch issues before they ship.

Key takeaways:
- useEffect runs after every render unless dependencies are properly specified.
- Unstable dependencies (new object/function references) can cause disguised infinite loops.
- useMemo/useCallback can stabilize dependencies; primitives are compared by value.
- Tools like react-hooks/exhaustive-deps and React Doctor help catch these bugs early.

Recommendation:
Read fully (read fully if troubleshooting useEffect bugs or interested in static analysis tools)

Why it matters:
read fully if troubleshooting useEffect bugs or interested in static analysis tools

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
