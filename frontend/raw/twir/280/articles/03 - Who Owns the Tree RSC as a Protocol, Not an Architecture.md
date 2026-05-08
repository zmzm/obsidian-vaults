---
type: twir-item
issue: 280
item: 3
item_type: item
date: 2026-05-06
source: https://tanstack.com/blog/who-owns-the-tree
tags:
  - "RSC"
  - "TanStack"
  - "Trees"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-05-06-TWIR-280|Index]]

# Item 3: Who Owns the Tree? RSC as a Protocol, Not an Architecture

Source: [https://tanstack.com/blog/who-owns-the-tree](https://tanstack.com/blog/who-owns-the-tree)

Summary:
Tanner Linsley discusses React Server Components (RSC) as a protocol for serializing and streaming UI, rather than a fixed architecture. He contrasts the traditional server-owned tree model (with 'use client' boundaries) with a client-owned model that can embed server-rendered fragments. TanStack Start supports both models, allowing flexible composition and bridging gaps in current framework capabilities.

Key takeaways:
- RSC is a protocol enabling both server-owned and client-owned tree composition.
- TanStack Start allows embedding server-rendered output in client-owned trees, not just the reverse.
- Both models can reach SPA or server-rendered extremes, but friction and defaults differ by framework.
- Composite Components in TanStack Start let clients fetch and cache server-rendered fragments for insertion anywhere in the client tree.

Recommendation:
Read fully (for those building with RSC or interested in advanced composition patterns)

Why it matters:
for those building with RSC or interested in advanced composition patterns

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
