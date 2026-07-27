---
type: source
status: active
updated: 2026-07-27
tags:
  - react
  - server-components
  - security
  - source
---

# React2DoS

This source captures a denial-of-service vulnerability in the React Flight protocol, adding an important security dimension to the Server Components branch.

## Summary

- The disclosed attack exploited recursive references in Flight deserialization to trigger disproportionate server-side computation.
- The issue affected React Server Components transport logic rather than ordinary client-side rendering.
- The fix changes how Map and Set references are marked as consumed, and affected applications need patched React versions.
- TWIR #291 adds a later Server Functions denial-of-service advisory across React Server Components packages, reinforcing that the server-function/RSC transport layer is a continuing security surface.

## Why This Source Matters

- It makes the `Server Components` page less abstract by grounding it in protocol-level operational risk.
- It is a reminder that custom serialization and transport layers create their own security surface, not just their own developer experience tradeoffs.
- It also improves the Next.js branch indirectly because framework users inherit these lower-level protocol risks.

## Caveats

- This is primarily a security disclosure and patch-oriented source, not a conceptual guide to RSC architecture.
- Version details and mitigation advice are time-sensitive and should be checked against current React security guidance when acting on them.

## Related Pages

- [[../concepts/Server Components|Server Components]]
- [[../tools/Next.js|Next.js]]
- [[../syntheses/Frontend Security Boundaries in Server-First React|Frontend Security Boundaries in Server-First React]]
- [[Next.js Server Actions Security]]
- [[TWIR 277]]
- [[TWIR 291]]

## Raw Sources

- [[../../raw/twir/277/articles/03 - React2DoS (CVE-2026-23869) When the Flight Protocol Crashes at Takeoff|TWIR item note]]
- [[../../raw/twir/277/2026-04-15-TWIR-277|TWIR #277]]
- [[../../raw/twir/291/articles/02 - React - Denial of Service in Server Functions|React - Denial of Service in Server Functions]]
- [[../../raw/twir/291/2026-07-22-TWIR-291|TWIR #291]]
