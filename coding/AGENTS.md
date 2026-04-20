# AGENTS

This vault is organized as an instruction-oriented coding vault.

Its purpose is not to act as a source-ingest wiki, but as a curated library of reusable coding rules, patterns, and domain-specific skills for AI-assisted software work.

## Vault Responsibilities

- `frontend/` contains frontend implementation skills and their references.
- `backend/` contains backend implementation skills and their references.
- `common/` contains cross-cutting skills that apply across domains or support the maintenance of the skill system itself.

## How to Use This Vault

When the user asks for coding help based on this vault:

1. Start with `index.md`.
2. Identify the relevant domain:
   - `frontend/`
   - `backend/`
   - `common/`
3. Read the most relevant `INDEX.md` if it exists.
4. Read the target `SKILL.md`.
5. Follow linked `references/` pages only as needed.

Do not load many skill folders at once unless the task clearly spans multiple domains.

## Skill Structure

Each skill directory should contain:

- `SKILL.md` as the entry point.
- `references/` for focused supporting guidance.

Optional supporting files are allowed when a skill genuinely needs scripts, templates, or packaging helpers.

Use the shared root files when creating or normalizing content:

- `RULES.md` for cross-vault rule priority and wording discipline.
- `templates/SKILL.template.md` for new or rewritten skills.
- `templates/REFERENCE.template.md` for new or rewritten references.
- `templates/INDEX.template.md` for new domain index pages.

## Authoring Rules

- Keep `SKILL.md` concise and routing-oriented.
- Put detailed conventions, examples, and edge cases into `references/`.
- Prefer explicit boundaries between neighboring skills.
- Prefer short, actionable rules over broad theory.
- Use examples only when they clarify a real decision or prevent a common mistake.

## Constraints

- Do not treat this vault like a knowledge wiki with `raw/` and synthesis layers.
- Do not duplicate the same guidance across many skills unless it is intentionally canonical.
- Do not create new skill folders for every small topic; prefer references inside an existing skill until a boundary is truly needed.
- Do not rewrite existing guidance wholesale unless the user asks for a broader refactor.

## Maintenance Priorities

When improving this vault, prioritize:

1. navigation clarity;
2. consistent skill boundaries;
3. removal of duplicated or conflicting rules;
4. better examples for recurring coding decisions;
5. gradual normalization of structure and metadata.

## Normalization Strategy

This vault may contain older skill files that predate the current structure.

When updating existing content:

1. preserve useful domain guidance;
2. align the file to the shared templates where practical;
3. replace repeated boilerplate with links to root guidance when possible;
4. rewrite overly absolute rules into explicit categories:
   - `mandatory`
   - `default`
   - `heuristic`
   - `exception`
5. prefer gradual migration over broad rewrites.
