---
type: tool
status: active
updated: 2026-04-22
tags:
  - react
  - framework
  - nextjs
---

# Next.js

Next.js is one of the main framework hubs in this vault. This page should collect platform changes, API additions, runtime capabilities, and architectural implications for React applications.

## Key Ideas

- The main job of this page is to route into stable Next.js branches rather than re-argue individual migration stories.
- Adapter APIs, caching, streaming, security boundaries, and infrastructure choices matter because they reshape application architecture.
- Next.js remains one of the clearest indicators of where the production React platform is moving.

## Practical Significance

- Use this page as the main overview for framework surface, runtime direction, and branch-level routing.
- Push hosting tradeoffs, migration judgments, and direct framework comparisons into synthesis and case-study pages instead of collapsing them back into the hub.

## Current Signals

- The strongest supported branches are now platform APIs, portability constraints, public security surface, and App Router caching behavior.
- Stable adapters, `use cache`, App Router ergonomics, stream-pipeline work, and debugging/tooling changes are all already represented in the source set.
- Evidence that framework fit can break down in client-heavy products is still important, but it now lives mainly in supporting syntheses and case studies instead of defining the whole hub.
- The page should therefore stay centered on framework surface area and route outward to portability, security, and fit-specific branches when those questions become primary.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../concepts/React Activity|React Activity]]
- [[../concepts/React use()|React use()]]
- [[../concepts/Trusted Types|Trusted Types]]
- [[React Router]]
- [[TanStack Start]]
- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../patterns/Typed Routing and URL State|Typed Routing and URL State]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js 16.2|Next.js 16.2]]
- [[../sources/Next.js Deployment Adapters|Next.js Deployment Adapters]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/Next.js Server Actions Security|Next.js Server Actions Security]]
- [[../sources/React2DoS|React2DoS]]
- [[../sources/Partial Prerendering Architecture|Partial Prerendering Architecture]]
- [[../sources/Next.js at Enterprise Level|Next.js at Enterprise Level]]
- [[../sources/Next.js Agentic Future|Next.js Agentic Future]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../sources/The Precompute Pattern|The Precompute Pattern]]
- [[../case-studies/Next.js App Router Exit|Next.js App Router Exit]]
- [[../case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]]
- [[../case-studies/Next.js Middleware Bypass|Next.js Middleware Bypass]]
- [[../case-studies/Next.js Inside ChatGPT|Next.js Inside ChatGPT]]
- [[../case-studies/Framework Conventions in the AI Era|Framework Conventions in the AI Era]]
- [[../syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]]
- [[../syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]]
- [[../case-studies/Railway Off Next.js|Railway Off Next.js]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/227/2025-03-26-TWIR-227|TWIR #227]]
- [[../../raw/twir/229/2025-04-09-TWIR-229|TWIR #229]]
- [[../../raw/twir/257/2025-11-05-TWIR-257|TWIR #257]]
- [[../../raw/twir/268/2026-02-11-TWIR-268|TWIR #268]]
- [[../../raw/twir/269/2026-02-18-TWIR-269|TWIR #269]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../../raw/twir/276/2026-04-08-TWIR-276|TWIR #276]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
- [[../sources/Next.js 16|Next.js 16]]
- [[../sources/Next.js 16.2|Next.js 16.2]]
- [[../sources/Next.js Deployment Adapters|Next.js Deployment Adapters]]
- [[../sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/Partial Prerendering Architecture|Partial Prerendering Architecture]]
- [[../sources/Next.js at Enterprise Level|Next.js at Enterprise Level]]
- [[../sources/Next.js Agentic Future|Next.js Agentic Future]]
- [[../sources/Next.js Skills|Next.js Skills]]
- [[../sources/The Precompute Pattern|The Precompute Pattern]]
- [[../sources/Next.js Server Actions Security|Next.js Server Actions Security]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../sources/Next.js catchError|Next.js catchError]]

## Open Questions

- Which new framework surfaces deserve their own concept or pattern pages before this hub starts flattening them.
- How much of the current portability and fit debate will remain specific to Next.js versus converging with broader React framework tradeoffs.
