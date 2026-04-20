---
id: frontend/performance/re-render-optimization
name: frontend/performance/re-render-optimization
kind: reference
domain: frontend
topics: [performance, re render optimization]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Re-render Optimization

## When to use

Use this document when:

- Reducing unnecessary component re-renders
- Optimizing list rendering
- Preventing prop reference changes
- Configuring React Query for optimal re-renders

## Rules

- Avoid inline objects in props (creates new reference)
- Avoid inline functions in props (creates new reference)
- Use useCallback for stable function references
- Use React.memo for components that receive same props
- Configure React Query staleTime to reduce refetches
- Use stable keys in lists

## Examples

### Good example

```typescript
// ✅ Good: Use static object
const cardStyle = { padding: 16 };
<UserCard user={user} style={cardStyle} />;

// ✅ Good: Use useCallback or stable reference
const handleEnroll = useCallback(
  (id: string) => {
    enroll(id);
  },
  [enroll],
);
<CourseCard course={course} onEnroll={handleEnroll} />;

// ✅ Good: Configure React Query staleTime
useQuery({
  queryKey: ['courses'],
  queryFn: fetchCourses,
  staleTime: 5 * 60 * 1000, // 5 minutes
});

// ✅ Good: Use stable keys
{
  courses.map(course => <CourseCard key={course.id} course={course} />);
}

// ✅ Good: Virtualization for long lists
import { useVirtualizer } from '@tanstack/react-virtual';
```

### Bad example

```typescript
// ❌ Bad: Creates new object on every render
<UserCard user={user} style={{ padding: 16 }} />

// ❌ Bad: Creates new function on every render
<CourseCard course={course} onEnroll={(id) => enroll(id)} />

// ❌ Bad: Using index as key
{courses.map((course, index) => (
  <CourseCard key={index} course={course} />
))}
```

## Anti-patterns

- Inline objects in props (creates new reference)
- Inline functions in props (creates new reference)
- Using index as React key
- Not configuring React Query staleTime
- Not using virtualization for long lists

## Notes

### Avoid Inline Objects

- Inline objects create new references on every render
- Causes memoized components to re-render unnecessarily
- Extract to constants or use useMemo

### Avoid Inline Functions

- Inline functions create new references on every render
- Causes memoized components to re-render unnecessarily
- Use useCallback for stable function references

### React Query Configuration

- Configure `staleTime` to reduce unnecessary refetches
- Reduces re-renders from query updates
- Balance between freshness and performance

### List Optimization

- Use stable keys (not index)
- Use virtualization for very long lists (>1000 items)
- Consider pagination instead of infinite scroll
- Use React.memo for list items when appropriate
