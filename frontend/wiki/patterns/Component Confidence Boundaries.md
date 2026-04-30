---
type: pattern
status: active
updated: 2026-04-22
tags:
  - testing
  - component-testing
  - storybook
  - browser-testing
---

# Component Confidence Boundaries

Component Confidence Boundaries is the pattern page for deciding what component-level tests and story-driven coverage can reliably prove before teams need route-level or end-to-end verification.

## Key Ideas

- Component testing is strongest when it verifies real user-visible states, interactions, and accessibility behavior rather than implementation details.
- Story-driven coverage can make missing UI states obvious, but it does not automatically prove full application integration correctness.
- Browser-realistic runtimes raise the ceiling of component confidence, yet they still sit below workflow-level confidence.

## Practical Significance

- This pattern gives the vault a dedicated home for Storybook-centered testing, browser-mode component tests, and the "shift left without lying to yourself" branch.
- It also clarifies a common confusion in frontend teams: component confidence is a useful layer, but it has boundaries that should stay explicit.

## Current Signals

- The archive now shows Storybook evolving toward a unified interaction, accessibility, visual, and coverage-oriented surface.
- Vitest Browser Mode adds a stronger runtime model for component tests than classic jsdom-only setups.
- Additional testing material reinforces the boundary: shifting left toward component testing is valuable, but selectors, coverage numbers, and stories still need user-facing discipline and clear limits.

## Related Pages

- [[Testing Strategy for React Apps]]
- [[../tools/Storybook|Storybook]]
- [[../sources/Storybook Component Testing|Storybook Component Testing]]
- [[../sources/Vitest Browser Mode|Vitest Browser Mode]]
- [[../syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]]
- [[../sources/TWIR 237|TWIR 237]]
- [[../sources/TWIR 240|TWIR 240]]
- [[../sources/TWIR 261|TWIR 261]]
- [[../sources/TWIR 265|TWIR 265]]
- [[../sources/TWIR 274|TWIR 274]]

## Sources

- [[../../raw/twir/237/articles/01 - Storybook 9|Storybook 9]]
- [[../../raw/twir/240/articles/09 - Frontend test coverage with Storybook 9|Frontend test coverage with Storybook 9]]
- [[../../raw/twir/245/articles/10 - Component Test with Storybook and Vitest|Component Test with Storybook and Vitest]]
- [[../../raw/twir/261/articles/12 - Vitest Browser Mode - The Future of Frontend Testing|Vitest Browser Mode - The Future of Frontend Testing]]
- [[../../raw/twir/265/articles/13 - Front-end testing at Preply shifting left towards component testing|Front-end testing at Preply: shifting left towards component testing]]
- [[../../raw/twir/274/articles/08 - Test IDs are an a11y smell|Test IDs are an a11y smell]]
- [[../sources/Storybook Component Testing|Storybook Component Testing]]
- [[../sources/Vitest Browser Mode|Vitest Browser Mode]]

## Open Questions

- How far browser-mode component testing can replace route-level integration tests for mainstream product teams.
- Whether story coverage will become a durable default workflow or remain strongest in design systems and component-library-heavy teams.
