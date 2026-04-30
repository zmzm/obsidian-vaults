---
type: twir-item
issue: 234
item: 2
item_type: item
date: 2025-05-14
source: https://github.com/facebook/react/pull/33152
tags:
  - "Vite"
  - "PR"
  - "RSC"
  - "ServerComponents"
status: auto
quality: keep
---

[[2025-05-14-TWIR-234|Index]]

# Item 2: React PR - Integrate React RSC with Vite

Source: [https://github.com/facebook/react/pull/33152](https://github.com/facebook/react/pull/33152)

Summary:
This PR introduces the react-server-dom-vite package, aiming to enable React Server Components (RSC) support in Vite-based projects. It addresses Vite’s ESM-based module system, leverages Vite’s modulepreload for chunk loading, and provides new APIs for module preloading and caching. The PR also discusses challenges with supporting "use client" in node_modules during development and outlines plans for further framework-agnostic RSC tooling.

Key takeaways:
- Enables RSC with Vite, handling ESM async loading and chunk preloading.
- Adds setPreloadModule API for custom module loading logic.
- Removes unnecessary bundler config and chunk encoding in RSC payloads.
- Highlights current limitations with "use client" in node_modules and ongoing workarounds.

Recommendation:
Read fully (for those integrating RSC with Vite or interested in bundler internals)

Why it matters:
for those integrating RSC with Vite or interested in bundler internals

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
