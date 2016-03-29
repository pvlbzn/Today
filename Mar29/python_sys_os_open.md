###Directory, os, sys, modules: Continued

####Open()

Difference between ```os.open()```, ```open()```, ```io.open()```:

```os.open()``` is intended for low-level I/O.

```io.open()``` is an alias for builtin ```open()```

```open()``` is a prefered way to deal with files. It opens file and return a corresponding [file object](https://docs.python.org/3/glossary.html#term-file-object) or raise OSError.

For regular file openings use the Context Managers:

```python
with open([filename]) as f:
	contents = f.read()
```

Invoking ```open``` in this fashion ensures that f's ```close``` method will be called at some point.

An example from [The Hitchhiker's Guide](http://docs.python-guide.org/en/latest/writing/structure/#modules):

```python
class CustomOpen(obj):
	def __init__(self, fname):
		self.f = open(fname)
	
	def __enter__(self):
		return self.f
	
	def __exit__(self, ctx_type, ctx_value, ctx_traceback):
		self.f.close()

# Use it
with CustomOpen([file]) as f:
	contents = f.read()
```


####sys.modules

Digging into [yesterday's](https://github.com/pvlbzn/Today/blob/master/Mar28/python_os_path.md) TODOL learn more about ```sys.modules```.

[Documentation](https://docs.python.org/3.5/library/sys.html#sys.modules) saying that this is a dictionary that maps module names to modules which have already been loaded.

```python
import sys

type(sys.modules)
>> <class 'dict'>

# Look at available methods
dir(dict)

# Print keys
sys.modules.keys()

sys.modules['posixpath]
>> <module 'posixpath' from '[path_to_python]/python3.5/posixpath.py'>

type(sys.modules['posixpath'])
>> <class 'module'>

```
