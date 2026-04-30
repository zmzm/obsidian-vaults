---
type: twir-item
issue: 217
item: 5
item_type: item
date: 2025-01-15
source: https://github.com/reactjs/react.dev/pull/6996
tags:
  - "Nextjs"
  - "Compiler"
  - "PR"
  - "15"
  - "19"
  - "Bun"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 5: React website PR - Upgrade to Next.js 15, React 19, enable React Compiler

Source: [https://github.com/reactjs/react.dev/pull/6996](https://github.com/reactjs/react.dev/pull/6996)

Summary:
The react.dev website is being upgraded to React 19, Next.js 15.1, and TypeScript 5.7.2, with the React Compiler enabled. This update removes legacy patches, addresses TypeScript and JSX issues, and results in a slight increase in global bundle size. The migration process revealed some compatibility issues, but the new stack is now working in both build and dev modes.

Key takeaways:
- React 19, Next.js 15.1, and React Compiler are now enabled on react.dev.
- Some TypeScript and JSX compatibility issues had to be resolved during the upgrade.
- Bundle size increased slightly, which may impact page load performance.
- The team recommends using newer compiler beta releases for best results.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
