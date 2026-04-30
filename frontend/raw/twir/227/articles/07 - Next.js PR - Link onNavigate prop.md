---
type: twir-item
issue: 227
item: 7
item_type: item
date: 2025-03-26
source: https://github.com/vercel/next.js/pull/77209
tags:
  - "Nextjs"
  - "PR"
status: auto
quality: keep
---

[[2025-03-26-TWIR-227|Index]]

# Item 7: Next.js PR - Link onNavigate prop

Source: [https://github.com/vercel/next.js/pull/77209](https://github.com/vercel/next.js/pull/77209)

Summary:
This PR adds an `onNavigate` prop to the Next.js `Link` component, allowing developers to execute logic specifically when SPA-like navigation is triggered. Unlike `onClick`, which fires on all clicks, `onNavigate` only runs when client-side navigation occurs and provides an event object with `preventDefault()` to optionally block navigation.

Key takeaways:
- `onNavigate` is distinct from `onClick` and only fires for SPA navigations (not external links or downloads).
- Enables conditional navigation logic, such as authentication checks before routing.
- Modifier key clicks (e.g., Ctrl+Click) do not trigger `onNavigate`.
- Provides finer control over navigation events in Next.js applications.

Recommendation:
Summary sufficient (read PR for edge cases or advanced usage)

Why it matters:
read PR for edge cases or advanced usage

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
