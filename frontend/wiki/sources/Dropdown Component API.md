---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - component-design
  - accessibility
---

# Dropdown Component API

This source captures dropdown authoring as a component-API design problem: flexible triggers, accessible interactions, closing behavior, and composable structure matter more than a narrow visual implementation.

## Summary

- Dropdowns share behavior but vary heavily in UI and interaction details, so rigid APIs age badly.
- Render props and compound components can expose trigger attributes and composition points without forcing one DOM shape.
- Robust dropdowns need multiple trigger modes, keyboard behavior, outside-click handling, Escape handling, and controlled-state escape hatches.
- Accessibility is part of the API contract, not a final implementation detail.

## Why This Source Matters

- It supports `Resilient React Components` with a concrete primitive where API shape, accessibility, and composition intersect.
- It complements existing component-design case studies by focusing on a common UI primitive rather than SSR or host-environment constraints.
- It provides a useful example for evaluating whether a component abstraction is flexible enough without becoming unstructured.

## Caveats

- The source comes from a component-library context, so app-local dropdowns may not need the same degree of API surface.
- The article summary is enough for current wiki support; deeper promotion should wait for more dropdown/menu-specific sources.

## Related Pages

- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[TWIR 215]]

## Raw Sources

- [[../../raw/twir/215/articles/01 - Building a dropdown|Building a dropdown]]
- [[../../raw/twir/215/2025-01-02-TWIR-215|TWIR #215]]
