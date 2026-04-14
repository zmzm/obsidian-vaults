---
type: source
status: active
updated: 2026-04-14
tags:
  - react
  - reconciliation
  - keys
  - source
---

# React Key Prop

This source is a practical explainer for how React uses `key` to preserve identity during reconciliation.

## Summary

- Keys help React identify list items correctly during reconciliation.
- Using array indexes as keys can introduce bugs, unstable UI behavior, and incorrect state retention.
- Keys are mainly important where identity must be preserved across list updates rather than as a blanket rule for every component.

## Why This Source Matters

- It gives the vault a concrete, developer-facing explanation of one of the most common React correctness pitfalls.
- It complements the broader rendering material by grounding reconciliation in a familiar everyday API.

## Caveats

- This is an educational source, not a deep architecture document.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React Identity and Reconciliation|React Identity and Reconciliation]]

## Raw Sources

- [[../../raw/twir/273/articles/09 - Making sense of 'key' prop in React|TWIR item note]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
