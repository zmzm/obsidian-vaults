---
type: concept
status: active
updated: 2026-06-26
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
- TWIR #279 shifts the branch from early implementation signal toward adoption maturity: brownfield compatibility, unsupported patterns, opt-outs, and toolchain integration now matter as much as raw optimization.
- TWIR #217 adds a production adoption signal from Wakelet, where measured UX improvements came with compatibility and code-quality caveats.
- TWIR #285 through #287 turn the Rust compiler from a PR-level signal into a broader toolchain adoption branch across Oxlint, Rolldown, SWC, Rspack, Next.js Turbopack, and Bun.
- TWIR #191, #195, #208, #209, and #213 add older compiler context: introductory explanations, OutlineJsx, Sanity Studio adoption, and real-code impact analysis.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../topics/React Rendering|React Rendering]]
- [[Signals]]
- [[../syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]
- [[../sources/React Compiler Adoption Maturity|React Compiler Adoption Maturity]]
- [[../sources/React Compiler at Wakelet|React Compiler at Wakelet]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../sources/TWIR 191|TWIR 191]]
- [[../sources/TWIR 195|TWIR 195]]
- [[../sources/TWIR 208|TWIR 208]]
- [[../sources/TWIR 209|TWIR 209]]
- [[../sources/TWIR 213|TWIR 213]]
- [[../sources/TWIR 285|TWIR 285]]
- [[../sources/TWIR 286|TWIR 286]]
- [[../sources/TWIR 287|TWIR 287]]
- [[../sources/React Compiler Toolchain Adoption|React Compiler Toolchain Adoption]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]

## Sources

- [[../../raw/twir/268/2026-02-11-TWIR-268|TWIR #268]]
- [[../../raw/twir/217/2025-01-15-TWIR-217|TWIR #217]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
- [[../../raw/twir/191/2024-06-26-TWIR-191|TWIR #191]]
- [[../../raw/twir/195/2024-08-07-TWIR-195|TWIR #195]]
- [[../../raw/twir/208/2024-11-06-TWIR-208|TWIR #208]]
- [[../../raw/twir/209/2024-11-13-TWIR-209|TWIR #209]]
- [[../../raw/twir/213/2024-12-11-TWIR-213|TWIR #213]]
- [[../../raw/twir/285/2026-06-10-TWIR-285|TWIR #285]]
- [[../../raw/twir/286/2026-06-17-TWIR-286|TWIR #286]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
- [[../sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]]
- [[../sources/React Compiler Rust Port|React Compiler Rust Port]]
- [[../sources/React Compiler Adoption Maturity|React Compiler Adoption Maturity]]
- [[../sources/React Compiler at Wakelet|React Compiler at Wakelet]]
- [[../sources/React Compiler Toolchain Adoption|React Compiler Toolchain Adoption]]

## Open Questions

- Which classes of optimizations are already covered reliably by the compiler.
- How recommendations around `memo`, derived state, and component boundaries may change.
