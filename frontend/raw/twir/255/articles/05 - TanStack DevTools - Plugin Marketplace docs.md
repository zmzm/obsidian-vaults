---
type: twir-item
issue: 255
item: 5
item_type: item
date: 2025-10-22
source: https://tanstack.com/devtools/latest/docs/third-party-plugins
tags:
  - "TanStack"
  - "DevTools"
status: auto
quality: keep
---

[[2025-10-22-TWIR-255|Index]]

# Item 5: TanStack DevTools - Plugin Marketplace docs

Source: [https://tanstack.com/devtools/latest/docs/third-party-plugins](https://tanstack.com/devtools/latest/docs/third-party-plugins)

Summary:
TanStack DevTools now supports a plugin marketplace for third-party devtools, including React plugins. Developers can submit plugins by adding metadata to a registry file, specifying package details, dependencies, and framework support. The documentation provides a clear structure for plugin submission and encourages contributions across multiple frameworks.

Key takeaways:
- Plugin marketplace enables community-driven devtools, including for React.
- Submission involves a structured metadata object with package info, dependencies, and optional documentation.
- Multiple plugins for different frameworks can be submitted.
- Encourages extensibility and ecosystem growth around TanStack DevTools.

Recommendation:
Read fully (read fully if building or submitting a plugin)

Why it matters:
read fully if building or submitting a plugin

Content:
# Third-party Plugins

```
'@tanstack/react-pacer-devtools': {
  packageName: '@tanstack/react-pacer-devtools',
  title: 'Pacer Devtools',
  description: 'Monitor and debug your Pacer animations and transitions',
  requires: {
    packageName: '@tanstack/react-pacer',
    minVersion: '0.16.4',
  },
  author: 'TanStack',
  framework: 'react',
  tags: ['TanStack'],
},
'@tanstack/solid-pacer-devtools': {
  packageName: '@tanstack/solid-pacer-devtools',
  title: 'Pacer Devtools',
  description: 'Monitor and debug your Pacer animations and transitions',
  requires: {
    packageName: '@tanstack/solid-pacer',
    minVersion: '0.14.4',
  },
  author: 'TanStack',
  framework: 'solid',
  tags: ['TanStack'],
},
```

```
'@tanstack/react-pacer-devtools': {
  packageName: '@tanstack/react-pacer-devtools',
  title: 'Pacer Devtools',
  description: 'Monitor and debug your Pacer animations and transitions',
  requires: {
    packageName: '@tanstack/react-pacer',
    minVersion: '0.16.4',
  },
  author: 'TanStack',
  framework: 'react',
  tags: ['TanStack'],
},
'@tanstack/solid-pacer-devtools': {
  packageName: '@tanstack/solid-pacer-devtools',
  title: 'Pacer Devtools',
  description: 'Monitor and debug your Pacer animations and transitions',
  requires: {
    packageName: '@tanstack/solid-pacer',
    minVersion: '0.14.4',
  },
  author: 'TanStack',
  framework: 'solid',
  tags: ['TanStack'],
},
```
