---
type: twir-item
issue: 198
item: 15
item_type: item
date: 2024-08-28
source: https://playfulprogramming.com/posts/why-is-css-in-js-slow
tags:
  - "CSS-in-JS"
status: auto
quality: keep
---

[[2024-08-28-TWIR-198|Index]]

# Item 15: Why is CSS-in-JS slow?

Source: [https://playfulprogramming.com/posts/why-is-css-in-js-slow](https://playfulprogramming.com/posts/why-is-css-in-js-slow)

Summary:
The article explains the inherent performance drawbacks of runtime CSS-in-JS solutions compared to static CSS. It details how CSS parsing and injection timing can cause FOUC (Flash of Unstyled Content) and why compiled CSS-in-JS tools (like PandaCSS, StyleX) avoid these issues by generating CSS at build time.

Key takeaways:
- Runtime CSS-in-JS introduces extra parsing and injection steps, delaying styling.
- Can cause FOUC and performance bottlenecks, especially in large apps.
- Compiled CSS-in-JS sidesteps these issues by generating static CSS.
- Understanding the rendering waterfall is key to diagnosing style performance.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
