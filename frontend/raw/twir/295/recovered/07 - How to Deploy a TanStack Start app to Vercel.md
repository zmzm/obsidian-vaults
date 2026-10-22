---
type: "twir-recovery"
issue: 295
item: 7
source: "https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel"
final_url: "https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel"
retrieved: "2026-10-22T11:30:09+00:00"
original_note: "frontend/raw/twir/295/articles/07 - How to Deploy a TanStack Start app to Vercel.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/07 - How to Deploy a TanStack Start app to Vercel|How to Deploy a TanStack Start app to Vercel]]

---
title: How to Deploy a TanStack Start app to Vercel
description: Deploy a TanStack Start app to Vercel with the Nitro Vite plugin. Covers Git and CLI deployment, Fluid compute defaults, and framework detection fixes.
url: "https://vercel.com/kb/guide/deploy-a-tanstack-start-app-to-vercel"
published: 2026-09-01
last\_updated: 2026-10-14
authors: Ben Sabic
related\_resources:
- title: "Build a Jev agent with TanStack Start and TanStack AI"
url: "https://vercel.com/i/using-jev-in-tanstack-start-with-tanstack-ai"
description: "Use Jev in TanStack Start through TanStack AI's Vercel Gateway adapter. Build a typed decision endpoint and compare the AI SDK integration."
install\_vercel\_plugin: npx plugins add vercel/vercel-plugin
---
\*\*Try Jev on Vercel AI Gateway\*\*
Give your application a faster way to decide what should happen next. Use Jev to route requests, flag content, and score priorities.
[Get started](https://vercel.com/kb/jev-from-typesafe-ai)
[TanStack Start](https://vercel.com/docs/frameworks/full-stack/tanstack-start) is a full-stack framework powered by TanStack Router for React and Solid, with support for full-document SSR, streaming, server functions, and bundling. It runs on Vercel when paired with Nitro, the server toolkit that builds your app for the Vercel runtime.
Vercel detects TanStack Start and Nitro automatically, so once the Nitro plugin is in place, you can deploy from Git or the [Vercel CLI](https://vercel.com/docs/cli) without extra build configuration.
In the steps below, you'll install the Nitro plugin, register it in your Vite config, deploy your app, and verify the live deployment. You'll also learn how Vercel runs your server functions on [Fluid compute](https://vercel.com/fluid) by default, and how to fix detection issues when Vercel doesn't apply the TanStack Start preset, such as in a monorepo.
## Prerequisites
Before you begin, make sure you have:
- A [Vercel account](https://vercel.com/signup) and Vercel CLI installed (`npm install -g vercel`)
- Node.js 24+ and a package manager (e.g., npm)
- An existing TanStack Start project, or a new one created from the [template](https://vercel.com/templates/other/tanstack-start-on-vercel)
- A Git repository on GitHub, GitLab, or Bitbucket
## How it works
TanStack Start apps are built on Vercel with Nitro. The [Nitro Vite](https://vercel.com/kb/guide/nitro-vite-plugin) plugin compiles your server code into output that Vercel deploys as [Vercel Functions](https://vercel.com/docs/functions). By default, Vercel runs these functions on Fluid compute, so your app scales with traffic, and you pay only for what you use, not for idle function time.
Because Vercel ships zero-configuration detection for both TanStack Start and Nitro, you don't need to set a build command or output directory. Vercel reads your project, identifies the framework, and applies the correct settings.
## Steps
### 1\. Add the Nitro plugin to your project
If you created your project from the Vercel template, Nitro is already configured, so you can skip to [step two](#2.-register-nitro-in-your-vite-config). For an existing project, install `nitro` from the root directory using your preferred package manager:
\*\*pnpm\*\*
```bash
pnpm i nitro
```
\*\*npm\*\*
```bash
npm i nitro
```
\*\*yarn\*\*
```bash
yarn add nitro
```
\*\*bun\*\*
```bash
bun add nitro
```
### 2\. Register Nitro in your Vite config
Add the `nitro` plugin to the `plugins` array in your `vite.config.ts` file. Place it alongside the TanStack Start and React plugins:
```typescript
import { tanstackStart } from '@tanstack/react-start/plugin/vite';
import { defineConfig } from 'vite';
import viteReact from '@vitejs/plugin-react';
import { nitro } from 'nitro/vite';
export default defineConfig({
plugins: [tanstackStart(), nitro(), viteReact()],
});
```
For a Solid project, swap the React plugins for their Solid equivalents and keep the `nitro()` plugin in place.
### 3\. Set environment variables
If your TanStack Start app uses private API keys or other secrets, save them to Vercel before deploying. Open your project's [Environment Variables settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fenvironment-variables), add each key-value pair, and select the applicable environments (Production, Preview, and Development). You can also add variables from the terminal with the Vercel CLI:
```bash
vercel env add MY\_KEY
```
The CLI prompts you for the value and the environments to apply it to. To scope a variable to one environment, pass it directly:
```javascript
vercel env add MY\_KEY production
```
The `VITE\_` prefix determines where a variable is available:
- Variables prefixed with `VITE\_` are bundled into your client-side code and readable in the browser through `import.meta.env`. Use this only for values that are safe to make public (e.g., publishable API keys).
- Variables without the prefix never reach the client bundle. They stay available to server-side code, such as [server functions](https://tanstack.com/start/v0/docs/framework/react/guide/server-functions) and loaders, through `process.env`. Keep secrets like database credentials and private API keys unprefixed.
> \*\*Warning:\*\*
>
> Never store a secret in a `VITE\_` variable. Anything with that prefix ships to the browser and can be read by anyone who visits your site.
To run your app locally with the same values, pull them into a `.env` file:
```bash
vercel env pull
```
You can't read [secret environment variables](https://vercel.com/docs/environment-variables/sensitive-environment-variables) (e.g., API keys) after creating them, so they won't appear in your `.env` file. Instead, create a separate, non-sensitive variable in the Development environment with a development credential.
After you change a variable in Vercel, redeploy for the change to take effect. Existing deployments keep the values they were built with.
### 4\. Deploy your app
When deploying your TanStack Start project to Vercel, you have two options.
\*\*Deploy from Git:\*\*
1. Commit and push your project to a Git repository.
2. Go to the [new project page](https://vercel.com/new) and import the repository.
3. Vercel detects TanStack Start and fills in the build settings for you. Confirm the framework preset reads \*\*TanStack Start\*\*, then select \*\*Deploy\*\*.
Each push to your main branch triggers a new deployment from now on.
\*\*Deploy with the Vercel CLI:\*\*
```bash
vercel
```
The CLI guides you through linking the project to Vercel, then builds and deploys it to your [preview environment](https://vercel.com/docs/deployments/environments#preview-environment-pre-production). That same deployment can be promoted to production with `vercel promote `, or you can trigger a new one with `vercel --prod`.
### 5\. Verify your deployment
After the build finishes, Vercel returns a deployment URL. Open it and verify that:
- The page renders with server-side content
- Navigating between routes works without errors
- Any server functions return the expected responses
If the home page loads but routes return 404 errors, confirm that `nitro()` is present in your Vite config and redeploy. Routing failures on Vercel usually stem from a missing or misplaced Nitro plugin. You can also check your [deployment logs](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fdeployments) for more information, including any errors.
## Troubleshooting
### Framework preset not detected
In a monorepo, or in a project that previously used a different framework, Vercel may not automatically detect TanStack Start.
\*\*You have three ways to set the framework preset:\*\*
- In the dashboard\*\*,\*\* under the project's [framework settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment%23framework-settings).
- In `vercel.json`:
```json
{
"framework": "tanstack-start"
}
```
- With the Vercel CLI:
```bash
vercel project update  --framework tanstack-start
```
### Build succeeds, but the deployment returns errors
Confirm your local build runs cleanly before deploying:
```bash
npm run build
```
Failing local builds indicate a potential issue with the project. Resolve the local error first, then redeploy. If the build passes locally but fails on Vercel, verify that your Node.js version in [project settings](https://vercel.com/d?to=%2F%5Bteam%5D%2F%5Bproject%5D%2Fsettings%2Fbuild-and-deployment%23node.js-version) matches the version you use locally.
## Further building
Use `vercelGatewayDecider` from [TanStack AI’s Vercel AI Gateway adapter](https://vercel.com/docs/ai-gateway/ecosystem/framework-integrations/tanstack-ai) with [Jev](https://vercel.com/i/what-is-jev) in [Moderate product reviews with Jev, TanStack AI, and AI Gateway](https://vercel.com/kb/guide/moderate-product-reviews-jev-tanstack-ai) to get typed choices, scores, and boolean probabilities instead of generated text.
## Related resources
- Read the full [TanStack Start on Vercel documentation](https://vercel.com/docs/frameworks/full-stack/tanstack-start)
- Learn how [Vercel Functions](https://vercel.com/docs/functions) run your server code
- Understand pricing and scaling with [Fluid compute](https://vercel.com/docs/fluid-compute)
- Explore the [TanStack Start docs](https://tanstack.com/start/latest/docs/framework/react/overview)
- Configure Vercel-specific features through the [Nitro Vercel provider docs](https://v3.nitro.build/deploy/providers/vercel)
- Learn about [TanStack Intent](https://vercel.com/kb/guide/using-tanstack-intent-to-ship-and-consume-agent-skills) and [TanStack Hotkeys](https://vercel.com/kb/guide/adding-keyboard-shortcuts-to-react-apps-with-tanstack-hotkeys)
- Build a [Jev agent with TanStack Start and TanStack AI](https://vercel.com/i/using-jev-in-tanstack-start-with-tanstack-ai)
## FAQ
### Does Vercel support TanStack Start out of the box?
Yes. Vercel ships zero-configuration detection for both TanStack Start and Nitro, so it identifies the framework and fills in the build command and output directory without manual setup. Once the Nitro plugin is in your Vite config, you can deploy straight from Git or the CLI.
### Do I get preview deployments for TanStack Start on Vercel?
Yes. When you connect a Git repository, every push to a branch creates a preview deployment with its own URL, and pushes to your main branch go to production. From the CLI, running `vercel` builds a preview you can promote with `vercel promote`, or you can deploy straight to production with `vercel --prod`.
### What does it cost to run the app on Vercel?
TanStack Start apps use Fluid compute with Active CPU pricing. This means you are billed only for the CPU time your functions actively use, not for time spent waiting on database queries or sitting idle between requests. You can start for free on the Hobby plan, designed for personal projects. For commercial use and team collaboration, Pro and Enterprise plans are available.
### Is TanStack Start fast on Vercel?
Yes. Vercel serves your static assets from its CDN and runs your server functions on Fluid compute, which reuses warm instances to reduce cold starts, keeping requests fast under load. TanStack Start also supports streaming server-side rendering, so the browser can begin showing the page before all server data has loaded, shortening the time users wait to see content.
### How does a TanStack Start app scale on Vercel?
Vercel runs your server functions on Fluid compute by default, which scales them up and down with traffic. There are no servers to provision or manage, so the same app handles a quiet day and a sudden spike without any changes on your end. You pay only for what you use, not for idle function time.
## Related Resources
- [Build a Jev agent with TanStack Start and TanStack AI](https://vercel.com/i/using-jev-in-tanstack-start-with-tanstack-ai): Use Jev in TanStack Start through TanStack AI's Vercel Gateway adapter. Build a typed decision endpoint and compare the AI SDK integration.
## More Nitro guides
- [What is the Nitro Vite plugin?](/kb/guide/nitro-vite-plugin): The Nitro Vite plugin (nitro/vite) adds SSR, API routes, and deploy-anywhere server builds to any Vite app. Learn what it does and how it runs on Vercel.
- [How to ship a Nitro app on Vercel](/kb/guide/ship-a-nitro-app-on-vercel): Deploy a Nitro app to Vercel with zero configuration. Learn how to ship from a template, the Vercel CLI, or Git, and configure ISR, cron jobs, Vercel Queues, per-route function settings, and Observability.
- [How to build an MCP server with Nuxt](/kb/guide/how-to-build-an-mcp-server-with-nuxt): Add an MCP server to your Nuxt app with the Nuxt MCP Toolkit. Create tools, resources, and prompt templates that AI assistants like Cursor and VS Code can connect to.
