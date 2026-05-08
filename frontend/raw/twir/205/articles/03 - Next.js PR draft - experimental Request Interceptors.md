---
type: twir-item
issue: 205
item: 3
item_type: item
date: 2024-10-16
source: https://github.com/vercel/next.js/pull/70961
tags:
  - "Nextjs"
  - "PR"
  - "Nodejs"
status: auto
quality: keep
---

[[2024-10-16-TWIR-205|Index]]

# Item 3: Next.js PR draft - experimental Request Interceptors

Source: [https://github.com/vercel/next.js/pull/70961](https://github.com/vercel/next.js/pull/70961)

Summary:
Next.js is proposing experimental Request Interceptors as a complement to Middleware, allowing code to run in the same process as the page or route handler, with full Node.js API access. Interceptors are defined per route segment and can be used for tasks like authentication, running before rendering or server actions. They address Middleware limitations (e.g., Edge-only, limited Node.js support) but come with trade-offs such as dynamic rendering opt-in and response header limitations.

Key takeaways:
- Request Interceptors run at the origin, enabling access to full Node.js APIs and per-route logic.
- Useful for authentication, logging, and pre-processing requests with more flexibility than Middleware.
- Interceptors delay rendering and must be efficient; they opt routes into dynamic rendering.
- Still experimental; API may change and Edge Runtime support is pending.

Recommendation:
Read fully (if building advanced Next.js apps or considering request lifecycle customization)

Why it matters:
if building advanced Next.js apps or considering request lifecycle customization

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
