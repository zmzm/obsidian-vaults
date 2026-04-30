---
type: twir-item
issue: 227
item: 2
item_type: item
date: 2025-03-26
source: https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2025-03-26-TWIR-227|Index]]

# Item 2: Next.js and the corrupt middleware: the authorizing artifact

Source: [https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware](https://zhero-web-sec.github.io/research-and-things/nextjs-and-the-corrupt-middleware)

Summary:
This in-depth technical write-up by the vulnerability reporters explains how the Next.js middleware bypass was discovered and exploited. It details the mechanics of the `x-middleware-subrequest` header, how its value could be guessed based on middleware placement, and how this allowed attackers to skip middleware logic—including authentication and authorization checks—across various Next.js versions. The article also discusses the evolution of middleware conventions and the broad scope of affected versions.

Key takeaways:
- Attackers could bypass middleware by supplying a crafted `x-middleware-subrequest` header, with the value derived from middleware file paths.
- The vulnerability affected all versions from 11.1.4 onward, not just legacy versions.
- Middleware execution order and naming conventions played a key role in exploitability.
- The write-up provides practical examples and clarifies the exploit's impact on route protection.

Recommendation:
Read fully (essential for understanding the technical root cause and exploitability)

Why it matters:
essential for understanding the technical root cause and exploitability

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
