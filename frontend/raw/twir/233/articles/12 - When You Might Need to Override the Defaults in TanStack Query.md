---
type: twir-item
issue: 233
item: 14
item_type: item
date: 2025-05-07
source: https://www.kxlaa.com/articles/when-you-might-need-to-override-the-defaults-in-tanstack-query
tags:
  - "TS"
  - "TanStack"
  - "TanStackQuery"
status: auto
quality: keep
---

[[2025-05-07-TWIR-233|Index]]

# Item 14: When You Might Need to Override the Defaults in TanStack Query

Source: [https://www.kxlaa.com/articles/when-you-might-need-to-override-the-defaults-in-tanstack-query](https://www.kxlaa.com/articles/when-you-might-need-to-override-the-defaults-in-tanstack-query)

Summary:
This article reviews scenarios where overriding TanStack Query’s defaults is beneficial, such as disabling retries for certain errors or tests, and adjusting cache staleness for rarely-changing or rate-limited data. It provides practical code examples for customizing retry logic and cache lifetimes, and references open source projects for further study. The focus is on fine-tuning query behavior for specific production needs.

Key takeaways:
- Override retry defaults for tests or specific error codes (e.g., 404, 401, 403) to avoid unnecessary delays.
- Adjust cache staleness and garbage collection times for static or rate-limited data.
- TanStack Query’s configuration is highly flexible; production apps often tweak defaults for optimal UX and resource usage.
- Reviewing open source implementations can provide practical patterns.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
