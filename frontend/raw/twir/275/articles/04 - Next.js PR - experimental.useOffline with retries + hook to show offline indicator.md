---
type: twir-item
issue: 275
item: 4
item_type: item
date: 2026-04-01
source: https://github.com/vercel/next.js/pull/92012
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 4: Next.js PR - experimental.useOffline with retries + hook to show offline indicator

Source: [https://github.com/vercel/next.js/pull/92012](https://github.com/vercel/next.js/pull/92012)

Content:
# [experiment] Add useOffline hook to expose offline state to userland by acdlite · Pull Request #92012 · vercel/next.js

Merged

[acdlite](https://github.com/acdlite) added a commit that referenced this pull request

[Mar 28, 2026](https://github.com/vercel/next.js/pull/92012#ref-commit-9045011)

[![@acdlite](https://avatars.githubusercontent.com/u/3624098?s=40&u=94d8ba563cef4d8fd24c4b666272a71af46a2fa1&v=4)](https://github.com/acdlite)

\*\*Current:\*\*

1. [#92011](https://github.com/vercel/next.js/pull/92011)

\*\*Up next:\*\*

2. [#92012](https://github.com/vercel/next.js/pull/92012)

---

When a navigation, server action, or prefetch fails due to a network
error, instead of falling back to MPA navigation or surfacing an error,
the request blocks until connectivity is restored and then retries
automatically.

Offline detection works by treating any \`fetch()\` rejection as a network
error (server errors resolve with a status code, they don't reject).
Once offline, a polling loop does HEAD requests with exponential backoff
to detect when connectivity returns. Browser offline/online events also
feed into this loop. Successful fetches from other code paths can
short-circuit the loop if they happen to land first.

Follow-up work will add a \`useOffline\` hook so apps can show an offline
indicator to the user, and allow navigations to read from stale cache
entries while offline.

Gated behind \`experimental.useOffline\`.

[![@acdlite](https://avatars.githubusercontent.com/u/3624098?s=40&u=94d8ba563cef4d8fd24c4b666272a71af46a2fa1&v=4)](https://github.com/acdlite) [acdlite](https://github.com/acdlite) changed the base branch from use-offline-retry to canary

[March 28, 2026 00:48](https://github.com/vercel/next.js/pull/92012#event-23989319114)

[![@acdlite](https://avatars.githubusercontent.com/u/3624098?s=40&v=4)](https://github.com/acdlite)

Adds a useOffline() hook exported from next/navigation that returns
true when the app is offline. The state is owned by a provider
component rendered in the app router, using useState + useOptimistic
so the value can update even during blocked transitions (e.g., a
navigation that's waiting for connectivity).

Gated behind the experimental.useOffline flag.

Refresh of use-offline-hook

[![@acdlite](https://avatars.githubusercontent.com/u/3624098?s=40&u=94d8ba563cef4d8fd24c4b666272a71af46a2fa1&v=4)](https://github.com/acdlite) [acdlite](https://github.com/acdlite) marked this pull request as ready for review

[March 28, 2026 00:59](https://github.com/vercel/next.js/pull/92012#event-23989466538)

Open

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)](https://github.com/apps/github-actions) [github-actions](https://github.com/apps/github-actions) bot locked as **resolved** and limited conversation to collaborators

[Apr 11, 2026](https://github.com/vercel/next.js/pull/92012#event-24406885839)

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
