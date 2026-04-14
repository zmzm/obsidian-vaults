---
type: twir-item
issue: 267
item: 5
item_type: item
date: 2026-02-04
source: https://www.inngest.com/blog/migrating-off-nextjs-tanstack-start
tags:
  - "Nextjs"
  - "TanStack"
  - "ServerComponents"
status: auto
---

[[2026-02-04-TWIR-267|Index]]

# Item 5: Why Inngest migrated off Next.js to TanStack Start

Source: [https://www.inngest.com/blog/migrating-off-nextjs-tanstack-start](https://www.inngest.com/blog/migrating-off-nextjs-tanstack-start)

Summary:
Inngest details their migration from Next.js to TanStack Start, motivated by slow local dev times and high cognitive overhead from Next.js's conventions and RSC model. After evaluating several alternatives, they chose TanStack Start for its explicit routing, faster reloads, and better fit for a small, multi-role team. The migration improved developer experience dramatically, with local load times dropping from 10–12s to 2–3s, and provided clearer architectural boundaries.

Key takeaways:
- Next.js's RSC and conventions can be a poor fit for smaller teams or those not focused exclusively on frontend.
- TanStack Start offers explicit routing, fast local dev, and a more transparent architecture.
- Migration required some refactoring, but resulted in significant productivity and morale gains.
- The article includes practical migration strategies and architectural comparisons.

Recommendation: Read fully (valuable for teams considering alternatives to Next.js or struggling with RSC complexity)

Related notes: [[Server Components]]
