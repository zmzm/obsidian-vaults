---
type: twir-item
issue: 272
item: 6
item_type: item
date: 2026-03-11
source: https://amplifying.ai/research/claude-code-picks
tags:
  - "shadcn"
status: auto
---

[[2026-03-11-TWIR-272|Index]]

# Item 6: What Claude Code Actually Chooses

Source: [https://amplifying.ai/research/claude-code-picks](https://amplifying.ai/research/claude-code-picks)

Summary:
A benchmark study reveals that Claude Code, when tasked with building real-world apps, most often chooses to build custom solutions rather than recommend popular tools. When it does pick tools, it favors modern, established ones—e.g., shadcn/ui over MUI, Zustand over Redux, Vitest over Jest. Deployment choices are stack-specific (Vercel for JS, Railway for Python), and traditional cloud providers are rarely selected. The study provides insight into how AI agents shape tool adoption in the React/JS ecosystem.

Key takeaways:
- Claude Code prefers custom/DIY solutions in most categories, but decisively picks certain tools when needed.
- Modern tools (e.g., shadcn/ui, Zustand, Vitest) are favored over legacy ones (e.g., MUI, Redux, Jest).
- Deployment recommendations are ecosystem-dependent, with Vercel dominating JS frontend.
- AI agent preferences may influence future tool adoption trends.

Recommendation: Read fully (read fully for detailed tool-by-tool breakdowns)
