---
type: twir-item
issue: 297
item: 3
item_type: item
date: 2026-09-16
source: https://github.com/facebook/stylex/pull/1865
tags:
  - "StyleX"
  - "RFC"
  - "CSS"
status: auto
quality: keep
---

[[2026-09-16-TWIR-297|Index]]

# Item 3: StyleX RFC - Add compile-time CSS enums and exhaustive matching

Source: [https://github.com/facebook/stylex/pull/1865](https://github.com/facebook/stylex/pull/1865)

Summary:
This RFC proposes adding compile-time CSS enums to StyleX, enabling developers to define CSS variables with a fixed set of possible states (enums) and perform exhaustive matching in styles. Enums can be overridden locally, inherit through the element tree, and are validated by TypeScript/Flow. The approach uses a CSS custom property "space hack" to simulate conditional values without native CSS if() support.

Key takeaways:
- Introduces enums for CSS variables, allowing exhaustive and type-safe value matching in StyleX.
- Enums can be overridden at any level, supporting inheritance and local assignment.
- The implementation is compatible with TypeScript/Flow and does not rely on native CSS if().
- This is the first in a series of related PRs to enhance StyleX's capabilities.

Recommendation:
Read fully

Content:
# [RFC] Add compile-time CSS enums and exhaustive matching by nmn · Pull Request #1865 · facebook/stylex · GitHub

[![@meta-cla](https://avatars.githubusercontent.com/in/1425812?s=40&v=4)](/apps/meta-cla)

[meta-cla](/apps/meta-cla)
Bot
added
the [CLA Signed](/facebook/stylex/issues?q=state%3Aopen%20label%3A%22CLA%20Signed%22)

This label is managed by the Facebook bot. Authors need to sign the CLA before a PR can be reviewed.

label

[Sep 10, 2026](#event-30870398293)
