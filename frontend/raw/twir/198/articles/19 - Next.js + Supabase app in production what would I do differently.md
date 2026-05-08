---
type: twir-item
issue: 198
item: 19
item_type: item
date: 2024-08-28
source: https://catjam.fi/articles/next-supabase-what-do-differently
tags:
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2024-08-28-TWIR-198|Index]]

# Item 19: Next.js + Supabase app in production: what would I do differently

Source: [https://catjam.fi/articles/next-supabase-what-do-differently](https://catjam.fi/articles/next-supabase-what-do-differently)

Summary:
A retrospective on building a mid-sized Next.js + Supabase app, sharing lessons learned about data modeling, server components, server actions, testing, and database practices. The author recommends using zod for schemas, favoring server components/actions for data operations, creating utility wrappers, and being cautious with mocking and row-level security.

Key takeaways:
- Use zod schemas for data validation and type inference.
- Prefer server components/actions for colocated, secure data fetching/mutation.
- Create HOFs for route/page/server action logic (auth, validation, error handling).
- Avoid mocking Supabase in tests; run E2E tests on built apps.
- Design database keys and RLS for future scalability and performance.

Recommendation:
Read fully

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml

Related notes: [[Server Components]]
