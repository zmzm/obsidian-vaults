---
type: twir-item
issue: 258
item: 8
item_type: item
date: 2025-11-12
source: https://vercel.com/blog/vercel-the-anti-vendor-lock-in-cloud
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2025-11-12-TWIR-258|Index]]

# Item 8: Vercel: The anti-vendor-lock-in cloud

Source: [https://vercel.com/blog/vercel-the-anti-vendor-lock-in-cloud](https://vercel.com/blog/vercel-the-anti-vendor-lock-in-cloud)

Summary:
Vercel positions itself as a platform that avoids vendor lock-in by letting developers write code for their framework (e.g., Next.js), not for Vercel-specific primitives. Applications deployed on Vercel remain portable and can run on other platforms without code changes, thanks to framework-defined infrastructure and open standards. Vercel’s approach is contrasted with other cloud providers that require proprietary APIs, making migration difficult.

Key takeaways:
- Vercel emphasizes portability by supporting open frameworks and standards.
- No Vercel-specific code is required in applications.
- Next.js adapters formalize the contract between framework and platform, ensuring portability.
- Most Next.js apps run outside Vercel, demonstrating practical portability.

Recommendation:
Summary sufficient

Content:
# Vercel: The anti-vendor-lock-in cloud

Vendor lock-in matters when choosing a cloud platform. Cloud platforms can lock you in by requiring you to build against their specific primitives. Vercel takes a different approach: you write code for your framework, not for Vercel.

On AWS, you configure Lambda functions, NAT Gateways, and DynamoDB tables. On Cloudflare, you write Workers, use KV stores, Durable Objects, and bind services with Worker Service Bindings. These primitives only exist with that vendor, which means migrating to another platform requires rewriting your application architecture.

Too often, cloud platforms make these choices for you. They define proprietary primitives, APIs, and services that pull your code deeper into their ecosystem until leaving becomes impractical.

At Vercel, we believe the opposite approach creates better software and a healthier web. We want developers to stay because they want to, not because they have to. That means building open tools, embracing standards, and ensuring your code remains portable no matter where it runs.

So Vercel works differently. It interprets your framework code and provisions infrastructure automatically. Your application does not need to know it runs on Vercel. You do not need to import Vercel modules or call Vercel APIs. This is [framework-defined infrastructure](/blog/framework-defined-infrastructure).

## [Link to heading](#what-vendor-lock-in-actually-means)What vendor lock-in actually means

Vendor lock-in happens when a platform builds features that deviate from open standards, which are accessed in your application code via proprietary APIs. If your application uses those features, you cannot move to another platform without rewriting code.

When you build against vendor primitives like AWS Step Functions or Cloudflare Durable Objects, those dependencies live in your application code. Your business logic ties to platform APIs, which means moving requires rewriting that logic to work with different primitives.

Framework conventions like the Next.js App Router, Remix loaders, SvelteKit endpoints, and Nitro storage adapters work differently. You build against the framework, not the platform. Multiple platforms can run the same framework code, keeping your application portable across any infrastructure that supports it.

![Framework-defined Infrastructure means developers define infrastructure through their framework, not through vendor-specific code or logic.](/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F4BNYrHEm0rcFhgHVp6kwbA%2F90ed98ff3d469b8c881232adac8a4c10%2FFDI.png&w=1920&q=75)![Framework-defined Infrastructure means developers define infrastructure through their framework, not through vendor-specific code or logic.](/vc-ap-vercel-marketing/_next/image?url=https%3A%2F%2Fassets.vercel.com%2Fimage%2Fupload%2Fcontentful%2Fimage%2Fe5382hct74si%2F5Pn3IgUloL9oxHx63mgrrn%2Fca192b60c0f682363755a01ba70dc8d9%2FFDI_-_Dark.png&w=1920&q=75)

Framework-defined Infrastructure means developers define infrastructure through their framework, not through vendor-specific code or logic.

## [Link to heading](#framework-defined-infrastructure-means-portable-code)Framework-defined infrastructure means portable code

This portability is possible because of framework-defined infrastructure (FDI). FDI means that the platform reads your code and determines what infrastructure you need. You follow your framework's patterns, Vercel handles the rest.

Complex production applications run on Vercel without mentioning `vercel` anywhere in their codebase. They follow Next.js conventions (or Remix, SvelteKit, Nuxt, or one of 40+ supported frameworks). Vercel analyzes the build output and provisions middleware, functions, static assets, and caching accordingly.

### [Link to heading](#local-development-requires-no-vercel-tooling)Local development requires no Vercel tooling

Platforms built on vendor primitives need complex simulators for local development. Cloudflare provides Wrangler to simulate Workers locally. AWS developers use LocalStack or SAM CLI to mock Lambda and other services. These tools approximate production behavior but never match it exactly.

With FDI, you run your framework's standard development server. For Next.js, run `next dev`. For Remix, `remix dev`. The code you write runs the same way locally and in production. There's no Vercel CLI to install and no simulation layer creating differences between environments.

This architectural choice has a direct impact on portability. When you write against framework standards instead of platform primitives, your code can run elsewhere without modification.

## [Link to heading](#most-next.js-apps-already-run-outside-of-vercel)Most Next.js apps already run outside of Vercel

Next.js is the most widely deployed framework on Vercel. Because of this, some might assume that this creates lock-in, but the data shows otherwise.

Based on Next.js telemetry tracking distinct projects, approximately 70% of Next.js applications run outside of Vercel. This also likely undercounts non-Vercel deployments because Vercel deployments rarely disable telemetry, while self-hosted deployments often opt out and won't appear in the data.

Many companies currently self-host Next.js on their own infrastructure, proving this portability in practice. Walmart.com serves millions of shoppers daily on self-hosted Next.js, Nike.com operates at global scale on their own systems, and Claude.ai also built their application with Next.js on their own infrastructure. These are large-scale production applications handling massive traffic on infrastructure that these companies control.

Every major cloud vendor provides Next.js deployment options. [Netlify](https://vercel.com/kb/guide/vercel-vs-netlify), Cloudflare, AWS Amplify, Google Cloud, and Azure all support Next.js natively. For custom infrastructure setups, open source projects like OpenNext enable Next.js to run with serverless architectures similar to Vercel.

## [Link to heading](#next.js-adapters-formalize-the-framework-platform-contract)Next.js adapters formalize the framework-platform contract

Platform providers told us integration was harder than it should be. This is why the [Next.js team built Build Adapters](https://nextjs.org/blog/next-16#build-adapters-api-alpha) as explicit versioned APIs to formalize the contract between framework and platform. Adapters define what Next.js outputs, what infrastructure features each route needs, and how platforms should handle them.

Every Next.js 16 application deployed on Vercel uses the same adapter API available to other platforms. Vercel does not have special access or different integration points. The test suite Vercel uses to validate features is available to all platform providers.

This is part of our broader [Open SDK strategy](/blog/open-sdk-strategy): building frameworks, SDKs, and tools that are open, portable, and usable on any platform.

## [Link to heading](#standards-first,-portable-always)Standards first, portable always

We prioritize standard protocols wherever possible. Databases offered on the Vercel Marketplace use standard protocols like Postgres and Redis. These are provided through marketplace partners like Neon, Supabase, and Upstash, or you can connect to any instance you operate. AWS is our preferred cloud provider, so when you connect to databases hosted in the same AWS region as your application, you get low-latency connectivity.

The same philosophy extends to our AI infrastructure. [AI Gateway](https://vercel.com/ai-gateway) supports the OpenAI API format, which has been established as a de-facto industry standard by OpenAI, Anthropic, and most other model providers. Switching between calling OpenAI directly or routing through the AI Gateway requires only changing the API endpoint URL in your configuration, with no code changes needed.

Some services require proprietary APIs because no industry standard exists yet. [Vercel Sandbox](https://vercel.com/docs/vercel-sandbox) provides secure execution of untrusted code. [Edge Config](https://vercel.com/docs/edge-config) offers ultra-low latency reads with a simple `get(key)` interface for distributed configuration. Moving to alternatives would require updating your code to use their APIs. However, the difference is that these services can be called from any infrastructure, including EC2 or your own servers, without requiring you to use Vercel for hosting. When industry-standard APIs emerge for these use cases, we will implement them.

Building portable open source software is a core value at Vercel. We build open source to create an enduring business that enables us to keep developing great open source software. Our goal is to improve the default quality of software for everyone, everywhere, whether they are Vercel customers or not.

When developers learn Next.js, Nuxt, or the AI SDK, they need to trust that investment won't trap them on a single platform. That trust drives broader adoption. Broader adoption creates a larger ecosystem. A larger ecosystem makes every platform better, including Vercel.

We want you to stay with Vercel because you choose to, not because you have to. The best way to earn that choice is to build tools that work everywhere and a platform that makes those tools better.
