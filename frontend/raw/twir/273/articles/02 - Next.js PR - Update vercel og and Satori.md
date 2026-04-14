---
type: twir-item
issue: 273
item: 2
item_type: item
date: 2026-03-18
source: https://github.com/vercel/next.js/pull/90933
tags:
  - "Nextjs"
  - "PR"
status: auto
---

[[2026-03-18-TWIR-273|Index]]

# Item 2: Next.js PR - Update vercel/og and Satori

Source: [https://github.com/vercel/next.js/pull/90933](https://github.com/vercel/next.js/pull/90933)

Summary:
This Next.js pull request updates the @vercel/og and Satori packages, bringing significant performance and feature improvements to image generation and layout handling. Highlights include 2–20x faster image responses, better CSS/SVG support, a new layout engine, and a font change from Noto Sans to Geist Sans. The update also addresses test and type resolution issues and includes regression tracking for performance metrics.

Key takeaways:
- Major speedup for image generation (ImageResponse API) using Sharp and optimized Satori core.
- Enhanced CSS/SVG features: CSS variables, object-fit, background size, and more.
- New layout engine with improved support for box-sizing, display: contents, and absolute positioning.
- Font default switched to Geist Sans; some test and type compatibility issues noted.

Recommendation: Read fully (for teams using Next.js image generation or interested in deep technical details)
