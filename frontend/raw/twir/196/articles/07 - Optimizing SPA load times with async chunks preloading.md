---
type: twir-item
issue: 196
item: 7
item_type: item
date: 2024-08-14
source: https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/
tags:
  - "DI"
  - "SPA"
status: auto
quality: keep
---

[[2024-08-14-TWIR-196|Index]]

# Item 7: Optimizing SPA load times with async chunks preloading

Source: [https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/](https://mmazzarolo.com/blog/2024-08-13-async-chunk-preloading-on-load/)

Summary:
This post explains how to reduce the initial load delay in client-side rendered React apps by preloading route-based code-split chunks. By injecting a script that maps routes to their corresponding async chunks and preloads them in parallel with the entry point, the waterfall effect is avoided. The solution is demonstrated with Rsbuild but is adaptable to other bundlers like Webpack.

Key takeaways:
- Route-based code splitting can cause sequential loading delays in SPAs.
- Preloading async chunks for the current route reduces initial load time.
- Implementation involves mapping routes to chunk names and injecting preload scripts at build time.
- The approach is bundler-agnostic and can be adapted beyond Rsbuild.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
