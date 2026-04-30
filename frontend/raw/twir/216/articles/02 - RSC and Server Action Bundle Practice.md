---
type: twir-item
issue: 216
item: 2
item_type: item
date: 2025-01-08
source: https://github.com/orgs/web-infra-dev/discussions/23
tags:
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-01-08-TWIR-216|Index]]

# Item 2: RSC and Server Action Bundle Practice

Source: [https://github.com/orgs/web-infra-dev/discussions/23](https://github.com/orgs/web-infra-dev/discussions/23)

Summary:
This discussion provides a detailed overview of how React Server Components (RSC) and Server Actions are bundled using webpack and Turbopack. It covers the distinction between client and server components, the role of directives like 'use client', and how bundlers identify, split, and reference client modules. The article walks through the rendering and hydration process, the creation of client references, and the mechanics of code splitting and manifest generation for efficient runtime loading.

Key takeaways:
- RSC introduces clear boundaries between client and server components, impacting bundler behavior.
- Bundlers must recognize directives and package.json exports to correctly split and reference code.
- Client components are replaced with references during server bundling, enabling runtime hydration.
- The integration process is complex and requires careful handling of module metadata and manifests.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
