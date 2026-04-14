---
type: twir-item
issue: 261
item: 9
item_type: item
date: 2025-12-03
source: https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/
tags:
status: auto
---

[[2025-12-03-TWIR-261|Index]]

# Item 9: React has changed, your Hooks should too

Source: [https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/](https://allthingssmitty.com/2025/12/01/react-has-changed-your-hooks-should-too/)

Summary:
This article argues that modern React (18/19) requires a rethink of Hook usage, moving away from overusing useEffect for data fetching and derived state. It advocates for render-driven derivation, useEffectEvent for effects, custom hooks for encapsulation, and useSyncExternalStore for subscriptions. The post also covers concurrency tools (useDeferredValue, startTransition), testing strategies, and the trend toward data-first, server-driven React apps.

Key takeaways:
- Avoid overusing useEffect; prefer render-time derivation and framework primitives.
- Encapsulate logic in custom hooks for maintainability and testability.
- useSyncExternalStore is the preferred pattern for external subscriptions.
- Leverage concurrency APIs for smoother, more responsive UIs.

Recommendation: Read fully (especially for teams modernizing their React codebase or hook patterns)
