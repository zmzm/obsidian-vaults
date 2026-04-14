---
type: twir-item
issue: 265
item: 11
item_type: item
date: 2026-01-21
source: https://github.com/prettier/prettier/pull/18533
tags:
status: auto
---

[[2026-01-21-TWIR-265|Index]]

# Item 11: useOptimistic Won't Save You

Source: [https://github.com/prettier/prettier/pull/18533](https://github.com/prettier/prettier/pull/18533)

Summary:
This article critically examines React 19's useOptimistic hook, highlighting its limitations and the complexity of implementing robust optimistic UI patterns in concurrent React. It walks through common pitfalls, such as race conditions and state desynchronization, and demonstrates why useOptimistic is not a complete solution for all optimistic update scenarios. The author provides code examples and discusses the need for careful state management even with the new hook.

Key takeaways:
- useOptimistic simplifies optimistic UI in some cases but does not eliminate race conditions or all manual state management.
- Optimistic updates in concurrent React remain complex, especially with transitions and rapid user interactions.
- Developers must still handle edge cases and potential UI inconsistencies.
- The article provides practical code samples illustrating these challenges.

Recommendation: Read fully (for anyone implementing optimistic UI in React)
