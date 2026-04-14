---
type: twir-item
issue: 267
item: 6
item_type: item
date: 2026-02-04
source: https://albertsikkema.com/ai/development/tools/reverse-engineering/2026/01/23/reverse-engineering-figma-make-files.html
tags:
  - "Reverse-Engineering"
status: auto
---

[[2026-02-04-TWIR-267|Index]]

# Item 6: Reverse-Engineering Figma Make: Extracting React Apps from Binary Files

Source: [https://albertsikkema.com/ai/development/tools/reverse-engineering/2026/01/23/reverse-engineering-figma-make-files.html](https://albertsikkema.com/ai/development/tools/reverse-engineering/2026/01/23/reverse-engineering-figma-make-files.html)

Summary:
A developer reverse-engineers Figma Make's .make files to extract embedded React applications, revealing that these files are ZIP archives containing binary-encoded source code. The process involves decompressing two chunks (deflate and Zstandard), decoding Figma's Kiwi schema, and reconstructing a working React app by fixing imports, assets, and build configs. The article provides practical tips for binary analysis and automation scripts for extraction.

Key takeaways:
- Figma Make .make files are ZIP archives with a custom binary format containing React source code.
- Extraction requires decompressing, schema decoding, and post-processing for imports and assets.
- Automation scripts can fully reconstruct a working React app from a .make file.
- Useful for developers needing to recover source from proprietary design tools.

Recommendation: Read fully (read fully if interested in reverse engineering or Figma Make internals)
