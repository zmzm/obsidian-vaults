---
type: pattern
evidence: mixed
evidence_reviewed: 2026-10-22
status: active
updated: 2026-10-22
tags: [design-systems, styling, component-api, migration]
---

# Design System Styling Contracts

A design-system styling contract defines which visual changes a component supports, how those changes compose, and where callers may deliberately escape the contract.

## Key Ideas

- Named variants express supported product meanings; arbitrary per-instance style objects or classes can create undocumented component APIs.
- Style compilation changes execution cost, while variant design changes maintenance cost. A faster compiler does not automatically produce a coherent design system.
- Inventory tokens and overrides so repeated exceptions can become supported variants rather than permanent implementation dependencies.
- Incremental migrations need old/new compatibility, visual checks, and a rollout mechanism. Primer compatibility wrappers show how component internals can migrate before all consumers.

## Practical Significance

- Specify supported variants and an explicit escape policy before broad conversion.
- Use visual regression and interaction checks to assess equivalence; measure both server style work and client initialization.
- The recovered className essay distinguishes real library behavior from proposed override inventories and illustrative mockups. Its author had not implemented the broad renaming migration, so do not describe those examples as measured production results.

## Related Pages

- [[../tools/StyleX|StyleX]]
- [[../tools/Panda CSS|Panda CSS]]
- [[Resilient React Components|Resilient React Components]]
- [[Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../case-studies/GitHub Primer CSS Modules Migration|GitHub Primer CSS Modules Migration]]

## Sources

- [[../../raw/twir/299/articles/07 - Props Are Not a Design System|07 - Props Are Not a Design System]]
- [[../../raw/twir/299/articles/05 - GitHub - Improving site performance by shipping more CSS|05 - GitHub - Improving site performance by shipping more CSS]]
- [[../../raw/twir/299/articles/03 - visualize it in Studio|03 - visualize it in Studio]]
- [[../../raw/twir/301/articles/07 - className Considered Harmful|07 - className Considered Harmful]] — summary-only; full extraction blocked.

- [[../../raw/twir/301/recovered/07 - className Considered Harmful|07 - className Considered Harmful]]

## Open Questions

- Which recurring overrides indicate a missing product variant?
- When does an escape hatch preserve useful flexibility, and when does it silently become the primary API?
