---
type: concept
status: active
updated: 2026-04-14
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

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../tools/React Router|React Router]]
- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[React use()]]
- [[../patterns/Caching in App Router|Caching in App Router]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../sources/TWIR 255|TWIR 255]]
- [[../sources/TWIR 257|TWIR 257]]
- [[../sources/TWIR 273|TWIR 273]]
- [[../sources/TWIR 274|TWIR 274]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]
- [[../case-studies/Next.js App Router Exit|Next.js App Router Exit]]
- [[../case-studies/Next.js Inside ChatGPT|Next.js Inside ChatGPT]]
- [[../case-studies/Building Bulletproof React Components|Building Bulletproof React Components]]
- [[../case-studies/Error Rendering with RSC|Error Rendering with RSC]]

## Sources

- [[../../raw/twir/255/2025-10-22-TWIR-255|TWIR #255]]
- [[../../raw/twir/257/2025-11-05-TWIR-257|TWIR #257]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../sources/Custom React Server Components Framework|Custom React Server Components Framework]]
- [[../sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]]
- [[../sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]]
- [[../sources/Next.js use cache with next-intl|Next.js use cache with next-intl]]

## Open Questions

- Which parts of the Server Components model are durable architecture shifts versus framework-specific implementation details.
- How much of the current complexity comes from React itself versus framework conventions layered on top.
