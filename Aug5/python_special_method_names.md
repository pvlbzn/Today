## "magic" methods
Magic methods are everything in oopython. They are always surrounded by double underscore, like `__init__`.

For example call the `dir` method on some object, say `1`:
```
[print(x) for x in dir(1)]

__abs__
__add__
__and__
...
...
...
numerator
real
to_bytes
```

There are 69 methods, and 60 of them are *magic methods*.


### New Object
Well known `__init__` method isn't first one to be called on new object creation. A first one is `__new__` and the last method in object's life cycle is `__del__`.

`__new__(cls, args)` it is a first method to get called in an object's instantiation. It takes the class, then any other arguments that will be passed to `__init__`.

`__del__(self)` it is a destructor. Better dont use it unless you are sure that you have to.


### Custom Classes
Magic methods helps to make behavior of a custom objects to be like built-ins. 

#### Comparison
- `__eq__(self, other)` behavior for the `==` operator
- `__ne__(self, other)` behavior for the `!=` operator
- `__lt__(self, other)` behavior for the `<` operator
- `__gt__(self, other)` behavior for the `>` operator
- `__le__(self, other)` behavior for the `<=` operator
- `__ge__(self, other)` behavior for the `>=` operator

For example, if numbers must be compared by number of digits, not by their meaning:

```
class Number(int):
    def __new__(cls, number):
        return int.__new__(cls, number)

    def __eq__(self, other):
        return len(str(self)) == len(str(other))

n1 = Number(10)
n2 = Number(99)

n1 == n2
> True
```

#### Numeric

- `__pos__(self)` unary positive
- `__neg__(self)` unary negation
- `__abs__(self)` builtin `abs()` function
- `__invert__(self)` implements `~` operator
- `__round__(self, n)` implements `round()` where `n` is decimal place to round to
- `__floor__(self)` implements `math.floor()`
- `__ceil__(self)` implements `math.ceil()`
- `__trunc__(self)` implements `math.trunc()`

```
x = 15
x.__neg__()
> -15
```

#### Operations
- `__add__(self, other)` addition
- `__sub__(self, other)` subtraction
- `__mul__(self, other)` multiplication
- `__floordiv__(self, other)` implements integer division `//`
- `__div__(self, other)` division
- `__truediv__(self, other)` *true* division
- `__mod__(self, other)` modulo
- `__divmod__(self, other)` implements `divmod()`
- `__pow__(self, other)` implements `**`
- `__lshift__(self, other)` `<<`
- `__rshift__(self, other)` `>>`
- `__and__(self, other)` `&`
- `__or__(self, other)` `|`
- `__xor__(self, other)` `^`

#### Aughmented assignment
Same methods as in *Operations* but with `i` prefix: `__iadd__(self, other). It makes possible to perform `a = a + b` as `a += b`.

#### Type Conversion
- `__int__(self)` to int
- `__long__(self)` to long
- `__float__(self)` to float
- `__complex__(self)` to complex
- `__oct__(self)` to octal
- `__hex__(self)` to hex
- `__index__(self)` to an int when the obj is used in a slice expression
- `__trunc__(self)` `math.trunc(self)`
- `__coerce__(self, other)` mixed mode arithemtic
