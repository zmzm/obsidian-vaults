---
type: twir-item
issue: 279
item: 2
item_type: item
date: 2026-04-29
source: https://github.com/facebook/react/pull/36173#issuecomment-4328422631
tags:
  - "Compiler"
  - "WIP"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-04-29-TWIR-279|Index]]

# Item 2: WIP port of React Compiler to Rust

Source: [https://github.com/facebook/react/pull/36173#issuecomment-4328422631](https://github.com/facebook/react/pull/36173#issuecomment-4328422631)

Summary:
Facebook is developing an experimental Rust port of the React Compiler, sharing early progress for community feedback. The Rust version mirrors the TypeScript architecture, using a Babel AST-based public API and integrating with Babel, OXC, and SWC. All fixtures pass, with performance already showing significant speedups (3x as a Babel plugin, 10x in transformation logic), though the project is still in early stages and lacks builds. The team is seeking partners for integration and is open to feedback on AST and scope representations.

Key takeaways:
- Rust port aims for parity with TypeScript implementation, using similar architecture and testing strategies.
- Early benchmarks show substantial performance improvements.
- Integrations for Babel, OXC, and SWC are in progress; partners are encouraged to experiment and provide feedback.
- Scope analysis is not yet implemented in Rust; current integrations must provide this data.

Recommendation:
Read fully (for those interested in compiler internals or contributing/integrating)

Why it matters:
for those interested in compiler internals or contributing/integrating

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
