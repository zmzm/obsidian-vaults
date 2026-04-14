---
type: case-study
status: active
updated: 2026-04-14
tags:
  - react
  - typescript
  - migration
  - code-quality
---

# Safer Frontend without React.FC

This case study captures a team-wide migration away from `React.FC` in order to improve type safety and surface hidden bugs.

## Context

- The team found that `React.FC` was masking useful TypeScript feedback instead of improving clarity.
- The problem was broad enough that fixing it manually would not scale across the codebase.

## What Changed

- Components moved toward explicit prop typing and explicit return typing.
- The migration was automated rather than left to gradual opportunistic cleanup.
- Linting and policy were used to stop regressions after the change.

## Why It Matters

- This is a good example of a code-quality migration where tooling, enforcement, and cleanup all mattered.
- It preserves a practical frontend-safety lesson that does not need its own core concept page.

## Main Lesson

- A safer frontend often comes from removing misleading convenience abstractions and then enforcing the better default at scale.

## Related Pages

- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../tools/React Router|React Router]]

## Raw Source

- [[../../raw/twir/269/articles/08 - The Journey to a Safer Frontend Why Gusto Removed React.FC|TWIR item note]]
- [[../../raw/twir/269/2026-02-18-TWIR-269|TWIR #269]]
