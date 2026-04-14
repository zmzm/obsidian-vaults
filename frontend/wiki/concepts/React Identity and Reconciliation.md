---
type: concept
status: active
updated: 2026-04-14
tags:
  - react
  - reconciliation
  - identity
  - keys
---

# React Identity and Reconciliation

React Identity and Reconciliation is the concept page for how React preserves, discards, and updates component instances across renders.

## Key Ideas

- Reconciliation is the process React uses to compare one render output against the next and decide what work should be preserved, updated, or replaced.
- Identity is not just about DOM reuse; it also determines whether component state is retained or reset.
- `key` is one of the most visible APIs that lets developers participate in reconciliation and identity control.

## Practical Significance

- This concept explains a large class of subtle React bugs involving list behavior, state retention, and unexpected remounts.
- It is a useful bridge between everyday React usage and deeper rendering internals.

## Current Signals

- The current source set already contains one practical source on `key` and several broader sources on Fiber and async rendering.
- That is enough to justify a dedicated concept node instead of leaving reconciliation scattered under the larger rendering topic.

## Related Pages

- [[React Compiler]]
- [[Signals]]
- [[React use()]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/React Key Prop|React Key Prop]]
- [[../sources/How State Updates Work Internally|How State Updates Work Internally]]
- [[../sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]]
- [[../sources/Async React Evolution|Async React Evolution]]

## Sources

- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/React Key Prop|React Key Prop]]
- [[../sources/How State Updates Work Internally|How State Updates Work Internally]]
- [[../sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]]
- [[../sources/Async React Evolution|Async React Evolution]]

## Open Questions

- Which reconciliation behaviors should later become their own narrower pages, such as list identity or state preservation semantics.
- How much internal reconciliation knowledge is actually useful for everyday application design.
