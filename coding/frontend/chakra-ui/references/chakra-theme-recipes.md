---
id: frontend/chakra-ui/chakra-theme-recipes
name: frontend/chakra-ui/chakra-theme-recipes
kind: reference
domain: frontend
topics: [chakra-ui, chakra theme recipes]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra Theme Recipes

## When to use

Use this document when:

- Creating component recipes with variants
- Defining component styling patterns
- Setting up dark mode support in recipes
- Registering recipes in theme configuration

## Rules

- Use `defineRecipe()` with `base`, `variants`, and `defaultVariants`
- Always specify `defaultVariants` in recipes
- Use `colorPalette` or token references, never hardcode colors
- Use `_dark` condition for dark mode variants
- Register recipes in theme config under `recipes` key

## Examples

### Good example

```typescript
import { defineRecipe } from '@chakra-ui/react';

export const badgeRecipe = defineRecipe({
  base: {
    display: 'inline-flex',
    fontWeight: 'semibold',
    fontSize: 'xs',
    borderRadius: '4px',
  },
  variants: {
    variant: {
      solid: {
        bg: 'colorPalette.500',
        color: 'white',
      },
      outline: {
        borderWidth: '1px',
        borderColor: 'colorPalette.500',
      },
    },
    size: {
      sm: { px: '1.5', py: '0.5' },
      md: { px: '2', py: '0.5' },
    },
  },
  defaultVariants: {
    variant: 'solid',
    size: 'md',
  },
});

// Dark mode pattern
subtle: {
  bg: 'colorPalette.100',
  color: 'colorPalette.800',
  _dark: {
    bg: 'colorPalette.800',
    color: 'colorPalette.100',
  },
},

// Registering in theme
import { createSystem, defaultConfig } from '@chakra-ui/react';
import { badgeRecipe } from './recipes/badge';

export const config = createSystem(defaultConfig, {
  theme: {
    tokens,
    semanticTokens,
    recipes: {
      badge: badgeRecipe,
    },
  },
});
```

### Bad example

```typescript
// ❌ Bad: Missing defaultVariants
export const badgeRecipe = defineRecipe({
  base: { ... },
  variants: { ... },
  // Missing defaultVariants
});

// ❌ Bad: Hardcoded colors
solid: {
  bg: '#3B82F6', // Should use colorPalette.500 or token reference
  color: '#ffffff',
},

// ❌ Bad: Using slot recipes for single-element components
export const badgeRecipe = defineRecipe({
  slots: ['root', 'label'], // Use slots only for multi-part components
});
```

## Anti-patterns

- Use slot recipes for single-element components
- Omit `defaultVariants` (always define defaults)
- Hardcode colors (use `colorPalette` or token references)
- Not supporting dark mode with `_dark` condition
- Not registering recipes in theme config

## Notes

### Recipe Location

```
libs/ui-themes/src/themes/[theme-name]/recipes/[component].ts
```

Example: `libs/ui-themes/src/themes/chakra-default/recipes/badge.ts`

### Recipe Structure

- `base`: Base styles applied to all variants
- `variants`: Object defining variant options (variant, size, etc.)
- `defaultVariants`: Required defaults for each variant type

### Dark Mode Pattern

Use `_dark` condition within variant definitions:

- Apply different styles for dark mode
- Maintain contrast and readability
- Reference semantic tokens when possible

### Registering Recipes

Add recipes to theme config under `recipes` key. Recipes are then available to components using the recipe name.
