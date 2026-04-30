---
type: twir-item
issue: 230
item: 1
item_type: featured
date: 2025-04-16
source: https://nextjs.org/blog/next-15-3
tags:
  - "Nextjs"
  - "153"
  - "Turbopack"
  - "Rspack"
status: auto
quality: keep
---

[[2025-04-16-TWIR-230|Index]]

# Item 1: Next.js 15.3

Source: [https://nextjs.org/blog/next-15-3](https://nextjs.org/blog/next-15-3)

Summary:
Next.js 15.3 introduces Turbopack for production builds (alpha), experimental Rspack support, new client instrumentation and navigation hooks, and TypeScript plugin improvements. Turbopack aims to significantly speed up builds, with benchmarks showing notable improvements over Webpack as core count increases. The release also adds hooks for early client-side monitoring and more granular navigation control, plus a new configuration structure for Turbopack. Rspack support is community-driven and offers an alternative for those needing Webpack compatibility.

Key takeaways:
- Turbopack for builds is in alpha; not recommended for mission-critical production yet, but shows strong performance gains.
- Rspack plugin offers experimental, near-Webpack-compatible bundling for Next.js users.
- New `instrumentation-client.js` file enables early client-side analytics and monitoring.
- Navigation hooks (`onNavigate`, `useLinkStatus`) provide fine-grained routing and loading state control.
- Turbopack config moves to a top-level key in `next.config.ts`; old config remains temporarily supported.

Recommendation:
Read fully (especially if you use Next.js in production or want to evaluate Turbopack/Rspack, or need advanced navigation/instrumentation features)

Why it matters:
especially if you use Next.js in production or want to evaluate Turbopack/Rspack, or need advanced navigation/instrumentation features

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
