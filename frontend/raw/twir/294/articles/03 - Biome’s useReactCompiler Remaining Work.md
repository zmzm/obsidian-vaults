---
type: twir-item
issue: 294
item: 3
item_type: item
date: 2026-08-19
source: https://github.com/biomejs/biome/issues/10974
tags:
  - "useReactCompiler"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-08-19-TWIR-294|Index]]

# Item 3: Biome’s useReactCompiler Remaining Work

Source: [https://github.com/biomejs/biome/issues/10974](https://github.com/biomejs/biome/issues/10974)

Summary:
Biome is tracking remaining work for its useReactCompiler feature, focusing on test case parity with Babel and OXC, and addressing edge cases and known divergences in the Rust port. The issue lists specific failing test cases, areas where Biome matches Babel but OXC lags, and backend limitations. Suggestions include splitting the rule, improving diagnostics, and optimizing the AST conversion pipeline.

Key takeaways:
- Biome’s React Compiler integration is close to Babel parity, but OXC’s oracle under-reports some errors.
- Several deep edge cases and backend limitations are documented and tracked.
- Plans to improve rule granularity and diagnostics, and to streamline AST handling.
- Community input and contributions are encouraged.

Recommendation:
Summary sufficient (unless you are contributing to Biome or need details on test case parity)

Why it matters:
unless you are contributing to Biome or need details on test case parity

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
