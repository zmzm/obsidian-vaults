---
type: twir-item
issue: 193
item: 4
item_type: item
date: 2024-07-24
source: https://github.com/vercel/next.js/pull/68102
tags:
  - "nextform"
  - "Nextjs"
  - "PR"
  - "ES"
status: auto
quality: keep
---

[[2024-07-24-TWIR-193|Index]]

# Item 4: Next.js PR - next/form

Source: [https://github.com/vercel/next.js/pull/68102](https://github.com/vercel/next.js/pull/68102)

Summary:
A new <Form> component is being introduced to Next.js, integrating form submissions with the Next.js router. It supports both GET (URL navigation) and POST (function action) modes, with progressive enhancement and prefetching capabilities for GET. The component restricts certain native form props to maintain consistency and offers partial support for submitter overrides, while matching browser behavior for unsupported cases.

Key takeaways:
- <Form> integrates tightly with Next.js routing, supporting both GET and POST actions.
- Prefetching and client navigation are built-in for GET forms, enhancing user experience.
- Some form props are intentionally restricted for consistency and to avoid conflicts.
- Submitter-specific props can override defaults, but may fall back to native browser behavior.

Recommendation:
Read fully (for those using or migrating to Next.js forms)

Why it matters:
for those using or migrating to Next.js forms

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
