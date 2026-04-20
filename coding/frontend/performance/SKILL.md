---
name: fe-performance
description: React performance optimization. Use for memoization, code splitting, bundle size.
triggers:

  keywords: ['React.memo', 'useMemo', 'useCallback', 'lazy(', 'Suspense', 'virtualize', 'bundle']
---

# Frontend Performance Skill

## When to use this knowledge

Use this skill when you are:

- Optimizing bundle size and reducing initial load time
- Reducing unnecessary re-renders in components
- Implementing code splitting and lazy loading routes
- Virtualizing long lists for better performance
- Memoizing expensive computations or callbacks
- Improving Core Web Vitals (LCP, FID, CLS)
- Profiling and measuring performance improvements

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Component memoization with React.memo
- Hook memoization with useMemo and useCallback
- Image optimization strategies
- Debouncing and throttling patterns
- Bundle size optimization
- Re-render optimization techniques

## Knowledge map

Always start here, then follow references as needed:

- Memoization (React.memo, useMemo, useCallback) → `references/memoization.md`
- Image Optimization → `references/image-optimization.md`
- Debouncing → `references/debouncing.md`
- Bundle Optimization → `references/bundle-optimization.md`
- Re-render Optimization → `references/re-render-optimization.md`

## Fast decision hints

- If the task is mainly about Optimizing bundle size and reducing initial load time, start with this skill.
- If the task also involves Reducing unnecessary re-renders in components, follow the most relevant reference page.
- If the work drifts into Implementing code splitting and lazy loading routes, check the nearest neighboring skill boundary.

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
