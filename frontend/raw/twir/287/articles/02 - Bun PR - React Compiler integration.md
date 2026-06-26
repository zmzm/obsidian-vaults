---
type: twir-item
issue: 287
item: 2
item_type: item
date: 2026-06-24
source: https://github.com/oven-sh/bun/pull/32504
tags:
  - "ReactCompiler"
  - "PR"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 2: Bun PR - React Compiler integration

Source: [https://github.com/oven-sh/bun/pull/32504](https://github.com/oven-sh/bun/pull/32504)

Summary:
Bun is integrating the upstream React Compiler as a built-in transform, enabling auto-memoization of components and hooks during build time without relying on Babel, SWC, or OXC. The integration ports the React Compiler’s Rust crates directly, optimizing hot-path data structures and providing a fast, native compilation pipeline. Benchmarks show significant performance improvements, and the integration passes nearly all upstream test fixtures.

Key takeaways:
- React Compiler is now a native option in Bun, invoked via bun build --react-compiler or Bun.build({ reactCompiler: true }).
- Eliminates intermediate ASTs and leverages Bun’s parser for direct compilation, resulting in faster builds (3.6× faster than Babel plugin).
- No new runtime dependencies; binary size increases by ~1MB.
- Extensive test coverage: 1,647/1,807 upstream fixtures pass, with clear documentation on limitations and new build options.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
