---
type: twir-item
issue: 267
item: 10
item_type: item
date: 2026-02-04
source: https://github.com/remix-run/agent-skills
tags:
  - "Skills"
status: auto
quality: keep
---

[[2026-02-04-TWIR-267|Index]]

# Item 10: React Router Agent Skills

Source: [https://github.com/remix-run/agent-skills](https://github.com/remix-run/agent-skills)

Summary:
The React Router team introduces "Agent Skills," a set of structured documentation modules designed to teach AI coding agents how to use React Router correctly in different modes (framework, data, declarative). Each skill provides up-to-date usage patterns, references, and code examples, ensuring agents generate accurate code regardless of their training data's currency.

Key takeaways:
- Agent Skills provide machine-readable, current best practices for React Router usage in various modes.
- Skills can be installed into projects for AI agents to reference during code generation or review.
- Each skill includes quick patterns, reference tables, and deep documentation for specific topics.
- This approach aims to improve AI-generated code quality and developer trust in agent-assisted workflows.

Recommendation:
Summary sufficient

Content:
# remix-run/agent-skills: Agent Skills for working with React Router · GitHub

[Agent Skills](https://agentskills.io) for building web applications.

These skills teach AI coding agents how to use frameworks and libraries correctly. Instead of relying on potentially outdated training data, agents can reference these skills for accurate, up-to-date patterns.

```
npx skills add remix-run/agent-skills
```

This installs the skills into your project so your AI agent can reference them.

Full-stack React apps using [React Router's](https://reactrouter.com) framework mode. Covers routing, loaders, actions, forms, sessions, middleware, error handling, and rendering strategies.

```
npx skills add remix-run/agent-skills --skill react-router-framework-mode
```

React apps using React Router's data mode with `createBrowserRouter` and `RouterProvider`. Covers route objects, loaders, actions, forms, pending UI, and optimistic updates without the Vite plugin.

```
npx skills add remix-run/agent-skills --skill react-router-data-mode
```

React apps using React Router's declarative mode with `BrowserRouter`. Covers JSX-based routing, navigation with Link/NavLink, and reading URL params without data loading features.

```
npx skills add remix-run/agent-skills --skill react-router-declarative-mode
```

Each skill contains:

- **`SKILL.md`** - Main entry point with quick patterns and a reference table
- **`references/`** - Detailed documentation for specific topics

When your AI agent encounters a relevant task, it loads the skill and references to generate accurate code using current APIs and best practices.

MIT
