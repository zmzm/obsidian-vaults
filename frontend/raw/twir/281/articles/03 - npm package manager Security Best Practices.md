---
type: twir-item
issue: 281
item: 3
item_type: item
date: 2026-05-13
source: https://github.com/lirantal/npm-security-best-practices
tags:
  - "Security"
  - "npm"
  - "Bun"
status: auto
quality: keep
---

[[2026-05-13-TWIR-281|Index]]

# Item 3: npm package manager Security Best Practices

Source: [https://github.com/lirantal/npm-security-best-practices](https://github.com/lirantal/npm-security-best-practices)

Summary:
This is a comprehensive, practical guide to npm security best practices, covering safe defaults, hardening against supply chain attacks, dependency resolution, and secure local development. It includes actionable advice for disabling post-install scripts, blocking git-based dependencies, using install cooldowns, leveraging security tools, and enforcing provenance and trust policies, with specific instructions for npm, pnpm, and Bun.

Key takeaways:
- Disable post-install scripts globally to prevent supply chain attacks; pnpm and Bun do this by default.
- Use trustPolicy (pnpm) to enforce provenance and block trust downgrades.
- Block git-based dependencies to avoid bypassing registry security.
- Harden installs with tools like npq and Socket Firewall; always enable 2FA and OIDC for publishing.

Recommendation:
Summary sufficient (read sections relevant to your workflow for implementation details)

Why it matters:
read sections relevant to your workflow for implementation details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
