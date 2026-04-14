---
type: log
updated: 2026-04-14
status: active
---

# Log

## [2026-04-10] setup | Initial LLM Wiki scaffold

- Created a split between `raw/`, `wiki/`, and `system/`.
- Moved the existing `TWIR` directory into `raw/twir/`.
- Added `AGENTS.md`, `index.md`, and the first wiki hubs.
- Next sensible step: create the first `source` pages and connect them to concepts and tools.

## [2026-04-14] ingest | First source pages from TWIR 275

- Evaluated the current `raw` layer as useful curated source material with good routing value.
- Added first normalized `source` pages for TWIR #275, React Compiler Rust port, React Trusted Types integration, TanStack Query `prefer-query-options`, and a React Fiber rendering explainer.
- Updated concept, tool, and topic hubs to reference concrete sources from the raw layer.
- Next sensible step: repeat this pass for TWIR #273 and #274, then start splitting `React Rendering` into narrower subtopics.

## [2026-04-14] ingest | Source pass over TWIR 273 and 274

- Added normalized `source` pages for TWIR #273 and #274 plus high-value items on custom RSC frameworks, Async React evolution, Next.js 16.2, `use cache` with `next-intl`, `use()`, and React Router type safety.
- Added new durable hubs for `Server Components` and `React Router`.
- Upgraded `Next.js` and `React Rendering` from seed pages to active topic hubs with stronger source grounding.
- Next sensible step: split out narrower pages for `use()`, caching, and typed routing patterns, or backfill more source coverage from the remaining TWIR items.

## [2026-04-14] ingest | Source coverage expansion for rendering and SSR

- Added `SSR Performance` as a new topic hub.
- Added source pages for React key handling, Next.js `catchError`, and TanStack Start SSR throughput.
- Connected these sources back into `React Rendering`, `Server Components`, and `Next.js`.
- Next sensible step: create dedicated concept or pattern pages for `use()`, caching, and React identity if those themes keep recurring in future sources.

## [2026-04-14] structure | New intermediate concept and pattern nodes

- Added `React use()` as a dedicated concept node between rendering, Suspense-style async flow, and framework usage.
- Added `Caching in App Router` as a dedicated pattern page for Next.js cacheability and request-time constraints.
- Rewired existing topic, concept, tool, and source pages to route through these intermediate nodes.
- Next sensible step: add `React Identity and Reconciliation` if key/state-identity material continues to recur.

## [2026-04-14] structure | React identity node

- Added `React Identity and Reconciliation` as a new concept node.
- Reconnected `React Key Prop`, Fiber rendering, and async rendering sources through this concept.
- Reduced pressure on `React Rendering` by moving reconciliation and identity into a more specific intermediate layer.
- Next sensible step: either deepen this area with state-preservation examples or continue building out additional durable concepts only when multiple sources support them.

## [2026-04-14] ingest | Expanded raw coverage from TWIR 268-272

- Evaluated the new `raw` additions and treated them as high-value support for existing hubs rather than as a reason to create many new top-level nodes.
- Added digest routing pages for TWIR #268 through #272.
- Added high-signal source pages for enterprise Next.js architecture, agent-facing Next.js direction, query abstractions, React Router integration points, transition usage, state update internals, and compiler-model boundaries.
- Updated `Next.js`, `TanStack Query`, `React Router`, `React Rendering`, `React Compiler`, `React Identity and Reconciliation`, and `Caching in App Router` with the new source support.

## [2026-04-14] synthesis | First framework comparison

- Added the first synthesis page: `Next.js vs TanStack Start`.
- Framed the comparison around platform breadth, explicit architecture, SSR performance, and Server Components ergonomics.
- Linked the synthesis back into `Next.js`, `SSR Performance`, and the global index.
- Next sensible step: add more synthesis pages only where the source base is already multi-source and asymmetric tradeoffs are visible.

## [2026-04-14] synthesis | Async React pattern comparison

