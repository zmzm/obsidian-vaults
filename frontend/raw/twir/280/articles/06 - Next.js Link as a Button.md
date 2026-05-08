---
type: twir-item
issue: 280
item: 6
item_type: item
date: 2026-05-06
source: https://kittygiraudel.com/2026/05/02/nextjs-link-as-a-button/
tags:
  - "Nextjs"
status: auto
quality: keep
---

[[2026-05-06-TWIR-280|Index]]

# Item 6: Next.js Link as a Button

Source: [https://kittygiraudel.com/2026/05/02/nextjs-link-as-a-button/](https://kittygiraudel.com/2026/05/02/nextjs-link-as-a-button/)

Summary:
This post explains how to combine Next.js's Link component with Ant Design's Button to achieve router navigation with correct semantics and accessibility. The recommended approach is to use Link with passHref and legacyBehavior to ensure the Button renders as an <a> element, not a <button>, and navigation is handled by Next.js routing.

Key takeaways:
- Passing href to Ant's Button triggers full page reload; using Link enables client-side navigation.
- Imperative routing renders a <button>, which is not semantically correct for navigation.
- Combining passHref and legacyBehavior props on Link allows Button to render as an <a> with router navigation.
- A reusable RouterButton component can encapsulate this pattern.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
