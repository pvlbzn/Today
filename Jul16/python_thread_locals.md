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



