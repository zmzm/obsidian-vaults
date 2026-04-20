---
type: index
status: active
updated: 2026-04-16
---

# Coding Vault Index

This file is the map of the coding vault. Start here, then move into the most relevant skill area.

## Domains

- [[frontend/INDEX|Frontend Skills Index]] — frontend implementation guidance for React, UI, routing, testing, performance, accessibility, and adjacent concerns.
- [[backend/INDEX|Backend Skills Index]] — backend implementation guidance for NestJS, API structure, database work, debugging, security, testing, and versioning.
- [[common/INDEX|Common Skills Index]] — cross-cutting skills for workflow, Serena usage, and skill authoring/packaging.

## Root Files

- [[AGENTS]] — operating rules for how to navigate and maintain this vault.
- [[RULES]] — shared rule hierarchy and wording model for all coding skills.
- [[log]] — append-only record of notable vault changes.
- [[templates/SKILL.template|Skill Template]] — canonical structure for new `SKILL.md` files.
- [[templates/REFERENCE.template|Reference Template]] — canonical structure for new `references/*.md` files.
- [[templates/INDEX.template|Index Template]] — canonical structure for new domain index pages.

## Intended Use

Use this vault when the goal is to steer how code should be written, reviewed, or structured.

Compared with a knowledge wiki, this vault is:

- more prescriptive;
- more operational;
- less source-oriented;
- organized around tasks and implementation decisions.

## QMD Growth Direction

If this vault becomes the base for a larger `QMD` corpus:

- keep the root navigation stable;
- keep domain boundaries explicit;
- normalize old files gradually instead of mass-rewriting them;
- prefer canonical references over duplicated advice;
- keep detailed examples in reference files, not in root maps.

## Query Heuristic

When answering with this vault:

1. determine the coding domain first;
2. choose the narrowest relevant skill;
3. consult references only where the decision needs more detail;
4. cross over to adjacent skills only when boundaries explicitly require it.
