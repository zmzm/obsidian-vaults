---
type: twir-item
issue: 226
item: 3
item_type: item
date: 2025-03-19
source: https://www.openstatus.dev/blog/live-mode-infinite-query
tags:
  - "TanStack"
status: auto
quality: keep
---

[[2025-03-19-TWIR-226|Index]]

# Item 3: Live Mode

Source: [https://www.openstatus.dev/blog/live-mode-infinite-query](https://www.openstatus.dev/blog/live-mode-infinite-query)

Summary:
This article provides a practical guide to implementing live data updates with TanStack’s useInfiniteQuery, focusing on cursor-based pagination for both loading older data and fetching new data in real-time (“live mode”). It details the required API structure, handling of timestamp boundaries to avoid data loss, and client-side integration using React Query. The post also warns against using OFFSET-based pagination in frequently updated datasets.

Key takeaways:
- Demonstrates live data fetching (prepend new data) and traditional pagination (append older data) with useInfiniteQuery.
- API should return data pages, nextCursor, and prevCursor for robust navigation.
- Careful handling of timestamp boundaries is crucial to avoid missing or duplicating data.
- OFFSET-based pagination is discouraged for dynamic datasets due to shifting data.

Recommendation:
Read fully (for anyone implementing real-time/infinite data loading in React)

Why it matters:
for anyone implementing real-time/infinite data loading in React

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
