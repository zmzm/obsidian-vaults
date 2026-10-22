---
type: twir-item
issue: 302
item: 6
item_type: item
date: 2026-10-21
source: https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4
tags:
  - "Nextjs"
  - "Navigation"
  - "v0"
  - "164"
status: auto
quality: keep
---

[[2026-10-21-TWIR-302|Index]]

# Item 6: Improving navigation experience in v0 with Next.js 16.4

Source: [https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4](https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4)

Summary:
This post details how Vercel's v0 app improved navigation by leveraging Next.js 16.4's Partial Prefetching and a coding agent workflow. By enabling Partial Prefetching and using the next-partial-prefetching-optimizer Skill, the team automated the process of ensuring key UI elements are prefetched and available immediately upon navigation. The article explains the optimization loop, test strategies, and technical adjustments made to maximize cache efficiency and user experience.

Key takeaways:
- Partial Prefetching allows Next.js to prefetch reusable route parts, improving perceived navigation speed.
- The next-partial-prefetching-optimizer Skill automates testing and refactoring for optimal prefetching.
- Adoption involves clear, testable goals and iterative optimization using Playwright tests.
- Caching strategies (e.g., 'use cache: remote') and cache invalidation are key to efficient data reuse.

Recommendation:
Read fully (for teams using Next.js 16.4 or interested in advanced navigation optimization)

Why it matters:
for teams using Next.js 16.4 or interested in advanced navigation optimization

