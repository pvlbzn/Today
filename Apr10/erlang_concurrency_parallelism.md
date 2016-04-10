####Concurrency, Parallelism

Abstract: if you look out of your window, all the things happening on the street happen in parallel.

In everyday language, words like concurrent, simulatneous, parallel mean almost the same thing. In PL, we need to be more precise, we nedd to distinguish between concurrent and parallel programs.

*Single-core computer can never run a parallel program.* However, it is possible to run concurrent programs on a single-core computer. Computer time-shares between the different tasks, maintaining the illusion that the different tasks run in parallel.

Parallel computers were rare and expensive, but today multicore computers are common. We can expect the number of cores pre chip to steadily increase.

Concurrent programs in Erlang are made from set of communicating sequential processes. An Erlang process is a little VM that can evaluate a single Erlang function. They arent OS processes.

To *write a concurrent program* you must identify a set of processes that will solve your problem, this act called **modeling concurrency**. This is kind of analogous to OOP design.

> The difference between a *good* and *bad* process model can *make* or *break* a design.

Concurrent program can be run on a parallel computer or on a set of networked computers.

Will concurrent program actually run in parallel on a parallel computer? Om a multicore box, the OS might decide to turn off a core to save energy. In a cloud,a computation might be suspended and moved to a new computer. These are things outside of control.

> Concurrency has to do with software structure; parallelism has to do with hardware.

-

####Sequential and Concurrent

Sequential languages are languages that were designed for writing sequential programs and have no linguistic constructs for describing concurrent computations. Concurrent PL are L that were designed for writing concurrent programs, thus have special constructs for expressign concyrrency in the L itself.

*In most sequential PL concurrency is provided as an interface to the __concurrency primitives of the host OS__*. In Erlang concurrency provided by the Erlang VM, not by OS.







