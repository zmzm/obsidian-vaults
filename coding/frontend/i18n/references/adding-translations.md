---
id: frontend/i18n/adding-translations
name: frontend/i18n/adding-translations
kind: reference
domain: frontend
topics: [i18n, adding translations]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Adding New Translations

## When to use

Use this document when:

- Adding new translation keys to the application
- Following the translation workflow
- Understanding key naming conventions
- Organizing translations by namespace

## Rules

- Always add to English locale first
- Then add to Polish locale
- Use descriptive, hierarchical keys
- Group related translations together
- Follow consistent naming conventions
- Use namespace for organization

## Examples

### Good example

```typescript
// 1. Add to English Locale First
// en/users.locales.ts
export const userLocales = {
  profile: {
    title: 'User Profile',
    updateSuccess: 'Profile updated successfully',
  },
};

// 2. Add to Polish Locale
// pl/users.locales.ts
export const userLocales = {
  profile: {
    title: 'Profil Użytkownika',
    updateSuccess: 'Profil zaktualizowany pomyślnie',
  },
};

// 3. Use in Component
const { t } = useTranslation('users');
<h1>{t('profile.title')}</h1>;

// Translation Key Structure
export const namespaceLocales = {
  // Feature sections
  featureName: {
    // Actions
    actions: {
      save: 'Save',
      cancel: 'Cancel',
    },
    // Errors
    errors: {
      notFound: 'Not found',
    },
  },
};
```

### Bad example

```typescript
// ❌ Bad: Adding to only one locale
// en/users.locales.ts
export const userLocales = {
  profile: { title: 'User Profile' },
};
// Missing Polish translation

// ❌ Bad: Inconsistent key naming
export const userLocales = {
  profileTitle: 'User Profile', // Should be profile.title
  profileUpdateSuccess: 'Updated', // Should be profile.updateSuccess
};

// ❌ Bad: Not using namespace
const { t } = useTranslation(); // Should specify namespace
```

## Anti-patterns

- Adding translations to only one locale
- Using flat key structure instead of hierarchical
- Not following consistent naming conventions
- Not grouping related translations
- Not using namespaces for organization

## Notes

### Workflow

1. **Add to English locale first** - Start with English as base
2. **Add to Polish locale** - Translate to Polish
3. **Use in component** - Import namespace and use translation key

### Key Naming Conventions

- Use descriptive, hierarchical keys: `profile.title`, `errors.notFound`
- Group related translations: `login.title`, `login.submit`, `login.errors`
- Use consistent naming: `actions.save`, `actions.cancel`, `actions.delete`

### Translation Key Structure

- Feature sections at top level
- Actions grouped under `actions`
- Errors grouped under `errors`
- Labels grouped under `labels`
- Validation grouped under `validation`

### Namespace Selection

- `common` - Shared UI text (buttons, errors, loading states)
- `auth` - Authentication pages
- `users` - User management
- `courses` - Course features
- `dashboard` - Dashboard-specific content
