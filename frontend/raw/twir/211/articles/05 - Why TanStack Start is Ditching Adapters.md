---
type: twir-item
issue: 211
item: 5
item_type: item
date: 2024-11-27
source: https://tanstack.com/blog/why-tanstack-start-is-ditching-adapters
tags:
  - "TanStack"
  - "Vite"
  - "Nitro"
status: auto
quality: keep
---

[[2024-11-27-TWIR-211|Index]]

# Item 5: Why TanStack Start is Ditching Adapters

Source: [https://tanstack.com/blog/why-tanstack-start-is-ditching-adapters](https://tanstack.com/blog/why-tanstack-start-is-ditching-adapters)

Summary:
TanStack Start, a new full-stack framework, initially considered writing adapters for each hosting platform but found this approach unsustainable. Instead, it leverages Nitro (with Vite and H3), which abstracts away platform-specific deployment concerns, making TanStack Start "adapter-less." This enables seamless deployment to platforms like Vercel and simplifies integration of advanced features.

Key takeaways:
- Adapters for every platform are hard to maintain; Nitro abstracts deployment targets.
- TanStack Start configures deployment via a simple preset option.
- Nitro, H3, and Vite provide out-of-the-box support for many hosting features (SSR, edge, env vars, streaming).
- Middleware and platform integration (e.g., skew protection) are handled via framework primitives.

Recommendation:
Read fully (especially if interested in modern full-stack React frameworks or deployment strategies)

Why it matters:
especially if interested in modern full-stack React frameworks or deployment strategies

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
