---
type: twir-item
issue: 217
item: 2
item_type: item
date: 2025-01-15
source: https://github.com/facebook/react/pull/31996
tags:
  - "ViewTransitions"
  - "PR"
  - "v2"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 2: React Core PR - Support only View Transitions v2

Source: [https://github.com/facebook/react/pull/31996](https://github.com/facebook/react/pull/31996)

Summary:
React will only support the View Transitions v2 specification for its new animation features, relying on View Transition Classes and Types for styling. This approach avoids partial or incorrect animations in browsers that lack full support, such as older Safari versions and Firefox (which has yet to implement the spec). The team prefers disabling animations entirely in unsupported browsers to prevent inconsistent behavior.

Key takeaways:
- Only browsers supporting View Transitions v2 (Chrome, Safari 18.2+) will animate; older versions and Firefox will not.
- Feature detection is done via the object form of startViewTransition, which throws on unsupported versions.
- Avoids ecosystem complexity and flaky effects by not supporting legacy naming-based transitions.
- No plans to optimize for soon-to-be-unsupported browsers.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
