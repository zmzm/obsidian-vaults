---
id: frontend/react-query/query-options
name: frontend/react-query/query-options
kind: reference
domain: frontend
topics: [react-query, query options]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Query Options

## When to use

Use this document when:

- Configuring query caching behavior
- Setting up refetch strategies
- Handling retries and error recovery
- Making queries conditional

## Rules

- Configure `staleTime` based on data freshness needs
- Configure `gcTime` (formerly cacheTime) for cache retention
- Use `enabled` for conditional queries
- Configure retry logic based on error types
- Set appropriate refetch options

## Examples

### Good example

```typescript
useQuery({
  queryKey: ['courses'],
  queryFn: fetchCourses,

  // Caching
  staleTime: 5 * 60 * 1000,        // Data considered fresh for 5 min
  gcTime: 10 * 60 * 1000,          // Keep in cache for 10 min

  // Refetching
  refetchOnWindowFocus: true,      // Refetch when window regains focus
  refetchOnMount: true,            // Refetch on component mount
  refetchOnReconnect: true,        // Refetch on network reconnect

  // Retries
  retry: 3,                        // Retry failed requests 3 times
  retryDelay: (attemptIndex) => Math.min(1000 * 2 ** attemptIndex, 30000),

  // Conditional
  enabled: !!userId,               // Only run if userId exists
});

// Error Handling with Custom Retry
export const useCourse = (id: string) => {
  return useQuery({
    queryKey: ['courses', id],
    queryFn: async () => {
      const response = await apiClient.get(`/courses/${id}`);
      return response.data;
    },
    retry: (failureCount, error: any) => {
      // Don't retry on 404
      if (error?.response?.status === 404) {
        return false;
      }
      // Retry up to 3 times for other errors
      return failureCount < 3;
    },
  });
};

// Stale Time Configuration
// Frequently changing data - short stale time
staleTime: 0, // Always refetch

// Stable data - longer stale time
staleTime: 5 * 60 * 1000, // 5 minutes

// Very stable data - very long stale time
staleTime: 30 * 60 * 1000, // 30 minutes
```

### Bad example

```typescript
// ❌ Bad: Not configuring staleTime
useQuery({
  queryKey: ['courses'],
  queryFn: fetchCourses,
  // Missing staleTime - refetches too often
});

// ❌ Bad: Retrying on 404 errors
retry: 3, // Should not retry 404s
  // ❌ Bad: Not using enabled for conditional queries
  useQuery({
    queryKey: ['user', userId],
    queryFn: fetchUser,
    // Missing enabled - runs even if userId is undefined
  });
```

## Anti-patterns

- Not configuring staleTime (causes excessive refetches)
- Retrying on non-retryable errors (404, 401)
- Not using enabled for conditional queries
- Setting staleTime too high for frequently changing data
- Not configuring retry logic appropriately
- Using `useEffect` for ordinary server-state fetching instead of query primitives
- Mixing query key formats or omitting important parameters from keys

## Notes

### Caching Options

- `staleTime`: How long data is considered fresh (default: 0)
- `gcTime`: How long unused data stays in cache (default: 5 minutes)
- Longer staleTime = fewer refetches but potentially stale data
- Balance between freshness and performance

### Refetch Options

- `refetchOnWindowFocus`: Refetch when window regains focus (default: true)
- `refetchOnMount`: Refetch on component mount (default: true)
- `refetchOnReconnect`: Refetch on network reconnect (default: true)
- Disable these for stable data to reduce unnecessary requests

### Retry Configuration

- `retry`: Number of retries or function returning boolean
- `retryDelay`: Function calculating delay between retries
- Don't retry on 404 (not found) or 401 (unauthorized)
- Use exponential backoff for retry delays

### Conditional Queries

- Use `enabled` option to control when query runs
- Prevents queries from running with invalid parameters
- Useful for dependent queries