- Added `Async React Patterns - use() vs useTransition vs useEffect`.
- Framed the comparison around render-time async reads, scheduling, and post-render side effects rather than treating the APIs as interchangeable.
- Explicitly noted that the current evidence for `useEffect` in the vault is weaker than for `use()` and `useTransition`.
- Linked the synthesis back into `React use()`, `React Rendering`, and the global index.

## [2026-04-14] synthesis | Compiler model comparison

- Added `React Compiler vs Fine-Grained Reactivity`.
- Framed the comparison around optimization within React's model versus a different runtime model built around dependency-level updates.
- Promoted `React Compiler` and `Signals` to active concept pages now that they are supported by a stronger comparative source base.
- Linked the synthesis back into `React Compiler`, `Signals`, `React Rendering`, and the global index.

## [2026-04-14] ingest | Caching and RSC performance branch

- Added routing pages for TWIR #255 and TWIR #257 because they materially strengthen the App Router caching branch.
- Added source pages for `Next.js 16`, `Partial Prerendering Architecture`, and `RSC Performance Tradeoffs`.
- Updated `Caching in App Router`, `Server Components`, `SSR Performance`, and `Next.js` with the stronger evidence base.
- Refined the framework comparison by noting that the Next.js side now has better support on caching and platform architecture.

## [2026-04-14] ingest | TanStack Start comparison branch

- Added a dedicated `TanStack Start` tool hub because the framework comparison branch now has enough independent evidence to justify it.
- Added routing pages for TWIR #256, #266, and #267.
- Added source pages for `TanStack Start Middleware`, `TanStack Start Migration Drivers`, and `TanStack Start Single-Flight Mutations`.
- Updated `Next.js vs TanStack Start`, `Next.js`, `TanStack Query`, and `SSR Performance` with stronger TanStack Start evidence.

## [2026-04-14] structure | Case-study layer and missed-article pass

- Added `wiki/case-studies/` as a new durable layer for interesting engineering practice that does not need to become a central hub.
- Updated `AGENTS.md` to distinguish core knowledge, case studies, and raw-only reference material.
- Reviewed TWIR issues from #275 back to #255 and promoted several missed but worthwhile articles into case studies instead of forcing them into core concept pages.
- Added first case studies for App Router exit, Next.js inside ChatGPT, async design components, React ProseMirror performance, frontend memory leaks, and Enzyme-to-RTL migration.

## [2026-04-14] ingest | Second case-study pass over TWIR 255-275

- Re-reviewed the TWIR archive specifically for engineering stories that were useful but too low-centrality for the core wiki layer.
- Added case studies for atomic state in deep trees, compiler silent failures, bulletproof component design, RSC error rendering, framework conventions in AI-assisted work, safer typing without `React.FC`, and virtual scrolling at massive scale.
- Linked the strongest new case studies back into `React Compiler`, `Server Components`, `React Rendering`, and `Next.js` so they support the graph instead of staying isolated.
- Left thin or mostly descriptive articles in `raw/` when they did not yet carry a strong operational lesson.

## [2026-04-14] lint | Connectivity audit and intermediate pattern pages

- Audited inbound-link strength across the wiki and found that several case studies were too dependent on broad hubs such as `React Rendering` and `Next.js`.
- Added `Effects and Cleanup Discipline` and `Resilient React Components` as intermediate pattern pages to give weaker case studies clearer landing zones.
- Rewired relevant concept, tool, synthesis, and case-study pages through these new patterns.
- Remaining weak spots now center mostly on the testing and frontend-safety branch rather than on rendering or component resilience.

## [2026-04-14] lint | Testing and safety branch pass

- Added `Testing Strategy for React Apps` to give testing migrations, browser-based component testing, and async RSC testing a shared landing page.
- Added `Type-Driven Frontend Safety` to connect route typing, safer component signatures, and codebase-wide reliability migrations.
- Rewired `Enzyme to RTL Migration`, `Safer Frontend without React.FC`, `React Router`, and `Trusted Types` so the testing and safety branch is no longer mostly isolated.
- Promoted `Trusted Types` to active now that it sits inside a clearer safety cluster instead of a single-source island.
