---
type: twir-item
issue: 217
item: 4
item_type: item
date: 2025-01-15
source: https://github.com/vercel/next.js/pull/74659
tags:
  - "Nextjs"
  - "PR"
  - "experimentalviewTransition"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 4: Next.js PR - experimental.viewTransition flag

Source: [https://github.com/vercel/next.js/pull/74659](https://github.com/vercel/next.js/pull/74659)

Summary:
Next.js introduces an experimental.viewTransition flag to enable React's unstable_ViewTransition component. This flag currently just opts into React's experimental build, but may later support Next.js-specific features for transitions, such as navigation types. The feature is behind a flag and is not yet production-ready.

Key takeaways:
- Enables use of React's experimental <ViewTransition /> in Next.js via a config flag.
- Lays groundwork for future Next.js-specific transition features.
- Currently experimental and tied to React's unstable API.
- Not intended for production; for experimentation and feedback.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
