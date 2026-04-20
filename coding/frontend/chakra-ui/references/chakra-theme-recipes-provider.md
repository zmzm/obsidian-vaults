---
id: frontend/chakra-ui/chakra-theme-recipes-provider
name: frontend/chakra-ui/chakra-theme-recipes-provider
kind: reference
domain: frontend
topics: [chakra-ui, chakra theme recipes provider]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra Theme Recipes & Provider

## When to use

Use this document when:

- Overriding default Chakra component styles with recipes
- Creating theme factory functions for dynamic themes
- Setting up ChakraProvider with custom theme system
- Understanding recipe overrides and provider configuration

## Rules

- Override default Chakra styles using recipes in theme config
- Use theme factory pattern for dynamic theme creation
- Pass system configuration to ChakraProvider via `value` prop
- Use semantic tokens in recipes for light/dark mode support
- Export theme factory functions for reusable theme creation

## Examples

### Good example

```typescript
// Component Recipes - Override default Chakra styles
recipes: {
  badge: {
    base: { fontWeight: 'semibold' },  // Base styles
    variants: {
      variant: {
        solid: {
          bg: 'colorPalette.solid',
          color: 'colorPalette.contrast'
        },
        subtle: {
          bg: 'colorPalette.50',
          color: 'colorPalette.700'
        }
      }
    }
  }
}

// Theme Factory Pattern
export const createChakraDefaultSystem = (mode: 'light' | 'dark' = 'light') => {
  return createSystem(
    defaultConfig,
    defineConfig({
      theme: {
        semanticTokens: {
          colors: {
            bg: { value: mode === 'light' ? 'white' : 'gray.900' },
          },
        },
      },
    }),
  );
};

// Provider Setup
import { ChakraProvider } from '@mentory/ui-components';
import { system } from '@mentory/ui-themes/chakra';

<ChakraProvider value={system}>
  <App />
</ChakraProvider>
```

### Bad example

```typescript
// ❌ Bad: Not using value prop
<ChakraProvider>
  <App />
</ChakraProvider> // Missing system configuration

// ❌ Bad: Creating system without factory pattern
const system = createSystem(...); // Should be a factory function for flexibility

// ❌ Bad: Not using semantic tokens in recipes
recipes: {
  badge: {
    variants: {
      solid: {
        bg: '#3B82F6', // Should use semantic tokens
      }
    }
  }
}
```

## Anti-patterns

- Not passing system to ChakraProvider via `value` prop
- Creating static system instead of factory function
- Not using semantic tokens in recipe overrides
- Hardcoding theme values instead of using tokens
- Not exporting theme factory for reusability

## Notes

### Component Recipes

Recipes allow you to override default Chakra component styles:

- Define in `recipes` object in theme config
- Use `base` for styles applied to all variants
- Use `variants` for variant-specific styles
- Reference semantic tokens for light/dark mode support

### Theme Factory Pattern

Theme factory functions allow dynamic theme creation:

- Accept parameters (e.g., mode, custom tokens)
- Return configured system using `createSystem`
- Enable theme switching and customization
- Match MUI pattern for consistency

### Provider Setup

ChakraProvider requires system configuration:

- Import system from theme package
- Pass via `value` prop
- Provider wraps entire application
- System is available to all components
