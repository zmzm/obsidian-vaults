---
id: frontend/testing/mutations
name: frontend/testing/mutations
kind: reference
domain: frontend
topics: [testing, mutations]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Testing Mutations

## When to use

Use this document when:

- Testing POST, PATCH, DELETE operations
- Verifying mutation success handling
- Testing mutation error handling
- Testing form submissions that trigger mutations

## Rules

- Mock mutation endpoints with MSW
- Test both success and error scenarios
- Verify cache invalidation after successful mutations
- Test user feedback (toasts, success messages)
- Use userEvent for form interactions

## Examples

### Good example

```typescript
import { screen, waitFor } from '@testing-library/react';
import userEvent from '@testing-library/user-event';
import { renderComponent, setupMswServer } from '@mentory/test-utils';
import { http, HttpResponse } from 'msw';

const server = setupMswServer();

// Creating Resources (POST)
it('should create course on valid submission', async () => {
  const user = userEvent.setup();
  server.use(
    http.post('/api/courses', async ({ request }) => {
      const body = await request.json();
      return HttpResponse.json(
        {
          data: { id: '1', ...body },
          success: true,
        },
        { status: 201 },
      );
    }),
  );
  renderComponent(<CreateCourseForm />);
  await user.type(screen.getByLabelText(/title/i), 'React Basics');
  await user.click(screen.getByRole('button', { name: /create/i }));
  await waitFor(() => {
    expect(screen.getByText(/success/i)).toBeInTheDocument();
  });
});

// Updating Resources (PATCH)
it('should update course', async () => {
  const user = userEvent.setup();
  server.use(
    http.patch('/api/courses/:id', async ({ request, params }) => {
      const body = await request.json();
      return HttpResponse.json({ data: { id: params.id, ...body }, success: true });
    }),
  );
  renderComponent(<EditCourseForm courseId="1" />);
  await user.clear(screen.getByLabelText(/title/i));
  await user.type(screen.getByLabelText(/title/i), 'Updated Title');
  await user.click(screen.getByRole('button', { name: /save/i }));
  await waitFor(() => {
    expect(screen.getByText(/updated successfully/i)).toBeInTheDocument();
  });
});

// Deleting Resources (DELETE)
it('should delete course', async () => {
  const user = userEvent.setup();
  server.use(http.delete('/api/courses/:id', () => HttpResponse.json({ success: true })));
  renderComponent(<CourseCard course={mockCourse} />);
  await user.click(screen.getByRole('button', { name: /delete/i }));
  await user.click(screen.getByRole('button', { name: /confirm/i }));
  await waitFor(() => {
    expect(screen.queryByText(mockCourse.title)).not.toBeInTheDocument();
  });
});

// Error Handling in Mutations
it('should handle mutation errors', async () => {
  const user = userEvent.setup();
  server.use(http.post('/api/courses', () => new HttpResponse(null, { status: 400 })));
  renderComponent(<CreateCourseForm />);
  await user.type(screen.getByLabelText(/title/i), 'Test Course');
  await user.click(screen.getByRole('button', { name: /create/i }));
  await waitFor(() => {
    expect(screen.getByRole('alert')).toHaveTextContent(/error/i);
  });
});
```

### Bad example

```typescript
// ❌ Bad: Not testing error scenarios
it('should create course', async () => {
  // Only testing success, missing error test
});

// ❌ Bad: Not verifying user feedback
it('should create course', async () => {
  // Missing verification of success message
});
```

## Anti-patterns

- Not testing error scenarios
- Not verifying user feedback after mutations
- Not testing confirmation dialogs for destructive actions
- Not using userEvent for interactions
- Not waiting for async operations

## Notes

- Always test both success and error scenarios
- Verify user feedback (toasts, success messages) after mutations
- Test confirmation dialogs for destructive actions (delete)
- Use `userEvent` for form interactions
- Use `waitFor` for async assertions
- Verify cache invalidation by checking updated data
