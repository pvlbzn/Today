###Starting and Stopping Threads

Countdown timer in `concurrency/cd.py`

```
import time
def countdown(n):
    while n > 0:
        print('t', n)
        n -= 1
        time.sleep(5)
```

Create and start thread `concurrency/thread.py`

```
from threading import Thread

# Create thread
t = Thread(target=coundown, args=(10, ))
# Launch it
t.start()
```

Threads are executed in their own system-level thread (like POSIX thread) that is fully managed by the host OS.

```
# Life check.
if t.is_alive():
	print('Thread is alive')
else:
	print('Thread is done')
```

The interpreter remains running until all threads terminate. For long-running threads or background tasks consider to use `daemon=True`. 

[Thread object](https://docs.python.org/3/library/threading.html#threading.Thread)

```
Thread(group=None, target=None, name=None, args=(), kwargs={}, *, daemon=None)
```

You can `.join(timeout=None)` thread. A call to `thread.join()` blocks the thread in which you are making the call until `thread` is finished. See example in `concurrency/join.py`.  
