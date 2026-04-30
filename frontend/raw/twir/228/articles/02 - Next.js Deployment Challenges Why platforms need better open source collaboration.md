---
type: twir-item
issue: 228
item: 4
item_type: item
date: 2025-04-02
source: https://www.netlify.com/blog/how-we-run-nextjs/
tags:
  - "Nextjsdeployment"
  - "Nextjs"
status: auto
quality: keep
---

[[2025-04-02-TWIR-228|Index]]

# Item 4: Next.js Deployment Challenges: Why platforms need better open source collaboration

Source: [https://www.netlify.com/blog/how-we-run-nextjs/](https://www.netlify.com/blog/how-we-run-nextjs/)

Summary:
Netlify details the engineering challenges of supporting Next.js deployments outside of Vercel, highlighting the lack of an adapter mechanism and insufficient documentation for production-grade serverless deployments. The post advocates for open standards and better collaboration to enable portability and maintainability across hosting providers. It also notes recent progress, such as the publication of an RFC for adapters.

Key takeaways:
- Next.js lacks a public adapter mechanism, making non-Vercel deployments complex and fragile.
- Other frameworks (Astro, SvelteKit, etc.) use adapters for easy portability; Next.js does not.
- Providers must reverse-engineer Vercel’s build output, increasing maintenance burden.
- Documentation for scalable, production serverless deployments is lacking, leading to potential pitfalls (e.g., stale cache issues).

Recommendation:
Read fully (valuable for teams deploying Next.js at scale or on non-Vercel platforms)

Why it matters:
valuable for teams deploying Next.js at scale or on non-Vercel platforms

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
