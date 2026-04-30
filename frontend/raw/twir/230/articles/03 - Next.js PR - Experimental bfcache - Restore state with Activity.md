---
type: twir-item
issue: 230
item: 3
item_type: item
date: 2025-04-16
source: https://github.com/vercel/next.js/pull/77992
tags:
  - "Nextjs"
  - "Activity"
  - "PR"
status: auto
quality: keep
---

[[2025-04-16-TWIR-230|Index]]

# Item 3: Next.js PR - Experimental bfcache - Restore state with <Activity>

Source: [https://github.com/vercel/next.js/pull/77992](https://github.com/vercel/next.js/pull/77992)

Summary:
This Next.js PR introduces an experimental feature leveraging React's `<Activity>` API to preserve and restore UI state (including React state) across route navigations, not just browser-native bfcache scenarios. Each route segment is wrapped in an Activity boundary, allowing React to keep inactive routes mounted and quickly restore their state on navigation. This approach also enables faster navigations and lays groundwork for speculative pre-rendering.

Key takeaways:
- `<Activity>` boundaries preserve React state across navigations, including for back/forward and regular links.
- Inactive routes are kept mounted, improving navigation speed and user experience.
- The feature is currently experimental, with a hardcoded cache size and plans for future configurability.
- Does not affect dynamic data caching, which is handled separately.

Recommendation:
Summary sufficient (read the PR if you want implementation details or plan to experiment with stateful navigation in Next.js)

Why it matters:
read the PR if you want implementation details or plan to experiment with stateful navigation in Next.js

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
