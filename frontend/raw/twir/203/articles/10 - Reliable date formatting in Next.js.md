---
type: twir-item
issue: 203
item: 10
item_type: item
date: 2024-10-01
source: https://next-intl-docs.vercel.app/blog/date-formatting-nextjs
tags:
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 10: Reliable date formatting in Next.js

Source: [https://next-intl-docs.vercel.app/blog/date-formatting-nextjs](https://next-intl-docs.vercel.app/blog/date-formatting-nextjs)

Summary:
This post explores pitfalls of using new Date() in React components, especially in shared components that may render on both server and client. Using new Date() during render can cause hydration mismatches and violate functional purity. The recommended approach is to generate "now" in a Server Component and pass it as a prop, or use React’s cache() to ensure consistency across a render pass.

Key takeaways:
- Avoid using new Date() during render in shared/client components to prevent hydration mismatches.
- Server Components can safely generate and pass "now" as a prop.
- Use React’s cache() to ensure a consistent "now" value across a render pass.
- Consider revalidation strategies for statically rendered pages.

Recommendation:
Read fully (read fully if you handle time-sensitive rendering in Next.js/React)

Why it matters:
read fully if you handle time-sensitive rendering in Next.js/React

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
