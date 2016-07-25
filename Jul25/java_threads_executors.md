## `java.util.concurrent`
Concurrency API appeared in Java 1.5.  This is utility classes commonly useful in concurrent programming. This package includes a few small standardized extensible frameworks and some classes that provide useful functionality (difficult to implement).

### Threads'n'Runnables
Before starting a new thread code to be executed by this thread, often called the *task*, is must be specified. This is done by implementing `Runnable` functional interface with a single method `run()`

```
// Because of Runnable is an interface lambda can be used.
Runnable task = () -> {
    String tname = Thread.currentThread().getName();
    System.out.println("hello " + tname);
};

task.run();

Thread thread = new Thread(task);
thread.start();

System.out.println("done");
```

It will print:

```
hello main
hello Thread-0
done

// or
hello main
done
hello Thread-0
```

Working with a `Thread` class directly can be error-prone. `java.util.concurrent` constantly involved over time.

### Executors
Concurrency API has the concept of an `ExecutorService` as an abstraction over threads. Executors are apable of running asynchronous tasks and manage a pool of threads.

```
ExecutorService exec = Executors.newSingleThreadExecutor();
exec.submit(() -> {
    String tname = Thread.currentThread().getName();
    System.out.println("hello " + tname);
});
```

This code will print `hello pool-1-thread-1`. `Executors` class, as can be read from its name, provides a factory methods for creating various kinds of executor service.
