---
type: twir-item
issue: 266
item: 15
item_type: item
date: 2026-01-28
source: https://github.com/resend/react-email/tree/canary/skills/react-email
tags:
  - "Skills"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 15: React Email Agent Skills

Source: [https://github.com/resend/react-email/tree/canary/skills/react-email](https://github.com/resend/react-email/tree/canary/skills/react-email)

Summary:
React Email has published an Agent Skill for building HTML emails with React components, supporting visual editing, sending, i18n, and best practices. The skill is structured for efficient context usage, with a main SKILL.md and topic-specific references, following the Agent Skills specification for AI agents.

Key takeaways:
- Provides structured, progressive documentation for React Email development.
- Supports visual editing, internationalization, and sending via Resend.
- Designed for AI agents to load only relevant context for each task.
- Follows Agent Skills open standard for modularity and efficiency.

Recommendation:
Read fully (read fully if using React Email or building AI agent integrations)

Why it matters:
read fully if using React Email or building AI agent integrations

Content:
# react-email/skills/react-email at canary · resend/react-email · GitHub

This directory contains an Agent Skill for building HTML emails with React Email components.

```
skills/
└── react-email/
    ├── SKILL.md              # Main skill instructions
    └── references/
        ├── COMPONENTS.md     # Complete component reference
        ├── EDITOR.md         # Visual email editor reference
        ├── I18N.md           # Internationalization guide
        ├── PATTERNS.md       # Common email patterns and examples
        ├── SENDING.md        # Email sending guide
        └── STYLING.md        # Styling and CSS reference
```

Agent Skills are a standardized format for giving AI agents specialized knowledge and workflows. This skill teaches agents how to:

- Build HTML email templates using React Email components
- Add a visual drag-and-drop email editor to a React application (using `@react-email/editor`)
- Send emails through Resend and other providers
- Implement internationalization for multi-language support
- Follow email development best practices

AI agents can load this skill to gain expertise in React Email development. The skill follows the [Agent Skills specification](https://agentskills.io) with:

- **SKILL.md**: Core instructions loaded when the skill is activated (< 350 lines)
- **references/**: Detailed documentation loaded on-demand for specific topics

The skill is structured for efficient context usage:

1. **Metadata** (~100 tokens): Name and description in frontmatter
2. **Core Instructions** (~3K tokens): Main SKILL.md content
3. **Detailed References** (as needed): Component docs, i18n guides, patterns

Agents load only what they need for each task.
