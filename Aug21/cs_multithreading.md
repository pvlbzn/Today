# Threads
Threads share all segments (data, stack, heap, code) except the stack. Each thread has a private stack, this is the main reason why each thread can do its own thing.

### Mutex and Semaphore
Mutex was discussed yesterday. A semaphore is a variable or abstact data type that is used for controlling access by multiple processes to a comon resourse in a concurrent system such as a multiprogramming OS. A basic semaphore is a variable that is changed (upped or downed) depending on programmer-defined conditions. Then, the variable used as a condition to control access to some shared resource.

While *mutexes* should be used to protect shared resources, *semaphores* should be used for signaling. *Not mutexes for signaling or semaphores for protecting shared resources*. 

Both, a mutex and a semaphore is used for a *critical sections*.

### POSIX
In POSIX, the thread type is `pthread_t`, mutex `pthread_mutex_t`, semaphore `sem_t` which belongs to `pthread.h` and `semaphore.h` header files. 

-

## Working With Threads
#### Creation
Function signature:

```
int pthread_create(pthread_t *thread,
                   const pthread_attr_t *attr,
                   void *(*start_routine)(void *),
                   void *arg)
```

`*thread` is a pointer to a `pthread_t` where the function stores the id of the newly created thread.

`*attr` accepts attributes and typically is `NULL`.

`*start_routine` is a function where new thread will start at. If the thread returns from the function, the thread is terminated as well (kind of `main`).

`*arg` is passed to the function when the thread is started.

#### Stop, Exit, Deatach
To exit a thread it should return from a thread function or by calling

`void pthread_exit(void *value_ptr)`

To deatach thread

`int pthread_detach(pthread_t thread)`

To stop a thread

`int pthread_cancel(pthread_t thread)`

#### Mutex, Semaphore

`int pthread_mutex_init(pthread_mutex_t *mutex, const pthread_mutexattr_t *attr)`

`*mutex` that will be initialized, second parameter, `*attr`, usually is `NULL` but also can be a structure that specifies different attrs for it.

For locking and unlocking

`int pthread_mutex_lock(pthread_mutex_t *mutex)`
`int pthread_mutex_unlock(pthread_mutex_t *mutex)`

are used respectively. For try to lock mutex

`int pthread_spin_trylock(pthread_spinlock_t *lock)`

is used. If it can't lock the mutex it returns an error instead of blocking.

In order to destroy mutex following funciton is used:

`int pthread_mutex_destroy(pthread_mutex_t *mutex)`

<br>

Semaphore follows a similar approach. They initialized with `sem_init`.
To "up" a semaphore `sem_post` is used, `sem_wait` used to "down" the semaphore. To destroy a semaphore use `sem_destroy`.

#### Join
In order to make one thread stop and wait for another thread to finish use

`int pthread_join(pthread_t thread, void **value_ptr)`

Where thread is an id to pick which thread to wait for and `**` parameter to capture the return value. Unjoined threads are called `zombies`.


## Performance
Spawning a thousands of threads with a short life time is expensive. A common pattern which is used to reduce this cost is a *thread pool*. At a startup an application will spawn a number of threads and supply them on demand. When the thread task completes, the thread returns to the pool for reuse later.

Each thread also gets its own stack, therefore consumes a memory.

