---
type: twir-item
issue: 262
item: 4
item_type: item
date: 2025-12-10
source: https://blog.cloudflare.com/5-december-2025-outage/
tags:
  - "5"
  - "2025"
  - "React2Shell"
  - "ServerComponents"
status: auto
---

[[2025-12-10-TWIR-262|Index]]

# Item 4: Cloudflare outage on December 5, 2025

Source: [https://blog.cloudflare.com/5-december-2025-outage/](https://blog.cloudflare.com/5-december-2025-outage/)

Summary:
Cloudflare experienced a 25-minute outage affecting ~28% of HTTP traffic due to changes made to mitigate the React Server Components vulnerability. The outage was triggered by an internal WAF configuration change that exposed a latent bug, unrelated to any cyber attack. The incident highlights the operational risks of rapid security mitigation and the need for safer rollout and configuration systems.

Key takeaways:
- Outage was caused by a WAF configuration change made in response to the React2Shell vulnerability.
- The bug was in legacy proxy code, triggered by disabling an internal test tool.
- Cloudflare is accelerating improvements to rollout and configuration safety.
- No evidence of attack; the incident was operational, not security-related.

Recommendation: Read fully (read fully if you manage infrastructure or WAFs affected by React vulnerabilities)

Related notes: [[Server Components]]
