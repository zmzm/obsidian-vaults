---
type: source
status: active
updated: 2026-04-30
tags:
  - accessibility
  - ai
  - react
---

# AI-Generated UI Accessibility

This source captures a recurring failure mode in AI-assisted React work: generated UI often optimizes for visual plausibility while missing semantic HTML, accessible names, keyboard behavior, landmarks, and ARIA contracts.

## Summary

- AI-generated React components frequently omit semantic structure and accessibility metadata because the feedback loop is visual rather than assistive-technology-aware.
- Common failures include missing roles, headings, labels, landmarks, keyboard interactions, and dynamic-update announcements.
- The practical mitigation is not just better prompting; teams need accessible primitives, linting, runtime checks, component tests, and review habits that make semantics explicit.
- A companion TWIR #279 item reinforces the same basic contract: use real HTML elements, maintain heading and landmark structure, label interactive elements, and manage focus intentionally.

## Why This Source Matters

- It connects the AI-era framework branch to a concrete quality risk instead of treating AI only as productivity tooling.
- It strengthens `Testing Strategy for React Apps` and `Component Confidence Boundaries` by making accessibility part of the component contract under test.
- It supports `Type-Driven Frontend Safety` by showing that enforceable policy and static checks matter beyond TypeScript types.

## Caveats

- The source is prescriptive and should be validated against real team workflows before becoming a full pattern page.
- AI tool quality changes quickly, but the underlying need for semantic UI contracts is durable.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[TWIR 278]]
- [[TWIR 279]]

## Raw Sources

- [[../../raw/twir/278/articles/05 - AI-Generated UI Is Inaccessible by Default|AI-Generated UI Is Inaccessible by Default]]
- [[../../raw/twir/279/articles/05 - Accessibility in React Common Mistakes and How to Fix Them|Accessibility in React: Common Mistakes and How to Fix Them]]
