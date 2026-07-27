---
type: twir-item
issue: 290
item: 3
item_type: item
date: 2026-07-15
source: https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary
tags:
  - "Suspense"
status: auto
quality: keep
---

[[2026-07-15-TWIR-290|Index]]

# Item 3: React Docs - What activates a Suspense boundary

Source: [https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary](https://react.dev/reference/react/Suspense#what-activates-a-suspense-boundary)

Summary:
This documentation explains when and how a <Suspense> boundary is activated in React, detailing its use cases, props, and caveats. It covers scenarios such as lazy-loading components, reading Promises with use, waiting for stylesheets, and server rendering. The guide also discusses fallback behavior, state preservation, and integration with streaming server rendering and selective hydration.

Key takeaways:
- <Suspense> shows a fallback UI while children are loading or suspending.
- Boundaries activate on lazy-loaded code, Promises with use, stylesheet loads, and server streaming.
- State is not preserved for suspended renders that haven't mounted; React retries from scratch.
- Advanced features include streaming, selective hydration, and experimental defer prop.

Recommendation:
Read fully (for anyone implementing or troubleshooting Suspense boundaries)

Why it matters:
for anyone implementing or troubleshooting Suspense boundaries

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
