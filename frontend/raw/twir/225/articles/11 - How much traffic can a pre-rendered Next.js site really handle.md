---
type: twir-item
issue: 225
item: 12
item_type: item
date: 2025-03-12
source: https://martijnhols.nl/blog/how-much-traffic-can-a-pre-rendered-nextjs-site-handle
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2025-03-12-TWIR-225|Index]]

# Item 12: How much traffic can a pre-rendered Next.js site really handle?

Source: [https://martijnhols.nl/blog/how-much-traffic-can-a-pre-rendered-nextjs-site-handle](https://martijnhols.nl/blog/how-much-traffic-can-a-pre-rendered-nextjs-site-handle)

Summary:
This article investigates the real-world scalability of pre-rendered Next.js sites by running load tests and analyzing server performance. The author finds that a single VPS can handle fewer concurrent users than expected due to the high number of requests per visit, discusses the impact of scaling and caching, and weighs the pros and cons of using services like Cloudflare or Vercel.

Key takeaways:
- Pre-rendered Next.js sites can be bottlenecked by the number of requests per page load.
- Scaling up containers and using caching/CDNs can help, but privacy or cost concerns may limit options.
- Real-world traffic spikes (e.g., from Hacker News) can quickly stress a typical VPS setup.
- Trade-offs exist between developer experience, performance, and infrastructure choices.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
