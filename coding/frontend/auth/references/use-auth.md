---
id: frontend/auth/use-auth
name: frontend/auth/use-auth
kind: reference
domain: frontend
topics: [auth, use auth]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# useAuth Hook

## When to use

Use this document when:

- Using the useAuth hook
- Accessing user information
- Implementing sign out
- Getting tokens for API calls

## Rules

- Always import from `@/shared/hooks/useAuth`
- Check `isLoaded` before rendering auth-dependent content
- Use convenience properties (email, firstName) instead of navigating user object
- Handle undefined/null cases for user properties

## Examples

### Good example

```typescript
// ✅ Good: Basic auth check
import { useAuth } from '@/shared/hooks/useAuth';

const ProfileButton = () => {
  const { isLoaded, isSignedIn, email, imageUrl, signOut } = useAuth();

  if (!isLoaded) {
    return <Skeleton w="32px" h="32px" borderRadius="full" />;
  }

  if (!isSignedIn) {
    return <Link to={ROUTES.LOGIN}>Sign In</Link>;
  }

  return (
    <Menu>
      <MenuButton>
        <Avatar src={imageUrl} name={email} size="sm" />
      </MenuButton>
      <MenuList>
        <MenuItem>{email}</MenuItem>
        <MenuItem onClick={() => signOut()}>Sign Out</MenuItem>
      </MenuList>
    </Menu>
  );
};

// ✅ Good: Get token for API calls
const useApiCall = () => {
  const { getToken } = useAuth();

  const fetchWithAuth = async (url: string) => {
    const token = await getToken();
    return fetch(url, {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    });
  };

  return { fetchWithAuth };
};
```

### Bad example

```typescript
// ❌ Bad: Not handling loading state
const { isSignedIn } = useAuth();
return isSignedIn ? <Profile /> : <Login />;

// ❌ Bad: Navigating user object directly
const { user } = useAuth();
return <p>{user?.emailAddresses?.[0]?.emailAddress}</p>;
// Use: const { email } = useAuth();

// ❌ Bad: Not handling undefined
const { email } = useAuth();
return <p>Hello {email.split('@')[0]}</p>; // email may be undefined
```

## Notes

### Accessing User Data

Use the flattened properties instead of navigating the user object:

```typescript
// ❌ Avoid
const { user } = useAuth();
const email = user?.emailAddresses?.[0]?.emailAddress;
const name = user?.firstName;

// ✅ Prefer
const { email, firstName, lastName, imageUrl, userId } = useAuth();
```

### Sign Out

```typescript
const { signOut } = useAuth();

// Basic sign out
await signOut();

// Sign out with redirect
await signOut({ redirectUrl: ROUTES.LOGIN });
```

### Getting Tokens

```typescript
const { getToken } = useAuth();

// Get default token
const token = await getToken();

// Get token for specific template (if configured in Clerk)
const customToken = await getToken({ template: 'custom-template' });
```
