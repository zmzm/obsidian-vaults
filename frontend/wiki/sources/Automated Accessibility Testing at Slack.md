---
type: source
status: active
updated: 2026-04-30
tags:
  - accessibility
  - testing
  - playwright
---

# Automated Accessibility Testing at Slack

This source captures Slack's operational accessibility-testing approach: automated checks are useful when integrated into realistic browser tests, filtered carefully, and treated as a supplement to broader accessibility review.

## Summary

- Slack found Playwright a better fit for Axe-based accessibility checks than trying to force everything through Jest or React Testing Library.
- The workflow depends on custom filtering, known-issue exclusions, and reusable Playwright fixtures.
- Automated accessibility testing is positioned as a supplement rather than a full substitute for manual review and assistive-technology testing.
- The source reinforces that accessibility checks need operational discipline, not just a one-line tool install.

## Why This Source Matters

- It strengthens `Testing Strategy for React Apps` with a production-scale accessibility testing example.
- It complements `AI-Generated UI Accessibility` by showing how semantic UI contracts can be enforced in CI/browser workflows.
- It supports `Component Confidence Boundaries` by clarifying what automated component or browser tests can and cannot prove.

## Caveats

- Slack's infrastructure may be heavier than what small teams need.
- Axe-style checks catch important classes of issues but do not prove complete accessibility.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[AI-Generated UI Accessibility]]
- [[TWIR 216]]

## Raw Sources

- [[../../raw/twir/216/articles/03 - Automated Accessibility Testing at Slack|Automated Accessibility Testing at Slack]]
- [[../../raw/twir/216/2025-01-08-TWIR-216|TWIR #216]]
