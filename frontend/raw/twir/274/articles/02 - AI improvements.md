---
type: twir-item
issue: 274
item: 2
item_type: item
date: 2026-03-25
source: https://nextjs.org/blog/next-16-2-ai
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-03-25-TWIR-274|Index]]

# Item 2: AI improvements

Source: [https://nextjs.org/blog/next-16-2-ai](https://nextjs.org/blog/next-16-2-ai)

Summary:
Next.js 16.2 introduces features to make AI-assisted development more effective, including bundling version-matched documentation with projects, forwarding browser logs to the terminal, and providing a dev server lock file for better process management. The new `@vercel/next-browser` CLI allows AI agents (and humans) to inspect running Next.js apps, including React DevTools data, errors, and network activity, all from the terminal. These changes aim to streamline agent-driven workflows and debugging, especially in environments where browser access is limited.

Key takeaways:
- Projects now include `AGENTS.md` and bundled docs for AI agents, improving context and accuracy.
- Browser errors can be forwarded to the terminal, aiding headless debugging.
- Dev server lock file prevents duplicate processes and provides actionable errors for agents.
- Experimental CLI (`next-browser`) exposes React DevTools and app diagnostics to agents via shell commands.

Recommendation:
Summary sufficient (read the full post if you are building AI-powered tools or want to integrate with agent workflows)

Why it matters:
read the full post if you are building AI-powered tools or want to integrate with agent workflows

Content:
---
title: "Next.js 16.2: AI Improvements"
description: Next.js 16.2 ships AGENTS.md in create-next-app, browser log forwarding, dev server lock file with PID, and next-browser for AI agent debugging.
url: "https://nextjs.org/blog/next-16-2-ai"
publishedAt: March 18th 2026
authors:
- Jude Gao
- Tim Neutkens
---
Next.js 16.2 includes several improvements designed for AI-assisted development. These changes make it easier for agents to understand your project, debug issues from the terminal, and inspect running apps — all without requiring a browser.
- [\*\*Agent-ready `create-next-app`\*\*](#ai-ready-project-setup): Scaffold AI-ready projects out of the box
- [\*\*Browser Log Forwarding\*\*](#browser-log-forwarding): Forward browser errors to the terminal for agent-powered debugging
- [\*\*Dev Server Lock File\*\*](#dev-server-lock-file): Actionable error messages when a second dev server tries to start
- [\*\*Experimental Agent DevTools\*\*](#experimental-agent-devtools): Give AI agents terminal access to React DevTools and Next.js diagnostics
## Agent-ready `create-next-app`
`create-next-app` now includes an `AGENTS.md` file by default, giving AI coding agents access to version-matched Next.js documentation from the start of your project.
This builds on our [research into `AGENTS.md`](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals), which found that giving agents access to bundled documentation achieved a 100% pass rate on Next.js evals — outperforming skill-based approaches that maxed out at 79%. The key insight: always-available context works better than on-demand retrieval, because agents often fail to recognize when they should search for documentation.
> [!NOTE]
> The `AGENTS.md` file is a short directive that tells agents to read the docs bundled at `node\_modules/next/dist/docs/` before writing any code. The Next.js npm package now includes the full documentation as plain Markdown files, giving agents accurate version-matched references locally without fetching external data.
For existing projects, the setup depends on your Next.js version.
\*\*On 16.2 or later\*\*, the docs are already bundled in the `next` package. Add these two files to the root of your project:
```md filename="AGENTS.md"
# Next.js: ALWAYS read docs before coding
Before any Next.js work, find and read the relevant doc in `node\_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.
```
The comment markers delimit the Next.js-managed section. You can add your own project-specific instructions outside them — future updates will only replace content between the markers.
`CLAUDE.md` is the instruction file for [Claude Code](https://docs.anthropic.com/en/docs/claude-code). The `@` directive tells it to include `AGENTS.md` as additional context:
```md filename="CLAUDE.md"
@AGENTS.md
```
\*\*On earlier versions\*\*, use the codemod to generate these files automatically:
```bash filename="terminal"
npx @next/codemod@latest agents-md
```
For more details, see the [AI agents setup guide](/docs/app/guides/ai-agents#existing-projects).
## Browser Log Forwarding
Next.js now forwards browser errors to the terminal by default during development, so you can see client-side errors without switching to the browser console. This is especially helpful for AI agents that operate primarily through the terminal and can't access a browser console.
By default, only errors are forwarded to the terminal. You can control the level of forwarding with `logging.browserToTerminal` in your `next.config.ts`:
```ts filename="next.config.ts"
const nextConfig = {
logging: {
browserToTerminal: true,
// 'error' — errors only (default)
// 'warn' — warnings and errors
// true — all console output
// false — disabled
},
};
export default nextConfig;
```
## Dev Server Lock File
Next.js now writes the running dev server's PID, port, and URL into the `.next/dev/lock` file. When a second `next dev` process starts in the same project directory, Next.js reads the lock file and prints an actionable error:
```bash filename="terminal"
Error: Another next dev server is already running.
- Local: http://localhost:3000
- PID: 12345
- Dir: /path/to/project
- Log: .next/dev/logs/next-development.log
Run kill 12345 to stop it.
```
This is especially useful for AI coding agents, which frequently attempt to start `next dev` without knowing a server is already running. The structured error gives the agent the PID to kill the existing process or the URL to connect to it — no manual intervention required.
The lock file also prevents two `next build` processes from running simultaneously, which could otherwise corrupt build artifacts.
## Experimental Agent DevTools
The features above help agents understand your project and debug issues. [`@vercel/next-browser`](https://github.com/vercel-labs/next-browser) extends this by letting agents inspect a running Next.js application.
`next-browser` is an experimental CLI that exposes browser-level data — screenshots, network requests, console logs — along with framework-specific insights from React DevTools and the Next.js dev overlay, like component trees, props, hooks, [Partial Prerendering (PPR)](/docs/app/getting-started/cache-components) shells, and errors. All returned as structured text via shell commands.
An LLM can't read a DevTools panel, but it can run `next-browser tree`, parse the output, and decide what to inspect next. Each command is a one-shot request against a persistent browser session, so agents can query the app repeatedly without managing browser state. This turns the browser into something an agent can reason about, instead of a UI it can't access.
### What it can do today
The feature set is evolving quickly. As of this release, `next-browser` supports:
- \*\*Inspect React component trees\*\* — view props, hooks, state, and source-mapped file locations
- \*\*Analyze PPR shells\*\* — identify static vs dynamic regions and blocked [Suspense boundaries](/docs/app/glossary#suspense-boundary)
- \*\*Access errors and logs\*\* — retrieve build and runtime issues from the dev server
- \*\*Monitor network activity\*\* — track requests since navigation, including server actions
- \*\*Capture visuals\*\* — take screenshots or record loading filmstrips
### Getting started
Install it as a [skill](https://skills.sh) (a reusable capability for AI agents):
```bash filename="terminal"
npx skills add vercel-labs/next-browser
```
Then type `/next-browser` in Claude Code, Cursor, or any AI agent that supports skills. The CLI manages a Chromium instance with React DevTools pre-loaded — no browser configuration required.
### Example: Growing the static shell
With [Partial Prerendering (PPR)](/docs/app/getting-started/cache-components), Next.js can serve a [static shell](/docs/app/glossary#static-shell) instantly from the edge — the parts of your page that don't depend on per-request data — then stream in the rest. The more content that fits in the static shell, the faster users see a meaningful page.
In practice, a single per-request fetch can accidentally make an entire page dynamic. Consider a blog post with a visitor counter:
```tsx filename="app/blog/[slug]/page.tsx"
export async function generateStaticParams() {
const posts = await getAllPosts();
return posts.map((post) => ({ slug: post.slug }));
}
export default async function BlogPost({ params }) {
const post = await getPost(params.slug);
const views = await getVisitorCount(params.slug); // per-request
return (

# {post.title}

{views} views

{post.content}

);
}
```
Every slug is enumerated in `generateStaticParams`, so the post content could be prerendered at build time. But `getVisitorCount` runs on every request — and because it sits at the top level of the component, it makes the \_entire page\_ dynamic. As a result, the entire page waits behind a loading skeleton instead of streaming in progressively.
An agent can use `next-browser` to diagnose this. Locking PPR mode shows only the static shell — in this case, the `app/blog/[slug]/loading.tsx` skeleton, because nothing in the page made it into the shell:
```bash filename="terminal"
next-browser ppr lock # Enter PPR mode
next-browser goto /blog/hello # The entire page is a loading skeleton
```
The agent then runs `ppr unlock` to find out what went wrong:
```bash filename="terminal"
next-browser ppr unlock
```
```bash filename="terminal"
# PPR Shell Analysis
# 1 dynamic hole, 1 static
blocked by:
- getVisitorCount (server-fetch)
owner: BlogPost at app/blog/[slug]/page.tsx:5
next step: Push the fetch into a smaller Suspense leaf
```
The report tells the agent exactly what to do: `getVisitorCount` is the blocker, it lives in `BlogPost`, and the fix is to push it into its own [Suspense boundary](/docs/app/glossary#suspense-boundary). The agent wraps just the counter:
```tsx filename="app/blog/[slug]/page.tsx"
export default async function BlogPost({ params }) {
const post = await getPost(params.slug);
return (

# {post.title}

— views}>

{post.content}

);
}
```
Running `ppr lock` again confirms the shell grew — the post content now prerenders instantly. Only the visitor count shows a fallback:
`next-browser` is still evolving, but it points toward a future where agents can debug and optimize apps with the same visibility as a developer.
## Feedback and Community
Share your feedback and help shape the future of Next.js:
- [GitHub Discussions](https://github.com/vercel/next.js/discussions)
- [GitHub Issues](https://github.com/vercel/next.js/issues)
- [Discord Community](https://nextjs.org/discord)
