---
type: twir-item
issue: 268
item: 5
item_type: item
date: 2026-02-11
source: https://www.sanity.io/blog/the-logo-soup-problem
tags:
  - "LogoSoup"
status: auto
---

[[2026-02-11-TWIR-268|Index]]

# Item 5: The logo soup problem (and how to solve it)

Source: [https://www.sanity.io/blog/the-logo-soup-problem](https://www.sanity.io/blog/the-logo-soup-problem)

Summary:
The article discusses the challenge of displaying a visually consistent row of partner logos, given their wildly varying aspect ratios, densities, and padding. It introduces the Proportional Image Normalization Formula (PINF) to scale logos in a way that balances width and height, and describes further refinements like density compensation and cropping to content. The LogoSoup React library is presented as a solution that automates these adjustments, analyzing each logo’s pixel data and applying normalization for a polished, balanced display.

Key takeaways:
- Simple width/height normalization fails for logos with diverse aspect ratios and densities.
- PINF formula provides a mathematical approach to balance logo sizing.
- LogoSoup React library automates normalization, density compensation, and cropping.
- Developers can fine-tune normalization and disable features as needed.

Recommendation: Read fully (read fully if you handle dynamic logo displays or want to use LogoSoup)
