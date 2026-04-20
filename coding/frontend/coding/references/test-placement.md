---
id: frontend/coding/test-placement
name: frontend/coding/test-placement
kind: reference
domain: frontend
topics: [coding, tests, file structure]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Test Placement

## When to use

Use this document when:

- deciding whether a component or hook needs its own test file
- placing tests for subcomponents
- cleaning up noisy folder structures driven only by test location

## Rules

### Mandatory

- keep tests near the code they primarily validate

### Default

- add a dedicated test file when the component or hook has meaningful behavior worth protecting
- give subcomponents their own tests only when they have independent logic, interaction, or rendering risk
- avoid blanket “every file must have a test file” rules when the behavior is already covered at a higher level

### Heuristics

- prefer integration-style coverage at the parent level when child behavior is mostly compositional
- prefer isolated tests when a child component has branching, form logic, accessibility behavior, or stateful interaction

### Exceptions

- if project policy or critical risk requires a direct test for a file, follow that local rule even when higher-level coverage exists

## Anti-patterns

- forcing a spec file for trivial leaf components with no independent behavior
- duplicating the same assertions in parent and child test files
- scattering tests far from the code they protect
