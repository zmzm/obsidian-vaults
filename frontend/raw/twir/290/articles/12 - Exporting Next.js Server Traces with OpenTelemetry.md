---
type: twir-item
issue: 290
item: 12
item_type: item
date: 2026-07-15
source: https://blog.sentry.io/nextjs-export-traces-opentelemetry/
tags:
  - "Nextjs"
  - "OpenTelemetry"
status: auto
quality: keep
---

[[2026-07-15-TWIR-290|Index]]

# Item 12: Exporting Next.js Server Traces with OpenTelemetry

Source: [https://blog.sentry.io/nextjs-export-traces-opentelemetry/](https://blog.sentry.io/nextjs-export-traces-opentelemetry/)

Summary:
Next.js supports server-side tracing out of the box, and with @vercel/otel, traces can be exported to any OpenTelemetry-compatible backend, such as Sentry. The article explains how to configure tracing, add custom spans for business logic, and the pros and cons of using OTLP export versus the Sentry SDK.

Key takeaways:
- Next.js emits traces for server-side operations by default.
- @vercel/otel simplifies exporting traces to OpenTelemetry backends.
- Custom spans can be added for detailed performance analysis (Node runtime only).
- Consider Sentry SDK for full-featured tracing, including browser-side data.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
