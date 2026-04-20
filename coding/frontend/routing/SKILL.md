---
name: fe-routing
description: React Router patterns, route guards, navigation. Use for routes.tsx and navigation logic.
triggers:

  paths: ['**/routes.tsx', '**/routes.constant.ts']
  keywords: ['useNavigate', 'Navigate', 'Route ', 'Routes', 'useParams', 'useLocation', 'ROUTES.']
---

# Frontend Routing Skill

## When to use this knowledge

Use this skill when you are:

- Adding or modifying routes in routes.tsx
- Creating route constants
- Implementing protected routes (auth guards)
- Using navigation hooks (useNavigate, useParams, useLocation)
- Handling route parameters and query strings

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Route configuration and constants
- Protected vs public routes
- Route guards with authentication
- Navigation patterns
- Route parameters and dynamic routes
- Lazy loading routes

## Knowledge map

Always start here, then follow references as needed:

- Route Guards → `references/route-guards.md`
- Navigation → `references/navigation.md`

## Fast decision hints

- If the task is mainly about Adding or modifying routes in routes.tsx, start with this skill.
- If the task also involves Creating route constants, follow the most relevant reference page.
- If the work drifts into Implementing protected routes (auth guards), check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **routing mechanics**. For authentication logic:

| Task                    | Use This Skill | Use `auth` Skill |
| ----------------------- | -------------- | ---------------- |
| Route configuration     | ✅             |                  |
| Protected route wrapper | ✅             |                  |
| useNavigate, useParams  | ✅             |                  |
| useAuth hook details    |                | ✅               |
| Login/logout flow       |                | ✅               |
| Session management      |                | ✅               |

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
