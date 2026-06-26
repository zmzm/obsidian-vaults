---
type: concept
status: active
updated: 2026-06-26
tags:
  - react
  - rsc
  - server-components
---

# Server Components

Server Components are a React architecture model where part of the component tree is rendered on the server and streamed to the client, reducing client-side JavaScript while changing how data fetching, caching, and composition are structured.

## Key Ideas

- Server Components shift part of application composition and data access into the server-rendering pipeline.
- They reduce the need to ship certain logic to the client, but introduce new framework, routing, and caching constraints.
- In practice, Server Components are not just a React feature; they are tightly coupled to framework architecture and deployment decisions.

## Practical Significance

- This is one of the most important concepts for understanding modern React frameworks.
- The topic belongs at the center of discussions about Next.js, custom app frameworks, `use cache`, and async rendering.

## Current Signals

- The raw layer already contains both framework-level usage and custom framework implementation perspectives.
- The vault has enough material to treat this as an active concept rather than a placeholder.
- The newer source base also adds more concrete performance-oriented evidence instead of only framework or API framing.
- It now also includes stronger evidence on protocol-level security risk and an explicit alternative model where RSC behaves more like cacheable streamed data.
- TWIR #279 adds a lower-level rendering source for how Suspense boundaries let streamed server UI arrive out of order while preserving final placement.
- Earlier archive coverage adds RSC bundler boundaries plus an explicit comparison between server functions and Server Components.
- TWIR #280 through #287 deepen the post-Next.js view of RSC: protocol-level framing, TanStack-specific usage, Flight security incidents, bundler integration, and Waku-style render slicing all point to RSC as a broader framework substrate.
- TWIR #197 through #213 add older support for Waku server actions, TanStack Start server functions, `react-server`, RSC DevTools visibility, RSC testing, and React 19's stable server-oriented direction.
- Astro comparisons are useful here when they clarify the boundary between island architecture and React Server Components, but Astro-specific framework guidance belongs on the Astro tool page.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/Astro|Astro]]
- [[../tools/React Router|React Router]]
- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[React Activity]]
- [[React use()]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../sources/TWIR 255|TWIR 255]]
- [[../sources/TWIR 257|TWIR 257]]
- [[../sources/TWIR 273|TWIR 273]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../sources/TWIR 277|TWIR 277]]
- [[../sources/TWIR 197|TWIR 197]]
- [[../sources/TWIR 198|TWIR 198]]
- [[../sources/TWIR 203|TWIR 203]]
- [[../sources/TWIR 209|TWIR 209]]
- [[../sources/TWIR 212|TWIR 212]]
- [[../sources/TWIR 213|TWIR 213]]
- [[../sources/TWIR 280|TWIR 280]]
- [[../sources/TWIR 282|TWIR 282]]
- [[../sources/TWIR 283|TWIR 283]]
- [[../sources/TWIR 285|TWIR 285]]
- [[../sources/TWIR 287|TWIR 287]]
- [[../sources/RSC as Protocol|RSC as Protocol]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[../sources/TanStack RSC as Data Streams|TanStack RSC as Data Streams]]
- [[../sources/React2DoS|React2DoS]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/RSC Bundle Boundaries|RSC Bundle Boundaries]]
- [[../sources/Server Functions vs Server Components|Server Functions vs Server Components]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../case-studies/Next.js App Router Exit|Next.js App Router Exit]]
- [[../case-studies/Next.js Inside ChatGPT|Next.js Inside ChatGPT]]
- [[../case-studies/Next.js App Router Slow Responses|Next.js App Router Slow Responses]]
- [[../case-studies/Building Bulletproof React Components|Building Bulletproof React Components]]
- [[../case-studies/Error Rendering with RSC|Error Rendering with RSC]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/215/2025-01-02-TWIR-215|TWIR #215]]
- [[../../raw/twir/216/2025-01-08-TWIR-216|TWIR #216]]
- [[../../raw/twir/217/2025-01-15-TWIR-217|TWIR #217]]
- [[../../raw/twir/218/2025-01-22-TWIR-218|TWIR #218]]
- [[../../raw/twir/257/2025-11-05-TWIR-257|TWIR #257]]
- [[../../raw/twir/261/2025-12-03-TWIR-261|TWIR #261]]
- [[../../raw/twir/262/2025-12-10-TWIR-262|TWIR #262]]
- [[../../raw/twir/263/2025-12-17-TWIR-263|TWIR #263]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
- [[../../raw/twir/197/2024-08-21-TWIR-197|TWIR #197]]
- [[../../raw/twir/198/2024-08-28-TWIR-198|TWIR #198]]
- [[../../raw/twir/203/2024-10-01-TWIR-203|TWIR #203]]
- [[../../raw/twir/209/2024-11-13-TWIR-209|TWIR #209]]
- [[../../raw/twir/212/2024-12-04-TWIR-212|TWIR #212]]
- [[../../raw/twir/213/2024-12-11-TWIR-213|TWIR #213]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
- [[../../raw/twir/280/2026-05-06-TWIR-280|TWIR #280]]
- [[../../raw/twir/282/2026-05-20-TWIR-282|TWIR #282]]
- [[../../raw/twir/283/2026-05-27-TWIR-283|TWIR #283]]
- [[../../raw/twir/285/2026-06-10-TWIR-285|TWIR #285]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/TanStack RSC as Data Streams|TanStack RSC as Data Streams]]
- [[../sources/React2DoS|React2DoS]]
- [[../sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]]
- [[../sources/RSC Bundle Boundaries|RSC Bundle Boundaries]]
- [[../sources/Server Functions vs Server Components|Server Functions vs Server Components]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../sources/RSC as Protocol|RSC as Protocol]]

## Open Questions

- Which parts of the Server Components model are durable architecture shifts versus framework-specific implementation details.
- How much of the current complexity comes from React itself versus framework conventions layered on top.
