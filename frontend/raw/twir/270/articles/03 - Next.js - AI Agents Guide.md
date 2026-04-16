---
type: twir-item
issue: 270
item: 3
item_type: item
date: 2026-02-25
source: https://nextjs.org/docs/app/guides/ai-agents
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-02-25-TWIR-270|Index]]

# Item 3: Next.js - AI Agents Guide

Source: [https://nextjs.org/docs/app/guides/ai-agents](https://nextjs.org/docs/app/guides/ai-agents)

Summary:
Next.js now bundles version-matched documentation within the npm package, enabling AI coding agents to access up-to-date docs directly from the project’s node_modules. The new AGENTS.md file instructs agents to consult these docs before generating code, improving accuracy and reducing reliance on outdated training data. The setup is automatic for new projects and easily retrofitted to existing ones.

Key takeaways:
- Bundled documentation ensures AI agents use accurate, version-matched Next.js APIs and guides.
- AGENTS.md serves as a standard entry point for agents, redirecting them from stale training data.
- Automatic setup via create-next-app; codemod available for older projects.
- Supports major AI coding agents (Claude, Copilot, Cursor, etc.) out of the box.

Recommendation:
Summary sufficient

Content:
---
title: How to set up your Next.js project for AI coding agents
description: Learn how to configure your Next.js project so AI coding agents use up-to-date documentation instead of outdated training data.
url: "https://nextjs.org/docs/app/guides/ai-agents"
version: 16.2.4
lastUpdated: 2026-04-15
prerequisites:
- "Guides: /docs/app/guides"
related:
- app/guides/mcp
---
Next.js ships version-matched documentation inside the `next` package, allowing AI coding agents to reference accurate, up-to-date APIs and patterns. An `AGENTS.md` file at the root of your project directs agents to these bundled docs instead of their training data.
## How it works
When you install `next`, the Next.js documentation is bundled at `node\_modules/next/dist/docs/`. The bundled docs mirror the structure of the [Next.js documentation site](https://nextjs.org/docs):
```txt
node\_modules/next/dist/docs/
├── 01-app/
│ ├── 01-getting-started/
│ ├── 02-guides/
│ └── 03-api-reference/
├── 02-pages/
├── 03-architecture/
└── index.mdx
```
This means agents always have access to docs that match your installed version — no network request or external lookup required.
The `AGENTS.md` file at the root of your project tells agents to read these bundled docs before writing any code. Most AI coding agents — including Claude Code, Cursor, GitHub Copilot, and others — automatically read `AGENTS.md` when they start a session.
## Getting started
### New projects
[`create-next-app`](/docs/app/api-reference/cli/create-next-app) generates `AGENTS.md` and `CLAUDE.md` automatically. No additional setup is needed:
```bash package="pnpm"
pnpm create next-app@canary
```
```bash package="npm"
npx create-next-app@canary
```
```bash package="yarn"
yarn create next-app@canary
```
```bash package="bun"
bun create next-app@canary
```
If you don't want the agent files, pass `--no-agents-md`:
```bash
npx create-next-app@canary --no-agents-md
```
### Existing projects
Ensure you are on Next.js `v16.2.0-canary.37` or later, then add the following files to the root of your project.
`AGENTS.md` contains the instructions that agents will read:
```md filename="AGENTS.md"
# Next.js: ALWAYS read docs before coding
Before any Next.js work, find and read the relevant doc in `node\_modules/next/dist/docs/`. Your training data is outdated — the docs are the source of truth.
```
`CLAUDE.md` uses the `@` import syntax to include `AGENTS.md`, so [Claude Code](https://docs.anthropic.com/en/docs/claude-code) users get the same instructions without duplicating content:
```md filename="CLAUDE.md"
@AGENTS.md
```
For earlier versions
On version 16.1 and earlier, use the codemod to generate these files automatically:
```bash
npx @next/codemod@latest agents-md
```
The codemod outputs the bundled docs to `.next-docs/` in the project root instead of `node\_modules/next/dist/docs/`, and the generated agent files will point to that directory.
## Understanding AGENTS.md
The default `AGENTS.md` contains a single, focused instruction: \*\*read the bundled docs before writing code\*\*. This is intentionally minimal — the goal is to redirect agents from stale training data to the accurate, version-matched documentation in `node\_modules/next/dist/docs/`.
The `` and `` comment markers delimit the Next.js-managed section. You can add your own project-specific instructions outside these markers without worrying about them being overwritten by future updates.
The bundled docs include guides, API references, and file conventions for the App Router and Pages Router. When an agent encounters a task involving routing, data fetching, or any other Next.js feature, it can look up the correct API in the bundled docs rather than relying on potentially outdated training data.
> \*\*Good to know:\*\* To see how bundled docs and `AGENTS.md` improve agent performance on real-world Next.js tasks, visit the [benchmark results](https://nextjs.org/evals).
## Next Steps- [Next.js MCP Server](/docs/app/guides/mcp)
- Learn how to use Next.js MCP support to allow coding agents access to your application state
---
For a semantic overview of all documentation, see [/docs/sitemap.md](/docs/sitemap.md)
For an index of all available documentation, see [/docs/llms.txt](/docs/llms.txt)
