---
type: twir-item
issue: 282
item: 1
item_type: featured
date: 2026-05-20
source: https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain
tags:
  - "Shai-Hulud"
  - "npm"
status: auto
quality: keep
---

[[2026-05-20-TWIR-282|Index]]

# Item 1: Mini Shai-Hulud worm keeps digging

Source: [https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain](https://www.wiz.io/blog/mini-shai-hulud-teampcp-hits-antv-supply-chain)

Summary:
A coordinated software supply chain attack, attributed to the “TeamPCP” threat actor, targeted npm packages (notably @antv), GitHub Actions, and a VSCode extension. The malware harvested credentials, exfiltrated sensitive data, and established persistent access using a Python-based backdoor. Exfiltration leveraged GitHub repositories, and the campaign demonstrates advanced operational maturity. Organizations are urged to audit for compromise, rotate credentials, and strengthen supply chain defenses.

Key takeaways:
- Attack affected npm packages, GitHub Actions, and a VSCode extension, with multi-stage infection and credential theft.
- Malware used GitHub infrastructure for payload delivery and data exfiltration, including orphaned commits and public repos.
- Persistence achieved via a Python backdoor polling GitHub for commands; detection indicators include specific file paths and repo descriptions.
- Immediate response should include auditing systems, rotating secrets, and implementing stronger supply chain controls.

Recommendation:
Read fully (especially if you use affected packages or manage CI/CD environments)

Why it matters:
especially if you use affected packages or manage CI/CD environments

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
