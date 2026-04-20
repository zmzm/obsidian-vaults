---
id: frontend/chakra-ui/chakra-theme-tokens
name: frontend/chakra-ui/chakra-theme-tokens
kind: reference
domain: frontend
topics: [chakra-ui, chakra theme tokens]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra Theme Tokens

## When to use

Use this document when:

- Defining design tokens (colors, fonts, spacing)
- Creating semantic tokens for light/dark modes
- Understanding token structure and organization
- Setting up token references in semantic tokens

## Rules

- Use `defineTokens()` for base design tokens
- Use `defineSemanticTokens()` for context-aware tokens
- Each token requires a `value` key
- Reference base tokens in semantic tokens using `{colors.name.shade}` syntax
- Use `DEFAULT` for base nested semantic tokens
- Never define token values directly without `value` key

## Examples

### Good example

```typescript
import { defineTokens } from '@chakra-ui/react';

export const tokens = defineTokens({
  colors: {
    primary: {
      50: { value: '#f0f9ff' },
      500: { value: '#0ea5e9' },
      900: { value: '#0c4a6e' },
    },
  },
  fonts: {
    heading: { value: 'Neusa, Roboto, sans-serif' },
    body: { value: 'Roboto, sans-serif' },
  },
  fontSizes: {
    xs: { value: '0.75rem' },
    md: { value: '1rem' },
  },
});

// Semantic tokens
import { defineSemanticTokens } from '@chakra-ui/react';

export const semanticTokens = defineSemanticTokens({
  colors: {
    bg: {
      DEFAULT: {
        value: { _light: '{colors.white}', _dark: '{colors.secondary.900}' },
      },
      subtle: {
        value: { _light: '{colors.secondary.50}', _dark: '{colors.secondary.800}' },
      },
    },
    fg: {
      DEFAULT: {
        value: { _light: '{colors.secondary.900}', _dark: '{colors.white}' },
      },
    },
  },
});
```

### Bad example

```typescript
// ❌ Bad: Token values without value key
export const tokens = defineTokens({
  colors: {
    primary: {
      500: '#0ea5e9', // Should be { value: '#0ea5e9' }
    },
  },
});

// ❌ Bad: Inline values in semantic tokens
semanticTokens: {
  colors: {
    bg: {
      value: '#ffffff', // Should reference {colors.white}
    }
  }
}

// ❌ Bad: Mixing token types
export const tokens = defineTokens({
  colors: {
    primary: { value: '#0ea5e9' },
    fontSize: { value: '1rem' }, // Should be in fontSizes category
  },
});
```

## Anti-patterns

- Define token values directly without `value` key
- Mix token types in wrong categories
- Use inline values in semantic tokens (always reference)
- Not using `DEFAULT` for base semantic tokens
- Hardcoding colors instead of referencing tokens

## Notes

### Location Pattern

```
libs/ui-themes/src/themes/[theme-name]/
├── config.ts              # System config
├── tokens.ts              # Design tokens
├── semantic-tokens.ts     # Semantic tokens
└── recipes/               # Component recipes
```

### Token Structure

- Base tokens: Use `defineTokens()` with nested objects
- Each token requires a `value` key
- Semantic tokens: Use `defineSemanticTokens()` for context-aware tokens
- Reference base tokens using `{colors.name.shade}` syntax
- Use `DEFAULT` for base nested semantic tokens

### Semantic Token Pattern

Semantic tokens adapt based on theme mode (light/dark):

- Use `_light` and `_dark` conditions
- Always reference base tokens, never hardcode values
- Use `DEFAULT` key for base semantic token values
