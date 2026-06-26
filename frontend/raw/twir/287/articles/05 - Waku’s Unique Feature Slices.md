---
type: twir-item
issue: 287
item: 5
item_type: item
date: 2026-06-24
source: https://newsletter.daishikato.com/p/waku-s-unique-feature-slices
tags:
  - "Astro"
status: auto
quality: keep
---

[[2026-06-24-TWIR-287|Index]]

# Item 5: Waku’s Unique Feature: Slices

Source: [https://newsletter.daishikato.com/p/waku-s-unique-feature-slices](https://newsletter.daishikato.com/p/waku-s-unique-feature-slices)

Summary:
Waku introduces "Slices," reusable components with their own render config, inspired by Gatsby’s Slice API. Slices are placed in a dedicated directory and referenced by ID in pages. They can be rendered statically or lazily loaded, enabling flexible composition and independent loading similar to Astro’s server islands.

Key takeaways:
- Slices are reusable, configurable components defined in src/pages/_slices and referenced via <Slice id="..."/>.
- Static and lazy slices are supported; lazy slices load independently after the initial page render.
- Slices must be declared in the page’s config unless lazy, which allows for dynamic, on-demand loading.
- The model is simple, composable, and aligns with Waku’s minimal philosophy.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
