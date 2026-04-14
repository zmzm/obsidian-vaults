---
type: twir-item
issue: 261
item: 11
item_type: item
date: 2025-12-03
source: https://eliocapella.com/blog/ai-library-migration-guide/
tags:
  - "6000"
  - "ASTs"
  - "SET"
status: auto
---

[[2025-12-03-TWIR-261|Index]]

# Item 11: Migrating 6000 React tests using AI Agents and ASTs

Source: [https://eliocapella.com/blog/ai-library-migration-guide/](https://eliocapella.com/blog/ai-library-migration-guide/)

Summary:
Elio Capella describes the process of migrating a large React test suite from Testing Library v13 to v14 using AI agents and AST-based codemods. The migration required understanding breaking changes, running both versions in parallel, and automating code updates with jscodeshift. The article details the workflow, challenges with async APIs and timing, and the importance of incremental, test-driven migration.

Key takeaways:
- Large-scale test migrations benefit from codemods and automated tooling.
- Running old and new versions in parallel eases incremental migration.
- v14 introduces async APIs and new setup patterns, requiring significant code changes.
- Manual intervention is still needed for edge cases and coverage validation.

Recommendation: Read fully (read fully if planning or managing large test migrations)
