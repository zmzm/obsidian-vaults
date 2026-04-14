---
type: twir-item
issue: 275
item: 5
item_type: item
date: 2026-04-01
source: https://github.com/TanStack/query/pull/10359
tags:
  - "TanStack"
  - "TanStackQuery"
  - "ESLint"
  - "PR"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 5: TanStack Query ESLint PR - Add prefer-query-options rule

Source: [https://github.com/TanStack/query/pull/10359](https://github.com/TanStack/query/pull/10359)

Summary:
A new ESLint rule, prefer-query-options, enforces the use of queryOptions()/infiniteQueryOptions() to co-locate query keys and functions, reducing duplication and potential errors. The rule is included in a new recommendedStrict config and is supported by extensive documentation and tests. This change encourages more maintainable and less error-prone query definitions in TanStack Query projects.

Key takeaways:
- prefer-query-options rule flags manual queryKey usage, enforcing co-location with query functions.
- Included in recommendedStrict ESLint config for stricter codebases.
- Comprehensive docs, examples, and tests provided.
- Aims to reduce duplication and improve maintainability of query code.

Recommendation: Summary sufficient

Related notes: [[TanStack Query]]
