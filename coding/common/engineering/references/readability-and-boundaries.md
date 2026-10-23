---
id: common/engineering/readability-and-boundaries
name: common/engineering/readability-and-boundaries
kind: reference
domain: common
topics: [readability, module boundaries, extraction]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# Readability and Boundaries

> **Canonical source** for shared naming, readability, and extraction decisions. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use when reviewing names, conditions, state mutations, or code that mixes transport handling, domain decisions, and persistence.

## Rules

### Default: readable decisions and module boundaries

- Name values and operations for their domain meaning; include units where confusion would change behavior (`timeoutMs`, `size_bytes`). Prefer `deliveryPending` to an unexplained `flag`.
- Make conditions readable in evaluation order. Use guard clauses or named predicates when they expose the reason for a branch; preserve short-circuit behavior and side-effect ordering.
- Make state mutations explicit. An apparent predicate such as `isReady()` should not silently persist a transition or send a request. Show those operations separately in the calling flow.
- Separate transport parsing/formatting, domain decisions, and persistence when their coupling makes a change or review difficult. A pure decision function and a small caller can be enough; classes and repository layers are not required.
- Extend the project's existing module boundaries and naming conventions before introducing a new architecture.

### Heuristics: extraction without indirection

- Extract when a name explains a cohesive decision, an invariant needs one owner, or independently changing behavior otherwise forces unrelated callers to change.
- Keep a short one-use sequence inline when extraction merely moves obvious statements behind a vague helper. A useful boundary reduces what callers must know; forwarding every argument through several wrappers adds indirection.
- Treat file/function length as a signal to inspect cohesion, nesting, and hidden effects. No line count is a universal limit; a longer readable mapping may be clearer than several tiny forwarding methods.
- Repetition is evidence to examine, not sufficient reason to merge code with different change drivers.

## Example: expose the decision and the mutation

```ts
type Job = { state: 'pending' | 'running'; approved: boolean };

function canStart(job: Job): boolean {
  return job.state === 'pending' && job.approved;
}

const job: Job = { state: 'pending', approved: true };
if (canStart(job)) job.state = 'running';
```

Bad: `if (check(job)) send(job)` where `check` also sets `running` and writes a file. The reviewer cannot see when execution becomes committed. The example above only clarifies mutation; concurrent claims and persistence need their own design.

## Related guidance

- [State and recovery](state-and-recovery.md) for transitions and concurrent claims.
- [Verification and change safety](verification-and-change-safety.md) for preserving behavior while extracting.
- [Backend services](../../../backend/coding/references/services.md) for NestJS conventions and examples.
