---
id: frontend/accessibility/testing
name: frontend/accessibility/testing
kind: reference
domain: frontend
topics: [accessibility, testing]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Testing Accessibility

> **Canonical source**: This is the authoritative reference for accessibility testing. The `fe-testing` skill references this document for
> all accessibility testing patterns.

## When to use

Use this document when:

- Writing automated accessibility tests with jest-axe
- Testing keyboard navigation in components
- Verifying screen reader compatibility (ARIA labels/roles)
- Testing focus management in modals and dialogs
- Adding accessibility tests to component test suites

## Rules

- Use jest-axe for automated accessibility testing
- Test keyboard navigation with userEvent
- Verify ARIA labels and roles are correct
- Test focus management in interactive components
- Include accessibility tests in component test suites

## Examples

### Good example

```typescript
// ✅ Good: jest-axe testing
import { axe, toHaveNoViolations } from 'jest-axe';

expect.extend(toHaveNoViolations);

it('should have no accessibility violations', async () => {
  const { container } = renderComponent(<LoginForm />);
  const results = await axe(container);
  expect(results).toHaveNoViolations();
});

// ✅ Good: Keyboard navigation testing
it('should navigate with keyboard', async () => {
  const user = userEvent.setup();
  renderComponent(<LoginForm />);

  // Tab through form
  await user.tab();
  expect(screen.getByLabelText(/email/i)).toHaveFocus();

  await user.tab();
  expect(screen.getByLabelText(/password/i)).toHaveFocus();
});

// ✅ Good: Screen reader testing
it('should have proper ARIA labels', () => {
  renderComponent(<CourseCard course={mockCourse} />);
  expect(screen.getByRole('article')).toHaveAccessibleName('React Basics');
  expect(screen.getByLabelText(/difficulty/i)).toHaveTextContent('BEGINNER');
});

// ✅ Good: Focus management testing
it('should manage focus correctly', async () => {
  const user = userEvent.setup();
  renderComponent(<Modal isOpen={true} />);
  const closeButton = screen.getByRole('button', { name: /close/i });
  expect(closeButton).toHaveFocus();
  await user.keyboard('{Escape}');
  expect(closeButton).not.toBeInTheDocument();
});
```

### Bad example

```typescript
// ❌ Bad: Not testing accessibility
it('should render form', () => {
  renderComponent(<LoginForm />);
  expect(screen.getByText(/email/i)).toBeInTheDocument();
});

// ❌ Bad: Testing implementation details instead of behavior
it('should have aria-label prop', () => {
  const { container } = renderComponent(<Button />);
  expect(container.querySelector('button')).toHaveAttribute('aria-label');
});
```

## Anti-patterns

- Skipping accessibility tests
- Testing implementation details instead of behavior
- Not testing keyboard navigation
- Missing screen reader compatibility tests
- Not verifying focus management

## Notes

- jest-axe catches many common accessibility issues automatically
- Keyboard navigation tests verify Tab, Enter, Escape, and arrow keys
- Screen reader tests verify ARIA labels and roles
- Focus management tests ensure modals trap and restore focus
- Accessibility tests should be part of every component test suite
- Manual testing with screen readers (NVDA, VoiceOver) is also important
