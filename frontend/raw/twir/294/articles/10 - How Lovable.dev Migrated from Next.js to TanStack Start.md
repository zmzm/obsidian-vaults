---
type: twir-item
issue: 294
item: 10
item_type: item
date: 2026-08-19
source: https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs
tags:
  - "TanStack"
  - "Nextjs"
  - "Lovabledev"
status: auto
quality: keep
---

[[2026-08-19-TWIR-294|Index]]

# Item 10: How Lovable.dev Migrated from Next.js to TanStack Start

Source: [https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs](https://lovable.dev/blog/how-we-migrated-lovable-dev-away-from-nextjs)

Summary:
Lovable.dev migrated a large, high-traffic Next.js app to TanStack Start, using a gradual, route-by-route approach. The migration involved running both frameworks in parallel, using feature flags for controlled rollout, and sharing most code between frameworks via a dedicated shared folder and module aliasing. Techniques like browser View Transitions and deterministic feature flags improved user experience and testability during the migration.

Key takeaways:
- Large-scale migration was done incrementally, with both frameworks live and feature-flagged.
- Shared codebase structure enabled 90–95% code reuse between frameworks.
- Browser View Transitions smoothed hard navigations between frameworks.
- Deterministic feature flags allowed reliable end-to-end testing during rollout.

Recommendation:
Read fully (for migration strategies, large-scale React app architecture, and DX improvements)

Why it matters:
for migration strategies, large-scale React app architecture, and DX improvements

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
