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
---

[[2026-02-25-TWIR-270|Index]]

# Item 3: Next.js - AI Agents Guide

Source: [https://nextjs.org/docs/app/guides/ai-agents](https://nextjs.org/docs/app/guides/ai-agents)

Summary:
Next.js now bundles version-matched documentation within the npm package, enabling AI coding agents to access up-to-date API references directly from the project. Projects can include an AGENTS.md file to instruct agents to use these docs, improving code generation accuracy. The guide explains setup for new and existing projects and details how agent files interact with various AI tools.

Key takeaways:
- Bundled docs ensure AI agents use accurate, version-specific Next.js documentation.
- AGENTS.md and CLAUDE.md files guide agents to these docs, reducing reliance on outdated training data.
- Setup is automatic for new projects; a codemod is available for older versions.
- Custom project instructions can be added outside the managed section of AGENTS.md.

Recommendation: Read fully (read fully if integrating AI agents into Next.js workflows)
