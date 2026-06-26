---
type: twir-item
issue: 286
item: 4
item_type: item
date: 2026-06-17
source: https://github.com/web-infra-dev/rspack/pull/14435
tags:
  - "ReactCompiler"
  - "PR"
  - "SWC"
  - "Babel"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 4: Rspack PR - Bump SWC to support the React Compiler

Source: [https://github.com/web-infra-dev/rspack/pull/14435](https://github.com/web-infra-dev/rspack/pull/14435)

Summary:
Rspack updates its SWC toolchain to support React Compiler configuration via builtin:swc-loader, making this the primary documented setup for React Compiler usage. The PR bumps SWC dependencies, updates loader typing, adds focused tests, and refreshes documentation (English/Chinese) to prioritize SWC-based integration, with Babel as an alternative.

Key takeaways:
- React Compiler is now supported and documented via builtin:swc-loader in Rspack.
- SWC dependencies and typings updated to expose new config options.
- Documentation prioritizes SWC-based setup; Babel remains as fallback.
- Targeted tests ensure correct compiler output.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
