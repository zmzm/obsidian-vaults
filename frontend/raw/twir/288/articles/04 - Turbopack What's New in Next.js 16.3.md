---
type: twir-item
issue: 288
item: 4
item_type: item
date: 2026-07-01
source: https://nextjs.org/blog/next-16-3-turbopack
tags:
  - "Nextjs"
  - "163"
  - "ReactCompiler"
  - "TS"
  - "Flow"
status: auto
quality: keep
---

[[2026-07-01-TWIR-288|Index]]

# Item 4: Turbopack: What's New in Next.js 16.3

Source: [https://nextjs.org/blog/next-16-3-turbopack](https://nextjs.org/blog/next-16-3-turbopack)

Summary:
Turbopack in Next.js 16.3 delivers major performance improvements, including drastic reductions in dev server memory usage (up to 90%), persistent file system caching for both dev and build, and experimental support for the Rust-based React Compiler. The release also adds support for the Vite-compatible import.meta.glob API and improves HMR efficiency, especially for large apps.

Key takeaways:
- Dev server memory usage is significantly reduced via memory eviction and file system cache.
- Persistent cache now speeds up both dev and build (CI) workflows.
- Experimental Rust React Compiler offers 20–50% faster compilation for large apps.
- import.meta.glob enables dynamic imports matching file patterns, similar to Vite.

Recommendation:
Read fully (for teams using Turbopack or interested in build performance and new APIs)

Why it matters:
for teams using Turbopack or interested in build performance and new APIs

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
