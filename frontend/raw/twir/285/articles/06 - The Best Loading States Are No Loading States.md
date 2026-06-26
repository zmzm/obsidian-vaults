---
type: twir-item
issue: 285
item: 6
item_type: item
date: 2026-06-10
source: https://jjenzz.com/best-loading-states-are-no-loading-states/
tags:
status: auto
quality: keep
---

[[2026-06-10-TWIR-285|Index]]

# Item 6: The Best Loading States Are No Loading States

Source: [https://jjenzz.com/best-loading-states-are-no-loading-states/](https://jjenzz.com/best-loading-states-are-no-loading-states/)

Summary:
The article argues that modern apps should minimize explicit loading states (spinners, skeletons) by leveraging route transitions and preloading data, returning to a model closer to traditional web navigation. By preloading data on link hover or intersection and only showing a global loading indicator as a fallback, developers can avoid scattered loading logic and improve perceived performance. The approach is demonstrated with TanStack Router, but is applicable to any router supporting route transitions.

Key takeaways:
- Advocates for preloading route data to avoid component-level loading states.
- Suggests using a single, global loading indicator only when preloading is insufficient.
- Encourages treating missing UI as a signal to improve preload coverage, not as a bug.
- Demonstrates the pattern with TanStack Router, but concept is router-agnostic.

Recommendation:
Summary sufficient (read full article for implementation details or if rethinking loading strategies)

Why it matters:
read full article for implementation details or if rethinking loading strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
