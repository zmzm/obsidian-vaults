---
type: twir-item
issue: 204
item: 5
item_type: item
date: 2024-10-09
source: https://bobaekang.com/blog/serverless-servers-and-the-challenge-of-new-react-architecture/
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2024-10-09-TWIR-204|Index]]

# Item 5: Serverless servers and the challenge of new React architecture

Source: [https://bobaekang.com/blog/serverless-servers-and-the-challenge-of-new-react-architecture/](https://bobaekang.com/blog/serverless-servers-and-the-challenge-of-new-react-architecture/)

Summary:
Vercel's new "serverless servers" feature enables in-function concurrency, allowing a single Node.js function instance to handle multiple concurrent requests, improving efficiency and reducing compute costs. The article connects this infrastructure evolution to React's full-stack architecture, where increased server-side rendering and data fetching amplify the need for scalable, efficient backend infrastructure. While in-function concurrency mainly benefits slow async operations (not synchronous rendering), the broader point is that modern React architectures require tight integration between framework and deployment infrastructure for optimal performance and cost.

Key takeaways:
- In-function concurrency allows Vercel Functions to handle multiple requests per instance, reducing costs for async-heavy workloads.
- React’s full-stack/server-centric patterns increase server load and async operations, making infrastructure efficiency critical.
- Next.js’s App Router and granular routing amplify server demands, highlighting the importance of deployment platform capabilities.
- Infrastructure and framework alignment is increasingly necessary for scalable, cost-effective React deployments.

Recommendation:
Read fully (for context on how infrastructure changes impact modern React/Next.js architectures)

Why it matters:
for context on how infrastructure changes impact modern React/Next.js architectures

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
