---
type: twir-item
issue: 284
item: 6
item_type: item
date: 2026-06-03
source: https://github.com/facebook/react/pull/36173#issuecomment-4608356402
tags:
  - "Compiler"
  - "PR"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-06-03-TWIR-284|Index]]

# Item 6: React Compiler update - The Rust compiler PR to be merged soon

Source: [https://github.com/facebook/react/pull/36173#issuecomment-4608356402](https://github.com/facebook/react/pull/36173#issuecomment-4608356402)

Summary:
React Compiler is being ported to Rust, with early results showing significant performance improvements (up to 3x faster as a Babel plugin, 10x faster transformation logic). The Rust port mirrors the TypeScript version’s architecture, using a Babel-like AST and a high-level intermediate representation (HIR). Integration examples for OXC and SWC are provided, and the team seeks feedback from partners. The port is still experimental, with all fixtures passing but further validation and optimization ongoing.

Key takeaways:
- Rust port of React Compiler is in progress, showing promising speedups over the TypeScript version.
- The architecture uses a Babel-like AST and HIR, aiming for compatibility with multiple toolchains (Babel, OXC, SWC).
- All test fixtures pass, but further validation and internal testing are needed.
- The team encourages partners to try integrating the Rust compiler and provide feedback.

Recommendation:
Summary sufficient (read PR for deep integration or contribution details)

Why it matters:
read PR for deep integration or contribution details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
