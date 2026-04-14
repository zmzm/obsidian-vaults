---
type: twir-item
issue: 262
item: 2
item_type: item
date: 2025-12-10
source: https://github.com/facebook/react/pull/35277
tags:
  - "PR"
  - "FlightReplyServer"
  - "ReactFlightClient"
  - "ServerComponents"
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 2: React PR - Patch FlightReplyServer with fixes from ReactFlightClient

Source: [https://github.com/facebook/react/pull/35277](https://github.com/facebook/react/pull/35277)

Summary:
A major React PR synchronizes FlightReplyServer (client-to-server) with ReactFlightClient (server-to-client), incorporating structural refactors and critical security fixes for React Server Components. The patch addresses deep cycle resolution, deferred error handling, and closes the CVE-2025-55182 vulnerability. The fix is bundled with other changes, making it hard to isolate the security-relevant code, and maintainers note the need for more granular commits in the future.

Key takeaways:
- React Server Components users must upgrade to 19.2.1 or later to patch a critical RCE vulnerability.
- The patch includes both refactors and the security fix, spanning over 1500 lines.
- The vulnerability allows RCE via a single crafted HTTP request in affected versions (19.0–19.2.0).
- The bundled nature of the fix complicates code review and reverse engineering.

Recommendation: Read fully (for those maintaining or auditing React Server Components)

Related notes: [[Server Components]]
