---
type: twir-item
issue: 281
item: 4
item_type: item
date: 2026-05-13
source: https://tannerlinsley.com/posts/projecting-react
tags:
  - "TanStack"
  - "Bun"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-05-13-TWIR-281|Index]]

# Item 4: Projecting React

Source: [https://tannerlinsley.com/posts/projecting-react](https://tannerlinsley.com/posts/projecting-react)

Summary:
This article explores building a custom, minimal React runtime projection tailored for TanStack Start, reducing bundle size by stripping unneeded features. The author describes the limitations of using Preact as a drop-in replacement for React 19, and details how a projection approach—selectively including only required React features—enables a much smaller, customizable runtime. The piece discusses the technical and philosophical implications of treating React’s API as a stable “base table” that can be projected differently for specific needs.

Key takeaways:
- Preact/compat is no longer a seamless drop-in for React 19, especially with new APIs and server features.
- Custom projection yields a React-compatible runtime as small as 7 KB gzip, with toggleable features.
- The approach enables precise control over which React features are included, optimizing for specific product requirements.
- Demonstrates that RSC (React Server Components) can work with such projections, with some trade-offs.

Recommendation:
Read fully (for those interested in React internals, custom runtimes, or advanced optimization)

Why it matters:
for those interested in React internals, custom runtimes, or advanced optimization

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
