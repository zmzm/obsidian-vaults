---
id: common/serena/tools
name: common/serena/tools
kind: reference
domain: common
topics: [serena, tools]
priority: medium
status: stable
canonical: false
updated: 2026-04-16
---

# Serena Tools Reference

## When to use

Use this document when you need to understand which Serena tool to use for a specific task.

## Discovery Tools

### `get_symbols_overview`

Get high-level view of file's symbols (classes, functions, exports).

```
get_symbols_overview(relative_path="path/to/file.ts")
get_symbols_overview(relative_path="path/to/file.ts", depth=1)  # Include children
```

**Use when**: Starting to explore a file, understanding structure before reading.

### `find_symbol`

Find symbols by name path pattern.

```
find_symbol(name_path_pattern="UserService")           # Find class
find_symbol(name_path_pattern="UserService/create")    # Find method
find_symbol(name_path_pattern="create", depth=0)       # All symbols named "create"
find_symbol(name_path_pattern="UserService", include_body=True)  # Include source code
find_symbol(name_path_pattern="get", substring_matching=True)    # Match "getValue", "getData"
```

**Name path patterns**:

- `functionName` - Simple name, matches anywhere
- `Class/method` - Relative path, matches suffix
- `/Class/method` - Absolute path within file

**Use when**: Locating specific symbol by name.

### `find_referencing_symbols`

Find all usages of a symbol across codebase.

```
find_referencing_symbols(name_path="create", relative_path="users.service.ts")
```

**Use when**: Understanding impact before changes, finding all callers.

### `search_for_pattern`

Regex search across files when symbol name unknown.

```
search_for_pattern(
  substring_pattern="TODO|FIXME",
  relative_path="apps/backend/",
  restrict_search_to_code_files=True
)
```

**Use when**: Symbol name unknown, searching non-code content.

## Reading Tools

### `read_file`

Read entire file or specific lines.

```
read_file(relative_path="file.ts")
read_file(relative_path="file.ts", start_line=10, end_line=50)
```

**Use when**: Need entire file or non-code files.

### `find_symbol` with `include_body=True`

Read specific function/class body only.

```
find_symbol(name_path_pattern="UserService/create", include_body=True)
```

**Use when**: Need specific function/method implementation (preferred over full file read).

## Editing Tools

### `replace_symbol_body`

Replace entire function/class/method.

```
replace_symbol_body(
  name_path="UserService/create",
  relative_path="users.service.ts",
  body="async create(dto: CreateUserDto): Promise<User> { ... }"
)
```

**Use when**: Rewriting entire function/method.

### `insert_after_symbol`

Add new code after a symbol.

```
insert_after_symbol(
  name_path="UserService/create",
  relative_path="users.service.ts",
  body="\n  async update(id: string, dto: UpdateUserDto): Promise<User> { ... }"
)
```

**Use when**: Adding new method to class, adding function to module.

### `insert_before_symbol`

Add code before a symbol.

```
insert_before_symbol(
  name_path="UserService",
  relative_path="users.service.ts",
  body="import { Logger } from '@nestjs/common';\n"
)
```

**Use when**: Adding imports, adding code at file beginning.

### `rename_symbol`

Rename symbol across entire codebase.

```
rename_symbol(
  name_path="oldFunctionName",
  relative_path="utils.ts",
  new_name="newFunctionName"
)
```

**Use when**: Renaming function/class/method everywhere.

### `replace_content`

Regex-based text replacement for small changes.

```
replace_content(
  relative_path="file.ts",
  needle="oldValue.*?endPattern",
  repl="newValue",
  mode="regex"
)
```

**Use when**: Changing few lines within large function (more efficient than replace_symbol_body).

## Tool Selection Quick Reference

| Need                   | Tool                                |
| ---------------------- | ----------------------------------- |
| See file structure     | `get_symbols_overview`              |
| Find symbol definition | `find_symbol`                       |
| Read function body     | `find_symbol` + `include_body=True` |
| Find all usages        | `find_referencing_symbols`          |
| Replace function       | `replace_symbol_body`               |
| Add method to class    | `insert_after_symbol`               |
| Add import             | `insert_before_symbol`              |
| Rename everywhere      | `rename_symbol`                     |
| Small line changes     | `replace_content`                   |

## Operating Discipline

- Start with `get_symbols_overview` before reading large code files.
- Use symbol paths such as `ClassName/methodName` for precise targeting.
- Check references before modifying symbols with cross-file impact.
- Prefer Serena over grep when you need semantic callers or definition-aware edits.
- Prefer grep or direct text tools when the change is trivial and symbol tooling adds unnecessary overhead.
