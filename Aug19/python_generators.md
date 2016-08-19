## Yield

```
def counter(n):
    print('in counter')
    while True:
        yield n
        print('post incrementing n')
        n += 1

c = counter(5)
> in counter

next(c)
> 5

next(c)
> 6

next(c)
> 7
```

`yield` is a keyword that is used like `return` except the function will return a generator.

```
def create_generator():
    l = range(5)
    for i in l:
        yield i*i

# When you call the function the code you have written
# in the function body doesnt run. Function returns the
# generator object
gen = create_generator()

for i in gen:
    print(i)
```

#### Iterators & Generators
Iterator is an iterable thing like list which you can use in `for x in y` construction. Generators are iterators, but you can only iterate over them once. That is because generators do not store all the values in memory, **they generate the values on the fly**

```
gen = (x*x for x in range(5))
for i in gen:
    print(i)

> 0
> 1
> 4
> 9
> 16

for i in gen:
    print(i)

# nothing happened
```


