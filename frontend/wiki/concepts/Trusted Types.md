---
type: concept
status: active
updated: 2026-04-14
tags:
  - security
  - browser
  - xss
---

# Trusted Types

Trusted Types are a browser security mechanism that restricts dangerous DOM sinks and helps reduce the risk of DOM-based XSS.

## Key Ideas

- Instead of freely passing strings into sensitive DOM APIs, the platform introduces typed trusted values.
- Trusted Types support in React matters as a bridge between the framework layer and the browser security model.
- This topic sits at the intersection of security and framework ergonomics.

## Practical Significance

- It is useful for understanding safer integration patterns for user-provided HTML and third-party content.
- It is worth tracking in the context of React APIs and browser platform evolution.

## Current Signals

- The current raw layer already contains a concrete React integration source, which is enough to treat this as an active concept rather than just a placeholder.
- Even though this branch is still smaller than the rendering and framework branches, it now has a clearer place inside a broader frontend-safety cluster.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../topics/React Rendering|React Rendering]]
- [[../patterns/Type-Driven Frontend Safety|Type-Driven Frontend Safety]]
- [[../sources/React Trusted Types Integration|React Trusted Types Integration]]

## Sources

- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
- [[../sources/React Trusted Types Integration|React Trusted Types Integration]]

## Open Questions

- Which React APIs and real-world scenarios benefit most from this integration.
- How this may affect libraries that work with HTML injection paths.
