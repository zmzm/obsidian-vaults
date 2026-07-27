---
type: twir-item
issue: 289
item: 2
item_type: item
date: 2026-07-08
source: https://github.com/vercel/next.js/discussions/95514
tags:
  - "Nextjs"
  - "RFC"
  - "WebSocket"
  - "Nodejs"
status: auto
quality: keep
---

[[2026-07-08-TWIR-289|Index]]

# Item 2: Next.js RFC - First-class WebSocket support in App Router Route Handlers

Source: [https://github.com/vercel/next.js/discussions/95514](https://github.com/vercel/next.js/discussions/95514)

Summary:
This RFC proposes adding first-class WebSocket support to Next.js App Router Route Handlers via a new NextResponse.upgrade() API. The API allows route handlers to inspect requests, perform authentication, and conditionally accept or reject WebSocket connections, all while integrating with Next.js routing, headers, cookies, and error handling. The implementation uses CrossWS for peer management and message handling, with lifecycle hooks for open, message, close, and error events. The goal is to eliminate the need for custom Node.js servers and unify the approach across self-hosted and adapter deployments.

Key takeaways:
- Introduces NextResponse.upgrade() for handling WebSocket upgrades in route handlers.
- Enables request inspection, authentication, and conditional acceptance within handlers.
- Uses CrossWS for peer tracking, pub/sub, and message APIs.
- Aims for consistent API across self-hosted and adapter deployments; does not support Edge runtime or Pages Router.

Recommendation:
Read fully (if using or planning to use WebSockets with Next.js App Router)

Why it matters:
if using or planning to use WebSockets with Next.js App Router

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
