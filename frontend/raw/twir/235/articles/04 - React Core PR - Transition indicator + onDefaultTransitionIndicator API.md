---
type: twir-item
issue: 235
item: 4
item_type: item
date: 2025-05-21
source: https://github.com/facebook/react/pull/33162
tags:
  - "TransitionIndicator"
  - "PR"
  - "onDefaultTransitionIndicator"
  - "onDefaultTransitionIndicatorAPI"
  - "API"
status: auto
quality: keep
---

[[2025-05-21-TWIR-235|Index]]

# Item 4: React Core PR - Transition indicator + onDefaultTransitionIndicator API

Source: [https://github.com/facebook/react/pull/33162](https://github.com/facebook/react/pull/33162)

Summary:
A new API, onDefaultTransitionIndicator, is proposed to trigger a native browser loading spinner during React transitions when no custom loading state is provided. The implementation uses the Navigation API (where supported) to simulate navigation events, ensuring users see a loading indicator during transitions. The system is designed to avoid conflicts with ongoing navigations and provides a way for routers to detect React-initiated transitions.

Key takeaways:
- Default browser spinner will show during React transitions if no loading UI is rendered.
- Uses the Navigation API for native integration (Chrome only for now).
- Designed to avoid interrupting ongoing navigations and supports concurrent transitions.
- Routers can distinguish React transitions via a "react-transition" info field.

Recommendation:
Summary sufficient (read PR for implementation details or if building custom routers/loaders)

Why it matters:
read PR for implementation details or if building custom routers/loaders

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
