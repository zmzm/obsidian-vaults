---
type: twir-item
issue: 301
item: 7
item_type: item
date: 2026-10-14
source: https://mattrothenberg.com/notes/classname-considered-harmful/
tags:
  - "One"
status: auto
quality: keep
---

[[2026-10-14-TWIR-301|Index]]

# Item 7: className Considered Harmful

Source: [https://mattrothenberg.com/notes/classname-considered-harmful/](https://mattrothenberg.com/notes/classname-considered-harmful/)

Summary:
The article argues that allowing unrestricted className overrides in component libraries leads to maintenance issues, API surface sprawl, and accidental dependency on internal implementation details. It surveys strategies for limiting or tracking overrides (e.g., UNSAFE_className, lint rules), and advocates for explicit, trackable override mechanisms to balance flexibility and maintainability. The author shares practical experiences from Cloudflare’s design system.

Key takeaways:
- Unrestricted className usage can make component APIs fragile and hinder refactoring.
- Explicit override props (e.g., UNSAFE_className) and lint rules help manage and audit overrides.
- Override inventories can reveal emerging needs and inform design system evolution.
- Balancing flexibility and control is a people/process decision as much as a technical one.

Recommendation:
Read fully (read fully if you maintain a design system or component library)

Why it matters:
read fully if you maintain a design system or component library

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: 403 Client Error: Forbidden for url: https://mattrothenberg.com/notes/classname-considered-harmful/. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
