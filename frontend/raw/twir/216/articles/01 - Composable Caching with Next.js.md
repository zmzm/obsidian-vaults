---
type: twir-item
issue: 216
item: 1
item_type: featured
date: 2025-01-08
source: https://nextjs.org/blog/composable-caching
tags:
  - "Nextjs"
  - "Compiler"
status: auto
quality: keep
---

[[2025-01-08-TWIR-216|Index]]

# Item 1: Composable Caching with Next.js

Source: [https://nextjs.org/blog/composable-caching](https://nextjs.org/blog/composable-caching)

Summary:
This article introduces the new 'use cache' directive in Next.js, which enables a more robust and composable caching model for server functions and components. The directive allows the Next.js compiler to automatically determine cache keys based on function dependencies, including those captured in closures, reducing the risk of cache-related bugs. It also explains how serializable and non-serializable inputs are handled, and how cache invalidation and tagging work. The approach is compared to runtime cache functions, highlighting the benefits of static analysis and reliability.

Key takeaways:
- 'use cache' is a compiler directive that enables automatic and accurate cache key generation, even with closures.
- The mechanism supports both serializable and non-serializable inputs, using references for the latter.
- Cache invalidation and tagging are supported, allowing fine-grained cache control.
- This model reduces manual cache key management and prevents common caching pitfalls.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
