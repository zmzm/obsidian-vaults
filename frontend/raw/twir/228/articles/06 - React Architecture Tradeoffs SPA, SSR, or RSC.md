---
type: twir-item
issue: 228
item: 8
item_type: item
date: 2025-04-02
source: https://reacttraining.com/blog/react-architecture-spa-ssr-rsc
tags:
  - "SPA"
  - "SSR"
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-04-02-TWIR-228|Index]]

# Item 8: React Architecture Tradeoffs: SPA, SSR, or RSC

Source: [https://reacttraining.com/blog/react-architecture-spa-ssr-rsc](https://reacttraining.com/blog/react-architecture-spa-ssr-rsc)

Summary:
The article contrasts React SPAs (Single Page Applications) with SSR (Server-Side Rendering) and RSC (React Server Components) frameworks, emphasizing that the React team now recommends frameworks over homegrown SPAs. It outlines the tradeoffs of SPAs (performance, SEO, architecture complexity) and explains how frameworks like Next.js and React Router Framework (Remix) provide hybrid SSR/CSR approaches that simplify architecture and data-fetching.

Key takeaways:
- SPAs offer flexibility but suffer from initial load, SEO, and complex state/data management.
- Frameworks handle SSR for fast initial loads and CSR for fast navigation, automating code-splitting and data-fetching.
- Modern frameworks reduce the need for client-side architecture glue (e.g., Redux, Context).
- React team recommends using frameworks (Next.js, Remix) over custom SPA setups.

Recommendation:
Read fully (read fully if evaluating architecture choices or migrating from SPA to framework)

Why it matters:
read fully if evaluating architecture choices or migrating from SPA to framework

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
