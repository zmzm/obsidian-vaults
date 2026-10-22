---
type: twir-item
issue: 300
item: 1
item_type: featured
date: 2026-10-07
source: https://nextjs.org/blog/next-16-4
tags:
  - "Nextjs"
  - "164"
status: auto
quality: keep
---

[[2026-10-07-TWIR-300|Index]]

# Item 1: Next.js 16.4

Source: [https://nextjs.org/blog/next-16-4](https://nextjs.org/blog/next-16-4)

Summary:
Next.js 16.4 introduces significant improvements, most notably making Cache Components the recommended default for all new and existing apps. This release also brings lazy compilation, smaller Turbopack output, React 19.3 features, and enhanced developer tooling. The new programming model enables granular, declarative caching at the component level, with features like Partial Prefetching and ensureStatic for static guarantees. Migration tools and configuration options are provided to ease adoption for existing projects.

Key takeaways:
- Cache Components are now the default and recommended for all Next.js apps, enabling opt-in, composable caching at the component level.
- New ensureStatic configuration allows strict enforcement of static rendering for routes or layouts, preventing accidental dynamic content.
- Partial Prefetching is now part of the model, improving navigation speed and flexibility.
- Developer tooling (e.g., next upgrade --agent) and migration guides are available to help teams transition.

Recommendation:
Read fully (especially if you maintain or architect Next.js apps, as the new model and migration details are substantial)

Why it matters:
especially if you maintain or architect Next.js apps, as the new model and migration details are substantial

Content:
---
title: Next.js 16.4
description: Next.js 16.4 introduces lazy compilation, smaller Turbopack output, React 19.3 features, Cache Components improvements, and new developer tooling.
url: "https://nextjs.org/blog/next-16-4"
docs\_index: /docs/llms.txt
publishedAt: October 6th 2026
---
Over the 16.x releases, we’ve introduced a new programming model that addresses many of the frustrations you've had with App Router from the start:
- It brings fast initial loads, even for personalized pages
- It gives server-rendered apps instant client navigations
- It makes caching opt-in, declarative, and composable
This new programming model is called Cache Components, and it will become the default in Next.js 17.
Prior to this release, we didn’t recommend it universally because there were some cases where it couldn’t achieve the same cost and performance guarantees as with the previous model.
This release includes key features that close those gaps.
\*\*Starting with Next.js 16.4, we’re excited to recommend Cache Components as the best choice for every Next.js app.\*\*
As of today, all new apps created with `create-next-app` will have Cache Components enabled by default. Greenfield projects can enjoy all the benefits of the new model with no reservations.
For existing apps, we’ve been investing in better agentic tooling to help codebases migrate to the new model. The new `next upgrade --agent` command gives agents version-specific guidance on upgrading your app, and dedicated Skills help agents with any refactorings needed for you to adopt Cache Components.
Next.js 16.4 also includes several out-of-the-box improvements for all Next.js apps, including less memory usage and disk size in dev, reduced compile times, smaller production bundles, and React 19.3.
Here’s a full overview of what to expect in this release, starting with Cache Components.
## What are Cache Components?
Cache Components are a suite of features that lets you mark specific parts of your component tree as eligible for caching. Think of `'use cache'` as a component-level version of the Cache-Control HTTP header:
```jsx {18,19}
import { cacheLife } from 'next/cache';
export default async function DashboardPage() {
const currentUser = await getCurrentUser();
return (

Welcome, {currentUser.name}

}>

);
}
async function Projects({ userId }) {
'use cache';
cacheLife('hours');
const projects = await db.query.projects.findMany({
where: eq(projectsTable.userId, userId),
});
return (

{projects.map((project) => (

{project.name}

))}

);
}
```
Next.js interprets these `'use cache'` annotations as it renders your pages, caching your component's UI in the browser (during client navigations) and, optionally, on the server (during server rendering, or ahead of time during the build).
These composable annotations let you mix client-side caching, fully pluggable server-side caching, and request-time rendering all within a single page, and they replace the implicit caching behaviors of the previous App Router versions.
To learn more about Cache Components, [read the guide on caching](/docs/app/getting-started/caching).
## What's new in Cache Components
In this post, we use "Cache Components" to refer to the new programming model, which you can use today by enabling two flags in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
cacheComponents: true,
partialPrefetching: true,
};
export default nextConfig;
```
Cache Components first shipped without Partial Prefetching, but it's now considered part of the model. You can learn more about Partial Prefetching from [our previous release post](/blog/next-16-3-instant-navigations#rethinking-prefetching).
Next, here's what's new for Cache Components in 16.4.
### Ensuring shells, prefetches, or pages are static
One of the hallmark features of `'use cache'` is the ability to build pages that stream static and dynamic content together in a single response from the server.
For example, you can compose the current user’s avatar alongside a blog post that is otherwise statically prerendered:
```jsx
export default function Page() {
return (
<>

);
}
// This component renders at request time
async function UserAvatar() {
const currentUser = await getCurrentUser();
// ...
}
// This component is statically prerendered
async function Content() {
'use cache';
await fetch('...');
// ...
}
```
Next.js can serve the prerendered blog post from cache (like your app's `/public` folder, or a CDN) and render the UserAvatar at request time, all from the same HTTP response.
This flexibility is what enables you to build apps with sophisticated UIs, without sacrificing speed or dynamism. But sometimes you \_want\_ to build an app with fully static pages. In those cases, one dynamic component can degrade the performance or cost characteristics of an otherwise optimized site.
In Next.js 16.4, `ensureStatic` offers a simple way to guarantee that a route’s shell, prefetch, or full navigation is static. For apps that want to avoid unintentional compute and keep their server costs down, this lets you prevent a dynamic component from accidentally sneaking into a route.
For example, if we wanted to enforce that our blog post page from the example above was always static, and that adding a dynamic component like UserAvatar should never be possible, we could add `export const ensureStatic` to the route:
```jsx {1,6}
export const ensureStatic = 'navigation';
export default function Page() {
return (
<>
 {/\* 🔴 This component fails the build \*/}
);
}
```
By setting `ensureStatic` to "navigation", Next.js will fail the build if any dynamic content is ever included in this page, ensuring that navigations to this route will never render at request time.
While "navigation" is the most restrictive form, you can also set `ensureStatic` to "prefetch" (to ensure links with explicit prefetching to this route only fetch static content) or "shell" (to ensure that only static content is fetched when this route is first discovered) if you need more fine-grained control.
In addition to using it on individual pages, you can also add `ensureStatic` to a layout to apply the same guarantees to all pages within that layout. For example, you could add `ensureStatic = 'navigation'` to the root layout to easily guarantee that every page navigation in your site is static:
```jsx {2}
// app/layout.tsx
export const ensureStatic = 'navigation';
export default async function RootLayout({ children }) {
// ...
}
```
Then, you could push it down to nested layouts if certain pages start to need dynamic content.
Many dynamic apps won't need this feature, but for optimized sites like ecommerce stores, marketing pages, or blogs, `ensureStatic` is a simple way to guard against unwanted request-time rendering.
Learn more about [keeping pages static](/docs/app/guides/keeping-pages-static) and the [`ensureStatic` config](/docs/app/api-reference/file-conventions/route-segment-config/ensureStatic).
### Excluding content from a prefetch
Prefetching is a powerful way to improve the UX of your Next.js applications.
By using `` or `useRouter().prefetch()`, you can eliminate loading states by prerendering a page's cached UI before an actual navigation takes place.
For example, let's look at a simple email app. Here's an Inbox that renders links to each message:
{/\* prettier-ignore \*/}
```jsx {7-12}
async function Inbox() {
const messages = await db.query.messages.findMany();
return (
);
}
```
And here's the Message page, which shows a spinner when loading a message thread for the first time, then caches it in the browser for subsequent visits:
{/\* prettier-ignore \*/}
```jsx {4,31,37}
// app/message/[id]/page.jsx
export default function Page({ params }) {
return (
}>
{params.then(({ id }) => (
))}
);
}
async function Message({ id }) {
const [message, thread] = await Promise.all([
getMessage(id),
getThread(id)
]);
return (
<>

{message.subject}

{message.body}

{thread.map((message) => (

{message.body}

))}
);
}
async function getMessage(id) {
'use cache';
return db.query.messages.findFirst({ where: eq(messages.id, id) });
}
async function getThread(id) {
'use cache';
return db.query.messages.findMany({
where: eq(messages.threadId, id),
orderBy: asc(messages.createdAt),
});
}
```
While this lets users instantly view messages they've already loaded, they'll still see the loading spinner when opening a message for the first time.
To eliminate that initial loading state, we could add `prefetch` to our Inbox's links:
{/\* prettier-ignore \*/}
```jsx {8}
async function Inbox() {
const messages = await db.query.messages.findMany();
return (
);
}
```
Now, each link will prefetch all the cached data and UI on the Message page as soon as it becomes visible, so it's ready by the time the user clicks.
This makes for a great UX by eliminating loading states from the app, but it also means that every visible link loads the \_entire\_ message thread ahead of time—even for messages the user never opens. For our email app, this might be too costly or introduce too much strain on our servers.
Instead of just turning prefetching back off, a better solution would be to only prefetch the first message, and defer rendering the rest of the thread until the user actually navigates.
In Next.js 16.4, we can do exactly this. The new `navigation` API lets you exclude loading cached content during a prefetch, effectively deferring it until an actual navigation takes place.
In our example, we could extract the thread into a new component, and add `await navigation()` to exclude it from the prefetch:
```jsx {1,19}
import { navigation } from 'next/cache';
async function Message({ id }) {
const message = await getMessage(id);
return (
<>

{message.subject}

{message.body}

}>
);
}
async function Thread({ id }) {
await navigation();
const thread = await getThread(id);
return (
<>
{thread.map((message) => (

{message.body}

))}
);
}
```
Now the Message page only renders the first message during a prefetch, and waits for a full navigation to load the rest of the thread from the database and render it.
In addition to `navigation()`, we've also added `prefetch()`, which you can await to exclude cached content that would otherwise be included in a route's shell. This way, rendering that content will be deferred until an explicit prefetch with `` or `useRouter().prefetch()`.
These APIs give you more control over what data gets loaded at different stages of a navigation, letting you balance eager and lazy rendering in a way that’s right for your app.
Learn more about [deferring work to a later stage](/docs/app/guides/optimizing-prefetching#defer-work-to-a-later-stage), and see the [`navigation`](/docs/app/api-reference/functions/navigation) and [`prefetch`](/docs/app/api-reference/functions/prefetch) API references.
## New agent features
We're investing in agent tooling to make Next.js a system that continuously helps keep your app secure and up to date. Next.js 16.4 builds on our documentation, Skills, and verification tools with agent upgrades and feedback, helping us learn from how you build and bring improvements back to your app.
### Agent upgrades
The new `--agent` option for `next upgrade` helps your agent upgrade your app from start to finish. It checks your installed version, selects a target release, and prepares the migration guides, any needed codemods, and verification steps for your agent. The agent applies the update, resolves migration issues, and checks that your app still works.
You or your agent can run it from your app's directory:
```bash filename="Terminal"
npx next@canary upgrade --agent=latest
```
Using `next@canary` runs the latest upgrade tooling, even if your app is on an older version of Next.js. Your agent gets up-to-date guidance to bring your app to the latest release.
Getting up to date is the first step. To help you stay current, Next.js 16.4 introduces `experimental.agentUpgrade`. As you or your agent run `next dev` or `next build`, Next.js will automatically nudge you or your agent when a relevant upgrade is available, so you don't have to remember to check yourself. When you choose to upgrade, it starts the same agent workflow with your configured policy.
You can configure these reminders in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
agentUpgrade: 'security',
},
};
export default nextConfig;
```
- \*\*`'security'` (the default policy):\*\* Remind you about upgrades that address known vulnerabilities affecting your installed version.
- \*\*`'latest'`:\*\* Remind you about newer major or minor releases and use the `latest` upgrade policy to keep your app current.
- \*\*`false`:\*\* Disable upgrade reminders.
We're also working on a future policy for this flag to help agents adopt new features and programming model changes idiomatically, such as migrating to Cache Components. Today, you can use our Skills for [adopting Cache Components](/docs/app/guides/ai-agents#next-cache-components-adoption) and [Partial Prefetching](/docs/app/guides/ai-agents#next-partial-prefetching-adoption) to have your agent help you migrate to the new model.
Learn more about [upgrading with a coding agent](/docs/app/guides/upgrading/agent-upgrade) and the [`agentUpgrade` config](/docs/app/api-reference/config/next-config-js/agentUpgrade).
### Agent feedback
Coding agents often encounter framework errors, unclear docs, or workarounds while building and upgrading apps. The new experimental agent feedback workflow lets them prepare draft reports that you can review and choose to send to the Next.js team.
Agent feedback is enabled by default when you create a new app with the recommended `create-next-app` settings. For existing apps, you can opt in through your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
agentFeedback: true,
},
};
export default nextConfig;
```
With this enabled, `next dev` adds instructions for your agent to collect potential issues while it works. When the task is finished, the agent prepares report drafts and opens them in your browser for review.
The agent is instructed to omit source code, logs, secrets, and project-specific details. You can edit or discard each report, and nothing is sent until you select \*\*Send feedback\*\*.
Agent feedback requires Next.js Telemetry to be enabled and does not run in CI.
Learn more about [agent feedback](/docs/app/guides/ai-agents#automatic-agent-feedback) and the [`agentFeedback` config](/docs/app/api-reference/config/next-config-js/agentFeedback).
## Improvements for all apps
### Smaller disk cache size
In 16.4, Turbopack's disk cache uses 20–25% less space, with no configuration changes required.
The cache now uses Zstandard compression for the data that takes up most of the space, while keeping LZ4 for metadata to preserve fast cache lookups. We have also improved our compaction routines to more efficiently drop stale data.
### Lazy server HMR
Previously, changing a shared server module could trigger updates for pages you'd visited earlier in the dev session, even if you were no longer viewing them.
In 16.4, Turbopack compiles and applies server updates only when a request needs them. The page you're viewing still updates as you edit, while other routes wait until they're requested again. This reduces unnecessary background work as you navigate through your app.
### Turbopack shared runtime
Turbopack now ships its runtime in a single chunk shared across routes. This reduces download sizes and improves cache hit rates.
Read our [blog on chunking](./turbopack-chunking) for more information on this and other chunking features.
### Smaller production bundles
In 16.4, Turbopack generates shorter CSS Module class names in production, reducing the size of stylesheets and the HTML and JavaScript that reference them. Development keeps the longer class names for easier debugging.
Additionally, Turbopack now uses export mangling to further reduce bundle size by shortening the internal JavaScript export names used to connect modules.
### React 19.3
Next.js 16.4 ships with React 19.3, bringing stable View Transitions and Fragment Refs, the new `browser()` API, and more.
Read the [React 19.3 announcement](https://react.dev/blog/2026/09/09/react-19-3) for a full overview of what's new.
## New experimental features
### Rust React Compiler
The React Compiler automatically optimizes component rendering, reducing the need for manual memoization. Its experimental Rust version, introduced in 16.3, runs directly inside Next.js instead of through Babel.
In 16.4, a new fast check lets it skip files that don't need optimization. It also avoids repeating those optimizations when building Client Components for server rendering, reducing the work needed to compile your app.
16.4 also includes numerous compiler updates that improve performance and correctness. The Turbopack team contributed memory allocation changes that reduced the React Compiler's memory usage by 30% and compile time by 15%.
Enable the React Compiler and opt into the Rust version in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
reactCompiler: true,
experimental: {
turbopackRustReactCompiler: true,
},
};
export default nextConfig;
```
Learn more about the [Rust React Compiler](/docs/app/api-reference/config/next-config-js/turbopackRustReactCompiler) and the [compiler performance improvements](https://github.com/vercel/next.js/pull/96820).
### Disk cache cleanup
As you edit your app, Next.js can retain cached compilation work that's no longer needed.
In 16.4, an experimental garbage collector removes this unused work from both memory and the disk cache, helping reduce resource usage during long dev sessions. It can also reclaim stale data from previous sessions, such as cached work for routes you've deleted.
Enable garbage collection in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
turbopackGc: true,
},
};
export default nextConfig;
```
Learn more about [`turbopackGc`](/docs/app/api-reference/config/next-config-js/turbopackGc).
### Lazy dynamic imports
Dynamic imports let you defer loading code, but Next.js normally compiles that code up front during development.
In 16.4, you can opt into compiling client-side dynamic imports only when the browser requests them. This reduces the initial compilation work for code you haven't used yet, such as a library loaded with `import()` after a button click.
Enable lazy dynamic imports in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
turbopackLazyDynamicImports: true,
},
};
export default nextConfig;
```
Some `next/dynamic` imports are still compiled eagerly.
Learn more about [`turbopackLazyDynamicImports`](/docs/app/api-reference/config/next-config-js/turbopackLazyDynamicImports).
### Worker threads
Turbopack runs tools like Babel, PostCSS, and webpack loaders in separate Node.js processes that communicate with it over sockets.
With worker threads, those tools run within a single process. This avoids the overhead of separate processes and socket communication, and is designed to reduce memory and CPU usage during development and builds.
Enable worker threads in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
turbopackPluginRuntimeStrategy: 'workerThreads',
},
};
export default nextConfig;
```
On Node.js 24.13.1 and newer, Next.js currently falls back to child processes due to a [Node.js bug](https://github.com/nodejs/node/issues/65100).
Learn more about [`turbopackPluginRuntimeStrategy`](/docs/app/api-reference/config/next-config-js/turbopackPluginRuntimeStrategy).
### Additional roots and global virtual store support
Next.js 16.4 can follow symlinked dependencies outside your project root by letting you declare additional roots. This makes it easier to work on linked local packages without expanding the project root to include unrelated directories.
This also enables manual integration with global virtual stores in [pnpm](https://pnpm.io/global-virtual-store), [Bun](https://bun.com/docs/pm/global-store), [Nub](https://nubjs.com/docs/install/virtual-store), and [aube](https://aube.sh/package-manager/global-virtual-store), which share installed dependencies across projects and worktrees to speed up installs. Automatic integration is planned for a future release.
Add the directories containing your linked dependencies to your Next.js config:
```ts filename="next.config.ts"
import path from 'node:path';
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
turbopackAdditionalRoots: {
linkedPackages: { path: path.join(\_\_dirname, '../packages') },
},
},
};
export default nextConfig;
```
For pnpm's global virtual store, add the store directory reported by `pnpm store path` as an additional root.
Learn more about [additional roots](/docs/app/api-reference/config/next-config-js/turbopack#additional-roots-experimental).
### Turbopack Bundle Analyzer
This release adds significant features to the Turbopack Bundle Analyzer. It now:
- Highlights the largest client routes in a new route summary homepage.
- Offers a new table view to quickly sort by the largest contributors to a route’s resources.
- Automatically creates snapshots of analyses you run over time and can diff bundles as your app changes.
- Distinguishes modules on the critical render path, and allows you to filter out async dependencies when exploring.
The bundle analyzer now also includes an experimental [`next-bundle-optimizer`](https://www.skills.sh/vercel/next.js/next-bundle-optimizer) agent skill to automatically discover, diagnose, and improve the amount of JavaScript and other resources your app ships.
To use the skill:
- Upgrade your Next.js app to 16.4.
- Run `npx skills add vercel/next.js --skill next-bundle-optimizer`.
- Run `/next-bundle-optimizer` in your AI agent of choice.
Learn more about the [Turbopack Bundle Analyzer](/docs/app/guides/package-bundling).
## Feedback and community
We hope you're excited to try out Next.js 16.4!
Let your agent upgrade your app with our new CLI command:
```bash
npx next@canary upgrade --agent=latest
```
or upgrade yourself:
```bash
npm install next@latest
```
And share your feedback to help shape the future of Next.js:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
## Contributors
Next.js is the result of the combined work of thousands of individual developers. This release was brought to you by:
- The \*\*Next.js\*\* team: [Andrew](https://github.com/acdlite), [Aurora](https://github.com/aurorascharff), [Dan](https://github.com/gaearon), [Hendrik](https://github.com/unstubbable), [Jamiboy](https://github.com/jamiboym), [Jan](https://github.com/kassens), [Janka](https://github.com/lubieowoce), [Jiwon](https://github.com/devjiwonchoi), [Joseph](https://github.com/icyJoseph), [Josh](https://github.com/gnoff), [Jude](https://github.com/gaojude), [Pete](https://github.com/petehunt), [Sam](https://github.com/samselikoff), [Sebbie](https://github.com/eps1lon), and [Tim](https://github.com/timneutkens).
- The \*\*Turbopack\*\* team: [Andrew](https://github.com/andrewimm), [Benjamin](https://github.com/bgw), [Jimmy](https://github.com/jimmyhmiller), [Luke](https://github.com/lukesandberg), [Niklas](https://github.com/mischnic), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
Huge thanks to @ztanner, @6iu8a, @swarnava, @lukahartwig, @uaoa, @orzazade, @Samiislam851, @jarrensj, @sampoder, @martinfrancois, @leejpsd, @alangenfeld, @aryabyte21, @kostyniuk, @Stanzilla, @bmorros94, @ranger-ross, @styfle, @itsybitsci, @Amusac, @anujbolewar, @spirosikmd, @mezotv, @Xanaado, @marcoshernanz, @mlekhi, @dacgray, @molebox, @jgruica, @zeeshan56656, @lazerg, @hamidrezahanafi, @marceloboeira, @DavidIlie, @fireairforce, @QingHeSite, @niketchandivade, @biubiukam, @seanbeirnes, @0ldh, @fabian-hiller, @hardfist, @bryan-ferry, @gdborton, @hammadxcm, @syedsohailhussain1, @kelvinampofo, @koenpunt, @mayur9210, @Jashnavi25, @akselipalmer, @m-kawafuji, @Janpot, and @kyamaz99 for helping!
