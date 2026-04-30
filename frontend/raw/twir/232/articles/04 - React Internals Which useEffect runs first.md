---
type: twir-item
issue: 232
item: 7
item_type: item
date: 2025-04-30
source: https://frontendmasters.com/blog/react-internals-which-useeffect-runs-first/
tags:
status: auto
quality: keep
---

[[2025-04-30-TWIR-232|Index]]

# Item 7: React Internals: Which useEffect runs first?

Source: [https://frontendmasters.com/blog/react-internals-which-useeffect-runs-first/](https://frontendmasters.com/blog/react-internals-which-useeffect-runs-first/)

Summary:
This in-depth article explains the order in which useEffect hooks run in nested React components. It clarifies that while parent components render before children, child effects are committed before parent effects due to React’s fiber tree traversal during the commit phase. The post walks through the React render and commit phases, fiber architecture, and the traversal algorithm that determines effect order.

Key takeaways:
- useEffect in child components runs before parent effects, despite parents rendering first.
- The React fiber tree and its depth-first traversal explain this behavior.
- Understanding the render and commit phases helps debug and predict effect execution order.

Recommendation:
Read fully (for anyone interested in React internals, debugging, or advanced hooks usage)

Why it matters:
for anyone interested in React internals, debugging, or advanced hooks usage

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
