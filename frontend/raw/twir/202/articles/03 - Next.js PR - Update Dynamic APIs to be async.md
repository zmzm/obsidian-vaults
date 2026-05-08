---
type: twir-item
issue: 202
item: 3
item_type: item
date: 2024-09-25
source: https://github.com/vercel/next.js/pull/68812
tags:
  - "Nextjs"
  - "PR"
  - "APIs"
status: auto
quality: keep
---

[[2024-09-25-TWIR-202|Index]]

# Item 3: Next.js PR - Update Dynamic APIs to be async

Source: [https://github.com/vercel/next.js/pull/68812](https://github.com/vercel/next.js/pull/68812)

Summary:
This PR migrates several Next.js dynamic APIs (cookies, headers, draftMode, searchParams, params) to async, enabling new rendering patterns and future features like partial prerendering. Synchronous access is temporarily supported for migration, with TypeScript types updated to enforce Promise-based usage. The change is breaking but includes codemods and backward compatibility to ease adoption.

Key takeaways:
- Dynamic APIs now return Promises, aligning with future rendering models.
- Synchronous access is deprecated but temporarily available for migration.
- TypeScript types enforce Promise-based usage, improving correctness.
- Enables advanced rendering strategies (e.g., partial prerendering) in Next.js.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
