---
name: fe-react-query
description: Server state with React Query. Use for API calls, mutations, caching.
triggers:

  paths: ['**/*.hook.ts', '**/*.hook.tsx']
  keywords: ['useQuery', 'useMutation', 'useInfiniteQuery', 'queryClient', '@tanstack/react-query', 'queryKey']
---

# React Query Skill

## When to use this knowledge

Use this skill when you are:

- Fetching data from APIs and managing server state
- Implementing mutations (POST, PATCH, DELETE operations)
- Handling cache invalidation after mutations
- Implementing pagination or infinite scrolling
- Working with dependent queries and query options
- Extracting React Query logic into custom hooks

## When not to use this knowledge

- "How does React Query work?" → use this skill
- "How do I structure my hook?" → use `fe-hook` skill

## What this skill covers

This skill provides guidance for:

- Query key conventions and best practices
- Mutation patterns and cache invalidation
- Advanced patterns (pagination, infinite queries, optimistic updates)
- Query options and configuration
- Custom hooks for React Query logic

## Knowledge map

Always start here, then follow references as needed:

- Mutations → `references/mutations.md`
- Cache Invalidation → `references/cache-invalidation.md`
- Advanced Patterns → `references/advanced-patterns.md`
- Query Options → `references/query-options.md`
- Custom Hooks → `references/custom-hooks.md`

## Fast decision hints

- If the task is mainly about Fetching data from APIs and managing server state, start with this skill.
- If the task also involves Implementing mutations (POST, PATCH, DELETE operations), follow the most relevant reference page.
- If the work drifts into Handling cache invalidation after mutations, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Prefer documented patterns over ad-hoc solutions
- `<default>` Default: Avoid listed anti-patterns unless explicitly justified
- `<heuristic>` Heuristic: If multiple references apply, compare them explicitly
- `<exception>` Exception: If deviating from the guidelines, clearly explain why and what is being violated

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**.

This skill focuses on **React Query library usage** (queries, mutations, cache).

| Task                                  | Use This Skill | Use `fe-hook` Skill |
| ------------------------------------- | -------------- | ------------------- |
| useQuery options (staleTime, enabled) | ✅             |                     |
| Query key conventions                 | ✅             |                     |
| Cache invalidation strategies         | ✅             |                     |
| Optimistic updates                    | ✅             |                     |
| Pagination/infinite queries           | ✅             |                     |
| Hook return interface design          |                | ✅                  |
| Hook naming conventions               |                | ✅                  |
| Hook composition patterns             |                | ✅                  |
| Adding toast/i18n to hooks            |                | ✅                  |
| Non-React-Query hooks                 |                | ✅                  |

**Rule of thumb**:

- "How does React Query work?" → use this skill
- "How do I structure my hook?" → use `fe-hook` skill

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
