---
name: task-workflow
description: Guide for task workflow and pre-task decisions. Use this skill to determine whether to explore first, load skills, or proceed directly with coding.
---

# Task Workflow

This skill governs how to start work without wasting context.

## When to use this knowledge

Use this skill when you are:

- deciding whether a task is exploration, implementation, or mixed
- deciding whether skills should be loaded at all
- planning a task that starts with investigation and later becomes coding
- trying to keep context lean while still using project-specific guidance

## When not to use this knowledge

- detailed domain implementation concerns that belong to frontend or backend skills
- semantic code navigation concerns that belong to `serena`
- creation, packaging, or normalization of skills themselves, which belongs to `skill-creator`

## What this skill covers

This skill provides guidance for:

- classifying the task before starting
- deciding when skills help versus when they only add noise
- sequencing exploration first and implementation second for mixed tasks
- choosing a sensible skill-loading order when multiple skills are needed

## Knowledge map

- This skill is intentionally compact and acts as a workflow router.
- Cross-check `../serena/SKILL.md` when the task is primarily code navigation.
- Cross-check `../skill-creator/SKILL.md` when the task is about creating or editing skills as artifacts.

## Fast decision hints

- If the user asked to implement, refactor, or fix code, load the relevant domain skills before editing.
- If the user asked to inspect, find, understand, or investigate, start with exploration and skip skill loading unless the task turns into implementation.
- If the task is mixed, split it into phases: explore first, then load the smallest useful set of skills before coding.

## Local rules

- `<default>` Default: Start by classifying the task as coding, exploration, or mixed.
- `<default>` Default: Do not load skills for pure navigation or discovery work.
- `<heuristic>` Heuristic: For mixed tasks, keep the exploration phase skill-light and load skills only once the implementation boundary is clear.
- `<exception>` Exception: Load a skill early during exploration only when the user explicitly asks for conventions, standards, or project-specific rules up front.

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **workflow choice and context discipline**. For:

- **semantic code navigation and symbol-level editing** → see `serena`
- **creating or packaging skills** → see `skill-creator`
- **domain implementation rules** → move into the relevant frontend or backend skill once the task is scoped

## Maintenance Notes

- Keep this file routing-oriented.
- Move dense examples and edge cases into references or neighboring workflow docs if they appear later.
- Prefer small, explicit workflow rules over long explanatory prose.
