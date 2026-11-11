---
type: twir-item
issue: 303
item: 8
item_type: item
date: 2026-10-28
source: https://nextjs.org/blog/ship-less-javascript-with-ai
tags:
  - "Nextjs"
  - "Bun"
status: auto
quality: keep
---

[[2026-10-28-TWIR-303|Index]]

# Item 8: Next.js skill - next-bundle-optimizer

Source: [https://nextjs.org/blog/ship-less-javascript-with-ai](https://nextjs.org/blog/ship-less-javascript-with-ai)

Summary:
Next.js 16.4 introduces the next-bundle-optimizer agent skill, enabling AI agents to analyze and optimize JavaScript bundles using Turbopack’s module graph. The tool can identify import patterns that bloat bundles, suggest and apply optimizations (like deferring heavy components or removing unused code), and generate pull requests. The updated bundle analyzer also offers improved manual tools for developers to explore, compare, and focus on critical render paths.

Key takeaways:
- AI-powered bundle analysis and optimization is now integrated into Next.js via next-bundle-optimizer.
- Identifies and fixes issues like eager loading, duplicate dependencies, and missed tree shaking.
- Manual bundle analysis tools are enhanced for human-driven optimization.
- Vercel’s own apps saw multi-megabyte JavaScript reductions using these tools.

Recommendation:
Read fully (read fully if you want to leverage AI for bundle optimization or explore advanced Next.js tooling)

Why it matters:
read fully if you want to leverage AI for bundle optimization or explore advanced Next.js tooling

Content:
---
title: Ship less JavaScript in Next.js with your AI agent
description: "Optimize your Next.js app's bundles with the next-bundle-optimizer agent skill, or explore them yourself with new Bundle Analyzer tools."
url: "https://nextjs.org/blog/ship-less-javascript-with-ai"
docs\_index: /docs/llms.txt
publishedAt: October 28th 2026
authors:
- Will Binns-Smith
---
As codebases grow, subtle changes to where and how JavaScript modules import one another can drastically impact how quickly users load and experience your app. In Next.js 16.1, we shipped the initial version of the Turbopack Bundle Analyzer, giving developers insights into their app's JavaScript bundles.
Now, in Next.js 16.4, we're giving your AI agent the tools to investigate those relationships and optimize your bundles. At Vercel, agents have identified and cut nearly \*\*two megabytes\*\* of unnecessary compressed JavaScript across v0 and vercel.com, with many critical pages saving hundreds of kilobytes. Let's dive into how it works.
## Bundle analysis, now for agents
Next.js now includes an agent skill to \*\*automatically\*\* optimize your app's JavaScript bundles. Since it uses its detailed module graph, the analyzer requires Turbopack, the default bundler since Next.js 16.
First, upgrade to Next.js 16.4 and add the [`next-bundle-optimizer`](https://www.skills.sh/vercel/next.js/next-bundle-optimizer) skill.
```bash filename="terminal"
npx skills add vercel/next.js --skill next-bundle-optimizer
```
Then run the skill in your AI agent with `/next-bundle-optimizer`.
The skill gives your agent access to Turbopack’s module graph to uncover unexpected import relationships. Consider this attempt to defer a heavy component:
```jsx filename="HeavyComponentLoader.js"
'use client';
import { lazy } from 'react';
export const HeavyComponentLoader = lazy(() => import('./HeavyComponent'));
```
If HeavyComponentLoader is the only module importing `./HeavyComponent`, its code will be deferred. However, if \*\*any other\*\* module in the same bundle statically imports `./HeavyComponent`, \*\*its code still loads upfront\*\*.
To find issues like these, the skill guides the agent to export saved `next analyze` snapshots as JSON and reconstruct Turbopack's module and chunk graphs for querying. Export the graph data for your own tools with `next analyze export`.
The agent identifies large [groups of connected modules](https://en.wikipedia.org/wiki/Louvain\_method) and determines their impact on the bundle. It traces their import chains and uses [minimum cut](https://en.wikipedia.org/wiki/Minimum\_cut) to identify a small set of import boundaries that could defer those modules. It then checks the proposed changes against your source code and how the components are used interactively in your app.
The agent can also find and fix:
- opportunities to move logic to React Server Components
- duplicate versions of large dependencies
- cases where tree shaking couldn't be applied and pulls in unused code
By default, the skill reports issues and suggested fixes. Run `/next-bundle-optimizer fix` to apply the proposed changes, rerun the analysis, and compare snapshots to measure their impact. Then ask your agent to open a pull request for each change.
### Putting the agent to work at Vercel
We used [`next-bundle-optimizer`](https://www.skills.sh/vercel/next.js/next-bundle-optimizer) to audit the [v0](https://v0.app) frontend, as well as the frontend of [vercel.com](https://vercel.com). The agent quickly identified opportunities to reduce compressed initial JavaScript across nearly every page.
In v0, the agent found:
- an experimental code editor loaded eagerly on nearly every v0 page, including for users outside the experiment. Saved \*\*150 KB\*\* on most pages.
- the app's centralized dialog registry eagerly loaded some heavy dialog components. Saved \*\*40–650 KB\*\* depending on the page.
- an unused trace viewer component that was reachable by most route modules. Saved \*\*7–61 KB\*\* depending on the page.
and on vercel.com:
- markdown rendering, syntax highlighting, and chart drawing for Vercel Agent were shipped even without the agent panel open. Saved \*\*255 KB\*\* on the dashboard page.
- a heavy natural language date parsing library was eagerly loaded before users interacted with the assistant. Saved \*\*55 KB\*\* on average.
- url parsing code was imported through a shared utility file that also pulled in the entire observability query engine. Saved \*\*125 KB\*\* on the deployments page.
In each case, we had the agent open a pull request, we verified the fix on a preview deployment, and shipped it.
In total, the agent has saved nearly two megabytes of compressed JavaScript across pages in our apps, either by eliminating it entirely, or deferring its loading until necessary.
## Bundle analysis for humans
The interactive bundle analyzer now has new tools for exploring your app's bundles yourself. To launch the bundle analyzer, run `next analyze` in your Next.js app directory.
### Find your largest routes
A new route summary homepage highlights your largest client routes, giving you a starting point for investigating bundle size.
From there, open a route and sort the new table view by size to find its largest contributors.
### Compare bundles as your app changes
The analyzer now automatically saves snapshots of the analyses you run. Diff them to measure an optimization’s impact or investigate bundle growth after a feature or dependency update.
### Focus on the critical render path
The analyzer now highlights modules on the critical render path and lets you filter out async dependencies, leaving only the code that loads synchronously for the initial render. [^initial-render]
Learn more about the [Next.js Bundle Analyzer](https://nextjs.org/docs/app/guides/package-bundling), or install the optimizer skill to start investigating your app's bundles with your agent.
## Feedback and community
Try the analyzer and optimizer skill on your own app, and share your feedback on the dedicated [GitHub discussion](https://github.com/vercel/next.js/discussions/86731). You can also find us on:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
[^initial-render]: Depending on how runtime state, RSC renders may include chunks created by next/dynamic in the initial load. Always test your app to verify which modules are actually part of the critical render path.
