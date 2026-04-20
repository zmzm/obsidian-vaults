---
id: frontend/react-query/advanced-patterns
name: frontend/react-query/advanced-patterns
kind: reference
domain: frontend
topics: [react-query, advanced patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Advanced React Query Patterns

## When to use

Use this document when:

- Implementing pagination with React Query
- Creating infinite scroll functionality
- Implementing optimistic updates
- Working with dependent queries

## Rules

- Use `placeholderData` for smooth pagination transitions
- Use `useInfiniteQuery` for infinite scroll
- Implement optimistic updates with `onMutate`, `onError`, `onSettled`
- Use `enabled` option for dependent queries
- Cancel queries in `onMutate` to prevent race conditions

## Examples

### Good example

```typescript
// Pagination
export const usePaginatedCourses = (page: number = 1, limit: number = 10) => {
  return useQuery({
    queryKey: ['courses', { page, limit }],
    queryFn: async () => {
      const response = await apiClient.get('/courses', {
        params: { page, limit },
      });
      return response.data;
    },
    placeholderData: previousData => previousData,
  });
};

// Infinite Queries
import { useInfiniteQuery } from '@tanstack/react-query';

export const useInfiniteCourses = () => {
  return useInfiniteQuery({
    queryKey: ['courses', 'infinite'],
    queryFn: async ({ pageParam = 1 }) => {
      const response = await apiClient.get('/courses', {
        params: { page: pageParam, limit: 10 },
      });
      return response.data;
    },
    getNextPageParam: (lastPage, pages) => {
      return lastPage.hasMore ? pages.length + 1 : undefined;
    },
    initialPageParam: 1,
  });
};

// Optimistic Updates
export const useUpdateCourse = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async ({ id, data }: { id: string; data: UpdateCourseDto }) => {
      const response = await apiClient.patch(`/courses/${id}`, data);
      return response.data;
    },
    onMutate: async ({ id, data }) => {
      await queryClient.cancelQueries({ queryKey: ['courses', id] });
      const previousCourse = queryClient.getQueryData(['courses', id]);
      queryClient.setQueryData(['courses', id], (old: any) => ({
        ...old,
        ...data,
      }));
      return { previousCourse };
    },
    onError: (_err, _variables, context) => {
      if (context?.previousCourse) {
        queryClient.setQueryData(['courses', id], context.previousCourse);
      }
    },
    onSettled: (_data, _error, { id }) => {
      queryClient.invalidateQueries({ queryKey: ['courses', id] });
    },
  });
};

// Dependent Queries
export const useCourseWithAssignments = (courseId: string) => {
  const { data: course } = useQuery({
    queryKey: ['courses', courseId],
    queryFn: async () => {
      const response = await apiClient.get(`/courses/${courseId}`);
      return response.data;
    },
  });

  const { data: assignments } = useQuery({
    queryKey: ['courses', courseId, 'assignments'],
    queryFn: async () => {
      const response = await apiClient.get(`/courses/${courseId}/assignments`);
      return response.data;
    },
    enabled: !!course, // Only run if course exists
  });

  return { course, assignments };
};
```

### Bad example

```typescript
// ❌ Bad: Not using placeholderData for pagination
export const usePaginatedCourses = (page: number) => {
  return useQuery({
    queryKey: ['courses', page],
    queryFn: async () => { ... },
    // Missing placeholderData - causes loading state on every page change
  });
};

// ❌ Bad: Not canceling queries in optimistic update
onMutate: async ({ id, data }) => {
  // Missing cancelQueries - race condition possible
  queryClient.setQueryData(['courses', id], data);
};
```

## Anti-patterns

- Not using placeholderData for pagination
- Not canceling queries in optimistic updates
- Not rolling back optimistic updates on error
- Not using enabled for dependent queries
- Missing initialPageParam in infinite queries

## Notes

### Pagination

- Use `placeholderData` to show previous data while loading next page
- Include page and limit in query key
- Smooth transitions between pages

### Infinite Queries

- Use `useInfiniteQuery` for infinite scroll
- Implement `getNextPageParam` to determine next page
- Use `initialPageParam` (required in v5+)
- Access pages via `data.pages` array

### Optimistic Updates

- Cancel queries in `onMutate` to prevent race conditions
- Save previous data for rollback
- Update cache optimistically
- Roll back on error using previous data
- Invalidate on settle to sync with server

### Dependent Queries

- Use `enabled` option to control when query runs
- Only run dependent query when prerequisite data exists
- Prevents unnecessary API calls
