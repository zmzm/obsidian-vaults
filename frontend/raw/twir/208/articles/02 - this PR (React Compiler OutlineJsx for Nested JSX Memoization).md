---
type: twir-item
issue: 208
item: 2
item_type: item
date: 2024-11-06
source: https://github.com/facebook/react/pull/30956
tags:
  - "Compiler"
  - "PR"
  - "OutlineJsx"
  - "JSX"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-11-06-TWIR-208|Index]]

# Item 2: this PR (React Compiler: OutlineJsx for Nested JSX Memoization)

Source: [https://github.com/facebook/react/pull/30956](https://github.com/facebook/react/pull/30956)

Summary:
This PR introduces a new compiler pass, OutlineJsx, to automatically extract nested JSX inside callbacks into separate components, enabling fine-grained memoization and reducing unnecessary re-renders. The change improves rendering performance, especially for lists, by ensuring only updated items are re-rendered. The discussion covers implementation details, future extension possibilities (like outlining JSX in loops), and technical trade-offs in the compiler's internal representation.

Key takeaways:
- OutlineJsx extracts nested JSX in callbacks, allowing the compiler to memoize them as separate components.
- This reduces over-rendering, particularly in list scenarios, by re-rendering only changed elements.
- The approach currently targets callbacks but could be expanded to other patterns (e.g., loops).
- Implementation involves new HIR nodes and careful analysis to avoid outlining mutating statements.

Recommendation:
Read fully (for those interested in React Compiler internals and optimization strategies)

Why it matters:
for those interested in React Compiler internals and optimization strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
