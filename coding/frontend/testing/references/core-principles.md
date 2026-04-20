---
id: frontend/testing/core-principles
name: frontend/testing/core-principles
kind: reference
domain: frontend
topics: [testing, core principles]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Testing Core Principles

## When to use

Use this document when:

- Writing component tests
- Setting up test utilities
- Understanding testing best practices
- Ensuring test coverage requirements

## Rules

- Use React Testing Library (RTL) for all component tests
- Use userEvent for simulating user interactions (not fireEvent)
- Use renderComponent from `@mentory/test-utils` library
- Use setupMswServer from `@mentory/test-utils` library
- Follow AAA pattern: Arrange → Act → Assert
- Achieve 80% minimum code coverage
- Test user behavior, not implementation details
- Prefer getByRole over other queries (accessibility)
- Test loading, success, and error states
- Use waitFor for async assertions
- Test form validation and submissions
- Test accessibility (ARIA labels, keyboard navigation)

## Examples

### Good example

```typescript
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { renderComponent, setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

describe('UserProfilePage', () => {
  it('should display user profile', async () => {
    server.use(http.get('/api/users/profile', () => HttpResponse.json({ data: mockProfile, success: true })));
    renderComponent(<UserProfilePage />);
    await waitFor(() => {
      expect(screen.getByText(/expected text/i)).toBeInTheDocument();
    });
  });
});
```

### Bad example

```typescript
// ❌ Bad: Mocking hook files
jest.mock('./UserProfilePage.hook.ts');

// ❌ Bad: Using fireEvent instead of userEvent
fireEvent.click(button);

// ❌ Bad: Querying by className
screen.getByClassName('user-profile');

// ❌ Bad: Not using test utils
render(<UserProfilePage />, { wrapper: AllTheProviders });
```

## Anti-patterns

- Mock custom hook files (`.hook.ts` or `.hook.tsx`)
- Create custom render utilities (use renderComponent)
- Manually set up MSW (use setupMswServer)
- Duplicate provider mocks (already in test-utils)
- Query by className or internal IDs
- Use fireEvent (use userEvent instead)
- Test implementation details instead of behavior

### Migration Exception

Temporary migration exception: shared infrastructure hooks used only for app wiring such as auth, router, or i18n may be mocked in
route-level tests until those suites are fully MSW-based.

### Query Priority

- Prefer `getByRole` over other queries
- Use `getByLabelText` for form fields
- Use `getByTestId` only as a last resort
- Never query by className or internal IDs

## Notes

### Critical Rules

**NEVER** mock custom hook files. Hooks contain business logic that should be tested as part of component integration.

**ALWAYS** use utilities from `@mentory/test-utils`:

- `renderComponent` - Wraps component with all required providers
- `setupMswServer` - Sets up MSW server with default handlers

### Coverage Requirements

- Minimum 80% coverage for all files
- Test all user-facing features
- Test loading, success, and error states
- Test accessibility (ARIA labels, keyboard navigation)
- Test form validation and submissions
