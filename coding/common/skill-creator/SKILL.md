---
name: skill-creator
description: Guide for creating effective skills. Use this skill when creating, restructuring, validating, or packaging skills for this vault.
---

# Skill Creator

This skill governs how skill artifacts should be structured so they remain small, discoverable, and reusable.

## When to use this knowledge

Use this skill when you are:

- creating a new skill folder
- rewriting or normalizing an existing skill
- deciding what belongs in `SKILL.md` versus `references/`, `scripts/`, or assets
- validating or packaging skill artifacts for reuse

## When not to use this knowledge

- ordinary implementation work that belongs to a domain skill
- code navigation tasks that belong to `serena`
- general task triage that belongs to `task-workflow`

## What this skill covers

This skill provides guidance for:

- skill anatomy and directory structure
- progressive disclosure between metadata, `SKILL.md`, and bundled resources
- choosing between instructions, references, scripts, and assets
- validation and packaging support for skill artifacts

## Knowledge map

- Skill structure example → `skill-md-structure.md`
- Reference structure example → `skill-reference-structure.md`
- Scaffolding script → `scripts/init_skill.py`
- Validation helper → `scripts/quick_validate.py`
- Packaging helper → `scripts/package_skill.py`

## Fast decision hints

- If you are creating a new skill, start with the structure docs and then scaffold with `scripts/init_skill.py`.
- If a skill is becoming long or noisy, move detailed material into `references/` instead of expanding `SKILL.md`.
- If the task is really about domain rules rather than skill packaging, switch to the appropriate frontend, backend, or common skill.

## Local rules

- `<default>` Default: Keep `SKILL.md` concise and routing-oriented.
- `<default>` Default: Put detailed examples, schemas, and edge cases into `references/` instead of the main skill file.
- `<heuristic>` Heuristic: Use scripts when a workflow is repetitive, fragile, or benefits from deterministic execution.
- `<exception>` Exception: Keep more detail in `SKILL.md` only when the skill is small enough that splitting it would hurt discoverability more than it helps.

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **skill creation and normalization**. For:

- **code navigation and symbol-level repo work** → see `serena`
- **task triage and deciding whether to load skills** → see `task-workflow`
- **domain-specific coding conventions** → move into the relevant frontend or backend skill

## Maintenance Notes

- Keep this file routing-oriented.
- Prefer one-level-deep references over sprawling prose in `SKILL.md`.
- Keep helper scripts only when they materially reduce repeated manual work.
