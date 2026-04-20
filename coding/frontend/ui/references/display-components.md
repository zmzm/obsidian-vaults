---
id: fe-ui/display-components
name: fe-ui/display-components
kind: reference
domain: frontend-ui
topics: [display-components]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# Display Components

## When to use

Use this document when:

- Using Avatar, Badge, Skeleton, and ThemeToggle components
- Displaying user avatars
- Showing status indicators with badges
- Creating loading placeholders
- Implementing theme switching

## Rules

- Always import from `@mentory/ui-components`
- Use Avatar for user profile images
- Use Badge for status indicators
- Use Skeleton for loading states
- Use ThemeToggle for dark/light mode switching

## Examples

### Good example

```typescript
// Avatar Component
import { Avatar, Badge } from '@mentory/ui-components';

export function UserProfile({ user }: { user: User }) {
  return (
    <div>
      <Avatar name={user.name} src={user.avatarUrl} />
      <h3>{user.name}</h3>
      <Badge>{user.role}</Badge>
    </div>
  );
}

// Badge Component
import { Badge } from '@mentory/ui-components';

// Status badges
<Badge colorScheme="green">Active</Badge>
<Badge colorScheme="red">Inactive</Badge>
<Badge colorScheme="blue">Pending</Badge>

// Role badges
<Badge>{user.role}</Badge>

// Skeleton Loading
import { Skeleton } from '@mentory/ui-components';

export function CourseCardSkeleton() {
  return (
    <div>
      <Skeleton height="200px" />
      <Skeleton height="24px" width="80%" />
      <Skeleton height="16px" width="60%" />
    </div>
  );
}

// ThemeToggle Component
import { ThemeToggle } from '@mentory/ui-components';

export function Header() {
  return (
    <header>
      <ThemeToggle />
    </header>
  );
}
```

### Bad example

```typescript
// ❌ Bad: Creating custom avatar component
<div className="avatar">
  <img src={user.avatarUrl} />
</div>

// ❌ Bad: Using div for badges
<div className="badge">{user.role}</div>

// ❌ Bad: Not using Skeleton for loading
<div>Loading...</div>
```

## Anti-patterns

- Creating custom display components instead of using provided ones
- Not using Skeleton for loading states
- Using divs for badges or status indicators
- Not using Avatar component for user images
- Missing ThemeToggle for theme switching

## Notes

- Avatar component handles fallback when image fails to load
- Badge component provides consistent styling for status indicators
- Skeleton component matches content structure for better UX
- ThemeToggle provides built-in dark/light mode switching
- All components are accessible and keyboard navigable
