---
type: twir-item
issue: 266
item: 16
item_type: item
date: 2026-01-28
source: https://vercel.com/changelog/ai-code-elements
tags:
  - "IDEs"
status: auto
quality: keep
---

[[2026-01-28-TWIR-266|Index]]

# Item 16: AI Code Elements - Vercel components to build the next generation of IDEs

Source: [https://vercel.com/changelog/ai-code-elements](https://vercel.com/changelog/ai-code-elements)

Summary:
Vercel introduces a suite of composable UI components (AI Code Elements) for building modern IDEs, coding apps, and agent interfaces. Components include agent configuration, code blocks, file trees, terminals, test results, and more, with a focus on developer experience and extensibility. Each component can be added individually via CLI.

Key takeaways:
- Modular components for building IDE-like UIs, including code, test, and agent interfaces.
- Designed for extensibility and integration with AI SDKs and coding agents.
- Includes advanced features like streaming, collapsible containers, and schema visualization.
- Easy installation via CLI; detailed documentation available.

Recommendation:
Read fully (read fully if building developer tools, IDEs, or AI coding interfaces)

Why it matters:
read fully if building developer tools, IDEs, or AI coding interfaces

Content:
# AI Code Elements

Today we're releasing a brand new set of components designed to help you build the next generation of IDEs, coding apps and background agents.

A composable component for displaying an AI SDK [ToolLoopAgent](https://ai-sdk.dev/docs/agents/overview) configuration with model, instructions, tools, and output schema.

```
1

npx ai-elements add agent
```

Building on what we've learned from [Streamdown](https://streamdown.ai/), we massively improved the code block component with support for a header, icon, filename, multiple languages and a more performant renderer.

```
1

npx ai-elements add code-block
```

The Commit component displays commit details including hash, message, author, timestamp, and changed files.

```
1

npx ai-elements add commit
```

The EnvironmentVariables component displays environment variables with value masking, visibility toggle, and copy functionality.

```
1

npx ai-elements add environment-variables
```

The FileTree component displays a hierarchical file system structure with expandable folders and file selection.

```
1

npx ai-elements add file-tree
```

The PackageInfo component displays package dependency information including version changes and change type badges.

```
1

npx ai-elements add package-info
```

The Sandbox component provides a structured way to display AI-generated code alongside its execution output in chat conversations. It features a collapsible container with status indicators and tabbed navigation between code and output views.

```
1

npx ai-elements add sandbox
```

The SchemaDisplay component visualizes REST API endpoints with HTTP methods, paths, parameters, and request/response schemas.

```
1

npx ai-elements add schema-display
```

The Snippet component provides a lightweight way to display terminal commands and short code snippets with copy functionality. Built on top of shadcn/ui InputGroup, it's designed for brief code references in text.

```
1

npx ai-elements add snippet
```

The StackTrace component displays formatted JavaScript/Node.js error stack traces with clickable file paths, internal frame dimming, and collapsible content.

```
1

npx ai-elements add stack-trace
```

The Terminal component displays console output with ANSI color support, streaming indicators, and auto-scroll functionality.

```
1

npx ai-elements add terminal
```

The TestResults component displays test suite results (like Vitest) including summary statistics, progress, individual tests, and error details.

```
1

npx ai-elements add test-results
```

Not code related, but since attachment were being used in Message, PromptInput and more, we broke it out into its own component - a flexible, composable attachment component for displaying files, images, videos, audio, and source documents.

```
1

npx ai-elements add attachments
```
