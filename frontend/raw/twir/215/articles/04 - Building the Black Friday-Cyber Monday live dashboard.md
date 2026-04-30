---
type: twir-item
issue: 215
item: 4
item_type: item
date: 2025-01-02
source: https://vercel.com/blog/building-the-black-friday-cyber-monday-live-dashboard
tags:
  - "Friday-Cyber"
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-01-02-TWIR-215|Index]]

# Item 4: Building the Black Friday-Cyber Monday live dashboard

Source: [https://vercel.com/blog/building-the-black-friday-cyber-monday-live-dashboard](https://vercel.com/blog/building-the-black-friday-cyber-monday-live-dashboard)

Summary:
This post details how Vercel built a real-time, data-heavy dashboard for Black Friday-Cyber Monday using Next.js and React Server Components. It covers backend optimizations (rolling window queries, Upstash KV for cumulative counts, ISR for caching), frontend techniques for smooth real-time visuals (rate-of-change animations, requestAnimationFrame), and accuracy/performance improvements. The architecture leverages RSCs for efficient data fetching and minimal client-side JavaScript.

Key takeaways:
- Backend uses rolling window queries and KV storage for efficient, scalable metrics aggregation.
- ISR (Incremental Static Regeneration) ensures data freshness with minimal database load.
- Frontend animates metric changes for a dynamic UX, adjusting rates for accuracy.
- React Server Components simplify data fetching and reduce client-side overhead.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
