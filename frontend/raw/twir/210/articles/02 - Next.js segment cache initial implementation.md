---
type: twir-item
issue: 210
item: 2
item_type: item
date: 2024-11-20
source: https://github.com/vercel/next.js/pull/72875
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2024-11-20-TWIR-210|Index]]

# Item 2: Next.js segment cache initial implementation

Source: [https://github.com/vercel/next.js/pull/72875](https://github.com/vercel/next.js/pull/72875)

Summary:
Next.js is introducing an experimental client Segment Cache, which caches data per route segment rather than per full URL. This approach deduplicates shared layouts in the cache, reducing bandwidth and improving efficiency. The cache is designed for synchronous reads and avoids async/await to prevent race conditions, with a scheduler inspired by React Suspense and Rust Futures. The implementation is not production-ready and will evolve to reach feature parity with the current system.

Key takeaways:
- Segment Cache enables per-segment data caching, deduplication, and more efficient navigation.
- Synchronous cache reads and pull-based task scheduling minimize race conditions.
- No eviction policy yet; LRU is planned for memory management.
- Still experimental—intended for future Next.js releases, not production use.

Recommendation:
Summary sufficient (unless contributing to Next.js internals or building advanced caching strategies)

Why it matters:
unless contributing to Next.js internals or building advanced caching strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
