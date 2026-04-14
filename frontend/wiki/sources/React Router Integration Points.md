---
type: source
status: active
updated: 2026-04-14
tags:
  - react-router
  - loaders
  - actions
  - source
---

# React Router Integration Points

This source frames React Router loaders and actions as integration boundaries rather than places to store business logic.

## Summary

- Loaders and actions should act as glue between transport concerns and business logic.
- Business logic should be tested separately, with only thin direct tests for route-level integration.
- The framing encourages route modules that are easier to test and maintain.

## Why This Source Matters

- It adds an architectural/testing perspective to the `React Router` page.
- It makes the router page more than a type-safety hub by connecting it to application structure and testing design.

## Caveats

- The advice is strongest when teams already separate business logic cleanly from routing layers.

## Related Pages

- [[../tools/React Router|React Router]]
- [[../sources/TWIR 270|TWIR 270]]

## Raw Sources

- [[../../raw/twir/270/articles/08 - React Router Loaders and Actions as Integration Points|TWIR item note]]
- [[../../raw/twir/270/2026-02-25-TWIR-270|TWIR #270]]
