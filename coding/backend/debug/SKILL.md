---
name: be-debug
description:

  Guide for debugging strategies and common issue resolution for NestJS applications. Use when troubleshooting backend issues including
  validation errors, Prisma query issues, authentication problems, async/await bugs, or environment configuration issues.
---

# Backend Debug Skill

## When to use this knowledge

Use this skill when you are:

- Debugging validation errors and DTO mismatches
- Resolving Prisma query issues and model name errors
- Fixing authentication/authorization problems
- Troubleshooting async/await issues
- Investigating environment variable problems

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Common NestJS issues and solutions
- Debugging tools and techniques
- Pre-deployment checklist

## Knowledge map

Always start here, then follow references as needed:

- Common issues → `references/common-issues.md`
- Debugging tools → `references/debugging-tools.md`

## Fast decision hints

- If the task is mainly about Debugging validation errors and DTO mismatches, start with this skill.
- If the task also involves Resolving Prisma query issues and model name errors, follow the most relevant reference page.
- If the work drifts into Fixing authentication/authorization problems, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Check DTO/schema alignment first (most common issue)
- `<default>` Default: Verify all async operations have `await`
- `<heuristic>` Heuristic: Inspect error logs and stack traces
- `<exception>` Exception: Test with correct Prisma model names (case-sensitive)

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**. For adjacent concerns, move to the neighboring skill with the clearest ownership.

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
