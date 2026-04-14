---
type: twir-item
issue: 271
item: 6
item_type: item
date: 2026-03-04
source: https://github.com/TheAlexLichter/oxlint-react-compiler-rules
tags:
  - "ReactCompiler"
status: auto
---

[[2026-03-04-TWIR-271|Index]]

# Item 6: Oxlint + React Compiler Rules integration demo

Source: [https://github.com/TheAlexLichter/oxlint-react-compiler-rules](https://github.com/TheAlexLichter/oxlint-react-compiler-rules)

Summary:
This project demonstrates integrating React Compiler (Hooks) rules into Oxlint via its JS plugin system, allowing developers to enforce React linting rules in a Rust-based linter. The example shows how to catch common React anti-patterns, such as calling setState in render, using a demo app with Vite 8 beta and Oxlint.

Key takeaways:
- Oxlint can now run React Compiler/ESLint rules via JS plugins, enhancing static analysis.
- Demonstrates catching infinite render loops and other common React mistakes.
- Configuration is straightforward, requiring explicit rule enabling.
- Useful for teams seeking faster or more robust linting in large codebases.

Recommendation: Summary sufficient

Related notes: [[React Compiler]]
