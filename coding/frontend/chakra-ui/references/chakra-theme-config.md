---
id: frontend/chakra-ui/chakra-theme-config
name: frontend/chakra-ui/chakra-theme-config
kind: reference
domain: frontend
topics: [chakra-ui, chakra theme config]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Chakra Theme Config

## When to use

Use this document when:

- Creating theme system configurations
- Organizing theme files and structure
- Setting up theme with createSystem and defineConfig
- Registering component recipes in theme

## Rules

- Use `createSystem()` to combine `defaultConfig` with custom theme
- Export config with descriptive name (e.g., `chakraDefaultConfig`)
- Use kebab-case for directory names
- Import recipes as named exports matching component name
- Never modify `defaultConfig` directly
- Always include semantic tokens in theme config

## Examples

### Good example

```typescript
import { createSystem, defaultConfig } from '@chakra-ui/react';
import { badgeRecipe } from './recipes/badge';
import { avatarRecipe } from './recipes/avatar';
import { semanticTokens } from './semantic-tokens';
import { tokens } from './tokens';

export const chakraDefaultConfig = createSystem(defaultConfig, {
  theme: {
    tokens,
    semanticTokens,
    recipes: {
      badge: badgeRecipe,
      avatar: avatarRecipe,
    },
  },
});
```

### Bad example

```typescript
// ❌ Bad: Modifying defaultConfig directly
const config = defaultConfig;
config.theme.colors.primary = '#000'; // Don't do this

// ❌ Bad: Missing semantic tokens
export const config = createSystem(defaultConfig, {
  theme: {
    tokens,
    // Missing semanticTokens
  },
});

// ❌ Bad: Inconsistent naming
export const myTheme = createSystem(...); // Should be descriptive like chakraDefaultConfig
```

## Anti-patterns

- Modify `defaultConfig` directly
- Mix theme organization patterns
- Create theme configs without semantic tokens
- Forget to export the config with descriptive name
- Use inconsistent naming conventions

## Notes

### File Structure

```
libs/ui-themes/src/themes/[theme-name]/
├── config.ts              # Main theme system (exports chakraDefaultConfig)
├── tokens.ts              # Design tokens
├── semantic-tokens.ts     # Semantic tokens
└── recipes/
    ├── badge.ts
    ├── avatar.ts
    └── icon-button.ts
```

### Naming Convention

- Config export: `[themeName]Config` (e.g., `chakraDefaultConfig`)
- Directory: `kebab-case` (e.g., `chakra-default/`)
- Recipe imports: Named exports matching component name

### Config Pattern

Always use `createSystem()` to combine `defaultConfig` with your custom theme. This ensures you're extending the default configuration
rather than replacing it.
