---
type: twir-item
issue: 190
item: 3
item_type: item
date: 2024-06-19
source: https://github.com/facebook/react/issues/29898
tags:
  - "19"
  - "Suspense"
status: auto
quality: keep
---

[[2024-06-19-TWIR-190|Index]]

# Item 3: React 19 Issue - Disabling prerendering siblings of suspended components breaking common pattern

Source: [https://github.com/facebook/react/issues/29898](https://github.com/facebook/react/issues/29898)

Summary:
This GitHub issue documents community concerns about React 19’s change to Suspense, specifically how it breaks the common pattern of colocated data fetching by turning parallel requests into waterfalls. The discussion advocates for making the new behavior opt-in and retaining the previous default, emphasizing the migration challenges and the importance of flexibility in React patterns.

Key takeaways:
- The change to Suspense breaks parallel data fetching, leading to measurable performance regressions.
- Migrating away from the old pattern is non-trivial and could require significant refactoring.
- The community suggests making the new Suspense behavior opt-in via a boundary strategy prop.
- The issue highlights the importance of preserving React’s flexibility and composability.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
