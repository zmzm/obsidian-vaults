---
id: frontend/i18n/testing
name: frontend/i18n/testing
kind: reference
domain: frontend
topics: [i18n, testing]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Testing i18n

## When to use

Use this document when:

- Writing tests for components with translations
- Mocking i18n in test setup
- Testing components that use useTranslation
- Understanding how translations work in tests

## Rules

- Use test-utils mock for i18n (already set up)
- Translation keys are returned as-is by mock
- Test for translation keys, not translated text
- Don't manually mock i18n (use test-utils)
- Test interpolation patterns when needed

## Examples

### Good example

```typescript
// The @mentory/test-utils library already mocks i18n
// You don't need to set it up manually

// In test
it('should display welcome message', () => {
  renderComponent(<WelcomePage />);
  // Translation keys are returned as-is by the mock
  expect(screen.getByText('welcome.title')).toBeInTheDocument();
});

// Testing with Translation Keys
it('should display translated text', () => {
  renderComponent(<WelcomePage />);
  // Translation keys are returned as-is by the mock
  expect(screen.getByText('welcome.title')).toBeInTheDocument();
});

// Testing Interpolation
it('should interpolate dynamic values', () => {
  renderComponent(<UserGreeting name="John" />);
  // Mock returns key, so check for interpolation pattern
  expect(screen.getByText(/greeting/i)).toBeInTheDocument();
});
```

### Bad example

```typescript
// ❌ Bad: Manually mocking i18n
jest.mock('react-i18next', () => ({
  useTranslation: () => ({
    t: (key: string) => key,
    i18n: { language: 'en' },
  }),
}));
// test-utils already does this

// ❌ Bad: Testing for translated text
expect(screen.getByText('Welcome to Mentory')).toBeInTheDocument();
// Should test for translation key instead
```

## Anti-patterns

- Manually mocking i18n (test-utils already does this)
- Testing for translated text instead of keys
- Not using renderComponent from test-utils
- Setting up i18n mocks in individual tests

## Notes

### Test Utils Mock

The `@mentory/test-utils` library already mocks i18n:

- `useTranslation` returns `{ t: (key) => key, i18n: { language: 'en' } }`
- Translation keys are returned as-is
- No need to set up i18n mocks manually

### Testing Strategy

- Test for translation keys, not translated text
- Translation keys are returned as-is by mock
- Use `renderComponent` from test-utils (includes i18n mock)
- Test interpolation by checking for key patterns

### Interpolation Testing

- Mock returns keys, so check for key patterns
- Use regex or partial matching for interpolation
- Don't test actual translated values in unit tests
