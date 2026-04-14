---
type: twir-item
issue: 266
item: 14
item_type: item
date: 2026-01-28
source: https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals
tags:
  - "Skills"
  - "AGENTSmd"
status: auto
---

[[2026-01-28-TWIR-266|Index]]

# Item 14: AGENTS.md outperforms Skills in evals

Source: [https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals](https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals)

Summary:
Vercel's evaluation found that embedding a compressed docs index in AGENTS.md (project root) enabled AI coding agents to achieve a 100% pass rate on Next.js 16 tasks, outperforming skills-based approaches (which maxed at 79% even with explicit instructions). The study highlights that passive, always-available context (AGENTS.md) is more reliable than active skill invocation, which agents often fail to trigger. The findings suggest that for framework-specific agent guidance, persistent context is superior to skills-based retrieval.

Key takeaways:
- AGENTS.md (persistent context) outperforms skills-based retrieval for AI coding agents.
- Skills were often not triggered, leading to no improvement over baseline.
- Explicit instructions helped, but results were fragile and wording-sensitive.
- Embedding a docs index in AGENTS.md achieved perfect scores in build, lint, and test tasks.

Recommendation: Read fully (read fully if building AI coding agents or interested in agent context strategies)
