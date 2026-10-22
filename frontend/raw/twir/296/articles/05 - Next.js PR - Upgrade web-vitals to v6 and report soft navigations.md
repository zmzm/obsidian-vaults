---
type: twir-item
issue: 296
item: 5
item_type: item
date: 2026-09-09
source: https://github.com/vercel/next.js/pull/97232
tags:
  - "Nextjs"
  - "PR"
  - "v6"
status: auto
quality: keep
---

[[2026-09-09-TWIR-296|Index]]

# Item 5: Next.js PR - Upgrade web-vitals to v6 and report soft navigations

Source: [https://github.com/vercel/next.js/pull/97232](https://github.com/vercel/next.js/pull/97232)

Summary:
Next.js upgrades its web-vitals dependency to v6.x, enabling reporting of soft navigations for key metrics (CLS, INP, LCP) and improving attribution via navigationURL. The update removes obsolete FID support, updates metric types and docs, and ensures accurate reporting for both initial and soft navigations. Test coverage and bundles are updated to match the new API.

Key takeaways:
- Soft navigation metrics are now reported, improving accuracy for client-side navigations.
- Obsolete FID metric and compatibility layers are removed, aligning with current web-vitals standards.
- Documentation and public metric types are updated for consistency with upstream.
- No significant bundle size or performance regressions reported.

Recommendation:
Read fully (read fully if you integrate with web-vitals or need precise navigation metrics)

Why it matters:
read fully if you integrate with web-vitals or need precise navigation metrics

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Python clipper extracted too little content. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
