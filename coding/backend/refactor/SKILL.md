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

- Behavior-preserving refactorings within approved scope
- Contract or scope changes that may require additional authorization
- Anti-patterns to fix
- Refactoring checklist

## Knowledge map

- Shared extraction decisions → [readability and boundaries](../../common/engineering/references/readability-and-boundaries.md).
- Shared behavior-preservation, evidence, and authorization principles → [verification and change safety](../../common/engineering/references/verification-and-change-safety.md).

Always start here, then follow references as needed:

- Safe refactorings → `references/safe-refactorings.md`
- Scope and permission → `references/permission-required.md`
- Anti-patterns → `references/anti-patterns.md`

## Fast decision hints

- If the task is mainly about Extracting utility functions and constants, start with this skill.
- If the task also involves Improving type safety and removing any types, follow the most relevant reference page.
- If the work drifts into Simplifying complex logic and conditionals, check the nearest neighboring skill boundary.

## Local rules

- `<default>` Default: Preserve existing behavior (all tests must pass)
- `<default>` Default: Run tests before and after refactoring
- `<heuristic>` Heuristic: Commit frequently with descriptive messages
- `<default>` Default: Follow project coverage requirements; coverage percentages are project-specific, not exceptions or universal quality targets.

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **its own domain scope**. For adjacent concerns, move to the neighboring skill with the clearest ownership.

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into `references/`.
- Prefer canonical references over duplicated guidance.
