---
type: source
status: active
updated: 2026-04-22
tags:
  - tanstack-query
  - eslint
  - source
---

# TanStack Query prefer-query-options

This source captures an important convention-level change in the TanStack Query ecosystem: pushing teams toward colocated query configuration through `queryOptions()` and `infiniteQueryOptions()`.

## Summary

- The `prefer-query-options` ESLint rule discourages manual `queryKey` definitions that drift away from the corresponding query function.
- The rule is included in a stricter recommended ESLint preset.
- The change is backed by docs, examples, and tests, which suggests it is intended as a durable convention rather than a one-off experiment.

## Why This Source Matters

- It signals a maturation of query authoring patterns, not just a new lint check.
- It is useful for understanding how TanStack Query wants teams to structure reusable query definitions.
- It supports the broader vault theme that framework and library ergonomics increasingly depend on conventions enforced by tooling.

## Caveats

- The note summarizes the motivation well, but it does not yet capture migration tradeoffs or edge cases.

## Related Pages

- [[../tools/TanStack Query|TanStack Query]]
- [[../topics/React Rendering|React Rendering]]
- [[Creating Query Abstractions]]
- [[Custom ESLint Rules]]

## Raw Sources

- [[../../raw/twir/275/articles/05 - TanStack Query ESLint PR - Add prefer-query-options rule|TWIR item note]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
