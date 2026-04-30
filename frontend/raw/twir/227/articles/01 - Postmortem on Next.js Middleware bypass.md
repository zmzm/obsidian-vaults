---
type: twir-item
issue: 227
item: 1
item_type: featured
date: 2025-03-26
source: https://vercel.com/blog/postmortem-on-next-js-middleware-bypass
tags:
  - "Nextjs"
  - "EAS"
status: auto
quality: keep
---

[[2025-03-26-TWIR-227|Index]]

# Item 1: Postmortem on Next.js Middleware bypass

Source: [https://vercel.com/blog/postmortem-on-next-js-middleware-bypass](https://vercel.com/blog/postmortem-on-next-js-middleware-bypass)

Summary:
This postmortem details the discovery, investigation, and remediation of a critical vulnerability (CVE-2025-29927) in Next.js Middleware, which allowed bypassing middleware protections via an internal header. The timeline covers initial disclosure, triage delays, technical analysis of the vulnerability, patch releases, and communication improvements. The post highlights lessons learned, process changes, and the introduction of a Long Term Support (LTS) policy for Next.js. It also outlines next steps to improve security reporting, partner communication, and documentation of internal APIs.

Key takeaways:
- Vulnerability allowed bypassing middleware by manipulating the `x-middleware-subrequest` header, affecting self-hosted and some deployment scenarios.
- Vercel-hosted, Netlify, and Cloudflare deployments were not impacted due to architectural differences.
- Delays in triage and communication highlighted the need for better processes and clearer partner outreach.
- Next.js has published an LTS policy and is consolidating security reporting through GitHub.

Recommendation:
Read fully (especially if you operate or secure Next.js applications or infrastructure)

Why it matters:
especially if you operate or secure Next.js applications or infrastructure

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
