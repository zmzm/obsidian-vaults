---
type: source
status: active
updated: 2026-04-14
tags:
  - react
  - security
  - trusted-types
  - source
---

# React Trusted Types Integration

This source records React support for Trusted Types and is the key source currently available in the vault for understanding this security-platform compatibility shift.

## Summary

- React now preserves Trusted Types objects rather than coercing them to strings.
- The change affects `dangerouslySetInnerHTML`, HTML and SVG attributes, and URL-like attributes.
- For applications not using Trusted Types, behavior remains effectively unchanged.
- For applications enforcing strict CSP and Trusted Types, the change removes a framework compatibility gap.

## Why This Source Matters

- It turns Trusted Types from a browser-only topic into a React application topic.
- It gives this vault a concrete anchor for discussing secure DOM injection paths.
- It is a good example of framework ergonomics improving through closer alignment with platform security primitives.

## Caveats

- The current raw note is concise and likely sufficient for routing, but not yet deep enough for policy design or implementation guidance.

## Related Pages

- [[../concepts/Trusted Types|Trusted Types]]
- [[../tools/Next.js|Next.js]]

## Raw Sources

- [[../../raw/twir/275/articles/03 - React PR - Enable Trusted Types integration|TWIR item note]]
- [[../../raw/twir/275/2026-04-01-TWIR-275|TWIR #275]]
