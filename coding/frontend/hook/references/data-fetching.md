---
id: frontend/hook/data-fetching
name: frontend/hook/data-fetching
kind: reference
domain: frontend
topics: [hook, data fetching]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Hooks for Data Fetching

> **See also**: For query options, key design, dependent queries, and cache-oriented behavior, see
> `fe-react-query/references/query-options.md` and `fe-react-query/references/custom-hooks.md`.

This document focuses on **hook-specific patterns** for wrapping queries.

## When to use

Use this document when:

- **Wrapping queries** in custom hooks with consistent return interfaces
- Adding **computed values** (isEmpty, formatted data) to query hooks
- Deciding what to **return from query hooks**

For raw `useQuery` configuration patterns → see `fe-react-query/query-options.md`

## Rules

- Files must use `.hook.ts` extension (never `.tsx`)
- Return enhanced interface with computed values
- Always provide default values for data
- Include `isEmpty` for list hooks

## Hook Return Interface Pattern

```typescript
// ✅ Good: Enhanced return interface
export const useCourses = (filters?: CourseFilters) => {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['courses', filters],
    queryFn: () => apiClient.get('/courses', { params: filters }),
  });

  return {
    courses: data?.data || [], // Default value
    isLoading,
    error,
    refetch,
    isEmpty: data?.data?.length === 0, // Computed value
    total: data?.meta?.total || 0, // Extracted metadata
  };
};

// ✅ Good: Single resource hook
export const useCourse = (courseId: string) => {
  const { data, isLoading, error } = useQuery({
    queryKey: ['courses', courseId],
    queryFn: () => apiClient.get(`/courses/${courseId}`),
    enabled: !!courseId,
  });

  return {
    course: data?.data,
    isLoading,
    error,
    isNotFound: !isLoading && !data?.data,
  };
};
```

```typescript
// ❌ Bad: Returning raw query result
export const useCourses = () => {
  return useQuery({...});  // Consumer has to extract data.data
};
```

## Naming Conventions

| Hook Type       | Naming Pattern               | Example                  |
| --------------- | ---------------------------- | ------------------------ |
| List query      | `use{Resource}s`             | `useCourses`, `useUsers` |
| Single resource | `use{Resource}`              | `useCourse`, `useUser`   |
| Filtered list   | `use{Resource}s` with params | `useCourses(filters)`    |

## Anti-patterns

- Returning raw query result instead of enhanced interface
- Missing default values for data
- Missing computed values (isEmpty, isNotFound)
- Using `.tsx` extension for hook files

## Notes

- This document covers **hook wrapper patterns**
- For query fundamentals (keys, staleTime, enabled) → `fe-react-query/query-options.md`
- For testing query hooks → `fe-react-query/custom-hooks.md`
