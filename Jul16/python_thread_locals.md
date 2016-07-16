## Thread Local
Thread-local data is data whose values are thread specific. Well, a code explains it much better:

{@see ./tl.py}

```
Th().start();
Th().start();
Th().start();

> Global: Thread-3
> Local:  Thread-2

> Global: Thread-3
> Local:  Thread-1

> Global: Thread-3
> Local:  Thread-3
```

`threading.local` is a class that represents thread-local data. Thread local storage is useful if you have a thread worker pool and each thread needs access to its own resource: network, database, etc. `threading` module uses the regular concept of threads. They have access to the process global data. `multiprocessing` module creates a new sub-process for each thread where is any global will be thread local.


Also, thread-local storage can be thought of as a namespace.

```
import threading


class Worker(threading.Thread):
    nmsp = threading.local()
    def run(self):
        self.nmsp.val = 0
        for i in range(5):
            self.nmsp.val += 1
            print("thread: {0}, value: {1}".format(self.name, self.nmsp.val))
```

Which will produce, beeing called 3 times

```
thread: Thread-1, value: 1
thread: Thread-1, value: 2
thread: Thread-1, value: 3
thread: Thread-1, value: 4
thread: Thread-1, value: 5

thread: Thread-2, value: 1
thread: Thread-2, value: 2
thread: Thread-2, value: 3
thread: Thread-2, value: 4
thread: Thread-2, value: 5

thread: Thread-3, value: 1
thread: Thread-3, value: 2
thread: Thread-3, value: 3
thread: Thread-3, value: 4
thread: Thread-3, value: 5
```
