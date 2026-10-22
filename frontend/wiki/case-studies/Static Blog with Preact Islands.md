---
type: case-study
status: active
updated: 2026-10-22
tags: [preact, static-sites, islands, migration, ai]
---

# Static Blog with Preact Islands

A captured personal-blog migration replaces a general-purpose Next.js build with a purpose-built static pipeline and selectively loaded Preact islands.

## Context

- The author’s content was static and already depended on React and MDX processing. The replacement rendered HTML with React at build time and retained selective client interactivity through Preact.
- MDX compilation and syntax highlighting happened during the build. Interactive desktop and palette components were loaded only on pages that needed them, with the palette deferred until use.
- A parity harness compared head tags, visible prose, and code blocks across 101 routes; it also uncovered content/feed and image problems.
- The author retained host-specific Build Output integration for assets, redirects, image optimization, and analytics, and accepted ownership of the replacement’s bugs and browser quirks.

## Why It Matters

- Content compilation, client runtime selection, interaction loading, and host integration can be chosen independently for a narrowly scoped site.
- The parity harness checks bounded outputs. It does not establish accessibility, all interaction behavior, or long-term maintenance equivalence.
- This supports a workload-specific framework-fit argument. It does not show that Preact alone caused every improvement or that bespoke tooling is preferable for team-scale dynamic applications.

## Related Pages

- [[../tools/Preact|Preact]]
- [[../tools/Astro|Astro]]
- [[../tools/Remix|Remix]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../patterns/Component Confidence Boundaries|Component Confidence Boundaries]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]

## Sources

- [[../../raw/twir/296/articles/07 - Replacing Next.js with a vibe-coded framework|07 - Replacing Next.js with a vibe-coded framework]]

## Open Questions

- How will the replacement absorb browser fixes and previously omitted framework behavior over time?
- Which interactive islands can remain isolated without introducing duplicated state or incompatible hydration assumptions?
