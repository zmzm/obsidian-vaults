---
type: log
updated: 2026-04-22
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

## [2026-04-16] maintenance | Sync wiki links with refreshed raw TWIR archive

- Rechecked the wiki against the updated raw TWIR archive after broad raw-source changes.
- Fixed stale raw-article links where issue item numbers shifted in TWIR #270.
- Lightly refreshed touched source and case-study pages without changing the overall wiki structure.
- Left the broader wiki architecture intact because the existing concept, tool, pattern, and synthesis layers still fit the expanded raw base.

## [2026-04-16] synthesis | New syntheses for testing, framework constraints, and component design

- Added a testing synthesis connecting RTL, browser-mode component testing, async RSC testing limits, and route-level integration boundaries.
- Added a framework synthesis connecting Next.js agentic direction, host-environment integration, and the value of conventions in AI-assisted work.
- Added a component-design synthesis connecting resilient component APIs, async-aware design, host constraints, and performance-sensitive integrations.
- Linked the new syntheses back into the index plus the existing `Testing Strategy for React Apps`, `Resilient React Components`, and `Next.js` hubs.

## [2026-04-16] ingest | Targeted pass over testing and AI/framework branches

- Added source pages for async RSC testing limits, Vitest Browser Mode, and Next.js workflow skills.
- Added a case study for a 6000-test AI-assisted migration to capture where codemods, migration guides, and validation gates made agentic work reliable.
- Rewired the new testing synthesis and pattern pages to use these stronger sources instead of depending mostly on raw notes.
- Strengthened the framework-constraints branch with supporting evidence that Next.js knowledge is being packaged directly for agent workflows.

## [2026-04-16] ingest | Component-design support pass

- Added a case study for `Building a Toast Component` to capture how interaction design, motion, and developer experience shape reusable UI primitives.
- Added `React Component API Game` as a light API-design source to support the maintainability side of component authoring.
- Rewired the component-design synthesis and resilience pattern to include these signals instead of depending only on SSR- and performance-heavy examples.

## [2026-04-20] maintenance | Clean TWIR 240-253: remove broken and useless articles

- Scanned all 14 TWIR issues (240-253), totaling ~146 articles.
- All articles had broken content extraction (Python clipper missing `lxml_html_clean`). Evaluated each on summary quality and topic relevance instead.
- Removed 59 articles classified as: sponsored/promotional content (Strapi, PostHog), clickbait rants (React is Awful, I tried Solid.js now I hate React, etc.), off-topic material (Three.js/WebGL, Astro, Telegram bots, Rive, ViteLand), outdated event announcements (Next.js Conf CFP, conference lists), thin tutorials (Stripe in 5 minutes, hooks from scratch, SEO guidelines), podcasts without substance, monthly recap duplicates, and niche items with no wiki path (Clojure RSC, valtio-reactive).
- Updated all 14 TWIR index files to remove references to deleted articles and cleaned up TL;DR and Action Items sections.
- Kept 87 articles covering: React core PRs (cacheSignal, Activity, Fragment refs, ViewTransition, useEffectEvent), React Compiler progress, Next.js releases and PRs, TanStack Start and TanStack DB, React Router evolution, Server Components patterns, testing strategy, SSR/self-hosting, and framework ecosystem shifts.
- No wiki pages or index.md referenced TWIR 240-253 articles, so no cross-layer link updates were needed.

## [2026-04-21] ingest | Broadened archive coverage and new issue pass

- Added detailed digest pages for every previously missing TWIR issue from #219 through #265, plus new digest pages for TWIR #276 and #277.
- Promoted new source pages for the Precompute pattern, TanStack's RSC-as-data-streams framing, React2DoS, Next.js Node.js stream work, React Router callsite revalidation, and custom ESLint rules.
- Added new case studies for Railway's migration off Next.js and GitHub's diff rendering performance work.
- Next sensible step: use the newly indexed issue layer to promote more individual articles into source, case-study, or synthesis pages where repetition justifies it.

## [2026-04-21] lint | Reconnect new archive and issue pages into the wiki graph

- Updated the global index so the full issue-level TWIR layer, new sources, and new case studies are navigable from the vault map.
- Rewired Next.js, Server Components, TanStack Start, React Router, rendering, caching, safety, and comparison pages to absorb the new material.
- Expanded the lint branch beyond type-only safety by connecting custom ESLint rules and effect-discipline enforcement back into the main graph.

## [2026-04-21] ingest | Promote repeated themes from TWIR 219-254

- Added durable pages for `TanStack DB`, `React Activity`, `React Router Middleware`, `Next.js Middleware Bypass`, and `Server Components Beyond Next.js`.
- Upgraded the data, routing, rendering, testing, and framework branches so repeated archive signals are no longer trapped inside issue summaries.
- Used the newly indexed TWIR layer as support rather than as an endpoint, promoting only themes with repeated cross-issue evidence.

## [2026-04-21] ingest | Promote transition, testing, and portability branches

