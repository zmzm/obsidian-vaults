---
type: twir-item
issue: 266
item: 3
item_type: item
date: 2026-01-28
source: https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472
tags:
  - "DoS"
  - "Nextjs"
  - "CVEs"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 3: Next.js DoS CVEs

Source: [https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472](https://vercel.com/changelog/summaries-of-cve-2025-59471-and-cve-2025-59472)

Summary:
Two medium-severity denial-of-service vulnerabilities (CVE-2025-59471 and CVE-2025-59472) were found in self-hosted Next.js apps. The first affects the Image Optimizer with unbounded remote image loading, and the second impacts Partial Pre-Rendering (PPR) in minimal mode, allowing memory exhaustion via POST requests. Vercel-hosted apps are not affected; patches and workarounds are available for self-hosted deployments.

Key takeaways:
- CVE-2025-59471: Unrestricted remote image loading can cause server memory exhaustion.
- CVE-2025-59472: PPR resume endpoint can be abused to exhaust memory in minimal mode.
- Fixed in Next.js 15.5.10, 15.6.0-canary.61, 16.1.5, and 16.2.0-canary.9.
- Self-hosted users should upgrade or apply recommended mitigations; Vercel-hosted apps require no action.

Recommendation:
Read fully (read fully if self-hosting Next.js and using affected features)

Why it matters:
read fully if self-hosting Next.js and using affected features

Content:
# Summaries of CVE-2025-59471 and CVE-2025-59472

Applications hosted on Vercel’s platform are not affected by these issues, and require no customer action.

[**CVE-2025-59471**](https://www.cve.org/CVERecord?id=CVE-2025-59471) (CVSS 5.9) affects the Image Optimizer when external image optimization is enabled via `remotePatterns`. The `/_next/image` endpoint loads remote images fully into memory without enforcing a maximum size, allowing an attacker to trigger out-of-memory conditions using very large images hosted on an allowed domain.

[**CVE-2025-59472**](https://www.cve.org/CVERecord?id=CVE-2025-59472) (CVSS 5.9) affects applications with Partial Pre-Rendering (PPR) enabled in minimal mode. The PPR resume endpoint accepts unauthenticated POST requests and processes attacker-controlled data, allowing memory exhaustion through unbounded request buffering or decompression.

**CVE-2025-59471**

- Next.js versions >=10 through <15.5.10
- Next.js versions >=16 through <16.1.5

**CVE-2025-59472**

- Next.js versions >=15 through <15.6.0-canary.61
- Next.js versions >=16 through <16.1.5

Both vulnerabilities can cause the Node.js process to terminate due to memory exhaustion, resulting in application downtime.

**CVE-2025-59471** requires external image optimization to be enabled and the attacker to control a large image hosted on an allowed domain.

**CVE-2025-59472** only affects applications running with the `experimental.ppr: true` or `cacheComponents: true` configuration options and `NEXT_PRIVATE_MINIMAL_MODE=1` as an environment variable.

**Fixed in:**

- `15.5.10`
- `15.6.0-canary.61`
- `16.1.5`
- `16.2.0-canary.9`

**Workaround:**

For self-hosted deployments unable to upgrade immediately:

- Restrict or remove untrusted `remotePatterns`
- Disable Partial Pre-Rendering or minimal mode
- Apply strict request size limits at the reverse proxy layer

We thank [Andrew MacPherson](https://x.com/AndrewMohawk) for their responsible disclosure through our bug bounty program.
