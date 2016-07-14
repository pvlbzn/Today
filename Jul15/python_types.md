## [PEP 484](https://www.python.org/dev/peps/pep-0484/)
Since 3.5 version Python has a types annotations.

```
def hello(name: str) -> str:
    return 'Hello ' + name

from typing import TypeVar, Iterable, Tuple

T = TypeVar('T', int, float, complex)

def in(v: Iterable[Tuple[T, T]]) -> T:
    return sum(x*y for x, y in v)
```

#### MyPy
MyPy is an optional static typing (checker) for Python. Main idea 
is to catch errors without running the code, well, type checking.

```
# Static typing is optional
def f():
    1 + 1

# Error. Statically typed.
def g() -> None:
    1 + 1
``` 

The `typing` module contains types definitions. Built in types is 
`int`, `float`, `bool`, `str`, `bytes`, `object`, `List[type]`, 
`Dict[type, type]`, `Iterable[type]`, `Sequence[type]`, `Any`.

#### Conclusion
The good part is types, static checking, and this "typing polymorphism" 
(use types or not is up to you). However it feels unnatural and weird 
to add types in function signatures but not in variable declarations.
From one point this stuf is legacy-friendly, from another - try to find 
out what the is this type!
