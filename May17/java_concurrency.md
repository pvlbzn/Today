## Processes and Threads
There are two basic units of execution:

- process
- thread

Java mostly concerned with threads, however processes are important too. Usually computer runs many processes and threads. Even one execution core machines. Processing time for them is shared among processes and threads usign "time slicing" feature.

Thus concurrency is possible on almost all kinds of machines. Of course, than more CPUs, than more concurrency is rewardong.

#### Process
Process has a self contained exectution environment: private set of basic run time resources, in particular, each process has its own memory space. What the user sees as a single application (process) may be a set of cooperating processes. Most OSes support Inter Process Communication, such as pipes and sockets.

#### Threads
Threads sometimes called as lightweight processes. Both, processes and threads provide an execution env, but threads are much chiper. Threads exist within a process, every process has at least one. Threads **share the process's resources**, including memory and open files. All Java apps starts within a main thread, which is capable to create additional threads.

#### Thread Objects
Each thread is associatd with an instance of the class `Thread`.

```
class PrimeThread extends Thread {
    long minPrime;
    PrimeThread(long minPrime) {
        this.minPrime = minPrime;
    }
    
    public void run() {
        // Compute.
    }
}
```

There are two stratigies for using Thread:

- create Thread each time
- Using an *executor*

