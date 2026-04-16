---
type: case-study
status: active
updated: 2026-04-16
tags:
  - testing
  - ai
  - codemods
  - migration
---

# Migrating 6000 React Tests with AI and ASTs

This case study captures a large-scale testing migration where AI agents were useful only after the work was constrained by migration guides, codemods, and strict validation loops.

## Context

- The migration covered nearly a thousand test files and more than six thousand test cases.
- The target was a major Testing Library upgrade with both API and timing-model changes.
- A naive "let the agent migrate everything" approach failed early because the error space was too broad.

## What Made It Work

- A migration guide was written and iteratively refined as new edge cases were discovered.
- Codemods converted the repeated syntax changes into testable AST transforms.
- Two package versions were run in parallel to allow incremental rollout.
- Every migrated file was validated with linting, test execution, and coverage checks before moving on.

## Why It Matters

- This is a strong testing-practice page, but it is also relevant to the AI/framework branch because it shows where agentic workflows need hard constraints.
- It preserves a realistic model for AI-assisted migration work: agents can accelerate the loop, but only after humans define the rails.

## Main Lesson

- Large AI-assisted code migrations succeed when automation is boxed in by codemods, explicit instructions, and verification gates.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[../case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]]

## Raw Source

- [[../../raw/twir/261/articles/11 - Migrating 6000 React tests using AI Agents and ASTs|TWIR item note]]
- [[../../raw/twir/261/2025-12-03-TWIR-261|TWIR #261]]
