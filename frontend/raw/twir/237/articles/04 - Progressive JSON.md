---
type: twir-item
issue: 237
item: 4
item_type: item
date: 2025-06-04
source: https://overreacted.io/progressive-json/
tags:
  - "JSON"
status: auto
quality: keep
---

[[2025-06-04-TWIR-237|Index]]

# Item 4: Progressive JSON

Source: [https://overreacted.io/progressive-json/](https://overreacted.io/progressive-json/)

Summary:
Dan Abramov explores the concept of "progressive JSON," applying ideas from progressive JPEGs to JSON data transfer. He discusses the limitations of traditional and streaming JSON, then proposes a breadth-first, placeholder-based approach that enables clients to incrementally resolve and use parts of a JSON tree as they arrive. This model could improve perceived performance and flexibility in data-heavy web apps.

Key takeaways:
- Traditional JSON transfer is all-or-nothing; streaming JSON is hard to use due to incomplete types.
- Progressive JSON uses placeholders and promises to allow out-of-order, incremental data resolution.
- This approach can decouple slow parts of the data tree from blocking the rest, improving UX.

Recommendation:
Read fully (for anyone interested in advanced data loading or RSC internals)

Why it matters:
for anyone interested in advanced data loading or RSC internals

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
