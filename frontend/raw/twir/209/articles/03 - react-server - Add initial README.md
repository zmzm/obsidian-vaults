---
type: twir-item
issue: 209
item: 3
item_type: item
date: 2024-11-13
source: https://github.com/facebook/react/tree/main/packages/react-server
tags:
  - "README"
  - "TS"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-11-13-TWIR-209|Index]]

# Item 3: react-server - Add initial README

Source: [https://github.com/facebook/react/tree/main/packages/react-server](https://github.com/facebook/react/tree/main/packages/react-server)

Summary:
The new README for the experimental react-server package explains its purpose: enabling custom React streaming server renderers. It covers the two main implementations, Fizz (for SSR) and Flight (for React Server Components), and describes their usage, including code samples for rendering and handling client/server references. The document also discusses prerendering, error handling, and the differences between real-time and ahead-of-time rendering.

Key takeaways:
- react-server is experimental and not as stable as core React packages.
- Fizz handles SSR by streaming HTML, while Flight enables React Server Components that never run on the client.
- The package supports advanced serialization (including Promises, Iterators, etc.) and both client and server references.
- Prerendering is supported with distinct error handling semantics; errors during prerendering can be omitted or trigger dynamic recovery.

Recommendation:
Read fully (for anyone building custom SSR/RSC solutions or frameworks)

Why it matters:
for anyone building custom SSR/RSC solutions or frameworks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
