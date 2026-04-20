---
id: frontend/error-handling/toast-notifications
name: frontend/error-handling/toast-notifications
kind: reference
domain: frontend
topics: [error-handling, toast notifications]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Toast Notifications

## When to use

Use this document when:

- Showing success/error feedback to users
- Handling API response feedback
- Notifying users of action results

## Rules

- Use toast for transient feedback (success, error, info)
- Use `variant: 'destructive'` for errors
- Use i18n for all toast messages
- Keep messages concise and actionable
- Don't overuse toasts (avoid toast spam)

## Examples

### Good example

```typescript
// ✅ Good: Success toast
import { useToast } from '@/shared/hooks/useToast';
import { useI18n } from '@/shared/hooks/useI18n';

const MyComponent = () => {
  const { toast } = useToast();
  const { t } = useI18n();

  const handleSave = async () => {
    try {
      await saveData();
      toast({
        title: t('common:saved'),
        description: t('profile:savedDescription'),
      });
    } catch {
      toast({
        title: t('common:error'),
        description: t('profile:saveError'),
        variant: 'destructive',
      });
    }
  };
};

// ✅ Good: Error toast in mutation
const updateMutation = useMutation({
  mutationFn: updateProfile,
  onSuccess: () => {
    toast({ title: t('profile:updated') });
  },
  onError: () => {
    toast({
      title: t('profile:updateError'),
      variant: 'destructive',
    });
  },
});
```

### Bad example

```typescript
// ❌ Bad: Hardcoded message
toast({ title: 'Profile saved!' });

// ❌ Bad: Technical error message
catch (error) {
  toast({ title: error.message }); // May expose internals
}

// ❌ Bad: No variant for error
toast({ title: t('error') }); // Missing variant: 'destructive'

// ❌ Bad: Toast spam
items.forEach(item => {
  toast({ title: `Saved ${item.name}` }); // Too many toasts
});
```

## Toast API

```typescript
const { toast } = useToast();

toast({
  title: string, // Required: Main message
  description: string, // Optional: Additional detail
  variant: 'default' | 'destructive', // Style variant
});
```

## Patterns

### Success after mutation

```typescript
const onSubmit = async (data: FormData) => {
  try {
    await mutation.mutateAsync(data);
    toast({
      title: t('common:saved'),
      description: t('form:savedDescription'),
    });
  } catch {
    toast({
      title: t('common:error'),
      description: t('form:saveError'),
      variant: 'destructive',
    });
  }
};
```

### Error-only toast

When success is obvious (e.g., navigation happens), only show error:

```typescript
const handleDelete = async (id: string) => {
  try {
    await deleteMutation.mutateAsync(id);
    // No toast - user sees item disappear
  } catch {
    toast({
      title: t('common:deleteError'),
      variant: 'destructive',
    });
  }
};
```

### With React Query onError

```typescript
useMutation({
  mutationFn: createItem,
  onError: () => {
    toast({
      title: t('item:createError'),
      description: t('item:tryAgain'),
      variant: 'destructive',
    });
  },
});
```

## Notes

### When to Show Toast

| Action                | Show Toast                |
| --------------------- | ------------------------- |
| Save/Update success   | Yes                       |
| Delete success        | Optional (if not obvious) |
| API error             | Yes (destructive)         |
| Form validation error | No (use field errors)     |
| Background sync       | Only on error             |

### Toast vs Inline Error

| Use Toast          | Use Inline Error      |
| ------------------ | --------------------- |
| Transient feedback | Persistent validation |
| Action result      | Field-specific errors |
| Global errors      | Form-level errors     |
