---
id: frontend/hook/principles
name: frontend/hook/principles
kind: reference
domain: frontend
topics: [hook, core principles]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Hook Principles

## When to use

Use this document when:

- Creating custom React hooks
- Extracting reusable logic from components
- Defining hook naming conventions and file structure
- Deciding return value patterns for hooks

## Rules

- Start hook names with "use" prefix
- Name hook files with ".hook.ts" extension (not .tsx)
- Return typed values with clear interfaces
- Keep hooks focused on single responsibility
- Extract reusable logic from components into hooks
- Follow React's Rules of Hooks (only call at top level)
- Use named object returns for 3+ values
- Use array returns for exactly 2 values (like useState)
- Compose multiple hooks for complex logic
- Define return type interfaces for clarity
- Extract React Query logic into custom hooks
- Keep hooks pure and testable

## Examples

### Good example

```typescript
// useUserProfile.hook.ts
import { useQuery } from '@tanstack/react-query';
import { apiClient } from '@/shared/api/apiClient';

interface UseUserProfileReturn {
  user: User | undefined;
  isLoading: boolean;
  error: Error | null;
  refetch: () => void;
}

export const useUserProfile = (): UseUserProfileReturn => {
  const { data, isLoading, error, refetch } = useQuery({
    queryKey: ['user', 'profile'],
    queryFn: async () => {
      const response = await apiClient.get('/users/me');
      return response.data;
    },
  });

  return { user: data, isLoading, error, refetch };
};

// Named object return (3+ values)
return {
  user,
  isLoading,
  error,
  refetch,
};

// Array return (exactly 2 values like useState)
return [value, setValue] as const;
```

### Bad example

```typescript
// ❌ Bad: Using .tsx extension
// useUserProfile.hook.tsx

// ❌ Bad: Including JSX in hook
export const useUserProfile = () => {
  return <div>User Profile</div>; // Hooks should not return JSX
};

// ❌ Bad: Calling hook conditionally
if (condition) {
  const data = useQuery(...); // Violates Rules of Hooks
}
```

## Anti-patterns

- include UI or JSX in hooks
- mix unrelated concerns in one hook without a clear abstraction boundary
- use `.hook.tsx` for logic-only hooks
- call hooks conditionally or in loops
- return inconsistent shapes across similar hooks
- push translation or presentational formatting into hooks when it belongs in components

## Notes

### File Naming Conventions

```
features/courses/
├── CoursePage/
│   ├── CoursePage.tsx          # Component
│   ├── CoursePage.hook.ts      # Page-specific hook
│   └── tests/
│       └── CoursePage.spec.tsx

shared/hooks/
├── useLocalStorage.hook.ts     # Shared utility hook
├── useDebounce.hook.ts
└── usePagination.hook.ts
```

- hook files must use `.hook.ts` extension, never `.hook.tsx`
- hooks should be co-located with components or in shared locations with clear ownership
- return type interfaces improve code clarity and IDE support
- named object returns are preferred for 3+ values
- array returns work well for exactly 2 values when the pattern is familiar
