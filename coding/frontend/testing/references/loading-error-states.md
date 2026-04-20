---
id: frontend/testing/loading-error-states
name: frontend/testing/loading-error-states
kind: reference
domain: frontend
topics: [testing, loading error states]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Testing Loading & Error States

## When to use

Use this document when:

- Testing loading states during data fetching
- Testing error states (404, 500, network errors)
- Testing empty states when no data is returned
- Verifying error handling in components

## Rules

- Use delayed responses to test loading states
- Test all error scenarios (404, 500, network errors)
- Test empty states when data array is empty
- Use `waitFor` for async state changes
- Verify error messages are displayed correctly

## Examples

### Good example

```typescript
import { screen, waitFor } from '@testing-library/react';
import { renderComponent, setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

// Loading State
it('should display loading spinner while fetching', () => {
  server.use(
    http.get('/api/courses', async () => {
      await new Promise(resolve => setTimeout(resolve, 100));
      return HttpResponse.json({ data: [], success: true });
    }),
  );
  renderComponent(<CourseList />);
  expect(screen.getByText(/loading/i)).toBeInTheDocument();
});

it('should display courses after loading', async () => {
  const mockCourses = [{ id: '1', title: 'React Basics' }];
  server.use(http.get('/api/courses', () => HttpResponse.json({ data: mockCourses, success: true })));
  renderComponent(<CourseList />);
  await waitFor(() => {
    expect(screen.getByText('React Basics')).toBeInTheDocument();
  });
});

// 404 Not Found
it('should display error alert on 404', async () => {
  server.use(http.get('/api/users/profile', () => new HttpResponse(null, { status: 404 })));
  renderComponent(<UserProfilePage />);
  await waitFor(() => {
    expect(screen.getByRole('alert')).toHaveTextContent(/not found/i);
  });
});

// Network Error
it('should display error alert on network error', async () => {
  server.use(http.get('/api/users/profile', () => HttpResponse.error()));
  renderComponent(<UserProfilePage />);
  await waitFor(() => {
    expect(screen.getByRole('alert')).toHaveTextContent(/error/i);
  });
});

// Server Error (500)
it('should handle server errors', async () => {
  server.use(http.get('/api/courses', () => new HttpResponse(null, { status: 500 })));
  renderComponent(<CourseList />);
  await waitFor(() => {
    expect(screen.getByText(/server error/i)).toBeInTheDocument();
  });
});

// Empty States
it('should display empty state when no data', async () => {
  server.use(http.get('/api/courses', () => HttpResponse.json({ data: [], success: true })));
  renderComponent(<CourseList />);
  await waitFor(() => {
    expect(screen.getByText(/no courses found/i)).toBeInTheDocument();
  });
});
```

### Bad example

```typescript
// ❌ Bad: Not testing loading state
it('should display courses', async () => {
  server.use(...);
  renderComponent(<CourseList />);
  // Missing loading state test
});

// ❌ Bad: Not testing error states
it('should display courses', async () => {
  server.use(http.get('/api/courses', () => HttpResponse.json({ data: [] })));
  renderComponent(<CourseList />);
  // Missing error state test
});
```

## Anti-patterns

- Not testing loading states
- Not testing error states
- Not testing empty states
- Not using waitFor for async state changes
- Not verifying error messages are displayed

## Notes

- Use delayed responses to test loading states
- Test all error scenarios: 404, 500, network errors
- Test empty states when data array is empty
- Always use `waitFor` for async state changes
- Verify error messages match expected text
- Test that error alerts are properly displayed
