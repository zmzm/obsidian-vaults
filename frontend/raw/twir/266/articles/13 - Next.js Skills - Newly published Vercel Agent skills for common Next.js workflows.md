---
type: twir-item
issue: 266
item: 13
item_type: item
date: 2026-01-28
source: https://github.com/vercel-labs/next-skills
tags:
  - "Skills"
  - "Nextjs"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 13: Next.js Skills - Newly published Vercel Agent skills for common Next.js workflows

Source: [https://github.com/vercel-labs/next-skills](https://github.com/vercel-labs/next-skills)

Summary:
Vercel has published a set of Agent Skills for automating and guiding common Next.js workflows, including best practices, upgrades, cache components, and more. Skills are modular, follow the Agent Skills open standard, and can be invoked via CLI or slash commands. The skills cover both essential and advanced Next.js topics, and are designed for integration with AI agents and developer tools.

Key takeaways:
- Skills automate Next.js best practices, upgrades, cache management, and debugging.
- Modular structure allows targeted installation and usage.
- Integrates with AI agents for workflow automation and guidance.
- Related skills exist for React patterns and other frameworks.

Recommendation:
Read fully (read fully if interested in AI-assisted Next.js workflows or agent-based automation)

Why it matters:
read fully if interested in AI-assisted Next.js workflows or agent-based automation

Content:
# GitHub - vercel-labs/next-skills · GitHub

Agent skills for common Next.js workflows.

Start here. These background skills are auto-applied to prevent common mistakes.

Core Next.js knowledge:

- [File Conventions](/vercel-labs/next-skills/blob/main/skills/next-best-practices/file-conventions.md) - Project structure and special files
- [RSC Boundaries](/vercel-labs/next-skills/blob/main/skills/next-best-practices/rsc-boundaries.md) - Server/Client Component rules
- [Data Patterns](/vercel-labs/next-skills/blob/main/skills/next-best-practices/data-patterns.md) - Fetching and mutation strategies
- [Async Patterns](/vercel-labs/next-skills/blob/main/skills/next-best-practices/async-patterns.md) - Next.js 15+ async APIs
- [Directives](/vercel-labs/next-skills/blob/main/skills/next-best-practices/directives.md) - `'use client'`, `'use server'`, `'use cache'`
- [Functions](/vercel-labs/next-skills/blob/main/skills/next-best-practices/functions.md) - Navigation hooks, server functions, generate functions
- [Runtime Selection](/vercel-labs/next-skills/blob/main/skills/next-best-practices/runtime-selection.md) - Node.js vs Edge runtime
- [Error Handling](/vercel-labs/next-skills/blob/main/skills/next-best-practices/error-handling.md) - Error boundaries and redirects
- [Route Handlers](/vercel-labs/next-skills/blob/main/skills/next-best-practices/route-handlers.md) - API routes with `route.ts`
- [Metadata](/vercel-labs/next-skills/blob/main/skills/next-best-practices/metadata.md) - SEO, OG images, sitemaps
- [Image](/vercel-labs/next-skills/blob/main/skills/next-best-practices/image.md) - `next/image` optimization
- [Font](/vercel-labs/next-skills/blob/main/skills/next-best-practices/font.md) - `next/font` optimization
- [Bundling](/vercel-labs/next-skills/blob/main/skills/next-best-practices/bundling.md) - Package compatibility, CSS imports, polyfills
- [Scripts](/vercel-labs/next-skills/blob/main/skills/next-best-practices/scripts.md) - Third-party scripts, Google Analytics
- [Hydration Errors](/vercel-labs/next-skills/blob/main/skills/next-best-practices/hydration-error.md) - Debugging mismatches
- [Suspense Boundaries](/vercel-labs/next-skills/blob/main/skills/next-best-practices/suspense-boundaries.md) - CSR bailout, Cache Components requirements
- [Parallel Routes](/vercel-labs/next-skills/blob/main/skills/next-best-practices/parallel-routes.md) - Modal patterns with intercepting routes
- [Self-Hosting](/vercel-labs/next-skills/blob/main/skills/next-best-practices/self-hosting.md) - Docker, standalone output, ISR
- [Debug Tricks](/vercel-labs/next-skills/blob/main/skills/next-best-practices/debug-tricks.md) - MCP endpoint, rebuild specific routes

```
# Install essentials (recommended)
npx skills add vercel-labs/next-skills --skill next-best-practices

# Or install everything
npx skills add vercel-labs/next-skills
```

Optional skills for specific needs. Invoke via slash commands.

Upgrading between Next.js versions with official migration guides.

```
npx skills add vercel-labs/next-skills --skill next-upgrade
```

Next.js 16 Cache Components and PPR. Covers `cacheComponents: true`, `'use cache'` directive, cache profiles, `cacheLife()`, `cacheTag()`, and `updateTag()`.

```
npx skills add vercel-labs/next-skills --skill next-cache-components
```

**Background skills** (`next-best-practices`) are automatically applied when relevant.

**Slash commands** for advanced skills:

```
/next-upgrade
/next-cache-components
```

For React-specific patterns (hooks, state management, component composition):

```
npx skills add vercel-labs/agent-skills --skill react-best-practices
```

Each skill follows the [Agent Skills open standard](https://github.com/anthropics/skills):

1. Create a directory under `skills/` with the skill name (prefix with `next-`)
2. Add a `SKILL.md` file with YAML frontmatter:

   ```
   ---
   name: next-skill-name
   description: Brief description
   user-invocable: false  # for background skills
   ---
   ```
3. For complex skills, add additional `.md` files and reference them from `SKILL.md`
