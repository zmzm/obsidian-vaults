---
type: twir-item
issue: 234
item: 3
item_type: item
date: 2025-05-14
source: https://github.com/TanStack/query/discussions/9135
tags:
  - "RFC"
status: auto
quality: keep
---

[[2025-05-14-TWIR-234|Index]]

# Item 3: React Query RFC - Unified Imperative Query Methods

Source: [https://github.com/TanStack/query/discussions/9135](https://github.com/TanStack/query/discussions/9135)

Summary:
This RFC proposes unifying the imperative query methods in React Query, which currently include fetchQuery, prefetchQuery, and ensureQueryData (plus their infinite variants). The discussion highlights confusion caused by overlapping APIs, inconsistent naming, and unclear usage recommendations. The goal is to streamline the API surface, reduce developer confusion, and clarify the intended use cases for each method.

Key takeaways:
- Current imperative APIs are redundant and confusing (fetchQuery, prefetchQuery, ensureQueryData).
- Naming does not always reflect behavior (e.g., fetchQuery may not fetch, prefetchQuery may refetch).
- Developers are unsure which method to use in different scenarios (SSR, route loaders, etc.).
- The RFC seeks feedback on consolidating and clarifying these APIs.

Recommendation:
Read fully (read fully if you rely heavily on React Query’s imperative APIs or want to contribute feedback)

Why it matters:
read fully if you rely heavily on React Query’s imperative APIs or want to contribute feedback

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
