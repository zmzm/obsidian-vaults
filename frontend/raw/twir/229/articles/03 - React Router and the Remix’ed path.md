---
type: twir-item
issue: 229
item: 4
item_type: item
date: 2025-04-09
source: https://zhero-web-sec.github.io/research-and-things/react-router-and-the-remixed-path
tags:
  - "ReactRouter"
status: auto
quality: keep
---

[[2025-04-09-TWIR-229|Index]]

# Item 4: React Router and the Remix’ed path

Source: [https://zhero-web-sec.github.io/research-and-things/react-router-and-the-remixed-path](https://zhero-web-sec.github.io/research-and-things/react-router-and-the-remixed-path)

Summary:
Security researchers discovered a vulnerability in React Router (specifically with the Express adapter) and Remix 2, allowing URL manipulation via Host/X-Forwarded-Host headers. This can lead to cache poisoning and potential denial of service if cache keys do not include URL parameters, with the vulnerability assigned CVE-2025-31137. The post details exploitation scenarios and the importance of proper sanitization in routing middleware.

Key takeaways:
- Vulnerability in React Router Express adapter and Remix 2 allows cache poisoning via unsanitized headers.
- Exploits include manipulating Host/X-Forwarded-Host to alter routing and cache behavior.
- Affects applications where cache keys do not include all URL parameters.
- CVE-2025-31137 assigned; mitigation requires careful header and parameter handling.

Recommendation:
Read fully (for anyone using React Router with Express or Remix in production)

Why it matters:
for anyone using React Router with Express or Remix in production

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
