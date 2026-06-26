---
type: twir-item
issue: 286
item: 2
item_type: item
date: 2026-06-17
source: https://github.com/rolldown/rolldown/pull/9801
tags:
  - "ReactCompiler"
  - "PR"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 2: Rolldown PR - Expose React Compiler options

Source: [https://github.com/rolldown/rolldown/pull/9801](https://github.com/rolldown/rolldown/pull/9801)

Summary:
This PR exposes Oxc’s experimental React Compiler to Rolldown’s transform option layers, allowing React/Vite users to opt into compiler memoization. The compiler can be enabled via several configuration paths (bundler, Vite plugin, standalone transform APIs) and runs as the first pass on the AST, with diagnostics integrated into standard error/warning channels. The implementation threads options through Rust/TS layers, and comprehensive tests cover all configuration scenarios.

Key takeaways:
- React Compiler can now be enabled in Rolldown and Vite via multiple config entry points.
- Runs early in the transform pipeline for accurate analysis and memoization.
- Node-side and fixture-based tests ensure robust coverage.
- Documentation and TS types updated for the new feature.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
