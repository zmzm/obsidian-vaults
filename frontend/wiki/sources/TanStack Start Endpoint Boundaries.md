---
type: source
status: active
updated: 2026-06-26
tags:
  - tanstack-start
  - security
  - server-functions
  - source
---

# TanStack Start Endpoint Boundaries

This source captures the security model for TanStack Start server functions: route guards are user-experience controls, while server functions are public HTTP endpoints that need their own authorization.

## Summary

- `beforeLoad` and similar route guards can protect navigation flow, but they do not secure server functions from direct calls.
- Each `createServerFn` behaves like an endpoint and must validate identity, permissions, and input at that boundary.
- Middleware can centralize repeated authentication and authorization checks, but the endpoint remains the security boundary.

## Why This Source Matters

- It gives the `TanStack Start` hub a concrete production-safety rule instead of only framework ergonomics.
- It mirrors the broader React framework lesson that server APIs exposed from frontend code are still network-facing surfaces.
- It connects routing, server functions, and security without forcing the topic into a generic auth page.

## Caveats

- The source is from an auth vendor, so the general boundary model is more durable than any product-specific implementation detail.
- Specific APIs may change as TanStack Start matures.

## Related Pages

- [[../tools/TanStack Start|TanStack Start]]
- [[../tools/React Router|React Router]]
- [[Server Functions vs Server Components]]
- [[Next.js Server Actions Security]]

## Raw Sources

- [[../../raw/twir/284/articles/05 - TanStack Start authentication A developer's guide for 2026|TWIR item note]]
- [[../../raw/twir/284/2026-06-03-TWIR-284|TWIR #284]]
