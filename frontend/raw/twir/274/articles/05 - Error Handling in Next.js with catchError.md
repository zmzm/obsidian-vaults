---
type: twir-item
issue: 274
item: 5
item_type: item
date: 2026-03-25
source: https://aurorascharff.no/posts/error-handling-in-nextjs-with-catch-error
tags:
  - "Nextjs"
  - "ServerComponents"
status: auto
---

[[2026-03-25-TWIR-274|Index]]

# Item 5: Error Handling in Next.js with catchError

Source: [https://aurorascharff.no/posts/error-handling-in-nextjs-with-catch-error](https://aurorascharff.no/posts/error-handling-in-nextjs-with-catch-error)

Summary:
Traditional error boundaries like react-error-boundary have limitations in the Next.js App Router, especially with Server Components and framework-level control flow errors. The new `unstable_catchError` from Next.js provides framework-aware error boundaries that properly handle Next.js-specific errors and support server data refetching on recovery.

Key takeaways:
- react-error-boundary can’t distinguish between user errors and Next.js control flow errors (e.g., notFound, redirect).
- Manual workarounds involve digest checks and router refreshes, but are brittle and require maintenance.
- `unstable_catchError` integrates with Next.js error conventions, supports built-in recovery, and works seamlessly with framework APIs.
- For try/catch in Server Components, `unstable_rethrow` simplifies framework error detection.

Recommendation: Read fully

Related notes: [[Server Components]]
