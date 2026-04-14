---
title: "Accelerate Next.js in Kubernetes"
source: "https://blog.platformatic.dev/93-faster-nextjs-in-your-kubernetes"
author:
published: 2025-11-25
created: 2026-04-14
description: "Watt optimizes Next.js on Kubernetes for 93% faster latency and near-perfect reliability, overcoming scaling challenges."
tags:
  - "clippings"
---
![93% Faster Next.js in (your) Kubernetes](https://blog.platformatic.dev/_next/image?url=https%3A%2F%2Fcdn.hashnode.com%2Fres%2Fhashnode%2Fimage%2Fupload%2Fv1767810050890%2F4cbd0ac4-7f49-4910-a180-68139d6b5566.jpeg&w=3840&q=75)

[![Matteo Collina](https://cdn.hashnode.com/res/hashnode/image/upload/v1656492960212/pf_f_CpSA.jpeg?auto=compress,format&format=webp)

Matteo Collina

](https://hashnode.com/@matteocollina)

[Matteo Collina](https://hashnode.com/@matteocollina)

[Next.js](http://next.js/) has been an incredibly popular project since its launch in 2016, and for good reason: it brings a world of capabilities to developers out-of-the-box. But, for teams looking to run it at scale in their own environments, it can also bring a world of pain.

We'll start by examining the complications of running this powerful framework in your own environment, and get under the hood (and I mean, down to the kernel) about why they happen.

Then, we'll walk you through the approach we took with [Watt](https://github.com/platformatic/platformatic) to solve them, and what it means for you if you happen to run Next.js on any other Node.js CPU-bound workload on-prem.

(And if you're just here for the benchmarks, feel free to scroll past all the technical bits 🙂.)

### The Fundamental Problems of Scaling Next (and Node) in Kubernetes

If you're running Node.js at any modicum of scale, specifically in containers, you may know some version of this story:

Traffic spikes hit during peak hours, and suddenly, some pods are maxed out at 100% CPU while others sit at 30% utilization.

Requests start timing out. Your monitoring dashboard lights up red. Users see loading spinners instead of content, and your error rate climbs to 8%.

So you over-provision. You add 50% more pods than you need to handle the uneven load distribution. Your cloud bill grows, but at least *most* requests succeed.

Except now you're paying for infrastructure that sits idle most of the time, and during the next traffic surge, you're back to the same problem - just with more pods experiencing the same uneven distribution.

Meanwhile, your median latency hovers around 182ms. That doesn't sound terrible until you realize each page load makes multiple API calls. Three sequential calls at 180ms each mean users wait over half a second for basic interactions. In e-commerce, that's the difference between a sale and an abandoned cart. In SaaS, it's the difference between a delighted user and a churned customer.

This point I'm trying to (not so subtly) emphasize is that this isn't just a performance problem. It's a revenue problem. Each failed request during peak traffic is a lost transaction. Every 100ms of latency measurably reduces conversion rates. And all that over-provisioned infrastructure? That's profit margin burning in idle CPU cycles.

And yes, at the end of this, I'm going to tell you how Watt can fix it all, and show you some numbers to prove it. Strap in, it's time to go spelunking into the internals of Node.js and Linux.

### Under the Hood

Ok. Time to get into the technical details.

For over a decade, the Node.js community has relied on two main approaches for scaling applications across multiple CPU cores:

#### 1\. The cluster module (and PM2)

When Node.js introduced the `cluster` module in 2011, it seemed perfect: fork multiple worker processes, share a server port, and let the master process distribute connections using round-robin load balancing. Tools like [PM2](https://www.npmjs.com/package/pm2) made this even easier.

But there's a hidden cost. The `cluster` architecture requires the master process to act as an internal load balancer - accepting every connection and transferring it to workers via IPC (inter-process communication). This introduces approximately **30% overhead** as every request passes through this coordination layer.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1764177938543/d1040360-01d3-4dec-a77c-79e0f506b6b4.png)

#### 2\. Horizontal scaling with single-CPU pods

In Kubernetes environments, the conventional wisdom became: deploy single-CPU pods behind a load balancer. Simple, stateless, easy to scale. But this approach creates a critical problem for frameworks that can't implement early request rejection.

#### The Early Rejection Problem

Here's the issue: Once a request enters Node.js's event loop queue, it cannot be rejected until processing begins:

```typescript
Request → TCP Accept → Event Loop Queue → [Wait] → Process → 503 (Too Late)
                     ↑
                Cannot reject here
```

This causes requests to pile up during overload, consuming memory and increasing latency for everyone. An ideal server would reject new requests immediately with a 503 before accepting them, allowing load balancers to route traffic elsewhere. But Node.js's event loop architecture makes this remarkably difficult.

### Why Next.js Makes This Worse

Frameworks like Next.js that rely on React server-side rendering (SSR) fundamentally **cannot implement early 503 responses**. They need the full request context before they can even determine what to do:

1. **Request Context Required**: SSR needs headers, cookies, and query params before rendering
2. **Dynamic Route Matching**: Next.js must accept the connection to determine which page to execute
3. **Data Fetching Dependencies**: Server components require the request to be in-flight, parallelizing I/O but postponing the CPU-bound activity (learn more why this cause [Event Loop blocking](https://www.youtube.com/watch?v=81AqwvXqgG0&t=536s)).
4. **Middleware Execution**: Next.js middleware runs after request acceptance, not before

By the time Next.js knows it's overloaded, the request is already queued and consuming resources.

#### The Compounding Effect

When you combine this with traditional scaling approaches, the problems multiply:

- **With** `cluster` /PM2: Every request pays the ~30% IPC overhead, even when the server isn't overloaded.
- **With single-CPU pods**: Round-robin distribution creates isolated queues where load imbalances compound. One pod might be drowning while another sits idle, but they can't share work.

What we needed was a way to scale across multiple cores **without** the coordination overhead of `cluster`, while also enabling better statistical distribution of load than isolated single-CPU pods.

## How We Solved This (with Watt)

We built **Watt** as an "application server" for Node.js to fix these fundamental issues of scaling Node.js in containerized environments.

Here's what we achieved running Next.js with Watt on AWS EKS under sustained load of 1,000 requests per second:

| Metric | PM2 (Cluster) | Single-CPU Pods | Watt |
| --- | --- | --- | --- |
| **Median Latency** | 182ms | 155ms | **11.6ms** |
| **P95 Latency** | 1,260ms | 1,000ms | **235ms** |
| **Success Rate** | 91.9% | 93.7% | **99.8%** |
| **Throughput** | 910 req/s | 972 req/s | **997 req/s** |

That's **93.6% faster median latency** and **near-perfect reliability** compared to the standard approaches for scaling Node.js applications.

These results come from production-grade benchmarks on real Next.js applications running on Kubernetes, comparing three common deployment strategies with identical total CPU resources (6 CPUs each). All configurations were tested under the same sustained load pattern, and Watt consistently outperformed both traditional approaches.

### Under the Hood (again)

**Watt** leverages a feature of the Linux kernel that allows us to distribute connections across multiple Node.js processes with zero coordination overhead: SO\_REUSEPORT. This `listen()` option allows us to eliminate the ~30% performance tax that PM2 and the `cluster` module impose through IPC-based load balancing.

The core idea is elegantly simple: instead of having a master process coordinate workers, let the **Linux kernel** handle load distribution directly via SO\_REUSEPORT to run multiple Node.js applications with zero coordination overhead.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1763740899094/46d5e789-2397-4bbb-9054-9a2b3ef6c2cd.png)

So, for teams running Node with any sort of performance sensitivity, here's what that means for you:

##### 1\. Zero-Overhead Load Balancing

Each Watt worker accepts connections directly from the OS using `SO_REUSEPORT`. There's no master process, no IPC coordination, no serialization overhead. The kernel distributes incoming connections using an efficient hash-based algorithm, and workers handle them independently.

##### 2\. Process Orchestration

While workers run independently, Watt manages the process lifecycle:

- Automatic restart of crashed processes
- Graceful shutdown handling
- Health monitoring and metrics
- Coordinated deployments

##### 3\. Shared HTTP Cache

Watt includes a shared HTTP cache layer across workers, reducing redundant work and improving cache hit rates. See our post on [bringing HTTP caching to Node.js](https://blog.platformatic.dev/bringing-http-caching-to-nodejs) for details. (Oh, and for you all working in Next.js, [you can now do component caching inside Watt as well.](https://blog.platformatic.dev/watt-v318-unlocks-nextjs-16s-revolutionary-use-cache-directive-with-redisvalkey))

##### 4\. Automatic Health Restarts

Event loop or heap catastrophic failures trigger graceful worker restarts without pod termination, maintaining service availability. These checks are executed from the main thread without triggering the worker thread's event loop; we can perform them even if the application event loop is blocked.

##### How It Works

Watt runs multiple Node.js applications as separate threads within a single Node.js process. Each thread operates independently with its own event loop, but they all share the same listening socket using `SO_REUSEPORT`:

```js
server.listen({
  host: '127.0.0.1',
  port: 3000,
  reusePort: true
})
```

This single flag - `reusePort: true` - is what enables the kernel to distribute connections efficiently. But rather than managing this yourself, Watt handles the entire orchestration for you while adding process management, health monitoring, and caching on top.

The result? The same performance as manually using `SO_REUSEPORT`, but with all the operational features you'd expect from a production application server.

Now, I know we are already 'under the hood' of Watt, but let's get a bit closer to the kernel, shall we?

#### (Even Deeper) Under the Hood:: How SO\_REUSEPORT Works

The magic behind Watt's performance comes from a Linux kernel feature called `SO_REUSEPORT`, available since kernel 3.9 (April 2013). This socket option fundamentally changes how the operating system distributes incoming connections to processes.

![](https://cdn.hashnode.com/res/hashnode/image/upload/v1763740381613/f15d6ed7-5254-4caa-960d-9df2440c81d9.png)

### Kernel-Level Load Distribution

When you set the `reusePort: true` option on Node.js's HTTP server, it calls this under the hood:

```c
setsockopt(socket, SOL_SOCKET, SO_REUSEPORT, &opt, sizeof(opt));
```

This tells the Linux kernel to distribute incoming connections across all processes listening on the same port using a two-stage hash-based algorithm:

**Stage 1: Listen Socket Lookup**

- All processes using SO\_REUSEPORT on the same port are grouped together in a shared array structure
- The destination port determines which bucket in the kernel's LISTEN hash table to search

**Stage 2: Connection Distribution**

- For each incoming connection, the kernel calculates a hash from the 4-tuple:
	```c
	hash(source_ip, source_port, dest_ip, dest_port)
	```
- This hash selects which worker process receives the connection
- The worker accepts the connection directly - no coordination needed

**Key Properties:**

- **Connection affinity**: Same client IP:port always reaches the same worker
- **Even distribution**: Hash function provides balanced load across workers
- **Zero coordination**: No IPC, no shared state, no serialization
- **Deterministic**: Based purely on connection parameters, not current load

This is fundamentally different from PM2/cluster, where the master process must accept each connection and then forward it to a worker via Unix domain sockets - adding ~30% overhead.

For more technical details on SO\_REUSEPORT, see:

- [Cloudflare: The Sad State of Linux Socket Balancing](https://blog.cloudflare.com/the-sad-state-of-linux-socket-balancing/)
- [NGINX: Socket Sharding in NGINX 1.9.1](https://www.f5.com/company/blog/nginx/socket-sharding-nginx-release-1-9-1)

### Practical Applications: Two-Layer Architecture in Kubernetes

When you deploy Watt with multiple workers on a Kubernetes pod with multiple CPUs, you get a two-layer load balancing system (with two layers of resiliency):

**Layer 1: Kubernetes Service**

- Distributes new TCP connections across pod IPs
- Uses round-robin or other configured algorithms
- Example: 3 pods become 3 endpoints

**Layer 2: Watt and Worker Threads within each pod**

- Kernel distributes connections across workers in the same pod using Watt and SO\_REUSEPORT
- Hash-based selection ensures balanced distribution
- Example: Each pod has 2 Watt workers for a total of 6 total workers

This creates better statistical multiplexing (combining multiple signals or data streams to share a single resource) than the traditional approach of 6 single-CPU pods.

Deeper under the hood we go…

##### 1\. Independent Event Loops

Each worker has its own event loop on its own CPU core. When Worker 1 is busy processing a slow Next.js SSR request, Worker 2's event loop continues processing its connections independently. Variance in request processing times affects fewer connections.

##### 2\. Resource Sharing Within Pods

Workers in the same pod share:

- Kernel page cache (file system operations)
- Memory for binary code (lower memory footprint)
- Single network namespace (lower context switching)

##### 3\. Better Failure Characteristics

With Watt's orchestration:

- Single worker crash: Only 1/6 capacity lost temporarily
- Automatic restart without pod termination
- Health checks at worker level, not pod level
- Graceful failover for catastrophic failures

##### 4\. Statistical Load Distribution

Hash-based distribution at both layers provides better statistical properties than round-robin to isolated pods. Connections are more evenly distributed, and the two-layer approach reduces the impact of connection-level variance.

## Production Benchmarks: Next.js on AWS EKS

Ok. Now for the fun part. The part where I show you what all this means for your applications, with numbers. (And welcome, to those of you who scrolled here from the beginning of the article.)

To validate the theoretical and simulation results, we ran production-grade benchmarks using Next.js on AWS EKS (Elastic Kubernetes Service), i.e. testing a real-world framework that cannot implement early request rejection.

The tests compared three Kubernetes deployment strategies:

1. **Single-CPU pods** (6 replicas × 1000m CPU limit, 2GB RAM each = 6 total CPUs)
2. **PM2 multi-worker pods** (3 replicas × 2000m CPU limit with 2 PM2 workers, 4GB RAM each = 6 total CPUs)
3. **Watt multi-worker pods** (3 replicas × 2000m CPU limit with 2 Watt workers, 4GB RAM each = 6 total CPUs)

Given that Next.js Server-Side Rendering is CPU-bound, using 6 CPUs provides a like-for-like comparison.

**Infrastructure:**

- **EKS Cluster:** 3 nodes running m5.2xlarge instances (8 vCPUs, 32GB RAM each)
- **Load Testing:** c7gn.large instance (2 vCPUs, 4GB RAM, network-optimized)
- **Load Pattern:** k6 with constant arrival rate of 1,000 requests/second for 120 seconds
- **Virtual Users:** 1,000 pre-allocated VUs

The environment is totally ephemeral and created on-demand via a shell script and the aws CLI.

All configurations used identical total CPU resources (6 CPUs) for fair comparison. For testing, we used [Grafana's K6](https://k6.io/), configured as follows:

**k6 Load Test Configuration:**

```javascript
import http from 'k6/http';
import { check } from 'k6';

export const options = {
  scenarios: {
    constant_arrival_rate: {
      executor: 'constant-arrival-rate',
      duration: '120s',
      rate: 1000,
      timeUnit: '1s',
      preAllocatedVUs: 1000,
    },
  },
};

export default function () {
  const res = http.get(__ENV.TARGET, {
    timeout: "5s"
  });
  check(res, {
    'status is 200': (r) => r.status === 200,
  });
}
```

This configuration maintains a constant arrival rate of 1,000 requests/second for 120 seconds, with 1,000 pre-allocated virtual users and a 5-second timeout per request.

You can find the complete source code for these benchmarks at: [https://github.com/platformatic/k8s-watt-performance-demo](https://github.com/platformatic/k8s-watt-performance-demo).

#### Benchmark Results

| Configuration | Throughput | Success Rate | Median Latency | P95 Latency |
| --- | --- | --- | --- | --- |
| Single-CPU pods (6×1) | 972 req/s | 93.7% | 155 ms | 1,000 ms |
| PM2 (3×2 workers) | 910 req/s | 91.9% | 182 ms | 1,260 ms |
| **Watt (3×2 workers)** | **997 req/s** | **99.8%** | **11.6 ms** | **235 ms** |

##### Key Findings

###### 1\. Throughput and Reliability

- **Watt vs PM2**: +9.6% more throughput (997 vs 910 req/s)
- **Watt vs Single-CPU**: +2.5% more throughput (997 vs 972 req/s)
- **Watt success rate**: 99.8% vs 91.9% (PM2) and 93.7% (single-CPU pods)

Under sustained load of 1,000 req/s, Watt maintained near-perfect reliability while both PM2 and single-CPU pod architectures experienced significant request failures (8.1% and 6.3% failure rates respectively).

###### 2\. Latency Performance

Watt delivers dramatically better latency across all percentiles:

- **Median (P50)**: 11.6ms vs 182ms (PM2) = **93.6% faster**
- **Median (P50)**: 11.6ms vs 155ms (single-CPU) = **92.5% faster**
- **P95**: 235ms vs 1,260ms (PM2) = **81.3% faster**
- **P95**: 235ms vs 1,000ms (single-CPU) = **76.5% faster**

###### 3\. Why Single-CPU Pods Underperform

Single-CPU pods suffer from two compounding issues: blind load distribution and limited self-healing capability.

Kubernetes distributes connections via round-robin without visibility into each pod's actual load. When one pod starts struggling—perhaps processing a slow SSR request—it keeps receiving new connections at the same rate as healthy pods.

The deeper problem: a Node.js process with a blocked event loop cannot effectively monitor itself. Health checks run on the same event loop, so by the time the process can report it's unhealthy, requests have already queued up and timed out. Kubernetes only sees the problem after users have already experienced failures.

###### 4\. Why PM2 Underperforms

PM2's lower throughput and higher latency validate our analysis of the cluster module overhead:

- Master process acts as internal load balancer, adding IPC overhead
- Every request requires socket transfer via Unix domain sockets
- Lower success rate (91.9%) indicates the coordination overhead impacts reliability under load

###### 5\. Watt's Advantages

Watt's key advantage is external health monitoring combined with `SO_REUSEPORT`.

Because Watt monitors workers from outside their event loops, it can detect when a worker is struggling and restart it before the situation cascades—without terminating the entire pod. This directly addresses the fundamental problem that a blocked Node.js process cannot effectively monitor itself.

The `SO_REUSEPORT` architecture eliminates the ~30% IPC overhead imposed by PM2 and the cluster module. Workers accept connections directly from the kernel with zero coordination. Our benchmark demonstrates results: a 99.8% success rate and a 93% faster median latency under sustained load.

##### Benchmark Configuration

The tests used Kubernetes deployments on AWS EKS with explicit resource limits:

```yaml
# Single-CPU pods - 6 replicas with 1000m CPU limit each
apiVersion: apps/v1
kind: Deployment
metadata:
  name: next
spec:
  replicas: 6  # 6 pods × 1 CPU = 6 total CPUs
  template:
    spec:
      containers:
        - name: next
          resources:
            requests:
              cpu: '1000m'
              memory: '2Gi'
            limits:
              cpu: '1000m'
              memory: '2Gi'

# PM2 multi-worker pods - 3 replicas with 2000m CPU limit, 2 workers each
apiVersion: apps/v1
kind: Deployment
metadata:
  name: next-pm2
spec:
  replicas: 3  # 3 pods × 2 CPUs = 6 total CPUs
  template:
    spec:
      containers:
        - name: next-pm2
          env:
            - name: WORKERS
              value: "2"
          resources:
            requests:
              cpu: '2000m'
              memory: '4Gi'
            limits:
              cpu: '2000m'
              memory: '4Gi'

# Watt multi-worker pods - 3 replicas with 2000m CPU limit, 2 workers each
apiVersion: apps/v1
kind: Deployment
metadata:
  name: next-watt
spec:
  replicas: 3  # 3 pods × 2 CPUs = 6 total CPUs
  template:
    spec:
      containers:
        - name: next-watt
          env:
            - name: WORKERS
              value: "2"
          resources:
            requests:
              cpu: '2000m'
              memory: '4Gi'
            limits:
              cpu: '2000m'
              memory: '4Gi'
```

These results confirm that SO\_REUSEPORT-based multi-worker pods (Watt) outperform both single-CPU pod scaling and PM2-based multi-worker approaches in real-world production scenarios on Kubernetes.

## Getting Started with Watt

What's more fun than reading about our results? Replicating them with your own apps in your own environment, of course.

As you might already know, Watt is open source, and straightforward to implement. Simply follow these steps to deploy Next.js in Kubernetes with Watt: [https://docs.platformatic.dev/docs/guides/deployment/nextjs-in-k8s](https://docs.platformatic.dev/docs/guides/deployment/nextjs-in-k8s).

#### Implementation and Configuration Tips

**From PM2:**

- Remove PM2 ecosystem files
- Replace `pm2 start` with your Watt-enabled entry point
- Set `workers` to match your previous PM2 instance count
- Update health checks to target individual workers if needed

**From Single-CPU Pods:**

- Reduce pod count and increase CPU per pod (maintain total CPU)
- Example: 6 × 1-CPU pods → 3 × 2-CPU pods with `workers: 2`
- Update resource limits to match worker count
- Monitor and adjust based on your traffic patterns (and check out our [Intelligent Command Center](https://blog.platformatic.dev/the-intelligent-command-center-for-nodejs-is-now-open-source) if you want to make your life even easier 🙂)

For complete documentation and advanced features like shared HTTP caching, visit the Watt GitHub repository.

## Conclusion

The 93% latency improvement we showed at the start of this post isn't magic - it's the result of eliminating unnecessary coordination overhead and letting the Linux kernel do what it does best: efficiently distributing network connections.

Traditional Node.js scaling approaches, whether PM2's cluster module or horizontally scaled single-CPU pods, impose architectural constraints that hurt performance:

- **PM2/cluster**: Every new connections pays a ~30% IPC tax for master-worker coordination
- **Single-CPU pods**: Isolated queues compound load imbalances, leading to higher failure rates

Watt takes a different approach: leverage SO\_REUSEPORT to let multiple Node.js workers accept connections directly from the kernel, with zero coordination overhead. Then, we add all the needed control systems like healthchecks. The result is consistent and dramatic:

- **93.6% faster median latency** than PM2
- **99.8% reliability** under sustained load
- **9.6% more throughput** with the same CPU resources

What makes this especially compelling is the simplicity of implementation. You don't need specialized hardware, complex infrastructure changes, or extensive code refactoring. The path from PM2 or single-CPU pods to Watt is straightforward, and the performance gains are immediate. (Believe me, compared to some of the things I've teams do to achieve even a quarter of these improvements, this is pretty incredible ROI for your time here.)

If you're running Node.js applications - especially frameworks like Next.js that can't implement early request rejection - on Kubernetes or with PM2, you now have a proven alternative. The benchmarks speak for themselves, and the implementation is open source.

Give [Watt](https://platformatic.dev/) a try on your next deployment and measure the difference yourself. Your p95 latency will thank you.

If you want to have a chat with us about any of this, or are interested in professional support or architecture guidance with Watt or any of our other projects, feel free to send an email to [info@platformatic.dev](mailto:info@platformatic.dev) or add either [Luca](https://www.linkedin.com/in/lucamaraschi/) or [me](https://www.linkedin.com/in/matteocollina/) on LinkedIn.

[#nodejs](https://blog.platformatic.dev/tag/nodejs) [#nextjs](https://blog.platformatic.dev/tag/nextjs)