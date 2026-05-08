---
type: twir-item
issue: 195
item: 8
item_type: item
date: 2024-08-07
source: https://jordaneldredge.com/notes/unstable_cache/
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2024-08-07-TWIR-195|Index]]

# Item 8: Next.js’s unstable_cache() demystified

Source: [https://jordaneldredge.com/notes/unstable_cache/](https://jordaneldredge.com/notes/unstable_cache/)

Summary:
The article explores the quirks and limitations of Next.js’s unstable_cache(), highlighting unpredictable behavior, serialization constraints, and context-specific caching. The author shares personal experiences and references community findings, ultimately opting for a simpler in-memory caching approach until the API matures.

Key takeaways:
- unstable_cache() caches across requests but has subtle, confusing behaviors.
- Returned values must be serializable; classes and some objects fail.
- Not suitable for scripts or non-request contexts.
- Simpler memoization may be preferable for many use cases.

Recommendation:
Read fully (read fully if you are considering or debugging unstable_cache in Next.js)

Why it matters:
read fully if you are considering or debugging unstable_cache in Next.js

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
