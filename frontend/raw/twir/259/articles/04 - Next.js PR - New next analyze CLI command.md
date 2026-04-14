---
type: twir-item
issue: 259
item: 4
item_type: item
date: 2025-11-19
source: https://github.com/vercel/next.js/pull/85915
tags:
  - "Nextjs"
  - "PR"
  - "CLI"
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 4: Next.js PR - New next analyze CLI command

Source: [https://github.com/vercel/next.js/pull/85915](https://github.com/vercel/next.js/pull/85915)

Summary:
A new next experimental-analyze CLI command generates bundle analyzer data for Next.js projects without writing chunks to disk, and can optionally serve the analyzer UI locally. This streamlines bundle analysis workflows, especially with Turbopack, and introduces several improvements for network errors and UI annotations.

Key takeaways:
- next experimental-analyze produces bundle analysis data and UI without full builds.
- --serve flag launches a local server for interactive analysis.
- Integrates with Turbopack and improves developer experience for performance tuning.

Recommendation:
Summary sufficient

Content:
# a built-in bundle analyzer for Turbopack by wbinnssmith · Pull Request #85915 · vercel/next.js · GitHub

```
…ercel#85915)

This implements `next experimental-analyze`, which generates bundle analyzer data without without writing chunks or other artifacts to disk. It also optionally serves the bundle analyzer so it can be browsed easily.

Examples:

`next experimental-analyze` - writes analyzer data and UI to `.next/diagnostics/analyze`
`next experimental-analyze --serve` - writes analyzer data and UI as well as serves the files on a static file server on localhost (by default on port 4000)
`next experimental-analyze --serve --port 4001` -- runs the above on port 4001
```
