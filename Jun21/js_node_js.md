## Node.js
Node.js is a runtime environment which interprets JavaScript using `V8` JavaScript engine which is implemented in C++. `V8` uses runtime optimizations such as inlining, ilision, caching and others.

Node.js has an asynchronous, event-driven architecture. It operates on a single thread, using non-blocking I/O calls, so node can handle lots of concurrent connections without the cost of thread context switching. Because of an architecture (observer pattern) every function which performing I/O must use a callback. In order to accommodate the single-threaded event loop, node utilizes the [`libuv`](https://en.wikipedia.org/wiki/Libuv) that uses fixed-size threadpool that is responsivle for all non-blocking async I/O ops.

Event driven programming is when a control flow is determined by events or changes in a state. The general impl is to have a central mechanism that listens for events and calls a callback function once an event has been detected.

#### `libuv`
`libuv` is a software library that provides async event notification.

>libuv enforces an asynchronous, event-driven style of programming. Its core job is to provide an event loop and callback based notifications of I/O and other activities. libuv offers core utilities like timers, non-blocking networking support, asynchronous file system access, child processes and more.

It provide features like async TCP, UPD, DNS resolution, etc.

#### Thread Pool
Thread pool is a pattern, consists of a number of threads, created to perform a number of tasks concurrently. Reason for using a thread pool, rather that the spawning one thread per task is to prevent the time and memory overhead inherent in thread creation. Task queue is responsible for a distributing tasks to threads. The threads in the pool take tasks off the queue, compute them, and repeat.

Thread pool has a pool size. Pool size is the number of threads.

#### Event Loop
