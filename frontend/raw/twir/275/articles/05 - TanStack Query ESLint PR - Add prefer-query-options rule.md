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
quality: keep
---

[[2026-04-01-TWIR-275|Index]]

# Item 5: TanStack Query ESLint PR - Add prefer-query-options rule

Source: [https://github.com/TanStack/query/pull/10359](https://github.com/TanStack/query/pull/10359)

Summary:
A new ESLint rule, prefer-query-options, enforces the use of queryOptions() or infiniteQueryOptions() to co-locate query keys and functions, preventing manual repetition and potential errors. The rule is stricter than previous ones and is included in a new recommendedStrict config. Extensive documentation, tests, and examples are provided to guide adoption.

Key takeaways:
- prefer-query-options rule flags manual query key usage, encouraging co-location for maintainability.
- New recommendedStrict config includes this rule for stricter codebases.
- Documentation and examples illustrate correct and incorrect usage patterns.
- Improves code consistency and reduces duplication in TanStack Query usage.

Recommendation:
Summary sufficient

Content:
# add prefer-query-options rule by Newbie012 · Pull Request #10359 · TanStack/query · GitHub

```
Verify each finding against the current code and only fix it if needed.

Nitpick comments:
In `@packages/eslint-plugin-query/src/__tests__/prefer-query-options.test.ts`:
- Around line 45-130: Add happy-path tests to cover direct and mapped builder
usages so the rule doesn't false-positive: add a valid case where useQuery is
called directly with a queryOptions call (e.g., useQuery(queryOptions({...}))
and a valid case where useQueries / useSuspenseQueries receive mapped builder
results (e.g., queries: [todosOptions, usersOptions].map(... ) or queries:
[todosOptions(), usersOptions()]). Update the test block under "hooks consuming
queryOptions result" in prefer-query-options.test.ts to include these scenarios
(referencing useQuery, useQueries, useSuspenseQueries, queryOptions,
todosOptions, usersOptions) as additional entries in the valid array.
- Around line 659-767: Add matching "happy path" valid tests for the queryClient
methods that accept full options so the rule verifies the allowed replacement
pattern; specifically add valid cases for fetchQuery, prefetchQuery,
fetchInfiniteQuery, prefetchInfiniteQuery, ensureQueryData, and
ensureInfiniteQueryData that demonstrate the accepted "shared/options" usage
(the intended replacement for the inline { queryKey, queryFn } pattern) so the
rule's client-side behavior is covered alongside the current invalid tests that
reference those methods.
```

Related notes: [[TanStack Query]]
