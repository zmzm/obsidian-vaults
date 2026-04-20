---
id: frontend/chakra-ui/v3-migration
name: frontend/chakra-ui/v3-migration
kind: reference
domain: frontend
topics: [chakra-ui, v3 migration]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra UI v3 Migration Guide

## When to use

Use this document when:

- Migrating from Chakra UI v2 to v3
- Understanding v3 API changes
- Setting up new Chakra UI v3 components
- Working with theme configuration in v3

## Rules

- Use `colorPalette` for color variants (not `colorScheme`)
- Use `createSystem()` and `defineConfig()` (not `extendTheme`)
- Define semantic tokens for light/dark modes
- Use `MentoryXProps` naming convention for component types
- Include `traceEventName` prop for analytics
- Always specify `defaultVariants` in recipes
- Follow atomic design structure
- Never use v2 API (`colorScheme`, `extendTheme`)
- Never modify `defaultConfig` directly
- Never hardcode colors in recipes (use `colorPalette` or token references)
- Never import directly from `@chakra-ui/*` in app code (use `@mentory/ui-components`)
- Never define token values without `value` key

## Examples

### Good example

```typescript
// ✅ Good: v3 API usage
<Badge colorPalette="primary" variant="solid">
  Label
</Badge>;

// ✅ Good: Theme setup with createSystem
import { createSystem, defaultConfig } from '@chakra-ui/react';
export const chakraDefaultConfig = createSystem(defaultConfig, {
  theme: {
    tokens,
    semanticTokens,
    recipes: {
      badge: badgeRecipe,
    },
  },
});

// ✅ Good: Semantic tokens
export const semanticTokens = defineSemanticTokens({
  colors: {
    bg: {
      value: {
        base: '{colors.gray.50}',
        _dark: '{colors.gray.900}',
      },
    },
  },
});
```

### Bad example

```typescript
// ❌ Bad: v2 API (colorScheme)
<Badge colorScheme="blue" variant="solid">Label</Badge>

// ❌ Bad: v2 API (extendTheme)
export const theme = extendTheme({
  colors: { ... },
});

// ❌ Bad: Hardcoded colors in recipes
const badgeRecipe = defineRecipe({
  base: {
    bg: '#3B82F6', // Should use colorPalette or token
  },
});
```

## Anti-patterns

- Using v2 API (`colorScheme`, `extendTheme`)
- Modifying `defaultConfig` directly
- Hardcoding colors in recipes
- Importing directly from `@chakra-ui/*` in app code
- Defining token values without `value` key
- Mixing v2 and v3 APIs

## Notes

### Key v3 Changes from v2

- `colorScheme` → `colorPalette`
- `extendTheme` → `createSystem() + defineConfig()`
- Monolithic components → Compositional patterns (e.g., `Avatar.Root`, `Avatar.Image`)
- Style props → Recipe-based styling

### Project File Structure

```
libs/ui-components/src/components/atoms/[Component]/
├── [Component].tsx         # Implementation
├── [Component].type.ts     # TypeScript interfaces
├── [Component].style.ts    # Styling hook
└── [Component].story.tsx   # Storybook stories

libs/ui-themes/src/themes/[theme-name]/
├── config.ts               # Main theme system
├── tokens.ts               # Design tokens
├── semantic-tokens.ts      # Semantic tokens
└── recipes/                # Component recipes
```
