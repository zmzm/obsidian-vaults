---
type: twir-item
issue: 275
item: 2
item_type: item
date: 2026-04-01
source: https://github.com/facebook/react/pull/36173
tags:
  - "ReactCompiler"
  - "PR"
  - "WIP"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 2: React Compiler PR - WIP port of React Compiler to Rust

Source: [https://github.com/facebook/react/pull/36173](https://github.com/facebook/react/pull/36173)

Summary:
An experimental, work-in-progress port of the React Compiler to Rust is underway, aiming for improved performance and broader integration with tools like OXC and SWC. The port mirrors the TypeScript implementation but leverages Rust’s performance and memory model, achieving promising early speedups. The API centers around a Rust representation of the Babel AST, with scope info provided externally for now. All fixtures currently pass, and the team is seeking feedback from partners interested in integrating the Rust compiler.

Key takeaways:
- Rust port is 3x faster as a Babel plugin, with transformation logic up to 10x faster; native integrations (OXC, SWC) expected to be even faster.
- The architecture closely follows the TS version, using HIR, CFG, and SSA, but adapts data structures for Rust’s ownership model.
- All test fixtures pass, indicating high correctness, but some areas (e.g., scope analysis) are still first-pass implementations.
- The team is open to feedback and collaboration, especially regarding AST and scope representation.

Recommendation: Read fully (read fully if you plan to integrate or contribute to the Rust compiler)

Related notes: [[React Compiler]]
