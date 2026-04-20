---
id: frontend/testing/user-interactions
name: frontend/testing/user-interactions
kind: reference
domain: frontend
topics: [testing, user interactions]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Testing User Interactions

## When to use

Use this document when:

- Testing form submissions and validation
- Simulating user clicks and keyboard interactions
- Testing dropdown selections
- Verifying user interaction flows

## Rules

- Always use `userEvent` for simulating user interactions (not fireEvent)
- Use `userEvent.setup()` before interactions
- Use `waitFor` for async assertions
- Test user behavior, not implementation details
- Use accessible queries (getByRole, getByLabelText)

## Examples

### Good example

```typescript
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { renderComponent, setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

// Form Submission
describe('LoginForm', () => {
  it('should submit form with valid credentials', async () => {
    const user = userEvent.setup();
    server.use(
      http.post('/api/auth/login', async ({ request }) => {
        const body = await request.json();
        return HttpResponse.json({
          data: { user: { id: '1', email: body.email }, token: 'fake-jwt-token' },
          success: true,
        });
      }),
    );

    renderComponent(<LoginForm />);

    const emailInput = screen.getByLabelText(/email/i);
    const passwordInput = screen.getByLabelText(/password/i);
    const submitButton = screen.getByRole('button', { name: /sign in/i });

    await user.type(emailInput, 'test@example.com');
    await user.type(passwordInput, 'password123');
    await user.click(submitButton);

    await waitFor(() => {
      expect(screen.getByText(/welcome/i)).toBeInTheDocument();
    });
  });
});

// Form Validation
it('should display validation error for invalid email', async () => {
  const user = userEvent.setup();
  renderComponent(<LoginForm />);

  const emailInput = screen.getByLabelText(/email/i);
  await user.type(emailInput, 'invalid-email');
  await user.tab(); // Trigger blur event

  expect(screen.getByText(/valid email/i)).toBeInTheDocument();
});

// Keyboard Navigation
it('should support keyboard navigation', async () => {
  const user = userEvent.setup();
  const onEnroll = jest.fn();

  renderComponent(<CourseCard course={mockCourse} onEnroll={onEnroll} />);

  const enrollButton = screen.getByRole('button', { name: /enroll/i });
  enrollButton.focus();
  await user.keyboard('{Enter}');

  expect(onEnroll).toHaveBeenCalledWith(mockCourse.id);
});

// Click Interactions
it('should handle button clicks', async () => {
  const user = userEvent.setup();
  const handleClick = jest.fn();

  renderComponent(<Button onClick={handleClick}>Click me</Button>);

  await user.click(screen.getByRole('button', { name: /click me/i }));

  expect(handleClick).toHaveBeenCalledTimes(1);
});

// Select Options
it('should select dropdown option', async () => {
  const user = userEvent.setup();
  renderComponent(<SelectForm />);
  const select = screen.getByLabelText(/difficulty/i);
  await user.selectOptions(select, 'BEGINNER');
  expect(select).toHaveValue('BEGINNER');
});
```

### Bad example

```typescript
// ❌ Bad: Using fireEvent instead of userEvent
fireEvent.click(button);

// ❌ Bad: Not using waitFor for async operations
await user.click(button);
expect(screen.getByText(/success/i)).toBeInTheDocument(); // May fail

// ❌ Bad: Testing implementation details
expect(component.state.isSubmitting).toBe(true);
```

## Anti-patterns

- Using fireEvent instead of userEvent
- Not using waitFor for async assertions
- Testing implementation details instead of behavior
- Not using accessible queries
- Not setting up userEvent before interactions

## Notes

- Always use `userEvent` for interactions - it simulates real user behavior
- Use `userEvent.setup()` before interactions
- Use `waitFor` for async assertions after user interactions
- Test what users see and do, not internal component state
- Use accessible queries (getByRole, getByLabelText) for better tests
