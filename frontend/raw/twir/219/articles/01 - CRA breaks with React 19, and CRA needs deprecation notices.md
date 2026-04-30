---
type: twir-item
issue: 219
item: 3
item_type: item
date: 2025-01-29
source: https://github.com/facebook/create-react-app/issues/17004
tags:
  - "CRA"
  - "19"
status: auto
quality: keep
---

[[2025-01-29-TWIR-219|Index]]

# Item 3: CRA breaks with React 19, and CRA needs deprecation notices

Source: [https://github.com/facebook/create-react-app/issues/17004](https://github.com/facebook/create-react-app/issues/17004)

Summary:
Create React App (CRA) is incompatible with React 19 due to peer dependency mismatches, especially with React Testing Library. Although a fix is available by updating template dependencies, the larger issue is that CRA is unmaintained and still widely used by beginners due to outdated documentation and tutorials. The community is pushing for explicit deprecation warnings in CRA’s CLI and docs, and recommends alternatives like Vite for new projects.

Key takeaways:
- CRA fails with React 19 due to outdated dependencies in templates.
- CRA has been unmaintained for over two years but is still widely referenced.
- No official deprecation notice appears in CRA’s CLI or docs.
- Vite is recommended as a modern alternative for client-side React apps.

Recommendation:
Read fully (important for teams maintaining legacy CRA projects or onboarding new React developers)

Why it matters:
important for teams maintaining legacy CRA projects or onboarding new React developers

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
