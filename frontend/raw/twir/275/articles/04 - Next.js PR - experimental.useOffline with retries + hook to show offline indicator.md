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
quality: keep
---

[[2026-04-01-TWIR-275|Index]]

# Item 4: Next.js PR - experimental.useOffline with retries + hook to show offline indicator

Source: [https://github.com/vercel/next.js/pull/92012](https://github.com/vercel/next.js/pull/92012)

Summary:
A new experimental useOffline() hook is introduced in Next.js, available from next/navigation, which returns true when the app is offline. The hook is managed by a provider in the app router and uses useState and useOptimistic to ensure state updates even during blocked transitions. This feature is behind the experimental.useOffline flag and is designed to help developers show offline indicators and handle retry logic.

Key takeaways:
- useOffline() hook detects offline state and is easy to integrate in app components.
- State management ensures updates during navigation or connectivity changes.
- Currently experimental and subject to change; feedback and testing encouraged.
- Useful for building resilient, user-friendly offline experiences in Next.js apps.

Recommendation:
Summary sufficient

Content:
# [experiment] Add useOffline hook to expose offline state to userland by acdlite · Pull Request #92012 · vercel/next.js · GitHub

```
**Current:**

1. #92011

**Up next:**

2. #92012

---

When a navigation, server action, or prefetch fails due to a network
error, instead of falling back to MPA navigation or surfacing an error,
the request blocks until connectivity is restored and then retries
automatically.

Offline detection works by treating any `fetch()` rejection as a network
error (server errors resolve with a status code, they don't reject).
Once offline, a polling loop does HEAD requests with exponential backoff
to detect when connectivity returns. Browser offline/online events also
feed into this loop. Successful fetches from other code paths can
short-circuit the loop if they happen to land first.

Follow-up work will add a `useOffline` hook so apps can show an offline
indicator to the user, and allow navigations to read from stale cache
entries while offline.

Gated behind `experimental.useOffline`.
```
