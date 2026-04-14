---
type: twir-item
issue: 254
item: 10
item_type: item
date: 2025-10-15
source: https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/
tags:
  - "Cloudflare"
  - "CPU"
  - "Nextjs"
status: auto
quality: keep
---

[[2025-10-15-TWIR-254|Index]]

# Item 10: Unpacking Cloudflare Workers CPU Performance Benchmarks

Source: [https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/](https://blog.cloudflare.com/unpacking-cloudflare-workers-cpu-performance-benchmarks/)

Summary:
This article analyzes recent CPU performance benchmarks comparing Cloudflare Workers and Vercel, identifying causes for initial disparities and detailing infrastructure and algorithmic improvements made by Cloudflare. It explains how platform-level optimizations and garbage collection tuning addressed issues, resulting in performance parity except for one Next.js case. The post emphasizes that most real-world workloads were unaffected by the original benchmark methodology.

Key takeaways:
- Benchmarking methodology and infrastructure tuning can significantly affect results.
- Cloudflare made improvements to isolate routing and garbage collection based on findings.
- Most users were not impacted by the observed performance gaps.
- Ongoing efforts are in place to close remaining gaps, especially for Next.js workloads.

Recommendation:
Read fully (read fully if interested in serverless performance or benchmarking)

Why it matters:
read fully if interested in serverless performance or benchmarking

Content:
# Unpacking Cloudflare Workers CPU Performance Benchmarks

On October 4, independent developer Theo Browne published [a series of benchmarks](https://github.com/t3dotgg/cf-vs-vercel-bench) designed to compare server-side JavaScript execution speed between Cloudflare Workers and Vercel, a competing compute platform built on AWS Lambda. The initial results showed Cloudflare Workers performing worse than Node.js on Vercel at a variety of CPU-intensive tasks, by a factor of as much as 3.5x.

We were surprised by the results. The benchmarks were designed to compare JavaScript execution speed in a CPU-intensive workload that never waits on external services. But, Cloudflare Workers and Node.js both use the same underlying JavaScript engine: [V8, the open source engine from Google Chrome](https://en.wikipedia.org/wiki/V8_(JavaScript_engine)). Hence, one would expect the benchmarks to be executing essentially identical code in each environment. Physical CPUs can vary in performance, but modern server CPUs do not vary by anywhere near 3.5x.

On investigation, we discovered a wide range of small problems that contributed to the disparity, ranging from some bad tuning in our infrastructure, to differences between the JavaScript libraries used on each platform, to some issues with the test itself. We spent the week working on many of these problems, which means over the past week Workers got better and faster for all of our customers. We even fixed some problems that affect other compute providers but not us, such as an issue that made trigonometry functions much slower on Vercel. This post will dig into all the gory details.

It's important to note that the original benchmark was not representative of billable CPU usage on Cloudflare, nor did the issues involved impact most typical workloads. Most of the disparity was an artifact of the specific benchmark methodology. Read on to understand why.

With our fixes, the results now look much more like we'd expect:

![BLOG-3051 2](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/4LbjDIgtezBKTCWKEW5ePJ/1b053a44c90cf6c59dd0da4d9f7d8057/BLOG-3051_2.png)

There is still work to do, but we're happy to say that after these changes, Cloudflare now performs on par with Vercel in every benchmark case except the one based on Next.js. On that benchmark, the gap has closed considerably, and we expect to be able to eliminate it with further improvements detailed later in this post.

We are grateful to Theo for highlighting areas where we could make improvements, which will now benefit all our customers, and even many who aren't our customers.

### Our benchmark methodology

We wanted to run Theo's test with no major design changes, in order to keep numbers comparable. Benchmark cases are nearly identical to Theo's original test but we made a couple changes in how we ran the test, in the hopes of making the results more accurate:

- Theo ran the test client on a laptop connected by a Webpass internet connection in San Francisco, against Vercel instances running in its sfo1 region. In order to make our results easier to reproduce, we chose instead to run our test client directly in AWS's us-east-1 datacenter, invoking Vercel instances running in its iad1 region (which we understand to be in the same building). We felt this would minimize any impact from network latency. Because of this, Vercel's numbers are slightly better in our results than they were in Theo's.
- We chose to use Vercel instances with 1 vCPU instead of 2. All of the benchmarks are single-threaded workloads, meaning they cannot take advantage of a second CPU anyway. Vercel's CTO, Malte Ubl, had [stated publicly on X](https://x.com/cramforce/status/1975656443954274780) that using single-CPU instances would make no difference in this test, and indeed, we found this to be correct. Using 1 vCPU makes it easier to reason about pricing, since both Vercel and Cloudflare charge for CPU time (`$`0.128/hr for Vercel in iad1, and `$`0.072/hr for Cloudflare globally).
- We made some changes to fix bugs in the test, for which [we submitted a pull request](https://github.com/t3dotgg/cf-vs-vercel-bench/pull/5). More on this below.

## Cloudflare platform improvements

Theo's benchmarks covered a variety of frameworks, making it clear that no single JavaScript library could be at fault for the general problem. Clearly, we needed to look first at the Workers Runtime itself. And so we did, and we found two problems â not bugs, but tuning and heuristic choices which interacted poorly with the benchmarks as written.

### Sharding and warm isolate routing: A problem of scheduling, not CPU speed

[Over the last year we shipped smarter routing that sends traffic to warm isolates more often](https://blog.cloudflare.com/eliminating-cold-starts-2-shard-and-conquer/). That cuts cold starts for large apps, which matters for frameworks with heavy initialization requirements like Next.js. The original policy optimized for latency and throughput across billions of requests, but was less optimal for heavily CPU-bound workloads for the same reason that such workloads cause performance issues in other platforms like Node.js: When the CPU is busy computing an expensive operation for one request, other requests sent to the same isolate must wait for it to finish before they can proceed.

The system uses heuristics to detect when requests are getting blocked behind each other, and automatically spin up more isolates to compensate. However, these heuristics are not precise, and the particular workload generated by Theo's tests â in which a burst of expensive traffic would come from a single client â played poorly with our existing algorithm. As a result, the benchmarks showed much higher latency (and variability in latency) than would normally be expected.

**It's important to understand that, as a result of this problem, the benchmark was not really measuring CPU time.** Pricing on the Workers platform is based on CPU time â that is, time spent actually executing JavaScript code, as opposed to time waiting for things. Time spent waiting for the isolate to become available makes the request take longer, but is not billed as CPU time against the waiting request. **So, this problem would not have affected your bill.**

After analyzing the benchmarks, we updated the algorithm to detect sustained CPU-heavy work earlier, then bias traffic so that new isolates spin up faster. The result is that Workers can more effectively and efficiently autoscale when different workloads are applied. I/O-bound workloads coalesce into individual already warm isolates while CPU-bound are directed so that they do not block each other. This change has already been rolled out globally and is enabled automatically for everyone. It should be pretty clear from the graph when the change was rolled out:

![BLOG-3051 3](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/Cio8BSY6tH7crMbXdnzYi/bab6314164907375eff2236a2bec21c3/image__7_.png)

### V8 garbage collector tuning

While this scheduling issue accounted for the majority of the disparity in the benchmark, we did find a minor issue affecting code execution performance during our testing.

The range of issues that we uncovered in the framework code in these benchmarks repeatedly pointed at [garbage collection](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Memory_management#garbage_collection) and memory management issues as being key contributors to the results. But, we would expect these to be an issue with the same frameworks running in Node.js as well. To see exactly what was going on differently with Workers and why it was causing such a significant degradation in performance, we had to look inwards at our own memory management configuration.

The [V8 garbage collector has a huge number of knobs](https://v8.dev/blog/trash-talk) that can be tuned that directly impact performance. One of these is the size of the "young generation". This is where newly created objects go initially. It's a memory area that's less compact, but optimized for short-lived objects. When objects have bounced around the "young space" for a few generations they get moved to the old space, which is more compact, but requires more CPU to reclaim.

V8 allows the embedding runtime to tune the size of the young generation. And it turns out, we had done so. Way back in June of 2017, just two months after the Workers project kicked off, we â or specifically, I, Kenton, as I was the only engineer on the project at the time â had configured this value according to V8's recommendations at the time for environments with 512MB of memory or less. Since Workers defaults to a limit of 128MB per isolate, this seemed appropriate.

V8's entire garbage collector has changed dramatically since 2017. When analyzing the benchmarks, it became apparent that the setting which made sense in 2017 no longer made sense in 2025, and we were now limiting V8's young space too rigidly. Our configuration was causing V8's garbage collection to work harder and more frequently than it otherwise needed to. As a result, we have backed off on the manual tuning and now allow V8 to pick its young space size more freely, based on its internal heuristics. This is already live on Cloudflare Workers, and it has given an approximately 25% boost to the benchmarks with only a small increase in memory usage. Of course, the benchmarks are not the only Workers that benefit: all Workers should now be faster. That said, for most Workers the difference has been much smaller.

## Tuning OpenNext for performance

The platform changes solved most of the problem. Following the changes, our testing showed we were now even on all of the benchmarks save one: Next.js.

Next.js is a popular web application framework which, historically, has not had built-in support for hosting on a wide range of platforms. Recently, a project called [OpenNext](https://opennext.js.org/) has arisen to fill the gap, making Next.js work well on many platforms, including Cloudflare. On investigation, we found several missing optimizations and other opportunities to improve performance, explaining much of why the benchmark performed poorly on Workers.

### Unnecessary allocations and copies

When profiling the benchmark code, we noticed that garbage collection was dominating the timeline. From 10-25% of the request processing time was being spent reclaiming memory.

![BLOG-3051 4](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/7lYdrV1WFzKEsD6qXspQ2K/725225d0d2e01f74057152b0d736868c/BLOG-3051_4.png)

![BLOG-3051 5](https://cf-assets.www.cloudflare.com/zkvhlag99gkb/6Ab4DJG0VzETky4t8rtYSe/23e9f0578bf8ac9834f7897d628b7cb2/BLOG-3051_5.png)

So we dug in and discovered that OpenNext, and in some cases Next.js and React itself, will often create unnecessary copies of internal data buffers at some of the worst times during the handling of the process. For instance, there's one `pipeThrough()` operation in the rendering pipeline that we saw creating no less than 50 2048-byte `Buffer` instances, whether they are actually used or not.

We further discovered that on every request, the [Cloudflare OpenNext adapter](https://github.com/opennextjs/opennextjs-cloudflare) has been needlessly copying every chunk of streamed output data as itâs passed out of the renderer and into the Workers runtime to return to users. Given this benchmark returns a 5 MB result on every request, that's a lot of data being copied!

In other places, we found that arrays of internal Buffer instances were being copied and concatenated using [`Buffer.concat`](https://nodejs.org/docs/latest/api/buffer.html#static-method-bufferconcatlist-totallength) for no other reason than to get the total number of bytes in the collection. That is, we spotted code of the form `getBody().length`. The function `getBody()` would concatenate a large number of buffers into a single buffer and return it, without storing the buffer anywhere. So, all that work was being done just to read the overall length. Obviously this was not intended, and fixing it was an easy win.

We've started opening a series of pull requests in OpenNext to fix these issues, and others in hot paths, removing some unnecessary allocations and copies:

We're not done. We intend to keep iterating through OpenNext code, making improvements wherever theyâre needed â not only in the parts that run on Workers. Many of these improvements apply to other OpenNext platforms. The shared goal of OpenNext is to make NextJS as fast as possible regardless of where you choose to run your code.

## Inefficient Streams Adapters

Much of the Next.js code was written to use Node.js's APIs for byte streams. Workers, however, prefers the web-standard [Streams API](https://developer.mozilla.org/en-US/docs/Web/API/Streams_API), and uses it to represent HTTP request and response bodies. This necessitates using adapters to convert between the two APIs. When investigating the performance bottlenecks, we found a number of examples where inefficient streams adapters are being needlessly applied. For example:

```
const stream = Readable.toWeb(Readable.from(res.getBody()))
```

`res.getBody()` was performing a `Buffer.concat(chunks)` to copy accumulated chunks of data into a new Buffer, which was then passed as an iterable into a Node.js [`stream.Readable`](https://nodejs.org/docs/latest/api/stream.html#readable-streams) that was then wrapped [by an adapter](https://nodejs.org/docs/latest/api/stream.html#streamreadabletowebstreamreadable-options) that returns a `ReadableStream`. While these utilities do serve a useful purpose, this becomes a data buffering nightmare since both Node.js streams and Web streams each apply their own internal buffers! Instead we can simply do:

```
const stream = ReadableStream.from(chunks);
```

This returns a `ReadableStream` directly from the accumulated chunks without additional copies, extraneous buffering, or passing everything through inefficient adaptation layers.

In other places we see that Next.js and React make extensive use of `ReadableStream` to pass bytes through, but the streams being created are value-oriented rather than byte-oriented! For example,

```
const readable = new ReadableStream({
  pull(controller) {
    controller.enqueue(chunks.shift());
    if (chunks.length === 0) {
      controller.close();
    }
});  // Default highWaterMark is 1!
```

Seems perfectly reasonable. However, there's an issue here. If the chunks are `Buffer` or `Uint8Array` instances, every instance ends up being a separate read by default. So if the `chunk` is only a single byte, or 1000 bytes, that's still always two reads. By converting this to a byte stream with a reasonable high water mark, we can make it possible to read this stream much more efficiently:

```
const readable = new ReadableStream({
  type: 'bytes',
  pull(controller) {
    controller.enqueue(chunks.shift());
    if (chunks.length === 0) {
      controller.close();
    }
}, { highWaterMark: 4096 });
```

Now, the stream can be read as a stream of bytes rather than a stream of distinct JavaScript values, and the individual chunks can be coalesced internally into 4096 byte chunks, making it possible to optimize the reads much more efficiently. Rather than reading each individual enqueued chunk one at a time, the ReadableStream will proactively call `pull()` repeatedly until the highWaterMark is reached. Reads then do not have to ask the stream for one chunk of data at a time.

While it would be best for the rendering pipeline to be using byte streams and paying attention to back pressure signals more, our implementation can still be tuned to better handle cases like this.

The bottom line? We've got some work to do! There are a number of improvements to make in the implementation of OpenNext and the adapters that allow it to work on Cloudflare that we will continue to investigate and iterate on. We've made a handful of these fixes already and we're already seeing improvements. Soon we also plan to start submitting patches to Next.js and React to make further improvements upstream that will ideally benefit the entire ecosystem.

Aside from buffer allocations and streams, one additional item stood out like a sore thumb in the profiles: `JSON.parse()` with a reviver function. This is used in both React and Next.js and in our profiling this was significantly slower than it should be. We built a microbenchmark and found that JSON.parse with a reviver argument recently got even slower when the standard [added a third argument](https://github.com/tc39/proposal-json-parse-with-source) to the reviver callback to provide access to the JSON source context.

For those unfamiliar with the reviver function, it allows an application to effectively customize how JSON is parsed. But it has drawbacks. The function gets called on every key-value pair included in the JSON structure, including every individual element of an Array that gets serialized. In Theo's NextJS benchmark, in any single request, it ends up being called well over 100,000 times!

Even though this problem affects all platforms, not just ours, we decided that we weren't just going to accept it. After all, we have contributors to V8 on the Workers runtime team! We've upstreamed a [V8 patch](https://chromium-review.googlesource.com/c/v8/v8/+/7027411) that can speed up `JSON.parse()` with revivers by roughly 33 percent. That should be in V8 starting with version 14.3 (Chrome 143) and can help everyone using V8, not just Cloudflare: Node.js, Chrome, Deno, the entire ecosystem.Â  If you are not using Cloudflare Workers or didn't change the syntax of your reviver you are currently suffering under the red performance bar.

We will continue to work with framework authors to reduce overhead in hot paths. Some changes belong in the frameworks, some belong in the engine, some in our platform.

## Node.js's trigonometry problem

We are engineers, and we like to solve engineering problems â whether our own, or for the broader community.

Theo's benchmarks were actually posted in response to a different benchmark by another author which compared Cloudflare Workers against Vercel. The original benchmark focused on calling trigonometry functions (e.g. sine and cosine) in a tight loop. In this benchmark, Cloudflare Workers performed 3x faster than Node.js running on Vercel.

The author of the original benchmark offered this as evidence that Cloudflare Workers are just faster. Theo disagreed, and so did we. We expect to be faster, but not by 3x! We don't implement math functions ourselves; these come with V8. We weren't happy to just accept the win, so we dug in.

It turns out that Node.js is not using the latest, fastest path for these functions. Node.js can be built with either the [clang](https://clang.llvm.org/) or [gcc](https://gcc.gnu.org/) compilers, and is written to support a broader range of operating systems and architectures than Workers. This means that Node.js' compilation often ends up using a lowest-common denominator for some things in order to provide support for the broadest range of platforms. V8 includes a [compile-time flag](https://github.com/search?q=repo%3Av8%2Fv8%20V8_USE_LIBM_TRIG_FUNCTIONS&type=code) that, in some configurations, allows it to use a faster implementation of the trig functions. In Workers, mostly by coincidence, that flag is enabled by default. In Node.js, it is not. We've opened a [pull request](https://github.com/nodejs/node/pull/60153) to enable the flag in Node.js so that everyone benefits, at least on platforms where it can be supported.

Assuming that lands, and once AWS Lambda and Vercel are able to pick it up, we expect this specific gap to go away, making these operations faster for everyone. This change won't benefit our customers, since Cloudflare Workers already uses the faster trig functions, but a bug is a bug and we like making everything faster.

Even the best benchmarks have bias and tradeoffs. It's difficult to create a benchmark that is truly representative of real-world performance, and all too easy to misinterpret the results of benchmarks that are not. [We particularly liked Planetscale's take on this subject.](https://planetscale.com/benchmarks)

These specific CPU-bound tests are not an ideal choice to represent web applications. Theo even notes this in his video. Most real-world applications on Workers and Vercel are bound by databases, downstream services, network, and page size. End user experience is what matters. CPU is one piece of that picture. That said, if a benchmark shows us slower, we take it seriously.

While the benchmarks helped us find and fix many real problems, we also found a few problems with the benchmarks themselves, which contributed to the apparent disparity in speed:

The benchmark is designed to be run on your laptop, from which it hits Cloudflare's and Vercel's servers over the Internet. It makes the assumption that latency observed from the client is a close enough approximation of server-side CPU time. The reasons are fair: As Theo notes, Cloudflare does not permit an application to measure its own CPU time, in order to prevent timing side channel attacks. Actual CPU time can be seen in logs after the fact, but gathering those may be a lot of work. It's just easier to measure time from the client.

However, as Cloudflare and Vercel are hosted from different data centers, the network latency to each can be a factor in the benchmark, and this can skew the results. Typically, this effect will favor Cloudflare, because Cloudflare can run your Worker in locations spread across 330+ cities worldwide, and will tend to choose the closest one to you. Vercel, on the other hand, usually places compute in a central location, so latency will vary depending on your distance from that location.

For our own testing, to minimize this effect, we ran the benchmark client from a VM on AWS located in the same data center as our Vercel instances. Since Cloudflare is well-connected to every AWS location, we think this should have eliminated network latency from the picture. We chose AWS's us-east-1 / Vercel's iad1 for our test as it is widely seen as the default choice; any other choice could draw questions about cherry-picking.

Cloudflare's servers aren't all identical. Although we refresh them aggressively, there will always be multiple generations of hardware in production at any particular time. Currently, this includes generations [10](https://blog.cloudflare.com/cloudflares-gen-x-servers-for-an-accelerated-future/), [11](https://blog.cloudflare.com/the-epyc-journey-continues-to-milan-in-cloudflares-11th-generation-edge-server/), and [12](https://blog.cloudflare.com/gen-12-servers/) of our server hardware.

Other cloud providers are no different. No cloud provider simply throws away all their old servers every time a new version becomes available.

Of course, newer CPUs run faster, even for single-threaded workloads. The differences are not as large as they used to be 20-30 years ago, but they are not nothing. As such, an application may get (a little bit) lucky or unlucky depending on what machine it is assigned to.

In cloud environments, even identical CPUs can yield different performance depending on circumstances, due to multitenancy. The server your application is assigned to is running many others as well. In AWS Lambda, a server may be running hundreds of applications; in Cloudflare, with our ultra-efficient runtime, a server may be running thousands. These "noisy neighbors" won't share the same CPU core as your app, but they may share other resources, such as memory bandwidth. As a result, performance can vary.

It's important to note that these problems create *correlated* noise. That is, if you run the test again, the application is likely to remain assigned to the same machines as before â this is true of both Cloudflare and Vercel. So, this noise cannot be corrected by simply running more iterations. To correct for this type of noise on Cloudflare, one would need to initiate requests from a variety of geographic locations, in order to hit different Cloudflare data centers and therefore different machines. But, that is admittedly a lot of work. (We are not familiar with how best to get an application to switch machines on Vercel.)

The Cloudflare version of the NextJS benchmark was not configured to use [force-dynamic](https://nextjs.org/docs/app/guides/caching#opting-out-2) while the Vercel version was. This triggered curious behavior. Our understanding is that pages which are not "dynamic" should normally be rendered statically at build time. With OpenNext, however, it appears the pages are still rendered dynamically, but if multiple requests for the same page are received at the same time, OpenNext will only invoke the rendering once. Before we made the changes to fix our scheduling algorithm to avoid sending too many requests to the same isolate, this behavior may have somewhat counteracted that problem. Theo reports that he had disabled force-dynamic in the Cloudflare version specifically for this reason: with it on, our results were so bad as to appear outright broken, so he intentionally turned it off.

Ironically, though, once we fixed the scheduling issue, using "static" rendering (i.e. not enabling force-dynamic) hurt Cloudflare's performance for other reasons. It seems that when OpenNext renders a "cacheable" page, streaming of the response body is inhibited. This interacted poorly with a property of the benchmark client: it measured time-to-first-byte (TTFB), rather than total request/response time. When running in dynamic mode â as the test did on Vercel â the first byte would be returned to the client before the full page had been rendered. The rest of the rendering would happen as bytes streamed out. But with OpenNext in non-dynamic mode, the entire payload was rendered into a giant buffer upfront, before any bytes were returned to the client.

Due to the TTFB behavior of the benchmark client, in dynamic mode, the benchmark actually does not measure the time needed to fully render the page. We became suspicious when we noticed that Vercel's observability tools indicated more CPU time had been spent than the benchmark itself had reported.

One option would have been to change the benchmarks to use TTLB instead â that is, wait until the last byte is received before stopping the timer. However, this would make the benchmark even more affected by network differences: The responses are quite large, ranging from 2MB to 15MB, and so the results could vary depending on the bandwidth to the provider. Indeed, this would tend to favor Cloudflare, but as the point of the test is to measure CPU speed, not bandwidth, it would be an unfair advantage.

Once we changed the Cloudflare version of the test to use force-dynamic as well, matching the Vercel version, the streaming behavior then matched, making the request fair. This means that neither version is actually measuring the cost of rendering the full page to HTML, but at least they are now measuring the same thing.

As a side note, the original behavior allowed us to spot that OpenNext has a couple of performance bottlenecks in its implementation of the composable cache it uses to deduplicate rendering requests. While fixes to these aren't going to impact the numbers for this particular set of benchmarks, we're working on improving those pieces also.

The React SSR benchmark contained a more basic configuration error. React inspects the environment variable `NODE_ENV` to decide whether the environment is "production" or a development environment. Many Node.js-based environments, including Vercel, set this variable automatically in production. Many frameworks, such as OpenNext, automatically set this variable for Workers in production as well. However, the React SSR benchmark was written against lower-level React APIs, not using any framework. In this case, the `NODE_ENV` variable wasn't being set at all.

And, unfortunately, when `NODE_ENV` is not set, React defaults to "dev mode", a mode that contains extra debugging checks and is therefore much slower than production mode. As a result, the numbers for Workers were much worse than they should have been.

Arguably, it may make sense for Workers to set this variable automatically for all deployed workers, particularly when Node.js compatibility is enabled. We are looking into doing this in the future, but for now we've updated the test to set it directly.

## What weâre going to do next

Our improvements to the Workers Runtime are already live for all workers, so you do not need to change anything. Many apps will already see faster, steadier tail latency on compute heavy routes with less jitter during bursts. In places where garbage collection improved, some workloads will also use fewer billed CPU seconds.

We also sent Theo a [pull request](https://github.com/t3dotgg/cf-vs-vercel-bench/pull/5) to update OpenNext with our improvements there, and with other test fixes.

But we're far from done. We still have work to do to close the gap between OpenNext and Next.js on Vercel â but given the other benchmark results, it's clear we can get there. We also have plans for further improvements to our scheduling algorithm, so that requests almost never block each other. We will continue to improve V8, and even Node.js â the Workers team employs multiple core contributors to each project. Our approach is simple: improve open source infrastructure so that everyone gets faster, then make sure our platform makes the most of those improvements.

And, obviously, we'll be writing more benchmarks, to make sure we're catching these kinds of issues ourselves in the future. If you have a benchmark that shows Workers being slower, send it to us with a repro. We will profile it, fix what we can upstream, and share back what we lea

... (content truncated)
