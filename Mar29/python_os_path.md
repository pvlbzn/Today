###Directory, os, sys, modules

There is always a current working directory in Python.

The [os module](https://github.com/python/cpython/blob/master/Lib/os.py) source code. I guess source code can be useful in many ways, while you learn. It is a good place to look as use of the best practices, PEP8, docstring and idiomatic Python.

```python
import os

# Get current working directory, like pwd
os.getcws()

# Change directory
os.chdir([dir])

# Use dir()
dir(os)
dir(os.path)
```

The [os.path](https://docs.python.org/3.1/library/os.path.html#module-os.path) module implements some useful functions on pathnames. The ```.expanduser``` and ```.expandvars``` are implemented in [posixpath.py](https://github.com/python/cpython/blob/1fe0fd9feb6a4472a9a1b186502eb9c0b2366326/Lib/posixpath.py), thus, I guess, ```os.path``` should be used because it is OS independent realization.

```python
import os

os.path.expanduser("~/.vimrc")
# '/Users/pvlbzn/.vimrc'
```

Code from ```os.py```

```python
...

if 'posix' in _names:
    name = 'posix'
    linesep = '\n'
    from posix import *
    try:
        from posix import _exit
        __all__.append('_exit')
    except ImportError:
        pass
    import posixpath as path

...

sys.modules['os.path'] = path
from os.path import (curdir, pardir, sep, pathsep, defpath, extsep, altsep,
    devnull)

...
```

Looks like Python injects particular path realization, which depends on OS, at runtime?

TODO: learn more about ```sys.modules```. What is it, how it works.



