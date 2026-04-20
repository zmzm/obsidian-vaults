---
type: twir-item
issue: 252
item: 4
item_type: item
date: 2025-10-01
source: https://blacksheepcode.com/posts/nuance_of_react_rendering_behaviour
tags:
status: auto
quality: keep
---

[[2025-10-01-TWIR-252|Index]]

# Item 4: The nuance of React rendering behaviour as it relates to children

Source: [https://blacksheepcode.com/posts/nuance_of_react_rendering_behaviour](https://blacksheepcode.com/posts/nuance_of_react_rendering_behaviour)

Summary:
This post explores subtle differences in React’s rendering behavior when children are rendered directly versus passed via props.children. Through code examples and compiled JSX output, it demonstrates that directly rendered children re-render on parent state changes, while children passed as props may not. The article questions why React’s documentation does not highlight this distinction and analyzes how JSX compiles under the hood.

Key takeaways:
- Directly rendered children are always re-evaluated on parent updates, while props.children may retain referential stability.
- React’s documentation does not distinguish between these two patterns, but real-world behavior can differ.
- Understanding compiled JSX helps clarify why these rendering differences occur.
- Awareness of this nuance can help optimize component performance and avoid unexpected re-renders.

Recommendation:
Read fully (read fully if you frequently design reusable components or optimize render performance)

Why it matters:
read fully if you frequently design reusable components or optimize render performance

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
