---
id: common/engineering/verification-and-change-safety
name: common/engineering/verification-and-change-safety
kind: reference
domain: common
topics: [verification evidence, testing, change safety, task authorization, refactoring]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# Verification and Change Safety

> **Canonical source** for shared test selection, evidence reporting, and authorized change boundaries. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use when planning checks, reviewing reliability claims, refactoring, or moving from local implementation to deployment or operational acceptance.

## Rules

### Mandatory: verification evidence and task authorization

- Report checks accurately as passed, failed, skipped, or unverified, including scope and material limitations. A skipped check did not pass; file existence, compilation, or a mock response does not prove retrieval, delivery, or live behavior.
- Distinguish implemented (code changed), tested (specified checks ran), deployed (the target runs that version), and operationally accepted (the requested workflow met its acceptance criteria in that environment). Evidence for one does not imply the others.
- Respect existing task authorization. Continue routine inspection, edits, and verification already within the approved scope without repeated permission requests. Authorization does not expand itself: production mutations, service restarts, deployments, and paid model calls must fit the authorized actions, target, limits, and cost. Prepare a concrete reviewable change before requesting any missing approval; do not execute the unauthorized step.
- Preserve unrelated work and public/persisted contracts during a behavior-preserving refactor. Label intentional behavior changes and apply their compatibility requirements explicitly.

### Default: behavior tests and change safety

- Select tests by observable behavior, invariants, and failure risk. Exercise important branching, invalid inputs, and failure boundaries instead of mirroring private helpers or asserting every call just because it exists.
- Include partial failure, concurrent claims, crash/restart, and replay checks when those risks are relevant. Inject failure around effect and persistence boundaries; prove safe recovery or explicit uncertainty, not just the happy path.
- Separate refactoring from behavior changes where practical so a reviewer can assess each. Establish relevant baseline behavior, make small changes, and run the checks affected by those changes. A pre-existing failure should be recorded rather than concealed.
- Use project-required checks and coverage thresholds. Coverage identifies unexercised paths; 80% or any other percentage is project-specific and does not prove assertions are meaningful.

### Heuristics: verification scope and live acceptance

- Keep verification proportional to impact: a local naming change may need existing focused checks; a retry/recovery change needs failure and replay evidence. Add tests when they protect behavior or an invariant, not merely to restate a reversible edit.
- Live acceptance can expose integration gaps but may cause real effects and cost. Use isolated fixtures or dry runs where sufficient and record what remains unverified; a dry run cannot prove the live mutation succeeded.

## Verification evidence: mocks, integration tests, and live acceptance

| Check | Useful evidence | Limit |
| --- | --- | --- |
| Mock-based unit test | Decision logic and responses to modeled dependency outcomes | The model may omit real provider behavior; no proof of real durability, routing, or transaction isolation |
| Integration test | Real adapters, serialization, storage constraints, and failure behavior exercised by its setup | Usually excludes some deployed configuration or dependencies |
| Live acceptance | The specified workflow works in the target environment under the observed conditions | Does not prove every race, restart window, or future run |

## Failure scenario: restart and replay

A mock test returns a successful remote result and passes. It does not prove that a process restart between execution and result persistence avoids duplicate work.

Better checks for that risk: interrupt after the remote effect but before saving confirmation, restart using persisted intent, reconcile by the same operation identity, and assert either one logical effect under the provider's idempotency contract or an explicit uncertain state. Separately fail delivery and verify that it resumes without re-executing the operation. Test concurrent claims if multiple workers are supported.

A useful report might say: “Unit and isolated integration checks passed. Live delivery was skipped because it requires an additional authorized external action. Deployment and operational acceptance remain unverified.” Include actual failures when present rather than copying this example as boilerplate.

## Related guidance

- [Contracts and validation](contracts-and-validation.md) for compatibility and internal renames.
- [State and recovery](state-and-recovery.md) and [retries and idempotency](retries-and-idempotency.md) for failure invariants.
- [Task-workflow](../../task-workflow/SKILL.md) for sequencing and context loading.
- [Backend test layer patterns](../../../backend/testing/references/test-layer-patterns.md) and [frontend testing](../../../frontend/testing/SKILL.md) for framework test setup.
- [Backend refactoring scope](../../../backend/refactor/references/permission-required.md) for contract-change examples.
