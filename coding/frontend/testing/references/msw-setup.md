---
id: frontend/testing/msw-setup
name: frontend/testing/msw-setup
kind: reference
domain: frontend
topics: [testing, msw setup]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# MSW Setup Guide

## When to use

Use this document when:

- Setting up MSW for API mocking in tests
- Overriding default MSW handlers
- Creating delayed responses for loading tests
- Understanding pre-configured handlers

## Rules

- **ALWAYS** use `setupMswServer()` from `@mentory/test-utils`
- Never manually set up MSW (beforeAll, afterEach, afterAll)
- Override handlers using `server.use()` in individual tests
- Use delayed responses for testing loading states
- Don't duplicate provider mocks already in test-utils

## Examples

### Good example

```typescript
import { setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

describe('MyComponent', () => {
  it('should fetch data', async () => {
    server.use(
      http.get('/api/users/profile', () => {
        return HttpResponse.json({
          data: { id: '1', email: 'test@example.com' },
          success: true,
        });
      }),
    );
    // ... test implementation
  });
});

// Overriding Handlers
it('should handle custom response', async () => {
  server.use(
    http.get('/api/courses', () => {
      return HttpResponse.json({
        data: [{ id: '1', title: 'Custom Course' }],
        success: true,
      });
    }),
  );
  // ... test
});

// Delayed Responses for Loading Tests
it('should show loading state', async () => {
  server.use(
    http.get('/api/courses', async () => {
      await new Promise(resolve => setTimeout(resolve, 100));
      return HttpResponse.json({ data: [], success: true });
    }),
  );
  // ... test loading spinner
});
```

### Bad example

```typescript
// ❌ Bad: Manual MSW setup
import { setupServer } from 'msw/node';
const server = setupServer();
beforeAll(() => server.listen());
afterEach(() => server.resetHandlers());
afterAll(() => server.close());

// ❌ Bad: Not using test-utils
const server = setupServer(...); // Should use setupMswServer()
```

## Anti-patterns

- Manually setting up MSW (beforeAll, afterEach, afterAll)
- Not using setupMswServer from test-utils
- Duplicating provider mocks
- Not overriding handlers when needed
- Creating custom MSW setup

## Notes

### Using Test Utils (REQUIRED)

**ALWAYS** use the `setupMswServer()` utility from `@mentory/test-utils`. The utility automatically:

- Sets up MSW server with all default handlers
- Calls `beforeAll()` to start the server with `onUnhandledRequest: 'error'`
- Calls `afterEach()` to reset handlers after each test
- Calls `afterAll()` to close the server

**Do NOT** manually call `beforeAll`, `afterEach`, or `afterAll` for MSW - it's handled by the utility.

### Pre-configured Handlers

The `@mentory/test-utils` library contains pre-configured handlers for:

- **Auth endpoints**: `/api/auth/login`, `/api/auth/logout`, `/api/auth/forgot-password`, `/api/auth/reset-password`,
  `/api/auth/verify-email`
- **User endpoints**: `/api/users`, `/api/users/:id`, `/api/users/profile`, `/api/users/:id/profile-completion`
- **Dashboard endpoints**: `/api/dashboard/stats`, `/api/dashboard/recent-activity`
- **File upload**: `/api/upload/avatar`, `/api/users/profile/avatar`

These handlers return standardized responses. Override them in individual tests using `server.use()` when you need different behavior.
