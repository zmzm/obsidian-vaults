---
id: common/engineering/contracts-and-validation
name: common/engineering/contracts-and-validation
kind: reference
domain: common
topics: [runtime validation, contracts, schema evolution, compatibility]
priority: high
status: stable
canonical: true
updated: 2026-10-23
---

# Contracts and Validation

> **Canonical source** for shared runtime boundary and compatibility decisions. Categories and priority follow [RULES](../../../RULES.md).

## When to use

Use when data enters through an API, CLI, environment, configuration file, upstream response, or persisted record, or when changing a public or stored contract.

## Rules

### Mandatory: runtime contracts and compatibility

- Validate untrusted data before relying on it for decisions or effects: shape, ranges, size limits, and relevant semantic constraints. Validation does not establish authorization; check access separately.
- Distinguish compile-time assumptions from runtime evidence. TypeScript annotations/assertions and Python type hints do not validate decoded JSON, environment strings, or disk contents.
- Preserve API and persisted-state compatibility unless a behavior change is authorized. Check consumers, stored versions, generated schemas, and mixed-version rollout before changing fields, meanings, or accepted values.

### Default: validate at ownership boundaries

- Validate configuration before starting dependent work. Decode and validate upstream responses and loaded state at their entry points; reject, quarantine, or migrate invalid/unknown versions explicitly rather than treating them as empty or successful.
- Convert validated transport values into domain values once, then maintain invariants internally. Revalidate where trust or ownership changes; avoid repeating identical checks through every internal call.
- Define outcomes that distinguish caller actions. A boolean is suitable for a true predicate; a job submission may need `rejected`, `confirmed`, and `uncertain` outcomes with appropriate reasons or references.
- Specify missing versus null values, defaults, units, and unknown-field behavior. For evolution, consider additive changes, versioned readers, backfill, rollback compatibility, and a migration path for existing records.
- Use the project's validation mechanism. NestJS, Prisma, Zod, and other libraries are implementation choices, not universal prerequisites.

### Heuristics: evolution and internal renames

- Use strict rejection for malformed command inputs; tolerant readers may suit independently evolving upstream responses if required fields and semantics remain checked. Silently dropping fields can hide producer mistakes.
- An internal symbol rename can be behavior-preserving when all consumers are updated. A serialized field, CLI option, exported symbol, or generated schema name may be a public contract; inspect actual consumers rather than inferring impact from a class name.

## Example: validate after decoding

```python
import json


def read_attempt_limit(text: str) -> int:
    data = json.loads(text)
    if not isinstance(data, dict):
        raise ValueError("configuration must be an object")
    limit = data.get("attempt_limit")
    # bool is an int subclass in Python; reject it here.
    if type(limit) is not int or not 1 <= limit <= 10:
        raise ValueError("attempt_limit must be an integer from 1 to 10")
    return limit
```

Bad: `const config = JSON.parse(text) as Config` followed by a remote call using `config.attemptLimit`. The assertion neither checks the value nor supplies a missing default. The example's range is specific to that configuration contract.

## Related guidance

- [Retries and idempotency](retries-and-idempotency.md) for outcome semantics.
- [State and recovery](state-and-recovery.md) for persisted invariants.
- [Backend input validation](../../../backend/security/references/input-validation.md) and [API DTO design](../../../backend/api/references/dto-design.md) for framework examples.
- [Database migrations](../../../backend/database/references/migrations.md) for Prisma procedures, within authorized scope.
