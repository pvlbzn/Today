## Profile Your Code

## `time`
A simple and old `time` utility:

```
$ time python program.py

real    time
user    time
sys     time
```

- `real` actual elapsed time
- `user` amount of cpu time spent outside of kernel
- `sys` amount of cpu time spent inside kernel

## `cProfile`
Python standard library provides two implementations of the same interface:

1. `cProfile`
2. `profile`

`cProfile` is a C extension which is suitable for profiling long-running programs. It is based on `lsprof`. `profile` is a pure Python module whose interface is imitated by `cProfile` but it adds significant overhead to profiled programs.

```
import cProfile

def loop():
    l = []
    for n in range(5000):
        l.append(16**n)

# Program should be wraped into the string
cProfile.run('
    loop()
')
```

Will output

```
>>> cProfile.run('loop()')
         5004 function calls in 0.180 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.178    0.178    0.179    0.179 <stdin>:1(loop)
        1    0.001    0.001    0.180    0.180 <string>:1(<module>)
        1    0.000    0.000    0.180    0.180 {built-in method builtins.exec}
     5000    0.001    0.000    0.001    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
```

There were 5004 calls.

- `ncals` number of calls
- `tottime` total time spent in the given function
- `percall` is `tottime` / `ncalls`
- `cumtime` cumulative time spent in this and all subfunctions
- `percall` is `cumtime` / primitive calls
- `filename:lineno(function)` respective data of each function


And [more](https://www.huyng.com/posts/python-performance-analysis)
