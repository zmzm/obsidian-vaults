---
id: frontend/react-query/mutations
name: frontend/react-query/mutations
kind: reference
domain: frontend
topics: [react-query, mutations]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# useMutation for Modifying Data

## When to use

Use this document when:

- Implementing POST, PATCH, DELETE operations
- Creating mutation hooks with cache invalidation
- Handling mutation success and error states
- Adding toast notifications to mutations

## Rules

- Use `useMutation` for all data modifications (POST, PATCH, DELETE)
- Always invalidate queries after successful mutations
- Use `apiClient` for network requests
- Handle success and error states with callbacks
- Return mutation functions and state from hooks

## Examples

### Good example

```typescript
import { useMutation, useQueryClient } from '@tanstack/react-query';
import { apiClient } from '@/shared/api/apiClient';

// Basic Mutation
export const useCreateCourse = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (data: CreateCourseDto) => {
      const response = await apiClient.post('/courses', data);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['courses'] });
    },
  });
};

// Mutation with Toast
const { mutate: createCourse, isPending, isError } = useCreateCourse();

const handleSubmit = (data: CreateCourseDto) => {
  createCourse(data, {
    onSuccess: newCourse => {
      toast.success(t('courseCreated'));
      navigate(`/courses/${newCourse.id}`);
    },
    onError: error => {
      toast.error(t('createFailed'));
    },
  });
};

// Update Mutation
export const useUpdateCourse = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async ({ id, data }: { id: string; data: UpdateCourseDto }) => {
      const response = await apiClient.patch(`/courses/${id}`, data);
      return response.data;
    },
    onSuccess: (_, variables) => {
      queryClient.invalidateQueries({ queryKey: ['courses', variables.id] });
    },
  });
};

// Delete Mutation
export const useDeleteCourse = () => {
  const queryClient = useQueryClient();
  return useMutation({
    mutationFn: async (id: string) => {
      const response = await apiClient.delete(`/courses/${id}`);
      return response.data;
    },
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['courses'] });
    },
  });
};
```

### Bad example

```typescript
// ❌ Bad: Not invalidating queries after mutation
export const useCreateCourse = () => {
  return useMutation({
    mutationFn: async (data) => {
      return apiClient.post('/courses', data);
    },
    // Missing onSuccess with invalidation
  });
};

// ❌ Bad: Not handling errors
export const useCreateCourse = () => {
  return useMutation({
    mutationFn: async (data) => { ... },
    // Missing onError handler
  });
};
```

## Anti-patterns

- Not invalidating queries after mutations
- Missing error handling in mutations
- Not using apiClient for network requests
- Not providing user feedback (toasts)
- Returning mutation object directly instead of extracted values

## Notes

- Always invalidate related queries after successful mutations
- Use `onSuccess` to invalidate queries and show success feedback
- Use `onError` to handle errors and show error feedback
- Return mutation functions and state for easy component usage
- Invalidate both specific and list queries when updating resources