- Added durable pages for `React View Transitions`, `Storybook`, and `Next.js Deployment Adapters`.
- Rewired rendering, testing, and framework pages so these themes now sit in the main graph instead of living only in archive issue summaries.
- Used repetition across multiple TWIR issues as the threshold for promotion rather than one especially interesting article.

## [2026-04-21] ingest | Tighten async cache, action security, and Storybook testing branches

- Added supporting source pages for `React cacheSignal`, `Next.js Server Actions Security`, and `Storybook Component Testing`.
- Rewired `React use()`, `Next.js`, `Storybook`, and `Testing Strategy for React Apps` so these recurring ideas no longer depend on issue pages alone.
- Used this pass to connect low-level async cache lifecycle, public action boundaries, and story-driven component testing back into the main wiki graph.

## [2026-04-21] ingest | Promote effect API and Next.js portability synthesis

- Added `React useEffectEvent` as a dedicated concept page instead of leaving the API buried inside release summaries and the broader effects pattern.
- Added `Next.js Portability Boundaries` as a synthesis page connecting adapters, non-Vercel metadata breakage, and host-level stream/runtime friction.
- Rewired `React Rendering`, `Effects and Cleanup Discipline`, `Next.js`, `Next.js Deployment Adapters`, and supporting TWIR issue pages so both branches sit inside the main graph.

## [2026-04-22] ingest | Deepen portability branch with host-specific supporting pages

- Added `Next.js Metadata Streaming Portability` as a supporting source page for the non-Vercel metadata and SEO failure mode.
- Added `Next.js Host Runtime Friction` as a case study tying Cloudflare/OpenNext runtime behavior, stream adapters, and SSR hot-path costs together.
- Rewired `Next.js`, `SSR Performance`, `Next.js Deployment Adapters`, `Next.js Node.js Streams for RSC`, the portability synthesis, and the global index so the portability branch now has real supporting structure below the synthesis layer.

## [2026-04-22] ingest | Split typed routing from generic type safety

- Added `URL State Safety` as a supporting source page for schema-aware search params, write throttling, and migration-minded URL state.
- Added `Typed Routing and URL State` as a dedicated pattern page connecting route manifests, typed links, validated search params, and route-tree inheritance across Next.js, React Router, and TanStack Router.
- Rewired `Type-Driven Frontend Safety`, `React Router`, `TanStack Start`, `Next.js`, `React Router Type Safety`, and the global index so routing safety no longer sits buried inside generic typing guidance.

## [2026-04-22] ingest | Separate component confidence from generic testing advice

- Added `Component Confidence Boundaries` as a dedicated pattern page for story-driven coverage, browser-realistic component tests, and the limits of component-level confidence.
- Rewired `Testing Strategy for React Apps`, `Storybook`, `Storybook Component Testing`, `Vitest Browser Mode`, and the global index so this branch is no longer flattened into one generic testing page.
- Used Storybook 9, Storybook coverage, Vitest Browser Mode, shift-left testing practice, and accessibility-oriented selector guidance as the supporting signal set.

## [2026-04-22] ingest | Deepen TanStack DB into sync-model pages

- Added `TanStack DB Query-Driven Sync` as a supporting source page for live-query maintenance, normalized collections, and API-facing query pushdown.
- Added `Client-First Data Sync` as a dedicated pattern page connecting sync-engine thinking, local-first UX, TanStack DB, and the limits of plain query-cache architectures.
- Rewired `TanStack DB`, `TanStack Query`, `TanStack Start`, and the global index so the data-sync branch now has a clearer model layer instead of one tool page carrying the whole argument.

## [2026-04-22] structure | Rebalance overloaded framework and rendering hubs

- Trimmed issue-heavy and loosely related links out of the most crowded hub pages so they point more consistently at durable concepts, patterns, sources, and case studies.
- Reframed `Next.js`, `TanStack Start`, `TanStack Query`, `React Router`, and `React Rendering` so the broad hubs behave more like routers and less like mixed summary pages.
- Next sensible step: normalize the global index if it starts flattening too many branches into one long page again.

## [2026-04-22] structure | Separate framework-hub responsibilities more clearly

- Reframed `Next.js` around platform surface, runtime direction, portability, security, and caching rather than letting migration stories dominate the hub.
- Reframed `TanStack Start` around explicit middleware, routing, mutation, and sync-model primitives rather than treating it mainly as the anti-Next.js branch.
- Kept direct comparison and migration material linked, but pushed it back down into synthesis and case-study pages where tradeoff arguments belong.

## [2026-04-22] structure | Normalize the global index

- Split the overloaded `Case Studies` section into framework-fit, architecture/performance, and testing/migration blocks.
- Replaced the flat `Sources` list with grouped issue-digest ranges plus thematic source clusters for frameworks, runtime/rendering, and data/testing/safety.
- Kept direct links to every `TWIR 219-277` digest while making the index materially shorter and easier to scan.

## [2026-04-22] lint | Backlink audit for second-order orphans

- Audited pages that were reachable from `index.md` but still weakly embedded in thematic pages.
- Reconnected weaker article-level nodes across query authoring, routing, rendering, security, and AI/framework branches.
- Kept this pass focused on durable article-level wiring instead of inflating the already large issue-digest layer.
