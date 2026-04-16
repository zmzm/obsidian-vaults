---
type: twir-item
issue: 269
item: 3
item_type: item
date: 2026-02-18
source: https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster
tags:
  - "WebStreams"
  - "10x"
  - "Nextjs"
  - "ServerComponents"
status: auto
quality: keep
---

[[2026-02-18-TWIR-269|Index]]

# Item 3: Vercel - We Ralph Wiggumed WebStreams to make them 10x faster

Source: [https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster](https://vercel.com/blog/we-ralph-wiggumed-webstreams-to-make-them-10x-faster)

Summary:
Vercel's engineering team identified major performance bottlenecks in Node.js's implementation of the WHATWG WebStreams API, especially as used in Next.js and React server rendering. By developing the `fast-webstreams` library, they achieved up to 14x speed improvements for key server rendering patterns, including React Flight. Their optimizations are influencing upstream Node.js development.

Key takeaways:
- Native WebStreams in Node.js are significantly slower than legacy streams due to Promise and object allocation overhead.
- The `fast-webstreams` library routes operations through optimized Node.js streams, reducing overhead and boosting throughput.
- For React Server Components (Flight), performance gains are especially dramatic, making server rendering much more efficient.
- Some of these optimizations are being proposed for inclusion in Node.js itself.

Recommendation:
Read fully (for anyone working on server rendering, performance, or low-level Node.js/React internals)

Why it matters:
for anyone working on server rendering, performance, or low-level Node.js/React internals

Content:
# We Ralph Wiggumed WebStreams to make them 10x faster

When we started profiling Next.js server rendering earlier this year, one thing kept showing up in the flamegraphs: WebStreams. Not the application code running inside them, but the streams themselves. The Promise chains, the per-chunk object allocations, the microtask queue hops. After [Theo Browne's server rendering benchmarks](/blog/fluid-compute-benchmark-results) highlighted how much compute time goes into framework overhead, we started looking at where that time actually goes. A lot of it was in streams.

Turns out that WebStreams have an [incredibly complete test suite](https://github.com/web-platform-tests/wpt/tree/master/streams), and that makes them a great candidate for doing an AI-based re-implementation in a purely test-driven and benchmark-driven fashion. This post is about the performance work we did, what we learned, and how this work is already making its way into Node.js itself through Matteo Collina's [upstream PR](https://github.com/nodejs/node/pull/61807).

Node.js has two streaming APIs. The older one (`stream.Readable`, `stream.Writable`, `stream.Transform`) has been around for over a decade and is heavily optimized. Data moves through C++ internals. Backpressure is a boolean. Piping is a single function call.

The newer one is the WHATWG Streams API: `ReadableStream`, `WritableStream`, `TransformStream`. This is the web standard. It powers `fetch()` response bodies, `CompressionStream`, `TextDecoderStream`, and increasingly, server-side rendering in frameworks like Next.js and React.

The web standard is the right API to converge on. But on the server, it is slower than it needs to be.

To understand why, consider what happens when you call `reader.read()` on a native WebStream in Node.js. Even if data is already sitting in the buffer:

1. A `ReadableStreamDefaultReadRequest` object is allocated with three callback slots
2. The request is enqueued into the stream's internal queue
3. A new Promise is allocated and returned
4. Resolution goes through the microtask queue

That is four allocations and a microtask hop to return data that was already there. Now multiply that by every chunk flowing through every transform in a rendering pipeline.

Or consider `pipeTo()`. Each chunk passes through a full Promise chain: read, write, check backpressure, repeat. An `{value, done}` result object is allocated per read. Error propagation creates additional Promise branches.

None of this is wrong. These guarantees matter in the browser where streams cross security boundaries, where cancellation semantics need to be airtight, where you do not control both ends of a pipe. But on the server, when you are piping React Server Components through three transforms at 1KB chunks, the cost adds up.

We benchmarked native WebStream `pipeThrough` at **630 MB/s** for 1KB chunks. Node.js `pipeline()` with the same passthrough transform: **~7,900 MB/s**. That is a 12x gap, and the difference is almost entirely Promise and object allocation overhead.

We have been working on a library called `fast-webstreams` that implements the WHATWG `ReadableStream`, `WritableStream`, and `TransformStream` APIs backed by Node.js streams internally. Same API, same error propagation, same spec compliance. The overhead is removed for the common cases.

The core idea is to route operations through different fast paths depending on what you are actually doing:

### [Link to heading](#when-you-pipe-between-fast-streams:-zero-promises)When you pipe between fast streams: zero Promises

This is the biggest win. When you chain `pipeThrough` and `pipeTo` between fast streams, the library does not start piping immediately. Instead, it records upstream links:

`source → transform1 → transform2 → ...`

When `pipeTo()` is called at the end of the chain, it walks upstream, collects the underlying Node.js stream objects, and issues a single `pipeline()` call. One function call. Zero Promises per chunk. Data flows through Node's optimized C++ path.

```
1

const source = new ReadableStream({

3

controller.enqueue(generateChunk());

7

const transform = new TransformStream({

8

transform(chunk, controller) {

9

controller.enqueue(process(chunk));

13

const sink = new WritableStream({

14

write(chunk) { consume(chunk); }

18

await source.pipeThrough(transform).pipeTo(sink);
```

The result: **~6,200 MB/s**. That is ~10x faster than native WebStreams and close to raw Node.js pipeline performance.

If any stream in the chain is not a fast stream (say, a native `CompressionStream`), the library falls back to either native `pipeThrough` or a spec-compliant `pipeTo` implementation.

### [Link to heading](#when-you-read-chunk-by-chunk:-synchronous-resolution)When you read chunk by chunk: synchronous resolution

When you call `reader.read()`, the library tries `nodeReadable.read()` synchronously. If data is there, you get `Promise.resolve({value, done})`. No event loop round-trip. No request object allocation. Only when the buffer is empty does it register a listener and return a pending Promise.

```
1

const reader = stream.getReader();

3

const { value, done } = await reader.read();
```

The result: **~12,400 MB/s**, or 3.7x faster than native.

### [Link to heading](#the-react-flight-pattern:-where-the-gap-is-largest)The React Flight pattern: where the gap is largest

This is the one that matters most for Next.js. React Server Components use a specific byte stream pattern: create a `ReadableStream` with `type: 'bytes'`, capture the controller in `start()`, enqueue chunks externally as the render produces them.

```
2

const stream = new ReadableStream({

8

ctrl.enqueue(new Uint8Array(payload1));

9

ctrl.enqueue(new Uint8Array(payload2));
```

Native WebStreams: **~110 MB/s**. fast-webstreams: **~1,600 MB/s**. That is **14.6x faster** for the exact pattern used in production server rendering.

The speed comes from `LiteReadable`, a minimal array-based buffer we wrote to replace Node.js's `Readable` for byte streams. It uses direct callback dispatch instead of EventEmitter, supports pull-based demand and BYOB readers, and costs about 5 microseconds less per construction. That matters when React Flight creates hundreds of byte streams per request.

### [Link to heading](#fetch-response-bodies:-streams-you-don't-construct-yourself)Fetch response bodies: streams you don't construct yourself

The examples above all start with `new ReadableStream(...)`. But on the server, most streams do not start that way. They start from `fetch()`. The response body is a native byte stream owned by Node.js's HTTP layer. You cannot swap it out.

This is a common pattern in server-side rendering: fetch data from an upstream service, pipe the response through one or more transforms, and forward the result to the client.

```
1

const upstream = await fetch('<https://api.example.com/data>');

4

const transformed = upstream.body

5

.pipeThrough(new TransformStream({ transform(chunk, ctrl) {  ctrl.enqueue(chunk); } }))

6

.pipeThrough(new TransformStream({ transform(chunk, ctrl) {  ctrl.enqueue(chunk); } }))

7

.pipeThrough(new TransformStream({ transform(chunk, ctrl) {  ctrl.enqueue(chunk); } }));

9

return new Response(transformed);
```

With native WebStreams, each hop in this chain pays the full Promise-per-chunk cost. Three transforms means roughly 6-9 Promises per chunk. At 1KB chunks, that gets you **~260 MB/s**.

The library handles this through deferred resolution. When `patchGlobalWebStreams()` is active, `Response.prototype.body` returns a lightweight fast shell wrapping the native byte stream. Calling `pipeThrough()` does not start piping immediately. It just records the link. Only when `pipeTo()` or `getReader()` is called at the end does the library resolve the full chain: it creates a single bridge from the native reader into Node.js `pipeline()` for the transform hops, then serves reads from the buffered output synchronously.

The cost model: one Promise at the native boundary to pull data in. Zero Promises through the transform chain. Sync reads at the output.

The result: **~830 MB/s**, or **3.2x faster** than native for the three-transform fetch pattern. For simple response forwarding without transforms, it is **2.0x faster** (850 vs 430 MB/s).

All numbers are throughput in MB/s at 1KB chunks on Node.js v22. Higher is better.

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| Operation | Node.js streams | fast | native | fast vs native |
| read loop | 26,400 | **12,400** | 3,300 | **3.7x** |
| write loop | 26,500 | **5,500** | 2,300 | **2.4x** |
| pipeThrough | 7,900 | **6,200** | 630 | **9.8x** |
| pipeTo | 14,000 | **2,500** | 1,400 | **1.8x** |
| for-await-of | — | **4,100** | 3,000 | **1.4x** |

The Promise-per-chunk overhead compounds with chain depth:

|  |  |  |  |
| --- | --- | --- | --- |
| Depth | fast | native | fast vs native |
| 3 transforms | **2,900** | 300 | **9.7x** |
| 8 transforms | **1,000** | 115 | **8.7x** |

|  |  |  |  |
| --- | --- | --- | --- |
| Pattern | fast | native | fast vs native |
| start + enqueue (React Flight) | **1,600** | 110 | **14.6x** |
| byte read loop | **1,400** | 1,400 | 1.0x |
| byte tee | **1,200** | 750 | **1.6x** |

|  |  |  |  |
| --- | --- | --- | --- |
| Pattern | fast | native | fast vs native |
| Response.text() | 900 | 910 | 1.0x |
| Response forwarding | **850** | 430 | **2.0x** |
| fetch → 3 transforms | **830** | 260 | **3.2x** |

Creating streams is also faster, which matters for short-lived streams:

|  |  |  |  |
| --- | --- | --- | --- |
| Type | fast | native | fast vs native |
| ReadableStream | **2,100** | 980 | **2.1x** |
| WritableStream | **1,300** | 440 | **3.0x** |
| TransformStream | **470** | 220 | **2.1x** |

fast-webstreams passes **1,100 out of 1,116** Web Platform Tests. Node.js's native implementation passes 1,099. The 16 failures that remain are either shared with native (like the unimplemented `type: 'owning'` transfer mode) or are architectural differences that do not affect real applications.

The library can patch the global `ReadableStream`, `WritableStream`, and `TransformStream` constructors:

```
1

import { patchGlobalWebStreams } from 'fast-webstreams';

3

patchGlobalWebStreams();
```

The patch also intercepts `Response.prototype.body` to wrap native fetch response bodies in fast stream shells, so `fetch()` → `pipeThrough()` → `pipeTo()` chains hit the pipeline fast path automatically.

At Vercel, we are looking at rolling this out across our fleet. We will do so carefully and incrementally. Streaming primitives sit at the foundation of request handling, response rendering, and compression. We are starting with the patterns where the gap is largest: React Server Component streaming, response body forwarding, and multi-transform chains. We will measure in production before expanding further.

A userland library should not be the long-term answer here. The right fix is in Node.js itself.

Work is already happening. After a conversation on X, Matteo Collina submitted [nodejs/node#61807](https://github.com/nodejs/node/pull/61807), "stream: add fast paths for webstreams read and pipeTo." The PR applies two ideas from this project directly to Node.js's native WebStreams:

1. **`read()`** **fast path**: When data is already buffered, return a resolved Promise directly without creating a

   `ReadableStreamDefaultReadRequest` object. This is spec-compliant because `read()` returns a Promise either way, and resolved promises still run callbacks in the microtask queue.
2. **`pipeTo()`** **batch reads**: When data is buffered, batch multiple reads from the controller queue without creating per-chunk request objects. Backpressure is respected by checking `desiredSize` after each write.

The PR shows **~17-20% faster** buffered reads and **~11% faster** `pipeTo`. These improvements benefit every Node.js user for free. No library to install, no patching, no risk.

James Snell's [Node.js performance issue #134](https://github.com/nodejs/performance/issues/134) outlines several additional opportunities: C++-level piping for internally-sourced streams, lazy buffering, eliminating double-buffering in WritableStream adapters. Each of these could close the gap further.

We will keep contributing ideas upstream. The goal is not for fast-webstreams to exist forever. The goal is for WebStreams to be fast enough that it does not need to.

**The spec is smarter than it looks.** We tried many shortcuts. Almost every one of them broke a Web Platform Test, and the test was usually right. The `ReadableStreamDefaultReadRequest` pattern, the Promise-per-read design, the careful error propagation: they exist because cancellation during reads, error identity through locked streams, and thenable interception are real edge cases that real code hits.

**`Promise.resolve(obj)`** **always checks for thenables.** This is a language-level behavior you cannot avoid. If the object you resolve with has a `.then` property, the Promise machinery will call it. Some WPT tests deliberately put `.then` on read results and verify that the stream handles it correctly. We had to be very careful about where `{value, done}` objects get created in hot paths.

**Node.js** **`pipeline()`** **cannot replace WHATWG** **`pipeTo`****.** We hoped to use `pipeline()` for all piping. It causes 72 WPT failures. The error propagation, stream locking, and cancellation semantics are fundamentally different. `pipeline()` is only safe when we control the entire chain, which is why we collect upstream links and only use it for full fast-stream chains.

**`Reflect.apply`****, not** **`.call()`****.** The WPT suite monkey-patches `Function.prototype.call` and verifies that implementations do not use it to invoke user-provided callbacks. `Reflect.apply` is the only safe way. This is a real spec requirement.

## [Link to heading](#we-built-most-of-fast-webstreams-with-ai)We built most of fast-webstreams with AI

Two things made that viable:

The amazing [Web Platform Tests](https://web-platform-tests.org/) gave us 1,116 tests as an immediate, machine-checkable answer to "did we break anything?" And we built a benchmark suite early on so we could measure whether each change actually moved throughput. The development loop was: implement an optimization, run the WPT suite, run benchmarks. When tests broke, we knew which spec invariant we had violated. When benchmarks did not move, we reverted.

The WHATWG Streams spec is long and dense. The interesting optimization opportunities sit in the gap between what the spec *requires* and what current implementations *do*. `read()` must return a Promise, but nothing says that Promise cannot already be resolved when data is buffered. That kind of observation is straightforward when you can ask an AI to analyze algorithm steps for places where the observable behavior can be preserved with fewer allocations.

fast-webstreams is [available on npm](https://www.npmjs.com/package/experimental-fast-webstreams) as `experimental-fast-webstreams`. The "experimental" prefix is intentional. We are confident in correctness, but this is an area of active development.

If you are building a server-side JavaScript framework or runtime and hitting WebStreams performance limits, we would love to hear from you. And if you are interested in improving WebStreams in Node.js itself, Matteo's [PR](https://github.com/nodejs/node/pull/61807) is a great place to start.

Related notes: [[Server Components]]
