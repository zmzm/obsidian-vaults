---
type: case-study
status: active
updated: 2026-04-14
tags:
  - react
  - performance
  - editor
  - prosemirror
---

# React ProseMirror Performance

This case study captures a concrete performance problem in the React and ProseMirror boundary and a design fix that materially reduces rerenders.

## Context

- The issue appears when rendering large documents through a React integration layer.
- Memoization helps, but API design can still defeat it.

## What Changed

- Passing `pos` as a prop caused broad rerender churn.
- Replacing that prop with a `getPos` function preserved the information flow while reducing rerenders.
- The result was a significant improvement in editor responsiveness at scale.

## Why It Matters

- This is a good example of performance depending on API shape, not only on low-level optimization.
- It preserves an editor-specific engineering lesson that does not need to become a top-level concept node to remain valuable.

## Main Lesson

- Integration APIs can create or destroy memoization value; correctness and performance are often tied to boundary design.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../syntheses/Designing React Components for Real Environments|Designing React Components for Real Environments]]

## Raw Source

- [[../../raw/twir/275/articles/09 - Making React ProseMirror really, really fast|TWIR item note]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
