---
type: "twir-recovery"
issue: 293
item: 1
source: "https://nextjs.org/blog/next-16-3"
final_url: "https://nextjs.org/blog/next-16-3"
retrieved: "2026-10-22T11:30:00+00:00"
original_note: "frontend/raw/twir/293/articles/01 - Next.js 16.3 - Instant Navigations and 90% less RAM in dev.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/01 - Next.js 16.3 - Instant Navigations and 90% less RAM in dev|Next.js 16.3 - Instant Navigations and 90% less RAM in dev]]

---
title: Next.js 16.3
description: Next.js 16.3 introduces Instant Navigations, a suite of tools for single-page-app responsiveness, plus a faster dev server, faster builds, and improved tooling for AI agents.
url: "https://nextjs.org/blog/next-16-3"
docs\_index: /docs/llms.txt
publishedAt: August 3rd 2026
---
Last month we published a preview release of 16.3 that let you try out [SPA-like navigations](/blog/next-16-3-instant-navigations), better [AI tooling](/blog/next-16-3-ai-improvements), and a \_much\_ less memory-hungry [dev server](/blog/next-16-3-turbopack).
Today, we're excited to announce that Next.js 16.3 is here!
This release is packed with improvements for all existing Next.js apps:
- [\*\*Less memory usage in dev.\*\*](#less-memory-usage-in-dev) Long dev sessions now use up to 90% less RAM.
- [\*\*Faster builds.\*\*](#faster-builds) Repeat builds can read unchanged artifacts from cache.
- [\*\*Faster type checking.\*\*](#faster-type-checking-with-typescript-7) `next build` can use TypeScript 7 for type checking.
- [\*\*Faster server-side rendering.\*\*](#faster-server-side-rendering) Next.js now handles up to 22% more requests under load.
- [\*\*Versioned docs for AI agents.\*\*](#versioned-docs-for-ai-agents) Coding agents read version-matched docs with no setup.
- [\*\*Fewer prefetch requests.\*\*](#fewer-prefetch-requests) Links trigger fewer requests by bundling smaller payloads.
- [\*\*Better caching for static assets.\*\*](#better-caching-for-static-assets) Immutable assets can optionally be reused across deploys.
- [\*\*Custom error boundaries.\*\*](#custom-error-boundaries) Recover from server errors by re-fetching failed data.
- [\*\*Built-in glob imports.\*\*](#built-in-glob-imports) Import multiple files with a new Turbopack API.
- [\*\*Root params.\*\*](#root-params) Easily access root-level params like `[lang]` from any Server Component.
It also includes \*\*Instant Navigations\*\*, an opt-in suite of tools that brings the responsiveness of client-driven SPAs to Next.js, without sacrificing the benefits that come with its server-driven model:
- [\*\*Instant Insights.\*\*](#instant-insights) A new devtool that automatically surfaces slow navigations.
- [\*\*Partial Prefetching.\*\*](#partial-prefetching) Fine-grained control over how much content a link should prefetch.
- [\*\*Better Incremental Static Regeneration.\*\*](#better-incremental-static-regeneration-isr) URLs omitted from build-time prerendering can now serve an instant loading shell to the first visitor.
- [\*\*Navigation Inspector.\*\*](#navigation-inspector) A new devtool that lets you visually inspect a navigation's loading shell.
- [\*\*Playwright test helper.\*\*](#playwright-test-helper) Write regression tests that prevent refactors from making a navigation slow.
The behaviors behind Instant Navigations will become the default in a future major version, as they're part of our work over the last year to simplify Next.js back to its roots: dynamic by default, with no hidden or implicit caching.
16.3 also includes [experimental features](#experimental-features) you can try today, such as the Rust-based React Compiler and network resilience.
---
This is our biggest update to the framework since Next.js 16.0 came out last November, and we can't wait for you to try it.
Upgrade by installing the latest version of `next` from npm:
```bash filename="terminal"
npm install next@latest
```
...and keep reading to learn about everything that's new!
## Improvements for today's apps
Next.js 16.3 includes improvements for all existing projects, including lower dev server memory usage, faster rendering, and better runtime performance, all with zero changes to your application code.
We recommend all apps upgrade to 16.3 to start getting these benefits today.
### Less memory usage in dev
In 16.3, Turbopack uses \*\*up to 90% less memory\*\* when running `next dev`. The reduction comes from two new features that are now enabled by default: disk caching for dev (first introduced in 16.1), and memory eviction.
We've been hearing [great reports](https://github.com/vercel/next.js/discussions/95130#discussioncomment-17439239) from early adopters, and we're excited to bring these performance improvements to all Next apps.
Learn more about [Turbopack's new memory eviction features](/docs/app/api-reference/config/next-config-js/turbopackMemoryEviction).
### Faster builds
The disk caching feature that's been speeding up dev since 16.1 now works with `next build` and is enabled by default. We've been dogfooding this in production at Vercel for months and are seeing some projects with \*\*5.5x faster builds\*\* on CI.
Learn more about setting up [Turbopack's new FileSystem Cache](/docs/app/api-reference/config/next-config-js/turbopackFileSystemCache).
### Faster type checking with TypeScript 7
[Typescript 7](https://devblogs.microsoft.com/typescript/announcing-typescript-7-0/) was released last month, which is a 10x faster native port of TypeScript with much faster type checking.
To start using TypeScript 7 for type checking during `next build`, just bump your project's local dependency:
```shell
pnpm add -D typescript@^7
```
Learn more about [configuring TypeScript's CLI in Next.js](/docs/app/api-reference/config/next-config-js/useTypeScriptCli).
### Faster server-side rendering
We replaced web streams with native Node.js streams in the App Router rendering layer, removing the overhead of converting between the two during server-side rendering.
In our benchmarks, apps handle up to \*\*22% more requests under load\*\*, with no changes to application code.
Read the [native Node.js streams PR](https://github.com/vercel/next.js/pull/94311) for more details.
### Versioned docs for AI agents
AI coding agents now automatically read documentation that matches your project's version of Next.js.
Running `next dev` writes and maintains a version-matched `AGENTS.md` block that points directly to the bundled docs in your project's local node modules. With that knowledge now reaching agents directly, we're retiring [our earlier Skills](https://github.com/vercel-labs/next-skills) that existed solely to bring current documentation to your apps.
Learn more about [setting up Next.js for AI coding agents](/docs/app/guides/ai-agents).
{/\* prettier-ignore \*/}
{/\* But Skills are still useful for longer multi-step workflows, and Next.js 16.3 adds several new first-party Skills focused on that work.
The [`next-dev-loop`](https://www.skills.sh/vercel/next.js/next-dev-loop) Skill gives your agent a repeatable way to inspect the running app, make an edit, and verify the result using the Next.js dev server and [`agent-browser`](https://github.com/vercel-labs/agent-browser):
```bash filename="terminal"
npx skills add vercel/next.js --skill next-dev-loop
```
Read our guide on [setting up Next.js for AI coding agents](/docs/app/guides/ai-agents).
For a deeper dive into these AI tooling improvements, read [Next.js 16.3: AI Improvements](/blog/next-16-3-ai-improvements). Later in this post, other Skills build on `next-dev-loop`. \\*/}
### Fewer prefetch requests
In 16.3, prefetches below a certain payload size are automatically bundled together to reduce the overall amount of prefetch requests your app makes.
Prefetches for larger shared segments still remain separate, so they can be reused across multiple routes.
Learn more about [prefetch inlining](/docs/app/api-reference/config/next-config-js/prefetchInlining).
### Better caching for static assets
Immutable static assets can now be reused across deployments. Since they're immutable, they cannot suffer from issues related to skew.
Learn more about [immutable static assets](/docs/app/api-reference/adapters/immutable-static-assets).
### Custom error boundaries
Previously, React error boundaries in Next.js interfered with application code that called `notFound` or `redirect`. They also could only reset client-side state, and gave you no way to retry Server Components that failed during rendering.
In Next.js 16.3, you can use `catchError` to define a custom error boundary that doesn't interfere with `notFound` or `redirect`:
```tsx filename="app/my-error-boundary.tsx"
'use client';
import { catchError, type ErrorInfo } from 'next/error';
function ErrorFallback(props: { title: string }, { error, retry }: ErrorInfo) {
return (

## {props.title}

{error.message}

 retry()}>Try again

);
}
export default catchError(ErrorFallback);
```
The boundary also receive a `retry()` function that you can call to refetch the boundary's children, which can include rerendering any Server Components.
Learn more about [custom error boundaries](/docs/app/getting-started/error-handling#nested-error-boundaries).
### Built-in glob imports
Turbopack now supports loading multiple modules from the file system using the Vite-compatible `import.meta.glob` API, which brings hot-module reloading and other benefits to Server Components that read from local files:
```tsx filename="app/blog/page.tsx"
import matter from 'gray-matter';
export default function Page() {
// .md needs a loader registered in next.config.js
const posts = import.meta.glob('./posts/\*.md', { eager: true });
return (

{Object.entries(posts).map(([path, mod]) => {
const { data } = matter(mod.default);
return- {data.title}
;
})}
);
}
```
Learn more about [glob imports](/docs/app/api-reference/turbopack#importmetaglob).
### Root params
Previously, the only way to access a dynamic route's params was to pass them down as props from the route's page.
This led to excessive prop-drilling for params defined above the root layout, which are effectively global and therefore likely to be used throughout your component tree.
Next.js 16.3 introduces a new feature for easily accessing these \_root params\_ from any Server Component, without the need for passing props:
```tsx {1,7} filename="app/[lang]/posts/[slug]/page.tsx"
import { lang } from 'next/root-params';
export default async function PostPage(
props: PageProps<'/[lang]/posts/[slug]'>,
) {
const { slug } = await props.params;
const language = await lang();
return (

Language: {language}

Post: {slug}

);
}
```
This makes it much more ergonomic for things like internationalization, where many shared utilities and deeply nested components need access to the current language. Additionally, root params also work inside of `use cache` scopes.
They're currently supported in Server Components, and we're planning on adding support for route handlers and Server Actions in a future release.
Learn more about [root params](/docs/app/api-reference/functions/next-root-params).
---
So that's what's new for every app that upgrades today. But 16.3 includes an exciting set of opt-in features that are paving the way for the next major version of the framework, and we're excited to dig into those next.
## Instant Navigations
Over the past year, we've been working on fixing the most frustrating things about building with Next.js.
Server Components helped apps ship less JavaScript and avoid network waterfalls, but they made navigations feel slow. The caching model was implicit, confusing, and not helpful for dynamic apps. Prefetching was too aggressive and costly.
Last November, we introduced a new caching primitive to the framework: the `'use cache'` directive. It's more explicit and composable than our previous server-side caching APIs, and now, it also brings client-side caching to Next.js for the first time.
We've been building on this primitive to address the navigation, caching, and prefetching problems above, and we ended up with a simpler, more powerful programming model. Server Components and Suspense are still the two primary building blocks, and `'use cache'` now integrates with them in a way that lets you build apps that are static, dynamic, or \_anywhere\_ in between.
For a deeper dive on these new behaviors, read [last month's announcement of Instant Navigations](/blog/next-16-3-instant-navigations).
In 16.3, you can start using building with all these new features by enabling two flags:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
cacheComponents: true,
partialPrefetching: true,
};
export default nextConfig;
```
And if you have existing projects to upgrade, you or your agent can [migrate an app to Cache Components](/docs/app/guides/migrating-to-cache-components).
Here's a look at what's getting better in Next.js.
### Instant Insights
While Server Components made Next.js apps faster at fetching data and rendering \_complete\_ pages, apps built with prior versions of Next.js often felt \_less responsive\_ than their client-driven counterparts (like SPAs), since those apps could render instant loading states without fetching from the server whenever you clicked a link.
It was possible to do this using separate `loading.tsx` files for each route, but it was far too easy to forget one and end up with a slow navigation.
We've fixed this by letting components that render dynamic UI either define inline loading states with Suspense, or mark part of their UI as prerenderable with `'use cache'`.
In either case, Next.js can extract this UI and load it into the client prior to a navigation, making your app feel as snappy as an SPA once users start clicking around it.
To ensure you don't miss a slow page, the Next.js DevTools now include \*\*Instant Insights\*\*, which surfaces any navigations you encounter that are not instant:
![]()

The new Instant Insights panel automatically surfaces slow navigations

Prefetching that UI ensures your server-rendered app always has \_some\_ UI ready to show the moment a user clicks a link, similar to how you would model loading states in an SPA.
Each insight also provides a prompt that teaches your agent how to apply your chosen fix.
Learn more about [Instant Insights](/docs/app/guides/instant-navigation#validate-instant-navigation).
### Partial Prefetching
Prior to 16.3, prefetching in Next.js was limiting: you could either define a reusable loading shell with `loading.tsx`, or opt-in to aggressive full-page prefetching with ``. Many apps suffered from these implicit and restrictive APIs, and ended up with blocking navigations on link clicks as a result.
To fix this, 16.3 adds a new prefetching behavior we call \*\*Partial Prefetching\*\*. Next.js can extract reusable loading shells from \_any\_ route's UI, and per-link prefetching via `` can include as much \_or as little\_ content from the target page as you like.
Learn how you or your agent can [adopt Partial Prefetching in your app](/docs/app/guides/adopting-partial-prefetching).
### Better Incremental Static Regeneration (ISR)
16.3 brings a new kind of Incremental Static Regeneration to dynamic, personalized apps. When you prerender only \_some\_ of a route's pages at build time with `generateStaticParams`, the rest of the page faced a tradeoff. They could show a loading shell but never get prerendered, or skip the shell and block the first visitor.
Now you get both. A page you don't prerender serves an instant loading shell on its first visit, then upgrades to the fully prerendered page in the background. Every later visitor gets the final content from the cache.
We're also exploring an API to control how often a page upgrades, for example based on traffic.
Learn more about [Incremental Static Regeneration with Cache Components](/docs/app/guides/incremental-static-regeneration-cache-components).
### Navigation Inspector
Because Next.js disables prefetching in development, it can be hard to understand exactly what a user will see during a particular navigation's loading sequence.
The new Navigation Inspector lets you pause page loads and client-side navigations at the shell, so you can see exactly what loading state the user would see:
![]()
See our documentation on [visualizing loading states with the Next.js DevTools](/docs/app/guides/instant-navigation#visualize-loading-states-with-the-nextjs-devtools).
### Playwright test helper
Another common failure mode is a page that navigates instantly today becoming slow tomorrow. Maybe a component that reads `cookies()` gets added to a shared header and de-opts the route to request-time rendering, or a `` boundary moves during a refactor and part of the page starts blocking. Either way, UI that used to appear immediately no longer does.
The new `instant()` test helper lets you write Playwright tests that assert exactly what content should be instantly visible during a navigation. The test fails whenever the instant UI changes, no matter the cause:
```ts {7-12} filename="e2e/instant-navigation.spec.ts"
import { expect, test } from '@playwright/test';
import { instant } from '@next/playwright';
test('product title is available immediately', async ({ page }) => {
await page.goto('/products/shoes');
// Assert what's visible without waiting for network
await instant(page, async () => {
await page.click('a[href="/products/hats"]');
await expect(page.locator('h1')).toContainText('Baseball Cap');
await expect(page.getByText('Checking inventory...')).toBeVisible();
});
await expect(page.getByText('12 in stock')).toBeVisible();
});
```
Learn more about [writing tests with the `instant` test helper](/docs/app/guides/instant-navigation#prevent-regressions-with-e2e-tests).
---
That's everything that's new with Instant Navigations! We're excited for you to try out these new features and hear what you think.
Lastly, there's a few new experimental features shipping with 16.3.
## Experimental features
Alongside the stable release, 16.3 ships a few experimental features you can opt into today behind configuration flags. They're still evolving, so let us know how they're working for you in the [Next.js 16.3 feedback discussion](https://github.com/vercel/next.js/discussions/95130).
### Rust-based React Compiler
The React Compiler optimizes your components at build time so you don't have to hand-tune memoization.
Until now, enabling the React Compiler meant running it through Babel in Node.js. The experimental Rust port instead runs directly inside Turbopack, avoiding the extra work of generating and reparsing code.
Enable the compiler and opt into the Rust version in your Next.js config:
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
In tests against large apps like [v0](https://v0.app), the Rust path cut the time from `next dev` to a ready page by 34% on a cold build and 46% on a warm one. These gains assume you've moved off Babel entirely. If you still run Babel for other transforms, the Rust compiler helps, but the gain is smaller.
Learn more about [the Rust React Compiler](/docs/app/api-reference/config/next-config-js/turbopackRustReactCompiler).
### Network resilience
When the network drops, a soft navigation, data fetch, or Server Action normally throws. With `experimental.useOffline` enabled, Next.js keeps it pending instead and retries once the connection returns. Enable the flag in your Next.js config:
```ts filename="next.config.ts"
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
useOffline: true,
},
};
export default nextConfig;
```
Because [Partial Prefetching](#partial-prefetching) already caches a route's shell on the client, a prefetched route still renders that shell when you navigate to it offline, and its data streams in once you reconnect.
A new `useOffline` hook reports when the app is offline, so you can show the user what's happening:
```tsx filename="app/offline-banner.tsx"
'use client';
import { useOffline } from 'next/offline';
export function OfflineBanner() {
const isOffline = useOffline();
if (!isOffline) return null;
return

You're offline. Retrying when you reconnect.

;
}
```
Read our guide on [handling connectivity drops](/docs/app/guides/offline-support).
## Feedback and Community
We hope you're excited to try out Next.js 16.3!
Upgrade today:
```bash filename="terminal"
npm install next@latest
```
And share your feedback to help shape the future of Next.js:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
## Contributors
Next.js is the result of the combined work of thousands of individual developers. This release was brought to you by:
- The \*\*Next.js\*\* team: [Andrew](https://github.com/acdlite), [Aurora](https://github.com/aurorascharff), [Dan](https://github.com/gaearon), [Hendrik](https://github.com/unstubbable), [Janka](https://github.com/lubieowoce), [Jiwon](https://github.com/devjiwonchoi), [Joseph](https://github.com/icyJoseph), [Josh](https://github.com/gnoff), [Jude](https://github.com/gaojude), [Pete](https://github.com/petehunt), [Sam](https://github.com/samselikoff), [Sebbie](https://github.com/eps1lon), [Tim](https://github.com/timneutkens), and [Zack](https://github.com/ztanner).
- The \*\*Turbopack\*\* team: [Andrew](https://github.com/andrewimm), [Benjamin](https://github.com/bgw), [Jimmy](https://github.com/jimmyhmiller), [Luke](https://github.com/lukesandberg), [Niklas](https://github.com/mischnic), [Tobias](https://github.com/sokra), and [Will](https://github.com/wbinnssmith).
Huge thanks to @denesbeck, @ztanner, @ijjk, @lllomh, @devjiwonchoi, @lukesandberg, @wbinnssmith, @sokra, @unstubbable, @timneutkens, @feedthejim, @gnoff, @abhishekmardiya, @icyJoseph, @mischnic, @mmastrac, @acdlite, @eps1lon, @JamBalaya56562, @bgw, @gaojude, @bgub, @remcohaszing, @aurorascharff, @VedantMadane, @fireairforce, @dagecko, @ctate, @banchichen, @andrewimm, @wwenrr, @TooTallNate, @hamidrezahanafi, @hamedniroomand, @sleitor, @Badbird5907, @MukundaKatta, @styfle, @SukkaW, @awo00, @christopherkindl, @GuinsooRocky, @maximecolin, @lubieowoce, @zana-abdi2002, @samselikoff, @rishishanbhag, @armando-andre, @tim123abc, @publictheta, @unclebay143, @yavorpunchev, @kakadiadarpan, @SyMind, @igorbabko, @sampoder, @StanislavKozachenko, @kristiyan-velkov, @huozhi, @RazinShafayet2007, @SJvaca30, @danyalahmed1995, @karlhorky, @MikhailStn, @ifer47, @niketchandivade, @gilest, @jahanzaib-iqbal-dev, @owenpearson, @davidgg, @fhfournier, @parkhojeong, @gaearon, @TariqulislamTuhin, @thsid, @jimmyhmiller, @Partha-Shankar, @M4cM4rco, @chippleh1392, @Pranav18M, @marcoshernanz, @manoraj, @ankurdotio, @WildChargerTV, @ZaforAbdullah, @wasim-builds, @petehunt, @DavidIlie, and @adhamfayrouzamf for helping!
