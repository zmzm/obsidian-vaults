---
type: twir-item
issue: 294
item: 9
item_type: item
date: 2026-08-19
source: https://julesblom.com/writing/hoistable-svg-defs-ii
tags:
  - "DOM"
  - "SVG"
  - "Effect"
status: auto
quality: keep
---

[[2026-08-19-TWIR-294|Index]]

# Item 9: Impersonating the DOM – Hoistable SVG Defs in React

Source: [https://julesblom.com/writing/hoistable-svg-defs-ii](https://julesblom.com/writing/hoistable-svg-defs-ii)

Summary:
This article explores advanced patterns for managing SVG <defs> in React, inspired by React 19’s <head> handling. It discusses the challenge of deduplicating SVG definitions across components and reviews several approaches, including React Aria’s technique of portaling into a fake DOM container. The solution leverages React’s commit phase and useSyncExternalStore to track mounted definitions efficiently, avoiding useEffect-based registries.

Key takeaways:
- Managing SVG <defs> in React requires deduplication and lifecycle tracking.
- React Aria’s approach uses a fake DOM container and portals to intercept mount/unmount events.
- useSyncExternalStore enables efficient updates from the fake container to React components.
- The pattern avoids the limitations of useEffect registries and leverages React’s internal reconciler.

Recommendation:
Read fully (for advanced React patterns and SVG handling)

Why it matters:
for advanced React patterns and SVG handling

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
