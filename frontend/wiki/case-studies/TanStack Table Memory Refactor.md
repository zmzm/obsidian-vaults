---
type: case-study
status: active
updated: 2026-06-26
tags:
  - tanstack
  - performance
  - memory
  - tables
---

# TanStack Table Memory Refactor

This case study preserves the TanStack Table V9 memory refactor as a concrete example of changing object shape to improve large-data UI scalability.

## Context

- TanStack Table V8 allocated many row, column, cell, and header objects with duplicated methods and closures.
- Large tables amplified that per-instance overhead until browser memory became the limiting factor.
- V9 moved shared behavior onto prototypes so repeated instances carried mostly unique data.

## What Helped

- Identifying duplicated methods and closures as the scaling bottleneck.
- Sharing methods through prototypes instead of recreating them for every table object.
- Accepting a small breaking change in exchange for a much better memory curve.

## Why It Matters

- This is a strong frontend performance case because it shows that JavaScript allocation shape can matter as much as React render count.
- It complements virtual-scrolling and rendering case studies with a lower-level memory model lesson.
- It is broadly transferable to libraries that instantiate many similar objects.

## Main Lesson

- In data-dense UI libraries, performance work often means changing the shape and lifetime of objects, not only reducing component rerenders.

## Related Pages

- [[../tools/TanStack|TanStack]]
- [[../topics/React Rendering|React Rendering]]
- [[Virtual Scrolling at Massive Scale]]
- [[../sources/TWIR 287|TWIR 287]]

## Raw Source

- [[../../raw/twir/287/articles/04 - How an Underrated Refactor Saved 90% Memory Usage|TWIR item note]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
