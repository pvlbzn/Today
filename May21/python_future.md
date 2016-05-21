### Fragmentation
Python fragmentation is a thing. There are a lot of things which were changed in version 3, and not all of them minor. Changes such as integer division or all strings unicode - they are huge in order to just migrate old code to a new version.

Consider two files: `py_2_future.py` and `py_2.py`. They both performs one operation on integer division:

```
$ python2.7 py_2_future.py
> 5 / 2 = 2.5

$ python2.7 py_2.py
> (5 / 2 = 2)
```

More on Python 3 changes [here](http://sebastianraschka.com/Articles/2014_python_2_3_key_diff.html).

### Sources

[`future.c`](https://github.com/python/cpython/blob/2d264235f6e066611b412f7c2e1603866e0f7f1b/Python/future.c), [`__future__.py`](https://github.com/python/cpython/blob/master/Lib/__future__.py).

```
all_feature_names = [
    "nested_scopes",
    "generators",
    "division",
    "absolute_import",
    "with_statement",
    "print_function",
    "unicode_literals",
    "barry_as_FLUFL",
    "generator_stop",
]
```

### Conclusion
It should be used like this:

```
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from builtins import (
         bytes, dict, int, list, object, range, str,
         ascii, chr, hex, input, next, oct, open,
         pow, round, super,
         filter, map, zip)
```

On python3 these statements will be ignored, on python2 they will shadow the corresponding builtins.