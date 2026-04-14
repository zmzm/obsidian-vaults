---
type: twir-item
issue: 275
item: 1
item_type: featured
date: 2026-04-01
source: https://nextjs.org/blog/nextjs-across-platforms
tags:
  - "Nextjs"
  - "OpenNext"
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 1: Next.js Across Platforms: Adapters, OpenNext, and Our Commitments

Source: [https://nextjs.org/blog/nextjs-across-platforms](https://nextjs.org/blog/nextjs-across-platforms)

Summary:
Next.js 16.2 introduces a stable Adapter API, a public adapter test suite, and a working group to standardize deployment across platforms. The Adapter API provides a typed, versioned interface for platform providers, enabling consistent integration and deployment. OpenNext played a pivotal role in bridging gaps between Next.js and hosting providers, leading to open collaboration and verified adapters. The new test suite and working group ensure ongoing compatibility and transparency for all ecosystem participants.

Key takeaways:
- The Adapter API formalizes the contract between Next.js and deployment platforms, supporting multi-provider, multi-tenant scenarios.
- Verified adapters must be open source and pass the shared test suite; Vercel, Bun, and others are available or in development.
- The test suite ensures feature parity and correctness across all adapters, not just Vercel.
- The Ecosystem Working Group provides early visibility and coordination for breaking changes and new features.

Recommendation: Read fully (especially for those deploying Next.js across diverse infrastructures or building custom adapters)
