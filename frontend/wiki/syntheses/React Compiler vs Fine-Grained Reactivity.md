---
type: synthesis
status: active
updated: 2026-04-14
tags:
  - react-compiler
  - signals
  - reactivity
  - comparison
---

# React Compiler vs Fine-Grained Reactivity

This synthesis compares React Compiler with fine-grained reactivity models such as signals-oriented systems, based on the current source set in the vault.

## Short Thesis

React Compiler looks like an optimization layer that preserves React's current runtime model. Fine-grained reactivity looks like a different runtime model entirely, where updates propagate through dependency graphs rather than through a component-tree scheduling model.

## What React Compiler Appears To Be

- A way to automate optimizations that React developers previously expressed manually.
- A compiler-assisted improvement to authoring style and runtime efficiency without abandoning core React semantics.
- A strategy that keeps React recognizable while making more code compiler-friendly.

In the current vault, React Compiler looks evolutionary rather than revolutionary.

## What Fine-Grained Reactivity Appears To Be

- A model where updates target dependencies more directly.
- A runtime built around reactive graphs rather than broad component-tree rerender behavior.
- A different mental model for how UI updates propagate and where costs are paid.

In the current vault, signals-style systems look like an architectural alternative, not just a more aggressive optimizer.

## Main Difference

- React Compiler changes how React code is optimized.
- Fine-grained reactivity changes how the UI runtime fundamentally behaves.

That distinction matters because the two approaches can produce similar surface-level performance claims while operating under very different constraints.

## Where React Compiler Looks Stronger

- Compatibility with existing React semantics and ecosystem expectations.
- Incremental adoption potential through compilers and toolchains.
- Better fit for teams that want improved performance without changing the mental model of React too radically.

## Where Fine-Grained Reactivity Looks Stronger

- More explicit dependency-level updates.
- A cleaner conceptual story for avoiding broad rerender work.
- Stronger alignment with runtime models that treat reactivity as graph propagation rather than tree scheduling.

## Practical Heuristic

- Prefer the React Compiler framing when the goal is to improve React authoring and optimization while staying inside the React ecosystem.
- Prefer the fine-grained reactivity framing when the real question is whether React's component-tree runtime model is itself the wrong abstraction for a given class of UI problems.

## Current Evidence Quality

- The vault has meaningful comparative material for the conceptual distinction.
- The vault has a stronger implementation signal for React Compiler than for any one specific fine-grained framework.
- That means the synthesis is strongest on model boundaries, not on detailed head-to-head benchmark claims.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../concepts/Signals|Signals]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]

## Sources

- [[../concepts/React Compiler|React Compiler]]
- [[../concepts/Signals|Signals]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]

## Open Questions

- Whether React Compiler will remain mostly an optimization layer or gradually pull more architecture decisions into compile time.
- How much fine-grained reactivity's conceptual clarity survives in large real-world applications and tooling ecosystems.
