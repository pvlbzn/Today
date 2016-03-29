###List Comprehensions

Possible shortest explanation is:

```
l = [1, 2, 3, 4, 5]

[n * 2 for n in l]

>>[2, 4, 6, 8, 10]
```

Basicaly it is a `for` loop with an additional perk.

```
l = [1, 2, 3, 4, 5]
[print(i) for i in l]
>>1
>>2
>>3
>>4
>>5
>>[None, None, None, None]
# List compr creates a new list, it doesnt violate original one.
l
[1, 2, 3, 4, 5]
```

or

```
import os
import glob

glob.glob('*.md')
>>['python_glob_meta.md', 'python_sys_os_open.md']

[os.path.realpath(f) for f in glob.glob('.*md')]
>>['real/path/today/Mar29/python_glob_meta.md',
>> 'real/path/today/Mar29/python_sys_os_open.md']
```

Some kind of usefull example in 'files_bigger_than.py'.
