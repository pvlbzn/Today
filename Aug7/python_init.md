## Module, Package
Python has concept of modules and packages. **Module** is a python file. Definitions from a module can be imported into other modules. Module name can be found in `__name__` variable. **Package** are the way of structuring Python's module namespace.

## `__init__.py`
Init file usually used for package declaring. 

```
package
├── __init__.py
├── module1.py
├── module2.py
└── subpackage
    ├── __init__.py
    ├── submodule1.py
    └── submodule2.py
```

`__init__.py` usually is empty, but it can be used to perform some kind of package setup. For example selected Classes and functions can be loaded into the package level.

```
# with empty __init__.py
from package.module1 import SomeClass
``` 

But this import may be added into the package's `__init__.py` file

```
# __init__.py
from module1 import SomeClass
```

Now `SomeClass` is in the package level.

```
# instead of
from package.module1 import SomeClass

# import now can be performed as
from package import SomeClass
```

`__init__.py` executes when package is imported:

```
# __init__.py
print('hello')

# import package
import package_with_init
> 'hello'
```

The reason to use package level import is that it can serve as a public API. User can take a look into `__init__.py` and understand what classes or functions are *designed* to be used. There are no private classes, methods, fields in Python, because Python community assumes that *we are all adults here* and if you want to use kind of private API it is your business.
