####Global Interpreter Lock

Talk by [David](http://www.youtube.com/watch?v=zEaosS1U5qY).

Source code is in `gil/cd.py`.

On my current machine it took ~5.40 sec.

However, threaded version of the code, `gil/th_cd.py` took ~6.62 sec to execute. On David's machine it took even more, 1.8 times longer. Most fun part is that if you disable one CPU, it will execute faster.


####Python Threads
- Python threads are **real** system threads.
- Fully managed by the host OS
- Represent threaded execution of the Python interpreter process (written in C)


####GIL
There is GIL in interpreter implementation and reason why it there is simplify this implementation.

- Parralel execution is forbidden
- There is a "global interpreter lock"
- The GIL ensures that only one thread runs in the interpreter at once
- Simplifies many low-level details(memory, callouts to C, etc)

Outcome of the GIL is that instead of parallel computing you get a cooperative multitasking.

```
				I/O	   I/O	   I/O     I/O
Thread I	---> |		|		| --->	|
			run  |		|		| run	|
Thread II		 | --->	|		|		|
				 | run	|		|		|
Thread III		 |		| --->	|		|
						  run
```

- When a thread is running, it **holds the GIL**
- GIL **released on I/O** (read, write, send, recv, etc)


####CPU Bound Tasks

CPU-bound threads that never perform I/O are handled as a special case. They are *checked* every 100 *ticks*.

```
CPU Bound	---------> | check | ---------> | check | ---------> etc
Thread		100 ticks			 100 ticks		      100 ticks
```

**Tick**:
Loosely one machine instruction. They are not strictly based on time, one ticks might be longer than others.

**Check**:

- Reset the tick counter
- Runs signal handlers if the main thread
- Releases the GIL
- Reacquires the GIL

This stuff is implemented [here](https://github.com/python/cpython/blob/master/Python/ceval.c)


####Python Locks

CPython interpret only one type of lock, it used for everything. It's not *mutex* lock. It's a **binary semaphore** constructed from a *pthreads* mutex and a condition variable.

**Locks**:
```
locked = 0						// Lock status. 0 - available, 1 - not.
mutex  = pthreads_mutex()		// Lock for the status
cond   = pthreads_cond()		// Used for waiting/wakeup
```

**aquare(), release()**:

```
// Preudocode

release() {
	mutex.acquire()
	locked = 0
	mutex.release()
	cond.signal()
}

acquire() {
	mutex.acquire()
	while (locked) {
		cond.wait(mutex)
	}
	locked = 1
	mutex.release()
}
```

There is a 'real' [implementation](https://github.com/python/cpython/blob/master/Python/ceval.c#L330-370), I guess at least. 

A critical aspect concerns this signalig between threads `cond.signal()` and `cond.wait(mutex)`.


####Thread Switching

```
Thread I		------------->
				running

Thread II		ready (waiting for GIL)
```

There are two cases:

**Easy case**: Thread I performs I/O

```
Thread I		----------------> 	| I/O |
				running		 		release the GIL
									signal pthread/OS
									context switch
											|
											v
Thread II		ready (waiting for GIL)		|--------------------->
											^
											acquire GIL
```

**Tricky case**: Thread I runs until the *check*

```
Thread I		-------------> 	|check| 	???
				100 ticks		release GIL
								signal pthreads/OS

Thread II		ready (waiting for GIL)		???
```

`???` which thread runs now? Either thread is able to run. Threads stored in a some queue in pthreads library.

**OS Scheduling**:

- The OS has a priority queue of threads/processes that are ready to run
- The signaled thread simply enters that queue (signaled thread means thread which was dequeued)
- The OS then runs the process or thread with the highest priority
- It may or may not be the signaled thread

**Highest priority wins case**: Thread 2 might immediately take over

```
Thread I		-------------> 		|check|
(Low priority)	100 ticks			release GIL
									signal pthreads/OS
									context switch
									acquire GIL
										|
										v
Thread II		ready (waiting for GIL)	|---------------->
(High priority)							Running
```

On 1 CPU threads works kind of long, hundreds of thousands *ticks* before switch. On 2 CPU threads start switching between each other substantially.

![alt text][1,2 CPU]
[1,2 CPU]: https://raw.githubusercontent.com/pvlbzn/Today/master/Apr13/one_two_cpu_threads.png

*Red marker* is actually bad. It's means that two CPU are fighting with earch other. OS thinks "Ok, I can run two threads", and keep first thread alive.

Things getting worst with even more CPU:
![alt text][4CPU]
[4CPU]: https://raw.githubusercontent.com/pvlbzn/Today/master/Apr13/four_threads_four_cpu.png

*Note, resolution twice higher than examples above, 1024 ticks instead of 2048.*

The similar issue applies to the I/O bound tasks. For more details check a source: [Interactive GIL Visualization](http://dabeaz.com/GIL/gilvis/index.html).


###The New GIL

Python 3.2 has a new GIL implementation.

####New Thread Switching

- Instead of ticks, there is now a global variable

```
static volatile int gil_drop_request = 0;
```

- A thread runs until the value gets set to 1
- At which point, the thread **must** drop the GIL

**How this happen**:

Suppose that there is just one thread

```
Thread I	----------------->
			running
```

And a new thread appeal

```
Thread I	----------------->
			running

Thread II	..................
			suspeded
			cv_wait(gil, TIMEOUT)
```

Waiting thread does a timed `cv_wait` on GIL. By default **TIMEOUT** is **5ms**, but it can be changed.

The idea is: Thread II waits to see if the GIL gets released voluntarily by Thread I (like if there is I/O or it goes to sleep for some other reason). 

Again, **easy case** is:

```
Thread I	-----------------> 	| I/O |
			running				| signal
								v
Thread II	..................	|------------------>
			suspeded			running
			cv_wait(gil, TIMEOUT)
```

**Forcing case**:

```
Thread I	------------------->
			gil_drop_request = 1
						 TIMEOUT
Thread II	....................|...|------------------>
								wait	running
```

After *drop request* a thread finishes an instruction and signal to other thread.


####Bad Thing

Bad thing about new GIL is in **response time**. New GIL increases response time. To handle I/O, a thread must go through the entire timeout sequence to get control.

```
			running
Thread I	------------------------------->
									TIMEOUT		running
Thread II			|......................|....|------------>
					data
					arrives
```

In other words, when data arrives on the waiting thread, it should wait for timeout from the beggining. Data arrived, 5ms, data processed.

Other thing, the thread which *drop requests* often don't get the GIL, GIL can be passed to another thread.









