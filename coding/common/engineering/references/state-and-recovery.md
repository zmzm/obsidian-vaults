---
id: common/engineering/state-and-recovery
name: common/engineering/state-and-recovery
kind: reference
domain: common
topics: [state transitions, crash recovery, persistence ordering, startup reconciliation, concurrency]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# State and Recovery

> **Canonical source** for shared state, crash recovery, and side-effect ordering decisions. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use for jobs, approval flows, service control, file delivery, or other workflows that can be interrupted, restarted, or handled concurrently.

## Rules

### Mandatory: transitions, durability, and concurrency

- Define states, allowed transitions, and invariants at the level the workflow needs. Identify who may transition state and what evidence establishes completion. An approval authorizes a bounded action; it does not prove execution or delivery.
- State the storage guarantee accurately: in-memory state disappears with the process; atomic publication prevents readers seeing a partial replacement; durable storage survives the failures covered by the storage contract. An atomic rename alone does not establish power-loss durability.
- Do not describe a local file write and a remote action as one atomic transaction. Enumerate the crash windows between intent persistence, dispatch, remote execution, outcome persistence, and delivery.
- Document concurrency assumptions. An in-process mutex protects only cooperating code in that process; a host-local lock does not coordinate other hosts or remote workers. Use storage-level conditional transitions, uniqueness, or leases with fencing where competing workers could violate an invariant.

### Default: persistence ordering and crash recovery

- Persist the operation identity and stable intent before dispatch when recovery depends on knowing what was attempted. If that persistence fails, stop before the effect. Recording intent does not prove that dispatch occurred.
- Persist confirmed execution evidence before treating the operation as complete. If recording the result fails after the remote action succeeds, treat recovery as uncertain and reconcile rather than blindly repeating the action.
- On startup, inspect interrupted or expired work and reconcile against authoritative external evidence. Do not turn every stale `running` record into a new attempt. If evidence cannot settle the outcome, retain uncertainty and expose a recovery action.
- Track execution separately from result delivery. An operation can succeed while notification or download delivery fails; resume delivery from a retained result when possible instead of re-executing the operation.
- Make claims and transitions atomic within the chosen storage boundary. A check followed by a write can race even if each call succeeds individually.

### Heuristics: recovery storage and leases

- Use durable intent/outbox records when recovery must outlive a process. Choose a database, journal, or file protocol according to actual crash and concurrency requirements; a small disposable script may need only an explicit failure report.
- Lease expiry means ownership may be stale, not that remote work stopped. Fence stale workers when supported, and reconcile effects that cannot be fenced.

## Failure scenario: result delivery after execution

| Transition | Evidence / recovery rule |
| --- | --- |
| `pending → dispatched` | Persist intent and claim first; a crash before or after dispatch leaves execution uncertain. |
| `dispatched → confirmed` | Record authoritative execution evidence; if absent after restart, query by the stable operation identity. |
| `confirmed → delivered` | Deliver the retained result; delivery failure leaves execution confirmed. |

Bad: mark `done` in memory, send the result, then save. A crash can lose both the result and the completion evidence. Better: record the confirmed result, then attempt delivery and record delivery evidence separately. Delivery can itself have an uncertain outcome, so it may need its own deduplication or acknowledgment contract.

For a service restart, process liveness alone is not proof that the requested recovery completed. For a generated file, artifact creation alone is not proof that the recipient received it.

## Related guidance

- [Retries and idempotency](retries-and-idempotency.md) for uncertain outcomes and duplicate prevention.
- [Contracts and validation](contracts-and-validation.md) for reading old or corrupt state.
- [Errors and observability](errors-and-observability.md) for health and completion evidence.
- [Database transactions](../../../backend/database/references/transactions.md) for effects contained in a database transaction.
