---
name: fe-auth
description: Authentication with Clerk. Use for useAuth hook, login/logout, protected content.
triggers:

  paths: ['**/auth/**', '**/ClerkProvider/**']
  keywords: ['useAuth', '@clerk/clerk-react', 'SignIn', 'SignUp', 'signOut', 'isSignedIn', 'getToken']
---

# Frontend Auth Skill

## When to use this knowledge

Use this skill when you are:

- Working with the useAuth hook
- Implementing login/logout functionality
- Accessing user information (userId, email, name)
- Getting authentication tokens for API calls
- Setting up Clerk provider
- Customizing Clerk components (SignIn, SignUp)

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- useAuth hook usage and return values
- Clerk component customization
- Token management for API calls
- User data access patterns
- Provider setup and configuration

## Knowledge map

Always start here, then follow references as needed:

- useAuth Hook → `references/use-auth.md`
- Clerk Components → `references/clerk-components.md`

## Fast decision hints

- If the task is mainly about Working with the useAuth hook, start with this skill.
- If the task also involves Implementing login/logout functionality, follow the most relevant reference page.
- If the work drifts into Accessing user information (userId, email, name), check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **authentication logic**. For route protection:

| Task                    | Use This Skill | Use `routing` Skill |
| ----------------------- | -------------- | ------------------- |
| useAuth hook usage      | ✅             |                     |
| User data (email, name) | ✅             |                     |
| signOut function        | ✅             |                     |
| getToken for API        | ✅             |                     |
| Protected route guards  |                | ✅                  |
| Navigate redirects      |                | ✅                  |
| Route configuration     |                | ✅                  |

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
