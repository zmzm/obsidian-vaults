---
type: twir-item
issue: 285
item: 2
item_type: item
date: 2026-06-10
source: https://github.com/react/react/pull/36173
tags:
  - "PR"
  - "RustCompiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-06-10-TWIR-285|Index]]

# Item 2: React Core PR - Port React Compiler to Rust

Source: [https://github.com/react/react/pull/36173](https://github.com/react/react/pull/36173)

Summary:
This PR details an experimental, in-progress port of the React Compiler from TypeScript to Rust, aiming for improved performance and easier integration with Rust-based tooling. The architecture closely mirrors the TypeScript version, with a Rust-based Babel AST as the public API and integrations for Babel, OXC, and SWC. Early benchmarks suggest significant speedups, and the port is seeking feedback from partners interested in integrating with other tools.

Key takeaways:
- The Rust port is work-in-progress, not yet internally tested at Meta, and requires manual setup to try.
- The Rust compiler is 3x faster as a Babel plugin and up to 10x faster in transformation logic.
- Integrations exist for Babel, OXC, and SWC, with plans for further optimization and API improvements.
- The port uses a Babel-like AST and is considering moving to patch-based output for efficiency.

Recommendation:
Read fully (for those interested in compiler internals, performance, or contributing to integrations)

Why it matters:
for those interested in compiler internals, performance, or contributing to integrations

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
