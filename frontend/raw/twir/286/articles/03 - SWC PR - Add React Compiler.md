---
type: twir-item
issue: 286
item: 3
item_type: item
date: 2026-06-17
source: https://github.com/swc-project/swc/pull/11917
tags:
  - "ReactCompiler"
  - "SWC"
  - "PR"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 3: SWC PR - Add React Compiler

Source: [https://github.com/swc-project/swc/pull/11917](https://github.com/swc-project/swc/pull/11917)

Summary:
SWC adds experimental support for the Rust React Compiler, bridging SWC and React Compiler ASTs/scopes and exposing configuration via .swcrc (jsc.transform.reactCompiler). Diagnostics are forwarded, and tests from upstream SWC integration are ported. The PR is pending publication of official React Compiler Rust crates, and some overlap with SWC’s resolver is noted for future refactoring.

Key takeaways:
- Enables React Compiler integration in SWC via a new bridge and config option.
- Diagnostics and configuration are surfaced through standard SWC mechanisms.
- Some architectural overlap with SWC’s resolver; future consolidation possible.
- Awaiting official crate publication to finalize dependencies.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
