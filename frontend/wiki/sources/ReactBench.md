---
type: source
status: active
updated: 2026-07-27
tags:
  - react
  - ai
  - testing
  - source
---

# ReactBench

ReactBench is a benchmark source for evaluating AI coding agents on realistic React work with quality checks beyond ordinary behavioral tests.

## Summary

- The benchmark uses production-style React tasks rather than isolated algorithm puzzles.
- Solutions must pass behavioral checks plus React-specific rules from React Doctor.
- The reported failure modes include subtle bugs, accessibility issues, and maintainability regressions, even when agents appear competent on ordinary tests.
- This makes ReactBench useful evidence for the gap between "passes tests" and "fits a real React codebase."

## Why This Source Matters

- It supports the vault's AI/framework branch with an evaluation artifact rather than another opinion piece.
- It strengthens the testing strategy branch by showing that React quality needs semantic, accessibility, and maintainability checks in addition to functional tests.
- It gives future agent-workflow discussions a place to anchor claims about production React difficulty.

## Caveats

- Benchmark rankings and model results will age quickly; keep this page focused on evaluation shape, not current leaderboard claims.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[../case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]]
- [[TWIR 291]]

## Raw Source

- [[../../raw/twir/291/articles/05 - ReactBench - Evaluates frontier coding agents on production React work|ReactBench - Evaluates frontier coding agents on production React work]]
