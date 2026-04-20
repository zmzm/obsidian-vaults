---
id: frontend/hook/utility-hooks
name: frontend/hook/utility-hooks
kind: reference
domain: frontend
topics: [hook, utility hooks]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Utility Hooks

## When to use

Use this document when:

- Creating reusable utility hooks (localStorage, debounce, pagination)
- Implementing common UI state patterns (dialogs, toggles)
- Building hooks for browser APIs
- Extracting shared logic into utility hooks

## Rules

- Keep utility hooks generic and reusable
- Handle edge cases (localStorage errors, etc.)
- Return consistent interfaces
- Use TypeScript generics for flexibility
- Handle cleanup in useEffect hooks

## Examples

### Good example

```typescript
// Local Storage Hook
// useLocalStorage.hook.ts
import { useState } from 'react';

export const useLocalStorage = <T>(key: string, initialValue: T): [T, (value: T) => void] => {
  const [storedValue, setStoredValue] = useState<T>(() => {
    try {
      const item = window.localStorage.getItem(key);
      return item ? JSON.parse(item) : initialValue;
    } catch {
      return initialValue;
    }
  });

  const setValue = (value: T) => {
    try {
      setStoredValue(value);
      window.localStorage.setItem(key, JSON.stringify(value));
    } catch (error) {
      console.error('Error writing to localStorage:', error);
    }
  };

  return [storedValue, setValue];
};

// Usage
const [theme, setTheme] = useLocalStorage<'light' | 'dark'>('theme', 'light');

// Debounce Hook
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

// Usage in search
const [searchTerm, setSearchTerm] = useState('');
const debouncedSearch = useDebounce(searchTerm, 300);

// Pagination Hook
// usePagination.hook.ts
import { useState } from 'react';

interface UsePaginationProps {
  totalItems: number;
  itemsPerPage: number;
  initialPage?: number;
}

export const usePagination = ({ totalItems, itemsPerPage, initialPage = 1 }: UsePaginationProps) => {
  const [currentPage, setCurrentPage] = useState(initialPage);
  const totalPages = Math.ceil(totalItems / itemsPerPage);

  const goToPage = (page: number) => {
    setCurrentPage(Math.max(1, Math.min(page, totalPages)));
  };

  return {
    currentPage,
    totalPages,
    goToPage,
    nextPage: () => goToPage(currentPage + 1),
    prevPage: () => goToPage(currentPage - 1),
    canGoNext: currentPage < totalPages,
    canGoPrev: currentPage > 1,
  };
};

// Dialog Hook
// useDialog.hook.ts
import { useState } from 'react';

export const useDialog = (initialState: boolean = false) => {
  const [isOpen, setIsOpen] = useState(initialState);
  return {
    isOpen,
    open: () => setIsOpen(true),
    close: () => setIsOpen(false),
    toggle: () => setIsOpen(prev => !prev),
  };
};
```

### Bad example

```typescript
// ❌ Bad: Not handling localStorage errors
export const useLocalStorage = (key: string, initialValue: any) => {
  const [value, setValue] = useState(() => {
    return JSON.parse(localStorage.getItem(key) || initialValue);
    // May throw if localStorage is unavailable
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

- Not handling edge cases (localStorage errors, SSR)
- Not cleaning up effects (timeouts, listeners)
- Not using TypeScript generics for flexibility
- Returning inconsistent interfaces
- Not handling browser API availability

## Notes

- Utility hooks should be generic and reusable across the application
- Always handle errors gracefully (localStorage may be unavailable)
- Clean up effects to prevent memory leaks
- Use TypeScript generics for type-safe utility hooks
- Place utility hooks in `shared/hooks/` directory
- Test utility hooks thoroughly as they're used widely
