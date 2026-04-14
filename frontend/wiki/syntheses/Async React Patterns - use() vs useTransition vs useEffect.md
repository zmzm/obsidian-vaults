---
type: synthesis
status: active
updated: 2026-04-14
tags:
  - react
  - async
  - use-hook
  - usetransition
  - useeffect
  - comparison
---

# Async React Patterns - use() vs useTransition vs useEffect

This synthesis compares three patterns that are often mixed together in React discussions: `use()`, `useTransition`, and `useEffect`.

## Short Thesis

`use()` is best understood as a render-time async read primitive. `useTransition` is best understood as a scheduling primitive for expensive synchronous UI updates. `useEffect` is not primarily an async rendering primitive at all, even though it has often been used that way in application code.

## What `use()` Is For

- Reading promises and context during render.
- Composing with Suspense and Error Boundaries.
- Replacing effect-driven loading boilerplate in cases where data can participate directly in render.

In the current vault, `use()` looks like the clearest signal of React moving async coordination into the render model itself.

## What `useTransition` Is For

- Deferring expensive synchronous UI updates.
- Keeping the interface responsive while lower-priority rendering work continues.
- Solving scheduling and responsiveness problems, not data fetching problems.

The current source base is especially clear that `useTransition` should not be treated as a generic async or network primitive.

## What `useEffect` Is For

- Synchronizing with systems outside React after render.
- Bridging React state and lifecycle with imperative APIs, subscriptions, timers, or DOM integration.

In practice, many teams historically used `useEffect` for data loading and async orchestration. The current vault points toward that pattern becoming less central, but the supporting evidence here is still thinner than for `use()` and `useTransition`.

## Main Distinction

- `use()` changes how data can be consumed during render.
- `useTransition` changes how rendering work is prioritized.
- `useEffect` runs after render and is about side effects, not render-time async composition.

These tools operate at different layers, which is why using them as interchangeable "async React tools" creates confusion.

## Practical Heuristic

- Use `use()` when async values should participate directly in render and Suspense-style composition is appropriate.
- Use `useTransition` when the real problem is expensive synchronous rendering work that should become lower priority.
- Use `useEffect` when you need to synchronize React with external systems after commit.

## Current Evidence Quality

- The vault has good support for `use()`.
- The vault has good practical guidance for `useTransition`.
- The vault has only weak direct support for a full `useEffect` comparison, because the most relevant item in raw material is not properly extracted.

So this synthesis is strongest as a clarification of boundaries between `use()` and `useTransition`, with `useEffect` included mostly as the common source of confusion they are often compared against.

## Related Pages

- [[../concepts/React use()|React use()]]
- [[../topics/React Rendering|React Rendering]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/React useTransition|React useTransition]]
- [[../case-studies/Async React Design Components|Async React Design Components]]
- [[../case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]]

## Sources

- [[../concepts/React use()|React use()]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/React useTransition|React useTransition]]
- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/273/articles/04 - Why we banned React's useEffect|Why we banned React's useEffect]]

## Open Questions

- Whether a stronger direct source base for `useEffect` patterns should later justify a dedicated comparison or concept page.
- How much of the shift away from effect-driven async flows will remain stable across framework ecosystems.
