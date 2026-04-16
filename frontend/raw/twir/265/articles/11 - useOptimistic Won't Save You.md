---
type: twir-item
issue: 265
item: 11
item_type: item
date: 2026-01-21
source: https://github.com/prettier/prettier/pull/18533
tags:
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 11: useOptimistic Won't Save You

Source: [https://github.com/prettier/prettier/pull/18533](https://github.com/prettier/prettier/pull/18533)

Summary:
This article analyzes the challenges of implementing optimistic UI updates in React, especially with the new useOptimistic hook in React 19. It demonstrates common pitfalls (race conditions, UI flicker), the complexity of correct manual implementations, and the limitations of useOptimistic in concurrent scenarios. The author concludes that while useOptimistic helps, developers must still handle edge cases and cannot rely on it as a silver bullet.

Key takeaways:
- Optimistic UI remains complex even with React's useOptimistic, especially under concurrent updates.
- Manual implementations require careful state management to avoid race conditions and UI inconsistencies.
- useOptimistic simplifies some aspects but does not eliminate all pitfalls.
- Developers should be cautious and test thoroughly when implementing optimistic updates.

Recommendation:
Read fully (for anyone implementing optimistic UI in React)

Why it matters:
for anyone implementing optimistic UI in React

Content:
# Upgrade MDX parser by fisker · Pull Request #18533 · prettier/prettier · GitHub

```
* extract micromark-extension-mdxjs

* defer the ESM parse to embed

* add a test case for undefined variable export

---------

Co-authored-by: autofix-ci[bot] <114827586+autofix-ci[bot]@users.noreply.github.com>
```
