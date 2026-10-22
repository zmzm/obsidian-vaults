---
type: case-study
status: active
updated: 2026-10-22
tags: [react, wasm, performance, resource-loading]
---

# Recraft WASM Resource Scheduling

Recraft improved first-canvas rendering by requesting and initializing a large WASM engine earlier, with approximately the same transferred bytes.

## Context

- The extracted account found the engine request behind JS discovery, project-data loading, style loading, and Suspense boundaries. Independent resources had become sequential through component placement.
- Preload hints exposed known URLs early, and moving initialization out of the blocked render path allowed independent work to overlap.
- The reported controlled experiment used about 18,000 users per arm over five days and improved first-canvas timing by 15–19% across the reported percentiles.
- An effect-reported initialization mark could occur after the canvas mark. Instrumentation placement must reflect actual work rather than assume React effect order equals engine readiness.

## Why It Matters

- Inspect resource discovery and dependency waterfalls before treating byte reduction as the only performance lever.
- Earlier fetching has bandwidth and lifetime costs; keep request-scoped or user-specific initialization separate from genuinely shareable resource work.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../sources/React Suspense Prewarming|React Suspense Prewarming]]
- [[../tools/React DevTools|React DevTools]]

## Sources

- [[../../raw/twir/301/articles/08 - How we made a 9 MB WebAssembly module feel faster without removing a single byte|08 - How we made a 9 MB WebAssembly module feel faster without removing a single byte]]

## Open Questions

- Which resource URLs are safe to expose and preload before user data is available?
- How much improvement comes from network overlap versus initialization overlap?
