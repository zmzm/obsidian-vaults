---
type: twir-item
issue: 265
item: 17
item_type: item
date: 2026-01-21
source: https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks
tags:
  - "BaseUI"
  - "UI"
status: auto
---

[[2026-01-21-TWIR-265|Index]]

# Item 17: Base UI composition pattern differs from Radix UI

Source: [https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks](https://nodejs.org/en/blog/vulnerability/january-2026-dos-mitigation-async-hooks)

Summary:
Base UI introduces the useRender hook for implementing render props in custom components, allowing consumers to override rendered elements or customize rendering logic. The pattern supports merging props and refs, and is designed to work seamlessly with React 19's ref handling (without forwardRef for primitives). The documentation provides examples and migration guidance from Radix UI.

Key takeaways:
- useRender enables flexible render prop patterns and element overrides in Base UI components.
- mergeProps simplifies combining event handlers, classNames, and styles.
- React 19's ref merging reduces the need for forwardRef in primitive components.
- Migration guidance is provided for users coming from Radix UI.

Recommendation: Summary sufficient
