---
type: twir-item
issue: 265
item: 14
item_type: item
date: 2026-01-21
source: https://nextjs.org/blog/turbopack-incremental-computation
tags:
  - "ReactCompiler"
status: auto
---

[[2026-01-21-TWIR-265|Index]]

# Item 14: Adapting Library Logic for React Compiler

Source: [https://nextjs.org/blog/turbopack-incremental-computation](https://nextjs.org/blog/turbopack-incremental-computation)

Summary:
This post details the process of adapting TanStack Form and similar libraries for compatibility with the React Compiler, highlighting subtle pitfalls with mutable state and referential stability. The author demonstrates how certain patterns (e.g., mutating objects returned from useState) can break under the compiler's memoization logic, especially when props are passed to child components. ESLint may not catch all such issues, so library authors must audit and refactor code to ensure compiler safety.

Key takeaways:
- React Compiler introduces stricter requirements for immutability and referential stability.
- Mutating state objects or relying on reference equality can cause subtle bugs under the compiler.
- Library authors must review and adapt patterns, especially for hooks and class-based logic.
- ESLint may not catch all problematic patterns; manual code review is necessary.

Recommendation: Read fully (for library maintainers and those preparing for React Compiler)

Related notes: [[React Compiler]]
