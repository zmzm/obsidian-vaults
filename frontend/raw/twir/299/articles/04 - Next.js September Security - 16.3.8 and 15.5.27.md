---
type: twir-item
issue: 299
item: 4
item_type: item
date: 2026-09-30
source: https://nextjs.org/blog/september-2026-security-release
tags:
  - "Nextjs"
  - "1638"
  - "15527"
status: auto
quality: keep
---

[[2026-09-30-TWIR-299|Index]]

# Item 4: Next.js September Security - 16.3.8 and 15.5.27

Source: [https://nextjs.org/blog/september-2026-security-release](https://nextjs.org/blog/september-2026-security-release)

Summary:
Next.js released security updates addressing several vulnerabilities, including a high-severity SSRF in image optimization and multiple medium-severity cache and information disclosure issues. Affected users should upgrade to v16.3.8 or v15.5.27. The post details each vulnerability, its impact, and mitigation steps.

Key takeaways:
- Critical and high-severity vulnerabilities fixed; immediate upgrade recommended.
- Issues include SSRF, cache poisoning, information disclosure, and draft mode leaks.
- Some vulnerabilities only affect self-hosted or development environments.
- Security program and bug bounty information provided.

Recommendation:
Read fully (read fully if you maintain Next.js apps, especially self-hosted or with custom image optimization)

Why it matters:
read fully if you maintain Next.js apps, especially self-hosted or with custom image optimization

Content:
---
title: September 2026 Security Release
description: The September 2026 security release for Next.js is now available
url: "https://nextjs.org/blog/september-2026-security-release"
docs\_index: /docs/llms.txt
publishedAt: September 30th 2026
authors:
- Josh Story
- Karim Rahal
- Sebastian Silbermann
---
[Last week](/blog/upcoming-nextjs-security-release-september-2026) we announced an upcoming security release for Next.js. A fix for one critical vulnerability and one high severity vulnerability was postponed due to upstream dependency delays.
Updates are now available in v16.3.8 (Active LTS) and v15.5.27 (Maintenance LTS) to address these issues. Please patch your Next.js dependencies to maintain the security of your applications.
```bash filename="Terminal"
npm install next@15.5.27 # for 15.5
npm install next@16.3.8 # for 16.3
```
## Impact
### Server-Side Request Forgery in Image Optimization (High Severity)
[\*\*CVE-2026-94483\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94483) / [\*\*GHSA-cjq9-62q9-8jv4\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-cjq9-62q9-8jv4)
An attacker-controlled, allow-listed remote URL can lead to Server-Side Request Forgery (for example to private IP ranges) during Image Optimization. If no `images.remotePatterns` are configured, your application is not affected.
[\*\*CVE-2026-94543\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94543) / [\*\*GHSA-4jqv-mc3x-m676\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-4jqv-mc3x-m676)
Self-hosted Next.js applications that use the Pages Router with statically generated (SSG) or incrementally regenerated (ISR) pages can have a page's cache entry replaced with content from a different route, causing the affected page to serve wrong content to every visitor until the entry is revalidated. Applications deployed on Vercel are not affected.
[\*\*CVE-2026-94484\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94484) / [\*\*GHSA-mcj8-r9mp-w47p\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-mcj8-r9mp-w47p)
Next.js applications that use a root-level catch-all page together with statically generated or Incremental Static Regeneration routes can have their shared response cache poisoned by a single unauthenticated crafted request.
[\*\*CVE-2026-94485\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94485) / [\*\*GHSA-f87g-xv8r-7p7x\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-f87g-xv8r-7p7x)
In Next.js App Router applications built with webpack, metadata image routes such as `opengraph-image` and `twitter-image` ignore the `dynamicParams` route segment option. An attacker can request metadata image URLs for dynamic segments that were deliberately excluded from `generateStaticParams()`. Applications built with Turbopack are not affected.
[\*\*GHSA-h694-7cp9-m8p3\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-h694-7cp9-m8p3)
With Cache Components enabled, a `'use cache'` function that calls another `'use cache'` function that reads a root param can be keyed incorrectly: the enclosing function's cache key omits that root param, so content produced for one root param value can be served for a different value, whether the page is prerendered or rendered dynamically. What values are leaked cannot be attacker controlled.
[\*\*CVE-2026-94544\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94544) / [\*\*GHSA-3w37-wq28-93x7\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-3w37-wq28-93x7)
Pending `use cache` fills are shared across requests for the same key without distinguishing Draft Mode requests from regular requests. A regular request that overlaps an editor's Draft Mode request receives unpublished content without any authentication; if that request prerenders a page, the unpublished content can be persisted into the generated page and served to all later visitors until the page is revalidated. Sites are affected if they enable Cache Components (or `experimental.useCache`) and serve Draft Mode previews whose cached functions return draft-dependent content.
### Information disclosure in the Next.js development server's Model Context Protocol endpoint (Low Severity)
[\*\*CVE-2026-94486\*\*](https://www.cve.org/CVERecord?id=CVE-2026-94486) / [\*\*GHSA-39w2-rjm5-chcv\*\*](https://github.com/vercel/next.js/security/advisories/GHSA-39w2-rjm5-chcv)
The Next.js development server (`next dev`) exposes a Model Context Protocol endpoint that does not verify which website a request originates from, allowing a malicious website visited by the developer to read sensitive development data, including the project's location on disk, source code snippets from error reports, the route inventory, and development logs. Only applications run with `next dev` are affected. Production deployments do not serve this endpoint.
## Our security program
We work with a talented set of researchers to secure Next.js and other open source frameworks through [Vercel's Open Source Bug Bounty](https://hackerone.com/vercel). Anyone interested in contributing to the security of eligible frameworks is encouraged to participate there.
Any questions or concerns regarding our security programs or vulnerability management can be sent to [security@vercel.com](mailto:security@vercel.com).
