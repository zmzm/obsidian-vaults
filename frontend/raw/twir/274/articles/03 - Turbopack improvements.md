---
type: twir-item
issue: 274
item: 3
item_type: item
date: 2026-03-25
source: https://nextjs.org/blog/next-16-2-turbopack
tags:
  - "Nextjs"
  - "TypeScript"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 3: Turbopack improvements

Source: [https://nextjs.org/blog/next-16-2-turbopack](https://nextjs.org/blog/next-16-2-turbopack)

Summary:
Turbopack, the default Next.js bundler, receives substantial updates in 16.2: server Fast Refresh is now much more efficient, WASM support in Web Workers is improved, and Subresource Integrity (SRI) is supported for enhanced security. Dynamic imports are now tree-shaken, and per-import loader configuration is possible via import attributes. Over 200 bug fixes and performance improvements have been made, and TypeScript configs for PostCSS are now supported.

Key takeaways:
- Server Fast Refresh is 67–100% faster, improving developer experience.
- SRI and better WASM support enhance security and compatibility.
- Dynamic imports are now tree-shaken for smaller bundles.
- Inline loader configuration and Lightning CSS options provide more flexibility.
- Over 200 fixes and improvements increase stability and performance.

Recommendation:
Read fully (read fully if you use Turbopack extensively or rely on advanced build customizations)

Why it matters:
read fully if you use Turbopack extensively or rely on advanced build customizations

Content:
---
title: "Turbopack: What's New in Next.js 16.2"
description: Turbopack in Next.js 16.2 brings faster builds, SRI support, postcss.config.ts, tree shaking of dynamic imports, Server Fast Refresh, inline loader configuration, and over 200 bug fixes.
url: "https://nextjs.org/blog/next-16-2-turbopack"
publishedAt: March 18th 2026
authors:
- Andrew Imm
- Tim Neutkens
---
Two releases after Turbopack became the default bundler for Next.js, we're focused on improving performance, fixing bugs, and increasing parity.
Here are some of the latest features shipping as part of [Next.js 16.2](/blog/next-16-2).
- [\*\*Server Fast Refresh\*\*](#server-fast-refresh): Fine-grained server-side hot reloading
- [\*\*Web Worker Origin\*\*](#web-worker-origin): Increasing support for WASM libraries in Workers
- [\*\*Subresource Integrity Support\*\*](#subresource-integrity-support): Subresource Integrity for JavaScript files
- [\*\*Tree Shaking of Dynamic Imports\*\*](#tree-shaking-of-dynamic-imports): Unused exports removed from dynamic `import()`
- [\*\*Inline Loader Configuration\*\*](#inline-loader-configuration): Per-import loader configuration via import attributes
- [\*\*Lightning CSS Configuration\*\*](#lightning-css-configuration): Experimental LightningCSS configuration options
- [\*\*Log Filtering\*\*](#log-filtering): Suppressing noisy logs and warnings with `ignoreIssue`
- [\*\*`postcss.config.ts` Support\*\*](#postcssconfigts-support): TypeScript PostCSS configuration
- [\*\*Performance Improvements and Bug Fixes\*\*](#performance-improvements-and-bug-fixes): Over 200 changes and bug fixes
Looking forward towards our next release, we'll be focused on speeding up compiler performance and reducing memory usage.
## Server Fast Refresh
We've reworked how server-side code is reloaded during development. The previous system cleared the `require.cache` for the changed module and all other modules in its import chain. This approach often reloaded more code than necessary, including unchanged `node\_modules`.
The new system brings the same Fast Refresh approach used in the browser to your server code. Turbopack's knowledge of the module graph means only the module that actually changed is reloaded, leaving the rest intact. This makes server-side hot reloading significantly more efficient.
In real-world Next.js applications, we've seen 67-100% faster application refresh and 400-900% faster compile time inside Next.js. These results scale from the smallest "hello world" starter project to large sites like `vercel.com`.

Server refresh time on a sample Next.js site

375% faster

Application (19ms → 9.7ms)

Today we're enabling this feature for all developers, by default. [Proxy](/docs/app/getting-started/proxy) and [Route Handlers](/docs/app/getting-started/route-handlers) will use the existing system today, but support for those is arriving in a future release. Share your feedback or any issues with this new feature on [GitHub](https://github.com/vercel/next.js/issues).
## Web Worker Origin
Previously, Web Workers were bootstrapped through a `blob://` URL. This streamlined loading the worker, but it set an empty `location.origin` value. Web Worker code that tried to use `importScripts()` or `fetch()` (usually in third-party libraries) would have been unable to resolve the request without changes.
With the updated Worker bootstrap code, the `origin` correctly points to your domain name, and relative fetches succeed. This should unblock anyone who had trouble running WASM code inside a Worker in previous versions.
## Subresource Integrity Support
Turbopack now supports [Subresource Integrity (SRI)](https://nextjs.org/docs/app/guides/content-security-policy#enabling-sri). SRI generates cryptographic hashes of your JavaScript files at build time, allowing browsers to verify that files haven't been modified.
Browsers provide a technology called Content Security Policy that allows sites to restrict the JavaScript that can run, eliminating entire classes of security issues. However, the typical `nonce`-based method for implementing this requires all pages to be dynamically rendered, impacting performance. Subresource Integrity is an alternative that computes a hash of each script ahead of time, and only allows the browser to execute scripts with approved hashes.
```js filename="next.config.js"
const nextConfig = {
experimental: {
sri: {
algorithm: 'sha256',
},
},
};
module.exports = nextConfig;
```
## Tree Shaking of Dynamic Imports
Turbopack now tree shakes destructured dynamic imports the same way it does static imports. Unused exports are removed from the bundle:
```ts
const { cat } = await import('./lib');
```
This is now equivalent to a static import for tree shaking purposes — any exports from `./lib` that aren't used will be tree-shaken.
## Inline Loader Configuration
Turbopack now supports per-import loader configuration via [import attributes](https://github.com/vercel/next.js/pull/89644). Instead of applying loaders globally through `turbopack.rules`, you can configure them on individual imports using the `with` clause:
```ts
import rawText from './data.txt' with {
turbopackLoader: 'raw-loader',
turbopackAs: '\*.js',
};
import value from './data.js' with {
turbopackLoader: 'string-replace-loader',
turbopackLoaderOptions: '{"search":"PLACEHOLDER","replace":"replaced value"}',
};
```
This is useful when only a specific import needs special treatment, avoiding side effects on other imports of the same file type. The available attributes are `turbopackLoader`, `turbopackLoaderOptions`, `turbopackAs`, and `turbopackModuleType`.
You should still prefer configuring your loaders in `next.config.ts` when possible, since code using inline loaders is less portable. This option is more useful for code generated from plugins or loaders.
## Lightning CSS Configuration
Lightning CSS is a fast, Rust-based CSS transformer used by Turbopack for CSS minification and prefixing. It also allows implementation of modern CSS features on older browsers, similar to what Babel or SWC do for JavaScript. Previously, the only way to toggle these settings was through a Browserslist configuration. Now with the experimental `lightningCssFeatures` option, you can force certain features to always or never transpile.
```ts
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
experimental: {
useLightningcss: true,
lightningCssFeatures: {
include: ['light-dark', 'oklab-colors'],
exclude: ['nesting'],
},
},
};
export default nextConfig;
```
## Log Filtering
Turbopack can now suppress noisy or expected warnings from streaming logs with the `turbopack.ignoreIssue` config option. This is useful for suppressing warnings from third-party code, generated files, or optional dependencies, as well as hiding expected errors from the Next.js error overlay.
You can match logs generated from specific code paths, as well as filter for specific title/description strings or patterns.
```ts
import type { NextConfig } from 'next';
const nextConfig: NextConfig = {
turbopack: {
ignoreIssue: [
{ path: '\*\*/vendor/\*\*' },
{ path: 'app/\*\*', title: 'Module not found' },
{ path: /generated\/.\*\.ts/, description: /expected error/i },
],
},
};
export default nextConfig;
```
## `postcss.config.ts` Support
Turbopack now supports `postcss.config.ts` in addition to the existing `.js` and `.cjs` variants.
## Performance Improvements and Bug Fixes
We've continued to invest in improving Turbopack internals. Over 200 changes and bug fixes have improved stability and compatibility across a wide range of projects. Optimizations in data encoding, internal representation formats, and hashing algorithms have improved memory usage and build time. We've made error logs clearer and expanded diagnostics to help you better understand compiler errors. We've also used your GitHub Issues as a guide for which features were missing since the 16.1 release.
## Feedback and Community
Share your feedback and help shape the future of Next.js:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
