## Imports

Despite in many languages imports is intuitive or, at least, straighforward, in Python it is not the case.

Example has following structure:

```
.
├── module_1
│   └── foo.py
├── module_2
│   └── bar.py
└── python_imports.md
```

#### Module
Module is a separate file with python script. Definitions from a module can be imported into other modules. The file name is the module name. Withing the file name available as the value of the global variable `__name__`.

```
>>> __name__
'__main__'

>>> from module_1 import foo
>>> foo.__name__
'module_1.foo'
```

When a module `foo` is imported, the interpreter forst searches for a built-in module with that name. If not found, it then searches for a file named `foo.py` in a list of directories given by the variable `sys.path`.

`sys.path` is initialized from:
- Directory containing the input script (or the current directory when no file is specified)
- PYTHONPATH
- Installation-dependent default

#### Packages
Packages are a way of structuring Pythons modules. It is about namespacing. 

Consider a following tree:

```
.
├── module
│   ├── module_1
│   │   ├── __init__.py
│   │   └── foo.py
│   └── module_2
│       ├── __init__.py
│       └── bar.py
└── python_imports.md
```

If interpreter called from root (`.`) then to import the `foo`, import statement should be `from module.module_1 import foo`. In `foo`, which imports `bar`, import statement should be `from ..module_2 import bar
` which is logical. `.` means current dir, `..` one dir up in the dir tree. Indeed `module_2` in in one directory up from the `foo`.

If `foo` imported from the `module` directory, the import statement looks like `from module_1 import foo` because `module_1` is stored in the `module`. Import statement in the `foo`, to import the `bar`, is `from module_2 import bar` because of the previous reason.

