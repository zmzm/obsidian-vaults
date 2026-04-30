---
type: twir-item
issue: 235
item: 2
item_type: item
date: 2025-05-21
source: https://github.com/facebook/react/pull/33215
tags:
  - "createStore"
  - "PR"
  - "API"
status: auto
quality: keep
---

[[2025-05-21-TWIR-235|Index]]

# Item 2: React Core PR - createStore() skeleton API

Source: [https://github.com/facebook/react/pull/33215](https://github.com/facebook/react/pull/33215)

Summary:
A new pull request introduces the skeleton for a createStore() API in React, laying groundwork for a future store-based state management solution. The API is not functional yet but sets up feature flags, test files, and basic type discussions. Community discussion centers on type safety, reducer/action flexibility, and compatibility with concurrent rendering.

Key takeaways:
- The createStore() API is in early, non-functional stages—primarily scaffolding.
- Intended usage: create a store and read its value with use(store).
- Type system considerations (covariance/contravariance for actions, strong typing for reducers).
- Community is comparing this direction to userland solutions and discussing concurrent rendering implications.

Recommendation:
Summary sufficient (read PR for deep type discussions or if following React state management evolution closely)

Why it matters:
read PR for deep type discussions or if following React state management evolution closely

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
