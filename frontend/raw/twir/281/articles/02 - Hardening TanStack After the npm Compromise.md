---
type: twir-item
issue: 281
item: 2
item_type: item
date: 2026-05-13
source: https://tanstack.com/blog/incident-followup
tags:
  - "TanStack"
  - "npm"
status: auto
quality: keep
---

[[2026-05-13-TWIR-281|Index]]

# Item 2: Hardening TanStack After the npm Compromise

Source: [https://tanstack.com/blog/incident-followup](https://tanstack.com/blog/incident-followup)

Summary:
TanStack experienced a sophisticated npm supply chain attack via GitHub Actions cache poisoning, leading to malicious package versions being published. The incident postmortem details the attack chain and immediate mitigations, including disabling caches, enforcing stricter 2FA, and removing insecure workflow patterns. The team acknowledges workflow design flaws and outlines both short-term and ongoing process improvements to prevent recurrence.

Key takeaways:
- Attack exploited pull_request_target and shared CI cache to steal a short-lived publish token.
- No maintainer credentials were directly compromised; the attack leveraged CI workflow trust boundaries.
- Immediate actions: disabled caches, pinned actions, enforced stronger 2FA, removed insecure workflow triggers.
- Root cause was a known-bad workflow pattern; ongoing work aims to redesign workflows for stronger isolation.

Recommendation:
Read fully (for anyone maintaining open source packages or CI/CD pipelines)

Why it matters:
for anyone maintaining open source packages or CI/CD pipelines

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
