---
id: frontend/accessibility/core-principles
name: frontend/accessibility/core-principles
kind: reference
domain: frontend
topics: [accessibility, core principles]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Accessibility Core Principles

## When to use

Use this document when:

- Implementing accessibility features in React components
- Ensuring WCAG AA compliance
- Adding keyboard navigation support
- Creating accessible forms and interactive elements
- Testing components with screen readers

## Rules

- Use semantic HTML (nav, main, article, button, not div)
- Add ARIA labels to interactive elements without visible text
- Maintain WCAG AA color contrast (4.5:1 for text)
- Support full keyboard navigation (Tab, Enter, Escape, arrows)
- Include focus indicators on all interactive elements
- Use ARIA roles when semantic HTML insufficient
- Add alt text to all meaningful images
- Implement skip links for navigation
- Test with screen readers (NVDA, VoiceOver)
- Provide loading states for async operations

## Examples

### Good example

```typescript
// ✅ Good: Use semantic HTML
<nav>
  <ul>
    <li><a href="/courses">Courses</a></li>
  </ul>
</nav>
<main>
  <article>
    <h1>Course Title</h1>
  </article>
</main>

// ✅ Good: Proper ARIA labels
<button aria-label={t('close')} onClick={onClose}>
  <X />
</button>
<div role="alert" aria-live="assertive">
  {error.message}
</div>
```

### Bad example

```typescript
// ❌ Bad: Using divs for interactive elements
<div onClick={onClose}>
  <X />
</div>

// ❌ Bad: Missing ARIA labels
<button onClick={onClose}>
  <X />
</button>
```

## Anti-patterns

- Use divs for buttons or links
- Rely solely on color to convey information
- Remove focus outlines without replacement
- Use placeholder as label
- Auto-play videos with sound

## Notes

- Semantic HTML should always be preferred over ARIA roles when possible
- Focus indicators must be visible and meet contrast requirements
- Screen reader testing should be part of the development workflow
- Color contrast ratios apply to both light and dark modes
