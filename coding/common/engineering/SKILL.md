---
name: engineering
description: Write and review maintainable, reliable software across TypeScript/JavaScript, Python, services, CLI tools, and automation. Use for module boundaries, runtime contracts, state recovery, uncertain retries, error handling, and verification evidence; use domain skills for framework conventions.
---

# Engineering

## When to use this knowledge

Use this skill when writing or reviewing code whose maintainability or reliability depends on boundaries, contracts, state transitions, external effects, or evidence of correct behavior. It applies across languages and runtimes, including small scripts.

## When not to use this knowledge

- Pure navigation, factual lookup, or work sequencing without an engineering decision: use [task-workflow](../task-workflow/SKILL.md) as needed.
- Framework syntax, UI composition, ORM configuration, or library setup alone: select the relevant [frontend](../../frontend/INDEX.md) or [backend](../../backend/INDEX.md) skill.
- Creating or packaging skills: use [skill-creator](../skill-creator/SKILL.md).

## Knowledge map

Start with the smallest relevant set; do not load every reference for every coding task.

| Decision in the task | Read |
| --- | --- |
| Naming, readable conditions, module boundaries, extraction | [Readability and boundaries](references/readability-and-boundaries.md) |
| External inputs, configuration, runtime validation, compatibility | [Contracts and validation](references/contracts-and-validation.md) |
| State transitions, persistence ordering, crash recovery, concurrent workers | [State and recovery](references/state-and-recovery.md) |
| Timeout with uncertain outcome, safe retries, idempotency, retry budgets | [Retries and idempotency](references/retries-and-idempotency.md) |
| Error categories, safe diagnostics, health signals | [Errors and observability](references/errors-and-observability.md) |
| Test selection, verification evidence, refactoring, task authorization | [Verification and change safety](references/verification-and-change-safety.md) |

For example, a timed-out side effect usually needs retries guidance; add state guidance if its outcome must survive restart. A local naming change usually needs only readability guidance.

## Local rules

- `<mandatory>` Mandatory: Apply the priority and category model in [Coding Vault Rules](../../RULES.md).
- `<default>` Default: Use these references as the canonical source for shared engineering principles. Follow existing project conventions for framework and tooling choices.
- `<heuristic>` Heuristic: Add a neighboring reference only when it resolves a concrete unanswered decision.

## Boundary with Other Skills

[Task-workflow](../task-workflow/SKILL.md) owns task classification, sequencing, and context loading; this skill owns engineering decisions within that work. [Frontend](../../frontend/INDEX.md) and [backend](../../backend/INDEX.md) skills own their framework conventions and examples. Use both when a framework task also presents a shared reliability concern. This skill does not introduce class layers, universal libraries, or a new project architecture.
