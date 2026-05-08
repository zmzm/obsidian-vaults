---
id: chakra-ui/anti-patterns
name: chakra-ui/anti-patterns
kind: reference
domain: frontend-ui
topics: [chakra-ui, anti-patterns, semantic tokens]
priority: high
status: stable
canonical: false
updated: 2026-05-08
---

# Anti-Patterns (Required)

## A1. CSS var bypass in TSX

Avoid:

```tsx
color="var(--chakra-colors-text-tertiary)"
```

Prefer:

```tsx
color="text-tertiary"
```

Prefer for icons:

```tsx
<Box color="text-tertiary">
  <Icon color="currentColor" />
</Box>
```

## A2. Inline style for common layout

Avoid:

```tsx
style={{ textDecoration: 'none', display: 'block', height: '100%' }}
```

Prefer Chakra props, a className utility, or a shared component.

## A3. Repeated heading and description blocks

Avoid manual `Text` plus `Text` blocks repeated per page.

Prefer:

```tsx
<SectionHeader ... />
```

## A4. Repeated subtle cards

Avoid repeating this structure everywhere:

```tsx
<Box p={4} bg="surface-subtle" borderRadius="md">
```

Prefer:

```tsx
<SurfaceBox ... />
```

## Allowed Exceptions

Inline style is allowed only for:

- dynamic width/height values computed at runtime, such as progress width
- charting/SVG APIs requiring a style object
- cases where Chakra props cannot express required behavior

Exception must be documented in a code comment when not obvious.
