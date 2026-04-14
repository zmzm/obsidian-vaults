---
type: twir-item
issue: 274
item: 4
item_type: item
date: 2026-03-25
source: https://aurorascharff.no/posts/implementing-nextjs-16-use-cache-with-next-intl-internationalization/
tags:
  - "Nextjs"
  - "16"
  - "ServerComponents"
status: auto
---

[[2026-03-25-TWIR-274|Index]]

# Item 4: Implementing Next.js 16 'use cache' with next-intl Internationalization

Source: [https://aurorascharff.no/posts/implementing-nextjs-16-use-cache-with-next-intl-internationalization/](https://aurorascharff.no/posts/implementing-nextjs-16-use-cache-with-next-intl-internationalization/)

Summary:
Next.js 16’s 'use cache' directive for React Server Components doesn’t work seamlessly with next-intl due to its reliance on request-time headers. The upcoming `next/root-params` API will resolve this, but until then, developers must use workarounds involving manual locale prop passing and static rendering setup.

Key takeaways:
- 'use cache' requires components to avoid request-time APIs like headers(), which next-intl uses for locale detection.
- Workaround: Use `generateStaticParams` and `setRequestLocale` to enable static rendering and pass locale as a prop for cached components.
- The future `next/root-params` API will allow deep param access without prop drilling or dynamic rendering.
- For now, mixing 'use cache' and next-intl requires careful setup to avoid runtime errors.

Recommendation: Read fully

Related notes: [[Server Components]]
