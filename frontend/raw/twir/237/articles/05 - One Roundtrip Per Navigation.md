---
type: twir-item
issue: 237
item: 5
item_type: item
date: 2025-06-04
source: https://overreacted.io/one-roundtrip-per-navigation/
tags:
status: auto
quality: keep
---

[[2025-06-04-TWIR-237|Index]]

# Item 5: One Roundtrip Per Navigation

Source: [https://overreacted.io/one-roundtrip-per-navigation/](https://overreacted.io/one-roundtrip-per-navigation/)

Summary:
This article examines the evolution from server-rendered HTML (single roundtrip for navigation and data) to client-driven JSON APIs (multiple fetches per navigation), highlighting inefficiencies and the tension between encapsulation and performance. It argues for approaches that restore single roundtrip data loading while preserving component-level data colocation, referencing modern frameworks and patterns.

Key takeaways:
- Server-rendered apps naturally batch data and UI in a single request, while client-driven apps often require multiple fetches.
- Colocating data fetching in components is desirable for maintainability but can lead to inefficient network usage.
- Modern solutions aim to reconcile component encapsulation with efficient, batched data loading.

Recommendation:
Read fully (especially for those architecting data fetching in React apps)

Why it matters:
especially for those architecting data fetching in React apps

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
