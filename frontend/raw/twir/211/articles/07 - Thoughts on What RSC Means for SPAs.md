---
type: twir-item
issue: 211
item: 7
item_type: item
date: 2024-11-27
source: https://blog.axlight.com/posts/thoughts-on-what-rsc-means-for-spas/
tags:
  - "RSC"
  - "SPAs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-11-27-TWIR-211|Index]]

# Item 7: Thoughts on What RSC Means for SPAs

Source: [https://blog.axlight.com/posts/thoughts-on-what-rsc-means-for-spas/](https://blog.axlight.com/posts/thoughts-on-what-rsc-means-for-spas/)

Summary:
This article discusses how React Server Components (RSC) can benefit SPAs, even without a runtime server. By serializing static parts of the component tree at build time, SPAs can reduce JS bundle size and offload work from the client. If an API server is present, RSC payloads can replace JSON, enabling streaming and component-level data transfer.

Key takeaways:
- RSC can reduce bundle size for SPAs by serializing static components at build time.
- RSC payloads can be fetched on demand, similar to lazy-loaded JS.
- With an API server, RSC enables streaming and avoids defining explicit data formats.
- Adopting RSC requires a mental shift in component responsibility (server vs client).

Recommendation:
Read fully (read fully if exploring RSC for SPA architectures)

Why it matters:
read fully if exploring RSC for SPA architectures

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
