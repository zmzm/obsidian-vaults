---
type: twir-item
issue: 275
item: 4
item_type: item
date: 2026-04-01
source: https://github.com/vercel/next.js/pull/92012
tags:
  - "Nextjs"
  - "PR"
  - "experimentaluseOffline"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 4: Next.js PR - experimental.useOffline with retries + hook to show offline indicator

Source: [https://github.com/vercel/next.js/pull/92012](https://github.com/vercel/next.js/pull/92012)

Summary:
A new experimental useOffline() hook is introduced in next/navigation, allowing apps to detect and respond to offline status. The hook is powered by a provider using useState and useOptimistic, ensuring state updates even during blocked transitions. This enables developers to implement offline indicators or retry logic in Next.js apps.

Key takeaways:
- useOffline() returns true when the app is offline, enabling responsive UI changes.
- State is managed via a provider and supports updates during navigation transitions.
- Feature is gated behind experimental.useOffline and is subject to change.
- Useful for improving UX in unreliable network conditions.

Recommendation: Summary sufficient
