---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - nextjs
  - suspense
  - server-actions
---

# TWIR 205

TWIR #205 is a strong old issue around Next.js 15 RC2, non-blocking React prerendering, request interceptors, `useActionState`, headless UI critiques, and RSC waterfall problems.

## Summary

- Next.js 15 RC2 captures Turbopack, async request APIs, server action security, and upgrade tooling.
- React re-landing non-blocking prerendering continues the Suspense/prewarming thread from #190 and #196.
- Request Interceptors, server-action helpers, and RSC waterfall discussion deepen the framework-boundary branch.

## Why This Source Matters

- It links React core rendering changes directly to Next.js platform evolution.
- It adds early support for the idea that server-side React can create waterfalls unless teams design data flow carefully.

## Caveats

- Some Next.js RC details may have changed by stable release.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../topics/React Rendering|React Rendering]]
- [[../concepts/Server Components|Server Components]]
- [[../patterns/Caching in App Router|Caching in App Router]]

## Raw Source

- [[../../raw/twir/205/2024-10-16-TWIR-205|2024-10-16-TWIR-205]]
