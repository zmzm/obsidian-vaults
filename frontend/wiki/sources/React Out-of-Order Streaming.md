---
type: source
status: active
updated: 2026-04-30
tags:
  - react
  - streaming
  - ssr
  - suspense
---

# React Out-of-Order Streaming

This source explains how React server rendering can stream UI chunks as data becomes ready while still preserving the intended final UI order.

## Summary

- React does not need to stream every server-rendered component strictly in DOM order.
- Suspense boundaries provide placeholders that let available UI reach the browser while slower async work resolves later.
- Resolved content can be delivered through later templates/scripts and swapped into the correct place in the UI.
- The mechanism improves perceived latency but makes SSR debugging and performance reasoning more dependent on Suspense boundaries and stream semantics.

## Why This Source Matters

- It gives the `React Rendering` and `SSR Performance` branches a concrete explanation of streaming mechanics instead of only high-level RSC framing.
- It supports `Server Components` by showing why stream transport and placeholder coordination are central to the model.
- It complements Next.js stream-pipeline sources: one explains React-level behavior, the other explains framework/runtime stream plumbing.

## Caveats

- The source is explanatory rather than a primary implementation document.
- Framework behavior can differ depending on routing, cache, and deployment pipeline choices around React's underlying streaming model.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../concepts/Server Components|Server Components]]
- [[Next.js Node.js Streams for RSC]]
- [[TWIR 279]]

## Raw Sources

- [[../../raw/twir/279/articles/04 - How React streams UI out of order and still manages to keep order|How React streams UI out of order and still manages to keep order]]
- [[../../raw/twir/279/2026-04-29-TWIR-279|TWIR #279]]
