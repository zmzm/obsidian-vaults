---
type: twir-item
issue: 294
item: 1
item_type: featured
date: 2026-08-19
source: https://oxc.rs/blog/2026-08-18-react-compiler-support
tags:
  - "ReactCompiler"
  - "179"
  - "Vite"
status: auto
quality: keep
---

[[2026-08-19-TWIR-294|Index]]

# Item 1: Oxlint 1.79 Adds React Compiler Support

Source: [https://oxc.rs/blog/2026-08-18-react-compiler-support](https://oxc.rs/blog/2026-08-18-react-compiler-support)

Summary:
Oxlint 1.79 and Oxc Transform now support the React Compiler, providing 22 new lint rules powered by the compiler’s validation passes. The oxc-transform-react package applies automatic memoization and is benchmarked at over 10x faster than Babel. Vite integration is available via @vitejs/plugin-react v6.1.0, and the integration is designed to be vendor-neutral. The Oxc team completed and improved the Rust port of React Compiler, resulting in better performance, diagnostics, and smaller binary size.

Key takeaways:
- 22 React Compiler-powered lint rules now available in Oxlint, aligned with ESLint presets.
- oxc-transform-react offers automatic memoization at significantly higher speed than Babel.
- Vite 8 integration via @vitejs/plugin-react v6.1.0, with compiler option for experimental use.
- Rust port of React Compiler was completed and optimized for performance, conformance, and diagnostics.
- Binary size reduced from 8.66 MiB to 3.97 MiB; React Compiler remains an optional package.

Recommendation:
Read fully (especially if you use Oxlint, Oxc, or are interested in React Compiler integration and performance details)

Why it matters:
especially if you use Oxlint, Oxc, or are interested in React Compiler integration and performance details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]], [[Vite]]
