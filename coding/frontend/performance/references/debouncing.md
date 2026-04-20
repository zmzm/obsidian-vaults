---
id: frontend/performance/debouncing
name: frontend/performance/debouncing
kind: reference
domain: frontend
topics: [performance, debouncing]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Debouncing Input

## When to use

Use this document when:

- Implementing search inputs
- Handling filter inputs
- Reducing API calls from user input
- Optimizing input-related performance

## Rules

- Debounce search inputs (300-500ms typical)
- Debounce filter inputs
- Use throttle for scroll/resize handlers (not debounce)
- Extract debounce logic to custom hook
- Clear timeout on unmount

## Examples

### Good example

```typescript
// ✅ Good: Debounce search
import { useDebounce } from '@/shared/hooks/useDebounce.hook';

export const SearchCourses: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');
  const debouncedSearch = useDebounce(searchTerm, 300);

  const { data: results } = useQuery({
    queryKey: ['courses', 'search', debouncedSearch],
    queryFn: () => searchCourses(debouncedSearch),
    enabled: !!debouncedSearch,
  });

  return <Input value={searchTerm} onChange={e => setSearchTerm(e.target.value)} />;
};

// useDebounce Hook
// useDebounce.hook.ts
import { useState, useEffect } from 'react';

export const useDebounce = <T>(value: T, delay: number = 500): T => {
  const [debouncedValue, setDebouncedValue] = useState<T>(value);

  useEffect(() => {
    const handler = setTimeout(() => {
      setDebouncedValue(value);
    }, delay);
    return () => clearTimeout(handler);
  }, [value, delay]);

  return debouncedValue;
};
```

### Bad example

```typescript
// ❌ Bad: Not debouncing search
export const SearchCourses: React.FC = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const { data: results } = useQuery({
    queryKey: ['courses', 'search', searchTerm],
    queryFn: () => searchCourses(searchTerm),
    // Triggers on every keystroke
  });
};

// ❌ Bad: Not cleaning up timeout
export const useDebounce = (value: any, delay: number) => {
  const [debounced, setDebounced] = useState(value);
  useEffect(() => {
    setTimeout(() => setDebounced(value), delay);
    // Missing cleanup
  }, [value, delay]);
};
```

## Anti-patterns

- Not debouncing search inputs
- Not debouncing filter inputs
- Using debounce for scroll handlers (should use throttle)
- Not cleaning up timeouts
- Debouncing with too short delay (causes too many calls)

## Notes

### When to Debounce

- Search inputs (300-500ms typical)
- Filter inputs
- Any input that triggers API calls or expensive operations

### When to Throttle (Not Debounce)

- Scroll handlers
- Resize handlers
- Mouse move handlers
- Throttle executes at regular intervals, debounce waits for pause

### Debounce Hook

- Extract to custom hook for reusability
- Always clean up timeout on unmount
- Use TypeScript generics for type safety
- Default delay of 500ms is reasonable starting point
