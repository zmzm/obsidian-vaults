---
type: twir-item
issue: 264
item: 4
item_type: item
date: 2026-01-14
source: https://www.tbeeren.com/post/experimenting-with-bun-from-idea-to-production-in-a-week
tags:
  - "Ant"
status: auto
quality: keep
---

[[2026-01-14-TWIR-264|Index]]

# Item 4: Experimenting with Bun: From Idea to Production in a Week

Source: [https://www.tbeeren.com/post/experimenting-with-bun-from-idea-to-production-in-a-week](https://www.tbeeren.com/post/experimenting-with-bun-from-idea-to-production-in-a-week)

Summary:
This post details an experiment migrating React SSR workloads from Node to Bun at scale, motivated by Node’s performance bottlenecks. The author benchmarks both runtimes in a real-world micro-frontend setup, finding that Bun significantly improves throughput, lowers latency, and enables faster pod scaling in Kubernetes. The write-up includes practical configuration tips for resource management and readiness probes.

Key takeaways:
- Bun outperforms Node for React SSR, with higher throughput and lower latency.
- Bun’s faster startup enables more responsive Kubernetes scaling during traffic spikes.
- Minimal code changes are needed to swap runtimes; most adjustments are around streaming APIs and deployment configs.
- The article provides concrete resource and probe configuration examples for production environments.

Recommendation:
Read fully (for anyone considering Bun for SSR or interested in React infrastructure performance)

Why it matters:
for anyone considering Bun for SSR or interested in React infrastructure performance

Content:
# Experimenting with Bun: From Idea to Production in a Week

Some week ago, I found myself having coffee at a conference with a few like-minded performance engineers. We seemed to have a lot in common — our love for coffee, geeky topics, and yes, an unhealthy obsession with stroopwafels. But beyond that, a shared frustration kept popping up: **server-side rendering

performance in Node.js**.

React SSR on Node felt heavy and blocking. Even on high-spec machines, the render loops would max out at **8–9 requests per second** — which is surprisingly low. It is a bottleneck we couldn’t easily sidestep, and it sparked a question I couldn’t accept: *can we make this faster? Can we push beyond Node’s limits while keeping things stable for production?*

At the same time, I’d been following **Bun** closely. With its 1.3.0 release and the promise of better concurrency, faster startup, and lower overhead, I thought: maybe this is the perfect opportunity to experiment.   
  
The timing was perfect. We’d just finished modernising our frontend architecture at Bol with React Router, NX, GraphQL, URQL — all neatly lined up, all still powered by Node. It felt like the right moment to challenge the foundation.

So I did. And somehow, by Friday,

Bun was running in production

.

## Finding the Limits

At Bol, we run over 20 different micro frontends to render the full webshop. All React apps, each SSR’d on the server, each its own little environment and their own routes and pages. Node has been our reliable runtime for years, but the more our traffic grows, the more it also shows its limits.

Especially during high-traffic moments like **Christmas or Black Friday**, Node would behave stable under peaks, but it would translate into spinning up loads of pods. CPU usage would spike, latency would climb, and Kubernetes starts scaling like it’s trying to reach an all-time high on pod usage. It works, but not elegantly.

Scaling horizontally helped — but it felt like brute-forcing the problem with a lot of resources rather than solving the root cause. It felt quite horrible to accept the fact that we could only run up to 8/9 request per second before we had to scale again. A position that to me - and to most developers - should not feel comfortable.

That was the problem: we could handle it, but not efficiently. And efficiency matters when you’re running thousands of requests per second at scale.

## The new kid on the block

Around that time, Bun 1.3.0 was released and gained renewed attention. Earlier versions were promising but felt too experimental for production workloads. This release, however, introduced more stability, better compatibility, and improved performance characteristics.

Bun is built on top of a different JavaScript engine (JavaScriptCore), a thinner runtime, and significantly faster startup behaviour. On paper, it looked particularly well suited for SSR workloads that are CPU bound, allocation heavy and sensitive to event loop latency.

That made it worth testing seriously.

## The Experiment

Instead of rebuilding anything, the idea was to test **one thing only** — the runtime.

It was worth exploring, and the plan was straightforward: create a proof of concept that could run **both Node and Bun**. Easy to benchmark and easy to throw away. Same codebase, same environment, same load. That way, any difference in performance would be purely down to the runtime.

We set it up so that the app could run on either runtime through a simple ConfigMap switch. That meant within minutes we could swap from Node to Bun (and back again) without redeploying a new image.

All it took was one small tweak in `entry.server.tsx` — Bun’s streaming API is slightly different — but that was it. Within a day, both versions were live in the cluster. And honestly? That moment felt a little magical. Seeing the same app, same codebase, powered by two completely different runtimes — it just worked.

## Benchmarks, Coffee, and Dashboards

With both environments up and running — one powered by Node, the other by Bun — it was time to see what actually happened under pressure.

A few Locust workers spun up, a Grafana dashboard blinking on the second screen, and a mug of coffee that was guaranteed to go cold before the first round of tests finished.

The setup was simple: one pod and consistent traffic. Node handled it as expected — around **16 requests per second**, with an average latency of **~1100 milliseconds**. Stable, predictable, and already close to the ceiling we’d been seeing in production. Do keep in mind, this is when we push it to the limits. Something we would never do in production because we need the head-room to scale on time - due to cold starts.

When the same test ran on Bun, the difference was immediately visible in graphs. Latency dropped to around **800 milliseconds**, and throughput climbed to **23 requests per second**. CPU utilization stayed lower across the board, and the response times were smoother. Same app, same environment — the only change was the runtime.

The first thing to optimize was pod resources. Here’s what we used:

```
resources:
  requests:
    cpu: "900m"       
    memory: 3000Mi    
  limits:
    cpu: "8"          
    memory: 3000Mi
```

### **Why these values?**

The `requests` field tells Kubernetes “this is the expected baseline usage.” HPA calculates CPU utilization based on this. The `limits` allow Bun to temporarily use more CPU when handling heavy SSR loops, which is crucial for maintaining low latency during traffic spikes.

Setting a higher CPU limit, like `8`, does **not** mean the pod always consumes 8 cores or costs extra. The pod only uses what it actually needs. This means Bun can burst during heavy SSR requests without impacting cost or stability, while HPA still scales based on the `requests` baseline. Essentially, it gives the runtime headroom to handle spikes efficiently without over-provisioning permanently.

Encouraged by the first results, the tests got bigger. We wanted to test how this behaves on heavy - production like - load. So we ramped up, and began scaling horizontally. Node pods usually took **30–32 seconds** to become ready, meaning the HPA always lagged behind real traffic spikes. Bun changed that entirely: pods were ready in 7 **seconds**, allowing scaling to be aggressive and precise.

```
startupProbe:
  httpGet:
    path: /api/ready   
    port: 8080
  initialDelaySeconds: 3  
  periodSeconds: 1        
  failureThreshold: 10    
  successThreshold: 1       
  timeoutSeconds: 1
```

### **What does this do?**

The `startupProbe` ensures Kubernetes knows when a pod is fully initialized and able to serve traffic. Because Bun starts so quickly, we can poll often and aggressively. This is why HPA can scale pods almost instantly without overshooting traffic.

```
readinessProbe:
  httpGet:
    path: /api/health   
    port: 8080
  periodSeconds: 2        
  successThreshold: 1     
  timeoutSeconds: 3       
  failureThreshold: 6
```

### **Why this matters:**

The `readinessProbe` controls whether traffic is sent to a pod. With these settings, traffic won’t go to a pod too early, but won’t wait too long either. This keeps the system safe and responsive under bursts.

As the user count climbed past **400 simulated sessions**, the graphs told an even clearer story. Node reached **27 pods**, serving around **236 requests per second**, with latency varying between **1100–2000ms**. Bun hit **17 pods**, serving **259 requests per second**, with latency consistently between **750–900ms**.

Scaling was smoother thanks to the HPA configuration:

```
scaleUp:
  stabilizationWindowSeconds: 0      
  policies:
    - type: Percent
      value: 200                     
      periodSeconds: 10
    - type: Pods
      value: 4                        
      periodSeconds: 15
  selectPolicy: Max

scaleDown:
  stabilizationWindowSeconds: 30     
  policies:
    - type: Percent
      value: 50
      periodSeconds: 15
  selectPolicy: Max

metrics:
  - type: Resource
    resource:
      name: cpu
      target:
        type: Utilization
        averageUtilization: 80
```

### **Breaking it down:**

- `scaleUp` policies let the HPA react aggressively — pods come online immediately when traffic rises.
- `scaleDown` policies are gentler to prevent oscillation — pods aren’t killed too quickly.
- CPU utilization target of 80% means we prefer using a little more pods at higher utilization, taking advantage of Bun’s concurrency.

By the end of the tests, the graphs showed clean, stable lines across all metrics: throughput, latency, CPU, memory. The system was not only faster but also more efficient. The coffee had gone cold, but the conclusion was clear: runtime alone changed the game.

## Scaling Smarter, Not Harder

Once the burst tests were running, it became obvious that Bun didn’t just make individual pods faster — it fundamentally changed how scaling could be approached. The old rules didn’t apply anymore. HPA policies that felt aggressive for Node suddenly became reasonable. Pods could be spun up almost on-demand, with minimal risk of failing readiness checks.

This meant we could push harder on the CPU target and shorten stabilization windows. Normally, that would make clusters jitter, pods changing between ready and not ready, or HPA overshooting and wasting resources. But with Bun’s 7-second cold starts, scaling happened in near real time. Peaks were caught at the last moment, without over-provisioning or leaving capacity idle.

Tweaking the readiness and startup probes was just as important. We set the startup probe to hit `/api/ready` every second, with a low failure threshold — Bun started fast enough that pods were ready to serve traffic almost instantly. The readiness probe checked `/api/health` frequently enough to give the HPA confidence that newly started pods could handle requests instantly. The result was that the cluster didn’t just scale; it scaled intelligently.

The effect of these changes was dramatic during higher load tests. Instead of dozens of Node pods quietly throttling CPU and struggling under latency spikes, Bun handled similar or higher traffic with fewer pods and more consistent performance. Resources were used optimally, burst handling was precise, and the system reacted in ways Node simply couldn’t.

![Image](/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2F6wgfy9fj%2Fproduction%2Fdcb30068263407645d86ab6102a00d2befcd0ad3-1709x1075.png%3Fw%3D1709%26auto%3Dformat&w=3840&q=75)

## Going Live With Bun: Real Traffic, Real Data

This whole thing started on a Monday. A simple idea:

> **“What if we run our architecture on Bun and just… see what happens?”**

Four days later, we pushed it into production with real customer traffic — safely, of course, using Istio’s `mirrorTraffic` to duplicate traffic into a Bun deployment running next to Node. No risks for users, just a source of data for us to benchmark different runtimes.

We started with 10%, bumped to 50%, then to 100%. During each step, we tweaked CPU requests and limits on the fly to understand how far we could push Bun.

And pretty quickly, some patterns emerged. Good ones.

## Memory usage

The first graph that caught everyone’s attention was memory.

Our Node pods - running Express and React Router - always sit comfortably somewhere around 780–820 MiB. Then Bun came online, which showed quite interesting insights of running on half the memory usage of node.

> **Node:** ~807 MiB

> **Bun:** ~447 MiB

There are a few reasons why this difference might happen:

- Bun uses **JavaScriptCore**, which has a smaller base footprint than V8.
- JSC tends to be more compact with small, short-lived allocations — exactly what SSR does a lot of.
- Bun’s runtime is thinner; fewer layers, fewer abstractions = less overhead by default.

What the exact cause is, we don’t know yet. There are things we *haven’t* measured yet, like exact heap snapshots or GC micro-behavior, so we’re not pretending to know everything. But the numbers speak for themselves: same workload, same architecture, noticeably lower memory usage.

## Event-loop lag

This one wasn’t expected. Something we hoped for to see improvements, but were unsure about. We have had issues for a long time with the rendered or React. A blocking process which is heavily CPU bound. We see spikes on the event-loop lag, causing problems of reaching high throughputs.

Node usually sits around 10–14ms event loop lag during production load. Nothing problematic, but definitely present when you want to push CPU.

The big surprise: with Bun, that dropped to **~3ms**.

Lower lag directly affects SSR responsiveness: fewer stalls inside render loops and faster IO turnaround. That means less jitter in tail latency — which is where SSR pain usually shows up.

We have some idea why this happens:

- Bun still uses libuv, but with far less built-up machinery than Node.
- The surrounding hooks, timers, and scheduling layers are simply leaner.
- JSC tends to perform well with synchronous, string-heavy, repetitive patterns — which is what React Router SSR does.

It’s one of those differences that looks small in isolation but becomes significant when multiplied by hundreds of concurrent requests.

## Latency (p99)

Latency is the metric that really matters to us — it’s what the user feels when a page renders. Numbers alone don’t tell the full story, so we spent a lot of time digging into how the SSR pipelines behave on Node vs Bun.

With mirrored traffic in production, the 99th percentile looked like this:

- > **Node p99:** ~1.25s
- > **Bun p99:** ~999ms

On the surface, that’s a 200–300ms improvement — noticeable, but the real story lies in *why*.

React SSR isn’t just a synchronous render; it’s a loop of multiple phases: reconciliation, rendering, stringifying JSX, and sending chunks over the HTTP stream. On Node, each of these steps can stall the event loop slightly:

- **Reconciliation:** when React compares the current VDOM to the previous one, even small components can accumulate overhead.
- **JS string conversion:** rendering to HTML strings requires multiple allocations and temporary objects, which can trigger GC.
- **Express middleware layers:** each layer adds micro-delays. On Node, these small delays add up, especially under concurrent requests.

All these small delays are multiplied across multiple SSR requests. That’s why Node’s latency graph often has “micro-spikes” — short GC pauses, tiny stalls in the event loop, or jitter from request scheduling.

Bun changes a few of these dynamics, even if we don’t fully understand all of it yet:

- **JavaScriptCore’s GC** seems to handle short-lived SSR objects more efficiently, causing fewer micro-pauses.
- **Lower baseline event loop lag** means React’s render loops spend less time waiting to schedule timers or callbacks.
- **Simpler runtime hooks** reduce internal scheduling overhead compared to Node + V8.

The result: fewer spikes, smoother tail latency, and a flatter p99 curve. It’s consistent and predictable, which is critical for SSR where a single slow request can block the entire render stream.

We’re still investigating exactly how Bun achieves this. Profiling React’s SSR on both runtimes shows hints: Bun allocates fewer temporary objects, and the CPU time per render loop is slightly lower. But there are many unknowns — how GC behavior interacts with React’s stringification, how Bun handles buffering of HTTP streams under heavy concurrency, and what this means for rendering very large component trees.

What excites me most is the potential impact on **Web Vitals**. Faster, smoother SSR could improve LCP and reduce CLS on initial page load. Once we fully integrate Bun into production traffic, we’ll have real numbers to see whether these internal improvements translate to measurable improvements for users.

The key takeaway: latency isn’t just about the average — it’s about how consistent the rendering pipeline behaves under load. And on that front, Bun seems to give React SSR more breathing room.

## Cost Impact

The performance improvements will also benefit the cost/ budget spent. Under mirrored production traffic, Bun required roughly thirty percent fewer pods and way less memory to handle the same load. Without any runtime specific tuning, this resulted in an estimated reduction of approximately twenty two percent in monthly scalable infrastructure costs for this workload.

These numbers are conservative and based on baseline configuration. Further optimisation is expected to increase the savings.

## What We Still Do Not Know

Bun is a newer runtime and not all questions have been answered.

We have not yet fully profiled the application, or checked the garbage collection behaviour under complex render trees. Tooling for deep profiling is still less mature than in the Node ecosystem. Behaviour under different streaming patterns and larger component trees requires further validation.

These are important considerations before broader adoption.

## Closing Thoughts

This experiment was not about replacing Node everywhere. It was about understanding how much the runtime alone influences SSR behaviour.

Faster startup times, lower memory usage, reduced event loop lag, and smoother scaling fundamentally change how SSR systems behave under load. In this case, switching the runtime alone was enough to improve performance, stability, and cost efficiency without changing the application architecture.

That makes Bun a compelling option for SSR workloads and an area worth continued exploration. Let’s see what this will bring us, and Bol in 2026.
