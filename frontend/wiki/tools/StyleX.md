---
type: tool
status: active
updated: 2026-10-22
tags: [stylex, styling, css, design-systems]
---

# StyleX

StyleX is a styling system focused on explicit composition, type-aware authoring, and build-time CSS. This hub connects the established Linear migration case to newer styling-state proposals.

## Key Ideas

- Runtime cost and customization contracts are separate reasons to adopt a styling system; both matter in a mature component library.
- Use the existing Linear case for migration evidence rather than treating every announcement or tutorial as a separate adoption case.
- The extracted enum RFC explores a finite set of inherited styling states with exhaustive matching. It is proposal evidence, not a guarantee of stable API availability.

## Practical Significance

- Compare styling systems through emitted work, component contracts, theming, escape hatches, and migration strategy.
- The TWIR 295 introductory and tutorial notes are summary-only; use the earlier Linear case and extracted RFC for stronger grounding.

## Related Pages

- [[Panda CSS|Panda CSS]]
- [[../patterns/Design System Styling Contracts|Design System Styling Contracts]]
- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../case-studies/GitHub Primer CSS Modules Migration|GitHub Primer CSS Modules Migration]]

## Sources

- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../../raw/twir/297/articles/03 - StyleX RFC - Add compile-time CSS enums and exhaustive matching|03 - StyleX RFC - Add compile-time CSS enums and exhaustive matching]]
- [[../../raw/twir/295/articles/03 - A deep dive into StyleX|03 - A deep dive into StyleX]] — summary-only tutorial.

## Open Questions

- Which enum proposals reach stable releases, and with what constraints?
- Where should a team prefer a constrained styling API over native CSS Modules?
