---
type: source
status: active
updated: 2026-04-14
tags:
  - tanstack-query
  - abstractions
  - source
---

# Creating Query Abstractions

This source captures a useful design tension in TanStack Query: abstraction helps consistency, but too much abstraction weakens flexibility and type inference.

## Summary

- Custom abstractions over query hooks can reduce duplication and centralize patterns.
- Over-abstraction can hide useful options and make advanced usage harder.
- Minimal abstractions often preserve both TypeScript inference and API clarity better than thick wrappers.

## Why This Source Matters

- It gives the `TanStack Query` page a concrete design-pattern discussion rather than only lint and convention signals.
- It helps frame query abstraction as a tradeoff space rather than an obviously good refactor direction.

## Caveats

- The guidance is principle-heavy and context-sensitive rather than universally prescriptive.

## Related Pages

- [[../tools/TanStack Query|TanStack Query]]
- [[../sources/TWIR 270|TWIR 270]]

## Raw Sources

- [[../../raw/twir/270/articles/06 - TkDodo - Creating Query Abstractions|TWIR item note]]
- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
