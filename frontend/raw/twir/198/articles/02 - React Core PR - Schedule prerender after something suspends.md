---
type: twir-item
issue: 198
item: 2
item_type: item
date: 2024-08-28
source: https://github.com/facebook/react/pull/30800
tags:
  - "PR"
status: auto
quality: keep
---

[[2024-08-28-TWIR-198|Index]]

# Item 2: React Core PR - Schedule prerender after something suspends

Source: [https://github.com/facebook/react/pull/30800](https://github.com/facebook/react/pull/30800)

Summary:
This React core PR introduces the concept of "prerender" renders, which are triggered when a component suspends (e.g., during data fetching). The prerender phase moves speculative rendering of sibling components into a separate step, ensuring the UI can update and show fallbacks before additional work is done. This change is behind a feature flag and is part of a larger effort to improve React's handling of Suspense and transitions.

Key takeaways:
- Adds a prerender phase to avoid blocking UI updates when a component suspends.
- Speculative rendering of siblings is deferred until after fallbacks are displayed.
- Aims to improve responsiveness and correctness during Suspense-driven transitions.
- Breaking change for canary users; peer dependency bumped for React 19 RC.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
