---
type: twir-item
issue: 191
item: 3
item_type: item
date: 2024-06-26
source: https://github.com/vercel/next.js/pull/67187
tags:
  - "Nextjs"
  - "PR"
  - "nextConfigrequiredEnv"
status: auto
quality: keep
---

[[2024-06-26-TWIR-191|Index]]

# Item 3: Next.js PR draft - nextConfig.requiredEnv

Source: [https://github.com/vercel/next.js/pull/67187](https://github.com/vercel/next.js/pull/67187)

Summary:
This draft PR introduces a requiredEnv option in Next.js configuration, allowing developers to specify environment variables that must be present during the build. If any required variables are missing, the build process exits early with a clear error message, preventing incomplete deployments.

Key takeaways:
- requiredEnv helps enforce presence of critical environment variables at build time.
- Missing variables cause the build to fail fast, reducing deployment errors.
- Usage involves listing required keys in next.config.mjs.

Recommendation:
Read fully (if you manage environment variables or CI/CD pipelines in Next.js)

Why it matters:
if you manage environment variables or CI/CD pipelines in Next.js

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
