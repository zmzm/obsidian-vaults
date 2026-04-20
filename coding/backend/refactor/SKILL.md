---
name: be-refactor
description:

  Guide for safe refactoring patterns for NestJS code that preserve existing behavior while improving code quality. Use when refactoring
  backend code including extracting utilities, improving type safety, simplifying logic, or splitting large files.
---

# Backend Refactor Skill

## When to use this knowledge

Use this skill when you are:

- Extracting utility functions and constants
- Improving type safety and removing any types
- Simplifying complex logic and conditionals
- Splitting large files into smaller modules
- Identifying and fixing anti-patterns

## When not to use this knowledge

- Tasks owned more directly by a neighboring skill
- Pure exploration or lookup work without implementation decisions

## What this skill covers

This skill provides guidance for:

- Safe refactorings that don't require permission
- Refactorings that require explicit permission
- Anti-patterns to fix
- Refactoring checklist

## Knowledge map

Always start here, then follow references as needed:

- Safe refactorings → `references/safe-refactorings.md`
- Permission required → `references/permission-required.md`
- Anti-patterns → `references/anti-patterns.md`

## Fast decision hints

- If the task is mainly about Extracting utility functions and constants, start with this skill.
- If the task also involves Improving type safety and removing any types, follow the most relevant reference page.
- If the work drifts into Simplifying complex logic and conditionals, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Preserve existing behavior (all tests must pass)
- `<default>` Default: Run tests before and after refactoring
- `<heuristic>` Heuristic: Commit frequently with descriptive messages
- `<exception>` Exception: Keep code coverage ≥80%

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**. For adjacent concerns, move to the neighboring skill with the clearest ownership.

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
