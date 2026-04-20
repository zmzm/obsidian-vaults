---
id: frontend/react-query/cache-invalidation
name: frontend/react-query/cache-invalidation
kind: reference
domain: frontend
topics: [react-query, cache invalidation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Cache Invalidation

## When to use

Use this document when:

- Invalidating queries after mutations
- Understanding when to invalidate cache
- Using selective invalidation patterns
- Keeping cache in sync with server state

## Rules

- Always invalidate queries after successful mutations
- Invalidate both list and specific resource queries when updating
- Use selective invalidation for precise cache updates
- Invalidate nested resources when parent changes
- Use `exact` option for precise matching when needed

## Examples

### Good example

```typescript
const queryClient = useQueryClient();

// After creating
onSuccess: () => {
  queryClient.invalidateQueries({ queryKey: ['courses'] });
};

// After updating
onSuccess: updatedCourse => {
  queryClient.invalidateQueries({ queryKey: ['courses'] });
  queryClient.invalidateQueries({ queryKey: ['courses', updatedCourse.id] });
};

// After deleting
onSuccess: () => {
  queryClient.invalidateQueries({ queryKey: ['courses'] });
};

// Invalidate all courses queries
queryClient.invalidateQueries({ queryKey: ['courses'] });

// Invalidate specific course
queryClient.invalidateQueries({ queryKey: ['courses', courseId] });

// Invalidate nested resource
queryClient.invalidateQueries({ queryKey: ['courses', courseId, 'assignments'] });

// Only invalidate exact match
queryClient.invalidateQueries({
  queryKey: ['courses'],
  exact: true,
});

// Invalidate all queries starting with 'courses'
queryClient.invalidateQueries({
  predicate: query => query.queryKey[0] === 'courses',
});
```

### Bad example

```typescript
// ❌ Bad: Not invalidating after mutation
onSuccess: () => {
  // Missing invalidation - cache will be stale
};

// ❌ Bad: Invalidating wrong queries
onSuccess: () => {
  queryClient.invalidateQueries({ queryKey: ['users'] }); // Wrong key
};
```

## Anti-patterns

- Not invalidating queries after mutations
- Invalidating wrong query keys
- Not invalidating both list and specific queries
- Forgetting to invalidate nested resources
- Over-invalidating (invalidating too many queries)

## Notes

### When to Invalidate

- After creating: Invalidate list queries
- After updating: Invalidate both list and specific resource queries
- After deleting: Invalidate list queries
- When related data changes: Invalidate nested resources

### Invalidation Patterns

- `['courses']` - Invalidates all queries starting with 'courses'
- `['courses', id]` - Invalidates specific course query
- `['courses', id, 'assignments']` - Invalidates nested resource
- Use `exact: true` for precise matching
- Use `predicate` for complex invalidation logic

### Selective Invalidation

- Use `exact: true` to match only exact query key
- Use `predicate` function for custom matching logic
- Balance between precise and broad invalidation
