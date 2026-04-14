---
type: twir-item
issue: 275
item: 1
item_type: featured
date: 2026-04-01
source: https://nextjs.org/blog/nextjs-across-platforms
tags:
status: auto
---

[[2026-04-01-TWIR-275|Index]]

# Item 1: Next.js Across Platforms: Adapters, OpenNext, and Our Commitments

Source: [https://nextjs.org/blog/nextjs-across-platforms](https://nextjs.org/blog/nextjs-across-platforms)

Content:
# Next.js Across Platforms: Adapters, OpenNext, and Our Commitments

Next.js 16.2 introduced a stable [Adapter API](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath), built in collaboration with [OpenNext](https://opennext.js.org/), Netlify, Cloudflare, AWS Amplify, and Google Cloud. This post covers how that happened, and the commitments we're making to ensure Next.js works well on every platform:

-   [**Adapter API (stable)**](https://nextjs.org/blog/nextjs-across-platforms#the-adapter-api): A typed, versioned description of your application that any platform can target.
-   [**Test suite**](https://nextjs.org/blog/nextjs-across-platforms#the-test-suite): Shared correctness tests for every adapter, including Vercel's.
-   [**Verified adapters**](https://nextjs.org/blog/nextjs-across-platforms#verified-adapters): Open-source, community-owned adapters hosted under the Next.js organization.
-   [**Ecosystem Working Group**](https://nextjs.org/blog/nextjs-across-platforms#the-ecosystem-working-group): A standing forum for coordinating changes across providers.

## How we got here[https://nextjs.org/blog/nextjs-across-platforms#how-we-got-here](https://nextjs.org/blog/nextjs-across-platforms#how-we-got-here)

Many Next.js apps are deployed as a single Node.js server running `next start`. Hundreds of thousands of teams do this today across any number of platforms, without limitations.

But scaling apps usually involves running multiple server instances. When you do, some things need to work correctly out of the box: cached content needs to stay synchronized across instances, on-demand revalidation needs to propagate, and streaming needs to work reliably. *These are functional requirements, not optimizations.*

Then there are the performance choices you opt into: serving cached content from a global CDN, running compute at the edge, optimizing cold starts with serverless functions. Each of these adds architectural complexity on top of what already needs to be correct.

Depending on the platform and architecture, the full surface area adds up: streaming, Server Components, Partial Prerendering, middleware, Cache Components, on-demand revalidation. Each capability and how they interact with one another was never formally documented. For platform providers looking to support Next.js at full fidelity in a multi-tenant environment across evolving releases, these challenges compounded:

> When the Next.js team reached out with an offer to discuss Netlify's challenges, we started compiling a laundry list of specific issues to share, but it quickly became clear that the common thread among 90% of these was simply the lack of a documented, stable mechanism to configure and read build output. That was what we needed above all. So that's what we told Jimmy, and we're glad we did.
>
> — Philippe Serhal, Engineer at Netlify

The missing piece was an **upstream, stable, public contract** that providers could build against.

## OpenNext built the bridge[https://nextjs.org/blog/nextjs-across-platforms#opennext-built-the-bridge](https://nextjs.org/blog/nextjs-across-platforms#opennext-built-the-bridge)

[OpenNext](https://opennext.js.org/) filled that gap. It translated Next.js build output into something providers could consume, mapping framework semantics onto each provider's primitives. What started as a compatibility layer became an **early production-grade adapter**, especially on AWS, with Cloudflare and Netlify joining the effort later. OpenNext showed that Next.js build output can serve as a stable, defined interface that adapters target directly.

That insight led to a broader collaboration between the Next.js team and the OpenNext maintainers, along with engineers from Netlify, Cloudflare, AWS Amplify, and Google Cloud. We published a [Build Adapters RFC](https://github.com/vercel/next.js/discussions/77740) in April 2025, formed a working group, and have been working together with these partners since then to design, test, and validate the API.

## The Adapter API[https://nextjs.org/blog/nextjs-across-platforms#the-adapter-api](https://nextjs.org/blog/nextjs-across-platforms#the-adapter-api)

Next.js 16.2 ships with a stable, public [Adapter API](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath).

On build, Next.js now produces a typed, versioned description of your application: routes, prerenders, static assets, runtime targets, dependencies, caching rules, and routing decisions. The adapter consumes this output and maps it onto a provider's infrastructure.

Adapters implement two hooks: `modifyConfig` (when configuration loads) and `onBuildComplete` (when the full output is available). Breaking changes require a new major version of Next.js.

Vercel's adapter uses this same public contract, with no private hooks or special integration path. It is [open source](https://github.com/nextjs/adapter-vercel).

As part of the working group's feedback, we have also reworked large sections of our documentation to better explain the platform integration surface. New guides cover the [Rendering Philosophy](https://nextjs.org/docs/app/guides/rendering-philosophy), the [Deploying to Platforms](https://nextjs.org/docs/app/guides/deploying-to-platforms) feature matrix, [PPR Platform Guide](https://nextjs.org/docs/app/guides/ppr-platform-guide), [How Revalidation Works](https://nextjs.org/docs/app/guides/how-revalidation-works), and [CDN Caching](https://nextjs.org/docs/app/guides/cdn-caching).

## The test suite[https://nextjs.org/blog/nextjs-across-platforms#the-test-suite](https://nextjs.org/blog/nextjs-across-platforms#the-test-suite)

We have made the Next.js test suite available for adapter authors. It covers streaming behavior, caching interactions, client navigation, and real-world edge cases. When a new feature ships, its behavior is encoded in these tests.

Adapter authors can run the suite using any adapter and get a pass/fail answer for each feature. This is the same test suite Vercel uses for its own adapter, so the correctness bar is shared across all providers.

## Verified adapters[https://nextjs.org/blog/nextjs-across-platforms#verified-adapters](https://nextjs.org/blog/nextjs-across-platforms#verified-adapters)

To become a **verified adapter** (hosted under the [Next.js GitHub organization](https://github.com/nextjs) and listed in the [Deploying to Platforms](https://nextjs.org/docs/app/guides/deploying-to-platforms) docs), two things are required: it must be open source and pass the full test suite. By making the adapter open source it ensures there is a place for the maintenance of the adapter, so that issues can be reported and triaged. The test suite ensures the adapter's compatibility with Next.js can be measured.

Each verified adapter is owned by the team that builds it. Publishing rights, release cadence, and implementation decisions are theirs, because platforms can be very different and we can't prescribe a specific implementation.

Providers can also build and ship closed-source adapters on the same public API.

The public Adapters API ships today with:

-   **[Vercel adapter](https://github.com/nextjs/adapter-vercel)**: open source, maps Next.js output to Vercel's serverless and CDN infrastructure.
-   **[Bun adapter](https://github.com/nextjs/adapter-bun)**: a reference adapter showing how to build a complete Next.js deployment target on an alternative runtime.

Adapters for **Netlify**, **Cloudflare**, and **AWS** through OpenNext are in active development, with expected releases later this year.

> Cloudflare has been part of OpenNext since the beginning because we believed developers deserve a stable, open contract for deploying Next.js apps anywhere. The official Next.js Adapter API makes that vision real. Developers running Next.js on Cloudflare's global developer platform will now have a shared foundation to build on, one designed in collaboration with the Next.js team to keep pace as the framework evolves. We are excited to be partners in this shared effort.
>
> — Fred K Schott, Engineer at Cloudflare

## The ecosystem working group[https://nextjs.org/blog/nextjs-across-platforms#the-ecosystem-working-group](https://nextjs.org/blog/nextjs-across-platforms#the-ecosystem-working-group)

We are establishing the [Next.js Ecosystem Working Group](https://nextjs.org/ecosystem-working-group), a standing forum between the Next.js team, hosting providers, and adapter maintainers. Meeting notes will be public. If you want to join the group, please reach out to [Jimmy](https://x.com/feedthejim).

We want providers to have early visibility into upcoming changes, not find out after a release. Breaking changes come with lead time proportional to their scope. New features are tested across environments before release. The full [governance document](https://nextjs.org/ecosystem-working-group) covers the commitments in detail.

-   [The Next.js Adapter API Just Shipped: Here's What Comes Next](https://www.netlify.com/blog/the-next-js-adapter-api-just-shipped-here-s-what-comes-next) (Netlify)
-   [3 Years of OpenNext](https://opennext.js.org/news/2026-03-25-3-years-of-opennext) (OpenNext)
-   [Next.js Deployment Adapters: A Bright Future for Next.js on Google Cloud](https://firebase.blog/posts/2026/03/nextjs-adapters) (Google Cloud / Firebase)

> The collaboration between OpenNext and the Next.js team transformed a community-driven workaround into an official standard, proving that the future of web frameworks is built on openness and shared innovation.
>
> — Dorseuil Nicolas, OpenNext

Thank you to the members of the Build Adapters working group: engineers at Netlify, Cloudflare, Google Cloud, AWS Amplify, and OpenNext who invested their time co-designing this API and validating it for their platforms. Thank you to every contributor who built adapters, filed bugs, and shipped workarounds.

Next.js is used by millions of developers, and many of them run on infrastructure that isn't Vercel. They deserve the same level of reliability and the same access to new features. The Adapter API provides that: a shared contract that any platform can build on, with a public test suite that holds everyone, including us, to the same standard.

Every new feature we develop will be documented in the adapter contract. The RFC process remains open, coordinated with adapter authors as the API evolves.

## Learn more[https://nextjs.org/blog/nextjs-across-platforms#learn-more](https://nextjs.org/blog/nextjs-across-platforms#learn-more)

-   [Adapter API](https://nextjs.org/docs/app/api-reference/config/next-config-js/adapterPath)
-   [Deploying to Platforms](https://nextjs.org/docs/app/guides/deploying-to-platforms)
-   [Rendering Philosophy](https://nextjs.org/docs/app/guides/rendering-philosophy)
-   [PPR Platform Guide](https://nextjs.org/docs/app/guides/ppr-platform-guide)
-   [How Revalidation Works](https://nextjs.org/docs/app/guides/how-revalidation-works)
-   [CDN Caching](https://nextjs.org/docs/app/guides/cdn-caching)
-   [Build Adapters RFC](https://github.com/vercel/next.js/discussions/77740)
-   [Vercel adapter](https://github.com/nextjs/adapter-vercel)
-   [Next.js Ecosystem Working Group](https://nextjs.org/ecosystem-working-group)
-   [OpenNext](https://opennext.js.org/)

Key takeaways:
- No key takeaways extracted.

Recommendation: Summary sufficient
