---
id: frontend/coding/state-management
name: frontend/coding/state-management
kind: reference
domain: frontend
topics: [coding, state management]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# State Management

## When to use

Use this document when:

- Deciding how to store state
- Choosing between React Query, Zustand, or useState
- Reviewing state-related logic

## Rules

- Use React Query for server state (data from APIs)
- Use Zustand for complex client state (shared across components)
- Use useState for local UI state only (modals, form inputs)
- Always handle loading/error states
- Extract state logic to hooks

## Examples

### Good example

```typescript
// ✅ Good: React Query for server state
// UserProfilePage.hook.ts
import { useQuery, useMutation } from '@tanstack/react-query';
import { apiClient } from '@/shared/api/apiClient';

export const useUserProfile = () => {
  const {
    data: user,
    isLoading,
    error,
  } = useQuery({
    queryKey: ['user', 'profile'],
    queryFn: async () => {
      const response = await apiClient.get('/users/me');
      return response.data;
    },
  });

  const { mutate: updateProfile } = useMutation({
    mutationFn: async (data: UpdateUserDto) => {
      const response = await apiClient.patch('/users/me', data);
      return response.data;
    },
  });

  return { user, isLoading, error, updateProfile };
};

// ✅ Good: Zustand for complex client state
// store.ts
import { create } from 'zustand';

interface AppState {
  sidebarOpen: boolean;
  toggleSidebar: () => void;
}

export const useAppStore = create<AppState>(set => ({
  sidebarOpen: false,
  toggleSidebar: () => set(state => ({ sidebarOpen: !state.sidebarOpen })),
}));

// ✅ Good: useState for local UI state
// Only for UI state like modals, form inputs
const [isOpen, setIsOpen] = useState(false);
const [inputValue, setInputValue] = useState('');
```

### Bad example

```typescript
// ❌ Bad: Using useState for server state
const [users, setUsers] = useState([]);
useEffect(() => {
  fetch('/api/users').then(r => r.json()).then(setUsers);
}, []);

// ❌ Bad: Using React Query for simple UI state
const { data: isOpen } = useQuery({
  queryKey: ['modal', 'isOpen'],
  queryFn: () => false, // Should use useState
});

// ❌ Bad: Not handling loading/error states
const { data: user } = useQuery({...});
return <div>{user.name}</div>; // What if user is undefined?
```

## Anti-patterns

- Using useState for server state
- Using React Query for simple UI state
- Not handling loading/error states
- Mixing state management approaches inconsistently
- Storing server state in component state

## Notes

- React Query handles caching, refetching, and synchronization automatically
- Zustand is for client state that needs to be shared across components
- useState should only be used for local component UI state
- Always handle loading, error, and success states
- Extract state logic to custom hooks for reusability
- Server state should never be stored in component state or Zustand
