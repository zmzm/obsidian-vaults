---
type: synthesis
status: active
updated: 2026-04-16
tags:
  - react
  - testing
  - rtl
  - rsc
  - browser-mode
---

# Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries

This synthesis connects the current testing branch in the vault: RTL-style behavior testing, browser-realistic component testing, and the harder boundaries introduced by async React and Server Components.

## Short Thesis

Modern React testing is moving toward more realistic environments and more explicit boundaries. The core shift is not simply from one library to another; it is from implementation-detail assertions toward tests that respect where confidence actually comes from.

## What Changed

- Enzyme-era testing assumed that shallow inspection and component internals were stable enough to test directly.
- RTL shifted the center of gravity toward user-visible behavior and DOM semantics.
- Browser-mode component testing pushes this further by running components in a real browser rather than relying only on jsdom approximations.
- Async React and Server Components add boundaries where component tests can no longer cheaply stand in for end-to-end confidence.

## Where Each Layer Fits

- RTL is strongest when the goal is user-facing behavior and accessible interaction semantics.
- Browser-mode component testing is strongest when timing, layout, browser APIs, or integration with real rendering behavior matter.
- Integration and e2e testing remain necessary when route loaders, actions, RSC boundaries, and server-driven composition are part of the real behavior under test.

## Main Tension

The modern testing problem is not choosing a single best tool. It is deciding how much realism is required before the test becomes trustworthy enough to justify its cost.

This is why the branch now points toward mixed strategies:

- behavior-first assertions over implementation-first assertions,
- browser-realistic execution where jsdom abstractions are too weak,
- and explicit use of integration boundaries when modern framework behavior spans client and server.

## Practical Heuristic

- Prefer RTL-style tests when the contract is UI behavior, semantics, and interaction.
- Prefer browser-mode component tests when the behavior depends on real browser capabilities or when jsdom creates false confidence.
- Prefer route-level integration or e2e tests when server/client boundaries, RSC behavior, or framework data flows are part of the feature.

## Why This Synthesis Matters

- It gives the vault a single page for the testing branch instead of leaving migration stories, RSC testing limitations, and browser-mode arguments scattered across patterns and raw notes.
- It also clarifies that modern React testing is about confidence placement, not just library preference.

## Related Pages

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/React Router|React Router]]
- [[../case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]]
- [[../case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]]
- [[../sources/React Router Integration Points|React Router Integration Points]]
- [[../sources/Testing Async React RSC Components|Testing Async React RSC Components]]
- [[../sources/Vitest Browser Mode|Vitest Browser Mode]]

## Sources

- [[../patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]]
- [[../case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]]
- [[../case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]]
- [[../sources/React Router Integration Points|React Router Integration Points]]
- [[../sources/Testing Async React RSC Components|Testing Async React RSC Components]]
- [[../sources/Vitest Browser Mode|Vitest Browser Mode]]
- [[../../raw/twir/258/articles/09 - Everything you need to know about act() in React tests|Everything you need to know about act() in React tests]]
- [[../../raw/twir/259/articles/10 - Testing async React RSC components|Testing async React RSC components]]
- [[../../raw/twir/261/articles/12 - Vitest Browser Mode - The Future of Frontend Testing|Vitest Browser Mode - The Future of Frontend Testing]]
- [[../../raw/twir/265/articles/13 - Front-end testing at Preply shifting left towards component testing|Front-end testing at Preply: shifting left towards component testing]]
- [[../../raw/twir/274/articles/08 - Test IDs are an a11y smell|Test IDs are an a11y smell]]

## Open Questions

- How much browser-mode component testing will replace jsdom-centered workflows over time.
- Whether RSC-heavy applications will push more teams toward route-level integration tests instead of component-level confidence.
