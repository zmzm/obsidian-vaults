---
type: twir-item
issue: 291
item: 4
item_type: item
date: 2026-07-22
source: https://github.com/reactjs/react.dev/pull/8527
tags:
  - "Reactdev"
  - "PR"
  - "OG"
status: auto
quality: keep
---

[[2026-07-22-TWIR-291|Index]]

# Item 4: React.dev PR - Dynamic OG images for docs pages

Source: [https://github.com/reactjs/react.dev/pull/8527](https://github.com/reactjs/react.dev/pull/8527)

Summary:
This pull request adds build-time generation of per-page Open Graph (OG) images for React documentation pages, so social media link previews display the specific page title (e.g., <Suspense>) instead of a generic banner. The implementation uses a static generation script with Satori and Resvg, integrates with the Next.js build, and updates SEO metadata accordingly. The design matches existing static cards, and the change has minimal impact on bundle size.

Key takeaways:
- Each docs page now has a unique OG image, improving link sharing and discoverability.
- Images are generated statically at build time, not on-demand, ensuring performance and reliability.
- The approach leverages Satori for rendering and Resvg for image output.

Recommendation:
Summary sufficient (read PR for implementation details or if contributing to react.dev)

Why it matters:
read PR for implementation details or if contributing to react.dev

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
