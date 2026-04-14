# AGENTS

This vault is organized as an LLM-maintained wiki focused on frontend topics.

## Layer Responsibilities

- `raw/` contains source materials and the incoming raw layer.
- `wiki/` contains only derived knowledge pages created and maintained by the agent.
- `system/` contains templates and helper materials that support the structure.

The agent should not rewrite content inside `raw/` unless the user explicitly asks for migration, renaming, or manual normalization of the structure.

## Directories

### Raw

- `raw/twir/` — This Week in React issues and related article notes.
- `raw/articles/` — standalone articles outside TWIR.
- `raw/notes/` — quick manual notes and rough observations.
- `raw/assets/` — local images and attachments.

### Wiki

- `wiki/concepts/` — concepts and mechanisms.
- `wiki/tools/` — frameworks, libraries, and tools.
- `wiki/patterns/` — architectural and UI/UX patterns.
- `wiki/topics/` — broad topic overview pages.
- `wiki/case-studies/` — concrete engineering stories, migrations, incident writeups, and practice-driven pages worth preserving even when they do not become central hubs.
- `wiki/sources/` — normalized pages for important individual sources.
- `wiki/syntheses/` — analytical takeaways, comparisons, and answers worth preserving as long-term knowledge.

## Page Types

Allowed base types:
- `concept`
- `tool`
- `pattern`
- `topic`
- `case-study`
- `source`
- `synthesis`

Every wiki page should have YAML frontmatter with at least:

```yaml
---
type: concept
status: seed
updated: 2026-04-10
tags: []
---
```

Allowed statuses:
- `seed` — an initial hub or starter page.
- `active` — a page with useful structure that is being actively maintained.
- `review` — a page that needs re-checking or refactoring.

## Naming

- Use human-readable filenames.
- For wiki pages, prefer English domain terms when they are standard in frontend work, for example `React Compiler.md`.
- Do not include dates in wiki page names unless the date itself is the subject.
- Source pages may include dates and issue numbers.

## Wiki Page Structure

Unless the user asks for a different format, use this compact structure:

1. Short definition or summary.
2. Key ideas.
3. Practical significance.
4. Related pages.
5. Sources.
6. Open questions.

Do not overbuild seed pages. A seed page may be short, but it should provide:
- a clear definition;
- at least 2-3 links to related pages;
- at least 1-2 source references or an explicit note that they are still missing.

## Core Knowledge vs Interesting Practice

This vault now distinguishes between two useful kinds of durable material:

### Core knowledge

These pages belong in:
- `wiki/concepts/`
- `wiki/tools/`
- `wiki/patterns/`
- `wiki/topics/`
- `wiki/syntheses/`

Use core pages when the material:
- builds reusable mental models;
- acts as a hub for many future links;
- helps answer recurring questions;
- is likely to accumulate multiple supporting sources over time.

### Interesting practice

These pages belong in:
- `wiki/case-studies/`

Use case studies when the material:
- describes a real migration, incident, optimization, or engineering decision;
- is worth preserving even if it does not justify a new central concept page;
- provides a concrete example, tradeoff analysis, or practice pattern;
- is interesting and reusable as evidence, but not necessarily a hub.

Case studies should support the graph without bloating the core knowledge layer.
They are explicitly allowed to be valuable even when they have lower link centrality.

### Reference-only material

Some raw items should remain only in `raw/` for now.

Keep material as raw-only when it:
- is mostly news;
- has weak or missing extraction;
- is too thin to justify either a core page or a case study;
- does not yet connect to any useful branch of the wiki.

## Ingest Rules

When the user asks to process a new source:

1. Determine where it belongs inside `raw/`.
2. Do not overwrite the source without an explicit request.
3. Create or update a page in `wiki/sources/` when needed.
4. Decide whether the source should also produce:
   - a core knowledge update,
   - a case study,
   - or only a raw/reference record for now.
5. Update related pages across `wiki/`.
6. Add links to `index.md` if new permanent pages were created.
7. Append an entry to `log.md`.

By default, one source should lead not only to a source page but also to updates on topical hubs when the material adds meaningful new knowledge.

When a source is interesting but does not cleanly fit an existing concept or tool hub, prefer preserving it as a `case-study` instead of dropping it.

## Query Rules

When the user asks a question about this vault:

1. Start with `index.md`.
2. Then read relevant pages from `wiki/`.
3. Use `raw/` only when primary context is needed or when the wiki is still too shallow.
4. If the answer is durable and reusable, propose saving it to `wiki/syntheses/` or create the page directly when that intent is obvious.

## Lint Rules

When checking wiki quality, look for:
- orphan pages;
- weak or missing backlinks;
- contradictions between pages;
- repeated mentions without a dedicated page;
- outdated or overly vague seed pages;
- duplication across nearby topics.

## Index and Log Updates

- `index.md` is the content map of the vault, not a journal.
- `log.md` is an append-only record of notable operations.

Each `log.md` entry should begin with a heading like:

```md
## [2026-04-10] setup | Initial LLM Wiki scaffold
```

After the heading, briefly list:
- what was created;
- what was updated;
- what next steps now make sense.

## Constraints

- Do not introduce new page types without clear value.
- Do not create standalone pages for every casual mention.
- Do not move knowledge into `wiki/` without minimal normalization and links.
- Do not turn `index.md` into a changelog.
- Do not mix the raw layer with the synthesized layer.
- Do not force every valuable article into a central concept or tool page.
- Do not treat low-centrality material as useless if it contains strong engineering lessons.

## Current Priority

This vault currently starts from TWIR material. The agent's near-term goal is to:
- use `raw/twir/` as the source layer;
- build durable hubs on top of it for key frontend topics;
- gradually turn issues and articles into a connected wiki around React and adjacent frontend tooling.
