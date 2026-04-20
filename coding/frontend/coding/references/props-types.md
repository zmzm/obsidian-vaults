---
id: frontend/coding/props-types
name: frontend/coding/props-types
kind: reference
domain: frontend
topics: [coding, props types]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Props and Types

## When to use

Use this document when:

- Designing component APIs
- Defining props and types
- Reviewing TypeScript usage

## Rules

- Always define prop interfaces
- Use TypeScript strictly
- Keep props minimal and focused
- Use composition over prop drilling
- Never use `any` type
- Make optional props explicit with `?`

## Examples

### Good example

```typescript
import { Card, Button } from '@mentory/ui-components';

interface UserCardProps {
  user: User;
  onEdit?: (userId: string) => void;
}

export const UserCard: React.FC<UserCardProps> = ({ user, onEdit }) => {
  const { t } = useTranslation('users');
  return (
    <Card>
      <h3>{user.email}</h3>
      {onEdit && (
        <Button onClick={() => onEdit(user.id)} size="sm">
          {t('actions.edit')}
        </Button>
      )}
    </Card>
  );
};

// Type definitions in separate file
// UserProfilePage.type.ts
export interface UserProfilePageProps {
  userId: string;
  onUpdate?: (user: User) => void;
}

export interface User {
  id: string;
  email: string;
  role: UserRole;
}

// Composition over prop drilling
<Parent>
  <UserCard user={user} />
  <UserActions onEdit={handleEdit} onDelete={handleDelete} />
</Parent>;
```

### Bad example

```typescript
// ❌ Bad: any type, unclear props
export const UserCard = (props: any) => {
  return <div>{props.data?.user?.name || 'Unknown'}</div>;
};

// ❌ Bad: Prop drilling
<Parent user={user} onEdit={handleEdit} onDelete={handleDelete} />;
```

## Anti-patterns

- Using `any` type for props
- Not defining prop interfaces
- Prop drilling through multiple levels
- Unclear or ambiguous prop names
- Too many props (consider composition)
- Missing optional prop indicators

## Notes

- Prop interfaces should be defined in `.type.ts` files for complex components
- Use composition to avoid prop drilling
- Optional props should be marked with `?`
- Props should be minimal and focused on component's responsibility
- Type definitions can be shared between component and hook files
- Use TypeScript strictly - avoid `any` and `unknown` when possible
