---
type: twir-item
issue: 271
item: 8
item_type: item
date: 2026-03-04
source: https://github.com/vercel/next.js/issues/85470
tags:
  - "Nextjs"
  - "15"
  - "16"
status: auto
quality: keep
---

[[2026-03-04-TWIR-271|Index]]

# Item 8: Next.js issue - Server requests and latency increased after upgrading from Next.js 15 to 16

Source: [https://github.com/vercel/next.js/issues/85470](https://github.com/vercel/next.js/issues/85470)

Summary:
A user reports that upgrading from Next.js 15 to 16 resulted in a doubling of server requests and increased latency, leading to higher server costs. The issue is documented with environment details and a reproduction link, seeking to understand and resolve the performance regression.

Key takeaways:
- Next.js 16 may introduce changes that increase server load and latency compared to v15.
- Performance regressions can have significant cost implications for self-hosted deployments.
- Issue includes reproducible example and detailed environment info for maintainers.

Recommendation:
Summary sufficient (read issue if affected by or investigating Next.js 16 performance)

Why it matters:
read issue if affected by or investigating Next.js 16 performance

Content:
# Server requests and latency increased after upgrading from Next.js 15 to 16 · Issue #85470 · vercel/next.js · GitHub

### Link to the code that reproduces this issue

<https://github.com/carlos-dubon/next-16>

### To Reproduce

Upgrade to Next.js version 16

### Current vs. Expected behavior

After upgrading from Next.js 15 to Next.js 16, I noticed that the number of requests effectively doubled. This has resulted in increased server strain and higher response latency. It also seems to require more resources and therefore higher server costs $$$ (good for cloud services I guess?) compared to v15.

Server request patterns and performance should remain consistent (or improve) after upgrading.

### Provide environment information

```
Operating System:
  Platform: darwin
  Arch: arm64
  Version: Darwin Kernel Version 25.0.0: Wed Sep 17 21:41:45 PDT 2025; root:xnu-12377.1.9~141/RELEASE_ARM64_T6000
  Available memory (MB): 65536
  Available CPU cores: 10
Binaries:
  Node: 24.10.0
  npm: 11.6.1
  Yarn: 1.22.22
  pnpm: N/A
Relevant Packages:
  next: 15.5.5 // An outdated version detected (latest is 16.0.0), upgrade is highly recommended!
  eslint-config-next: N/A
  react: 19.1.1
  react-dom: 19.1.1
  typescript: 5.9.3
Next.js Config:
  output: N/A
```

### Which area(s) are affected? (Select all that apply)

Performance

### Which stage(s) are affected? (Select all that apply)

Other (Deployed)

### Additional context

The screenshot shows the ops/s after deploying v16 around 3:30 PM, I then proceeded to revert back my changes:

[![Image](https://private-user-images.githubusercontent.com/69093659/506700712-4f821069-a8f1-4226-a8cd-10a37bc98093.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYzMjk1NTgsIm5iZiI6MTc3NjMyOTI1OCwicGF0aCI6Ii82OTA5MzY1OS81MDY3MDA3MTItNGY4MjEwNjktYThmMS00MjI2LWE4Y2QtMTBhMzdiYzk4MDkzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDE2VDA4NDczOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE5MDNkYTIwMDBiNDQwN2I2NGJkYjljNGNjY2E4NjJlY2NmYWYwOTNiNWIyZWI4NzM3OTZjYzYzZjA3YjNhMmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.QabWslYyeFg9DVuDPWSy-N8ePbEAnD7aCgalfQPtyS8)](https://private-user-images.githubusercontent.com/69093659/506700712-4f821069-a8f1-4226-a8cd-10a37bc98093.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NzYzMjk1NTgsIm5iZiI6MTc3NjMyOTI1OCwicGF0aCI6Ii82OTA5MzY1OS81MDY3MDA3MTItNGY4MjEwNjktYThmMS00MjI2LWE4Y2QtMTBhMzdiYzk4MDkzLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA0MTYlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNDE2VDA4NDczOFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWE5MDNkYTIwMDBiNDQwN2I2NGJkYjljNGNjY2E4NjJlY2NmYWYwOTNiNWIyZWI4NzM3OTZjYzYzZjA3YjNhMmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRnBuZyJ9.QabWslYyeFg9DVuDPWSy-N8ePbEAnD7aCgalfQPtyS8)

I am self-hosting Next.js, and upgrading will most likely increase our cloud bill $$$.
