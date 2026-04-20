---
type: twir-item
issue: 250
item: 3
item_type: item
date: 2025-09-17
source: https://blog.cloudflare.com/deep-dive-into-cloudflares-sept-12-dashboard-and-api-outage/
tags:
  - "useEffect"
  - "API"
status: auto
quality: keep
---

[[2025-09-17-TWIR-250|Index]]

# Item 3: Cloudflare had a major outage due to an useEffect infinite loop triggering API requests

Source: [https://blog.cloudflare.com/deep-dive-into-cloudflares-sept-12-dashboard-and-api-outage/](https://blog.cloudflare.com/deep-dive-into-cloudflares-sept-12-dashboard-and-api-outage/)

Summary:
Cloudflare experienced a major outage caused by a React useEffect bug that repeatedly triggered API calls due to an unstable object in the dependency array. This led to a thundering herd of requests, overwhelming their Tenant Service API and cascading failures across their dashboard and other APIs. The post details the incident timeline, root cause analysis, and the mitigation steps taken, including improvements to deployment, rate limiting, and observability.

Key takeaways:
- A React useEffect dependency mistake can have severe production consequences, especially with API calls.
- Including unstable objects in dependency arrays can cause infinite loops and repeated side effects.
- Robust deployment and monitoring practices (e.g., rollout automation, rate limiting) are critical for resilience.
- Postmortem includes actionable lessons for React teams on effect management and incident response.

Recommendation:
Summary sufficient (read full post for in-depth incident/ops details)

Why it matters:
read full post for in-depth incident/ops details

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
