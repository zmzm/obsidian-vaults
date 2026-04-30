---
type: concept
status: active
updated: 2026-04-21
tags:
  - react
  - effects
  - hook
  - async-rendering
---

# React useEffectEvent

`useEffectEvent` is the React concept for pulling non-reactive logic out of effects while still reading the latest props and state at call time.

## Key Ideas

- `useEffectEvent` lets an effect call logic that should see fresh values without forcing the whole effect to re-subscribe whenever that callback identity changes.
- The point is not "stable callbacks" in the usual memoization sense; the point is separating reactive dependencies from imperative event-like logic inside effects.
- It matters because many teams misuse effects by mixing subscription setup, business logic, and stale-closure workarounds in one place.

## Practical Significance

- This concept gives the vault a cleaner node between `Effects and Cleanup Discipline` and broader async-rendering APIs like `use()` and transitions.
- It is especially useful when refactoring effect-heavy code that currently over-depends on refs, `useCallback`, or intentionally broken dependency arrays.

## Current Signals

- The archive now contains both release-level framing and focused explanation material for `useEffectEvent`.
- React Conf 2025 recap material also reinforces that this is part of the current React API direction rather than a one-off niche trick.
- That is enough to justify a dedicated concept page instead of leaving it as a footnote inside the effects page.

## Related Pages

- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[../topics/React Rendering|React Rendering]]
- [[React use()]]
- [[../sources/Custom ESLint Rules|Custom ESLint Rules]]
- [[../sources/TWIR 252|TWIR 252]]
- [[../sources/TWIR 253|TWIR 253]]
- [[../sources/TWIR 254|TWIR 254]]

## Sources

- [[../../raw/twir/252/articles/01 - React 19.2|React 19.2]]
- [[../../raw/twir/253/articles/08 - Quick look into the useEffectEvent|Quick look into the useEffectEvent]]
- [[../../raw/twir/254/articles/09 - React Conf 2025 – Recap (React & React Native Days)|React Conf 2025 – Recap (React & React Native Days)]]

## Open Questions

- When `useEffectEvent` genuinely simplifies effect design versus just hiding an effect that should be removed altogether.
- How often teams will need it once render-time async patterns replace more classic effect-driven orchestration.
