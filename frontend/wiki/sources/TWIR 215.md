---
type: source
status: active
updated: 2026-04-30
tags:
  - twir
  - digest
  - nextjs
  - react-forms
---

# TWIR 215

TWIR #215 is an early-2025 digest around component API design, Next.js fit, RSC-backed dashboards, `use()`, and React 19 forms.

## Summary

- The issue includes a component-design source on building dropdowns with flexible triggers, controlled/uncontrolled behavior, keyboard behavior, and accessible composition.
- It adds a client-heavy dashboard migration story away from Next.js toward plain React, TanStack Router, and Rspack.
- It captures a Vercel dashboard example that uses Next.js, RSC, ISR, KV-backed counters, and animated real-time metrics.
- It contributes early React 19 material around replacing thrown promises with `use()` and simplifying forms through action-based patterns.

## Why This Source Matters

- It strengthens the component-design branch with an accessibility-sensitive primitive example.
- It gives the Next.js fit branch another concrete case where framework features were not worth their cost for a dashboard.
- It adds older support for `React use()` and progressive React form patterns that later issues continue to reinforce.

## Caveats

- Some items are tutorial-level and should support broader pages rather than become central pages themselves.
- The Vercel dashboard item is useful as an RSC/Next.js example, but it is also a vendor case study and should be read with that context.

## Related Pages

- [[../patterns/Resilient React Components|Resilient React Components]]
- [[../tools/Next.js|Next.js]]
- [[../concepts/React use()|React use()]]
- [[Progressive React Forms]]
- [[Dropdown Component API]]
- [[../case-studies/ComfyDeploy Off Next.js|ComfyDeploy Off Next.js]]

## Raw Source

- [[../../raw/twir/215/2025-01-02-TWIR-215|2025-01-02-TWIR-215]]
