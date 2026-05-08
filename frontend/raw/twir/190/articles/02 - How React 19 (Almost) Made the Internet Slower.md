---
type: twir-item
issue: 190
item: 2
item_type: item
date: 2024-06-19
source: https://blog.codeminer42.com/how-react-19-almost-made-the-internet-slower/
tags:
  - "19"
  - "Suspense"
status: auto
quality: keep
---

[[2024-06-19-TWIR-190|Index]]

# Item 2: How React 19 (Almost) Made the Internet Slower

Source: [https://blog.codeminer42.com/how-react-19-almost-made-the-internet-slower/](https://blog.codeminer42.com/how-react-19-almost-made-the-internet-slower/)

Summary:
This post explains how a subtle change in React 19’s Suspense implementation could have degraded performance for many apps using parallel data fetching or lazy loading. It walks through the technical details, the rationale from the React team, and the developer experience implications, emphasizing the tension between performance best practices and ergonomic component/data colocation. The article also notes the React team’s decision to revert the change after community feedback.

Key takeaways:
- React 19 initially disabled parallel rendering of siblings in Suspense, causing sequential (waterfall) data fetching.
- The change was minimally documented and would have broken a widely used pattern for both data fetching and React.lazy.
- The rationale was to improve fallback rendering latency, but it conflicted with established DX and patterns.
- After significant community outcry, the React team decided to postpone the change.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
