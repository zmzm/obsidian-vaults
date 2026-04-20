---
type: twir-item
issue: 237
item: 7
item_type: item
date: 2025-06-04
source: https://overreacted.io/why-does-rsc-integrate-with-a-bundler/
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-06-04-TWIR-237|Index]]

# Item 7: Why Does RSC Integrate with a Bundler?

Source: [https://overreacted.io/why-does-rsc-integrate-with-a-bundler/](https://overreacted.io/why-does-rsc-integrate-with-a-bundler/)

Summary:
This article explains why React Server Components (RSC) require bundler integration, focusing on the need to serialize not just data but also code references for client components. It details how bundler bindings (for Parcel, Webpack, etc.) enable efficient module resolution and code splitting, allowing RSC to send references to client code that can be loaded and executed as needed.

Key takeaways:
- RSC serialization must reference client modules, not just data, to enable interactivity.
- Bundlers generate code chunks and teach React how to reference and load them on the client.
- The RSC API for serialization/deserialization is exposed via bundler-specific packages.

Recommendation:
Read fully (read fully for deep dives into RSC or bundler integration)

Why it matters:
read fully for deep dives into RSC or bundler integration

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
