---
id: fe-ui/components
name: fe-ui/components
kind: reference
domain: frontend-ui
topics: [components]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# Component Usage Examples

## When to use

Use this document when:

- Using Button, Card, Alert, Toast, and Dialog components
- Understanding component variants and sizes
- Implementing user feedback (alerts, toasts)
- Creating modal dialogs

## Rules

- Always import from `@mentory/ui-components`
- Use appropriate variants for buttons (default, destructive, outline, etc.)
- Use appropriate sizes (sm, default, lg)
- Handle disabled states properly
- Use toasts for non-blocking feedback
- Use dialogs for modal interactions

## Examples

### Good example

```typescript
import { Button } from '@mentory/ui-components';

// Variants
<Button variant="default">{t('save')}</Button>
<Button variant="destructive">{t('delete')}</Button>
<Button variant="outline">{t('cancel')}</Button>
<Button variant="secondary">{t('edit')}</Button>
<Button variant="ghost">{t('viewDetails')}</Button>
<Button variant="link">{t('learnMore')}</Button>

// Sizes
<Button size="sm">{t('small')}</Button>
<Button size="default">{t('default')}</Button>
<Button size="lg">{t('large')}</Button>

// Disabled state
<Button disabled>{t('loading')}</Button>

// Card Component
import { Card } from '@mentory/ui-components';

export function CourseCard({ course }: { course: Course }) {
  const { t } = useI18n();
  return (
    <Card>
      <h3>{course.title}</h3>
      <p>{course.description}</p>
      <Button onClick={() => enroll(course.id)}>{t('enroll')}</Button>
    </Card>
  );
}

// Alert Component
import { Alert } from '@mentory/ui-components';

// Error alert
<Alert status="error">
  <AlertTitle>{t('error.title')}</AlertTitle>
  <AlertDescription>{error.message}</AlertDescription>
</Alert>

// Success alert
<Alert status="success">
  <AlertTitle>{t('success.title')}</AlertTitle>
  <AlertDescription>{t('success.message')}</AlertDescription>
</Alert>

// Toast Notifications
import { useToast } from '@mentory/ui-components';

export function MyComponent() {
  const toast = useToast();
  const handleSuccess = () => {
    toast({
      title: t('success.title'),
      description: t('success.message'),
      status: 'success',
      duration: 5000,
      isClosable: true,
    });
  };
  return <Button onClick={handleSuccess}>{t('showToast')}</Button>;
}

// Dialog (Modal) Component
import { Dialog, Button } from '@mentory/ui-components';

export function DeleteConfirmation() {
  const [isOpen, setIsOpen] = useState(false);
  return (
    <>
      <Button variant="destructive" onClick={() => setIsOpen(true)}>
        {t('delete')}
      </Button>
      <Dialog isOpen={isOpen} onClose={() => setIsOpen(false)}>
        <h2>{t('confirmDelete.title')}</h2>
        <p>{t('confirmDelete.message')}</p>
        <Button variant="outline" onClick={() => setIsOpen(false)}>
          {t('cancel')}
        </Button>
        <Button variant="destructive" onClick={handleDelete}>
          {t('confirm')}
        </Button>
      </Dialog>
    </>
  );
}
```

### Bad example

```typescript
// ❌ Bad: Importing from Chakra UI directly
import { Button } from '@chakra-ui/react';

// ❌ Bad: Using wrong variant
<Button variant="danger">{t('delete')}</Button> // Should be "destructive"

// ❌ Bad: Not handling disabled state
<Button onClick={handleClick}>{t('submit')}</Button> // Should disable when loading
```

## Anti-patterns

- Importing directly from `@chakra-ui/*` packages
- Using wrong variant names
- Not handling disabled states
- Not using appropriate sizes
- Mixing UI libraries

## Notes

- Always import from `@mentory/ui-components`, never from `@chakra-ui/*`
- Button variants: default, destructive, outline, secondary, ghost, link
- Button sizes: sm, default, lg
- Use toasts for non-blocking feedback
- Use dialogs for modal interactions requiring user confirmation
- See display-components.md for Avatar, Badge, and Skeleton examples
