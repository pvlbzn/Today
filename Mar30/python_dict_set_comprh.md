###Dictionary, Set Comprehension
####Dictionary

It's like list comprehension, but it constructs a dict, not list.

Example from [diveintopython3](http://www.diveintopython3.net/comprehensions.html)

```
import os
import glob

# List comprehension
lmeta = [(f, os.stat(f)) for f in glob.glob('*.md')]

# Dictionary Comprehension
dmeta = {f:os.stat(f) for f in glob.glob('*.md')}
```

List comprehension will produce a list of tuples [(foo, bar), ... ]

Dict comprehension will produce a dict {'foo': bar, ... }

```
{'python_list_compr.md': os.stat_result(st_mode=33188, st_ino=16893289, st_dev=16777220, st_nlink=1, st_uid=501, st_gid=20, st_size=672, st_atime=1459271040, st_mtime=1459270973, st_ctime=1459270973), ... }
```


Awesome feature of the REPL tool `help(os.stat_result)`.

Also, cool trick with dict comprehension:

```
dict = {'a': 1, 'b': 2, 'c': 3}
{v: k for k, v in dict.items()}
>>{1: 'a', 2: 'b', 3: 'c'}
```

This works only with **immutable** values, like strings or tuples. 





####Set

Everything is similar, just remember about set behaviour.

```
s = set(range(15))
{n ** 2 for n in s}
# Set is unordered
>> {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

# And not indexed
s[0]
>> TypeError: 'set' object does not support indexing

# Data structures comprehension is just great
{n for n in s if n%2 == 0}
>> {0, 8, 2, 4, 6}
```

