---
type: source
status: active
updated: 2026-04-14
tags:
  - react
  - state
  - fiber
  - source
---

# How State Updates Work Internally

This source gives a useful internal model for why React state updates are scheduled, batched, and not immediately visible after `setState`.

## Summary

- State updates are queued and scheduled rather than applied as direct synchronous mutations.
- Hooks are stored on Fiber nodes and participate in the update queue mechanism.
- Understanding queues and batching helps explain many everyday React state pitfalls.

## Why This Source Matters

- It strengthens both `React Rendering` and `React Identity and Reconciliation` with internals-level support.
- It gives the wiki a more explicit state-model source instead of inferring state behavior only from rendering sources.

## Caveats

- This is still an educational secondary source, not the canonical implementation reference.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React Identity and Reconciliation|React Identity and Reconciliation]]
- [[../sources/TWIR 272|TWIR 272]]

## Raw Sources

- [[../../raw/twir/272/articles/03 - How state updates work internally|TWIR item note]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
