---
type: twir-item
issue: 206
item: 4
item_type: item
date: 2024-10-23
source: https://www.framer.com/blog/sites-interactive-faster/
tags:
  - "50"
status: auto
quality: keep
---

[[2024-10-23-TWIR-206|Index]]

# Item 4: Framer Sites Now Become Interactive 50% Faster

Source: [https://www.framer.com/blog/sites-interactive-faster/](https://www.framer.com/blog/sites-interactive-faster/)

Summary:
Framer has improved site interactivity speed by 50% by restructuring how React Suspense boundaries are used during hydration. Instead of a single Suspense boundary, Framer now wraps each data-fetching component in its own boundary, reducing redundant renders and making hydration a linear process. This optimization leads to faster user interactivity, especially on slower devices, and is automatically rolled out to all Framer sites.

Key takeaways:
- Granular Suspense boundaries prevent repeated re-renders during hydration, improving performance.
- Hydration is now O(n) instead of causing multiple redundant renders.
- Users experience faster interactive times, with measurable improvements even on fast devices.
- The approach is generally applicable to React apps using Suspense for data fetching.

Recommendation:
Read fully (read fully if interested in React hydration internals or performance engineering)

Why it matters:
read fully if interested in React hydration internals or performance engineering

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
