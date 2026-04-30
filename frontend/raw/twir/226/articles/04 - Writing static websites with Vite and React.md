---
type: twir-item
issue: 226
item: 5
item_type: item
date: 2025-03-19
source: https://blog.carlosn.com.br/post/writing-static-websites-with-vite-and-react/
tags:
  - "Perf"
status: auto
quality: keep
---

[[2025-03-19-TWIR-226|Index]]

# Item 5: Writing static websites with Vite and React

Source: [https://blog.carlosn.com.br/post/writing-static-websites-with-vite-and-react/](https://blog.carlosn.com.br/post/writing-static-websites-with-vite-and-react/)

Summary:
The post introduces vite-ssg-react, a tool for building static websites using React and Vite, where each JSX file renders directly to HTML without a router abstraction. The approach leverages SSR during development for fast feedback and outputs static HTML/CSS/JS for production, with no client-side React runtime or hydration. The author discusses the benefits (SEO, performance, code reuse) and current limitations, and outlines ideas for future improvements.

Key takeaways:
- vite-ssg-react enables static site generation with React, outputting pure HTML/JS/CSS.
- No client-side React runtime; components are used as pure functions for HTML generation.
- SSR is used in development for fast reloads; production builds are static and SEO-friendly.
- Limitations include lack of React hooks and incomplete ecosystem support; project is experimental.

Recommendation:
Summary sufficient (read full post if interested in static site generation with React/Vite)

Why it matters:
read full post if interested in static site generation with React/Vite

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
