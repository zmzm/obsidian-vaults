---
id: frontend/chakra-ui/chakra-theme-setup
name: frontend/chakra-ui/chakra-theme-setup
kind: reference
domain: frontend
topics: [chakra-ui, chakra theme setup]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra UI Theme Setup

## When to use

Use this document when:

- Setting up a new Chakra UI v3 theme
- Creating theme with createSystem and defineConfig
- Defining semantic tokens for light/dark modes
- Understanding v3 theme API changes

## Rules

- Use `createSystem + defineConfig` (not `extendTheme`)
- Always define semantic tokens for light/dark modes
- Use `_light` and `_dark` conditions in semantic tokens
- Reference base tokens in semantic tokens using `{colors.name.shade}` syntax
- Export system configuration for use in ChakraProvider

## Examples

### Good example

```typescript
import { createSystem, defaultConfig, defineConfig } from '@chakra-ui/react';

const config = defineConfig({
  theme: {
    tokens: { /* colors, fonts, spacing */ },
    semanticTokens: { /* light/dark responsive tokens */ },
    recipes: { /* component variants */ }
  }
});

export const system = createSystem(defaultConfig, config);

// Semantic tokens (light/dark responsive)
semanticTokens: {
  colors: {
    'colorPalette.solid': {
      value: {
        _light: '{colors.colorPalette.500}',
        _dark: '{colors.colorPalette.200}'
      }
    }
  }
}
```

### Bad example

```typescript
// ❌ Bad: Using v2 API (extendTheme)
export const theme = extendTheme({
  colors: { ... },
});

// ❌ Bad: Missing semantic tokens
const config = defineConfig({
  theme: {
    tokens: { ... },
    // Missing semanticTokens
  }
});

// ❌ Bad: Hardcoding values in semantic tokens
semanticTokens: {
  colors: {
    bg: {
      value: '#ffffff', // Should reference tokens
    }
  }
}
```

## Anti-patterns

- Using v2 API (`extendTheme` instead of `createSystem + defineConfig`)
- Missing semantic tokens for light/dark modes
- Hardcoding values in semantic tokens instead of referencing base tokens
- Not using `_light` and `_dark` conditions properly

## Notes

### Theme Creation (v3 API)

**Use `createSystem + defineConfig`** (not `extendTheme`):

- `defineConfig` defines your theme configuration
- `createSystem` combines it with `defaultConfig`
- Always include tokens, semanticTokens, and recipes

### Semantic Tokens Pattern

Semantic tokens use `_light` and `_dark` conditions for responsive theming:

- Reference base tokens using `{colors.name.shade}` syntax
- Use `value` key with object containing `_light` and `_dark` properties
- Semantic tokens adapt automatically based on theme mode
