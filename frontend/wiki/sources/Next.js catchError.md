---
type: source
status: active
updated: 2026-04-14
tags:
  - nextjs
  - error-handling
  - source
---

# Next.js catchError

This source captures why framework-aware error handling matters in the Next.js App Router model.

## Summary

- Traditional error boundary helpers struggle with Next.js control-flow errors such as `notFound()` and `redirect()`.
- `unstable_catchError` is designed to integrate with Next.js conventions instead of treating those flows as ordinary user errors.
- The source also highlights recovery behavior and server-data refresh patterns that are difficult to express with generic React error handling utilities.

## Why This Source Matters

- It adds a framework-specific error-handling perspective to the `Next.js` page.
- It is a good example of how App Router architecture creates APIs that do not map cleanly to generic React abstractions.

## Caveats

- The API discussed here is explicitly unstable and may change.

## Related Pages

- [[../tools/Next.js|Next.js]]
- [[../concepts/Server Components|Server Components]]

## Raw Sources

- [[../../raw/twir/274/articles/05 - Error Handling in Next.js with catchError|TWIR item note]]
- [[../../raw/twir/274/2026-03-25-TWIR-274|TWIR #274]]
