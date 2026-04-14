---
type: twir-item
issue: 268
item: 4
item_type: item
date: 2026-02-11
source: https://anita-app.com/blog/articles/react-compiler-and-why-class-objects-work-against-memoization.html
tags:
  - "ReactCompiler"
status: auto
---

[[2026-02-11-TWIR-268|Index]]

# Item 4: React Compiler and why class objects can work against memoization

Source: [https://anita-app.com/blog/articles/react-compiler-and-why-class-objects-work-against-memoization.html](https://anita-app.com/blog/articles/react-compiler-and-why-class-objects-work-against-memoization.html)

Summary:
This article analyzes how the React Compiler’s automatic memoization can be undermined by class-based object models. Because React’s memoization relies on reference equality, passing class instances (with methods for derived values) leads to unnecessary recomputation if the instance reference changes, even if the underlying data is unchanged. The author suggests alternatives: expose primitives for dependencies, use plain data objects with pure helper functions, or pass only the minimal required data to child components to maximize memoization efficiency.

Key takeaways:
- React Compiler’s memoization is most effective with plain data and pure functions, not class instances.
- Passing class instances as props can cause unnecessary recomputation due to reference changes.
- Manual useMemo/useCallback can work but requires exposing internals and adds boilerplate.
- Prefer passing primitives or derived values directly to components for optimal memoization.

Recommendation: Read fully (for teams using class-based models or migrating to React Compiler)

Related notes: [[React Compiler]]
