---
type: twir-item
issue: 283
item: 6
item_type: item
date: 2026-05-27
source: https://formisch.dev/blog/one-core-six-frameworks/
tags:
status: auto
quality: keep
---

[[2026-05-27-TWIR-283|Index]]

# Item 6: One core, six frameworks, zero runtime abstraction

Source: [https://formisch.dev/blog/one-core-six-frameworks/](https://formisch.dev/blog/one-core-six-frameworks/)

Summary:
This post introduces Formisch, a schema-first form library that supports six frameworks by swapping in native reactivity primitives at build time, rather than using a runtime abstraction layer. The approach allows for framework-native integration, smaller bundles, and type safety, benefiting all supported frameworks simultaneously.

Key takeaways:
- Formisch uses each framework's native signal/reactivity system, avoiding runtime adapters and reducing bundle size.
- The core library is framework-agnostic at the source level, with build-time selection of the appropriate adapter.
- This design enables better integration with framework features (batching, scheduling) and easier tree-shaking.
- Type safety is maintained from a single schema source, and improvements benefit all frameworks.

Recommendation:
Read fully (especially for those interested in cross-framework libraries or advanced form handling)

Why it matters:
especially for those interested in cross-framework libraries or advanced form handling

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
