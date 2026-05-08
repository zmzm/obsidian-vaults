---
type: twir-item
issue: 212
item: 2
item_type: item
date: 2024-12-04
source: https://github.com/vercel/next.js/pull/73193
tags:
  - "Nextjs"
  - "PR"
  - "APIs"
status: auto
quality: keep
---

[[2024-12-04-TWIR-212|Index]]

# Item 2: Next.js PR - Undeprecate revalidate APIs and rename expire APIs

Source: [https://github.com/vercel/next.js/pull/73193](https://github.com/vercel/next.js/pull/73193)

Summary:
A Next.js pull request reverses the deprecation of revalidateTag and revalidatePath APIs, clarifying that they will remain supported. The new expireTag and expirePath APIs are introduced with an unstable_ prefix, signaling ongoing iteration and different semantics. This maintains existing revalidation workflows while allowing experimentation with new cache expiration APIs.

Key takeaways:
- revalidateTag and revalidatePath are no longer deprecated and will continue to be supported.
- expireTag and expirePath are introduced as unstable APIs for cache expiration, with potential future changes.
- The change avoids breaking existing code and clarifies the intended evolution of cache management in Next.js.

Recommendation:
Summary sufficient (read the PR if you rely on these APIs or need details on cache strategies)

Why it matters:
read the PR if you rely on these APIs or need details on cache strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
