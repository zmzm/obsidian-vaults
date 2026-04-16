---
type: twir-item
issue: 269
item: 7
item_type: item
date: 2026-02-18
source: https://dev.to/elvissautet/nextjs-finally-has-competition-2lg7
tags:
  - "TanStack"
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-02-18-TWIR-269|Index]]

# Item 7: Next.js Finally Has Competition (TanStack Start)

Source: [https://dev.to/elvissautet/nextjs-finally-has-competition-2lg7](https://dev.to/elvissautet/nextjs-finally-has-competition-2lg7)

Summary:
TanStack Start is positioned as a serious alternative to Next.js, addressing pain points with React Server Components and execution boundaries. The article provides a deep, practical comparison, showing how TanStack Start offers explicit server/client separation, type safety, and a more predictable developer experience. It includes real code examples and discusses the trade-offs of each framework.

Key takeaways:
- Next.js's Server Components model introduces complexity around server/client boundaries and serialization.
- TanStack Start, built by the creator of React Query and TanStack Router, emphasizes explicitness and type safety.
- The new framework allows normal React patterns without "use client" directives or file splitting.
- The article is data-driven and offers actionable advice for framework selection.

Recommendation:
Read fully (for developers choosing a React framework or interested in the future of full-stack React)

Why it matters:
for developers choosing a React framework or interested in the future of full-stack React

Content:
# Next.js Finally Has Competition

Next.js made React easy. TanStack Start made React feel like React again.

If you're picking a framework for something real in February 2026, this is the article I wish someone had written for me. Not a feature matrix. Not a "both are great" dodge. I did the research so you don't have to redo it. Every number is sourced. Every claim is verifiable. You'll know exactly which framework to pick by the end, and it'll be different depending on what you're building.

Next.js 16.1.6. TanStack Start 1.159.5 RC. Current as of today.

## The five-year answer is dead

For five years, there was one answer. Someone asks "what React framework should I use?" and you say Next.js. Meeting over.

That answer worked because it was true. Next.js gave you file-based routing, server-side rendering, image optimization, and a deployment story so smooth it felt illegal. Vercel made the framework, Vercel ran the hosting, and the DX was great. You shipped, it worked, you moved on with your life.

Then in 2023, the App Router replaced the Pages Router, and React Server Components became the default mental model. Every component became a Server Component unless you opted out with `"use client"`. Server Actions let you write backend logic inside frontend files. Three separate caching layers ran automatically under the hood. The promise was incredible: less JavaScript shipped to the browser, faster page loads, simpler data fetching.

The reality was different.

A GitHub discussion titled "With the new App Router, are people putting 'use client' everywhere?" has been open since 2023. People are still commenting on it in 2026. The most common complaint isn't that Server Components don't work. It's that developers can't predict when their code runs on the server and when it runs in the browser. The boundary between the two environments is invisible until it breaks.

Next.js 16 fixed the caching problem. All dynamic code now runs at request time by default. You opt into caching explicitly with the new `"use cache"` directive. This is a massive improvement over the old implicit caching that confused everyone. Credit where it's due: Vercel listened and fixed the biggest pain point.

But the architectural tension remains. Your app is split into two execution environments, and you're responsible for managing the boundary between them. Some developers thrive in this model. Others spend more time debugging serialization errors than building features.

Meanwhile, in Utah, a furniture-making open source developer had a different idea.

## The most mass-adopted solo developer in React history

Tanner Linsley built React Query. That library that replaced your 200-line Redux saga with 5 lines of `useQuery` and just worked. Before React Query, managing server state in React was a pain that entire teams spent weeks solving poorly. After React Query, it was a solved problem. 12 million weekly downloads. Used at Apple, Google, Netflix, Amazon, Walmart.

Same person built React Table. Same person built React Virtual. Same person built TanStack Router, which quietly became the most type-safe router in the React ecosystem. 13 open source projects, 112,660 GitHub stars across them, over 4 billion total downloads. 1.3 million repositories depend on his code.

Two years ago, he went full-time on open source. Built a team of 36 contributors. Funds them properly. Ships at a pace that shouldn't be possible for an independent project.

TanStack Start is his full-stack React framework. Built on TanStack Router and Vite. The philosophy is simple: your code should be explicit about what runs where, types should catch errors before runtime does, and you shouldn't need a $500/month hosting platform to serve a React app.

It's still a Release Candidate. That matters, and I'll explain exactly how much.

## The code tells the real story

Here's a dashboard page in Next.js 16:

```
// app/dashboard/page.tsx
export default async function Dashboard() {
  const stats = await db.getStats()
  return <StatsView data={stats} />
}
```

Enter fullscreen mode

Exit fullscreen mode

Clean. The component fetches data on the server. No loading state, no useEffect, no state management. The component IS the data layer. This is Server Components at their absolute best, and it's a real achievement in developer experience.

But now your PM says the dashboard needs a filter button.

You can't add `useState` to this file. Server Components don't support hooks. So you create a new file:

```
// app/dashboard/stats-view.tsx
'use client'

import { useState } from 'react'

export function StatsView({ data }) {
  const [filter, setFilter] = useState('all')
  const filtered = data.filter(d => filter === 'all' || d.type === filter)
  return (
    <>
      <button onClick={() => setFilter('revenue')}>Revenue</button>
      <DataTable rows={filtered} />
    </>
  )
}
```

Enter fullscreen mode

Exit fullscreen mode

One `useState` and you need a separate file, a `"use client"` directive, and an understanding of serialization boundaries. The `data` prop crossed from server to client, which means it was serialized as JSON, which means you can't pass functions, Dates, Maps, Sets, or class instances through it. If your stats object had a Date field, it arrived as a string. If it had a method, it vanished.

The more interactive your app gets, the more files carry `"use client"`, and the less Server Components actually help you. For content-heavy pages with minimal interactivity, this model is brilliant. For dashboards, admin panels, data-heavy apps? You're fighting the architecture more than leveraging it.

Same page in TanStack Start:

```
// routes/dashboard.tsx
import { createFileRoute } from '@tanstack/react-router'
import { createServerFn } from '@tanstack/react-start'
import { useState } from 'react'

const getStats = createServerFn({ method: 'GET' })
  .handler(async () => {
    return db.getStats()
  })

export const Route = createFileRoute('/dashboard')({
  loader: () => getStats(),
  component: Dashboard,
})

function Dashboard() {
  const stats = Route.useLoaderData()
  const [filter, setFilter] = useState('all')
  const filtered = stats.filter(d => filter === 'all' || d.type === filter)

  return (
    <>
      <button onClick={() => setFilter('revenue')}>Revenue</button>
      <DataTable rows={filtered} />
    </>
  )
}
```

Enter fullscreen mode

Exit fullscreen mode

One file. The server function is explicitly declared. The component is a normal React component that uses any hook it wants. There's no invisible boundary. When the page loads, the loader runs `getStats()` on the server, hydrates the result, and the component renders with full interactivity from the start.

You didn't have to think about which execution environment you're in. The server function runs on the server because you said so. Everything else runs wherever React runs. There's nothing to debug because there's nothing hidden.

Now here's the part nobody writes about: the TypeScript experience.

In Next.js, `params` in a dynamic route come as `Promise<{ id: string }>` since version 15. Search params are untyped strings. If your route is `/users/[id]` and someone navigates to `/users/abc` when your code expects a number, you find out at runtime.

In TanStack Start, route params are inferred from the file path and validated at the route level. Search params get full Zod validation. If your loader expects `params.id` as a number, TypeScript catches `string` at compile time. If your search params need `?page=number&sort=string`, you define the schema once and every component that reads those params gets autocomplete, validation, and error handling for free.

This isn't a nice-to-have. This is the difference between catching a bug in your editor and catching it in production at 2am.

And the middleware story makes the gap wider. TanStack Start middleware works at both the request level and the server function level, on both client and server. You chain middleware together and each layer passes typed context to the next. Your auth middleware validates a session and provides a `user` object. Your permissions middleware receives that typed `user` and checks access. Your logging middleware receives both. Every layer has full type inference. No `any` casts. No runtime surprises.

```
const authMiddleware = createMiddleware().server(async ({ next }) => {
  const user = await validateSession()
  if (!user) throw redirect({ to: '/login' })
  return next({ sendContext: { user } })
})

const getProtectedData = createServerFn({ method: 'GET' })
  .middleware([authMiddleware])
  .handler(async ({ context }) => {
    // context.user is fully typed here. No cast needed.
    return db.getData(context.user.id)
  })
```

Enter fullscreen mode

Exit fullscreen mode

In Next.js 16, `middleware.ts` was renamed to `proxy.ts`. It runs at the network edge, before your application code. It can't access your database, can't run server-side logic, and has a fundamentally different execution model from your route handlers. For anything beyond redirects and header manipulation, you need Server Actions or API routes, which are separate concepts with separate mental models.

## The SEO myth that won't die

This is the section that saves people the most time, because the #1 reason developers default to Next.js without thinking is SEO. The assumption goes: Next.js does SSR and static generation, Google loves it, and TanStack Start is the new kid so it probably can't compete. Right?

Wrong. And it's not even close to right.

TanStack Start ships with full SSR enabled by default. When Googlebot hits your page, it receives completely rendered HTML with all your content visible. No JavaScript execution required for crawling. This is the same thing Next.js does. The HTML arrives complete from the server.

But let me show you what TanStack Start's SEO tooling actually looks like, because nobody talks about this:

```
export const Route = createFileRoute('/posts/$postId')({
  loader: async ({ params }) => {
    const post = await fetchPost(params.postId)
    return { post }
  },
  head: ({ loaderData }) => ({
    meta: [
      { title: loaderData.post.title },
      { name: 'description', content: loaderData.post.excerpt },
      { property: 'og:title', content: loaderData.post.title },
      { property: 'og:image', content: loaderData.post.coverImage },
      { name: 'twitter:card', content: 'summary_large_image' },
    ],
    scripts: [
      {
        type: 'application/ld+json',
        children: JSON.stringify({
          '@context': 'https://schema.org',
          '@type': 'Article',
          headline: loaderData.post.title,
          author: { '@type': 'Person', name: loaderData.post.author.name },
          datePublished: loaderData.post.publishedAt,
        }),
      },
    ],
  }),
  component: PostPage,
})
```

Enter fullscreen mode

Exit fullscreen mode

That's meta tags, Open Graph, Twitter Cards, AND JSON-LD structured data, all driven by typed loader data, all rendered server-side before the page hits the browser. The `head` function receives the same typed `loaderData` your component gets, so your SEO metadata is always in sync with your page content. No separate data fetch for meta tags. No chance of the title saying one thing while the page shows another.

TanStack Start also has static prerendering and automatic sitemap generation:

```
// vite.config.ts
tanstackStart({
  prerender: {
    routes: ['/blog', '/blog/posts/*'],
    crawlLinks: true,  // discovers all linked pages automatically
  },
  sitemap: {
    enabled: true,
    host: 'https://yoursite.com',
  },
})
```

Enter fullscreen mode

Exit fullscreen mode

Static HTML pages at build time. Automatic link crawling to find every route. Generated `sitemap.xml`. And ISR (Incremental Static Regeneration) using standard HTTP cache headers that work with any CDN. Not just Vercel's.

TanStack Start even has LLMO documentation (LLM Optimization) for the AI search era. As traffic from Perplexity, ChatGPT search, and Google AI Overviews grows, the docs show how to structure content for AI crawlers, including `llms.txt` support, the AI equivalent of `robots.txt`. Next.js doesn't have this in their docs yet.

So where does Next.js actually have a real SEO edge? Two specific places.

First, `next/image`. Automatic responsive images, format conversion to WebP/AVIF, lazy loading, and built-in CDN delivery. Image-heavy sites get measurably better Core Web Vitals. TanStack Start has no image component. You'll use Cloudflare Image Resizing, imgproxy, or a similar third-party service. It works, but it's not zero-config.

Second, Partial Prerendering. Next.js 16 can serve a static shell instantly while streaming dynamic content into Suspense boundaries. The static parts hit the browser before the server finishes computing the dynamic bits. For content sites with some personalization (user avatar in the corner, live comments below a static article), this is a real performance win that TanStack Start can't match today.

But for the actual SEO fundamentals (server-rendered HTML, meta tags, structured data, sitemaps, static generation, ISR), the two frameworks are at parity. If someone tells you TanStack Start is bad for SEO, they haven't looked at it since 2024.

## The numbers nobody argues with

I'm pulling from four sources: GitHub issues with reproduction repos, the Inngest engineering blog (a real company that migrated), Vercel's own documentation, and heap snapshots from open issues.

**Dev server memory.**

TanStack Start dev server sits at roughly 200MB and stays there. Vite does almost nothing at startup. It only transforms files when you request them.

This matters if you're on a laptop. This matters a lot if your team is in Nairobi or Lagos on 8GB machines where the dev server competing with Chrome and Figma means constant swapping.

**Production memory.**

This is where it gets serious. GitHub issue #88603, filed January 2026 against Next.js 16.1.0, documents memory leaks causing OOM crashes in Docker and Kubernetes. Linear memory growth over hours until the pod gets killed and restarts. Issue #85914 from November 2025 reproduces it with just `output: standalone` and a single `fetch` call. The reporter tested Node 20, 22, and 24. Same behavior on all versions.

There are currently 6 open GitHub discussions about Next.js memory leaks in containerized environments, spanning from 2021 to January 2026. The pattern is the same: memory grows linearly, garbage collection doesn't reclaim it, pods restart.

I haven't found equivalent reports for TanStack Start. That's likely because fewer people run it in production. But the thinner runtime (no RSC protocol, no flight format, no custom serialization layer) means less surface area for leaks. Take that with the context it deserves.

**Build speed.**

Turbopack is legitimately fast. 2-5x faster builds than Webpack. This is one of Next.js 16's biggest wins and the numbers hold up. The filesystem caching is excellent too. Restarts are near-instant when the cache is warm.

TanStack Start uses Vite, which was already fast. Build times are comparable. Neither framework will bottleneck your CI pipeline in 2026.

**Bundle size.**

Next.js baseline is around 92KB gzipped. With Server Components, pages that are mostly static content can ship significantly less JavaScript because component code stays on the server.

TanStack Start baseline is around 42KB. Everything hydrates on the client, so more JavaScript ships, but the total is still smaller because there's no RSC runtime overhead, no flight protocol, no serialization layer.

For content sites where Server Components shine, Next.js ships less JS. For interactive apps where most components end up as `"use client"` anyway, TanStack Start ships less. Know your app before you optimize.

**Real migration data.**

Inngest, a developer tools company, published their migration story in early 2026. Before, on Next.js: 10-12 second local page loads on every route. After, on TanStack Start: 2-3 seconds on first load, instant on subsequent routes. Migration took 2 weeks with 1 engineer using AI assistance. The quote that circled their Slack: "I cannot believe how snappy it is."

Another team documented a 60% reduction in build times after migrating a production app from Next.js 16, along with eliminating hydration errors entirely.

Two data points, not a trend. But they're consistent with what the architecture predicts.

## The security incident you need to know about

In December 2025, CVE-2025-55182 was assigned to the React Server Components protocol. CVSS score: 10.0 out of 10. Maximum severity. Unauthenticated remote code execution affecting all Next.js App Router deployments.

Six CVEs total in two months, all related to the RSC implementation.

This was patched. If you're on Next.js 16.1.6, you're safe. But it exposed something about the architectural difference between these frameworks that matters for your risk calculation.

React Server Components add a protocol layer between client and server. That layer has a serialization format, a transport mechanism, and a trust boundary. Every protocol layer is attack surface. This isn't a criticism of the Next.js team's security practices. It's structural: more moving parts means more things that can break.

TanStack Start uses plain HTTP for server functions. Standard request/response. The attack surface is the same as any Express or Fastify server. No custom protocol. No flight format. No novel serialization.

If you're in a regulated industry, if you have compliance requirements, or if your threat model involves more than script kiddies, this difference deserves weight.

## The money

Vercel Pro costs $20/user/month plus usage. A team of 5 pays $100/month before a single visitor hits the site. At meaningful traffic, costs climb. Teams at scale report $500-2,000+ monthly.

Next.js works fine on other platforms. AWS, Railway, Fly.io, a VPS. But the smoothest DX, the features that work without configuration, the zero-thought deployments are optimized for Vercel. This is how Vercel makes money. They built a great framework and a great hosting platform and designed them to work best together. Legitimate business model. Just know it's part of the deal.

TanStack Start deploys to anything that runs Node. A $24/month Hetzner VPS handles surprising traffic. Cloudflare CDN on the free tier covers most apps. Production setup for under $30/month.

At the same scale where teams spend $500+/month on Vercel, self-hosted TanStack Start runs for $100-400/month. Over a year, that's $5,000-20,000. Over three years with growth, $50,000-200,000.

But self-hosting means you handle deployments, monitoring, SSL, and incidents yourself. If you have 2 engineers and no DevOps experience, Vercel's premium buys you time. If you have infrastructure people, the savings are serious.

## Where Next.js wins and it's not close

**Content-driven sites.** Blog, marketing site, e-commerce catalog, docs, anything where pages are mostly text and images with light interactivity. As I covered in the SEO section, both frameworks handle the fundamentals equally well. But Server Components give Next.js an edge that matters: pages load with zero JavaScript for static parts. The `"use cache"` directive makes caching explicit and clean. Partial Prerendering serves a static shell instantly while streaming dynamic bits in. For content where milliseconds of load time affect conversion rates, this is a real advantage TanStack Start can't match today.

**Ecosystem.** TikTok, Nike, Hulu, Target, The Washington Post. Next.js runs at scales TanStack Start hasn't seen. If something breaks, there's a Stack Overflow answer. Hiring is easier because every React developer has at least some Next.js experience. Integration libraries exist for everything. Years of battle scars that you inherit for free.

**Image pipeline.** `next/image` handles responsive sizing, lazy loading, format conversion, and CDN delivery automatically. TanStack Start has no equivalent. For image-heavy sites, this alone could justify Next.js.

**Stability.** Next.js 16 is a stable release. TanStack Start is a Release Candidate. The API is frozen and Tanner has committed to no breaking changes before 1.0. But RC means fewer production deployments, fewer edge cases discovered, fewer battle scars. If you need to tell your CTO "this is production-proven," Next.js is the honest answer.

Full stop.

## Where TanStack Start wins and it's not close

**Interactive apps.** Dashboards, admin panels, internal tools, anything where users interact more than they read. In these apps, nearly every component needs client-side state, which means `"use client"` on nearly everything in Next.js, which means Server Components aren't helping. TanStack Start gives you full React everywhere without fighting an architecture designed for a different use case.

**Type safety.** Not a preference. A capability gap. Validated typed route params. Typed search params with Zod schemas. Typed loader data flowing from server to component without a single `as` cast. Typed middleware chains with context inference across layers. In Next.js, params are async Promises and search params are untyped strings. For large apps, this prevents entire categories of production bugs.

**Dev experience on real hardware.** If your dev server eats 6-10GB of RAM, that's the difference between running your app alongside Chrome and Figma, or running it alone and waiting. TanStack Start's ~200MB footprint keeps your machine responsive. For teams where 8GB or 16GB machines are the standard, this is the difference between productive and frustrated.

**Deployment freedom.** Node, Deno, Bun, Cloudflare Workers, any VPS, any container platform. No hosting provider gets preferential treatment. The framework doesn't care where you run it. For teams that want to own their infrastructure, this converts directly to money saved.

**Middleware.** Composable, typed, works at request level and server function level, on both client and server. Auth middleware provides a typed user to permissions middleware which provides typed access to data middleware. Every layer fully inferred. No `any`. In Next.js, `proxy.ts` runs at the edge with a different execution model from your route handlers. For complex backend logic, TanStack Start's middleware is the more powerful primitive.

No contest.

## Five questions that decide your framework

Stop reading comparisons. Answer these.

**1. Is your app mostly reading or mostly interacting?**

Users primarily consume content -> Next.js. Server Components eliminate JavaScript for static content. Real advantage.

Users primarily interact with the UI -> TanStack Start. You'll put `"use client"` on everything in Next.js anyway.

**2. How big is your team?**

Under 5 developers, no DevOps -> Next.js + Vercel. Deployment convenience is worth the premium.

Team already manages infrastructure -> TanStack Start. Hosting savings fund a junior dev's salary.

**3. Are you invested in TanStack already?**

Using React Query + Router + Table -> TanStack Start is a natural extension. Same team, same philosophy, same types.

Starting fresh -> Next.js has the gentler learning curve and more help available when you're stuck.

**4. Can you ship on a Release Candidate?**

Need to tell stakeholders "version 1.0, production-proven" -> Next.js.

Comfortable with RC status, can read source when docs don't cover your edge case -> TanStack Start rewards the bet with a better architecture for interactive work.

**5. What's your hosting budget?**

Tight, need cost control -> TanStack Start on a VPS. $30-100/month goes far.

Flexible, want zero infrastructure thinking -> Next.js on Vercel. Worth every dollar.

## What happens next

TanStack Start 1.0 is imminent. Frozen API, stable RC for months. When it ships, the "not production-ready" argument disappears and this becomes a pure technical decision.

RSC support is planned for TanStack Start post-1.0. When that lands, it gets the content-site advantages without the architectural complexity. That changes everything.

If you're productive on Next.js today, nothing here means you should migrate. But if you've felt the friction, if you've debugged a serialization boundary or watched your dev server consume more RAM than your production server or wondered why you can't use a basic React hook in half your files, now you know there's an alternative that solves exactly those problems.

Pick the one that matches what you're building. Not what's trending. What fits.

If this saved you a week of research, [buy me a coffee](https://buymeacoffee.com/vizboard). If you want more like this, I'm [@elvisautet](https://x.com/elvisautet) on X.

---

Related notes: [[Server Components]]
