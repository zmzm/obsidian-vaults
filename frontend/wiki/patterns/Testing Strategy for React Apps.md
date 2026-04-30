---
type: pattern
status: active
updated: 2026-04-21
tags:
  - react
  - testing
  - rtl
  - component-testing
---

# Testing Strategy for React Apps

Testing Strategy for React Apps is the pattern page for choosing the right mix of component, integration, and end-to-end tests in modern React codebases.

## Key Ideas

- Good frontend testing strategy is not about maximizing one test style; it is about putting confidence at the cheapest reliable layer.
- Modern React testing increasingly favors user-facing behavior, browser-realistic environments, and integration-focused boundaries over implementation-detail assertions.
- Async React and Server Components put pressure on older testing assumptions, especially where render and side-effect timing differ from classic client-only React.

## Practical Significance

- This pattern gives the vault a landing page for testing migrations, RTL-oriented practice, component testing, and cases where e2e is still the more reliable option.
- It also keeps testing guidance out of unrelated framework or rendering hubs.

## Current Signals

- The source base already contains a large migration from Enzyme to RTL, material on `act()`, async RSC testing limitations, browser-based component testing, and shift-left testing strategy.
- That is enough to justify a dedicated pattern page rather than leaving testing material scattered or raw-only.
- The older archive now also adds route-middleware testing as a distinct example of integration-oriented frontend verification.

## Related Pages

- [[Component Confidence Boundaries]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/React Router|React Router]]
- [[../tools/Storybook|Storybook]]
- [[../sources/React Router Middleware|React Router Middleware]]
- [[../sources/Storybook Component Testing|Storybook Component Testing]]
- [[../case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]]
- [[../case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]]
- [[../sources/Testing Async React RSC Components|Testing Async React RSC Components]]
- [[../sources/Vitest Browser Mode|Vitest Browser Mode]]
- [[../syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]]

## Sources

- [[../../raw/twir/258/articles/09 - Everything you need to know about act() in React tests|Everything you need to know about act() in React tests]]
- [[../../raw/twir/259/articles/10 - Testing async React RSC components|Testing async React RSC components]]
- [[../../raw/twir/261/articles/12 - Vitest Browser Mode - The Future of Frontend Testing|Vitest Browser Mode - The Future of Frontend Testing]]
- [[../../raw/twir/225/articles/03 - Test Middleware in React Router|Test Middleware in React Router]]
- [[../../raw/twir/265/articles/13 - Front-end testing at Preply shifting left towards component testing|Front-end testing at Preply: shifting left towards component testing]]
- [[../../raw/twir/274/articles/08 - Test IDs are an a11y smell|Test IDs are an a11y smell]]
- [[../case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]]

## Open Questions

- Whether the vault later needs separate pages for component testing, RSC testing, and accessibility-driven testing.
- How much browser-based component testing will replace jsdom-centered workflows over time.
