---
type: pattern
status: active
updated: 2026-04-21
tags:
  - react
  - effects
  - cleanup
  - reliability
---

# Effects and Cleanup Discipline

Effects and Cleanup Discipline is the pattern page for how React code should synchronize with external systems without leaking subscriptions, timers, listeners, or stale side effects.

## Key Ideas

- Effects should exist to synchronize React with systems outside render, not to compensate for missing render-time data primitives.
- Cleanup is part of correctness, not only a performance concern.
- Small local mistakes in effect handling can accumulate into systemic reliability issues across large applications.

## Practical Significance

- This pattern gives the vault a dedicated landing page for memory leaks, side-effect hygiene, and the boundary between render logic and external synchronization.
- It also helps separate async rendering concepts from effect discipline, which are often confused in day-to-day React usage.

## Current Signals

- The current source base already includes practical evidence on memory leaks at scale and direct comparison material around `useEffect` versus newer async/rendering primitives.
- That is enough to justify a dedicated pattern node instead of leaving effect discipline buried inside broader rendering discussions.
- The newer archive also adds more explicit decision-tree guidance and proof that teams increasingly enforce effect discipline with lint rules instead of only review feedback.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React use()|React use()]]
- [[../concepts/React useEffectEvent|React useEffectEvent]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[../sources/Custom ESLint Rules|Custom ESLint Rules]]
- [[../case-studies/GitHub Diff Performance|GitHub Diff Performance]]
- [[../case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]]

## Sources

- [[../../raw/twir/271/articles/13 - Frontend Memory Leaks A 500-Repository Static Analysis|Frontend Memory Leaks A 500-Repository Static Analysis]]
- [[../../raw/twir/273/articles/04 - Why we banned React's useEffect|Why we banned React's useEffect]]
- [[../../raw/twir/276/articles/05 - You really, really, really don't need an effect! I swear!|You really, really, really don't need an effect! I swear!]]
- [[../sources/Custom ESLint Rules|Custom ESLint Rules]]
- [[../case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]]

## Open Questions

- Which classes of effects should later be modeled separately, such as subscriptions, DOM integration, or async orchestration.
- Whether the vault needs a narrower follow-up page specifically for `useEffectEvent` and event-driven effect patterns.
