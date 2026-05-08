---
type: twir-item
issue: 208
item: 7
item_type: item
date: 2024-11-06
source: https://alexocallaghan.com/upgrading-react-with-microfrontends
tags:
status: auto
quality: keep
---

[[2024-11-06-TWIR-208|Index]]

# Item 7: Upgrading React with micro-frontend

Source: [https://alexocallaghan.com/upgrading-react-with-microfrontends](https://alexocallaghan.com/upgrading-react-with-microfrontends)

Summary:
This article describes a strategy for incrementally upgrading React versions in a micro-frontend architecture. By introducing a "bridge" component (using @module-federation/bridge-react), teams can render micro-frontends in separate React trees, allowing individual upgrades without affecting the shell or other micro-frontends. The approach maintains compatibility and enables gradual migration to newer React versions.

Key takeaways:
- Micro-frontends can be upgraded independently by rendering them in isolated React trees via a bridge component.
- The @module-federation/bridge-react package facilitates this separation.
- Compatibility is maintained by checking for a BRIDGE export and adapting loading logic.
- Once all micro-frontends are bridged, the shell can be upgraded safely.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
