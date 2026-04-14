---
type: concept
status: active
updated: 2026-04-14
tags:
  - react
  - compiler
---

# React Compiler

React Compiler is a direction in the React ecosystem where part of the optimization and reactive analysis burden moves into the compiler layer.

## Key Ideas

- The compiler aims to infer optimizations that previously often required manual patterns.
- Changes around React Compiler affect not only performance but also the way components are authored.
- A Rust-based implementation and tighter integration with other toolchain components could affect both performance and adoption.

## Practical Significance

- This topic matters for understanding future React best practices.
- It is worth tracking which existing optimization patterns become less necessary and which constraints remain.

## Current Signals

- The current raw layer already contains a high-value implementation signal through the Rust port work.
- This suggests the topic should be tracked both as a React concept and as a build-toolchain topic.
- New raw material also adds a stronger comparative source on compiler-driven UI models and their limits.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../topics/React Rendering|React Rendering]]
- [[Signals]]
- [[../syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]

## Sources

- [[../../raw/twir/268/2026-02-11-TWIR-268|TWIR #268]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]

## Open Questions

- Which classes of optimizations are already covered reliably by the compiler.
- How recommendations around `memo`, derived state, and component boundaries may change.
