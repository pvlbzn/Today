# Use of Special Methods
*Dunder*/*magic* methods are meant to be called by the Python interpreter. Programmer writes `len(obj)`, interpreter calls `obj.__len__()` if `obj` is a user defined method.

For a built-ins (list, str, etc) `len()` returns the value of the `PyVarObject.ob_size` field, which is a member of a C struct. This is done for a performance reasons.

Usually the special methods are invoked implicitly. `item in arr` actually calls `iter(arr)` which may call `arr.__iter__()`.

In general pythonistas should implement special methods more often than invoking them explicitly. Advantage of calling built-in function, like `len` instead of `obj.__len__()` is performance and a common sense.

## Magic Methods
There are 83 special methods.
!{'oo.py'}

#### `__repr__`
`__repr__` is called by the `repr` built-in. The REPL and debugger call `repr` which returns an object string representation. Result of the `__repr__` should, if possible, match the source code to recreate the object. E.g. `Vector(15, 28)` is a good representation, while `Vector x: 15, y: 28` isn't.

#### Operator Overloading
A new object on return is expected.

#### Boolean
Instances of user defined classes are considered to be *truthy* until `__bool__` or `__len__` is implemented. For example custom class `Score`

```
class Score(object):
    def __init__(self, score):
        self.score = score

# Instance of the Score with a negative score
s = Score(-15)

if s:
    print('s is truthy')

's is truthy'            # but it isn't
```
