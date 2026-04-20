---
id: frontend/coding/patterns
name: frontend/coding/patterns
kind: reference
domain: frontend
topics: [coding, patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Common Patterns

## When to use

Use this document when:

- Writing React components
- Handling conditional rendering
- Rendering lists or handling events
- Managing loading, error, and empty states

## Rules

- Use early returns for conditional rendering
- Use unique stable keys for list items (not index)
- Use named event handlers instead of inline functions
- Handle loading, error, and empty states explicitly
- Keep component logic simple and readable

## Examples

### Good example

```typescript
// ✅ Good: Early returns
if (isLoading) return <LoadingSpinner />;
if (error) return <ErrorMessage error={error} />;
if (!data) return <EmptyState />;
return <DataDisplay data={data} />;

// ✅ Good: Unique stable keys
{
  users.map(user => <UserCard key={user.id} user={user} />);
}

// ✅ Good: Named handlers
const handleSubmit = (e: React.FormEvent) => {
  e.preventDefault();
  onSubmit(formData);
};
return <form onSubmit={handleSubmit}>...</form>;

// ✅ Good: Loading states
if (isLoading) {
  return <LoadingSpinner />; // Use appropriate loading component
}

// ✅ Good: Error states
if (error) {
  return <ErrorMessage error={error} />; // Use appropriate error component
}

// ✅ Good: Empty states
if (!data || data.length === 0) {
  return <EmptyState message={t('noData')} />; // Use appropriate empty state component
}
```

### Bad example

```typescript
// ❌ Bad: Index as key
{
  users.map((user, index) => <UserCard key={index} user={user} />);
}

// ❌ Bad: Inline arrow functions in JSX
<form onSubmit={(e) => { e.preventDefault(); onSubmit(formData); }}>

// ❌ Bad: Not handling states
return <DataDisplay data={data} />; // What if data is undefined?
```

## Anti-patterns

- Using array index as React key
- Inline arrow functions in JSX props
- Not handling loading/error/empty states
- Complex conditional rendering logic
- Mixing business logic with rendering

## Notes

- Early returns make code more readable and reduce nesting
- Stable keys help React efficiently update lists
- Named handlers are easier to test and debug
- Always handle all possible states (loading, error, empty, success)
- Keep conditional rendering simple and predictable
- For specific UI component usage (Skeleton, Alert, etc.), see the UI skill
- This skill focuses on general React patterns, not specific component APIs
