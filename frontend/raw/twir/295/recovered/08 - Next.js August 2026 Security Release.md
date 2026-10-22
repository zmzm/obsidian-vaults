---
type: "twir-recovery"
issue: 295
item: 8
source: "https://nextjs.org/blog/august-2026-security-release"
final_url: "https://nextjs.org/blog/august-2026-security-release"
retrieved: "2026-10-22T11:30:09+00:00"
original_note: "frontend/raw/twir/295/articles/08 - Next.js August 2026 Security Release.md"
editorial_review: "pending"
truncated: false
---

Original intake note: [[../articles/08 - Next.js August 2026 Security Release|Next.js August 2026 Security Release]]

---
title: August 2026 Security Release
description: The August 2026 security release for Next.js is now available
url: "https://nextjs.org/blog/august-2026-security-release"
docs\_index: /docs/llms.txt
publishedAt: August 25th 2026
authors:
- Josh Story
- Karim Rahal
- Sebastian Silbermann
---
[Last week](/blog/upcoming-nextjs-security-release-august-2026) we announced an upcoming security release for Next.js. [Earlier today](/blog/nextjs-security-release-august-2026-update), we moved the release forward after identifying an additional critical severity vulnerability in one of our upstream dependencies.
Updates are now available in v16.3.3 (Active LTS) and v15.5.24 (Maintenance LTS) to address these issues. Please patch your Next.js dependencies to maintain the security of your applications.
```bash filename="Terminal"
npm install next@15.5.24 # for 15.5
npm install next@16.3.3 # for 16.3
```
## Impact
### Unauthenticated Remote Code Execution in the Image Optimization API when using AVIF (Critical Severity)
[\*\*GHSA-2xp9-vwfh-vxw4\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-2xp9-vwfh-vxw4) / [\*\*GHSA-g89c-p67h-r497\*\*](https://github.com/strukturag/libheif/security/advisories/GHSA-g89c-p67h-r497)
A vulnerability in the underlying libheif library used by `sharp` can lead to unauthenticated remote code execution when Next.js optimizes an attacker-controlled AVIF image. The patched releases disable AVIF optimization until an upstream fix is propagated.
### Unauthenticated Remote Code Execution on Windows-hosted servers (Critical Severity)
[\*\*CVE-2026-75604\*\*](https://www.cve.org/CVERecord?id=CVE-2026-75604) / [\*\*GHSA-p293-qw3h-jr36\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-p293-qw3h-jr36)
A vulnerability in applications using both the Pages Router and App Router without Cache Components can lead to unauthenticated remote code execution when the Next.js server uses a Windows filesystem. Linux and macOS are not affected by this issue. There is no known workaround for affected Windows-hosted applications.
## Our security program
We work with a talented set of researchers to secure Next.js and other open source frameworks through [Vercel's Open Source Bug Bounty](https://hackerone.com/vercel). Anyone interested in contributing to the security of eligible frameworks is encouraged to participate there.
Any questions or concerns regarding our security programs or vulnerability management can be sent to [security@vercel.com](mailto:security@vercel.com).
