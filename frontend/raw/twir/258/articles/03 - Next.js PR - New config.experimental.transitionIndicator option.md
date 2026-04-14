---
type: twir-item
issue: 258
item: 3
item_type: item
date: 2025-11-12
source: https://github.com/vercel/next.js/pull/86000
tags:
  - "Nextjs"
  - "PR"
  - "configexperimentaltransitionIndicator"
status: auto
quality: keep
---

[[2025-11-12-TWIR-258|Index]]

# Item 3: Next.js PR - New config.experimental.transitionIndicator option

Source: [https://github.com/vercel/next.js/pull/86000](https://github.com/vercel/next.js/pull/86000)

Summary:
A new experimental configuration option, transitionIndicator, has been introduced to Next.js. This flag will be used to switch to navigation.navigate() where available, addressing known navigation bugs. The PR is part of ongoing improvements to navigation and transition handling in Next.js, though some issues remain and are tracked for future updates.

Key takeaways:
- Adds config.experimental.transitionIndicator to Next.js.
- Intended to improve navigation by leveraging navigation.navigate() when possible.
- Addresses known bugs, with further work planned.
- Part of broader navigation and transition enhancements.

Recommendation:
Summary sufficient

Content:
# Enable React's default Transition indicator behind a flag by eps1lon · Pull Request #86000 · vercel/next.js · GitHub

[![@github-actions](https://avatars.githubusercontent.com/in/15368?s=40&v=4)](/apps/github-actions)
[github-actions](/apps/github-actions)
bot

locked as

**resolved** 

and limited conversation to collaborators

[Dec 1, 2025](#event-21262037740)
