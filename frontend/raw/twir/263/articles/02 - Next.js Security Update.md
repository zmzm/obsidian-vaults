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
quality: keep
---

[[2025-12-17-TWIR-263|Index]]

# Item 2: Next.js Security Update

Source: [https://nextjs.org/blog/security-update-2025-12-11](https://nextjs.org/blog/security-update-2025-12-11)

Summary:
Next.js issued a security advisory tracking the impact of the React Server Components vulnerabilities (DoS and source code exposure) on Next.js applications using the App Router. The advisory details affected versions and provides explicit upgrade instructions, noting that previous fixes were incomplete and a new patch is required. No workarounds exist—upgrading is mandatory.

Key takeaways:
- Next.js App Router users must upgrade to the latest patched version; previous upgrades may be insufficient.
- DoS and source code exposure vulnerabilities are inherited from upstream React issues.
- Affected versions and fixed versions are clearly listed; use the provided npx tool for deterministic upgrades.
- Pages Router apps are not affected but upgrading is still recommended.

Recommendation:
Read fully

Content:
---
title: "Next.js Security Update: December 11, 2025"
description: Two additional vulnerabilities have been identified in React Server Components. Users should upgrade to patched versions immediately.
url: "https://nextjs.org/blog/security-update-2025-12-11"
publishedAt: December 11th 2025
authors:
- Josh Story
- Sebastian Markbåge
---
Two additional vulnerabilities have been identified in the React Server Components (RSC) protocol. These issues were discovered while security researchers examined the patches for [React2Shell](/blog/CVE-2025-66478). \*\*Importantly, neither of these new issues allow for Remote Code Execution.\*\* The patch for React2Shell remains fully effective.
These vulnerabilities originate in the upstream React implementation ([CVE-2025-55183](https://www.cve.org/CVERecord?id=CVE-2025-55183), [CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184)). This advisory tracks the downstream impact on Next.js applications using the App Router. For full details, see the [React blog post](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components).
> \*\*Addendum:\*\* The initial fix for CVE-2025-55184 was incomplete. A complete fix has been issued under [CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779). If you previously upgraded to one of the initially recommended versions, please upgrade again to the latest patched versions listed below.
## Impact
### Denial of Service: [CVE-2025-55184](https://www.cve.org/CVERecord?id=CVE-2025-55184) (High Severity)
A specifically crafted HTTP request can be sent to any App Router endpoint that, when deserialized, can cause an infinite loop that hangs the server process and prevents future HTTP requests from being served.
> \*\*Note:\*\* The initial fix for this vulnerability was incomplete. A complete fix has been issued under [CVE-2025-67779](https://www.cve.org/CVERecord?id=CVE-2025-67779). Users who previously upgraded must upgrade again to the latest patched versions.
A specifically crafted HTTP request can cause a Server Function to return the compiled source code of other [Server Functions](https://react.dev/reference/rsc/server-functions) in your application. This could reveal business logic. Secrets could also be exposed if they are defined directly in your code (rather than accessed via environment variables at runtime) and referenced within a Server Function. Depending on your bundler configuration, these values may be inlined into the compiled function output.
## Affected and Fixed Next.js Versions
Applications using React Server Components with the App Router are affected. The table below shows which versions are affected by each vulnerability and the corresponding fix:
| Version | DoS (CVE-2025-55184) | Source Code Exposure (CVE-2025-55183) | Fixed In |
| ----------- | -------------------- | ------------------------------------- | ------------------ |
| >=13.3 | ✓ | — | Upgrade to 14.2.35 |
| 14.x | ✓ | — | 14.2.35 |
| 15.0.x | ✓ | ✓ | 15.0.7 |
| 15.1.x | ✓ | ✓ | 15.1.11 |
| 15.2.x | ✓ | ✓ | 15.2.8 |
| 15.3.x | ✓ | ✓ | 15.3.8 |
| 15.4.x | ✓ | ✓ | 15.4.10 |
| 15.5.x | ✓ | ✓ | 15.5.9 |
| 15.x canary | ✓ | ✓ | 15.6.0-canary.60 |
| 16.0.x | ✓ | ✓ | 16.0.10 |
| 16.x canary | ✓ | ✓ | 16.1.0-canary.19 |
Pages Router applications are not affected, but we still recommend upgrading to a patched version.
## Required Action
All users should upgrade to the latest patched version in their release line:
If you are on Next.js >=13.3, 14.0.x, or 14.1.x, upgrade to the latest 14.2.x release.
```bash filename="Terminal"
npm install next@14.2.35 # for 14.x
npm install next@15.0.7 # for 15.0.x
npm install next@15.1.11 # for 15.1.x
npm install next@15.2.8 # for 15.2.x
npm install next@15.3.8 # for 15.3.x
npm install next@15.4.10 # for 15.4.x
npm install next@15.5.9 # for 15.5.x
npm install next@16.0.10 # for 16.0.x
npm install next@15.6.0-canary.60 # for 15.x canary releases
npm install next@16.1.0-canary.19 # for 16.x canary releases
```
Run `npx fix-react2shell-next` to launch an interactive tool which can check versions and perform deterministic version bumps per the recommended versions above. See the [GitHub repository](https://github.com/vercel-labs/fix-react2shell-next) for full details.
```bash filename="Terminal"
npx fix-react2shell-next
```
There is no workaround. Upgrading to a patched version is required.
## Resources
- CVE-2025-67779 (Complete DoS Fix): [CVE](https://www.cve.org/CVERecord?id=CVE-2025-67779), [Next.js](https://github.com/vercel/next.js/security/advisories/GHSA-5j59-xgg2-r9c4)
- CVE-2025-55184 (DoS): [React](https://www.cve.org/CVERecord?id=CVE-2025-55184), [Next.js](https://github.com/vercel/next.js/security/advisories/GHSA-mwv6-3258-q52c)
- CVE-2025-55183 (Source Code Exposure): [React](https://www.cve.org/CVERecord?id=CVE-2025-55183), [Next.js](https://github.com/vercel/next.js/security/advisories/GHSA-w37m-7fhw-fmv9)
- [React blog: Denial of Service and Source Code Exposure in React Server Components](https://react.dev/blog/2025/12/11/denial-of-service-and-source-code-exposure-in-react-server-components)
- [Previous Security Advisory: CVE-2025-66478](/blog/CVE-2025-66478)
## Discovery
Thank you to [RyotaK](https://ryotak.net) from GMO Flatt Security Inc. and [Andrew MacPherson](https://github.com/AndrewMohawk) for discovering and responsibly disclosing these vulnerabilities. We are intentionally limiting technical detail in this advisory to protect developers who have not yet upgraded.

Related notes: [[Server Components]]
