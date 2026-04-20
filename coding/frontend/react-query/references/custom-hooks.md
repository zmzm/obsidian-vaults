---
id: frontend/react-query/custom-hooks
name: frontend/react-query/custom-hooks
kind: reference
domain: frontend
topics: [react-query, custom hooks]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Custom Hooks Pattern

## When to use

Use this document when:

- Extracting React Query logic to custom hooks
- Creating reusable data fetching hooks
- Building mutation hooks with side effects
- Testing React Query hooks

## Rules

- Extract query logic to custom hooks
- Extract mutation logic to custom hooks
- Include cache invalidation in mutation hooks
- Return consistent interfaces from hooks
- Handle loading, error, and success states
- Prefer returning an extracted interface instead of the raw mutation/query object when that improves clarity for consumers

## Examples

### Good example

```typescript
// Extract Query Logic
// hooks/useCourses.hook.ts
export const useCourses = (filters?: CourseFilters) => {
  return useQuery({
    queryKey: ['courses', filters],
    queryFn: async () => {
      const response = await apiClient.get('/courses', { params: filters });
      return response.data;
    },
  });
};

// Extract Mutation Logic
// hooks/useCreateCourse.hook.ts
export const useCreateCourse = () => {
  const queryClient = useQueryClient();
  const { toast } = useToast();
  const { t } = useTranslation('courses');

  return useMutation({
    mutationFn: async (data: CreateCourseDto) => {
      const response = await apiClient.post('/courses', data);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['courses'] });
      toast({ title: t('success.created') });
    },
    onError: (error: any) => {
      toast({
        title: t('error.createFailed'),
        description: error.message,
        variant: 'destructive',
      });
    },
  });
};
```

### Bad example

```typescript
// ❌ Bad: Query logic in component
export const CoursesList = () => {
  const { data } = useQuery({
    queryKey: ['courses'],
    queryFn: fetchCourses,
  });
  // Should be in custom hook
};

// ❌ Bad: Not extracting mutation logic
export const CreateCourseForm = () => {
  const queryClient = useQueryClient();
  const mutation = useMutation({...});
  // Should be in custom hook
};
```

## Anti-patterns

- Keeping query logic in components
- Not extracting mutation logic to hooks
- Missing cache invalidation in mutation hooks
- Inconsistent return interfaces
- Not handling loading/error states

## Notes

### Testing with React Query

```typescript
import { QueryClient, QueryClientProvider } from '@tanstack/react-query';
import { renderHook, waitFor } from '@testing-library/react';

const createWrapper = () => {
  const queryClient = new QueryClient({
    defaultOptions: {
      queries: { retry: false },
      mutations: { retry: false },
    },
  });
  return ({ children }: { children: React.ReactNode }) => <QueryClientProvider client={queryClient}>{children}</QueryClientProvider>;
};

it('should fetch courses successfully', async () => {
  const { result } = renderHook(() => useCourses(), {
    wrapper: createWrapper(),
  });
  await waitFor(() => expect(result.current.isSuccess).toBe(true));
  expect(result.current.data).toHaveLength(3);
});
```

### Hook Organization

- Place hooks in feature directories or shared/hooks
- Co-locate hooks with components when feature-specific
- Use `.hook.ts` extension for hook files
- Return consistent interfaces (data, isLoading, error, etc.)

### Benefits

- Reusability across components
- Easier testing
- Separation of concerns
- Consistent data fetching patterns
- Centralized error handling

### Mutation Hook Return Pattern

When wrapping mutations, prefer returning a clear consumer-facing API instead of leaking the entire raw mutation object.

```typescript
export const useCreateCourse = () => {
  const mutation = useMutation({ /* ... */ });

  return {
    createCourse: mutation.mutate,
    createCourseAsync: mutation.mutateAsync,
    isPending: mutation.isPending,
    isError: mutation.isError,
    isSuccess: mutation.isSuccess,
    error: mutation.error,
  };
};
```
