---
id: frontend/routing/navigation
name: frontend/routing/navigation
kind: reference
domain: frontend
topics: [routing, navigation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Navigation Patterns

## When to use

Use this document when:

- Navigating between pages programmatically
- Handling route parameters
- Working with query strings
- Using navigation hooks

## Rules

- Use `useNavigate` for programmatic navigation
- Use `useParams` to access route parameters
- Use `useLocation` for current location info
- Always use ROUTES constants, never hardcode paths
- Use `replace: true` when you don't want back navigation

## Examples

### Good example

```typescript
// ✅ Good: Programmatic navigation
import { useNavigate } from 'react-router-dom';
import { ROUTES } from '../shared/constants/routes.constant';

const MyComponent = () => {
  const navigate = useNavigate();

  const handleClick = () => {
    navigate(ROUTES.DASHBOARD);
  };

  const handleReplace = () => {
    // User can't go back to this page
    navigate(ROUTES.LOGIN, { replace: true });
  };

  return <Button onClick={handleClick}>Go to Dashboard</Button>;
};

// ✅ Good: Route parameters
// Route: /courses/:id
const CourseDetailPage = () => {
  const { id } = useParams<{ id: string }>();
  const { course } = useCourse(id!);
  // ...
};

// ✅ Good: Navigate with state
navigate(ROUTES.DASHBOARD, {
  state: { from: 'checkout' },
});

// ✅ Good: Link component with constants
import { Link } from 'react-router-dom';
<Link to={ROUTES.COURSES}>View Courses</Link>;
```

### Bad example

```typescript
// ❌ Bad: Hardcoded path
navigate('/dashboard');

// ❌ Bad: window.location for SPA navigation
window.location.href = '/dashboard';

// ❌ Bad: Not typing params
const { id } = useParams(); // id is string | undefined, not typed
```

## Navigation Hooks

| Hook                | Purpose                 |
| ------------------- | ----------------------- |
| `useNavigate()`     | Programmatic navigation |
| `useParams()`       | Access URL parameters   |
| `useLocation()`     | Current location object |
| `useSearchParams()` | Query string parameters |

## Notes

### Dynamic Route Navigation

```typescript
// For routes like /courses/:id
const navigateToCourse = (courseId: string) => {
  navigate(ROUTES.COURSE_DETAIL.replace(':id', courseId));
};

// Or use template literal helper
const navigateToCourse = (courseId: string) => {
  navigate(`/courses/${courseId}`);
};
```

### Query Parameters

```typescript
const [searchParams, setSearchParams] = useSearchParams();

// Read param
const filter = searchParams.get('filter');

// Set param
setSearchParams({ filter: 'active' });

// Add to existing
setSearchParams(prev => {
  prev.set('page', '2');
  return prev;
});
```
