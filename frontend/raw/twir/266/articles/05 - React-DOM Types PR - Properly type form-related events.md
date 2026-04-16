---
type: twir-item
issue: 266
item: 5
item_type: item
date: 2026-01-28
source: https://github.com/DefinitelyTyped/DefinitelyTyped/pull/74383
tags:
  - "React-DOM"
  - "PR"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 5: React-DOM Types PR - Properly type form-related events

Source: [https://github.com/DefinitelyTyped/DefinitelyTyped/pull/74383](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/74383)

Summary:
This PR updates React's TypeScript types to deprecate React.FormEvent (which was equivalent to SyntheticEvent) and introduces more accurate typing for form-related events (change, input, invalid, reset, submit). It also adds a second parameter to ChangeEvent for specifying the event target, improving type safety. The changes are limited to React 19 types to minimize disruption, with some adjustments deferred to React 20.

Key takeaways:
- React.FormEvent is deprecated in favor of more precise event types.
- ChangeEvent now supports specifying the target type for better type safety.
- Some breaking changes are held for React 20 to reduce migration friction.
- Improves accuracy of event typing, which may surface previously hidden type errors.

Recommendation:
Read fully (read fully if maintaining large TypeScript React codebases or custom form components)

Why it matters:
read fully if maintaining large TypeScript React codebases or custom form components

Content:
# [react] Properly type form-related events by eps1lon · Pull Request #74383 · DefinitelyTyped/DefinitelyTyped · GitHub

[![@eps1lon](https://avatars.githubusercontent.com/u/12292047?s=40&u=d1523888bc16deb2ce9f5294e4849d1a2f02270c&v=4)](/eps1lon)
[eps1lon](/eps1lon)

marked this pull request as ready for review

[January 23, 2026 10:57](#event-22239882144)
