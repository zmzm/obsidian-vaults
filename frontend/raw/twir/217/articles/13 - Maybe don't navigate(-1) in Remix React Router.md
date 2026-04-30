---
type: twir-item
issue: 217
item: 13
item_type: item
date: 2025-01-15
source: https://programmingarehard.com/2025/01/13/maybe-dont-navigate-1.html/
tags:
  - "ReactRouter"
  - "1"
status: auto
quality: keep
---

[[2025-01-15-TWIR-217|Index]]

# Item 13: Maybe don't navigate(-1) in Remix/React Router

Source: [https://programmingarehard.com/2025/01/13/maybe-dont-navigate-1.html/](https://programmingarehard.com/2025/01/13/maybe-dont-navigate-1.html/)

Summary:
The post warns against using navigate(-1) for "Back" links in Remix/React Router, as it manipulates the browser's global history stack and can navigate users out of your app. Instead, it recommends passing a "back" state via <Link> and handling navigation within app boundaries, providing reusable hooks for this pattern.

Key takeaways:
- navigate(-1) can send users outside your app, leading to poor UX.
- Prefer passing explicit "back" state via <Link> and handling navigation in-app.
- Custom hooks can encapsulate this logic for reuse.
- Pattern ensures "Back" links behave consistently within the app.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
