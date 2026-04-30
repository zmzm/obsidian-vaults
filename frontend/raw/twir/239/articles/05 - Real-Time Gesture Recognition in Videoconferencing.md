---
type: twir-item
issue: 239
item: 6
item_type: item
date: 2025-06-18
source: https://blog.swmansion.com/real-time-gesture-recognition-in-videoconferencing-4711855a1a53
tags:
  - "Real-Time"
status: auto
quality: keep
---

[[2025-06-18-TWIR-239|Index]]

# Item 6: Real-Time Gesture Recognition in Videoconferencing

Source: [https://blog.swmansion.com/real-time-gesture-recognition-in-videoconferencing-4711855a1a53](https://blog.swmansion.com/real-time-gesture-recognition-in-videoconferencing-4711855a1a53)

Summary:
This article details the implementation of real-time hand gesture recognition in a React-based videoconferencing app. It explains the challenges of combining computer vision, low-latency streaming, and real-time video compositing in the browser. The solution leverages MediaPipe for gesture detection, Smelter for video effects, and Fishjam for WebRTC communication, with performance optimizations via Web Workers and WASM.

Key takeaways:
- Real-time gesture recognition in the browser is resource-intensive and requires careful use of browser APIs (Web Workers, WebRTC, WebGL/WebGPU).
- MediaPipe is used for hand landmark detection, with processing offloaded to a Web Worker to avoid blocking the main thread.
- Smelter (WASM-based) and Fishjam simplify video compositing and real-time communication, respectively.
- The approach demonstrates how React can orchestrate complex, AI-powered video features in modern web apps.

Recommendation:
Summary sufficient

Content:
Content not available.

Notes:
Content extraction failed: Python clipper failed: Missing Python deps: No module named 'lxml_html_clean'. Install deps: pip3 install requests readability-lxml markdownify beautifulsoup4 lxml
