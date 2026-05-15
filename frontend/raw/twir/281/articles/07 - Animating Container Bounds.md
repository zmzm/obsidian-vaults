---
type: twir-item
issue: 281
item: 7
item_type: item
date: 2026-05-13
source: https://www.userinterface.wiki/animating-container-bounds
tags:
status: auto
quality: keep
---

[[2026-05-13-TWIR-281|Index]]

# Item 7: Animating Container Bounds

Source: [https://www.userinterface.wiki/animating-container-bounds](https://www.userinterface.wiki/animating-container-bounds)

Summary:
This post demonstrates how to smoothly animate container width or height changes in React using a custom useMeasure hook (built on ResizeObserver) and Motion for animation. The pattern involves measuring the inner content’s size and animating the outer container to match, resulting in fluid transitions for dynamic content like buttons or accordions. The approach is simple, dependency-light, and adaptable to various UI scenarios.

Key takeaways:
- useMeasure hook tracks element size changes via ResizeObserver.
- Animate outer container’s bounds based on measured inner content for smooth transitions.
- Works for both width (e.g., button labels) and height (e.g., expandable panels).
- Avoids initial animation glitches by checking bounds before animating.

Recommendation:
Summary sufficient (read for implementation details if needed)

Why it matters:
read for implementation details if needed

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
