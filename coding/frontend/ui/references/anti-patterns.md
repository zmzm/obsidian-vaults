---
id: fe-ui/anti-patterns
name: fe-ui/anti-patterns
kind: reference
domain: frontend-ui
topics: [anti-patterns]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# UI Anti-Patterns

## When to use

Use this document when:

- Reviewing UI component usage
- Identifying common UI mistakes
- Understanding what to avoid
- Refactoring existing UI code

## Rules

- NEVER import directly from `@chakra-ui/*` packages
- ALWAYS import from `@mentory/ui-components`
- NEVER mix UI libraries
- NEVER use raw HTML elements for interactive UI
- NEVER create custom wrappers around Chakra components
- NEVER use inline styles

## Examples

### Good example

```typescript
// ✅ Good: Import from @mentory/ui-components
import { Button, useToast } from '@mentory/ui-components';

// ✅ Good: Use Button component
<Button onClick={handleClick}>
  {t('clickMe')}
</Button>

// ✅ Good: Use Chakra's styling props
import { Box } from '@mentory/ui-components';
<Box p={4} color="red.500">
```

### Bad example

```typescript
// ❌ Bad: Import Directly from Chakra UI
import { Button } from '@chakra-ui/react';
import { useToast } from '@chakra-ui/react';

// ❌ Bad: Mix UI Libraries
import { Button as MuiButton } from '@mui/material';

// ❌ Bad: Use Raw HTML Elements for Interactive UI
<div onClick={handleClick} style={{ cursor: 'pointer', background: 'blue' }}>
  Click me
</div>

// ❌ Bad: Create Custom Wrappers Around Chakra Components
import { Button as ChakraButton } from '@chakra-ui/react';

export function MyButton(props) {
  return <ChakraButton {...props} />;
}

// ❌ Bad: Use Inline Styles
<div style={{ padding: '16px', color: 'red' }}>
```

## Anti-patterns

- Import directly from `@chakra-ui/*` packages
- Mix UI libraries (Material-UI, Ant Design, etc.)
- Use raw HTML elements for interactive UI
- Create custom wrappers around Chakra components
- Use inline styles instead of Chakra props
- Bypass the ui-components library

## Notes

### Migration Notes

**Previous**: shadcn/ui + Tailwind CSS **Current**: Chakra UI via @mentory/ui-components

**Key Changes:**

- All imports now from `@mentory/ui-components` instead of `@/shared/ui/*`
- No more Tailwind CSS classes (use Chakra's styling props)
- No more shadcn CLI commands
- Provider changed from individual component providers to `ChakraProvider`
- Responsive design uses Chakra's array/object syntax instead of Tailwind breakpoints

### Why Use @mentory/ui-components

- Provides consistent API wrapper around Chakra UI
- Ensures design system consistency
- Single source of truth for UI components
- Direct imports bypass this abstraction and break consistency
