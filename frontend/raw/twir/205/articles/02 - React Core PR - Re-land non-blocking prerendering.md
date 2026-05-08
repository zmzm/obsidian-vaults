---
type: twir-item
issue: 205
item: 2
item_type: item
date: 2024-10-16
source: https://github.com/facebook/react/pull/31238
tags:
  - "PR"
status: auto
quality: keep
---

[[2024-10-16-TWIR-205|Index]]

# Item 2: React Core PR - Re-land non-blocking prerendering

Source: [https://github.com/facebook/react/pull/31238](https://github.com/facebook/react/pull/31238)

Summary:
This React core pull request partially re-lands a previous change to make prerendering always non-blocking, after addressing issues that caused a prior revert. The update ensures that when a synchronous update suspends, sibling prerendering does not block the main thread, improving responsiveness. The rollout is being done incrementally for better control and testing.

Key takeaways:
- Non-blocking prerendering improves React's responsiveness during Suspense and concurrent rendering.
- The change was previously reverted due to breakages, now reintroduced with additional feature flag checks.
- Rollout is incremental to manage stability and testing.

Recommendation:
Summary sufficient (read PR for deep internals or if maintaining React forks)

Why it matters:
read PR for deep internals or if maintaining React forks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
