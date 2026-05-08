---
type: twir-item
issue: 203
item: 3
item_type: item
date: 2024-10-01
source: https://github.com/vercel/next.js/pull/69949
tags:
  - "Nextjs"
  - "PR"
  - "API"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 3: Next.js PR - Add connection() as a new dynamic API

Source: [https://github.com/vercel/next.js/pull/69949](https://github.com/vercel/next.js/pull/69949)

Summary:
Next.js introduces a new connection() API to replace the unstable_noStore() API. connection() returns a Promise that resolves only when a real user request is present, allowing components to block prerendering until runtime. This enables more granular control over when static or dynamic rendering occurs, especially in partial prerendering contexts.

Key takeaways:
- connection() is a new async API to defer rendering until a real user request exists.
- Replaces unstable_noStore(), aligning with new dynamic rendering patterns.
- Useful for excluding code from prerendering and controlling render timing in PPR scenarios.
- Does not expose the full Request object for safety and clarity.

Recommendation:
Summary sufficient (read the PR if you need implementation details or are migrating from unstable_noStore()

Why it matters:
read the PR if you need implementation details or are migrating from unstable_noStore(

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
