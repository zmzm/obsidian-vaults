---
id: fe-ui/styling
name: fe-ui/styling
kind: reference
domain: frontend-ui
topics: [styling, design, ui, ux]
priority: high
status: stable
canonical: false
updated: 2026-04-16
---

# Styling Guidelines

## When to use

Use this document when:

- Customizing component styles
- Using Chakra styling props
- Understanding theme configuration
- Applying consistent spacing and typography

## Rules

- DO NOT modify Chakra UI theme directly
- DO request changes to the ui-components library theme
- DO use the provided component variants and props
- DO use Chakra's styling props (sx, chakra prop) when needed
- Use semantic colors from the theme
- Use consistent spacing scale
- Follow typography system

## Examples

### Good example

```typescript
import { Button } from '@mentory/ui-components';

// Using Chakra's styling props (when necessary)
<Button
  bg="blue.500"
  color="white"
  _hover={{ bg: 'blue.600' }}
>
  Custom Styled Button
</Button>

// Color Palette
// Status colors
<Button bg="green.500">Success</Button>
<Button bg="red.500">Error</Button>
<Button bg="blue.500">Info</Button>
<Button bg="yellow.500">Warning</Button>

// Spacing
<Box p={4} m={2} gap={3}>
  {/* p={4} = 16px padding */}
  {/* m={2} = 8px margin */}
  {/* gap={3} = 12px gap */}
</Box>

// Typography
<Heading size="lg">Large Heading</Heading>
<Text fontSize="md">Medium Text</Text>
<Text fontSize="sm">Small Text</Text>

// Accessibility in Styling
// Proper labeling
<Label htmlFor="email">{t('email')}</Label>
<Input id="email" type="email" aria-required="true" />

// ARIA labels for icon buttons
<Button aria-label={t('close')}>
  <X />
</Button>

// Disabled state
<Button disabled aria-disabled="true">
  {t('submit')}
</Button>
```

### Bad example

```typescript
// ❌ Bad: Using inline styles
<div style={{ padding: '16px', color: 'red' }}>

// ❌ Bad: Modifying theme directly
const theme = extendTheme({
  colors: { custom: '#000' },
});

// ❌ Bad: Not using semantic colors
<Button bg="#3B82F6">Button</Button> // Should use theme color
```

## Anti-patterns

- Using inline styles instead of Chakra props
- Modifying Chakra UI theme directly
- Not using semantic colors from theme
- Inconsistent spacing usage
- Not following typography system

## Notes

### Theme and Styling

The ui-components library uses a centralized theme configuration. To customize styles:

1. **DO NOT** modify Chakra UI theme directly
2. **DO** request changes to the ui-components library theme
3. **DO** use the provided component variants and props
4. **DO** use Chakra's styling props (sx, chakra prop) when needed

### Color Palette

- Use semantic colors from the theme
- Status colors: green (success), red (error), blue (info), yellow (warning)
- Don't hardcode color values

### Spacing

- Use consistent spacing scale (multiples of 4px)
- p={4} = 16px padding, m={2} = 8px margin
- Use gap for flex/grid layouts

### Typography

- Follow typography system (Heading, Text components)
- Use consistent font sizes (sm, md, lg, xl, 2xl, etc.)
- Maintain readable line heights

### Testing UI Components

```typescript
import { render, screen } from '@testing-library/react';
import { ChakraProvider } from '@mentory/ui-components';

function renderComponent(ui: React.ReactElement) {
  return render(<ChakraProvider>{ui}</ChakraProvider>);
}

it('should render button', () => {
  renderComponent(<Button>Click me</Button>);
  expect(screen.getByRole('button', { name: /click me/i })).toBeInTheDocument();
});
```
