---
type: topic
status: active
updated: 2026-06-26
tags:
  - react
  - rendering
  - performance
---

# React Rendering

React Rendering is the overview topic for how React updates UI, how rendering models evolve, and how alternative reactive approaches influence current frontend discussions.

## Scope

- Fiber and the React rendering model.
- `startTransition` and update prioritization.
- Signal-like and fine-grained reactive approaches.
- The impact of React Compiler on optimization practices.

## Practical Significance

- This is a useful top-level page for connecting material that would otherwise be split across performance, concurrency, and reactivity.
- It is a good bridge between concepts, tools, and primary sources.

## Current Signals

- The raw layer already includes strong material on `startTransition`, signals-oriented reactivity, and Fiber internals.
- This is enough to justify evolving this page into a central map for rendering and scheduling topics.
- TWIR #273 and #274 also add historical async-rendering context and developer-facing APIs like `use()`.
- TWIR #270 and #272 now add more concrete material on transitions and state update internals.
- The surrounding graph is also now more balanced: rendering links outward to async APIs, client-data models, and framework transport choices instead of only to React internals.
- TWIR #279 adds a clearer React-level explanation of out-of-order server streaming through Suspense placeholders and later content swaps.
- TWIR #218 adds React Scan as a small tooling signal for surfacing unnecessary rerenders during development.
- TWIR #283 and #287 add product-performance evidence around server-first component architecture, local-first perceived latency, styling contracts, and allocation-shape improvements for very large tables.
- TWIR #190, #196, #205, #209, and #210 add the older Suspense sibling-prerendering and prewarming thread that explains why render scheduling can create or avoid data waterfalls.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../concepts/React View Transitions|React View Transitions]]
- [[../concepts/Signals|Signals]]
- [[../concepts/Server Components|Server Components]]
- [[../concepts/React Activity|React Activity]]
- [[../concepts/React Identity and Reconciliation|React Identity and Reconciliation]]
- [[../concepts/React use()|React use()]]
- [[../concepts/React useEffectEvent|React useEffectEvent]]
- [[../tools/Next.js|Next.js]]
- [[../tools/React Router|React Router]]
- [[../tools/TanStack Query|TanStack Query]]
- [[../tools/TanStack DB|TanStack DB]]
- [[SSR Performance]]
- [[../patterns/Client-First Data Sync|Client-First Data Sync]]
- [[../patterns/Effects and Cleanup Discipline|Effects and Cleanup Discipline]]
- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]
- [[../syntheses/React Compiler vs Fine-Grained Reactivity|React Compiler vs Fine-Grained Reactivity]]
- [[../syntheses/Server Components Beyond Next.js|Server Components Beyond Next.js]]
- [[../sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]]
- [[../sources/Async React Evolution|Async React Evolution]]
- [[../sources/How State Updates Work Internally|How State Updates Work Internally]]
- [[../sources/React Key Prop|React Key Prop]]
- [[../sources/React useTransition|React useTransition]]
- [[../sources/React Suspense Prewarming|React Suspense Prewarming]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/React Scan|React Scan]]
- [[../sources/TWIR 283|TWIR 283]]
- [[../sources/TWIR 287|TWIR 287]]
- [[../sources/React Compiler Toolchain Adoption|React Compiler Toolchain Adoption]]
- [[../case-studies/Async React Design Components|Async React Design Components]]
- [[../case-studies/Atomic State in Deep Trees|Atomic State in Deep Trees]]
- [[../case-studies/Building Bulletproof React Components|Building Bulletproof React Components]]
- [[../case-studies/React ProseMirror Performance|React ProseMirror Performance]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[../case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]]
- [[../case-studies/Virtual Scrolling at Massive Scale|Virtual Scrolling at Massive Scale]]
- [[../case-studies/GitHub Diff Performance|GitHub Diff Performance]]
- [[../case-studies/Linear StyleX Migration|Linear StyleX Migration]]
- [[../case-studies/TanStack Table Memory Refactor|TanStack Table Memory Refactor]]

## Sources

- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
- [[../../raw/twir/218/2025-01-22-TWIR-218|TWIR #218]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
- [[../../raw/twir/190/2024-06-19-TWIR-190|TWIR #190]]
- [[../../raw/twir/196/2024-08-14-TWIR-196|TWIR #196]]
- [[../../raw/twir/205/2024-10-16-TWIR-205|TWIR #205]]
- [[../../raw/twir/209/2024-11-13-TWIR-209|TWIR #209]]
- [[../../raw/twir/210/2024-11-20-TWIR-210|TWIR #210]]
- [[../../raw/twir/283/2026-05-27-TWIR-283|TWIR #283]]
- [[../../raw/twir/287/2026-06-24-TWIR-287|TWIR #287]]
- [[../sources/Async React Evolution|Async React Evolution]]
- [[../sources/TanStack DB Query-Driven Sync|TanStack DB Query-Driven Sync]]
- [[../sources/How State Updates Work Internally|How State Updates Work Internally]]
- [[../sources/React Key Prop|React Key Prop]]
- [[../sources/React useTransition|React useTransition]]
- [[../sources/React Suspense Prewarming|React Suspense Prewarming]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]]
- [[../sources/React Out-of-Order Streaming|React Out-of-Order Streaming]]
- [[../sources/React Scan|React Scan]]
- [[../sources/React Compiler Toolchain Adoption|React Compiler Toolchain Adoption]]

## Open Questions

- Which subtopics inside React Rendering should be split into narrower pages.
- Where the boundary should sit between rendering topics and state/reactivity topics.
