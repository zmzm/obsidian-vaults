---
id: frontend/i18n/principles
name: frontend/i18n/principles
kind: reference
domain: frontend
topics: [i18n, core principles]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# i18n Principles

## When to use

Use this document when:

- Localizing UI text and adding translations
- Organizing translations by namespace
- Implementing multilingual support
- Understanding translation workflow

## Rules

- Localize all visible UI text (no exceptions)
- Use useTranslation hook for all text content
- Organize translations by namespace (auth, users, courses, etc.)
- Add translations to both EN and PL locale files
- Use interpolation for dynamic values
- Handle pluralization with \_one/\_other suffixes
- Use common namespace for shared text (buttons, errors)
- Format dates/numbers based on locale (Intl API)
- Keep translation keys descriptive and hierarchical

## Examples

### Good example

```typescript
import { useTranslation } from 'react-i18next';

export const WelcomePage: React.FC = () => {
  const { t } = useTranslation('auth');
  return (
    <div>
      <h1>{t('welcome.title')}</h1>
      <p>{t('welcome.description')}</p>
      <button>{t('actions.getStarted')}</button>
    </div>
  );
};
```

### Bad example

```typescript
// ❌ Bad: Hardcoded strings
export const WelcomePage: React.FC = () => {
  return (
    <div>
      <h1>Welcome</h1>
      <p>Get started today</p>
      <button>Click Here</button>
    </div>
  );
};

// ❌ Bad: Concatenating translation strings
const message = t('click') + ' ' + t('here');

// ❌ Bad: Dynamic translation keys
t('click' + 'here');
```

## Anti-patterns

- hardcode visible strings in UI code
- concatenate translation fragments instead of using interpolation
- use dynamic translation keys
- translate technical values that should stay technical
- forget one locale while updating another
- skip namespace discipline once translations grow

## Notes

### Namespace Organization

```
i18n/
├── en/
│   ├── common.locales.ts      # Shared UI text (buttons, errors)
│   ├── auth.locales.ts        # Authentication pages
│   ├── users.locales.ts       # User management
│   ├── courses.locales.ts     # Course features
│   └── dashboard.locales.ts   # Dashboard
└── pl/
    ├── common.locales.ts
    ├── auth.locales.ts
    └── ...
```

### Namespace Selection

| Namespace   | Use For                                           |
| ----------- | ------------------------------------------------- |
| `common`    | Buttons, errors, loading states, shared UI text   |
| `auth`      | Login, signup, password reset, email verification |
| `users`     | User profiles, settings, management               |
| `courses`   | Course list, details, creation, editing           |
| `dashboard` | Dashboard-specific content                        |

### Adding New Translations

1. Add to English locale file (`en/[namespace].locales.ts`)
2. Add to Polish locale file (`pl/[namespace].locales.ts`)
3. Use in component: `const { t } = useTranslation('namespace');`

### Accessibility Reminder

- aria-labels, placeholders, and other user-facing accessibility text also need translation coverage
