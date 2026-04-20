---
name: fe-testing
description: Testing with RTL, MSW, Jest. Use renderComponent and setupMswServer from @mentory/test-utils.
triggers:

  paths: ['**/*.spec.tsx', '**/*.spec.ts', '**/tests/**']
  keywords: ['renderComponent', 'setupMswServer', '@testing-library', 'screen.get', 'userEvent', 'waitFor']
---

# Frontend Testing Skill

## When to use this knowledge

Use this skill when you are:

- Writing or fixing tests for React components
- Creating integration tests for features
- Testing form validation and submissions
- Testing user interactions (clicks, keyboard navigation)
- Mocking API calls with MSW
- Testing loading, success, and error states
- Ensuring test coverage requirements

## When not to use this knowledge

- Writing production feature code (use feature-specific frontend skills)
- Changing shared design-system component implementation details (use `chakra-ui` / `fe-coding` as needed)

## What this skill covers

This skill provides guidance for:

- Core principles and critical rules
- Test structure and best practices
- MSW setup and API mocking
- User interaction testing patterns
- Loading and error state testing
- Mutation testing (POST/PATCH/DELETE)
- Accessibility testing
- Query selector priorities
- Test utilities and coverage requirements

## Knowledge map

Always start here, then follow references as needed:

- Core Principles → `references/core-principles.md`
- MSW Setup → `references/msw-setup.md`
- User Interactions → `references/user-interactions.md`
- Loading & Error States → `references/loading-error-states.md`
- Mutations → `references/mutations.md`
- Query Selectors → `references/query-selectors.md`

**Cross-skill references:**

- Accessibility Testing → See `fe-accessibility` skill (`references/testing.md`)
- Test Utils → `references/test-utils.md`

## Fast decision hints

- File path matches `*.spec.ts[x]` or `**/tests/**`: start with this skill
- You need mock API behavior or async UI assertions: use `setupMswServer` + `renderComponent`
- If test strategy depends on ARIA semantics, cross-check `fe-accessibility` references

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**. For adjacent concerns, move to the neighboring skill with the clearest ownership.

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
