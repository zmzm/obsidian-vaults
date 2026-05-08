---
type: twir-item
issue: 212
item: 5
item_type: item
date: 2024-12-04
source: https://kurtextrem.de/posts/improve-inp-react
tags:
  - "INP"
  - "Virtualization"
  - "ReactCompiler"
status: auto
quality: keep
---

[[2024-12-04-TWIR-212|Index]]

# Item 5: How To Improve INP: React

Source: [https://kurtextrem.de/posts/improve-inp-react](https://kurtextrem.de/posts/improve-inp-react)

Summary:
This in-depth article explores techniques to optimize Interaction-to-Next-Paint (INP) in React applications, focusing on concurrent rendering, hydration strategies, and event handling. It covers React 18 features like startTransition, useTransition, <Suspense>, and progressive hydration, along with practical tips for reducing main thread blocking and improving perceived responsiveness. The guide emphasizes granular Suspense boundaries, abortable transitions, and the use of virtualization and scheduler APIs to further enhance performance.

Key takeaways:
- Upgrading to React 18 and leveraging concurrent rendering APIs (startTransition, useTransition) is foundational for INP improvements.
- Granular <Suspense> boundaries and selective/progressive hydration reduce hydration costs and speed up user feedback.
- Use virtualization, abortable transitions, and defer non-critical work to minimize main thread blocking and redundant renders.
- Tools like React Compiler, react-scan, and Million Lint can help identify and fix performance bottlenecks.

Recommendation:
Read fully (highly actionable for React performance optimization, especially for apps with INP or Core Web Vitals concerns)

Why it matters:
highly actionable for React performance optimization, especially for apps with INP or Core Web Vitals concerns

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[React Compiler]]
