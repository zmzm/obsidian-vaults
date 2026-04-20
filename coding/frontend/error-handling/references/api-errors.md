---
id: frontend/error-handling/api-errors
name: frontend/error-handling/api-errors
kind: reference
domain: frontend
topics: [error-handling, api errors]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# API Error Handling

## When to use

Use this document when:

- Handling API call failures
- Implementing error responses in mutations
- Showing API errors to users

## Rules

- Handle all API errors with try/catch or onError
- Never expose raw API error messages to users
- Use i18n for error messages
- Log detailed errors for debugging
- Show user-friendly messages via toast

## Examples

### Good example

```typescript
// ✅ Good: Try/catch with toast
const onSubmit = async (data: ProfileFormData) => {
  try {
    await updateProfileMutation.mutateAsync(data);
    toast({
      title: t('user:profileUpdated'),
      description: t('user:profileUpdatedDescription'),
    });
    return true;
  } catch {
    toast({
      title: t('user:profileUpdateError'),
      description: t('user:profileUpdateErrorDescription'),
      variant: 'destructive',
    });
    return false;
  }
};

// ✅ Good: React Query onError
const mutation = useMutation({
  mutationFn: createCourse,
  onSuccess: () => {
    toast({ title: t('course:created') });
    queryClient.invalidateQueries({ queryKey: ['courses'] });
  },
  onError: error => {
    console.error('Create course failed:', error);
    toast({
      title: t('course:createError'),
      variant: 'destructive',
    });
  },
});

// ✅ Good: Handling specific error types
const handleApiError = (error: unknown) => {
  if (error instanceof ApiError) {
    if (error.status === 404) {
      toast({ title: t('error:notFound'), variant: 'destructive' });
    } else if (error.status === 403) {
      toast({ title: t('error:forbidden'), variant: 'destructive' });
    } else {
      toast({ title: t('error:general'), variant: 'destructive' });
    }
  } else {
    toast({ title: t('error:unexpected'), variant: 'destructive' });
  }
};
```

### Bad example

```typescript
// ❌ Bad: Exposing raw error
catch (error) {
  toast({ title: error.message }); // May expose "TypeError: x is undefined"
}

// ❌ Bad: No error handling
await mutation.mutateAsync(data); // May throw unhandled

// ❌ Bad: Silent failure
catch (error) {
  console.log(error); // User doesn't know it failed
}

// ❌ Bad: Hardcoded message
catch {
  toast({ title: 'Something went wrong' }); // Not translated
}
```

## Patterns

### Mutation with full error handling

```typescript
export function useCreateCourse() {
  const { toast } = useToast();
  const { t } = useI18n();
  const queryClient = useQueryClient();

  return useMutation({
    mutationFn: (data: CreateCourseDto) => api.courses.create(data),
    onSuccess: () => {
      toast({ title: t('course:created') });
      queryClient.invalidateQueries({ queryKey: ['courses'] });
    },
    onError: error => {
      console.error('Create course failed:', error);
      toast({
        title: t('course:createError'),
        description: t('course:tryAgain'),
        variant: 'destructive',
      });
    },
  });
}
```

### Form submission with error return

```typescript
const onSubmit = async (data: FormData): Promise<boolean> => {
  try {
    await mutation.mutateAsync(data);
    toast({ title: t('form:success') });
    return true;
  } catch {
    toast({ title: t('form:error'), variant: 'destructive' });
    return false;
  }
};

// Usage
const success = await onSubmit(data);
if (success) {
  navigate(ROUTES.DASHBOARD);
}
```

## Notes

### Error Response Handling

| Status | User Message                         |
| ------ | ------------------------------------ |
| 400    | Validation error - check form fields |
| 401    | Session expired - please sign in     |
| 403    | Not authorized                       |
| 404    | Not found                            |
| 500    | Server error - try again later       |

### Logging vs Displaying

```typescript
catch (error) {
  // Log full error for debugging
  console.error('API call failed:', error);

  // Show user-friendly message
  toast({
    title: t('error:general'),
    variant: 'destructive',
  });
}
```
