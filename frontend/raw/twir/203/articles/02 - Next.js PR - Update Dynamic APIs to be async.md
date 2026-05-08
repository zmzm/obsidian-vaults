---
type: twir-item
issue: 203
item: 2
item_type: item
date: 2024-10-01
source: https://github.com/vercel/next.js/pull/68812
tags:
  - "Nextjs"
  - "PR"
  - "APIs"
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 2: Next.js PR - Update Dynamic APIs to be async

Source: [https://github.com/vercel/next.js/pull/68812](https://github.com/vercel/next.js/pull/68812)

Summary:
Next.js is updating its dynamic APIs (cookies, headers, draftMode, searchParams, params) to be asynchronous, returning Promises instead of synchronous values. This change enables advanced rendering strategies like partial prerendering and dynamic IO, but is a breaking change requiring codemods and TypeScript updates for migration. Backward compatibility is maintained temporarily, with dev warnings for legacy usage.

Key takeaways:
- Dynamic APIs (cookies, headers, etc.) now return Promises; sync access is deprecated but temporarily supported.
- Migration path includes codemods, TypeScript type updates, and backward compatibility shims.
- Enables new rendering patterns (e.g., partial prerendering, dynamic IO).
- Future plans include stricter type enforcement and moving toward standard types like URLSearchParams.

Recommendation:
Read fully (if you use or maintain Next.js apps that rely on these APIs; migration details are important)

Why it matters:
if you use or maintain Next.js apps that rely on these APIs; migration details are important

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
