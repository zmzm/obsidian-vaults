---
type: twir-item
issue: 204
item: 7
item_type: item
date: 2024-10-09
source: https://codelynx.dev/posts/how-work-server-actions
tags:
  - "NextJS"
  - "Nextjs"
  - "Bun"
status: auto
quality: keep
---

[[2024-10-09-TWIR-204|Index]]

# Item 7: How Do Server Actions Work in NextJS?

Source: [https://codelynx.dev/posts/how-work-server-actions](https://codelynx.dev/posts/how-work-server-actions)

Summary:
This technical deep dive demystifies how Next.js implements server actions, tracing the flow from client-side invocation to backend execution. The article explains the bundling of server actions, unique action IDs, the role of createServerReference, and how requests are dispatched and resolved through reducers and fetch calls. It clarifies that server actions are not "magic" but a coordinated system of client-server communication, routing, and state management.

Key takeaways:
- Server actions are referenced by unique IDs and invoked via client-side proxies that dispatch requests to the server.
- Next.js bundles server actions into the client bundle, enabling transparent invocation from the UI.
- The system uses fetch with custom headers to route and execute the correct server action on the backend.
- The process supports data revalidation, redirection, and state updates, all handled through reducers and promises.

Recommendation:
Read fully (for a clear, step-by-step understanding of Next.js server action internals)

Why it matters:
for a clear, step-by-step understanding of Next.js server action internals

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Next.js]]
