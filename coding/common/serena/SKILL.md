---
name: serena
description: Guide for using Serena MCP semantic code tools effectively. Use when navigating codebases, finding symbol definitions or references, and making symbol-level code edits.
---

# Serena MCP Skill

This skill governs when Serena is the right tool and how to use it without wasting context.

## When to use this knowledge

Use this skill when you are:

- navigating an unfamiliar codebase by symbols rather than raw text
- finding definitions, references, call sites, and file structure
- editing code at symbol level with lower risk than broad text replacement
- deciding whether Serena tools are better than grep or full-file reads

## When not to use this knowledge

- **regular search (grep)** for plain-text patterns, non-code files, or unknown identifiers
- **full-file reading** when symbol-level reads are enough
- **broad text replacement** only when the change is too small or too local to justify symbol tooling

## What this skill covers

This skill provides guidance for:

- selecting the right Serena tool for navigation or editing
- workflows for understanding code, debugging, refactoring, and adding features
- symbol-level editing discipline
- tradeoffs between Serena, grep, and text replacement

## Knowledge map

- Tool reference → `references/tools.md`
- Common workflows → `references/workflows.md`
- Editing patterns → `references/editing.md`

## Fast decision hints

- If you need to understand a code file, start with `get_symbols_overview` before reading bodies.
- If you need to assess impact before changing behavior, use `find_referencing_symbols` before editing.
- If the task is simple text search outside code structure, prefer grep instead of Serena.

## Local rules

- `<default>` Default: Start with overview instead of reading entire files.
- `<default>` Default: Use symbol paths for precision such as `ClassName/methodName`.
- `<heuristic>` Heuristic: Check references before modifying symbols that may have cross-file impact.
- `<exception>` Exception: Prefer text tools over Serena only when the change is trivial and symbol tooling adds unnecessary overhead.

For cross-vault wording and priority rules, see `../../RULES.md` or the nearest root copy in context.

## Boundary with Other Skills

This skill covers **semantic code navigation and symbol-level editing**. For:

- **task triage and deciding whether to load skills** → see `task-workflow`
- **skill creation and packaging** → see `skill-creator`
- **domain-specific implementation rules** → move into the relevant frontend or backend skill after navigation is complete

## Maintenance Notes

- Keep this file focused on tool choice and operating discipline.
- Put detailed tool behavior and step-by-step workflows into references.
- Prefer explicit tool-selection rules over generic “best practices” phrasing.
