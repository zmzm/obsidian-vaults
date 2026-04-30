---
type: case-study
status: active
updated: 2026-04-21
tags:
  - react
  - performance
  - rendering
  - virtualization
---

# GitHub Diff Performance

This case study preserves a large-scale React performance refactor where GitHub simplified diff-line rendering to reduce memory pressure, DOM size, and interaction latency on huge pull requests.

## Context

- The target UI had to remain usable across extreme pull-request sizes, not just average cases.
- Earlier architecture optimized for component reuse and DOM parity, but that design accumulated too much runtime cost at scale.

## What Helped

- Flattening the React component tree and accepting some duplication to reduce wrapper overhead.
- Moving complex state into conditionally rendered children instead of paying for it on every diff line.
- Replacing scattered lookups and effects with predictable O(1) data access and stricter top-level state handling.
- Using virtualization for the largest pull requests so the DOM only reflects the visible working set.

## Why It Matters

- This is a strong practice page because it shows how performance work often comes from changing component and state shape, not from one isolated micro-optimization.
- It supports the rendering branch with real evidence that simpler trees, fewer effects, and explicit data access rules compound at scale.
- It also complements existing performance case studies with a UI-density and interaction-latency perspective.

## Main Lesson

- Large React surfaces get faster when teams optimize for less structure, less state, and less work per visible unit, then enforce those choices consistently.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[Virtual Scrolling at Massive Scale]]
- [[React ProseMirror Performance]]
- [[../sources/TWIR 277|TWIR 277]]

## Raw Source

- [[../../raw/twir/277/articles/05 - GitHub - The uphill climb of making diff lines performant|TWIR item note]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
