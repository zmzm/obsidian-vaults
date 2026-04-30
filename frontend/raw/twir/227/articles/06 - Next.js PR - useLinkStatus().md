---
type: twir-item
issue: 227
item: 6
item_type: item
date: 2025-03-26
source: https://github.com/vercel/next.js/pull/77300
tags:
  - "Nextjs"
  - "PR"
  - "useLinkStatus"
status: auto
quality: keep
---

[[2025-03-26-TWIR-227|Index]]

# Item 6: Next.js PR - useLinkStatus()

Source: [https://github.com/vercel/next.js/pull/77300](https://github.com/vercel/next.js/pull/77300)

Summary:
This pull request introduces the `useLinkStatus` hook for Next.js, which provides loading state feedback during navigation transitions, especially when link prefetching is disabled. The hook returns a `pending` state before navigation completes, helping to prevent UI "freezes" during route changes. It only works with the App Router and must be used within a descendant of a `Link` component.

Key takeaways:
- `useLinkStatus` enables custom loading indicators for navigation triggered by Next.js `Link`.
- Only effective when prefetch is disabled or navigation occurs before prefetch completes.
- Not supported in the Pages Router; always returns `pending: false` outside App Router.
- Only the last clicked link’s pending state is shown if multiple links are clicked quickly.

Recommendation:
Summary sufficient (read PR for implementation or usage specifics)

Why it matters:
read PR for implementation or usage specifics

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
