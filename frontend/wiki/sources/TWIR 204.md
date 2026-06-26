---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - nextjs
  - server-actions
  - vite
---

# TWIR 204

TWIR #204 is an older issue around Meta's React usage, Next.js 15 canary breaking changes, serverless server concurrency, server-action mechanics, Vite environment APIs, and server-side React mental models.

## Summary

- Next.js canary changes continue the async request API migration branch.
- Serverless server concurrency adds runtime and hosting context for new React architecture.
- Server Actions mechanics and `useActionState` validation patterns support progressive forms and server-function pages.
- Vite environment APIs and "React on the server is not PHP" broaden framework architecture discussion.

## Why This Source Matters

- It gives older support for the operational cost of React's server architecture: request APIs, deployment model, and concurrency behavior all matter.

## Caveats

- Several items describe canary-stage behavior and should be treated historically.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../sources/Progressive React Forms|Progressive React Forms]]
- [[../concepts/Server Components|Server Components]]
- [[../topics/SSR Performance|SSR Performance]]

## Raw Source

- [[../../raw/twir/204/2024-10-09-TWIR-204|2024-10-09-TWIR-204]]
