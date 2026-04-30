---
type: twir-item
issue: 225
item: 4
item_type: item
date: 2025-03-12
source: https://sergiodxa.com/tutorials/create-a-per-request-singleton-with-react-router-middleware
tags:
  - "ReactRouter"
  - "Per-Request"
status: auto
quality: keep
---

[[2025-03-12-TWIR-225|Index]]

# Item 4: How to Create a Per-Request Singleton with React Router Middleware

Source: [https://sergiodxa.com/tutorials/create-a-per-request-singleton-with-react-router-middleware](https://sergiodxa.com/tutorials/create-a-per-request-singleton-with-react-router-middleware)

Summary:
This guide introduces a pattern for creating per-request singletons using React Router's middleware API. It provides a utility for instantiating a class once per request and sharing it across loaders or actions, which is useful for caching or batching. The article includes implementation details and usage examples.

Key takeaways:
- The pattern ensures a new instance per request, ideal for request-scoped caching or batching.
- Provided utility (createSingletonMiddleware) simplifies singleton setup and retrieval.
- Works by storing the instance in the middleware context.
- Not suitable for sharing instances across requests.

Recommendation:
Read fully (read fully if you need per-request singleton logic)

Why it matters:
read fully if you need per-request singleton logic

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
