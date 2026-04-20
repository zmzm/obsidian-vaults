---
name: chakra-ui
description: Chakra UI v3 theme system and component wrappers. Use when working in libs/ui-components/.
triggers:

  paths: ['libs/ui-components/**']
  keywords: ['createSystem', 'defineConfig', 'defineRecipe', 'semantic.token', '@chakra-ui/react']
---

# Chakra UI v3 Development Guide

## When to use this knowledge

Use this skill when you are:

- Creating or wrapping Chakra UI components in @mentory/ui-components library
- Setting up theme systems with tokens, semantic tokens, and recipes
- Implementing component patterns following atomic design
- Migrating from Chakra UI v2 to v3
- Creating or modifying theme configurations
- Working with color palettes and design tokens
- Implementing dark mode support

## When not to use this knowledge

- Working in `libs/ui-components/` → use this skill
- Working in `apps/*/` → use `fe-ui` skill

## What this skill covers

This skill provides guidance for:

- Component wrapper structure and atomic design file organization
- Theme system setup with createSystem() and defineConfig()
- Design tokens and semantic tokens for light/dark modes
- Component styling with recipes and variants
- v3 API changes and migration from v2
- Project rules and best practices

## Knowledge map

Always start here, then follow references as needed:

- v3 Migration → `references/v3-migration.md`
- Component Patterns → `references/chakra-v3-component-patterns.md`
- Theme Config → `references/chakra-theme-config.md`
- Theme Setup → `references/chakra-theme-setup.md`
- Theme Tokens → `references/chakra-theme-tokens.md`
- Theme Recipes → `references/chakra-theme-recipes.md`
- Recipes Provider → `references/chakra-theme-recipes-provider.md`

## Fast decision hints

- If the task is mainly about Creating or wrapping Chakra UI components in @mentory/ui-components library, start with this skill.
- If the task also involves Setting up theme systems with tokens, semantic tokens, and recipes, follow the most relevant reference page.
- If the work drifts into Implementing component patterns following atomic design, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**.

This skill is for **library authors** working on the @mentory/ui-components package.

| Task                              | Use This Skill | Use `fe-ui` Skill |
| --------------------------------- | -------------- | ----------------- |
| Creating new component wrappers   | ✅             |                   |
| Setting up theme tokens/recipes   | ✅             |                   |
| Migrating Chakra v2 → v3          | ✅             |                   |
| Configuring dark mode             | ✅             |                   |
| **Using** Button, Card, Alert     |                | ✅                |
| Building forms with UI components |                | ✅                |
| Responsive design with props      |                | ✅                |
| Component styling in app code     |                | ✅                |

**Rule of thumb**:

- Working in `libs/ui-components/` → use this skill
- Working in `apps/*/` → use `fe-ui` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
