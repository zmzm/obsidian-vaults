---
type: twir-item
issue: 276
item: 4
item_type: item
date: 2026-04-08
source: https://blog.railway.com/p/moving-railways-frontend-off-nextjs
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-04-08-TWIR-276|Index]]

# Item 4: Moving Railway's Frontend Off Next.js

Source: [https://blog.railway.com/p/moving-railways-frontend-off-nextjs](https://blog.railway.com/p/moving-railways-frontend-off-nextjs)

Summary:
Railway migrated its entire frontend from Next.js to Vite + TanStack Router, motivated by slow build times and a mismatch between Next.js's server-first philosophy and Railway's client-heavy, real-time app. The migration was completed in two large PRs with no downtime, replacing Next.js-specific APIs and reworking routing/layouts. The new stack offers faster builds, type-safe routing, explicit control, and better alignment with Railway's needs, at the cost of some built-in features and ecosystem maturity.

Key takeaways:
- Next.js's server-first model and slow builds prompted the switch; Vite + TanStack Router better fit Railway's client-driven app.
- Migration involved decoupling from Next.js APIs, extracting components, and reimplementing routing/layouts.
- Gains include faster iteration, type-safe routing, and explicit architecture; trade-offs include loss of built-in features and less mature ecosystem.
- The new stack supports Railway's deployment model with edge caching and immutable assets.

Recommendation:
Read fully (especially for teams considering framework migrations or evaluating client-first alternatives to Next.js)

Why it matters:
especially for teams considering framework migrations or evaluating client-first alternatives to Next.js

Content:
# Moving Railway's Frontend Off Next.js

Railway's entire production frontend no longer runs on Next.js. The dashboard, the canvas, [railway.com](http://railway.com/), all of it now runs on Vite + TanStack Router, and we shipped the migration in two PRs with zero downtime.

Next.js got [railway.com](http://railway.com/) from zero to a production app serving millions of users monthly. It's an excellent framework, but it stopped being the right one for our product.

Frontend builds had crept past 10 minutes. Six of those minutes were Next.js alone, half of it stuck on "finalizing page optimization." For a team that ships multiple times a day, that kind of build time isn't a minor annoyance. It's like a very expensive tax on every single iteration.

Railway’s app is overwhelmingly client-side. The dashboard is a rich, stateful interface. The canvas is real-time. Websockets are everywhere. The server-first primitives in Next.js weren't something we used, and we'd ended up building our own abstractions on top of the Pages Router just to support layouts and routing concerns that the framework didn't handle the way we needed.

We were still on the Pages Router, which made shared layouts hacky. Every layout pattern was a bolted-on workaround rather than a first-class framework primitive. The App Router would have solved some of these problems, but it leans heavily into server-first patterns, and our product is intentionally client-driven. Adopting it would have meant rebuilding around a paradigm we don't need.

We wanted a stack that matches how we actually build: explicit, client-first, and fast to iterate on. It also helps that we genuinely enjoy working with it.

For the Product team, we wanted a few niceties that help us avoid thinking about how we needed to implement our front-end and found the following to really convince us.

- Type-safe routing out of the box. Route params and search params are inferred, autocomplete works across the entire route tree, and the routes themselves are generated from the file system.
- First-class layouts. Pathless layout routes replaced all of our previous hacks with something composable and predictable.
- A dev loop fast enough that you stop thinking about it. Instant HMR, near-zero startup time. The feedback cycle between changing code and seeing the result effectively disappears.
- SSR where it actually matters. Marketing pages, the changelog, careers. Pure client-side everywhere else, because we're not going to force server rendering on screens that don't benefit from it. (Ed: This Blog, ironically isn’t on Tanstack yet.)
- An explicit model. Meaning, we found TanStack to lean less on framework magic, more control over how things actually work under the hood.

Several of us tried TanStack Start over the holidays and the reaction was unanimous. We like building with it, and for a product like Railway's dashboard, that matters as much as any benchmark.

Once we made the choice, I got to work. Pre-squash before merge, I must have made 100s of commits.  
Migrating a production frontend that serves millions of users across 200+ routes is the kind of thing that usually takes months of parallel running and incremental cutover. We were on a deadline, so I did it in two pull requests.

PR 1 replaced everything Next.js-specific: `next/image`, `next/head`, `next/router`. Each was swapped for either a native browser API or a framework-agnostic alternative. This PR changed nothing about the framework itself. It just removed every dependency on it, so that PR 2 could be a clean swap.

PR 2 swapped the framework. 200+ routes migrated. We systematically extracted everything non-routing-related from page files into individual React components first, then generated all routes from the original page tree.

We then added Nitro as the server layer and replaced `next.config.js` with Nitro config, consolidating redirects (500+), security headers, and caching rules into one place. We also replaced Node.js APIs that Next.js had provided polyfills for (Buffer, `url.parse`, and others) with browser-native alternatives, which left us with cleaner code as a side effect.

Merged on an early Sunday morning. The team dogfooded immediately with a live war room in Discord, and a stream of fixes landed same day. No downtime.

Sure we gained a faster, more explicit stack, but not without trade-offs.

- Built-in image optimization. We replaced `next/image` with `<img>` tags and Fastly image optimization at the edge.
- Parts of the ecosystem. We replaced tools like `next-seo` and `next-sitemap` with small in-house equivalents. Straightforward to build, no extra dependencies.
- Maturity. TanStack Start is new, and rougher edges can be expected. We're comfortable with that because the direction is right, the maintainers are responsive, and we sponsor both Vite and TanStack because we believe in where they're going.

We run our production frontend the same way our users run theirs: preview deploys per PR, health checks, zero-downtime rollouts. When we swapped the entire build system and framework, we didn't touch infrastructure. We changed code, pushed it, and Railway handled the rest.

Fastly now serves most of our traffic directly from the edge. Marketing pages are cached, dynamic pages use ISR where needed, and our frontend servers are mostly idle as a result. Vite's asset model makes this work particularly well. Each module gets its own content-hashed chunk, so shipping a change to billing only invalidates that chunk. Returning users download kilobytes, not megabytes.

This is how we think frontends should be deployed: the build is fast, the assets are immutable and cache-friendly, and the infrastructure underneath handles rollouts, previews, and routing without you having to think about it. Your frontend framework should be optimized for iteration speed, and your infrastructure should make shipping those iterations invisible. That's the experience we're building for ourselves and for everyone on Railway.

The speed of iteration on a frontend matters more now than it ever has.

Builds that took 10+ minutes now finish in under two. The dev server starts instantly. Route changes are type-checked at the boundary. Layouts compose without workarounds.

The gap between writing code and getting it in front of users is the bottleneck, and everything we've done here, the framework swap, the edge caching, the asset model, is about closing that gap. Vite + TanStack sets us up for a world where shipping frontend changes is near-instant, and that's the world we're building toward.
