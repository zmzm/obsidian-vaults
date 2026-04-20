---
id: fe-ui/forms
name: fe-ui/forms
kind: reference
domain: frontend-ui
topics: [forms, validation, ux]
priority: high
status: stable
canonical: true
updated: 2026-04-16
---

# Form Components

> **See also**: For comprehensive form accessibility patterns (ARIA, screen readers, validation announcements), see
> `fe-accessibility/references/forms.md`.

This document focuses on **using @mentory/ui-components** for forms.

## When to use

Use this document when:

- Using Input, Textarea, Select, Switch from `@mentory/ui-components`
- Building form layouts with UI components
- Implementing form validation display

For accessibility patterns → see `fe-accessibility/forms.md` For form state hooks → see `fe-hook/form-state.md`

## Available Form Components

| Component  | Use For                              |
| ---------- | ------------------------------------ |
| `Input`    | Text, email, password, number fields |
| `Textarea` | Multi-line text input                |
| `Select`   | Dropdown selection                   |
| `Switch`   | Boolean toggles                      |
| `Label`    | Field labels                         |
| `Alert`    | Validation error display             |

## Basic Form Structure

```typescript
import { Input, Label, Button, Select } from '@mentory/ui-components';

export function CreateCourseForm() {
  const { t } = useTranslation('courses');
  return (
    <form>
      <div>
        <Label htmlFor="title">{t('form.title')}</Label>
        <Input id="title" type="text" placeholder={t('form.titlePlaceholder')} required />
      </div>
      <div>
        <Label htmlFor="difficulty">{t('form.difficulty')}</Label>
        <Select id="difficulty">
          <option value="BEGINNER">{t('difficulty.beginner')}</option>
          <option value="INTERMEDIATE">{t('difficulty.intermediate')}</option>
        </Select>
      </div>
      <Button type="submit">{t('create')}</Button>
    </form>
  );
}
```

## Form Validation Display

```typescript
import { Input, Label, Alert } from '@mentory/ui-components';

export function LoginForm() {
  const [errors, setErrors] = useState<Record<string, string>>({});

  return (
    <form>
      <Label htmlFor="email">{t('email')}</Label>
      <Input id="email" type="email" aria-invalid={!!errors.email} aria-describedby={errors.email ? 'email-error' : undefined} />
      {errors.email && (
        <Alert status="error" id="email-error">
          {errors.email}
        </Alert>
      )}
    </form>
  );
}
```

## Switch for Booleans

```typescript
import { Switch, Label } from '@mentory/ui-components';

<div>
  <Label htmlFor="notifications">{t('notifications')}</Label>
  <Switch id="notifications" />
</div>;
```

## Anti-patterns

- Missing label association with inputs
- Using `type="text"` for email/password fields
- Not using Switch for boolean toggles
- Importing from `@chakra-ui/*` instead of `@mentory/ui-components`

## Notes

- Always import from `@mentory/ui-components`
- For full accessibility requirements (ARIA, keyboard) → `fe-accessibility/forms.md`
- For form state management hooks → `fe-hook/form-state.md`
