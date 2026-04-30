---
type: twir-item
issue: 216
item: 3
item_type: item
date: 2025-01-08
source: https://slack.engineering/automated-accessibility-testing-at-slack/
tags:
status: auto
quality: keep
---

[[2025-01-08-TWIR-216|Index]]

# Item 3: Automated Accessibility Testing at Slack

Source: [https://slack.engineering/automated-accessibility-testing-at-slack/](https://slack.engineering/automated-accessibility-testing-at-slack/)

Summary:
Slack shares their journey integrating automated accessibility testing into their development workflow, focusing on the use of Axe with Playwright for E2E tests. They discuss challenges embedding accessibility checks into React Testing Library and Jest, and how Playwright’s flexibility allowed for better integration. The article details customizations for filtering violations, managing exclusions, and leveraging Playwright fixtures to streamline accessibility checks and reporting.

Key takeaways:
- Automated accessibility testing is a supplement, not a replacement, for manual and user-involved testing.
- Embedding Axe in Playwright proved more practical than in Jest/RTL due to technical constraints.
- Custom filtering and exclusion logic are necessary to manage false positives and known issues.
- Playwright’s fixture system enables reusable, consistent accessibility checks across tests.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
