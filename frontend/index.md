---
type: index
updated: 2026-04-16
status: active
---

# Frontend Wiki Index

This file is the map of the vault. Start here, then drill into specific pages.

## Raw

- [[raw/twir/273/2026-03-18-TWIR-273|TWIR #273]] — source issue and related article notes.
- [[raw/twir/274/2026-03-25-TWIR-274|TWIR #274]] — source issue and related article notes.
- [[raw/twir/275/2026-04-01-TWIR-275|TWIR #275]] — source issue and related article notes.

## Concepts

- [[wiki/concepts/React Compiler|React Compiler]] — the React compiler effort and its impact on component authoring.
- [[wiki/concepts/React Identity and Reconciliation|React Identity and Reconciliation]] — how React preserves or resets component identity across renders.
- [[wiki/concepts/React use()|React use()]] — render-time reading of promises and context as part of async-aware React rendering.
- [[wiki/concepts/Signals|Signals]] — a reactivity model centered on explicit dependencies and localized updates.
- [[wiki/concepts/Server Components|Server Components]] — the server-driven component model shaping modern React framework architecture.
- [[wiki/concepts/Trusted Types|Trusted Types]] — a browser security mechanism for reducing DOM-based XSS.

## Tools

- [[wiki/tools/Next.js|Next.js]] — framework hub for ecosystem changes, platform direction, and runtime capabilities.
- [[wiki/tools/React Router|React Router]] — routing, generated types, and type-safe navigation in framework-oriented React apps.
- [[wiki/tools/TanStack Start|TanStack Start]] — explicit full-stack React framework hub for middleware, SSR, and comparison with Next.js.
- [[wiki/tools/TanStack Query|TanStack Query]] — hub for data-fetching, query conventions, and server-state practices.

## Patterns

- [[wiki/patterns/Caching in App Router|Caching in App Router]] — cacheability, request-time APIs, and rendering boundaries in Next.js App Router.
- [[wiki/patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]] — side-effect hygiene, external synchronization, and cleanup correctness in React.
- [[wiki/patterns/Resilient React Components|Resilient React Components]] — reusable component design under SSR, hydration, streaming, and host constraints.
- [[wiki/patterns/Testing Strategy for React Apps|Testing Strategy for React Apps]] — choosing the right mix of component, integration, and end-to-end testing in React.
- [[wiki/patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]] — using types, generated contracts, and enforced APIs to reduce runtime bugs.

## Topics

- [[wiki/topics/React Rendering|React Rendering]] — overview page for rendering, Fiber, transitions, and reactive update models.
- [[wiki/topics/SSR Performance|SSR Performance]] — throughput, latency, and server-side rendering optimization patterns across frameworks.

## Case Studies

- [[wiki/case-studies/Next.js App Router Exit|Next.js App Router Exit]] — a real migration story away from App Router after sustained production use.
- [[wiki/case-studies/Next.js Inside ChatGPT|Next.js Inside ChatGPT]] — host-environment integration lessons from running Next.js inside ChatGPT.
- [[wiki/case-studies/Framework Conventions in the AI Era|Framework Conventions in the AI Era]] — why framework conventions become more valuable, not less, in AI-assisted engineering.
- [[wiki/case-studies/Async React Design Components|Async React Design Components]] — using async React primitives inside reusable component APIs.
- [[wiki/case-studies/Atomic State in Deep Trees|Atomic State in Deep Trees]] — improving deep-tree performance by replacing broad context updates with atomic state.
- [[wiki/case-studies/Building Bulletproof React Components|Building Bulletproof React Components]] — resilient component-authoring patterns for SSR, hydration, and concurrency.
- [[wiki/case-studies/Building a Toast Component|Building a Toast Component]] — a UI primitive case study where motion, gestures, and developer experience shape the component contract.
- [[wiki/case-studies/Error Rendering with RSC|Error Rendering with RSC]] — how failure handling differs across RSC, SSR, and browser rendering.
- [[wiki/case-studies/React ProseMirror Performance|React ProseMirror Performance]] — API-shape-driven rerender reduction in a large editor integration.
- [[wiki/case-studies/React Compiler Silent Failures|React Compiler Silent Failures]] — why compiler adoption needs workflow checks rather than silent fallback.
- [[wiki/case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]] — empirical memory leak patterns across a large frontend corpus.
- [[wiki/case-studies/Enzyme to RTL Migration|Enzyme to RTL Migration]] — large-scale test migration strategy and lessons.
- [[wiki/case-studies/Migrating 6000 React Tests with AI and ASTs|Migrating 6000 React Tests with AI and ASTs]] — AI-assisted migration that only worked once codemods, guides, and validation gates constrained the workflow.
- [[wiki/case-studies/Safer Frontend without React.FC|Safer Frontend without React.FC]] — a codebase-wide type-safety migration away from `React.FC`.
- [[wiki/case-studies/Virtual Scrolling at Massive Scale|Virtual Scrolling at Massive Scale]] — systems-level rendering and interaction techniques for extreme data tables.

## Sources

- [[wiki/sources/TWIR 255|TWIR 255]] — digest issue covering Next.js 16, async React framing, and practical RSC performance questions.
- [[wiki/sources/TWIR 256|TWIR 256]] — digest issue covering middleware and migration pressure from Next.js toward TanStack Start.
- [[wiki/sources/TWIR 257|TWIR 257]] — digest issue covering Partial Prerendering and cache-related request semantics.
- [[wiki/sources/TWIR 266|TWIR 266]] — digest issue covering TanStack Start mutation flows and adjacent TanStack integration material.
- [[wiki/sources/TWIR 267|TWIR 267]] — digest issue covering a concrete migration from Next.js to TanStack Start.
- [[wiki/sources/TWIR 268|TWIR 268]] — digest issue covering component robustness, enterprise Next.js, and TanStack Router auth patterns.
- [[wiki/sources/TWIR 269|TWIR 269]] — digest issue covering Next.js platform direction, agent tooling, and framework competition.
- [[wiki/sources/TWIR 270|TWIR 270]] — digest issue covering query abstractions, React Router patterns, and transition usage.
- [[wiki/sources/TWIR 271|TWIR 271]] — digest issue covering RSC ergonomics, Fiber motivation, and ecosystem shifts around React.
- [[wiki/sources/TWIR 272|TWIR 272]] — digest issue covering state internals, compiler-model comparisons, and more Server Components context.
- [[wiki/sources/TWIR 273|TWIR 273]] — digest issue covering Server Components, SSR tradeoffs, and Async React context.
- [[wiki/sources/TWIR 274|TWIR 274]] — digest issue centered on Next.js 16.2, `use cache`, `use()`, and routing ergonomics.
- [[wiki/sources/TWIR 275|TWIR 275]] — curated digest issue that routes several important frontend themes into the wiki.
- [[wiki/sources/Custom React Server Components Framework|Custom React Server Components Framework]] — case study on building a tailored RSC framework.
- [[wiki/sources/Creating Query Abstractions|Creating Query Abstractions]] — tradeoffs around wrapping query APIs versus keeping abstractions thin.
- [[wiki/sources/Async React Evolution|Async React Evolution]] — historical and conceptual bridge from Fiber to modern async React.
- [[wiki/sources/Compiler-Driven UI Boundaries|Compiler-Driven UI Boundaries]] — comparison between React Compiler and more compiler-first reactive models.
- [[wiki/sources/How State Updates Work Internally|How State Updates Work Internally]] — internals-level explanation of queued and batched React state updates.
- [[wiki/sources/Next.js 16|Next.js 16]] — major release anchor for explicit caching, PPR, MCP tooling, and React 19.2 support.
- [[wiki/sources/Next.js 16.2|Next.js 16.2]] — release anchor for platform direction, performance, and debugging improvements.
- [[wiki/sources/Next.js at Enterprise Level|Next.js at Enterprise Level]] — enterprise architecture, SSR/SSG tradeoffs, and caching concerns in large Next.js apps.
- [[wiki/sources/Next.js Agentic Future|Next.js Agentic Future]] — framework direction toward agent-facing tooling and structured runtime context.
- [[wiki/sources/Next.js Skills|Next.js Skills]] — agent-oriented operational knowledge packaged as reusable Next.js workflow skills.
- [[wiki/sources/Next.js catchError|Next.js catchError]] — framework-aware error handling in the App Router model.
- [[wiki/sources/Next.js use cache with next-intl|Next.js use cache with next-intl]] — practical caching and i18n friction in the App Router model.
- [[wiki/sources/Partial Prerendering Architecture|Partial Prerendering Architecture]] — the move from error-based to promise-based dynamic detection in PPR.
- [[wiki/sources/React Compiler Rust Port|React Compiler Rust Port]] — implementation-level signal for the React Compiler direction.
- [[wiki/sources/React Component API Game|React Component API Game]] — lightweight API-design practice signal for naming, prop shape, and maintainability judgment.
- [[wiki/sources/React Key Prop|React Key Prop]] — practical reconciliation guidance around keys and component identity.
- [[wiki/sources/React Router Integration Points|React Router Integration Points]] — loaders and actions as route-level integration glue rather than business logic containers.
- [[wiki/sources/Testing Async React RSC Components|Testing Async React RSC Components]] — practical limits and workarounds for testing async Server Components below full integration tests.
- [[wiki/sources/Vitest Browser Mode|Vitest Browser Mode]] — browser-realistic component testing as a layer between jsdom tests and e2e coverage.
- [[wiki/sources/React use Hook|React use Hook]] — developer-facing explanation of `use()` as part of async-aware rendering.
- [[wiki/sources/React useTransition|React useTransition]] — practical usage boundaries for transition-driven UI updates.
- [[wiki/sources/React Router Type Safety|React Router Type Safety]] — generated route types and typed navigation ergonomics.
- [[wiki/sources/React Trusted Types Integration|React Trusted Types Integration]] — React support for Trusted Types and secure DOM sinks.
- [[wiki/sources/RSC Performance Tradeoffs|RSC Performance Tradeoffs]] — practical comparison of CSR, SSR, and RSC with measurable performance framing.
- [[wiki/sources/TanStack Start SSR Throughput|TanStack Start SSR Throughput]] — SSR hot-path optimization case study with strong profiling discipline.
- [[wiki/sources/TanStack Start Middleware|TanStack Start Middleware]] — explicit middleware model for full-stack React workflows.
- [[wiki/sources/TanStack Start Migration Drivers|TanStack Start Migration Drivers]] — reasons teams cite for leaving Next.js for TanStack Start.
- [[wiki/sources/TanStack Start Single-Flight Mutations|TanStack Start Single-Flight Mutations]] — one-round-trip mutation/data refresh pattern in TanStack Start.
- [[wiki/sources/TanStack Query prefer-query-options|TanStack Query prefer-query-options]] — convention-level shift toward colocated query definitions.
- [[wiki/sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]] — rendering internals explainer around Fiber, lanes, and scheduling.

## Syntheses

- [[wiki/syntheses/Next.js vs TanStack Start|Next.js vs TanStack Start]] — first framework comparison synthesis based on the current source base.
- [[wiki/syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]] — comparison of render-time async reads, scheduling, and post-render effects.
- [[wiki/syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]] — comparison between compiler-assisted React optimization and dependency-graph runtime models.
- [[wiki/syntheses/Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries|Testing Modern React - RTL, Browser Mode, RSC, and Integration Boundaries]] — testing synthesis across RTL, browser-realistic component testing, and server/client integration boundaries.
- [[wiki/syntheses/Frameworks as Constraints in the AI Era|Frameworks as Constraints in the AI Era]] — why framework conventions become more valuable as human-and-agent coordination infrastructure.
- [[wiki/syntheses/Designing React Components for Real Environments|Designing React Components for Real Environments]] — synthesis for reusable component APIs under SSR, async rendering, host constraints, and performance pressure.

## System

- [[AGENTS]] — agent operating rules for this vault.
- [[log]] — record of notable updates.
