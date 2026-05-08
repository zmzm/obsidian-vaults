---
type: twir-item
issue: 203
item: 11
item_type: item
date: 2024-10-01
source: https://www.epicweb.dev/inverse-assertions
tags:
status: auto
quality: keep
---

[[2024-10-01-TWIR-203|Index]]

# Item 11: Inverse Assertions

Source: [https://www.epicweb.dev/inverse-assertions](https://www.epicweb.dev/inverse-assertions)

Summary:
The article discusses how to properly test that a side effect does not occur in React Testing Library. Instead of immediately asserting absence (which can cause false positives), it recommends using waitFor to assert the presence of the effect and expecting that assertion to fail (inverse assertion). This approach avoids race conditions and ensures reliable negative testing.

Key takeaways:
- Negative assertions can produce false positives if not timed correctly.
- Use waitFor to assert the unwanted effect, then expect it to fail (inverse assertion).
- Avoid sleep; prefer waitFor for all time-dependent side effects.
- Fine-tune waitFor with custom intervals and timeouts as needed.

Recommendation:
Read fully (read fully if you write tests with negative assertions)

Why it matters:
read fully if you write tests with negative assertions

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
