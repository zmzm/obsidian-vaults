---
type: index
updated: 2026-04-22
status: active
---

# Frontend Wiki Index

This file is the map of the vault. Start here, then drill into specific pages.

## Raw

- [[raw/twir/258/2025-11-12-TWIR-258|TWIR #258]] — source issue and related article notes.
- [[raw/twir/259/2025-11-19-TWIR-259|TWIR #259]] — source issue and related article notes.
- [[raw/twir/260/2025-11-26-TWIR-260|TWIR #260]] — source issue and related article notes.
- [[raw/twir/261/2025-12-03-TWIR-261|TWIR #261]] — source issue and related article notes.
- [[raw/twir/262/2025-12-10-TWIR-262|TWIR #262]] — source issue and related article notes.
- [[raw/twir/263/2025-12-17-TWIR-263|TWIR #263]] — source issue and related article notes.
- [[raw/twir/264/2026-01-14-TWIR-264|TWIR #264]] — source issue and related article notes.
- [[raw/twir/265/2026-01-21-TWIR-265|TWIR #265]] — source issue and related article notes.
- [[raw/twir/273/2026-03-18-TWIR-273|TWIR #273]] — source issue and related article notes.
- [[raw/twir/274/2026-03-25-TWIR-274|TWIR #274]] — source issue and related article notes.
- [[raw/twir/275/2026-04-01-TWIR-275|TWIR #275]] — source issue and related article notes.
- [[raw/twir/276/2026-04-08-TWIR-276|TWIR #276]] — source issue and related article notes.
- [[raw/twir/277/2026-04-15-TWIR-277|TWIR #277]] — source issue and related article notes.

## Concepts

- [[wiki/concepts/React Compiler|React Compiler]] — the React compiler effort and its impact on component authoring.
- [[wiki/concepts/React Activity|React Activity]] — visibility, preserved state, and lower-priority hidden work in async React UIs.
- [[wiki/concepts/React Identity and Reconciliation|React Identity and Reconciliation]] — how React preserves or resets component identity across renders.
- [[wiki/concepts/React View Transitions|React View Transitions]] — declarative tree-level transitions coordinated with rendering, Suspense, and React scheduling.
- [[wiki/concepts/React use()|React use()]] — render-time reading of promises and context as part of async-aware React rendering.
- [[wiki/concepts/React useEffectEvent|React useEffectEvent]] — separation of non-reactive effect logic from subscription dependencies while still reading fresh values.
- [[wiki/concepts/Signals|Signals]] — a reactivity model centered on explicit dependencies and localized updates.
- [[wiki/concepts/Server Components|Server Components]] — the server-driven component model shaping modern React framework architecture.
- [[wiki/concepts/Trusted Types|Trusted Types]] — a browser security mechanism for reducing DOM-based XSS.

## Tools

- [[wiki/tools/Next.js|Next.js]] — framework hub for ecosystem changes, platform direction, and runtime capabilities.
- [[wiki/tools/React Router|React Router]] — routing, generated types, and type-safe navigation in framework-oriented React apps.
- [[wiki/tools/Storybook|Storybook]] — story-driven component development and increasingly integrated UI testing and coverage workflows.
- [[wiki/tools/TanStack DB|TanStack DB]] — embedded client-side database layer for live queries, normalized local data, and lower-rerender UI updates.
- [[wiki/tools/TanStack Start|TanStack Start]] — explicit full-stack React framework hub for middleware, SSR, and comparison with Next.js.
- [[wiki/tools/TanStack Query|TanStack Query]] — hub for data-fetching, query conventions, and server-state practices.

## Patterns

- [[wiki/patterns/Caching in App Router|Caching in App Router]] — cacheability, request-time APIs, and rendering boundaries in Next.js App Router.
- [[wiki/patterns/Client-First Data Sync|Client-First Data Sync]] — when client data should behave like a synchronized working set instead of a thin fetch cache.
- [[wiki/patterns/Component Confidence Boundaries|Component Confidence Boundaries]] — what story-driven and browser-realistic component testing can prove before route-level or e2e verification is still needed.
- [[wiki/patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]] — side-effect hygiene, external synchronization, and cleanup correctness in React.
- [[wiki/patterns/Resilient React Components|Resilient React Components]] — reusable component design under SSR, hydration, streaming, and host constraints.
- [[wiki/patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]] — choosing the right mix of component, integration, and end-to-end testing in React.
- [[wiki/patterns/Typed Routing and URL State|Typed Routing and URL State]] — validated route params, typed links, and schema-aware URL state as one routing contract.
- [[wiki/patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]] — using types, generated contracts, and enforced APIs to reduce runtime bugs.

## Topics

- [[wiki/topics/React Rendering|React Rendering]] — overview page for rendering, Fiber, transitions, and reactive update models.
- [[wiki/topics/SSR Performance|SSR Performance]] — throughput, latency, and server-side rendering optimization patterns across frameworks.

## Case Studies

### Framework Fit And Hosting

- [[wiki/case-studies/Next.js App Router Exit|Next.js App Router Exit]] — a real migration story away from App Router after sustained production use.
- [[wiki/case-studies/Next.js Host Runtime Friction|Next.js Host Runtime Friction]] — runtime-level portability case around stream adapters, buffering, and host-specific SSR behavior.
- [[wiki/case-studies/Next.js Inside ChatGPT|Next.js Inside ChatGPT]] — host-environment integration lessons from running Next.js inside ChatGPT.
- [[wiki/case-studies/Framework Conventions in the AI Era|Framework Conventions in the AI Era]] — why framework conventions become more valuable, not less, in AI-assisted engineering.
- [[wiki/case-studies/Railway Off Next.js|Railway Off Next.js]] — a production migration story where a client-heavy product moved from Next.js toward a Vite- and TanStack-based stack.
- [[wiki/case-studies/Next.js Middleware Bypass|Next.js Middleware Bypass]] — a security incident showing how framework internals, deployment topology, and communication affect real production risk.

### React Architecture And Performance

- [[wiki/case-studies/Async React Design Components|Async React Design Components]] — using async React primitives inside reusable component APIs.
- [[wiki/case-studies/Atomic State in Deep Trees|Atomic State in Deep Trees]] — improving deep-tree performance by replacing broad context updates with atomic state.
- [[wiki/case-studies/Building Bulletproof React Components|Building Bulletproof React Components]] — resilient component-authoring patterns for SSR, hydration, and concurrency.
- [[wiki/case-studies/Building a Toast Component|Building a Toast Component]] — a UI primitive case study where motion, gestures, and developer experience shape the component contract.
- [[wiki/case-studies/Error Rendering with RSC|Error Rendering with RSC]] — how failure handling differs across RSC, SSR, and browser rendering.
- [[wiki/case-studies/React ProseMirror Performance|React ProseMirror Performance]] — API-shape-driven rerender reduction in a large editor integration.
- [[wiki/case-studies/React Compiler Silent Failures|React Compiler Silent Failures]] — why compiler adoption needs workflow checks rather than silent fallback.
- [[wiki/case-studies/Virtual Scrolling at Massive Scale|Virtual Scrolling at Massive Scale]] — systems-level rendering and interaction techniques for extreme data tables.
- [[wiki/case-studies/GitHub Diff Performance|GitHub Diff Performance]] — large-scale React rendering simplification, virtualization, and latency reduction in GitHub's diff UI.
- [[wiki/case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]] — empirical memory leak patterns across a large frontend corpus.

### Testing, Migration, And Type Safety

- [[wiki/case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]] — large-scale test migration strategy and lessons.
- [[wiki/case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]] — AI-assisted migration that only worked once codemods, guides, and validation gates constrained the workflow.
- [[wiki/case-studies/Safer Frontend without React.FC|Safer Frontend without React.FC]] — a codebase-wide type-safety migration away from `React.FC`.

## Sources

This section is grouped by role so the index stays navigable without losing direct links to the underlying pages.

### Issue Digests

- `219-229`: [[wiki/sources/TWIR 219|TWIR 219]], [[wiki/sources/TWIR 220|TWIR 220]], [[wiki/sources/TWIR 221|TWIR 221]], [[wiki/sources/TWIR 222|TWIR 222]], [[wiki/sources/TWIR 223|TWIR 223]], [[wiki/sources/TWIR 224|TWIR 224]], [[wiki/sources/TWIR 225|TWIR 225]], [[wiki/sources/TWIR 226|TWIR 226]], [[wiki/sources/TWIR 227|TWIR 227]], [[wiki/sources/TWIR 228|TWIR 228]], [[wiki/sources/TWIR 229|TWIR 229]]
- `230-239`: [[wiki/sources/TWIR 230|TWIR 230]], [[wiki/sources/TWIR 231|TWIR 231]], [[wiki/sources/TWIR 232|TWIR 232]], [[wiki/sources/TWIR 233|TWIR 233]], [[wiki/sources/TWIR 234|TWIR 234]], [[wiki/sources/TWIR 235|TWIR 235]], [[wiki/sources/TWIR 236|TWIR 236]], [[wiki/sources/TWIR 237|TWIR 237]], [[wiki/sources/TWIR 238|TWIR 238]], [[wiki/sources/TWIR 239|TWIR 239]]
- `240-249`: [[wiki/sources/TWIR 240|TWIR 240]], [[wiki/sources/TWIR 241|TWIR 241]], [[wiki/sources/TWIR 242|TWIR 242]], [[wiki/sources/TWIR 243|TWIR 243]], [[wiki/sources/TWIR 244|TWIR 244]], [[wiki/sources/TWIR 245|TWIR 245]], [[wiki/sources/TWIR 246|TWIR 246]], [[wiki/sources/TWIR 247|TWIR 247]], [[wiki/sources/TWIR 248|TWIR 248]], [[wiki/sources/TWIR 249|TWIR 249]]
- `250-259`: [[wiki/sources/TWIR 250|TWIR 250]], [[wiki/sources/TWIR 251|TWIR 251]], [[wiki/sources/TWIR 252|TWIR 252]], [[wiki/sources/TWIR 253|TWIR 253]], [[wiki/sources/TWIR 254|TWIR 254]], [[wiki/sources/TWIR 255|TWIR 255]], [[wiki/sources/TWIR 256|TWIR 256]], [[wiki/sources/TWIR 257|TWIR 257]], [[wiki/sources/TWIR 258|TWIR 258]], [[wiki/sources/TWIR 259|TWIR 259]]
- `260-269`: [[wiki/sources/TWIR 260|TWIR 260]], [[wiki/sources/TWIR 261|TWIR 261]], [[wiki/sources/TWIR 262|TWIR 262]], [[wiki/sources/TWIR 263|TWIR 263]], [[wiki/sources/TWIR 264|TWIR 264]], [[wiki/sources/TWIR 265|TWIR 265]], [[wiki/sources/TWIR 266|TWIR 266]], [[wiki/sources/TWIR 267|TWIR 267]], [[wiki/sources/TWIR 268|TWIR 268]], [[wiki/sources/TWIR 269|TWIR 269]]
- `270-277`: [[wiki/sources/TWIR 270|TWIR 270]], [[wiki/sources/TWIR 271|TWIR 271]], [[wiki/sources/TWIR 272|TWIR 272]], [[wiki/sources/TWIR 273|TWIR 273]], [[wiki/sources/TWIR 274|TWIR 274]], [[wiki/sources/TWIR 275|TWIR 275]], [[wiki/sources/TWIR 276|TWIR 276]], [[wiki/sources/TWIR 277|TWIR 277]]

### Frameworks And Routing

- `Next.js`: [[wiki/sources/Next.js 16|Next.js 16]], [[wiki/sources/Next.js 16.2|Next.js 16.2]], [[wiki/sources/Next.js Deployment Adapters|Next.js Deployment Adapters]], [[wiki/sources/Next.js Metadata Streaming Portability|Next.js Metadata Streaming Portability]], [[wiki/sources/Next.js Node.js Streams for RSC|Next.js Node.js Streams for RSC]], [[wiki/sources/Next.js Server Actions Security|Next.js Server Actions Security]], [[wiki/sources/Next.js at Enterprise Level|Next.js at Enterprise Level]], [[wiki/sources/Next.js Agentic Future|Next.js Agentic Future]], [[wiki/sources/Next.js Skills|Next.js Skills]], [[wiki/sources/Next.js catchError|Next.js catchError]], [[wiki/sources/Next.js use cache with next-intl|Next.js use cache with next-intl]], [[wiki/sources/The Precompute Pattern|The Precompute Pattern]], [[wiki/sources/Partial Prerendering Architecture|Partial Prerendering Architecture]]
- `React Router / URL contracts`: [[wiki/sources/React Router Middleware|React Router Middleware]], [[wiki/sources/React Router Callsite Revalidation|React Router Callsite Revalidation]], [[wiki/sources/React Router Integration Points|React Router Integration Points]], [[wiki/sources/React Router Type Safety|React Router Type Safety]], [[wiki/sources/URL State Safety|URL State Safety]]
- `TanStack Start / RSC stacks`: [[wiki/sources/TanStack Start Middleware|TanStack Start Middleware]], [[wiki/sources/TanStack Start Migration Drivers|TanStack Start Migration Drivers]], [[wiki/sources/TanStack Start Single-Flight Mutations|TanStack Start Single-Flight Mutations]], [[wiki/sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]], [[wiki/sources/TanStack RSC as Data Streams|TanStack RSC as Data Streams]], [[wiki/sources/Custom React Server Components Framework|Custom React Server Components Framework]]

### React Runtime And Rendering

- [[wiki/sources/Async React Evolution|Async React Evolution]] — historical and conceptual bridge from Fiber to modern async React.
- [[wiki/sources/How State Updates Work Internally|How State Updates Work Internally]] — internals-level explanation of queued and batched React state updates.
- [[wiki/sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]] — rendering internals explainer around Fiber, lanes, and scheduling.
- [[wiki/sources/React use Hook|React use Hook]] — developer-facing explanation of `use()` as part of async-aware rendering.
- [[wiki/sources/React useTransition|React useTransition]] — practical usage boundaries for transition-driven UI updates.
- [[wiki/sources/React cacheSignal|React cacheSignal]] — cache-scope-aware cancellation for async resources tied to React's cache lifecycle.
- [[wiki/sources/React Key Prop|React Key Prop]] — practical reconciliation guidance around keys and component identity.
- [[wiki/sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]] — practical comparison of CSR, SSR, and RSC with measurable performance framing.
- [[wiki/sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]] — comparison between React Compiler and more compiler-first reactive models.
- [[wiki/sources/React Compiler Rust Port|React Compiler Rust Port]] — implementation-level signal for the React Compiler direction.

### Data, Testing, And Safety

- `Client data and query models`: [[wiki/sources/Creating Query Abstractions|Creating Query Abstractions]], [[wiki/sources/TanStack Query prefer-query-options|TanStack Query prefer-query-options]], [[wiki/sources/TanStack DB Query-Driven Sync|TanStack DB Query-Driven Sync]]
- `Testing`: [[wiki/sources/Storybook Component Testing|Storybook Component Testing]], [[wiki/sources/Vitest Browser Mode|Vitest Browser Mode]], [[wiki/sources/Testing Async React RSC Components|Testing Async React RSC Components]]
- `Safety and policy`: [[wiki/sources/Custom ESLint Rules|Custom ESLint Rules]], [[wiki/sources/React Trusted Types Integration|React Trusted Types Integration]], [[wiki/sources/React2DoS|React2DoS]]
- `Authoring`: [[wiki/sources/React Component API Game|React Component API Game]]

## Syntheses

- [[wiki/syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]] — first framework comparison synthesis based on the current source base.
- [[wiki/syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]] — comparison of render-time async reads, scheduling, and post-render effects.
- [[wiki/syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]] — comparison between compiler-assisted React optimization and dependency-graph runtime models.
- [[wiki/syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]] — testing synthesis across RTL, browser-realistic component testing, and server/client integration boundaries.
- [[wiki/syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]] — why framework conventions become more valuable as human-and-agent coordination infrastructure.
- [[wiki/syntheses/Designing React Components for Real Environments|Designing React Components for Real Environments]] — synthesis for reusable component APIs under SSR, async rendering, host constraints, and performance pressure.
- [[wiki/syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]] — synthesis of where adapter-level portability ends and hosting-specific Next.js friction still begins.
- [[wiki/syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]] — synthesis of how RSC escapes the original Next.js-only mental model across routers, bundlers, and custom stacks.

## System

- [[AGENTS]] — agent operating rules for this vault.
- [[log]] — record of notable updates.
