# Python Data Model
Python Data Model can be understanded as a description of *Python as a framework*. If formalizes the interfaces of the building blocks of the language itself: sequences, iterators, functions, classes, context managers, etc. Python interpreter invokes special methods (magic methods) to perform basic object operations.

`object[key]` is supported by the `__getitem__` (pronounces as *dunder-getitem*) method. In order to evaluate `object[key]` the interpreter calls `object.__getitem__(key)`. This example shows why Python data model can be described as a framework.

*Dunder methods* allows custom objects behave like a first-class objects (built-ins):

- Iterations
- Collections
- Attribute access
- Operator overloading
- Function invocation
- Object creating/destruction
- String representations
- Managed context (`with`)


```
class Pool:
    '''
    Whatever pool
    '''

    def __init__(self, items):
        self._items = items

    def __len__(self):
        return self._items
```

Create a new `Pool` object `p = Pool(15)` and call a built-in function `len` - it will return `15`.
