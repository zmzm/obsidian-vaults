---
type: twir-item
issue: 286
item: 6
item_type: item
date: 2026-06-17
source: https://github.com/whatwg/html/issues/12591
tags:
  - "HTML"
status: auto
quality: keep
---

[[2026-06-17-TWIR-286|Index]]

# Item 6: HTML proposal - Localized time formatting without JavaScript

Source: [https://github.com/whatwg/html/issues/12591](https://github.com/whatwg/html/issues/12591)

Summary:
A proposal to extend the HTML <time> element to support localized, absolute date/time formatting natively, without JavaScript. The approach introduces a format attribute and several additional attributes to control formatting, timezone, and locale, with rendering handled via a UA shadow root or CSS content. The goal is to enable correct, cacheable, and accessible time displays in SSR/static HTML.

Key takeaways:
- Would allow server-rendered HTML to display user-localized times without JS.
- Uses new attributes on <time> for formatting, locale, and timezone control.
- Rendering handled in a way that avoids DOM content replacement issues.
- Proposal aims to match Intl.DateTimeFormat’s capabilities for absolute times.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
