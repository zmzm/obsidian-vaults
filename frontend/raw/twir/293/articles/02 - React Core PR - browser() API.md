---
type: twir-item
issue: 293
item: 2
item_type: item
date: 2026-08-05
source: https://github.com/react/react/pull/37143
tags:
  - "browser"
  - "PR"
  - "API"
status: auto
quality: keep
---

[[2026-08-05-TWIR-293|Index]]

# Item 2: React Core PR - browser() API

Source: [https://github.com/react/react/pull/37143](https://github.com/react/react/pull/37143)

Summary:
A new browser() API is proposed for react-dom, enabling components to intentionally suspend during SSR and only render in the browser. This codifies a common pattern where certain components should not render on the server, providing a clean, recoverable error mechanism that avoids noisy error logs. The API must be used within a Suspense boundary and is designed to be isomorphic, supporting advanced use cases. Implementation details focus on error handling, silent recovery, and feature flagging for safe rollout.

Key takeaways:
- browser() allows you to suspend rendering on the server, resuming only in the browser, without hacky error suppression.
- Must be used inside a Suspense boundary; outside usage is currently an error.
- Designed for advanced SSR/client-only rendering patterns, with careful error handling and logging suppression.
- Implementation is feature-flagged and can be disabled if necessary before stable release.

Recommendation:
Summary sufficient (unless you plan to use or contribute to this API directly)

Why it matters:
unless you plan to use or contribute to this API directly

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
