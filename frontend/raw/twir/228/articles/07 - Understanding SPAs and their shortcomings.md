---
type: twir-item
issue: 228
item: 9
item_type: item
date: 2025-04-02
source: https://reacttraining.com/blog/problems-you-face-with-spas
tags:
  - "SPAs"
status: auto
quality: keep
---

[[2025-04-02-TWIR-228|Index]]

# Item 9: Understanding SPAs and their shortcomings

Source: [https://reacttraining.com/blog/problems-you-face-with-spas](https://reacttraining.com/blog/problems-you-face-with-spas)

Summary:
This post explains the classic and modern definitions of SPAs, focusing on their technical implementation (client-side rendering, large bundles, serial requests) and scaling issues. It highlights problems with code-splitting and lazy loading, particularly around data-fetching, and recommends using frameworks with SSR and loaders to avoid common SPA pitfalls.

Key takeaways:
- SPAs load all JS upfront or use code-splitting, leading to serial requests and slower navigation/data-fetching.
- Data-fetching inside components exacerbates performance issues with code-splitting.
- Frameworks (Next.js, React Router Framework) provide SSR and better data-loading patterns, mitigating SPA downsides.
- Using loaders for data-fetching outside components is the recommended approach.

Recommendation:
Summary sufficient (read full post for in-depth SPA vs. framework comparison)

Why it matters:
read full post for in-depth SPA vs. framework comparison

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
