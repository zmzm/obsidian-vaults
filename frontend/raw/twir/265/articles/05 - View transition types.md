---
type: twir-item
issue: 265
item: 5
item_type: item
date: 2026-01-21
source: https://github.com/expo/skills
tags:
  - "Navigation"
status: auto
quality: keep
---

[[2026-01-21-TWIR-265|Index]]

# Item 5: View transition types

Source: [https://github.com/expo/skills](https://github.com/expo/skills)

Summary:
This MDN article explains how to use view transition types in web applications, enabling different animations for DOM updates based on transition context (e.g., forward, backward, or custom actions). The guide covers both SPA and MPA scenarios, showing how to specify transition types in JavaScript and apply targeted CSS animations using new pseudo-classes. Examples demonstrate practical usage for image galleries and story apps.

Key takeaways:
- View transition types allow fine-grained control over UI animations during navigation or content changes.
- Developers can specify transition types in JavaScript and target them in CSS with :active-view-transition-type().
- Supports both SPA and MPA architectures, improving UX consistency.
- Enables more expressive and context-aware UI transitions in React apps.

Recommendation:
Read fully (for those implementing custom transitions or advanced UI animations)

Why it matters:
for those implementing custom transitions or advanced UI animations

Content:
# expo/skills: A collection of AI agent skills for working with Expo projects and Expo Application Services · GitHub

Official AI agent skills from the Expo team for building, deploying, and debugging robust Expo apps.

We primarily use [Claude Code](https://claude.com/claude-code) at Expo, skills are fine-tuned for Opus models. But you can use these skills with any AI agent.

Add the marketplace:

```
/plugin marketplace add expo/skills
```

Install the plugin:

**Install from GitHub**

1. Open Cursor Settings (Cmd+Shift+J / Ctrl+Shift+J)
2. Navigate to `Rules & Command` → `Project Rules` → Add Rule → Remote Rule (GitHub)
3. Enter: `https://github.com/expo/skills.git`

**How it works:** Skills are automatically discovered and used by the agent based on context. When you ask questions about Expo development, the agent will automatically use the relevant skills (e.g., `building-ui`, `data-fetching`, `deployment`) based on the skill descriptions.

**Note:** Skills won't appear in the `/` slash command menu. The `/` menu in Cursor is for custom commands (stored in `.cursor/commands/`), not for skills. Skills work via auto-discovery - the agent uses them automatically when your questions match their descriptions.

**Verify installation:** After adding the Remote Rule, try asking the agent Expo-related questions like:

- "How do I build a UI with Expo Router?"
- "How do I make API calls in my Expo app?"
- "How do I deploy my Expo app to the App Store?"

If the skills are working, the agent will use the relevant skill content to answer your questions.

```
bunx skills add expo/skills
```

> This will extract the skills individually so you'll need to manually upgrade them.

MIT
