---
name: fe-coding
description: General React patterns, file structure, TypeScript. Use for architecture decisions.
triggers:

  paths: ['apps/frontend/**/*.tsx', 'apps/frontend/**/*.ts']
  keywords: ['useState', 'useEffect', 'useReducer', 'React.FC', 'interface.*Props']
---

# Frontend Coding Skill

## When to use this knowledge

Use this skill when you are:

- Writing or refactoring frontend code structure
- Making architectural or structural decisions
- Defining component APIs and props interfaces
- Managing local, client, or server state architecture
- Organizing files and modules
- Reviewing frontend code quality and consistency
- Understanding general React patterns and best practices

## When not to use this knowledge

- **UI component library usage** → See `ui` skill
- **Component styling and design system** → See `ui` skill
- **Specific component APIs** → See `ui` skill

## What this skill covers

This skill provides guidance for:

- General React coding patterns (conditional rendering, lists, event handlers)
- Common anti-patterns to avoid (library-agnostic)
- File and folder structure conventions
- Rules for props and TypeScript types
- State management approaches and trade-offs
- Code organization and architecture principles

## Knowledge map

Always start here, then follow references as needed:

- Anti-patterns → `references/anti-patterns.md`
- Patterns → `references/patterns.md`
- Component structure → `references/component-structure.md`
- Hook file conventions → `references/hook-file-conventions.md`
- Test placement → `references/test-placement.md`
- Props & types → `references/props-types.md`
- State management → `references/state-management.md`

## Fast decision hints

- If the task is mainly about Writing or refactoring frontend code structure, start with this skill.
- If the task also involves Making architectural or structural decisions, follow the most relevant reference page.
- If the work drifts into Defining component APIs and props interfaces, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple patterns apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **general React development practices** and is **library-agnostic**. For:

- **UI component library usage** → See `ui` skill
- **Component styling and design system** → See `ui` skill
- **Specific component APIs** → See `ui` skill
- **Chakra UI theme configuration** → See `chakra-ui` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
