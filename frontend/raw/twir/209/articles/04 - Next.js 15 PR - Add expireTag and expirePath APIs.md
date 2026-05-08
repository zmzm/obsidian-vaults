---
type: twir-item
issue: 209
item: 4
item_type: item
date: 2024-11-13
source: https://github.com/vercel/next.js/pull/72485
tags:
  - "Nextjs"
  - "15"
  - "PR"
  - "APIs"
  - "TS"
status: auto
quality: keep
---

[[2024-11-13-TWIR-209|Index]]

# Item 4: Next.js 15 PR - Add expireTag and expirePath APIs

Source: [https://github.com/vercel/next.js/pull/72485](https://github.com/vercel/next.js/pull/72485)

Summary:
This PR introduces expireTag() and expirePath() APIs to Next.js, replacing the older revalidateTag and revalidatePath methods, which are now deprecated. The new APIs clarify the cache invalidation process by marking entries as expired, ensuring fresh data is generated on the next request. expireTag can now accept multiple tags, aligning with the new unstable_cacheTag API.

Key takeaways:
- expireTag and expirePath replace and deprecate revalidateTag and revalidatePath.
- expireTag supports multiple tags as arguments.
- The new naming clarifies that affected cache entries are expired and will not be used on subsequent requests.
- Aims to reduce confusion and improve cache invalidation semantics in Next.js.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
