---
type: source
status: active
evidence: mixed
evidence_reviewed: 2026-10-22
updated: 2026-10-22
tags: [react, transitions, actions, source]
---

# React useTransition

This source page preserves earlier performance guidance while correcting its overly narrow description using the current React reference.

## Summary

The current reference includes async Actions and pending UI in transitions. Custom request ordering remains application-owned, and updates after await currently need another transition wrapper. The older article’s synchronous-only framing should not be treated as a complete API contract.

## Why This Source Matters

Separates update priority and Action coordination from fetching policy, mutation sequencing, and expensive synchronous computation.

## Related Pages

- [[../topics/React Rendering|React Rendering]]
- [[../concepts/React use()|React use()]]
- [[../patterns/Optimistic Mutation Coordination|Optimistic Mutation Coordination]]
- [[../syntheses/Async React Patterns - use() vs useTransition vs useEffect|Async React Patterns - use() vs useTransition vs useEffect]]

## Sources

- [[../../raw/articles/React useTransition Reference - 2026-10-22|React useTransition Reference - 2026-10-22]]
- [React useTransition reference](https://react.dev/reference/react/useTransition)
- [[../../raw/twir/270/articles/10 - React’s useTransition The hook you’re probably using wrong|10 - React’s useTransition The hook you’re probably using wrong]] — historical article; its narrow framing is superseded for general API guidance.

## Open Questions

- Which async flows need higher-level framework ordering rather than a custom transition?
