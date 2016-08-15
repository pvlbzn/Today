## Dependencies Management
Node Package Manager provides very convinient way to manage package by itself, but also package dependencies. Python has a `setuptools` library for this (kind of) purpose.

#### `setuptools`
From docs:

> Setuptools is a collection of enhancements to the Python distutils (for Python 2.6 and up) that allow developers to more easily build and distribute Python packages, especially ones that have dependencies on other packages.

```
from setuptools import setup, find_packages

setup(
    name = 'today_i_learned',
    version = '0.1',
    packages = find_packages(),
    install_requires=[
        'requests>=2.11.0'
    ]
)
```

Now, `python3 setup.py install` will install required dependencies and `./program.py` will return `200`.

