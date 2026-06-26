---
type: tool
status: active
updated: 2026-06-26
tags:
  - astro
  - framework
  - static-sites
  - islands
---

# Astro

Astro is the tool hub for content-heavy, static-first, and island-architecture frontend applications in this vault.

## Key Ideas

- Astro's recurring value is selective interactivity: ship mostly HTML by default, then hydrate only the pieces that need client behavior.
- The important architectural thread is not "non-React versus React"; it is how static generation, server rendering, content pipelines, and client islands compose.
- Astro is a useful comparison point for Next.js because it makes different tradeoffs around content sites, self-hosting, JavaScript payload, and dynamic page islands.

## Practical Significance

- Use Astro as the route for sources about content-heavy framework fit, islands architecture, Content Layer, Server Islands, and static/dynamic composition outside Next.js.
- Keep React-specific Server Components material on `Server Components`, but link Astro when a source compares RSC to islands or static-first architecture.
- Treat migration stories toward Astro as framework-fit evidence, especially when the workload is SEO-heavy, mostly static, or selectively interactive.

## Current Signals

- TWIR #190 and #212 show the early Astro branch around Server Islands, Content Layer, zero-JS view transitions, and React Query integration inside Astro's island model.
- TWIR #232 and #233 add comparison material against Next.js and RSC, including page-size evidence and an Astro-over-Next.js production decision.
- TWIR #272 gives Astro 6 a stronger platform signal: Live Content Collections, CSP, production-like runtime development, Cloudflare integration, Rust compiler work, and route caching.
- TWIR #280 adds large-scale SSG benchmark evidence where Astro behaves better than array-oriented path-generation approaches at high page counts.
- The branch is still mostly tool/framework evidence; only the strongest production migration stories should become case-study pages.

## Related Pages

- [[Next.js]]
- [[React Router]]
- [[TanStack Start]]
- [[../concepts/Server Components|Server Components]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[../sources/TWIR 190|TWIR 190]]
- [[../sources/TWIR 212|TWIR 212]]
- [[../sources/TWIR 232|TWIR 232]]
- [[../sources/TWIR 233|TWIR 233]]
- [[../sources/TWIR 238|TWIR 238]]
- [[../sources/TWIR 272|TWIR 272]]
- [[../sources/TWIR 280|TWIR 280]]
- [[../sources/TWIR 287|TWIR 287]]

## Sources

- [[../../raw/twir/190/articles/06 - Future of Astro series - Zero-JS view transitions, Astro Content Layer, and Server Islands|Future of Astro series]]
- [[../../raw/twir/190/articles/12 - Using React Query with Astro|Using React Query with Astro]]
- [[../../raw/twir/202/articles/15 - Astro Content Layer - A Deep Dive|Astro Content Layer - A Deep Dive]]
- [[../../raw/twir/212/articles/01 - Astro 5.0|Astro 5.0]]
- [[../../raw/twir/232/articles/07 - From Next.js to Astro A Page Size Comparison|From Next.js to Astro: A Page Size Comparison]]
- [[../../raw/twir/233/articles/05 - RSC for Astro Developers|RSC for Astro Developers]]
- [[../../raw/twir/233/articles/11 - Why Kleinanzeigen.de Picked Astro Over Next.js|Why Kleinanzeigen.de Picked Astro Over Next.js]]
- [[../../raw/twir/238/articles/08 - Astro Integrations Explained|Astro Integrations Explained]]
- [[../../raw/twir/272/articles/01 - Astro 6.0|Astro 6.0]]
- [[../../raw/twir/280/articles/05 - Time to Yield - An SSG benchmark across five React frameworks|SSG benchmark across five React frameworks]]
- [[../../raw/twir/287/articles/05 - Waku’s Unique Feature Slices|Waku's Unique Feature Slices]]

## Open Questions

- Whether the Kleinanzeigen Astro-over-Next.js item deserves a dedicated case-study page after full source extraction is available.
- Whether Astro's route caching, Server Islands, and Content Layer should become a broader `Static/Dynamic Composition` pattern page if more framework-neutral sources accumulate.
