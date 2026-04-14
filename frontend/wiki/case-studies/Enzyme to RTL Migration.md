---
type: case-study
status: active
updated: 2026-04-14
tags:
  - testing
  - enzyme
  - rtl
  - migration
---

# Enzyme to RTL Migration

This case study captures a large-scale testing migration from Enzyme to React Testing Library across many repositories and tens of thousands of tests.

## Context

- The migration was driven by Enzyme’s deprecation and poor fit with modern React.
- The scope was large enough that tooling, communication, and sequencing mattered as much as code changes.

## What Made It Work

- Smaller packages were migrated first.
- Internal education and documentation supported teams during the shift.
- Migration progress was tracked centrally.
- The destination testing model emphasized user-facing behavior rather than implementation details.

## Why It Matters

- This is a strong engineering-practice page, even though it does not belong in a core React concept hub.
- It preserves migration lessons that can help future testing transitions or large-scale codebase changes.

## Main Lesson

- Large technical migrations succeed through process design and education, not just better replacement tools.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../sources/TWIR 260|TWIR 260]]

## Raw Source

- [[../../raw/twir/260/articles/09 - Moving Mountains How We Migrated from Enzyme to React Testing Library|TWIR item note]]
- [[../../raw/twir/260/2025-11-26-TWIR-260|TWIR #260]]
