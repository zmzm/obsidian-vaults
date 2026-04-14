---
type: twir-item
issue: 259
item: 5
item_type: item
date: 2025-11-19
source: https://github.com/vercel/next.js/pull/86120
tags:
  - "Nextjs"
  - "PR"
  - "CLI"
status: auto
quality: keep
---

[[2025-11-19-TWIR-259|Index]]

# Item 5: Next.js PR - New next upgrade CLI command

Source: [https://github.com/vercel/next.js/pull/86120](https://github.com/vercel/next.js/pull/86120)

Summary:
The next upgrade command is a convenience alias for running @next/codemod@canary upgrade, using the current package manager. It simplifies upgrading Next.js projects and codemods, defaulting to stable canary codemods, and is intended to make upgrades more accessible and consistent.

Key takeaways:
- next upgrade streamlines the upgrade process for Next.js and related codemods.
- Uses the package manager invoked (e.g., pnpm, yarn, npm).
- Defaults to canary codemods, which are considered stable for this purpose.

Recommendation:
Summary sufficient

Content:
# [next-upgrade] Add `next upgrade` by eps1lon · Pull Request #86120 · vercel/next.js · GitHub

[![@eps1lon](https://avatars.githubusercontent.com/u/12292047?s=40&u=d1523888bc16deb2ce9f5294e4849d1a2f02270c&v=4)](/eps1lon)
[eps1lon](/eps1lon)

changed the base branch from

sebbie/11-14-\_next-upgrade\_force\_install\_of\_dev\_dependencies

to

canary
[November 14, 2025 19:00](#event-20950547997)
