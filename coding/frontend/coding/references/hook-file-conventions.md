---
id: frontend/coding/hook-file-conventions
name: frontend/coding/hook-file-conventions
kind: reference
domain: frontend
topics: [coding, hooks, file structure]
priority: medium
status: stable
canonical: true
updated: 2026-04-16
---

# Hook File Conventions

## When to use

Use this document when:

- naming and placing hook files
- deciding between component-local hooks and shared hooks
- cleaning up inconsistent hook file conventions

## Rules

### Mandatory

- use `.hook.ts` for hook files
- start hook names with `use`

### Default

- keep component-specific hooks next to the component that owns them
- move reusable hooks to a shared location with clearer ownership
- prefer one main component hook instead of several tiny local hook files unless the split has a strong reason

### Heuristics

- if a helper is reused across siblings or features, it likely wants a shared location
- if a hook exists only to hide a few lines with no meaningful abstraction, keep the logic in the component

### Exceptions

- preserve established nearby naming if strict local consistency matters more than global cleanup

## Anti-patterns

- using `.hook.tsx`
- proliferating many tiny local hooks with weak boundaries
- hiding trivial logic behind a hook that adds indirection without reuse
