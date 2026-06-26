---
type: twir-item
issue: 284
item: 4
item_type: item
date: 2026-06-03
source: https://performance.dev/the-conductor-rewrite
tags:
  - "TanStackQuery"
status: auto
quality: keep
---

[[2026-06-03-TWIR-284|Index]]

# Item 4: The Conductor Rewrite: What They Changed to Make It Fast

Source: [https://performance.dev/the-conductor-rewrite](https://performance.dev/the-conductor-rewrite)

Summary:
Conductor, a local-first React app wrapped in Tauri, underwent a major rewrite to double its performance. The team focused on eliminating network bottlenecks, leveraging a local SQLite database, and optimizing UI responsiveness. Their stack includes React 19, TanStack Router, TanStack Query, Zustand, and a range of performance-focused libraries. The article details the architectural choices, measurement strategies, and the impact of running locally with Tauri versus Electron.

Key takeaways:
- Local-first architecture (SQLite, no remote DB) eliminates network latency, improving perceived speed.
- Tauri is chosen over Electron for better cold start and UI performance, fitting their Rust-based backend.
- The stack leverages modern React, TanStack tools, and virtualization libraries for efficient rendering.
- Performance gains required precise measurement and iterative UI optimization after removing network delays.

Recommendation:
Read fully (for those interested in performance optimization, local-first apps, or modern React desktop stacks)

Why it matters:
for those interested in performance optimization, local-first apps, or modern React desktop stacks

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[TanStack Query]]
