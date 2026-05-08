---
type: twir-item
issue: 199
item: 4
item_type: item
date: 2024-09-04
source: https://fotis.xyz/posts/introducing-svg-use/
tags:
  - "svg-use"
  - "EAS"
status: auto
quality: keep
---

[[2024-09-04-TWIR-199|Index]]

# Item 4: Introducing @svg-use

Source: [https://fotis.xyz/posts/introducing-svg-use/](https://fotis.xyz/posts/introducing-svg-use/)

Summary:
@svg-use is a new toolchain and set of bundler plugins for ergonomically loading SVGs as components using SVG’s `<use href>` mechanism, as an alternative to SVG-in-JS. The article compares SVG-in-JS (e.g., via svgr) with referencing SVGs as assets using `<img src>` and `<use href>`, analyzing the tradeoffs in theming, performance, and portability. @svg-use aims to make the `<use href>` pattern more competitive by addressing ergonomics and future-proofing for web standards.

Key takeaways:
- SVG-in-JS offers theming and easy import, but increases JS bundle size and DOM duplication.
- `<img src>` is efficient for delivery but lacks theming capabilities.
- `<use href>` enables referencing shared SVG assets with better performance and theming potential.
- @svg-use provides tooling to make `<use href>` practical in React and JS frontends.

Recommendation:
Read fully (for those dealing with SVGs/icons in React apps)

Why it matters:
for those dealing with SVGs/icons in React apps

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
