---
type: topic
status: active
updated: 2026-04-22
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
- [[../sources/React use Hook|React use Hook]]
- [[../case-studies/Async React Design Components|Async React Design Components]]
- [[../case-studies/Atomic State in Deep Trees|Atomic State in Deep Trees]]
- [[../case-studies/Building Bulletproof React Components|Building Bulletproof React Components]]
- [[../case-studies/React ProseMirror Performance|React ProseMirror Performance]]
- [[../case-studies/React Compiler Silent Failures|React Compiler Silent Failures]]
- [[../case-studies/Frontend Memory Leaks at Scale|Frontend Memory Leaks at Scale]]
- [[../case-studies/Virtual Scrolling at Massive Scale|Virtual Scrolling at Massive Scale]]
- [[../case-studies/GitHub Diff Performance|GitHub Diff Performance]]

## Sources

- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
- [[../../raw/twir/272/2026-03-11-TWIR-272|TWIR #272]]
- [[../../raw/twir/273/2026-03-18-TWIR-273|TWIR #273]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/Async React Evolution|Async React Evolution]]
- [[../sources/TanStack DB Query-Driven Sync|TanStack DB Query-Driven Sync]]
- [[../sources/How State Updates Work Internally|How State Updates Work Internally]]
- [[../sources/React Key Prop|React Key Prop]]
- [[../sources/React useTransition|React useTransition]]
- [[../sources/React use Hook|React use Hook]]
- [[../sources/How React Fiber Renders Your UI|How React Fiber Renders Your UI]]

## Open Questions

- Which subtopics inside React Rendering should be split into narrower pages.
- Where the boundary should sit between rendering topics and state/reactivity topics.
