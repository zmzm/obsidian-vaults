---
name: fe-error-handling
description: Error boundaries, toast notifications, API error handling. Use for user feedback on errors.
triggers:

  paths: ['**/ErrorBoundary/**', '**/error*.ts']
  keywords: ['ErrorBoundary', 'useErrorBoundary', 'captureError', 'toast', 'variant.*destructive', 'onError', 'catch']
---

# Frontend Error Handling Skill

## When to use this knowledge

Use this skill when you are:

- Setting up error boundaries
- Showing error feedback to users (toasts)
- Handling API errors in mutations
- Handling async operation failures
- Implementing try/catch patterns

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- ErrorBoundary component usage
- useErrorBoundary hook
- Toast notifications for errors
- API error handling patterns
- Try/catch patterns in async code

## Knowledge map

Always start here, then follow references as needed:

- Error Boundaries → `references/error-boundaries.md`
- Toast Notifications → `references/toast-notifications.md`
- API Errors → `references/api-errors.md`

## Fast decision hints

- If the task is mainly about Setting up error boundaries, start with this skill.
- If the task also involves Showing error feedback to users (toasts), follow the most relevant reference page.
- If the work drifts into Handling API errors in mutations, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **frontend error surfacing and recovery patterns**. For:

- **React Query request orchestration** → see `react-query`
- **form-level validation rendering** → see `ui`
- **route protection and redirect behavior** → see `routing`

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
