---
id: common/engineering/errors-and-observability
name: common/engineering/errors-and-observability
kind: reference
domain: common
topics: [error handling, observability, redaction, readiness, business completion]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# Errors and Observability

> **Canonical source** for shared error semantics, safe diagnostics, and completion signals. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use when translating errors, isolating failed work, adding diagnostics, or deciding what a health check or successful response actually proves.

## Rules

### Mandatory: safe error categories and diagnostics

- Preserve useful safe categories and causal context: invalid input, denied access, conflict, dependency failure, and uncertain execution require different responses. Do not collapse them into `false`, `null`, or a generic success report.
- Treat arbitrary error messages, response bodies, and stack traces as potentially sensitive. They may contain credentials, request data, filesystem paths, or upstream payloads. Redact or allowlist diagnostic fields before logging or returning them; access-controlled logs still need data minimization.
- Separate user-facing messages from operator diagnostics. Give users a safe reason and next action; retain causal detail in an appropriately protected diagnostic channel without exposing raw exceptions.

### Default: catch ownership and structured events

- Catch errors to translate at a boundary, recover, isolate independent work, or add useful context. Otherwise propagate to an established handler. The presence of Prisma, file I/O, or an HTTP call does not by itself require or forbid a catch.
- Preserve the original cause through the project's error mechanism. Causes may contain sensitive data too; preservation in memory does not authorize automatic serialization into logs.
- Emit structured events with stable event names, safe outcome categories, and correlation/operation identifiers. Carry correlation through async work and retries, and distinguish attempts from logical operations. Avoid secrets and personal data in identifiers and log each failure at an intentional ownership boundary.
- Report partial success and isolated failures explicitly. Catching one item's failure so a batch continues must leave observable evidence of that failure.

### Heuristics: diagnostics and health signals

- Select diagnostic detail by audience and need; a bounded, redacted trace in a protected sink can help investigation, while a safe category and correlation identifier may suffice for routine events.
- Health signals answer different questions; use only those needed for the service and requested operation:

| Signal | What it establishes | What it cannot establish alone |
| --- | --- | --- |
| Liveness | The process can respond to its liveness check | Dependencies work or a requested job completed |
| Readiness | The instance currently meets its traffic-admission criteria | Every feature or dependency is healthy |
| Application health | Defined capabilities/dependencies pass their checks | A particular business operation succeeded |
| Business completion | Operation-specific success evidence exists | The recipient received the result, unless delivery is part of that evidence |

## Example: preserve a cause without exposing it

```python
class UpstreamUnavailable(RuntimeError):
    pass


def read_status(client):
    try:
        return client.read_status()
    except TimeoutError as cause:
        raise UpstreamUnavailable("status lookup timed out") from cause
```

At the boundary, emit a safe event such as `status_lookup_failed` with category `upstream_timeout` and a validated correlation identifier. Keep the cause available for controlled diagnosis. Bad: log `str(cause)` and the entire request, then return `success: true` because the worker is still alive.

## Related guidance

- [Retries and idempotency](retries-and-idempotency.md) for timeout semantics.
- [State and recovery](state-and-recovery.md) for execution versus delivery.
- [Backend error handling](../../../backend/coding/references/error-handling.md) for NestJS translation and filters.
- [API error responses](../../../backend/api/references/error-responses.md) for HTTP-facing conventions.
