---
type: twir-item
issue: 246
item: 3
item_type: item
date: 2025-08-20
source: https://aurorascharff.no/posts/server-client-component-composition-in-practice/
tags:
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-08-20-TWIR-246|Index]]

# Item 3: Server and client component composition in practice

Source: [https://aurorascharff.no/posts/server-client-component-composition-in-practice/](https://aurorascharff.no/posts/server-client-component-composition-in-practice/)

Summary:
The post explores best practices for composing React Server Components (RSCs) with client components, emphasizing how to retain server-side benefits while enabling client-side interactivity. It demonstrates the anti-pattern of converting server components to client components for simple UI state, and instead recommends wrapping server components with client wrappers for interactivity. Several practical examples are provided, such as motion wrappers and "Show More" toggles, to illustrate how to keep data fetching on the server and UI state on the client.

Key takeaways:
- Avoid converting server components to client components just to add interactivity; use client wrappers instead.
- Keeping data fetching on the server reduces client bundle size and improves performance.
- The composition pattern keeps responsibilities clear and components reusable.
- Practical examples show how to apply this pattern for animations, toggles, and more.

Recommendation:
Read fully (especially for teams adopting RSCs or optimizing for performance and maintainability)

Why it matters:
especially for teams adopting RSCs or optimizing for performance and maintainability

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
