###Glob, metadata

####Glob

The [`glob`](https://docs.python.org/3/library/glob.html?highlight=glob#module-glob) module finds all the pathnames matching a specified pattern according to the rules used by the Unix shell.

```python
import os
import glob

glob.glob('.py')
>>['how_many_x_in_y.py']

os.chdir(os.path.expanduser('~'))
glob.glob('.*rc')
>>['.bashrc', '.netrc', '.vimrc']
```

####Metadata

[`os.stat()`](https://docs.python.org/3/library/os.html?highlight=os.stat#os.stat) get the status of a file or a file descriptor, return a `stat_result` object.

_Note_: Symlink is a [symbolic link](https://en.wikipedia.org/wiki/Symbolic_link), special kind of file that points to another filem like an alias.

_Note_: Just to clarefy difference between relative path and absolute.

```
relative path: index.html
			   /some/path/img.png

absolute path: http://www.google.com
			   http://www.google.com/some/path/img.png
```

Metadata:

```python
import os
os.listdir()
>>['how_many_x_in_y.py', 'python_glob_path.md', 'python_sys_os_open.md']

meta = os.stat('how_many_x_in_y.py')
meta.st_mtime
>> 1459257927.0

meta.st_size
>> 858

import time
time.localtime(meta.st_mtime)
>>time.struct_time(tm_year=2016, tm_mon=3, tm_mday=29, tm_hour=16, tm_min=25, tm_sec=27, tm_wday=1, tm_yday=89, tm_isdst=0)
```




