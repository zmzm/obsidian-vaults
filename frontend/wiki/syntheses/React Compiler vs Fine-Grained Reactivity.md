---
type: synthesis
status: active
evidence: mixed
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [react-compiler, signals, reactivity, comparison]
---

# React Compiler vs Fine-Grained Reactivity

This comparison separates compiler-generated reuse from dependency-level subscriptions while allowing both to coexist inside a React application.

## Short Thesis

Compiler optimization and fine-grained subscriptions answer different questions: which computations can be reused, and which consumers should be notified. A library can combine them; they are not necessarily exclusive framework choices.

## What the Evidence Supports

- The extracted compiler adoption account shows build integration, diagnostic/version alignment, and workload-specific build improvements. Faster compilation is separate from faster UI interactions.
- The extracted context example distinguishes broad consumer invalidation from expensive child work. Narrow derived props and compiler or memo reuse can reduce downstream work without introducing a context-selector API.
- The MobX integration PR illustrates a compatibility seam: automatic observer wrapping and compiler opt-outs are proposed so dependency tracking retains ownership. Proposal status does not establish every integration’s current behavior.
- Fine-grained subscriptions in a React library can limit notifications while React still owns rendering and scheduling. A signals implementation inside a library is not evidence that the whole app changed runtime models.

## Practical Significance

- Measure notification count, expensive component work, commits, and user-perceived latency separately before selecting an optimization.
- For an existing React application, check purity, bailouts, third-party tracking, and compiler/toolchain versions before attributing missed optimization to React’s entire runtime.
- For external stores, evaluate subscription granularity together with concurrency and consistency behavior; fewer rerenders alone do not establish correctness.

## Evidence Limits

The archive has stronger compiler implementation and adoption evidence than controlled comparisons with any single signals runtime. Conceptual simplicity and performance superiority cannot be ranked from these sources alone.

## Related Pages

- [[../concepts/React Compiler|React Compiler]]
- [[../concepts/Signals|Signals]]
- [[../topics/React Rendering|React Rendering]]
- [[../sources/React Compiler Toolchain Adoption|React Compiler Toolchain Adoption]]
- [[../sources/React Compiler Production Memoization|React Compiler Production Memoization]]
- [[../case-studies/TanStack Table Memory Refactor|TanStack Table Memory Refactor]]

## Sources

- [[../../raw/twir/296/articles/06 - React Now Rusted All The Way Out|06 - React Now Rusted All The Way Out]]
- [[../../raw/twir/300/articles/06 - Making React Context Cheap with React Compiler|06 - Making React Context Cheap with React Compiler]]
- [[../../raw/twir/301/articles/03 - MobX PR - MobX React plugin|03 - MobX PR - MobX React plugin]]
- [[../../raw/twir/291/articles/07 - Inside TanStack Table V9 Reactivity|07 - Inside TanStack Table V9 Reactivity]] — retained supporting reactivity reference; verify extraction before detailed implementation claims.

## Open Questions

- How much measured work comes from subscriptions, component execution, DOM commit, or unrelated computation?
- Which tracking libraries safely combine their ownership rules with compiler-generated reuse?
