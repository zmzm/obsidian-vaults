---
type: tool
status: active
evidence: full-text
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [preact, islands, hydration, prerendering]
---

# Preact

Preact is a UI rendering library connected here to prerendering, selective interactive islands, and resumed hydration through recovered primary guides and an application case.

## Key Ideas

- The preset guide describes generating HTML at build time through a prerender entry and discovered links. This is a separate decision from which components hydrate in the browser.
- The islands guide gives independent client entry points, serialized initial props, and a manifest connecting production assets to server HTML. Islands require explicit loading and state boundaries.
- The maintainer’s hydration account distinguishes resumed client hydration, DOM-range boundary bookkeeping, and server streaming. These are related mechanisms rather than one feature.
- The retrieved hydration account says resumed boundaries continue when dependencies resolve, whereas React can prioritize interaction. It also records unresolved useId consistency concerns; keep version and publication context with these claims.

## Practical Significance

- Choose the server-output strategy, hydration boundaries, and interaction-loading policy separately.
- Compatibility must be assessed for the features and components actually used. The static-blog case is application evidence, not proof of complete React parity.
- The three previously missing guides were recovered on 2026-10-22. Historical release plans describe the source’s state, not a verified current release matrix.

## Related Pages

- [[Astro|Astro]]
- [[Vite|Vite]]
- [[Remix|Remix]]
- [[../case-studies/Static Blog with Preact Islands|Static Blog with Preact Islands]]
- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]

## Sources

- [[../../raw/twir/197/recovered/09 - Preact - Prerendering with Preset Vite|09 - Preact - Prerendering with Preset Vite]]
- [[../../raw/twir/208/recovered/14 - Preact - Simplifying Islands Architecture|14 - Preact - Simplifying Islands Architecture]]
- [[../../raw/twir/290/recovered/10 - Async hydration in Preact|10 - Async hydration in Preact]]
- [[../../raw/twir/296/articles/07 - Replacing Next.js with a vibe-coded framework|07 - Replacing Next.js with a vibe-coded framework]]

## Open Questions

- Which hydration and identifier limitations apply to the exact deployed Preact version?
- How do independently loaded islands share state without accidental duplication or lifetime ambiguity?
