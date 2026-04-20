---
id: frontend/accessibility/aria-patterns
name: frontend/accessibility/aria-patterns
kind: reference
domain: frontend
topics: [accessibility, aria patterns]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# ARIA Patterns

## When to use

Use this document when:

- Adding ARIA attributes to improve screen reader support
- Implementing live regions for dynamic content
- Creating accessible loading and status states
- Using ARIA roles when semantic HTML is insufficient

## Rules

- Use ARIA labels for interactive elements without visible text
- Use aria-live regions for dynamic content updates
- Use aria-busy for loading states
- Use semantic HTML when possible, ARIA as supplement
- Provide aria-describedby for form validation messages
- Use role attributes only when necessary

## Examples

### Good example

```typescript
// Icon buttons without visible text
<button aria-label={t('close')} onClick={onClose}>
  <X />
</button>

// Search input with label
<input
  type="text"
  aria-label={t('searchCourses')}
  placeholder={t('searchPlaceholder')}
/>

// Live region for dynamic content
export const Toast: React.FC<ToastProps> = ({ message }) => {
  return (
    <div role="status" aria-live="polite" aria-atomic="true">
      {message}
    </div>
  );
};

// Loading state with aria-busy
export const CourseList: React.FC = () => {
  const { courses, isLoading } = useCourses();
  if (isLoading) {
    return (
      <div role="status" aria-live="polite" aria-busy="true">
        <Loader2 className="animate-spin" />
        <span className="sr-only">{t('loading')}</span>
      </div>
    );
  }
  return (
    <div role="region" aria-label={t('coursesList')}>
      {courses.map((course) => (
        <CourseCard key={course.id} course={course} />
      ))}
    </div>
  );
};
```

### Bad example

```typescript
// ❌ Bad: Missing ARIA label for icon button
<button onClick={onClose}>
  <X />
</button>

// ❌ Bad: Using role="button" instead of <button>
<div role="button" onClick={handleClick}>Click me</div>

// ❌ Bad: Missing aria-busy for loading state
<div>
  <Loader2 className="animate-spin" />
</div>
```

## Anti-patterns

- Using ARIA roles when semantic HTML would work
- Missing ARIA labels on icon-only buttons
- Not announcing dynamic content changes
- Using role="button" instead of `<button>` element
- Overusing ARIA attributes unnecessarily

## Notes

- Prefer semantic HTML over ARIA roles when possible
- aria-live="polite" for non-urgent updates, "assertive" for urgent
- aria-atomic="true" announces entire region, "false" announces only changes
- Common ARIA roles: `alert`, `status`, `dialog`, `menu`, `region`
- Screen readers announce aria-live regions when content changes
