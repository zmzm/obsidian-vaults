---
type: twir-item
issue: 269
item: 8
item_type: item
date: 2026-02-18
source: https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4
tags:
  - "ReactFC"
status: auto
---

[[2026-02-18-TWIR-269|Index]]

# Item 8: The Journey to a Safer Frontend: Why Gusto Removed React.FC

Source: [https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

Summary:
Gusto migrated away from using React.FC in their codebase after discovering it masked TypeScript errors and reduced type safety. The team automated the transition to explicit prop and return types, surfacing hidden bugs and improving code quality. The article outlines the rationale, migration process, and cultural impact of this change.

Key takeaways:
- React.FC can hide unused props and break type inference, leading to subtle bugs.
- Migrating to explicit prop and return types improves TypeScript’s effectiveness and code reliability.
- The migration was automated and enforced with a linter rule to prevent regressions.
- The process uncovered and resolved numerous latent issues across the codebase.

Recommendation: Read fully (read fully only if planning a similar migration or interested in TypeScript/React best practices)
