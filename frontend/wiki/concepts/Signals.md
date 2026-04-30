---
type: concept
status: active
updated: 2026-04-14
tags:
  - reactivity
  - signals
---

# Signals

Signals are a reactivity model where updates propagate through a dependency graph more locally and explicitly than in a classic tree-wide rerender model.

## Key Ideas

- Signal-based models emphasize targeted updates and explicit dependencies.
- For frontend architecture, this matters as an alternative or complement to the familiar React mental model.
- The topic intersects with discussions about reactive cores, fine-grained updates, and UI performance.

## Practical Significance

- It helps compare different reactivity models rather than discussing React in isolation.
- It is a useful lens for evaluating routing, state, and rendering abstractions.

## Current Signals

- The current source set is still lighter here than in some other areas, but it now has enough comparative material to support a durable concept page.
- The strongest current value of this page is as a comparative lens against React Compiler and tree-scheduled rendering.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../tools/TanStack Query|TanStack Query]]
- [[React Compiler]]
- [[../syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]]
- [[../case-studies/Atomic State in Deep Trees|Atomic State in Deep Trees]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]

## Sources

- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]

## Open Questions

- Where a signals-based model genuinely simplifies reasoning and where it introduces new complexity.
- Which parts of the React ecosystem are effectively moving in a similar direction without explicitly using signals.
