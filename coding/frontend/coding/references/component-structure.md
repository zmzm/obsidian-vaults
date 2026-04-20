---
id: frontend/coding/component-structure
name: frontend/coding/component-structure
kind: reference
domain: frontend
topics: [coding, component structure]
priority: high
status: stable
canonical: true
updated: 2026-04-16
---

# Component Structure

## When to use

Use this document when:

- creating a new component folder
- deciding whether a concern belongs in the component file, a hook, or a subcomponent
- restructuring an oversized component tree

## Decision Table

| If... | Prefer... | Why |
| ----- | ---------- | --- |
| the component is simple and mostly presentational | keep a small local structure | avoid unnecessary file sprawl |
| the component has meaningful stateful logic | extract a `ComponentName.hook.ts` file | isolate stateful logic from rendering |
| a child section has its own props, tests, or behavior | promote it to a subcomponent folder | keep boundaries explicit |
| a helper hook is reusable beyond one component | move it to `shared/hooks/` or a clearer shared location | avoid component-local coupling |

## Rules

### Mandatory

- component files use PascalCase and match the folder name
- hook files use `.hook.ts`, not `.hook.tsx`

### Default

- start with the smallest folder structure that keeps boundaries clear
- extract a component hook only when the component has enough logic to justify it
- promote repeated or behaviorally distinct UI sections into subcomponents

### Heuristics

- avoid creating type, constant, or style files until the component actually needs them
- avoid deep component nesting when composition can be flattened

### Exceptions

- preserve an existing local convention when consistency with nearby files matters more than ideal structure

## Anti-patterns

- creating a full multi-file folder for trivial presentational components
- using `.hook.tsx` for logic-only hooks
- mixing unrelated UI sections into one large component file when they already have independent behavior

## Notes

- This page replaces the generic “everything gets the same file tree” model with a lighter default.
- Pair with `test-placement.md` for test layout decisions.
