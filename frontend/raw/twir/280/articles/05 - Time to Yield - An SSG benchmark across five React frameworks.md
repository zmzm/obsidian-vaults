---
type: twir-item
issue: 280
item: 5
item_type: item
date: 2026-05-06
source: https://dev.to/lazarv/time-to-yield-20m8
tags:
  - "SSG"
  - "TanStack"
  - "Astro"
status: auto
quality: keep
---

[[2026-05-06-TWIR-280|Index]]

# Item 5: Time to Yield - An SSG benchmark across five React frameworks

Source: [https://dev.to/lazarv/time-to-yield-20m8](https://dev.to/lazarv/time-to-yield-20m8)

Summary:
This benchmark compares static site generation (SSG) performance across five frameworks (Next.js, TanStack Start, Gatsby, Astro, and @lazarv/react-server) at large scales (up to 500k pages). The results show that streaming path generation (as in @lazarv/react-server) dramatically improves time-to-first-page and memory usage compared to array-based approaches. Next.js and Gatsby struggle or crash at high page counts, while streaming frameworks scale efficiently.

Key takeaways:
- Most frameworks require an array of paths, causing high memory usage and slow first-page output at scale.
- Streaming path generation (async generators) enables O(1) memory and immediate HTML output.
- @lazarv/react-server and Astro outperform Next.js and Gatsby at very large scales.
- The architectural choice of yield vs. return for path generation is decisive for SSG scalability.

Recommendation:
Read fully (for anyone working with large-scale SSG or interested in framework internals)

Why it matters:
for anyone working with large-scale SSG or interested in framework internals

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
