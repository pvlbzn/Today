## Decorator
A decorator is a function that takes another function and extends the bevahiour of the latter function without expliciltly modifying it.


```
# Load function
def fib(n=34):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

# Decorator function
def timing(fn):
    def wrapper():
        t1 = time.time()
        fn()
        t2 = time.time()
        return t2 - t1
    return wrapper

# Use without decorator
timing(fib)()

# Use with decorator
@timing
def function():
    fib()
```

Above code may be explained as: *take one code block and insert it into another one*. Now, timing decorator can be conviniently used.

```
@timing
def foo():
    s = ''
    for n in range(int(1e7)):
        s += str(n)

@timing
def bar():
    s = ''
    for n in range(int(1e7)):
        s.__add__(str(n))

@timing
def baz():
    s = []
    for n in range(int(1e7)):
        s.append(str(n))
    s = ''.join(s)
```

These function will output an amount of passed time.

```
a, b, c = foo(), bar(), baz()
a   # 4.791781902313232
b   # 4.668297052383423
c   # 5.3237128257751465
```
