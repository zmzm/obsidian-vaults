---
type: twir-item
issue: 304
item: 6
item_type: item
date: 2026-11-04
source: https://github.com/vercel/next.js/pull/100850
tags:
  - "Nextjs"
  - "PR"
status: auto
quality: keep
---

[[2026-11-04-TWIR-304|Index]]

# Item 6: Next.js PR - create-next-app always uses the App Router, no router choice prompt

Source: [https://github.com/vercel/next.js/pull/100850](https://github.com/vercel/next.js/pull/100850)

Summary:
create-next-app now defaults to using the App Router for all new projects, removing the interactive prompt that previously allowed users to select the Pages Router. The change simplifies project setup and eliminates accidental selection of the older routing system, though an explicit --no-app flag still allows opting out.

Key takeaways:
- App Router is now the default for all new Next.js projects.
- The router choice prompt and saved preferences are removed.
- --no-app remains for explicit opt-out; Pages Router templates are still available.
- Documentation and tests updated to reflect the new default.

Recommendation:
Summary sufficient

Content:
# remove App Router prompt and always use App Router by timneutkens · Pull Request #100850 · vercel/next.js · GitHub

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)](/apps/github-actions)

[github-actions](/apps/github-actions)
Bot
added
[create-next-app](/vercel/next.js/issues?q=state%3Aopen%20label%3Acreate-next-app)

Related to our CLI tool for quickly starting a new Next.js application.

[created-by: Turbopack team](/vercel/next.js/issues?q=state%3Aopen%20label%3A%22created-by%3A%20Turbopack%20team%22)

PRs by the Turbopack team.

[Documentation](/vercel/next.js/issues?q=state%3Aopen%20label%3ADocumentation)

Related to Next.js' official documentation.

[tests](/vercel/next.js/issues?q=state%3Aopen%20label%3Atests)
labels
[Oct 28, 2026](#event-34508287192)
