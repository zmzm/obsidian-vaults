---
type: twir-item
issue: 215
item: 5
item_type: item
date: 2025-01-02
source: https://peterkellner.net/2024/12/31/replacing-legacy-throw-in-react-19-with-suspense-and-use/
tags:
  - "19"
status: auto
quality: keep
---

[[2025-01-02-TWIR-215|Index]]

# Item 5: Replacing Legacy throw in React 19 with Suspense and use

Source: [https://peterkellner.net/2024/12/31/replacing-legacy-throw-in-react-19-with-suspense-and-use/](https://peterkellner.net/2024/12/31/replacing-legacy-throw-in-react-19-with-suspense-and-use/)

Summary:
React 19 introduces a formal .use() API for Suspense, replacing the legacy pattern of throwing Promises to trigger suspension. The new approach is cleaner and more explicit, though React continues to support the old "throw Promise" pattern for backward compatibility. The article explains both methods and their implications for async data handling in React components.

Key takeaways:
- Legacy Suspense used "throw Promise" to pause rendering; React 19 adds .use(resource) for this purpose.
- .use() is clearer, more robust, and future-proof for async data and Suspense.
- Both patterns are currently supported for backward compatibility, but .use() is recommended going forward.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
