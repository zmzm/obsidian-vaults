---
type: twir-item
issue: 258
item: 2
item_type: item
date: 2025-11-12
source: https://vercel.com/changelog/support-for-tanstack-start
tags:
  - "TanStack"
  - "Nitro"
status: auto
quality: keep
---

[[2025-11-12-TWIR-258|Index]]

# Item 2: Vercel — Support for TanStack Start

Source: [https://vercel.com/changelog/support-for-tanstack-start](https://vercel.com/changelog/support-for-tanstack-start)

Summary:
Vercel now natively detects and supports TanStack Start applications, a full-stack framework based on TanStack Router for React and Solid. Developers can deploy TanStack Start apps on Vercel with minimal configuration, leveraging Vercel’s Fluid compute and Active CPU pricing for efficient scaling and cost control. Documentation and templates are available for quick setup and deployment.

Key takeaways:
- First-class Vercel support for TanStack Start, enabling seamless deployment and scaling.
- Uses Fluid compute with usage-based pricing.
- Simple integration via Vite plugin and nitro().
- Official docs and starter templates provided.

Recommendation:
Summary sufficient

Content:
# Support for TanStack Start

Vercel detects and supports TanStack Start applications, a full-stack framework powered by TanStack Router for React and Solid.

[Create a new TanStack Start app](https://vercel.com/templates/starter/tanstack-start-on-vercel) or add nitro() to vite.config.ts in your existing application to easily deploy your projects:

```
1

import { tanstackStart } from '@tanstack/react-start/plugin/vite'

2

import { defineConfig } from 'vite'

3

import viteReact from '@vitejs/plugin-react'

4

import { nitro } from 'nitro/vite'

6

export default defineConfig({
```

TanStack Start apps on Vercel use [Fluid compute](https://vercel.com/fluid) with [Active CPU pricing](/blog/introducing-active-cpu-pricing-for-fluid-compute) by default. This means your TanStack Start app will automatically scale up and down based on traffic, and you only pay for what you use, not for idle function time.

Visit the [TanStack Start on Vercel documentation](https://vercel.com/docs/frameworks/full-stack/tanstack-start) to learn more
