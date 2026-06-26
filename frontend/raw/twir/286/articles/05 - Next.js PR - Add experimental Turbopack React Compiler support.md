---
type: twir-item
issue: 286
item: 5
item_type: item
date: 2026-06-17
source: https://github.com/vercel/next.js/pull/94573
tags:
  - "ReactCompiler"
  - "Nextjs"
  - "PR"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 5: Next.js PR - Add experimental Turbopack React Compiler support

Source: [https://github.com/vercel/next.js/pull/94573](https://github.com/vercel/next.js/pull/94573)

Summary:
Next.js introduces an experimental.rustReactCompiler config option to enable the Rust-based React Compiler in Turbopack builds. This option requires config.reactCompiler to be set and only applies to client and SSR code. The compiler runs directly on Turbopack’s SWC AST for efficiency, but there are caveats with decorator transforms in non-TS files.

Key takeaways:
- Experimental opt-in for Rust React Compiler in Turbopack via config.
- Only affects client and SSR code, not React Server Components.
- Integrates directly with SWC AST for performance.
- Some transform ordering issues with decorators in .js/.jsx files.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]], [[Server Components]]
