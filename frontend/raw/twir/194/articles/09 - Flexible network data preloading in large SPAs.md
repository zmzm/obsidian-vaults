---
type: twir-item
issue: 194
item: 9
item_type: item
date: 2024-07-31
source: https://mmazzarolo.com/blog/2024-07-29-data-preloading-script/
tags:
  - "Preloading"
  - "SPAs"
  - "Nextjs"
status: auto
quality: keep
---

[[2024-07-31-TWIR-194|Index]]

# Item 9: Flexible network data preloading in large SPAs

Source: [https://mmazzarolo.com/blog/2024-07-29-data-preloading-script/](https://mmazzarolo.com/blog/2024-07-29-data-preloading-script/)

Summary:
This post explores custom strategies for preloading network data in large client-side rendered SPAs, aiming to improve initial load performance by starting network requests before the app mounts. It presents a pattern for making data-fetching functions preloadable and discusses implementation details for scalable usage.

Key takeaways:
- Preloading critical data via injected scripts can reduce perceived load times in SPAs.
- The pattern allows functions to check for preloaded results, avoiding redundant fetches.
- Useful when not using frameworks like Next.js or Remix, which handle these optimizations natively.
- Implementation details include promise management and integration with React state.

Recommendation:
Read fully (if building large SPAs without SSR/SSG frameworks and optimizing load performance)

Why it matters:
if building large SPAs without SSR/SSG frameworks and optimizing load performance

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
