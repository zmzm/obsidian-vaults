---
id: frontend/i18n/interpolation
name: frontend/i18n/interpolation
kind: reference
domain: frontend
topics: [i18n, interpolation]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Interpolation (Dynamic Values)

## When to use

Use this document when:

- Adding dynamic values to translation strings
- Creating error messages with variable content
- Implementing form validation messages
- Displaying user-specific or data-driven text

## Rules

- Use double curly braces `{{variable}}` for interpolation
- Pass values as object to `t()` function
- Format dates and numbers using Intl API
- Keep interpolation simple and readable
- Use descriptive variable names

## Examples

### Good example

```typescript
// Locale file
export const userLocales = {
  greeting: 'Hello, {{name}}!',
  courseProgress: 'You have completed {{count}} out of {{total}} courses',
  lastLogin: 'Last login: {{date}}',
};

// Component
const { t } = useTranslation('users');

<p>{t('greeting', { name: user.name })}</p>
<p>{t('courseProgress', { count: 5, total: 10 })}</p>
<p>{t('lastLogin', { date: formatDate(user.lastLogin) })}</p>

// Error Messages with Interpolation
export const commonLocales = {
  errors: {
    notFound: '{{resource}} not found',
    minLength: '{{field}} must be at least {{min}} characters',
  },
};

// Usage
const { t } = useTranslation('common');
if (error.status === 404) {
  return <Alert>{t('errors.notFound', { resource: 'User' })}</Alert>;
}

// Form Validation with Interpolation
export const formsLocales = {
  validation: {
    required: '{{field}} is required',
    minLength: '{{field}} must be at least {{min}} characters',
  },
};

// Usage
const { t } = useTranslation('forms');
<Input error={t('validation.required', { field: t('labels.email') })} />
```

### Bad example

```typescript
// ❌ Bad: Concatenating translations
<p>{t('hello')} {user.name} {t('welcomeBack')}</p>

// ❌ Bad: Not using interpolation
<p>Hello, {user.name}!</p> // Hardcoded "Hello"

// ❌ Bad: Complex interpolation logic
<p>{t('message') + ': ' + user.name}</p>
```

## Anti-patterns

- Concatenating translation strings
- Not using interpolation for dynamic values
- Hardcoding parts of translated strings
- Complex interpolation logic in components
- Not formatting dates/numbers based on locale

## Notes

- Use `{{variable}}` syntax in locale files
- Pass interpolation values as object: `t('key', { variable: value })`
- Format dates and numbers using Intl API based on current locale
- Keep interpolation simple - complex logic should be in components
- Nested interpolation is possible: `t('validation.required', { field: t('labels.email') })`
