---
type: source
status: active
updated: 2026-04-16
tags:
  - react
  - transitions
  - rendering
  - source
---

# React useTransition

This source gives practical guidance on where `useTransition` actually fits in React performance work.

## Summary

- `useTransition` is intended for expensive synchronous UI updates, not network requests.
- It produces both an immediate render and a deferred render.
- `useDeferredValue` and debouncing remain better fits for other classes of problems.

## Why This Source Matters

- It strengthens the `React Rendering` topic with an explicit usage boundary for transitions.
- It helps prevent a common category error where transitions are used as a generic async primitive.

## Caveats

- This is practical guidance, not a formal React specification.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React use()|React use()]]
- [[../sources/TWIR 270|TWIR 270]]

## Raw Sources

- [[../../raw/twir/270/articles/10 - React’s useTransition The hook you’re probably using wrong|TWIR item note]]
- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
