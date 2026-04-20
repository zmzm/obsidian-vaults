---
id: frontend/i18n/patterns
name: frontend/i18n/patterns
kind: reference
domain: frontend
topics: [i18n, patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Common i18n Patterns

## When to use

Use this document when:

- Creating error messages with translations
- Implementing form labels and validation
- Formatting dates and numbers based on locale
- Organizing locale file structure

## Rules

- Group related translations (errors, labels, actions)
- Use hierarchical key structure
- Format dates/numbers using Intl API
- Keep locale files organized by feature
- Use consistent naming conventions

## Examples

### Good example

```typescript
// Error Messages
export const commonLocales = {
  errors: {
    network: 'Network error. Please check your connection.',
    unauthorized: 'You are not authorized to perform this action.',
    notFound: '{{resource}} not found',
    serverError: 'Something went wrong. Please try again later.',
  },
};

// Usage
const { t } = useTranslation('common');
if (error.status === 404) {
  return <Alert>{t('errors.notFound', { resource: 'User' })}</Alert>;
}

// Form Labels and Validation
export const formsLocales = {
  labels: {
    email: 'Email address',
    password: 'Password',
    confirmPassword: 'Confirm password',
  },
  validation: {
    required: '{{field}} is required',
    minLength: '{{field}} must be at least {{min}} characters',
    emailInvalid: 'Please enter a valid email address',
    passwordMismatch: 'Passwords do not match',
  },
};

// Usage in form
const { t } = useTranslation('forms');
<Label>{t('labels.email')}</Label>
<Input error={t('validation.required', { field: t('labels.email') })} />

// Dates and Numbers
import { useTranslation } from 'react-i18next';

const { t, i18n } = useTranslation('common');

// Format dates based on locale
const formatDate = (date: Date) => {
  return new Intl.DateTimeFormat(i18n.language).format(date);
};

// Format numbers
const formatNumber = (num: number) => {
  return new Intl.NumberFormat(i18n.language).format(num);
};

<p>{t('created')}: {formatDate(course.createdAt)}</p>
<p>{t('price')}: {formatNumber(course.price)}</p>
```

### Bad example

```typescript
// ❌ Bad: Flat structure without grouping
export const authLocales = {
  welcomeTitle: 'Welcome',
  welcomeDescription: 'Description',
  loginTitle: 'Sign In',
  // Hard to organize and find
};

// ❌ Bad: Not formatting dates/numbers
<p>{course.createdAt}</p>; // Should use Intl API

// ❌ Bad: Inconsistent naming
export const authLocales = {
  welcome: { title: 'Welcome' },
  loginTitle: 'Sign In', // Should be login.title
};
```

## Anti-patterns

- Flat locale file structure without grouping
- Not formatting dates/numbers based on locale
- Inconsistent key naming conventions
- Mixing different concerns in same keys
- Not using hierarchical structure

## Notes

### Locale File Structure

```typescript
// en/auth.locales.ts
export const authLocales = {
  welcome: {
    title: 'Welcome to Mentory',
    description: 'Accelerate your IT skills',
  },
  login: {
    title: 'Sign In',
    email: 'Email address',
    password: 'Password',
    submit: 'Sign in',
    forgotPassword: 'Forgot password?',
  },
  errors: {
    invalidCredentials: 'Invalid email or password',
    accountLocked: 'Account is locked. Try again in {{minutes}} minutes',
  },
};
```

### Key Naming Conventions

- Use descriptive, hierarchical keys: `profile.title`, `errors.notFound`
- Group related translations: `login.title`, `login.submit`, `login.errors`
- Use consistent naming: `actions.save`, `actions.cancel`, `actions.delete`

### Date and Number Formatting

- Use `Intl.DateTimeFormat` for dates based on locale
- Use `Intl.NumberFormat` for numbers based on locale
- Access current language via `i18n.language`
- Formatting adapts automatically to locale
