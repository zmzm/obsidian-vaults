---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - nextjs
  - server-functions
  - react-use
---

# TWIR 203

TWIR #203 is an older issue around the Server Actions to Server Functions rename, async Next.js dynamic APIs, `connection()`, environment-variable tooling, React hooks rules, and `use()` data fetching.

## Summary

- The rename from Server Actions to Server Functions clarifies that server-executed functions are broader than form actions.
- Next.js async dynamic APIs and `connection()` continue the request/runtime boundary branch.
- `use()` data fetching, hook rules, local-storage hooks, and date formatting support React correctness and SSR-safety themes.

## Why This Source Matters

- It provides early vocabulary for the server-function branch used throughout the later vault.
- It also supports the distinction between render-time data reads and effect-driven fetching.

## Caveats

- API names from this era should be checked against later stable Next.js and React docs before implementation.

## Related Pages

- [[../concepts/React use()|React use()]]
- [[../concepts/Server Components|Server Components]]
- [[../tools/Next.js|Next.js]]
- [[../sources/Server Functions vs Server Components|Server Functions vs Server Components]]

## Raw Source

- [[../../raw/twir/203/2024-10-01-TWIR-203|2024-10-01-TWIR-203]]
