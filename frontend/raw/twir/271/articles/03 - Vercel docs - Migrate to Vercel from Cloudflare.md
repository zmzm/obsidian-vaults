---
type: twir-item
issue: 271
item: 3
item_type: item
date: 2026-03-04
source: https://vercel.com/kb/guide/migrate-to-vercel-from-cloudflare
tags:
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 3: Vercel docs - Migrate to Vercel from Cloudflare

Source: [https://vercel.com/kb/guide/migrate-to-vercel-from-cloudflare](https://vercel.com/kb/guide/migrate-to-vercel-from-cloudflare)

Summary:
This guide details the process of migrating applications from Cloudflare Pages or Workers to Vercel, covering project setup, domain migration, build configuration, environment variables, and feature mapping. It explains how Vercel’s platform auto-detects frameworks, manages CI/CD, and supports seamless DNS and environment variable migration. The documentation also covers how to map Cloudflare-specific features to Vercel equivalents and ensure a smooth transition with minimal downtime.

Key takeaways:
- Vercel provides automated framework detection and CI/CD, simplifying migration from Cloudflare.
- DNS and domain migration steps are outlined for zero-downtime transitions.
- Environment variables and secrets can be mapped and scoped per environment.

Recommendation:
Read fully (read fully only if planning a migration)

Why it matters:
read fully only if planning a migration

Content:
# Migrate to Vercel from Cloudflare

This guide will explain how to migrate your Cloudflare Pages or Workers application to Vercel.

We’ll cover everything from initial project setup to migrating compute, storage, and redirects. Vercel supports all core Cloudflare features, but instead, with a focus on open source and open standard technologies.

Vercel makes it easy to [import your existing code](https://vercel.com/docs/git#deploying-a-git-repository). In the Vercel dashboard, click “New Project” and select your Git provider (GitHub, GitLab, Bitbucket, etc.).

Choose your repository from the list. Vercel will auto-detect your framework and propose default settings (build command, output directory) based on that framework. You can adjust these settings if needed (for example, set a custom root directory or specific build command).

Once configured, click Deploy. Vercel will pull your code and perform the initial build and deployment automatically. When finished, you will have a live URL on Vercel.

Vercel’s platform recognizes a [wide range of frontend frameworks, backend frameworks, and static site generators](https://vercel.com/docs/frameworks). If your project is in Next.js, SvelteKit, Astro, Nitro, Express, etc., Vercel will apply the optimal build settings by default. This means you usually don’t need to manually specify build commands or output folders for popular frameworks.

For example, a Next.js app defaults to `npm run build` (which calls `next build`) and outputs to the `.next` directory automatically, while an Astro site might default to `astro build` with output to `dist`. You can override any of these in Project Settings or in a `vercel.json` config file if necessary.

After the project is linked, Vercel sets up [continuous deployment](https://vercel.com/docs/deployments). Every push to your Git repo’s main or production branch triggers a new production build, and pull request branches get deployed as Preview deployments.

This mirrors Cloudflare Pages’ Git integration (which also builds on git pushes), so you’ll have a familiar workflow on Vercel. The main difference is that Vercel provides extensive integration with frontend and full-stack frameworks (including functions and SSR if applicable), as well as the ability to create [fully custom environments](https://vercel.com/docs/deployments/environments#custom-environments).

1. Keep Cloudflare as your DNS provider
2. Add the domain to your Vercel project by visiting the domains tab in your team dashboard.
3. Once you have added the domain, go back to your domains dashboard and click on the domain to open the configuration page (If you have SSL certificates already configured for this domain on Vercel, you can skip steps 3-5).
4. Scroll to the bottom and click "Pre-generate SSL Certificates" (alternatively, you can use the CLI. Both methods are documented [here](https://vercel.com/docs/domains/pre-generating-ssl-certs#setting-your-dns-records-and-finalizing)).
5. Copy the TXT records into Cloudflare DNS for your domain and click "Verify" to issue an SSL certificate. Please note that the records may take time to propagate.
6. In your Cloudflare domain dashboard, delete the exist A record pointing to the worker and immediately add a new A record pointing to the IP address listed in your projects domain settings for apex domains. For subdomains, use the unique CNAME record listed in your projects domain settings (for example d1d4fc829fe7bc7c.vercel-dns-017.com). Ensure the proxy is disabled (gray-cloud the record) so traffic goes directly to Vercel.
7. The TTL is generally 5 minutes on Cloudflare domains, you can verify this in [Domain Digger](https://digger.tools/) by looking at the TTL for the TXT records on your domain. This means it will usually take about 5 minutes for changes to propagate.

Alternatively, you can change your domain's nameservers to Vercel's nameservers at your registrar. This moves DNS management entirely to Vercel. Any existing DNS records from Cloudflare will need to be recreated in Vercel.

After aliasing and updating DNS:

1. Remove the domain from your original project/Cloudflare setup
2. Configure any redirects (e.g., `apex` to `www`) as needed

DNS changes can take up to 48 hours to propagate globally. Vercel doesn't automatically add both apex and `www`, you need to add both if you want both.

Learn more about performing a [zero-downtime migration](https://vercel.com/docs/domains/working-with-domains/transfer-your-domain#configure-domain).

Migrating the build process from Cloudflare Pages to Vercel is usually straightforward and involves removing Cloudflare-specific settings for Vercel’s framework auto-detection:

- Build Command: In Cloudflare Pages, you specify a build command (e.g. `npm run build`) in the Pages UI or `wrangler.toml`. Identify the command you used. In Vercel, if your project is recognized (Next.js, Create React App, etc.), the build command is often inferred. Otherwise, you can [explicitly set the build command](https://vercel.com/docs/builds/configure-a-build#framework-settings) in Project Settings → Build & Development or in `vercel.json`.
- Output Directory: Cloudflare Pages also requires specifying the output folder (e.g. `build` or `dist`) where the static site is generated. On Vercel, the output directory is determined automatically for known frameworks, or you can configure it via `vercel.json` (`"outputDirectory": "build"` for example). Double-check that the directory Vercel expects matches what your build produces. If your build output is not in the default location, set the `outputDirectory` accordingly.
- Node.js or polyfills: If your site uses a specific Node.js version or requires polyfills, note that Vercel by default uses Node 24 for builds and Functions (as of [late 2025](https://vercel.com/changelog/node-js-24-lts-is-now-generally-available-for-builds-and-functions)). Cloudflare Pages builds run in an environment you configured (often latest Node LTS). You can specify an `"engines": { "node": "20.x" }` in your `package.json` or use Vercel’s config if you need a different Node version. Further, Workers run on a limited edge environment, which does not support all Node.js features. On Vercel, you can use the entire Node.js runtime.

After migrating, [trigger a deployment](https://vercel.com/docs/deployments#deployment-methods) on Vercel. Watch the build logs to ensure that your site is building successfully with the right command and output. Vercel’s logs will indicate which command was run.

Both Cloudflare Pages and Cloudflare Workers allow you to define environment variables/secrets (API keys, configuration values, etc.). When migrating:

- Gather existing variables: In the Cloudflare Pages dashboard, note all Environment Variables and any secret values you set (they may be encrypted/hidden in UI, so ensure you have the values stored securely). Cloudflare Workers secrets (set via `wrangler secret put`) also need to be collected. Common examples include API tokens, database URLs, or feature flags.
- Add them in Vercel: Go to your Vercel Project Settings → [Environment Variables](https://vercel.com/docs/environment-variables). For each variable, set the Name and Value. Vercel lets you scope vars to three environments: Development, Preview, and Production. This corresponds to local dev (`vercel dev` or your local builds), preview deployments (from git branches), and production deployments (main branch). You can mirror Cloudflare’s usage, for instance, Cloudflare has a concept of Production vs Preview variables. In Vercel, you can mark certain values to only apply in Production. Add your variables accordingly, marking secrets as sensitive (Vercel encrypts them at rest and conceals them in the dashboard by default).
- Usage in code: In Vercel Functions (Node.js runtime) or builds, environment variables are accessed via `process.env.YOUR_VAR` (just like in Node.js). If you have larger config needed at the edge, consider using Vercel Edge Config (a key-value store for edge reads) or storing data in an external service.
- Updating values: Any time you change an environment variable in Vercel, you’ll need to redeploy for it to take effect (changes aren’t retroactive to already-deployed instances). This is similar to Cloudflare Workers, where you’d redeploy the script if a bound variable changed. Vercel provides [CLI commands](https://vercel.com/docs/cli/env) (`vercel env pull`) to sync environment variables to a local `.env` file for development, if needed. When changing values in the Vercel dashboard, Vercel will prompt you to re-deploy.

If your Cloudflare Worker was reading secrets via `env.SECRET` (from the worker context), switch to reading `process.env.SECRET` in your Vercel Function code. The values you set in the dashboard will be provided at build and runtime.

Cloudflare Pages supports a `_redirects` file for defining URL redirects, and Cloudflare Workers can programmatically rewrite requests. On Vercel, you have a few ways to implement equivalent behavior:

Vercel’s [config file](https://vercel.com/docs/project-configuration#file-based-configuration) supports both [redirects](https://vercel.com/docs/redirects) and [rewrites](https://vercel.com/docs/rewrites) rules. For static sites or when not using a framework, this is the easiest approach. In your project root, create `vercel.json` and add rules under the `"redirects"` and `"rewrites"` keys. For example, a Cloudflare `_redirects` rule like:

can be expressed in `vercel.json` as:

```
"$schema": "https://openapi.vercel.sh/vercel.json",

{ "source": "/old-path", "destination": "/new-path", "permanent": true }
```

This uses `permanent: true` to indicate HTTP 301 status. You can similarly add multiple objects for each redirect. For rewrites (URL path proxying without changing the browser URL), use the `"rewrites"` array with `source` and `destination`. Vercel’s patterns support wildcards and regex just like Cloudflare’s dynamic `_redirects` syntax.

For instance, Cloudflare’s `_redirects` allows placeholders like `/*` – in Vercel you might use `:path*` in the source. e.g. a rule to rewrite `/docs/*` to `/api/docs/*` would be:

```
"$schema": "https://openapi.vercel.sh/vercel.json",

{ "source": "/docs/:path*", "destination": "/api/docs/:path*" }
```

If your project is using Next.js or similar frameworks, you can define `redirects()` and `rewrites()` functions in your config file. These functions return arrays of rules with the same fields (`source`, `destination`, etc.). For example:

```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {

{ source: '/old-path', destination: '/new-path', permanent: true }

{ source: '/docs/:slug*', destination: '/api/docs/:slug*' }

export default nextConfig
```

This achieves the same effect, and is convenient if you want all configuration in one place. Under the hood, Vercel will translate these to the appropriate routing rules for our CDN.

If you had Cloudflare Workers handling redirects (for example, responding with a 301 for certain paths), you can also [define redirects](https://vercel.com/docs/redirects) inside your Vercel Functions.

Make sure to remove or disable the `_redirects` file from your build output if you migrate rules to Vercel’s config, to avoid any confusion (Vercel does not automatically read a `_redirects` file like Cloudflare Pages would).

Cloudflare Pages allows defining response headers via a `_headers` file in the published directory (or via Cloudflare Workers altering responses). To implement custom HTTP headers (for security, caching, etc.) on Vercel:

Similar to redirects, you can define a `"headers"` array in `vercel.json` for static projects. Each entry can specify a `source` path pattern and a list of headers to add. For example, if your Cloudflare `_headers` file had:

you can translate this to `vercel.json` as:

```
"$schema": "https://openapi.vercel.sh/vercel.json",

"source": "/admin/:path*",

{ "key": "X-Frame-Options", "value": "DENY" },

{ "key": "Cache-Control", "value": "no-store" }
```

This will apply those headers to all routes under `/admin`. You can use wildcards or regex in `source` as needed (just like for redirects).

If using Next.js or similar frameworks, you have an `async headers()` function option. For instance:

```
import type { NextConfig } from 'next'

const nextConfig: NextConfig = {

{ key: "X-Frame-Options", value: "DENY" },

{ key: "Cache-Control", value: "no-store" }

export default nextConfig
```

This achieves the same result. Next.js will ensure those headers are sent for matching routes.

If you need to set headers conditionally (say based on cookies or user agent), you can do that with [Middleware](https://vercel.com/docs/routing-middleware) or [Functions](https://vercel.com/docs/functions) on Vercel. But for most static rules (security headers like CSP, CORS, etc.), the `vercel.json` or Next.js config approach is ideal. It’s similar to Cloudflare Pages’ `_headers`.

Cloudflare Workers run custom code using a minimal edge runtime (only option). Vercel provides [Functions](https://vercel.com/docs/functions), which can run full Node.js, Python, and other runtimes.

For example, you can define Functions [manually to create an API](https://vercel.com/guides/hosting-backend-apis), or have Functions created automatically as part of your framework build process (e.g. a server-rendered page in a framework like Next.js).

Suppose you have a Cloudflare Worker that responds to requests with a simple message:

```
async fetch(request, env) {

return new Response("Hello from Cloudflare!", { status: 200 });
```

On Vercel, you could create an equivalent Vercel Function without needing to use a framework. For example:

```
export function GET(request: Request) {

return new Response('Hello from Vercel!');
```

[Fluid compute](https://vercel.com/docs/functions/fluid-compute) on Vercel brings the benefits of a persistent server to Vercel Functions. In practical terms, Fluid allows a single function instance to handle multiple requests concurrently (whereas traditionally, one request per instance was the rule).

This means if you have many quick requests, Vercel can reuse the same warm function to serve them in parallel, reducing cold starts and cost. Cloudflare Workers have a similar concurrency profile, but at the expense of limiting the runtime environment and ecosystem compatibility.

Cloudflare Workers KV is a globally replicated key-value store (eventually consistent) often used for caching and configuration.

We recommend the following options on Vercel instead:

1. Redis: A fast key-value store with strong consistency and using a standard open protocol. You can purchase and use managed Redis through multiple providers on our [Marketplace](https://vercel.com/marketplace) with a few clicks. This will provision a Redis database and automatically inject the connection URL and credentials into your project’s environment variables.
2. Edge Config: Vercel also offers an eventually consistent [config store](https://vercel.com/docs/edge-config). The vast majority of your reads will complete within 15ms at P99, or as low as microseconds in some scenarios.

Cloudflare KV operations in a Worker look like:

```
await env.MY_KV_NAMESPACE.put('key1', 'value1');

let val = await env.MY_KV_NAMESPACE.get('key1');
```

On Vercel, using Redis (for example Upstash’s Redis client):

```
import { Redis } from '@upstash/redis';

const redis = Redis.fromEnv();

await redis.set('key1', 'value1');

let val = await redis.get('key1');
```

You can use any Redis client (`ioredis`, `node-redis`) since you’re using a full Node.js runtime.

If you have existing data in Cloudflare KV that you need to migrate, you’ll have to export it via Cloudflare’s API (or a script iterating over keys) and then import to Redis. Cloudflare KV doesn’t have a direct export tool, but you can list keys (with a prefix) and fetch values, then write them to the new store. [Upstash Redis](https://vercel.com/marketplace/upstash) supports batch writes which can speed up importing large sets.

Cloudflare R2 is an S3-compatible object storage service often used to store images, videos, or large static files. Vercel Blob is an object storage solution that serves a similar purpose, letting you store and serve blobs (files) easily, integrated with your deployments.

```
import { put } from '@vercel/blob';

const blob = await put('avatar.jpg', imageFile, {
```

Learn more about getting started with [Vercel Blob](https://vercel.com/docs/vercel-blob).

Cloudflare Durable Objects provide a unique way to maintain stateful, singleton instances on the edge. You can achieve similar (but not exact) capabilities using a combination of Vercel Functions and external state (like Redis), leveraging open-source utilities like [resumable streams](https://github.com/vercel/resumable-stream). This avoids being tied to a proprietary runtime for state.

`resumable-stream` was designed to help with server-sent events (SSE) or any streaming over HTTP where you want clients to be able to disconnect and reconnect without losing their place in the stream. It effectively gives you a way to have stateful streams and multi-client coordination, similar to what one might build with Durable Objects.

If your Durable Object was used for something like a globally consistent counter or lock, you can achieve that with an atomic Redis operation (e.g., `INCR` for a counter, which is atomic, or a Redis `SETNX` for a lock). If it was used for storing JSON data or a small dataset per object, you could use Redis hashes or a SQL database row.

The approach above uses a library (`resumable-stream`) that is open source (MIT license) and a database (Redis) that is open standard and widely supported. You are not confined to Vercel’s platform. You could take this same approach to any Node.js hosting provider. Vercel is simply providing the hosting for your functions and making it easy to plug in Redis (via their marketplace integration or your own setup).

Cloudflare Workers are often used as edge middleware. For example, rewriting URLs, checking cookies before serving a page, or injecting headers. If you were using Cloudflare Pages Functions or a Worker on a route to act as middleware, you can use Next.js Proxy (if your project is Next.js) or Vercel Routing Middleware for any other framework (or without).

Middleware is a special file that runs before every request is processed by your application. You create a file `proxy.ts` (or `.js`) at the root of your project. This file can inspect the incoming request and modify the response or redirect as needed.

Learn more about [Middleware](https://vercel.com/docs/edge-middleware/quickstart).

This is a non-exhaustive mapping on Cloudflare features and products to Vercel:

By completing the steps above, you should have your custom domains serving from Vercel, your redirects, headers, and environment configured, and your Cloudflare Workers logic running as Vercel Functions or Routing Middleware.

Test your application thoroughly after migration. Ensure that all endpoints, pages, and more work as expected on Vercel. In most cases, you’ll find improved development velocity and comparable (or better) performance. Reach out in our [community](https://community.vercel.com/) if you have any questions.
