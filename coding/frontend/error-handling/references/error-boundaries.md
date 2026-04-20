---
id: frontend/error-handling/error-boundaries
name: frontend/error-handling/error-boundaries
kind: reference
domain: frontend
topics: [error-handling, error boundaries]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Error Boundaries

## When to use

Use this document when:

- Setting up ErrorBoundary component
- Handling unexpected render errors
- Creating fallback UIs for errors

## Rules

- Wrap main content in ErrorBoundary
- ErrorBoundary catches render errors, not event handler errors
- Provide reset functionality to recover from errors
- Log errors for debugging
- Show user-friendly fallback UI

## Examples

### Good example

```typescript
// ✅ Good: ErrorBoundary in layout
// shared/layouts/MainLayout/MainLayout.tsx
import { ErrorBoundary } from '@/shared/components/ErrorBoundary/ErrorBoundary';

export const MainLayout = ({ children }: MainLayoutProps) => {
  return (
    <Box minH="100vh">
      <Header />
      <ErrorBoundary>
        {children}
      </ErrorBoundary>
    </Box>
  );
};

// ✅ Good: Custom fallback
<ErrorBoundary fallback={<CustomErrorPage />}>
  {children}
</ErrorBoundary>

// ✅ Good: Section-level boundary
<ErrorBoundary>
  <DashboardWidgets />
</ErrorBoundary>
<ErrorBoundary>
  <RecentActivity />
</ErrorBoundary>
```

### Bad example

```typescript
// ❌ Bad: ErrorBoundary for event handlers
// ErrorBoundary won't catch this
const handleClick = () => {
  throw new Error('Click error'); // Not caught by boundary
};

// ❌ Bad: No reset option
const ErrorFallback = () => (
  <div>Something went wrong</div>
  // No way to recover
);
```

## ErrorBoundary Component

The ErrorBoundary component in `shared/components/ErrorBoundary/`:

```typescript
// Usage
<ErrorBoundary>
  {children}
</ErrorBoundary>

// With custom fallback
<ErrorBoundary fallback={<MyFallback />}>
  {children}
</ErrorBoundary>
```

### Props

| Prop       | Type      | Description                 |
| ---------- | --------- | --------------------------- |
| `children` | ReactNode | Content to render           |
| `fallback` | ReactNode | Optional custom fallback UI |

### Default Fallback

The default fallback shows:

- Error icon
- "Error" title (i18n)
- Error message
- "Try Again" button (resets error state)
- "Refresh Page" button (full reload)

## useErrorBoundary Hook

```typescript
const { hasError, error, resetError, captureError } = useErrorBoundary();
```

| Return         | Type                   | Description                 |
| -------------- | ---------------------- | --------------------------- |
| `hasError`     | boolean                | Whether an error was caught |
| `error`        | Error \| undefined     | The caught error            |
| `resetError`   | () => void             | Clear error and retry       |
| `captureError` | (error: Error) => void | Manually capture an error   |

### Global Error Capture

The hook automatically listens for:

- `window.onerror` - Global JS errors
- `unhandledrejection` - Unhandled promise rejections

## Notes

### What ErrorBoundary Catches

| Caught                      | Not Caught                        |
| --------------------------- | --------------------------------- |
| Errors during rendering     | Event handlers                    |
| Errors in lifecycle methods | Async code (setTimeout, promises) |
| Errors in constructor       | Server-side rendering             |
| Errors in child components  | Errors in the boundary itself     |

### Multiple Boundaries

Use multiple boundaries to isolate failures:

```typescript
// If DashboardWidgets fails, RecentActivity still works
<ErrorBoundary>
  <DashboardWidgets />
</ErrorBoundary>
<ErrorBoundary>
  <RecentActivity />
</ErrorBoundary>
```
