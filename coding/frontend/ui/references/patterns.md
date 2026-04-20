---
id: fe-ui/patterns
name: fe-ui/patterns
kind: reference
domain: frontend-ui
topics: [patterns]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# Common UI Patterns

## When to use

Use this document when:

- Implementing loading, empty, and error states
- Creating conditional rendering patterns
- Building list displays
- Handling component states

## Rules

- Always handle loading states with Skeleton
- Always handle empty states with helpful messages
- Always handle error states with Alert
- Use conditional rendering for state management
- Provide clear user feedback for all states

## Examples

### Good example

```typescript
// Loading State
import { Skeleton } from '@mentory/ui-components';

if (isLoading) {
  return (
    <div>
      <Skeleton height="200px" />
      <Skeleton height="24px" />
      <Skeleton height="16px" />
    </div>
  );
}

// Empty State
import { Button } from '@mentory/ui-components';

if (courses.length === 0) {
  return (
    <div>
      <h3>{t('noCourses.title')}</h3>
      <p>{t('noCourses.description')}</p>
      <Button onClick={onCreate}>{t('createFirstCourse')}</Button>
    </div>
  );
}

// Error State
import { Alert } from '@mentory/ui-components';

if (isError) {
  return (
    <Alert status="error">
      <AlertTitle>{t('error.title')}</AlertTitle>
      <AlertDescription>{error.message}</AlertDescription>
    </Alert>
  );
}

// Success State
import { Alert } from '@mentory/ui-components';

<Alert status="success">
  <AlertTitle>{t('success.title')}</AlertTitle>
  <AlertDescription>{t('success.message')}</AlertDescription>
</Alert>;

// Conditional Rendering
{
  user && <UserProfile user={user} />;
}

{
  isAdmin && <AdminPanel />;
}

// List Patterns
{
  courses.map(course => <CourseCard key={course.id} course={course} />);
}
```

### Bad example

```typescript
// ❌ Bad: Not handling loading state
return <div>{data.map(...)}</div>; // What if data is undefined?

// ❌ Bad: Not handling empty state
return <div>{items.map(...)}</div>; // What if items is empty?

// ❌ Bad: Not handling error state
return <div>{data.title}</div>; // What if there's an error?
```

## Anti-patterns

- Not handling loading states
- Not handling empty states
- Not handling error states
- Not providing user feedback
- Rendering undefined data

## Notes

- Always handle all possible states: loading, error, empty, success
- Use Skeleton for loading states to match content structure
- Provide helpful empty states with actionable next steps
- Display clear error messages with recovery options
- Use conditional rendering to manage component states
- Always check for data existence before rendering
