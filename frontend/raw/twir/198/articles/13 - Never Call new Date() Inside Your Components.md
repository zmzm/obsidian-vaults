---
type: twir-item
issue: 198
item: 13
item_type: item
date: 2024-08-28
source: https://kyleshevlin.com/never-call-new-date-inside-your-components/
tags:
status: auto
quality: keep
---

[[2024-08-28-TWIR-198|Index]]

# Item 13: Never Call new Date() Inside Your Components

Source: [https://kyleshevlin.com/never-call-new-date-inside-your-components/](https://kyleshevlin.com/never-call-new-date-inside-your-components/)

Summary:
The article argues against calling impure functions like new Date() or Math.random() inside React components, especially for initial state, due to test flakiness and unpredictability. Instead, it recommends passing such values as props or using default parameters, making components pure and easier to test.

Key takeaways:
- Avoid impure functions in components to ensure deterministic rendering and testing.
- Pass values like dates or random numbers as props or via default parameters.
- Pattern applies to other impure functions (e.g., Math.random).
- Improves testability and maintainability.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
