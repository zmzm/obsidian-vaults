---
type: twir-item
issue: 289
item: 3
item_type: item
date: 2026-07-08
source: https://performance.dev/chatgpt
tags:
  - "ChatGPT"
  - "OpenAI"
  - "TanStackQuery"
status: auto
quality: keep
---

[[2026-07-08-TWIR-289|Index]]

# Item 3: Reverse Engineering ChatGPT Web: How OpenAI Built for a Billion Users

Source: [https://performance.dev/chatgpt](https://performance.dev/chatgpt)

Summary:
This article reverse-engineers the architecture of ChatGPT Web, focusing on its evolution from Next.js (Pages Router) to Remix, and finally to React Router 7 in framework mode. The analysis highlights OpenAI’s preference for off-the-shelf libraries (React 19, React Router, TanStack Query, Tailwind, etc.) and a strong emphasis on server-side rendering for fast first paint and accessibility. The migration story reveals a pragmatic approach, using Remix and then React Router mainly for routing and data loading, while relying on TanStack Query for client-side state.

Key takeaways:
- ChatGPT Web migrated from Next.js to Remix, then to React Router 7, prioritizing flexibility and performance.
- Uses standard libraries for UI, state, and styling; avoids proprietary solutions.
- Emphasizes server-side rendering and streaming for fast, accessible user experience.
- Data loading is handled by TanStack Query rather than framework-specific loaders.

Recommendation:
Read fully (for insights into large-scale React app architecture and migration strategies)

Why it matters:
for insights into large-scale React app architecture and migration strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
