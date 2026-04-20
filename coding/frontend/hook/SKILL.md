---
name: fe-hook
description: Custom hook design patterns. Use for hook structure, naming, return interfaces.
triggers:

  paths: ['**/*.hook.ts', '**/*.hook.tsx']
  keywords: ['export const use', 'return {', 'export function use']
  excludes: ['**/*.spec.*']
---

# Frontend Hook Skill

## When to use this knowledge

Use this skill when you are:

- Extracting reusable logic from components into custom hooks
- Creating data fetching hooks with React Query
- Building form state management hooks
- Implementing shared stateful logic across components
- Composing multiple hooks for complex functionality
- Creating utility hooks for common patterns

## When not to use this knowledge

- "How do I structure my hook?" → use this skill
- "How does React Query work?" → use `fe-react-query` skill

## What this skill covers

This skill provides guidance for:

- Hook naming conventions and file structure
- Return value patterns (objects vs arrays)
- Data fetching hooks with React Query
- Mutation hooks for POST/PATCH/DELETE operations
- Form state management patterns
- Utility hooks (localStorage, debounce, pagination)
- Hook composition patterns

## Knowledge map

Always start here, then follow references as needed:

- Core Principles → `references/core-principles.md`
- Data Fetching → `references/data-fetching.md`
- React Query Custom Hooks → `../react-query/references/custom-hooks.md`
- Form State → `references/form-state.md`
- Utility Hooks → `references/utility-hooks.md`
- Composition → `references/composition.md`

## Fast decision hints

- If the task is mainly about Extracting reusable logic from components into custom hooks, start with this skill.
- If the task also involves Creating data fetching hooks with React Query, follow the most relevant reference page.
- If the work drifts into Building form state management hooks, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**.

This skill focuses on **hook design patterns** (return interfaces, naming, composition).

| Task                               | Use This Skill | Use `fe-react-query` Skill |
| ---------------------------------- | -------------- | -------------------------- |
| Hook return interface design       | ✅             |                            |
| Hook naming conventions            | ✅             |                            |
| Hook composition patterns          | ✅             |                            |
| Adding toast/i18n to hooks         | ✅             |                            |
| Utility hooks (localStorage, etc.) | ✅             |                            |
| Query key conventions              |                | ✅                         |
| Cache invalidation strategies      |                | ✅                         |
| Optimistic updates                 |                | ✅                         |
| Pagination/infinite queries        |                | ✅                         |

**Rule of thumb**:

- "How do I structure my hook?" → use this skill
- "How does React Query work?" → use `fe-react-query` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
