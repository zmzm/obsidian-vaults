---
type: case-study
status: active
updated: 2026-06-26
tags:
  - react
  - stylex
  - styling
  - performance
---

# Linear StyleX Migration

This case study captures Linear's migration from styled-components to StyleX as a styling-runtime and maintainability optimization.

## Context

- The migration was motivated by runtime performance pressure, styled-components maintenance concerns, and the need for stricter styling contracts.
- StyleX moved more styling work to build time and provided deterministic resolution and stronger encapsulation.
- The migration needed to preserve developer experience across a mature product codebase.

## What Helped

- Defining a new styling foundation before broad migration.
- Using codemods and agent-assisted workflows for repetitive conversion.
- Keeping lint rules strict while preserving escape hatches through CSS Modules for cases StyleX could not express cleanly.

## Why It Matters

- It is a useful styling case study because the gain is not only faster CSS; it is a clearer contract for how components express styles.
- It supports the rendering branch by showing that runtime styling choices can become measurable UI cost.
- It also belongs near component-resilience material because styling APIs constrain composition and maintenance.

## Main Lesson

- Large styling migrations work when the target system improves both runtime behavior and authoring constraints, and when automation is paired with explicit escape hatches.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../sources/TWIR 287|TWIR 287]]

## Raw Source

- [[../../raw/twir/287/articles/03 - Moving Linear from styled‑components to StyleX|TWIR item note]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
