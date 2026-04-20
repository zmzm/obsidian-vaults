---
id: frontend/accessibility/forms
name: frontend/accessibility/forms
kind: reference
domain: frontend
topics: [accessibility, forms]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Form Accessibility

## When to use

Use this document when:

- Creating accessible forms with proper labels
- Implementing form validation with error messages
- Handling required fields and input associations
- Ensuring forms are keyboard navigable

## Rules

- Always associate labels with inputs using htmlFor/id
- Use aria-required for required fields
- Use aria-invalid and aria-describedby for validation errors
- Provide clear error messages associated with inputs
- Use semantic form elements (form, label, input, button)

## Examples

### Good example

```typescript
// ✅ Good: Accessible form
export const LoginForm: React.FC = () => {
  const { t } = useTranslation('auth');
  return (
    <form aria-label={t('loginForm')}>
      <div>
        <Label htmlFor="email">{t('email')}</Label>
        <Input
          id="email"
          type="email"
          aria-required="true"
          aria-invalid={!!errors.email}
          aria-describedby={errors.email ? 'email-error' : undefined}
        />
        {errors.email && (
          <span id="email-error" role="alert">
            {errors.email}
          </span>
        )}
      </div>
      <div>
        <Label htmlFor="password">{t('password')}</Label>
        <Input
          id="password"
          type="password"
          aria-required="true"
          aria-describedby="password-help"
        />
        <span id="password-help">{t('passwordRequirements')}</span>
      </div>
      <Button type="submit" aria-label={t('submitLogin')}>
        {t('signIn')}
      </Button>
    </form>
  );
};

// Required fields
<Label htmlFor="email">
  {t('email')}
  <span aria-label="required">*</span>
</Label>
<Input id="email" aria-required="true" />
```

### Bad example

```typescript
// ❌ Bad: Missing label association
<Input type="email" placeholder="Email" />

// ❌ Bad: Error not associated with input
<Input id="email" />
{errors.email && <span>{errors.email}</span>}

// ❌ Bad: Using placeholder as label
<Input placeholder="Enter your email" />
```

## Anti-patterns

- Using placeholder text as the only label
- Not associating error messages with inputs
- Missing required field indicators
- Using divs instead of semantic form elements
- Not providing helper text for complex inputs

## Notes

- Error messages should use role="alert" for immediate announcement
- aria-describedby links inputs to help text and error messages
- Required fields should be indicated visually and with aria-required
- Form validation should be announced to screen readers
- Helper text should be associated with inputs using aria-describedby
