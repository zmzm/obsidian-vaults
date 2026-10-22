---
type: tool
status: active
updated: 2026-10-22
tags: [panda-css, styling, compiler, design-systems]
---

# Panda CSS

Panda CSS is a styling toolchain that extracts styles from source and supplies token, recipe, and design-system APIs. The captured 2.0 material separates extraction performance from the JavaScript cost left at call sites.

## Key Ideas

- The captured engine rewrite uses Oxc with native and WebAssembly bindings; faster extraction primarily affects build and editor workflows.
- Extracting a stylesheet does not necessarily remove browser work: calls that resolve style objects or variants may remain.
- Bundler source transforms can replace supported calls with computed class strings. Check emitted bundles and dynamic fallbacks rather than infer zero runtime from the presence of CSS files.
- Panda Studio exposes tokens and usage; publishing a design system is a separate concern from repeatedly extracting consumer sources.

## Practical Significance

- Evaluate build time, client style-resolution work, emitted CSS/JS, and authoring constraints independently.
- Treat the captured Node/ESM requirements and transform options as version-specific migration inputs.

## Related Pages

- [[StyleX|StyleX]]
- [[../patterns/Design System Styling Contracts|Design System Styling Contracts]]
- [[../case-studies/GitHub Primer CSS Modules Migration|GitHub Primer CSS Modules Migration]]
- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]

## Sources

- [[../../raw/twir/299/articles/01 - Panda CSS 2.0 - Same styling API, a new engine underneath|01 - Panda CSS 2.0 - Same styling API, a new engine underneath]]
- [[../../raw/twir/299/articles/02 - The styling runtime disappears from your bundle|02 - The styling runtime disappears from your bundle]]
- [[../../raw/twir/299/articles/03 - visualize it in Studio|03 - visualize it in Studio]]

## Open Questions

- Which dynamic call sites survive transformation in a real application?
- How do token publication and consumer extraction affect monorepo build costs?
