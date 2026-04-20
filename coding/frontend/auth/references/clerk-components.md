---
id: frontend/auth/clerk-components
name: frontend/auth/clerk-components
kind: reference
domain: frontend
topics: [auth, clerk components]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Clerk Components

## When to use

Use this document when:

- Using SignIn or SignUp components
- Customizing Clerk component appearance
- Setting up auth pages

## Rules

- Clerk components (SignIn, SignUp) may be imported directly
- Customize appearance using the `appearance` prop
- Use i18n for text that wraps Clerk components
- Show loading state while Clerk initializes

## Examples

### Good example

```typescript
// ✅ Good: Login page with Clerk SignIn
import { SignIn } from '@clerk/clerk-react';
import { useLoginPage } from './LoginPage.hook';

export function LoginPage() {
  const { isLoaded } = useLoginPage();
  const { t } = useI18n();

  if (!isLoaded) {
    return <LoadingPage />;
  }

  return (
    <Box minH="100vh" display="flex" alignItems="center" justifyContent="center">
      <Card>
        <CardHeader textAlign="center">
          <CardTitle>{t('auth:signInTitle')}</CardTitle>
          <CardDescription>{t('auth:signInDescription')}</CardDescription>
        </CardHeader>
        <CardContent display="flex" justifyContent="center">
          <SignIn
            appearance={{
              elements: {
                formButtonPrimary: 'bg-primary hover:bg-primary/90',
              },
            }}
            signUpUrl={t('auth:signUpUrl')}
          />
        </CardContent>
      </Card>
    </Box>
  );
}

// ✅ Good: Signup page
import { SignUp } from '@clerk/clerk-react';

export function SignupPage() {
  return (
    <SignUp
      appearance={{
        elements: {
          formButtonPrimary: 'bg-primary hover:bg-primary/90',
        },
      }}
      signInUrl="/login"
    />
  );
}
```

### Bad example

```typescript
// ❌ Bad: No loading state
export function LoginPage() {
  return <SignIn />; // Clerk may not be ready
}

// ❌ Bad: Hardcoded text around Clerk
export function LoginPage() {
  return (
    <div>
      <h1>Sign In to Your Account</h1> {/* Should use i18n */}
      <SignIn />
    </div>
  );
}
```

## Clerk Component Props

### SignIn

| Prop          | Description                     |
| ------------- | ------------------------------- |
| `appearance`  | Customize styles                |
| `signUpUrl`   | URL for sign up link            |
| `redirectUrl` | Where to redirect after sign in |
| `routing`     | 'hash' \| 'path' \| 'virtual'   |

### SignUp

| Prop          | Description                     |
| ------------- | ------------------------------- |
| `appearance`  | Customize styles                |
| `signInUrl`   | URL for sign in link            |
| `redirectUrl` | Where to redirect after sign up |

## Notes

### Appearance Customization

```typescript
<SignIn
  appearance={{
    elements: {
      // Override specific elements
      formButtonPrimary: 'bg-primary hover:bg-primary/90 text-white',
      card: 'shadow-none',
      headerTitle: 'text-xl font-bold',
      formFieldInput: 'border-gray-300',
    },
    variables: {
      // Override CSS variables
      colorPrimary: '#your-color',
      borderRadius: '8px',
    },
  }}
/>
```

### Page Structure Pattern

Auth pages follow this structure:

```
features/auth/
├── LoginPage/
│   ├── LoginPage.tsx        # Component
│   ├── LoginPage.hook.ts    # Hook (checks isLoaded)
│   └── LoginPage.type.ts    # Types
├── SignupPage/
├── ForgotPasswordPage/
└── ...
```
