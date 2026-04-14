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
---

[[2026-01-28-TWIR-266|Index]]

# Item 5: React-DOM Types PR – Properly type form-related events

Source: [https://github.com/DefinitelyTyped/DefinitelyTyped/pull/74383](https://github.com/DefinitelyTyped/DefinitelyTyped/pull/74383)

Summary:
This PR deprecates React.FormEvent (which was equivalent to React.SyntheticEvent) and introduces more accurate typing for form-related events (change, input, invalid, reset, submit) in React 19 types. It also refines ChangeEvent typing to specify the target, with changes limited to React 19 to minimize disruption. The PR includes improved test coverage and notes that further changes may be deferred to React 20.

Key takeaways:
- Deprecates React.FormEvent in favor of more precise event types.
- Adds target typing to ChangeEvent for better type safety.
- Changes only affect latest (React 19) types to reduce breaking changes.
- Improved tests for event target narrowing and proper handler typing.

Recommendation: Summary sufficient (read PR if you maintain or heavily rely on React type definitions)
