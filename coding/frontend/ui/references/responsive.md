---
id: fe-ui/responsive
name: fe-ui/responsive
kind: reference
domain: frontend-ui
topics: [responsive, design, ui, ux]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# Responsive Design

## When to use

Use this document when:

- Creating responsive layouts
- Adapting components for different screen sizes
- Using Chakra UI responsive props
- Implementing mobile-first designs

## Rules

- Use Chakra UI responsive props (array or object syntax)
- Follow mobile-first approach
- Use consistent breakpoint values
- Test at all breakpoints
- Hide/show content based on screen size when appropriate

## Examples

### Good example

```typescript
import { Button } from '@mentory/ui-components';

// Array syntax (mobile-first)
<Button size={['sm', 'md', 'lg']}>
  Responsive Button
</Button>

// Object syntax
<Button
  width={{ base: '100%', md: '50%', lg: '300px' }}
  fontSize={{ base: 'sm', md: 'md', lg: 'lg' }}
>
  Responsive Button
</Button>

// Responsive Grid
import { Grid } from '@mentory/ui-components';

<Grid templateColumns={{ base: '1fr', md: 'repeat(2, 1fr)', lg: 'repeat(3, 1fr)' }} gap={4}>
  {courses.map(course => (
    <CourseCard key={course.id} course={course} />
  ))}
</Grid>

// Responsive Text
<Heading fontSize={{ base: 'xl', md: '2xl', lg: '3xl' }}>{t('welcome')}</Heading>

// Responsive Spacing
<Box padding={{ base: 4, md: 6, lg: 8 }} margin={{ base: 2, md: 4 }}>
  Content
</Box>

// Hide/Show Based on Screen Size
import { Box } from '@mentory/ui-components';

// Hide on mobile, show on desktop
<Box display={{ base: 'none', md: 'block' }}>
  Desktop Only Content
</Box>

// Show on mobile, hide on desktop
<Box display={{ base: 'block', md: 'none' }}>
  Mobile Only Content
</Box>
```

### Bad example

```typescript
// ❌ Bad: Not using responsive props
<Button size="lg">Button</Button> // Same size on all screens

// ❌ Bad: Using media queries instead of Chakra props
@media (max-width: 768px) {
  .button { width: 100%; }
}

// ❌ Bad: Not following mobile-first
<Button width={{ lg: '100%', base: '50%' }}> // Should be base first
```

## Anti-patterns

- Not using responsive props
- Using CSS media queries instead of Chakra props
- Not following mobile-first approach
- Inconsistent breakpoint usage
- Not testing at all breakpoints

## Notes

### Breakpoint Values

- `base` - 0px (mobile)
- `sm` - 480px
- `md` - 768px (tablet)
- `lg` - 992px (desktop)
- `xl` - 1280px (large desktop)
- `2xl` - 1536px (extra large)

### Responsive Syntax

- **Array syntax**: `[base, sm, md, lg]` - Mobile-first, applies to breakpoint and up
- **Object syntax**: `{ base: value, md: value }` - More explicit control

### Common Patterns

- Responsive grids: 1 column mobile, 2 tablet, 3+ desktop
- Responsive text: Smaller on mobile, larger on desktop
- Responsive spacing: Tighter on mobile, more spacious on desktop
- Hide/show: Show/hide content based on screen size
