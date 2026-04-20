---
name: fe-ui
description: UI components from @mentory/ui-components. Use for styling, forms, layouts in app code.
triggers:

  paths: ['apps/*/src/**/*.tsx', 'apps/*/src/**/*.ts']
  keywords: ['@mentory/ui-components', 'Button', 'Card', 'Alert', 'Box', 'Flex', 'Stack', 'Input', 'FormControl']
  excludes: ['libs/ui-components/**']
---

# Frontend UI Skill

## When to use this knowledge

Use this skill when you are:

- Working with UI components from @mentory/ui-components library
- Using specific component APIs (Button, Card, Alert, etc.)
- Building user interfaces and layouts with UI components
- Creating forms with validation using UI components
- Displaying alerts, toasts, or dialogs
- Implementing responsive design patterns with Chakra props
- Styling components using design system props
- Setting up providers and component wrappers

## When not to use this knowledge

- Working in `libs/ui-components/**` on design-system internals (use `chakra-ui`)
- Working on generic React architecture concerns without UI-library specifics (use `fe-coding`)

## What this skill covers

This skill provides guidance for:

- Core principles and import rules for @mentory/ui-components
- Available components and their specific APIs
- Component usage examples and patterns
- Form patterns using UI components
- Responsive design strategies with Chakra props
- UI-specific patterns (loading, empty, error states with components)
- Styling guidelines using design system props
- Provider setup and configuration

## Knowledge map

Always start here, then follow references as needed:

- Core Principles → `references/core-principles.md`
- Components → `references/components.md`
- Display Components → `references/display-components.md`
- Forms → `references/forms.md`
- Responsive Design → `references/responsive.md`
- Patterns → `references/patterns.md`
- Styling → `references/styling.md`
- Anti-Patterns → `references/anti-patterns.md`

## Fast decision hints

- File path starts with `apps/frontend/src/**` and uses visual components: use this skill
- You are choosing props/variants for `Button`, `Card`, `Alert`, `Dialog`, `Select`: use this skill
- You are editing theme tokens/recipes/provider internals: switch to `chakra-ui`

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**.

This skill is for **application developers** using the @mentory/ui-components library.

| Task                              | Use This Skill | Use Other Skill |
| --------------------------------- | -------------- | --------------- |
| Using Button, Card, Alert         | ✅             |                 |
| Building forms with UI components | ✅             |                 |
| Responsive design with props      | ✅             |                 |
| Component styling in app code     | ✅             |                 |
| Creating component wrappers       |                | `chakra-ui`     |
| Theme tokens/recipes              |                | `chakra-ui`     |
| General React patterns            |                | `fe-coding`     |
| File structure, props/types       |                | `fe-coding`     |

**Rule of thumb**:

- Working in `apps/*/` with UI components → use this skill
- Working in `libs/ui-components/` → use `chakra-ui` skill
- General React patterns → use `fe-coding` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
