---
id: frontend/testing/query-selectors
name: frontend/testing/query-selectors
kind: reference
domain: frontend
topics: [testing, query selectors]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Query Selectors Priority

## When to use

Use this document when:

- Choosing which query method to use
- Understanding query selector priorities
- Testing accessible components
- Writing maintainable tests

## Rules

- Use queries in priority order (most accessible first)
- Prefer `getByRole` for interactive elements
- Use `getByLabelText` for form fields
- Use `getByText` for non-interactive content
- Only use `getByTestId` as last resort

## Examples

### Good example

```typescript
// 1. getByRole (Most Accessible)
screen.getByRole('button', { name: /submit/i });
screen.getByRole('textbox', { name: /email/i });
screen.getByRole('heading', { name: /welcome/i });
screen.getByRole('article');
screen.getByRole('alert');

// 2. getByLabelText (For Form Fields)
screen.getByLabelText(/email address/i);
screen.getByLabelText(/password/i);
screen.getByLabelText(/search courses/i);

// 3. getByPlaceholderText (If No Label)
screen.getByPlaceholderText(/search courses/i);
screen.getByPlaceholderText(/enter your email/i);

// 4. getByText (For Non-Interactive Content)
screen.getByText(/welcome to mentory/i);
screen.getByText('React Basics');
screen.getByText(/loading/i);

// 5. getByTestId (Last Resort Only)
screen.getByTestId('user-profile-card');
screen.getByTestId('course-list-item');
```

### Bad example

```typescript
// ❌ Bad: Querying by className
container.querySelector('.user-card');

// ❌ Bad: Querying by internal IDs
screen.getByTestId('submit-button'); // Should use getByRole

// ❌ Bad: Using getByText for interactive elements
screen.getByText('Submit'); // Should use getByRole('button')
```

## Anti-patterns

- Querying by className or internal IDs
- Using getByTestId for interactive elements
- Using getByText for buttons and links
- Not using accessible queries
- Querying implementation details

## Notes

### Query Priority Order

1. **getByRole** - Most accessible, tests what screen readers see
2. **getByLabelText** - For form fields with labels
3. **getByPlaceholderText** - If no label available
4. **getByText** - For non-interactive content
5. **getByTestId** - Last resort only, for elements that can't be queried otherwise

### Common Roles

- `button` - Clickable buttons
- `textbox` - Input fields
- `heading` - h1-h6 elements
- `article` - Article content
- `alert` - Alert messages
- `dialog` - Modal dialogs
- `navigation` - Navigation menus
- `list` - Lists
- `listitem` - List items

### Querying Multiple Elements

```typescript
// Get all buttons
screen.getAllByRole('button');

// Get all list items
screen.getAllByRole('listitem');

// Get all headings
screen.getAllByRole('heading');
```

### Querying with Options

```typescript
// Exact text match
screen.getByRole('button', { name: 'Submit' });

// Case-insensitive regex
screen.getByRole('button', { name: /submit/i });

// Partial match
screen.getByRole('button', { name: /save/i });
```
