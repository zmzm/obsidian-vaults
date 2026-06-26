---
type: twir-item
issue: 286
item: 1
item_type: featured
date: 2026-06-17
source: https://oxc.rs/docs/guide/usage/linter/rules/react/react-compiler.html
tags:
  - "170"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 1: Oxlint 1.70 - Add a react/react-compiler rule

Source: [https://oxc.rs/docs/guide/usage/linter/rules/react/react-compiler.html](https://oxc.rs/docs/guide/usage/linter/rules/react/react-compiler.html)

Summary:
Oxlint 1.70 introduces an experimental lint rule that runs the React Compiler's analysis in lint-only mode, surfacing violations of the Rules of React (e.g., conditional hooks, reading refs during render, mutating props/state). The rule mirrors diagnostics from eslint-plugin-react-compiler and can optionally report compiler bailouts where optimization is skipped. Configuration is flexible, and the rule is enabled via standard Oxlint config or CLI.

Key takeaways:
- Detects code patterns that break React's rules and hinder compiler optimizations.
- Reports both violations and, optionally, bailouts where code can't be optimized.
- Experimental status: rule behavior may change as it matures.
- Easy to enable in Oxlint via config or CLI.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
