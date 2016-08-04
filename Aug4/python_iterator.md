## Iterators
Files which can be used with `for ... in` construction are called iterable obejcts. The built-in function `iter` takes an iterable object and returns an iterator.

**Iterable** is a container which has the `__iter__()` method defined.
**Iterator** is an object that supports the **iterator protocol** which means that the following tho methods needs to be defined:
1. `__iter__`
2. `__next__`

```
i = iter([1, 2, 3])
next(i)
> 1
next(i)
> 2
next(i)
> 3
next(i)
> StopIteration
```

Iterator behavior can be added to classes. Define an `__iter__()` method which returns an object with a `__next__()` method. If the class defines `__next__()`, then `__iter__()` can return `self`

```
class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIretation
        self.index = self.index - 1
        return self.data[self.index]
```

## Generators
Generators are a simple and powerful tool for creating *iterators*. They are written like regular functions but use the `yield` statement whenever they want to return data.

```
def reverse(data):
    for index in range(len(data) - 1, -1, -1):
        yield data[index]

for char in reverse('gold'):
    print(char)

> d
> l
> o
> g
```

What makes generators so compact is that the `__iter__()` and `__next__()` methods are created automatically.


## `for`
The `for` loop under the hood first invokes the `__iter__()` method of the container to get the iterator of the container. Then it calls the `__next__()` method until `StopIteration` exception raised.
