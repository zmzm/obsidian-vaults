---
type: twir-item
issue: 282
item: 4
item_type: item
date: 2026-05-20
source: https://lachlan.nz/blog/the-react2shell-story
tags:
  - "React2Shell"
status: auto
quality: keep
---

[[2026-05-20-TWIR-282|Index]]

# Item 4: The React2Shell Story

Source: [https://lachlan.nz/blog/the-react2shell-story](https://lachlan.nz/blog/the-react2shell-story)

Summary:
This is a detailed narrative of discovering and reporting the critical React2Shell remote code execution vulnerability (CVE-2025-55182) in React’s Flight protocol. The author describes the process of reverse engineering the undocumented protocol, identifying a flaw where prototype properties could be referenced and exploited, and the subsequent responsible disclosure and patch by Meta. The post also explores how the protocol’s flexibility and lack of strict validation enabled novel attack vectors.

Key takeaways:
- React’s Flight protocol allowed referencing prototype properties, leading to a critical RCE vulnerability.
- Lack of protocol documentation and strict validation increased attack surface for Next.js and React Server Functions.
- The vulnerability was quickly patched after responsible disclosure; developers are urged to update.
- The story highlights the importance of protocol transparency and input validation in modern frameworks.

Recommendation:
Read fully (for security awareness and understanding the implications of protocol-level vulnerabilities)

Why it matters:
for security awareness and understanding the implications of protocol-level vulnerabilities

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
