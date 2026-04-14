---
type: twir-item
issue: 263
item: 2
item_type: item
date: 2025-12-17
source: https://nextjs.org/blog/security-update-2025-12-11
tags:
  - "Nextjs"
  - "DoS"
  - "ServerComponents"
status: auto
---

[[2025-12-17-TWIR-263|Index]]

# Item 2: Next.js Security Update

Source: [https://nextjs.org/blog/security-update-2025-12-11](https://nextjs.org/blog/security-update-2025-12-11)

Summary:
Next.js issued a security advisory detailing the downstream impact of the React Server Components vulnerabilities (DoS and Source Code Exposure) on Next.js applications using the App Router. The advisory clarifies affected versions, provides upgrade instructions, and notes that previous fixes were incomplete. Pages Router apps are not affected, but upgrading is still recommended.

Key takeaways:
- Next.js App Router projects must upgrade to specific patched versions; see the provided table for version mapping.
- The advisory includes a CLI tool (npx fix-react2shell-next) to automate version checks and upgrades.
- No workaround exists; upgrading is mandatory for protection.
- Technical details are intentionally limited until most users have upgraded.

Recommendation: Read fully

Related notes: [[Server Components]]
