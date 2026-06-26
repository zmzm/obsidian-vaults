---
type: twir-item
issue: 282
item: 5
item_type: item
date: 2026-05-20
source: https://saschb2b.com/blog/flight-protocol-dos
tags:
  - "DoS"
  - "Security"
  - "Expo"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-05-20-TWIR-282|Index]]

# Item 5: The Flight Protocol Made Your DoS My Problem

Source: [https://saschb2b.com/blog/flight-protocol-dos](https://saschb2b.com/blog/flight-protocol-dos)

Summary:
This article discusses CVE-2026-23870, a high-severity denial-of-service vulnerability in React’s Flight protocol deserializer, allowing a single malformed HTTP request to pin Node.js processes. The author explains how the protocol’s lack of strict structural validation made frameworks vulnerable, and emphasizes that the boundary between client and server is a true network boundary, not just an implementation detail. Guidance is provided for identifying and patching affected applications.

Key takeaways:
- CVE-2026-23870 enables unauthenticated DoS via malformed Flight payloads; affects all major Next.js App Router versions and react-server-dom-* packages.
- The underlying issue is insufficient validation in the Flight protocol parser, exposing server internals to external requests.
- Immediate upgrades are required; audit and patch instructions are provided.
- The incident underscores the need to treat framework boundaries as security boundaries.

Recommendation:
Read fully (critical for anyone deploying React Server Components or Next.js App Router)

Why it matters:
critical for anyone deploying React Server Components or Next.js App Router

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
