---
type: twir-item
issue: 196
item: 2
item_type: item
date: 2024-08-14
source: https://github.com/facebook/react/issues/29898
tags:
  - "DI"
  - "19"
status: auto
quality: keep
---

[[2024-08-14-TWIR-196|Index]]

# Item 2: React 19 - Disabling prerendering siblings of suspended components breaking common pattern

Source: [https://github.com/facebook/react/issues/29898](https://github.com/facebook/react/issues/29898)

Summary:
A proposed change in React 19 disables prerendering for sibling components of suspended components, leading to performance regressions in common data-fetching patterns. Community members report that this causes requests to execute sequentially rather than in parallel, increasing load times and breaking established best practices. Suggestions include making the new behavior opt-in and allowing developers to choose between parallel and sequential strategies.

Key takeaways:
- React 19's change impacts performance by forcing sequential data fetching in some patterns.
- The community is concerned about migration difficulty and loss of flexibility.
- There is a call for making the new prerendering strategy configurable.
- The issue is significant enough to affect upgrade decisions for some projects.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
