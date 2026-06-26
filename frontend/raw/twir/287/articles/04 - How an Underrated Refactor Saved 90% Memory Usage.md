---
type: twir-item
issue: 287
item: 4
item_type: item
date: 2026-06-24
source: https://tanstack.com/blog/tanstack-table-v9-memory-performance
tags:
  - "90"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 4: How an Underrated Refactor Saved 90% Memory Usage

Source: [https://tanstack.com/blog/tanstack-table-v9-memory-performance](https://tanstack.com/blog/tanstack-table-v9-memory-performance)

Summary:
TanStack Table V9 achieved up to 90% memory reduction compared to V8 for large tables by refactoring to use shared prototypes for row, column, cell, and header objects. Previously, each instance had its own methods and closures, leading to high memory usage. By moving methods to prototypes and reducing per-instance closures, memory usage now scales much better for large datasets.

Key takeaways:
- V8 created millions of nearly identical objects with duplicated methods and closures, causing memory bloat.
- V9 uses shared prototypes, so only data is unique per instance; methods are shared, drastically reducing memory.
- Benchmarks show V9 can handle 10–16 million rows before hitting browser memory limits, versus 1–1.5 million in V8.
- The refactor is simple, broadly applicable, and introduces only one breaking change.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
