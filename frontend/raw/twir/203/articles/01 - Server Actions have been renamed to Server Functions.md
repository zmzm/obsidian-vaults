---
type: twir-item
issue: 203
item: 1
item_type: featured
date: 2024-10-01
source: https://19.react.dev/reference/rsc/server-functions
tags:
  - "ServerFunctions"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 1: Server Actions have been renamed to Server Functions

Source: [https://19.react.dev/reference/rsc/server-functions](https://19.react.dev/reference/rsc/server-functions)

Summary:
React 19 has renamed "Server Actions" to "Server Functions" to clarify that not all server-executed functions are actions. Server Functions allow Client Components to call async functions on the server, supporting patterns like form submissions and progressive enhancement. The documentation details usage patterns, integration with forms, useActionState, and migration notes for bundlers/frameworks. The APIs for implementing Server Functions in frameworks are still stabilizing, so pinning React versions is recommended for now.

Key takeaways:
- "Server Actions" are now "Server Functions"; actions are a subset of functions used in action props or called from actions.
- Server Functions enable Client Components to trigger server-side logic asynchronously.
- Integration with new React 19 features: forms, useActionState, and progressive enhancement.
- Underlying APIs for bundlers/frameworks are not yet stable—pin React versions to avoid breakage.

Recommendation:
Read fully (especially if building or maintaining frameworks/bundlers, or using new React 19 form features)

Why it matters:
especially if building or maintaining frameworks/bundlers, or using new React 19 form features

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
