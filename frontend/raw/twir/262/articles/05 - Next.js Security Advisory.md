---
type: twir-item
issue: 262
item: 5
item_type: item
date: 2025-12-10
source: https://nextjs.org/blog/CVE-2025-66478
tags:
  - "Nextjs"
  - "React2Shell"
  - "ServerComponents"
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 5: Next.js Security Advisory

Source: [https://nextjs.org/blog/CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478)

Summary:
Next.js published a security advisory for CVE-2025-66478, which mirrors the upstream React2Shell vulnerability (CVE-2025-55182). The advisory details affected versions, fixed releases, and provides explicit upgrade instructions. All users of Next.js App Router with React Server Components must upgrade immediately; there is no workaround, and secret rotation is recommended for previously unpatched deployments.

Key takeaways:
- All Next.js App Router users with RSC must upgrade to patched versions (15.0.5+, 16.0.7+, or latest canaries).
- No workaround exists; patching is mandatory.
- Secret rotation is advised for apps that were online and unpatched during the vulnerability window.
- Comprehensive resources and upgrade tools are provided.

Recommendation: Read fully (read fully if you maintain a Next.js app using App Router and RSC)

Related notes: [[Server Components]]
