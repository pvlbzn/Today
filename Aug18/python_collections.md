## Python Types
Every book or blog post on 'learn python' uses and describes built-ins `list`, `tuple`, `dict`, `set` but usually the `collections` module left without proper attention since most common tasks doesnt require `collections` functionality. For example I need a ordered dictionary, what to do? I can build a bicycle or use `collections.OrdereDict` and simplify logic, perhaps win some performance and, most importantly allow to a reader to understand what's goig on instantly.

### `collections`
The `collections` module includes container data types beyoond the built-ins.

```
dir(collections)

# Magic methods are omitted
['AsyncIterable', 'AsyncIterator', 'Awaitable',
 'ByteString', 'Callable', 'ChainMap', 'Container',
 'Coroutine', 'Counter', 'Generator', 'Hashable',
 'ItemsView', 'Iterable', 'Iterator', 'KeysView',
 'Mapping', 'MappingView', 'MutableMapping',
 'MutableSequence', 'MutableSet', 'OrderedDict',
 'Sequence', 'Set', 'Sized', 'UserDict', 'UserList',
 'UserString', 'ValuesView', 'abc', 'defaultdict',
 'deque', 'namedtuple']
```

*Why last classes are lowercase-named?*

### Other Data Types
The built-ins and the `collections` module is not only one source of data types. There are also `array`, `Queue`, `struct`, `weakref`.

Each of them I'll learn separately.

