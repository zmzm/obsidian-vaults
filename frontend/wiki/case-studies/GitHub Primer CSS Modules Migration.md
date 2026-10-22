---
type: case-study
status: active
updated: 2026-10-22
tags: [github, css-modules, styling, migration]
---

# GitHub Primer CSS Modules Migration

GitHub Primer replaced runtime CSS-in-JS with CSS Modules while preserving compatibility for a much larger product codebase still using sx overrides.

## Context

- The extracted engineering account describes both server style-collection cost and browser initialization cost as migration drivers.
- Each component had old/new styles behind a flag, visual equivalence checks, and staged rollout from the team to staff and then users.
- A compatibility package kept sx-based consumers working while direct imports used the migrated implementation; completing the component library did not complete the product migration.
- The article reports 55% less page SSR time and 25% less component initialization time for its measured migration context, not expected gains for every application.

## Why It Matters

- A design system can carry architectural change incrementally when the compatibility seam and rollout are explicit.
- Reducing consumer escape-hatch usage was a separate phase from changing component internals.

## Related Pages

- [[Linear StyleX Migration|Linear StyleX Migration]]
- [[../patterns/Design System Styling Contracts|Design System Styling Contracts]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../tools/Panda CSS|Panda CSS]]

## Sources

- [[../../raw/twir/299/articles/05 - GitHub - Improving site performance by shipping more CSS|05 - GitHub - Improving site performance by shipping more CSS]]

## Open Questions

- How should compatibility-layer usage be measured and retired?
- Which styles can become named variants rather than migrated one-for-one?
