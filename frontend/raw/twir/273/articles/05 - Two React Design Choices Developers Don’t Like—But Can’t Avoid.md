---
type: twir-item
issue: 273
item: 5
item_type: item
date: 2026-03-18
source: https://dev.to/playfulprogramming/two-react-design-choices-developers-dont-like-but-cant-avoid-d6g
tags:
  - "LikeBut"
status: auto
---

[[2026-03-18-TWIR-273|Index]]

# Item 5: Two React Design Choices Developers Don’t Like—But Can’t Avoid

Source: [https://dev.to/playfulprogramming/two-react-design-choices-developers-dont-like-but-cant-avoid-d6g](https://dev.to/playfulprogramming/two-react-design-choices-developers-dont-like-but-cant-avoid-d6g)

Summary:
The author examines two widely disliked React design choices—deferred state commits and dependency arrays in effects—arguing they stem from deep architectural constraints around asynchronicity and determinism. Drawing on experience with Signals and Solid.js, the piece explains why React’s approach, though unpopular, is necessary for consistency in async UI.

Key takeaways:
- Deferred state commits ensure UI consistency during async updates.
- Dependency arrays in effects are a practical solution to avoid unnecessary recalculations.
- Signals and other reactive models offer alternatives but face similar core challenges.
- Async state management is fundamentally complex and shapes framework design.

Recommendation: Read fully (for advanced understanding of React’s architectural tradeoffs)
