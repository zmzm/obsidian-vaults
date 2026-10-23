---
id: common/engineering/retries-and-idempotency
name: common/engineering/retries-and-idempotency
kind: reference
domain: common
topics: [uncertain retries, idempotency, timeouts, backoff, rate limits]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# Retries and Idempotency

> **Canonical source** for shared retry and duplicate-prevention decisions. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use when a request times out, a worker replays work, an upstream is unavailable, or retry logic might repeat a side effect.

## Rules

### Mandatory: uncertain retries and idempotency

- Classify operations by actual semantics. A read may acknowledge a message or consume a one-use token; a write may safely set a value. HTTP method or function name alone does not establish retry safety.
- Distinguish explicit rejection, confirmed success, and uncertain outcome. A timeout, dropped connection, or local cancellation does not prove that the remote operation did not execute. Even an error response may follow a committed effect; rely on the provider's contract.
- Retry effects only when their semantics, a supported idempotency contract, or reconciliation makes repeating safe. Do not infer universal exactly-once execution from a local lock, retry loop, or deduplication table.
- Keep an idempotency key stable for one logical operation and its payload. Define its scope (such as account plus operation type), retention period, concurrent-request behavior, and treatment of payload mismatches. A new key on every attempt defeats deduplication; reuse for a different intent can suppress legitimate work.

### Default: idempotency keys, reconciliation, and timeout budgets

- Return a confirmed result without re-execution. For a rejection that guarantees no effect, correct the cause or retry only if it is transient and within authorization. For uncertainty, query authoritative status by operation identity before replaying where possible. A “not found” response clears replay only when the provider's consistency and retention guarantees establish that no effect occurred.
- Persist the key and normalized payload when work must survive restart; do not regenerate payload fields such as timestamps on each attempt. A client-generated key only helps when the receiver enforces its contract through the effect boundary; storing it locally is insufficient.
- Bound attempts, per-attempt time, total elapsed time, and resource/cost exposure. Use capped exponential backoff with jitter for retryable failures; honor provider rate-limit guidance such as `Retry-After` within the remaining budget.
- Give one layer ownership of retries where practical. Allocate nested timeout budgets so connection setup, attempts, backoff, cleanup, and response delivery fit the outer deadline; independent retry loops can multiply attempts.
- Stop on exhausted budgets, non-retryable failures, unresolved unsafe uncertainty, or authorization limits, and report the retained operation identity and next recovery step safely.

### Heuristics: duplicate-versus-loss tradeoffs

- Repeatedly setting a desired state may be idempotent in one contract but still trigger notifications or race with newer state. Check those consequences before replaying.
- When reconciliation is impossible, choose and document the tradeoff: suppressing replay avoids duplicates but may abandon work that never executed; replaying improves recovery but may duplicate effects. High-impact uncertainty can require an operator decision. Neither choice establishes exactly-once execution.

## Failure scenario: timeout after remote acceptance

Bad: a delivery request times out, so the caller immediately resends with a new request key. The first request may already have delivered the file.

Better: retain the original key and payload, check the receiver's status, and retry with that same key only within the receiver's supported scope and retention window. If status is unknown and the receiver offers no deduplication, preserve `uncertain` and use the documented duplicate-versus-loss policy. A local `sent = true` flag cannot settle the remote result.

## Related guidance

- [State and recovery](state-and-recovery.md) for durable intent and startup reconciliation.
- [Contracts and validation](contracts-and-validation.md) for explicit outcomes.
- [Verification and change safety](verification-and-change-safety.md) for replay tests and authorized production or paid calls.
- [Backend rate limiting](../../../backend/security/references/rate-limiting.md) for server-side NestJS examples.
