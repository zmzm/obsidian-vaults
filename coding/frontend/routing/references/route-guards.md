---
id: frontend/routing/route-guards
name: frontend/routing/route-guards
kind: reference
domain: frontend
topics: [routing, route guards]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Route Guards

## When to use

Use this document when:

- Implementing protected routes
- Handling authentication redirects
- Creating role-based access

## Rules

- Use `useAuth` hook to check authentication state
- Show loading state while auth is loading
- Redirect unauthenticated users to login
- Redirect authenticated users away from auth pages
- Use `Navigate` component with `replace` prop for redirects

## Examples

### Good example

```typescript
// ✅ Good: Protected route pattern (from routes.tsx)
export function AppRoutes() {
  const { isLoaded, isSignedIn } = useAuth();

  // Show loading while auth state is being determined
  if (!isLoaded) {
    return <LoadingPage />;
  }

  return (
    <MainLayout>
      <Routes>
        {/* Public routes - redirect to dashboard if signed in */}
        <Route path={ROUTES.LOGIN} element={isSignedIn ? <Navigate to={ROUTES.DASHBOARD} replace /> : <LoginPage />} />

        {/* Protected routes - redirect to login if not signed in */}
        <Route
          path="/*"
          element={
            isSignedIn ? (
              <Routes>
                <Route path={ROUTES.DASHBOARD} element={<DashboardPage />} />
                {/* ... more protected routes */}
              </Routes>
            ) : (
              <Navigate to={ROUTES.LOGIN} replace />
            )
          }
        />
      </Routes>
    </MainLayout>
  );
}
```

### Bad example

```typescript
// ❌ Bad: No loading state
const { isSignedIn } = useAuth();
// Renders before auth state is known

// ❌ Bad: Redirect without replace
<Navigate to={ROUTES.LOGIN} />;
// Creates history entry, back button doesn't work correctly

// ❌ Bad: Inline auth check in component
const DashboardPage = () => {
  const { isSignedIn } = useAuth();
  if (!isSignedIn) return <Navigate to={ROUTES.LOGIN} />;
  // Auth should be handled at route level
};
```

## Anti-patterns

- Checking auth in individual page components
- Not handling loading state
- Using `navigate()` instead of `<Navigate />` for guards
- Forgetting `replace` prop on redirects

## Notes

### Public vs Protected Routes

| Route Type                  | When Signed In        | When Not Signed In |
| --------------------------- | --------------------- | ------------------ |
| Public (login, signup)      | Redirect to dashboard | Show page          |
| Protected (dashboard, etc.) | Show page             | Redirect to login  |
| Open (forgot-password)      | Show page             | Show page          |

### Loading State

Always check `isLoaded` before `isSignedIn`:

- `isLoaded: false` → Show loading spinner
- `isLoaded: true, isSignedIn: false` → Not authenticated
- `isLoaded: true, isSignedIn: true` → Authenticated
