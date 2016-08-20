# Multithreading Safety
Multithreaded apps often require sync objects. These objects are used to protect memory from being corrupted - modified by multiple threads at the same time.

## Race Condition
A race condition is the behavior of an electronic, software or other system where the output is dependent on the sequence or timing of other *uncontrollable* events. It becomes a bug when events do not happen in the order the programmer intended. Critical race conditions often happen when the process or threads depeds on some shared state. Operations upon shared states are **critical sections** that must be **mutually exclusive**. The memory model defined in the c11 and c++11 uses the term "data race" for a critical race condition caused by concurrent reads and writes of a shared memory location. C/C++ program containing a data race has undefined behavior.

#### Memory Model 
Descibes the interactions of threads through memory and their shared use of the data. A memory model allows a compiler to perform many important optimizations. Loop fusion move statements in the program and changes in the ordering of reads and writes can cause race conditions. Without a memory model, a compiler is not allowed to apply such optimizations to multi-threaded programs.

Modern PL implement a memory model. The memory model specifies synch barriers that are sstablished via special sync operations such as acquiring a lock by entering a sync block or method.

*Offtopic but*:

```
// The loop fusion
int i, a[100], b[100];

for (i = 0; i < 100; i++) {
    a[i] = 1;
}
for (i = 0; i < 100; i++) {
    b[i] = 2;
}

// Loop is eq to
for (i = 0; i < 100; i++) {
    a[i] = 1;
    b[i] = 2;
}
```

#### Race Condition Example
Usually race condition is hard to reproduce since the end results is nondeterministic and depends on the relative timing between interfering threads. On practice it means that test on first run can fail but pass on another run.

```
// Ok
+---------+---------+-----+-------+
| Thread1 | Thread2 | <-> | Value |
+=========+=========+=====+=======+
|         |         |     |       |
+---------+---------+-----+-------+
| read    |         | <-  | 0     |
+---------+---------+-----+-------+
| val++   |         |     | 0     |
+---------+---------+-----+-------+
| write   |         | ->  | 1     |
+---------+---------+-----+-------+
|         | read    | <-  | 1     |
+---------+---------+-----+-------+
|         | val++   |     | 1     |
+---------+---------+-----+-------+
|         | write   | ->  | 2     |
+---------+---------+-----+-------+

// Race Condition
+---------+---------+-----+-------+
| Thread1 | Thread2 | <-> | Value |
+=========+=========+=====+=======+
|         |         |     |       |
+---------+---------+-----+-------+
| read    |         | <-  | 0     |
+---------+---------+-----+-------+
|         | read    | <-  | 0     |
+---------+---------+-----+-------+
| val++   |         |     | 0     |
+---------+---------+-----+-------+
|         | val++   |     | 0     |
+---------+---------+-----+-------+
| write   |         | ->  | 1     |
+---------+---------+-----+-------+
|         | write   | ->  | 1     |
+---------+---------+-----+-------+
```

Result is 1 instead of 2 because the increment operations are ot mutually exclusive. Mutually exclusuve operation are those that cannot be interrupred while accessing some resource such as memory location.

## `mutex`
Conceptually `mutex` is a rubber duck in this example:

> When I am having a big heated discussion at work, I use a rubber chicken which I keep in my desk for just such occasions. The person holding the chicken is the only person who is allowed to talk. If you don't hold the chicken you cannot speak. You can only indicate that you want the chicken and wait until you get it before you speak. Once you have finished speaking, you can hand the chicken back to the moderator who will hand it to the next person to speak. This ensures that people do not speak over each other, and also have their own space to talk.

*[Xetius](http://stackoverflow.com/users/274/xetius)*

