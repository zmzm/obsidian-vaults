---
type: twir-item
issue: 211
item: 3
item_type: item
date: 2024-11-27
source: https://github.com/vercel/next.js/pull/72195
tags:
  - "Nextjs"
  - "PR"
  - "CSS"
status: auto
quality: keep
---

[[2024-11-27-TWIR-211|Index]]

# Item 3: Next.js PR - CSS inlining

Source: [https://github.com/vercel/next.js/pull/72195](https://github.com/vercel/next.js/pull/72195)

Summary:
Next.js introduces an experimental inlineCSS flag for the App Router, which inlines CSS as <style> tags instead of generating <link> tags. This leverages React 19's automatic CSS precedence and deduplication, aiming to optimize LCP/FCP for sites with relatively static CSS. The feature is experimental and not recommended for production use yet.

Key takeaways:
- inlineCSS inlines all CSS assets as <style> tags, managed by React 19.
- Intended to improve performance metrics (LCP/FCP) for certain site types.
- Works with both Webpack and Turbopack.
- Experimental—do not use in production.

Recommendation:
Summary sufficient (read PR if interested in experimental Next.js features or CSS optimization)

Why it matters:
read PR if interested in experimental Next.js features or CSS optimization

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
