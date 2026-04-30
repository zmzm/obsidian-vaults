---
type: source
status: active
updated: 2026-04-21
tags:
  - eslint
  - linting
  - react
  - source
---

# Custom ESLint Rules

This source argues that custom ESLint rules are one of the most effective ways to turn recurring review advice into enforceable frontend policy.

## Summary

- ESLint rules operate on ASTs, which makes them precise enough to encode project-specific code-quality constraints.
- The article uses `useEffect` misuse as the motivating example: if the same review conversation repeats, a rule can usually eliminate it.
- The source also doubles as a compact explanation of how AST-based JavaScript tooling works in practice.

## Why This Source Matters

- It strengthens the `Type-Driven Frontend Safety` branch by adding lint policy to the vault's safety model rather than relying only on TypeScript.
- It also helps the `Effects and Cleanup Discipline` page because effect misuse is exactly the kind of repeated mistake that lint rules can catch reliably.
- More broadly, it supports the vault's interest in explicit constraints over ad hoc review culture.

## Caveats

- The article is advocacy plus implementation guidance, not proof that every team should immediately write custom rules.
- Custom rules are most valuable when a pattern is both common and expensive enough to justify enforcement.

## Related Pages

- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[TWIR 277]]

## Raw Sources

- [[../../raw/twir/277/articles/10 - Now more than ever, you need to master custom ESLint rules|TWIR item note]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
