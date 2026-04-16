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
  - "Bun"
status: auto
quality: keep
---

[[2026-03-18-TWIR-273|Index]]

# Item 2: Next.js PR - Update vercel/og and Satori

Source: [https://github.com/vercel/next.js/pull/90933](https://github.com/vercel/next.js/pull/90933)

Summary:
Next.js has updated its @vercel/og and satori dependencies, bringing major improvements in image generation speed, CSS/SVG support, and layout engine capabilities. The update introduces up to 20x faster image responses, better CSS features, and a switch from Noto Sans to Geist Sans as the default font. Some regressions and breaking changes (e.g., removed exports) are noted, and there are ongoing discussions about bundled versions and test adjustments.

Key takeaways:
- ImageResponse API is now 2–20x faster due to Sharp integration and Satori optimizations.
- Expanded CSS/SVG support: CSS variables, object-position, text-indent, object-fit, background size, and more.
- Layout engine improvements: support for box-sizing, display: contents, position: static/absolute, align-content, and percentage gap values.
- Default font changed to Geist Sans; some breaking changes for consumers of internal APIs.

Recommendation:
Read fully (for anyone using Next.js image generation or custom rendering pipelines)

Why it matters:
for anyone using Next.js image generation or custom rendering pipelines

Content:
# Update `@vercel/og` and `satori` vendors by shuding · Pull Request #90933 · vercel/next.js · GitHub

```
The new `@vercel/og` and `satori` include many improvements:
- 2~20x faster image generation (`ImageResponse` API) by using Sharp for
rasterization, and optimized Satori core
- Better CSS/SVG coverage:
  - vercel/satori#736
  - vercel/satori#734
  - vercel/satori#733
  - vercel/satori#732
  - vercel/satori#728
  - vercel/satori#724
  - vercel/satori#717
  - vercel/satori#718
  - vercel/satori#719
- Updated layout engine (vercel/satori#689):
  - Support for `box-sizing`
  - Support for `display: contents`
  - Support for `position: static`
  - Support for `align-content: space-evenly`
  - Better support for `position: absolute`
  - Support for percentage values for `gap`
- Noto Sans → Geist Sans
```
