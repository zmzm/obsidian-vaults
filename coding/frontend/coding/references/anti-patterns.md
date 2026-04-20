---
id: frontend/coding/anti-patterns
name: frontend/coding/anti-patterns
kind: reference
domain: frontend
topics: [coding, anti patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Anti-Patterns to Avoid

## When to use

Use this document when:

- Reviewing existing frontend code
- Refactoring components or hooks
- Creating new frontend code
- You notice growing complexity or unclear responsibilities

## Rules

- Extract business logic to hooks
- Always use i18n for visible text
- Use design system styling props, not inline styles
- Extract API calls to React Query hooks
- Use proper TypeScript types, never `any`

## Examples

### Good example

```typescript
// ✅ Good: Business logic in hook
export const UserList = () => {
  const { users, isLoading } = useUsers();
  if (isLoading) return <LoadingSpinner />;
  return <>{users.map(...)}</>;
};

// ✅ Good: i18n for text
const { t } = useTranslation('common');
<Button>{t('actions.clickHere')}</Button>;

// ✅ Good: Design system styling
import { Box } from '@mentory/ui-components';
<Box p={4} color="red.500">

// ✅ Good: API calls in hook
const { users } = useUsers();

// ✅ Good: Proper types
const handleClick = (data: UserDto) => { ... };
```

### Bad example

```typescript
// ❌ Bad: Mix Business Logic in Components
export const UserList = () => {
  const [users, setUsers] = useState([]);
  useEffect(() => {
    fetch('/api/users')
      .then((r) => r.json())
      .then(setUsers); // Business logic in component
  }, []);
  return <>{users.map(...)}</>;
};

// ❌ Bad: Hardcode Strings
<Button>Click Here</Button>;

// ❌ Bad: Use Inline Styles
<div style={{ padding: '16px', color: 'red' }}>

// ❌ Bad: Put API Calls in Components
useEffect(() => {
  fetch('/api/users').then(setUsers);
}, []);

// ❌ Bad: Use any Type
const handleClick = (data: any) => { ... };
```

## Anti-patterns

- Mixing business logic in components
- Hardcoding strings instead of using i18n
- Using inline styles instead of design system props
- Putting API calls directly in components
- Using `any` type in TypeScript
- Not extracting reusable logic to hooks
- Creating components that are too complex

## Notes

- Business logic should always be in hooks, not components
- All visible text must use i18n, even English
- Inline styles break design system consistency (see UI skill for specific styling patterns)
- API calls should use React Query hooks
- TypeScript `any` defeats the purpose of type safety
- Complex components should be broken into smaller pieces
- For UI component library usage, see the UI skill
