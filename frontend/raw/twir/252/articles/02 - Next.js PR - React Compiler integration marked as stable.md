---
type: twir-item
issue: 252
item: 2
item_type: item
date: 2025-10-01
source: https://github.com/vercel/next.js/pull/84220
tags:
  - "Compiler"
  - "Nextjs"
  - "PR"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-10-01-TWIR-252|Index]]

# Item 2: Next.js PR - React Compiler integration marked as stable

Source: [https://github.com/vercel/next.js/pull/84220](https://github.com/vercel/next.js/pull/84220)

Summary:
A Next.js pull request marks React Compiler integration as stable, but highlights a configuration mismatch that currently breaks the feature. The PR shifts the config from config.experimental?.reactCompiler to config.reactCompiler, but related code still references the old property, causing the compiler not to activate as expected. Test failures and loader initialization issues are noted, with a need for further fixes before the compiler works reliably.

Key takeaways:
- React Compiler is now considered stable in Next.js but is still off by default and not yet fully functional due to config mismatches.
- Code references to the old experimental config prevent the compiler from activating, even when enabled in the main config.
- Test suites for partial hydration and streaming are failing, indicating unresolved integration issues.
- Developers should monitor for follow-up fixes before relying on React Compiler in production Next.js apps.

Recommendation:
Summary sufficient (read PR or follow Next.js changelogs if planning to use React Compiler soon)

Why it matters:
read PR or follow Next.js changelogs if planning to use React Compiler soon

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
