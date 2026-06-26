---
type: source
status: active
updated: 2026-06-26
tags:
  - twir
  - digest
  - nextjs
  - security
  - ppr
---

# TWIR 202

TWIR #202 is an older Next.js-heavy issue around async dynamic APIs, cache poisoning, Cloudflare PPR, URL-controlled state, and migration tooling.

## Summary

- Next.js dynamic APIs moving async foreshadow the App Router request-boundary changes that later become stable.
- A cache-poisoning vulnerability adds security context to Next.js framework behavior.
- PPR on Cloudflare Workers, content visibility, and Parcel-to-Vite migration material support portability and performance branches.

## Why This Source Matters

- It is an early anchor for Next.js 15 request API changes and portability work around PPR.
- It also adds security evidence before later middleware and RSC protocol incidents.

## Caveats

- Version-specific vulnerability and migration details are time-sensitive.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../patterns/Typed Routing and URL State|Typed Routing and URL State]]
- [[../topics/SSR Performance|SSR Performance]]
- [[../syntheses/Next.js Portability Boundaries|Next.js Portability Boundaries]]

## Raw Source

- [[../../raw/twir/202/2024-09-25-TWIR-202|2024-09-25-TWIR-202]]
