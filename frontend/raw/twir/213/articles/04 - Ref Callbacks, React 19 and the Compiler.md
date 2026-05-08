---
type: twir-item
issue: 213
item: 4
item_type: item
date: 2024-12-11
source: https://tkdodo.eu/blog/ref-callbacks-react-19-and-the-compiler
tags:
  - "React19"
  - "19"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-12-11-TWIR-213|Index]]

# Item 4: Ref Callbacks, React 19 and the Compiler

Source: [https://tkdodo.eu/blog/ref-callbacks-react-19-and-the-compiler](https://tkdodo.eu/blog/ref-callbacks-react-19-and-the-compiler)

Summary:
This post revisits the use of ref callbacks in React, correcting earlier misconceptions and updating for React 19 and the React Compiler. It clarifies when useCallback is (and isn't) necessary for refs, highlights new cleanup capabilities for ref callbacks in React 19, and discusses implications for future codebases using the compiler. The author provides practical advice for avoiding unnecessary useCallback and leveraging new ref features.

Key takeaways:
- useCallback for refs is often unnecessary; prefer stable functions outside components when possible.
- React 19 allows ref callbacks to return cleanup functions, similar to useEffect.
- Over-reliance on useCallback can complicate future migration to the React Compiler.
- Prefer storing primitives in state when using ref callbacks to avoid re-render loops.

Recommendation:
Read fully (read fully if you use custom refs or plan to adopt the compiler)

Why it matters:
read fully if you use custom refs or plan to adopt the compiler

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