Content:
---
title: Improving navigation experience in v0 with Next.js 16.4
description: How we used Partial Prefetching and a coding agent to improve navigation across v0 with Next.js 16.4.
url: "https://nextjs.org/blog/improving-navigation-experience-in-v0-with-nextjs-16-4"
docs\_index: /docs/llms.txt
publishedAt: October 16th 2026
authors:
- Aurora Scharff
---
Previously, we shared how a coding agent used the `instant()` Playwright test helper to [make navigations instant](/blog/making-v0-navigations-instant) in [v0](https://v0.app), Vercel's AI app builder. That work focused on the core `/chat` experience.
In other parts of v0, users saw loading skeletons when they returned to pages they had already opened. Useful content was not always ready before the first click, either. We wanted those pages to behave more like a single-page app, with content prefetched on the way in and still available on the way back.
[Next.js 16.3](/blog/next-16-3#partial-prefetching) introduced Partial Prefetching. [Next.js 16.4](/blog/next-16-4#excluding-content-from-a-prefetch) added more control over when cached content loads, along with the new [`next-partial-prefetching-optimizer` Skill](#try-it-yourself) for optimizing what gets prefetched.
In this post, we'll look at how we used the Skill to improve v0's navigation experience.
## What Partial Prefetching changes
In previous versions of Next.js, `prefetch={true}` fetched the entire destination, including dynamic content. This could fetch pages users never opened, while clicking before the prefetch finished still led to a slow navigation. Turning prefetching off avoided those requests but moved all of the work until after the click.
With [Partial Prefetching](/blog/next-16-3#partial-prefetching), Next.js prefetches the reusable parts of a route so they're ready before the click, while the rest loads during navigation. Cached content, including personalized content stored in the browser, can be prefetched and reused on return visits. For selected links, [`prefetch={true}`](/docs/app/api-reference/components/link#prefetch) resolves the destination URL so cached content for a dynamic route such as `/products/[id]` can be included in the prefetch.
Starting with [Next.js 16.4](/blog/next-16-4#whats-new-in-cache-components), `create-next-app` enables [Cache Components](/blog/next-16-4#whats-new-in-cache-components) and [Partial Prefetching](/blog/next-16-3#partial-prefetching) by default, as the recommended model for all Next.js apps:
```ts filename="next.config.ts" highlight={4-5}
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
cacheComponents: true,
partialPrefetching: true,
};
export default nextConfig;
```
When we started this work, v0 was already using Cache Components. The earlier work on `/chat` had also incrementally adopted Partial Prefetching for a few routes:
```ts filename="app/.../chat/page.tsx"
export const prefetch = 'partial';
```
To bring the same model to the rest of v0, we enabled Partial Prefetching globally before starting the refactor. The [adoption guide](/docs/app/guides/adopting-partial-prefetching) includes an existing [`next-partial-prefetching-adoption` Skill](/docs/app/guides/ai-agents#next-partial-prefetching-adoption) for this change.
## Making the goal testable
Each navigation needed a clear, testable target for the prefetched UI.
The [`instant()` Playwright helper](/docs/app/guides/instant-navigation#prevent-regressions-with-e2e-tests) acts as a lock around the click. It holds back content that only arrives during navigation, so a test can assert on the UI available before the click:
```ts filename="e2e/template-navigation.spec.ts" highlight={1,8-14}
import { instant } from '@next/playwright';
import { expect, test } from '@playwright/test';
test('prefetches the primary template UI', async ({ page }) => {
await page.goto('/templates');
const card = page.getByTestId('template-card-link').first();
await instant(page, async () => {
await card.click();
await page.waitForURL('\*\*/templates/\*');
await expect(page.getByTestId('template-detail-skeleton')).toHaveCount(0);
await expect(page.getByTestId('template-detail-header')).toBeVisible();
await expect(page.getByTestId('template-detail-title')).toBeVisible();
await expect(page.getByTestId('template-detail-preview')).toBeVisible();
});
});
```
In this example, the test checks that the template header, title, and preview are already available without showing the broad loading skeleton. If any of that UI is missing, the test fails.
## The optimization loop
To automate this process, Next.js 16.4 includes the new [`next-partial-prefetching-optimizer` Skill](/docs/app/guides/ai-agents#next-partial-prefetching-optimizer). It guides an agent through the following loop until the `instant()` test passes:
```text diagram
Choose the navigation and target UI
│
▼
Write a passing instant() test for the current UI
│
▼
Add the target assertions and confirm they fail
│
▼
Refactor the app ◀────────────────────────────┐
using caching and prefetching │
│ │
▼ │
Rebuild and rerun the test │
│ │
├── still failing ─────────────────┘
│
▼ passing
Verify the regression check and keep the test
```
This is especially useful in a larger codebase, where reaching the intended UI can take several iterations and refactors. The agent can keep running the loop until the `instant()` test passes.
The test remains in the codebase and can run in CI to catch future regressions.
The Skill can make a best effort from a broad goal. For this work, we wanted more control over exactly how the UI loaded, so the prompts below define what should be ready before the click and what could wait.
## Applying the loop across v0
We asked an agent with the [Skill installed](#try-it-yourself) to run this workflow across v0 and split the work into feature-specific PRs. For each PR, we tried the interaction in the preview before merging, then tracked four production metrics after it shipped:
- [\*\*Runtime Cache spend\*\*](https://vercel.com/docs/caching/runtime-cache#observability) for cache reads and writes
- \*\*Request volume\*\* for the affected routes, including prefetch requests and [Function Invocations](https://vercel.com/docs/functions/usage-and-pricing#invocations)
- [\*\*Active CPU\*\*](https://vercel.com/docs/functions/usage-and-pricing#active-cpu) used to serve those routes
- [\*\*Data transfer\*\*](https://vercel.com/docs/manage-cdn-usage) from prefetch requests
Let's look at a few examples of how the Skill worked.
### Prefetching useful content for `/templates/[id]`
Before the refactor, opening a card from `/templates` showed a loading skeleton while the template details loaded. Returning to the same template fetched those details again and brought back the skeleton.
The UX we wanted instead was:
```prompt
When I open a Template from the "Templates" page, prefetch its header, title, and preview so I see them right away.
```
To make that UX possible, the agent separated public template data from personalized viewer state. The public data was safe to share across users, so the agent cached it with [`'use cache: remote'`](/docs/app/api-reference/directives/use-cache-remote).
On Vercel, this stores the result in [Runtime Cache](https://vercel.com/docs/caching/runtime-cache), where requests from different users and function instances can reuse it. With a self-hosted `next start`, `'use cache: remote'` uses memory unless you configure [`cacheHandlers.remote`](/docs/app/api-reference/config/next-config-js/cacheHandlers). Plain [`'use cache'`](/docs/app/api-reference/directives/use-cache) also uses memory by default.
The cached data also needed a lifetime and a way to invalidate it. [`cacheLife()`](/docs/app/api-reference/functions/cacheLife) sets the lifetime, while [`cacheTag()`](/docs/app/api-reference/functions/cacheTag) provides an invalidation key:
```tsx filename="app/.../templates/[id]/page.tsx" highlight={1,4-6}
import { cacheLife, cacheTag } from 'next/cache';
async function loadCachedPublicTemplatePageData(templateId: string) {
'use cache: remote';
cacheTag(`template:${templateId}`);
cacheLife('hours');
return loadPublicTemplatePageData(templateId);
}
```
Publishing or updating a template calls [`revalidateTag()`](/docs/app/api-reference/functions/revalidateTag), marking the cached data stale so a later request refreshes it.
With the template data now reusable, the agent added [`prefetch={true}`](#what-partial-prefetching-changes) to each link from `/templates`:
```tsx filename="app/templates/template-card.tsx" highlight={3}
import Link from 'next/link';
;
```
After the refactor, the template header, title, and preview were ready before the click and remained available when users returned:
### Avoiding unnecessary prefetches in large grids
The first rollout made the selected template's content available immediately, but it also started a richer prefetch for every visible card in `/templates`. The [production metrics](#applying-the-loop-across-v0) showed that prefetch requests to `/templates/[id]` had increased \*\*2.9×\*\*, so we tuned when the richer prefetch started.
We still wanted to prefetch the card a user was likely to open, so we asked the agent:
```prompt
On the "Templates" page, wait until I hover, focus, or touch a card before prefetching its details. Don't prefetch every card as soon as it appears.
```
The agent changed the richer prefetch to wait for [user intent](/docs/app/guides/prefetching#hover-triggered-prefetch), starting on hover, focus, or touch rather than when the card entered the viewport.
The core behavior can be expressed in a few lines:
```tsx filename="app/components/prefetch-link.tsx"
const [intent, setIntent] = useState(false);
setIntent(true)}
onFocus={() => setIntent(true)}
onTouchStart={() => setIntent(true)}
/>;
```
In v0, the agent added this behavior to an existing custom Link wrapper:
```tsx filename="app/templates/template-card.tsx"

```
For the Templates grid, this kept the selected Template's details available before the click without treating every card as equally likely to be opened. Throughout the refactor, the pattern was also used for other large lists and grids in v0. Smaller, fixed groups continued to prefetch when their links became visible.
### Reusing personalized content under `/settings`
Before the refactor, pages under `/settings` could show their loading state on the first visit and again when users returned. Because the content is personalized, it needed to stay in the browser rather than a cache shared between users.
The UX we wanted was:
```prompt
When I move between pages in "Settings", I want "Advanced", "Workspace", and "Usage" prefetched before I click them. Let the other pages load when I open them, then keep them available if I go back.
```
The agent used [`'use cache: private'`](/docs/app/api-reference/directives/use-cache-private) to keep this content in the browser.
URLs under `/settings` include the account or team in `[scope]`, such as `/acme/settings/advanced`. Passing `scope` into the cached function makes it part of the cache key, keeping each account or team's content separate. The \*\*Advanced\*\* page could reuse the result for five minutes:
```tsx filename="app/.../settings/advanced/page.tsx" highlight={1,4-6}
import { cacheLife, cacheTag } from 'next/cache';
async function AdvancedSettings({ scope }: { scope: string }) {
'use cache: private';
cacheLife({ stale: 300 });
cacheTag('settings:advanced');
return ;
}
```
For cached data that users could change, the agent paired each read with the action that updates it. For example, when users save \*\*Custom Instructions\*\* for v0 to follow across chats and projects, the [Server Action](/docs/app/guides/server-actions) calls [`updateTag()`](/docs/app/api-reference/functions/updateTag). This immediately expires the cached \*\*Advanced\*\* settings, so users see the new value in the same roundtrip.
Once this content was cached, the agent added `prefetch={true}` to the \*\*Advanced\*\*, \*\*Workspace\*\*, and \*\*Usage\*\* links to resolve each scoped destination and include its cached content in the prefetch. Other pages under `/settings` loaded after the click, then remained available when users returned.
After the refactor, the selected pages opened with their content ready, while the others stayed available after the first visit:
### Balancing prefetching and cost
We also wanted to improve navigation from `/projects` into an individual project. Before the refactor, opening one showed a broad loading state. Reopening it fetched the content again and brought the loading state back.
The \*\*Recent Chats\*\* section was still useful to cache for return visits, but it did not need to be prefetched.
Next.js 16.4 includes a new [`navigation()`](/docs/app/api-reference/functions/navigation) API that lets you decide which cached work waits until navigation:
```tsx filename="app/.../comments.tsx" highlight={4}
import { navigation } from 'next/cache';
async function Comments() {
await navigation();
const comments = await getComments();
return ;
}
```
Cached work after `navigation()` waits until the page opens, then stays available when users return. This works well for lower-priority content that isn't needed right away.
For this navigation, the UX we wanted was:
```prompt
When I open a Project from the "Projects" page, I want the title and "Production Deployment" ready when I click. Prefetch them on hover, focus, or touch. Keep "Recent Chats" cached for return visits, but don't prefetch it.
```
The agent cached and prefetched the project details, with `navigation()` before \*\*Recent Chats\*\*:
```tsx filename="app/.../projects/[id]/page.tsx" highlight={2,8-10,17}
import { Suspense } from 'react';
import { navigation } from 'next/cache';
function ProjectPage({ project }: { project: Project }) {
return (
<>
}>
);
}
async function RecentChats({ projectId }: { projectId: string }) {
await navigation();
const chats = await loadProjectChats(projectId);
return ;
}
```
Another use of `navigation()` was `/settings/usage`. The agent kept the tabs, filters, and \*\*Activity\*\* UI in the prefetch, while the credits dashboard and usage fields loaded during navigation and remained available on return visits.
After the refactor, the broad loading state was gone. The project title and \*\*Production Deployment\*\* section appeared first, followed by \*\*Recent Chats\*\*, which stayed cached for return visits:
## Reviewing the results
We reviewed the metrics after each PR and tuned the work as we went. Once all the PRs had merged, the whole-app comparison showed total daily cost was \*\*2.9% lower\*\*, even as Shared Runtime Cache spend grew to \*\*4.3×\*\* its pre-refactor level, adding about \*\*$3.44 per day\*\*. Fewer requests and lower compute and transfer offset that increase, bringing the request-serving costs we tracked down \*\*14.4%\*\*.
Traffic and unrelated deployments changed during the same period, so we treated the whole-app numbers as confirmation that the refactor had not made v0 more expensive, not as savings caused solely by this work.
We also doubled the number of `instant()` tests covering these navigations. Across the areas we changed, users saw more useful content as soon as they opened a page and fewer loading states when they returned. The tests now protect that experience as v0 evolves.
## Try it yourself
You can use the [`next-partial-prefetching-optimizer` Skill](https://github.com/vercel/next.js/blob/canary/skills/next-partial-prefetching-optimizer/SKILL.md) to run the same loop in your app. It assumes your app already uses Cache Components and Partial Prefetching. The [Cache Components migration guide](/docs/app/guides/migrating-to-cache-components) and [Partial Prefetching adoption guide](/docs/app/guides/adopting-partial-prefetching) cover those prerequisites.
Install the Skill for your coding agent:
```bash
npx skills add vercel/next.js --skill next-partial-prefetching-optimizer
```
Once installed, most coding agents will invoke it automatically when the request matches. Depending on your harness, you can also ask the agent to invoke the `next-partial-prefetching-optimizer` Skill or use `/partial-prefetching-optimizer`.
Describe the navigation you want to improve in your own words, as in the examples above, or ask the agent to find opportunities in your app.
To apply these patterns yourself, follow the [Optimizing prefetching guide](/docs/app/guides/optimizing-prefetching). The Skill uses the same guidance under the hood.
## Feedback and community
Try it on your own app, and let us know how it goes:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
