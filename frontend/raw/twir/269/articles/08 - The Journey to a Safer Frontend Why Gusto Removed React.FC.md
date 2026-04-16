---
type: twir-item
issue: 269
item: 8
item_type: item
date: 2026-02-18
source: https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4
tags:
  - "ReactFC"
status: auto
quality: keep
---

[[2026-02-18-TWIR-269|Index]]

# Item 8: The Journey to a Safer Frontend: Why Gusto Removed React.FC

Source: [https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4](https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4)

Summary:
Gusto's engineering team removed the use of React.FC from their codebase after discovering that it masked TypeScript errors and reduced type safety. By switching to explicit prop types and return values, they improved type checking, uncovered hidden bugs, and standardized component definitions. The migration was automated and enforced with linting to prevent regressions.

Key takeaways:
- React.FC can hide unused props and allow invalid default values, undermining TypeScript's safety guarantees.
- Migrating to explicit prop typing and return types surfaces real issues and improves code quality.
- The change was implemented at scale with automated scripts and enforced via lint rules.
- The process led to both technical and cultural improvements in the codebase.

Recommendation:
Summary sufficient (read the full post if planning a similar migration or interested in TypeScript/React best practices)

Why it matters:
read the full post if planning a similar migration or interested in TypeScript/React best practices

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: 403 Client Error: Forbidden for url: https://engineering.gusto.com/the-journey-to-a-safer-frontend-why-we-removed-react-fc-095ff0b3e2e4. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
