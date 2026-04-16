---
type: twir-item
issue: 267
item: 9
item_type: item
date: 2026-02-04
source: https://alexocallaghan.com/react-design-system-library-mcp
tags:
  - "MCP"
status: auto
quality: keep
---

[[2026-02-04-TWIR-267|Index]]

# Item 9: React design system library MCP

Source: [https://alexocallaghan.com/react-design-system-library-mcp](https://alexocallaghan.com/react-design-system-library-mcp)

Summary:
Mintel describes integrating Storybook's experimental MCP (Model Context Protocol) addon with their internal React design system library, enabling AI agents to query component documentation programmatically. The setup involves Storybook 10, MCP server configuration, and a CLI for exposing component manifests to other teams. This facilitates AI-assisted code migration and design system adoption across projects.

Key takeaways:
- Storybook's MCP addon exposes structured component documentation for AI agents and developer tools.
- The MCP server can be run locally or per-project, making design system metadata widely accessible.
- Teams can automate migration and code review tasks by querying the MCP server for component usage and documentation.
- The approach streamlines design system adoption and supports AI-driven development workflows.

Recommendation:
Summary sufficient

Content:
# React design system library MCP

At Mintel we maintain our own internal React design system component library. Working with our product design team we embed our design system standards into component implementations, and document them using [Storybook](https://storybook.js.org/).

With increased adoption of AI agents in our development workflows, we wanted to explore how we could expose our design system documentation by providing a local MCP CLI with our design system npm package.

The Storybook team are in early development of [@storybook/addon-mcp](https://storybook.js.org/addons/@storybook/addon-mcp) which exposes Storybook documentation via an MCP (Model Context Protocol) server. This allows AI agents to query the component library documentation in a structured way, as well as offering tools to aid generating storybook stories.

We upgraded to Storybook 10 and set-up the addon configuration in `.storybook/main.ts`:

```
const config: StorybookConfig = {
  addons: ["@storybook/addon-mcp"],
  features: {
    experimentalComponentsManifest: true,
  },
};
```

Both Storybook 10 and React are required for generating component manfiests, which exposes more details about each component including the props and API documentation.

The addon starts up the MCP server when Storybook is run locally, and we can access the server at `http://localhost:6006/mcp`.

```
{
  "mcpServers": {
    "storybook-mcp": {
      "url": "http://localhost:6006/mcp",
      "type": "http"
    }
  }
}
```

The MCP server works by generating files in `manifests` directory when the Storybook is built. These files contain the component metadata and documentation in a structured format.

The addon is useful for developers working on the design system itself, but we wanted to make the MCP server available to other development teams using the design system.

To do this we hooked into the underlying `@storybook/mcp` package to add a CLI to the library to allow starting the MCP server in stdio mode. Other teams can then run the latest version of the design system library MCP server with a single command: `pnpm dlx <library-name>@latest`.

We extended our library build process to also build the Storybook, and copy the generated manifests to the published package.

```
# Build the storybook
pnpm build-storybook
# Copy manifest files into package dist
mkdir -p ./dist/manifests
cp -r ./storybook-static/manifests/ ./dist/manifests/
# Build the library
pnpm vite build
```

We also added a CLI entry point to the package to start the MCP server in stdio mode.

```
// package.json
{
  "bin": "./dist/mcp.js"
}
```

```
#!/usr/bin/env node
 
import { McpServer } from "tmcp";
import { ValibotJsonSchemaAdapter } from "@tmcp/adapter-valibot";
import { StdioTransport } from "@tmcp/transport-stdio";
import {
  type StorybookContext,
  addListAllDocumentationTool,
  addGetDocumentationTool,
} from "@storybook/mcp";
import fs from "node:fs/promises";
import pkgJson from "./package.json";
 
const adapter = new ValibotJsonSchemaAdapter();
const server = new McpServer(
  {
    name: pkgJson.name,
    version: pkgJson.version,
    description: pkgJson.description,
  },
  {
    adapter,
    capabilities: {
      tools: { listChanged: true },
    },
    instructions:
      "You can use this MCP server to access Mintel Design System documentation, with component API docs for the React component library.",
  }
).withContext<StorybookContext>();
 
addListAllDocumentationTool(server).then(() => {
  addGetDocumentationTool(server).then(() => {
    const transport = new StdioTransport(server);
 
    transport.listen({
      format: "markdown",
      manifestProvider: async (_request, path) =>
        fs.readFile(`${__dirname}/${path}`, "utf-8"),
    });
  });
});
```

Teams can now set up the MCP server to run locally by configuring IDEs like Cursor:

```
{
  "mcpServers": {
    "mintel-design-system": {
      "command": "pnpm",
      "args": ["dlx", "<package-name>@latest"]
    }
  }
}
```

It can also be configured to run per-project, using the specific version of the design system library used in the project:

```
{
  "mcpServers": {
    "mintel-design-system": {
      "command": "pnpm",
      "args": ["exec", "<package-name>"]
    }
  }
}
```

We're still figuring out the best ways to leverage the MCP server, but it's already proving useful with prompts like:

> Evaluate if any components in this codebase can be swapped for Mintel Design System components

> Create a plan for migrating to the new Mintel Design System Button component

> Implement a filterable list of content using Mintel Design System components
