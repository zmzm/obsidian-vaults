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
quality: keep
---

[[2025-12-10-TWIR-262|Index]]

# Item 5: Next.js Security Advisory

Source: [https://nextjs.org/blog/CVE-2025-66478](https://nextjs.org/blog/CVE-2025-66478)

Summary:
Next.js published a security advisory for CVE-2025-66478, downstream of the React2Shell vulnerability. All applications using React Server Components with the App Router in Next.js 15.x and 16.x are affected and must upgrade to patched versions. The advisory provides clear upgrade instructions, a CLI tool for patching, and recommends rotating secrets if apps were exposed.

Key takeaways:
- Next.js 15.x and 16.x (App Router) are vulnerable; immediate upgrade is required.
- Patched versions and a CLI tool (`npx fix-react2shell-next`) are provided.
- No workarounds exist; patching is mandatory.
- Secret rotation is recommended for previously unpatched deployments.

Recommendation:
Read fully (read fully if you maintain a Next.js App Router app)

Why it matters:
read fully if you maintain a Next.js App Router app

Content:
---
title: "Security Advisory: CVE-2025-66478"
description: A critical vulnerability (CVE-2025-66478) has been identified in the React Server Components protocol. Users should upgrade to patched versions immediately.
url: "https://nextjs.org/blog/CVE-2025-66478"
publishedAt: December 3rd 2025
authors:
- Josh Story
- Sebastian Markbåge
---
> \*\*December 06, 9:05 PM PST:\*\* If your application was online and unpatched as of December 4th, 2025 at 1:00 PM PT, we strongly encourage you to rotate any secrets it uses, starting with your most critical ones.
> \*\*December 06, 7:29 AM PST:\*\* An npm package has been released to update affected Next.js apps. Use `npx fix-react2shell-next` to update now, or visit the [GitHub repository](https://github.com/vercel-labs/fix-react2shell-next) to learn more.
A critical vulnerability has been identified in the React Server Components (RSC) protocol. The issue is rated CVSS 10.0 and can allow remote code execution when processing attacker-controlled requests in unpatched environments.
This vulnerability originates in the upstream React implementation ([CVE-2025-55182](https://www.cve.org/CVERecord?id=CVE-2025-55182)). This advisory ([CVE-2025-66478](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp)) tracks the downstream impact on Next.js applications using the App Router.
## Impact
The vulnerable RSC protocol allowed untrusted inputs to influence server-side execution behavior. Under specific conditions, an attacker could craft requests that trigger unintended server execution paths. This can result in remote code execution in unpatched environments.
> All users should upgrade to a patched version immediately. See the [required action](#required-action) section for specific instructions.
## Affected Next.js Versions
Applications using React Server Components with the App Router are affected when running:
- Next.js 15.x
- Next.js 16.x
- Next.js 14.3.0-canary.77 and later canary releases
Next.js 13.x, Next.js 14.x stable, Pages Router applications, and the Edge Runtime are not affected.
## Fixed Versions
The vulnerability is fully resolved in the following patched Next.js releases:
- 15.0.5
- 15.1.9
- 15.2.6
- 15.3.6
- 15.4.8
- 15.5.7
- 16.0.7
We also released patched canary releases for Next.js 15 and 16:
- 15.6.0-canary.58 (for 15.x canary releases)
- 16.1.0-canary.12 (for 16.x canary releases)
These versions include the hardened React Server Components implementation.
## Required Action
All users should upgrade to the latest patched version in their release line:
```bash filename="Terminal"
npm install next@15.0.5 # for 15.0.x
npm install next@15.1.9 # for 15.1.x
npm install next@15.2.6 # for 15.2.x
npm install next@15.3.6 # for 15.3.x
npm install next@15.4.8 # for 15.4.x
npm install next@15.5.7 # for 15.5.x
npm install next@16.0.7 # for 16.0.x
npm install next@15.6.0-canary.58 # for 15.x canary releases
npm install next@16.1.0-canary.12 # for 16.x canary releases
```
If you are on Next.js 14.3.0-canary.77 or a later canary release, downgrade to the latest stable 14.x release:
```bash filename="Terminal"
npm install next@14
```
If you're currently using canary releases to enable PPR, you can update to 15.6.0-canary.58, which includes a fix for the vulnerability while continuing to support PPR. For other ways to patch older versions, see this [discussion post](https://github.com/vercel/next.js/discussions/86813).
Run `npx fix-react2shell-next` to launch an interactive tool which can check versions and perform deterministic version bumps per the recommended versions above. See the [GitHub repository](https://github.com/vercel-labs/fix-react2shell-next) for full details.
```bash filename="Terminal"
npx fix-react2shell-next
```
There is no workaround—upgrading to a patched version is required.
### Rotating environment variables
Once you have patched your version and re-deployed your application, we recommend rotating all your application secrets. Learn about working with environment variables in the documentation [here](https://nextjs.org/docs/app/guides/environment-variables).
## Resources
- Security advisories: [React (CVE-2025-55182)](https://www.cve.org/CVERecord?id=CVE-2025-55182), [Next.js (CVE-2025-66478)](https://github.com/vercel/next.js/security/advisories/GHSA-9qr9-h5gf-34mp)
- [React blog: Critical Security Vulnerability in React Server Components](https://react.dev/blog/2025/12/03/critical-security-vulnerability-in-react-server-components)
- [Vercel Knowledge Base: React2Shell Security Bulletin](https://vercel.com/kb/bulletin/react2shell)
- [Netlify Blog: Netlify's response to the critical React security vulnerability](https://ntl.fyi/cve-2025-55182)
- [AWS Security Blog: China-nexus cyber threat groups rapidly exploit React2Shell vulnerability](https://aws.amazon.com/blogs/security/china-nexus-cyber-threat-groups-rapidly-exploit-react2shell-vulnerability-cve-2025-55182/)
- [Google Cloud Blog: Responding to CVE-2025-55182: Secure your React and Next.js workloads](https://cloud.google.com/blog/products/identity-security/responding-to-cve-2025-55182)
- [Fastly Blog: Fastly's Proactive Protection for React2Shell, Critical React RCE CVE-2025-55182 and CVE-2025-66478](https://www.fastly.com/blog/fastlys-proactive-protection-critical-react-rce-cve-2025-55182)
- [Akamai Blog: CVE-2025-55182: React and Next.js Server Functions Deserialization RCE](https://www.akamai.com/blog/security-research/cve-2025-55182-react-nextjs-server-functions-deserialization-rce)
## Discovery
Thank you to [Lachlan Davidson](https://github.com/lachlan2k) for discovering and responsibly disclosing this vulnerability. We are intentionally limiting technical detail in this advisory to protect developers who have not yet upgraded.

Related notes: [[Server Components]]
