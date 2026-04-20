---
id: frontend/testing/test-utils
name: frontend/testing/test-utils
kind: reference
domain: frontend
topics: [testing, test utils]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Test Utils Reference

## When to use

Use this document when:

- Understanding available test utilities
- Setting up components for testing
- Using pre-configured mocks
- Understanding MSW handlers

## Rules

- Always use `renderComponent` from `@mentory/test-utils`
- Always use `setupMswServer` from `@mentory/test-utils`
- Don't manually mock providers (already in test-utils)
- Override MSW handlers using `server.use()` when needed
- Use pre-configured handlers when possible

## Current exceptions

- `temporary`: some legacy tests imported `renderComponent` via relative paths (`test-utils/test-utils`).
  Exit condition: all frontend tests import test utilities from `@mentory/test-utils` only.

## Examples

### Good example

```typescript
// renderComponent
import { renderComponent } from '@mentory/test-utils';

renderComponent(<MyComponent />);

// setupMswServer
import { setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

// Using i18n in Tests
it('should display translated text', () => {
  renderComponent(<WelcomePage />);
  // Translation keys are returned as-is by the mock
  expect(screen.getByText('welcome.title')).toBeInTheDocument();
});
```

### Bad example

```typescript
// ❌ Bad: Creating custom render
const customRender = (ui) => render(ui, { wrapper: MyWrapper });

// ❌ Bad: Manual MSW setup
import { setupServer } from 'msw/node';
const server = setupServer();
beforeAll(() => server.listen());

// ❌ Bad: Manually mocking providers
jest.mock('react-i18next', () => ({ ... }));
```

## Anti-patterns

- Creating custom render utilities
- Manually setting up MSW
- Manually mocking providers
- Not using test-utils utilities
- Duplicating provider mocks

## Notes

### Available Utilities

#### renderComponent

Wraps component with all required providers:

- QueryClientProvider (with retry disabled)
- i18n Provider (mocked)
- Theme Provider (mocked)
- Router (mocked)

#### setupMswServer

Sets up MSW server with default handlers:

- Automatically handles `beforeAll()` - Starts server
- Automatically handles `afterEach()` - Resets handlers
- Automatically handles `afterAll()` - Closes server
- Uses `onUnhandledRequest: 'error'` for better debugging

### Pre-configured Mocks

#### Clerk Authentication

- `ClerkProvider`, `useUser`, `useAuth`, `UserButton`, `SignIn`, `SignUp`
- Pre-configured with mock user data

#### i18n (react-i18next)

- `useTranslation` hook with translation function
- Returns translation keys as-is for easy testing
- Pre-configured translations for user and auth modules

#### React Router

- `BrowserRouter`, `useNavigate`, `useSearchParams`, `useLocation`, `Link`
- Mock navigation functions

#### Theme Provider (next-themes)

- `ThemeProvider`, `useTheme`
- Default light theme

### Pre-configured MSW Handlers

Default handlers available for:

- Auth endpoints (`/api/auth/*`)
- User endpoints (`/api/users/*`)
- Dashboard endpoints (`/api/dashboard/*`)
- File upload (`/api/upload/*`)

Override in tests using `server.use()`.
